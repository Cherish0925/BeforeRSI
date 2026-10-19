#!/usr/bin/env python3
"""Execute a bounded self-optimizing numerical optimizer experiment.

No LLM, fitted growth equation, or invented improvement data is used.
Only NumPy and Python are required. All task scores come from objective calls.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import platform
import time

import numpy as np

TRAIN_FAMILIES = ("sphere", "ellipsoid", "rosenbrock")
OOD_FAMILIES = ("rotated_ellipsoid", "rastrigin", "ackley")
BASE = np.array([-0.2, -0.35, 0.15, -0.6, 0.6, -0.6])
COUNTS = {"objective_calls": 0, "meta_evaluations": 0}


def seed(*parts: int) -> int:
    return int(np.random.SeedSequence(parts).generate_state(1)[0])


@dataclass
class Task:
    family: str
    center: np.ndarray
    rotation: np.ndarray
    weights: np.ndarray
    search_seed: int

    def __call__(self, x):
        COUNTS["objective_calls"] += 1
        z = 4.0 * (np.asarray(x) - self.center)
        if self.family == "sphere":
            return float(z @ z)
        if self.family == "ellipsoid":
            return float((self.weights * z) @ z)
        if self.family == "rotated_ellipsoid":
            y = self.rotation @ z
            return float((self.weights * y) @ y)
        if self.family == "rosenbrock":
            y = z + 1.0
            return float(np.sum(100.0 * (y[1:] - y[:-1] ** 2) ** 2
                                + (1.0 - y[:-1]) ** 2))
        if self.family == "rastrigin":
            return float(np.sum(z*z + 10.0 * (1.0 - np.cos(2.0*np.pi*z))))
        if self.family == "ackley":
            return float(-20.0*np.exp(-0.2*np.sqrt(np.mean(z*z)))
                         - np.exp(np.mean(np.cos(2.0*np.pi*z))) + 20.0 + math.e)
        raise ValueError(self.family)


def tasks(families, count_each, dimension, task_seed):
    rng = np.random.default_rng(task_seed)
    result = []
    for family in families:
        for _ in range(count_each):
            q, _ = np.linalg.qr(rng.normal(size=(dimension, dimension)))
            weights = np.geomspace(1.0, float(rng.uniform(20.0, 100.0)), dimension)
            result.append(Task(family, rng.uniform(-0.45, 0.45, dimension),
                               q, weights, int(rng.integers(1, 2**31))))
    return result


def optimize(objective, start, actor, budget, search_seed, log=None):
    """The same algorithm acts on numeric tasks and on its own 6-D configuration.

    M = three coefficients predicting log mutation scale from time/success.
    H = coordinate/global mutation, antithetic pairing, periodic restart.
    H is decoded by signs of the final three configuration coordinates.
    Each iteration consumes exactly one objective call, including the incumbent.
    """
    rng = np.random.default_rng(search_seed)
    best = np.asarray(start, dtype=float).copy()
    value = float(objective(best))
    initial = value
    if log is not None:
        log.append({"candidate": best.tolist(), "loss": value})
    recent = 0.2
    pending = None
    for t in range(1, budget):
        # Coefficients are bounded by configuration space [-1,1]^6.
        log_scale = -1.8 + 1.7*actor[0] + 3.0*actor[1]*(t/budget)
        log_scale += 2.0*actor[2]*(recent - 0.2)
        scale = math.exp(max(-7.0, min(0.5, float(log_scale))))
        if actor[5] > 0 and t % 8 == 0:
            proposed = rng.uniform(-1.0, 1.0, best.size)
            pending = None
        elif actor[4] > 0 and pending is not None:
            proposed = pending
            pending = None
        else:
            if actor[3] > 0:
                delta = np.zeros(best.size)
                delta[int(rng.integers(best.size))] = rng.normal()*scale*math.sqrt(best.size)
            else:
                delta = rng.normal(size=best.size)*scale
            proposed = best + delta
            if actor[4] > 0:
                pending = best - delta  # pair about the same original center
        proposed = np.clip(proposed, -1.0, 1.0)
        trial = float(objective(proposed))
        improved = trial < value
        if improved:
            best, value = proposed.copy(), trial
        recent = 0.85*recent + 0.15*float(improved)
        if log is not None:
            log.append({"candidate": proposed.tolist(), "loss": trial})
    return best, value, initial


def score(config, cohort, budget):
    result = []
    for task in cohort:
        _, final, initial = optimize(task, np.zeros(task.center.size), config,
                                     budget, task.search_seed)
        # Score is a fractional reduction relative to the zero-vector start.
        # All comparisons use identical tasks and random streams.
        result.append(float(1.0 - final/max(initial, 1e-15)))
    return np.asarray(result)


def improve(target, actor, feedback, cfg, search_seed, mode="policy", audit=False):
    trace = [] if audit else None

    def loss(candidate):
        COUNTS["meta_evaluations"] += 1
        return float(1.0 - score(candidate, feedback, cfg["task_budget"]).mean())

    if mode == "policy":
        child, final, initial = optimize(loss, target, actor, cfg["meta_budget"],
                                         search_seed, trace)
    else:
        rng = np.random.default_rng(search_seed)
        child = target.copy()
        initial = final = loss(child)
        if trace is not None:
            trace.append({"candidate": child.tolist(), "loss": final})
        for k in range(1, cfg["meta_budget"]):
            if mode == "random":
                candidate = rng.uniform(-1.0, 1.0, target.size)
            elif mode == "pattern":
                candidate = child.copy()
                cycle, direction = divmod(k-1, 2*target.size)
                coordinate, sign = divmod(direction, 2)
                candidate[coordinate] += (1 if sign == 0 else -1)*0.5/(cycle+1)
                candidate = np.clip(candidate, -1.0, 1.0)
            else:
                raise ValueError(mode)
            value = loss(candidate)
            if value < final:
                child, final = candidate.copy(), value
            if trace is not None:
                trace.append({"candidate": candidate.tolist(), "loss": value})
    assert final <= initial + 1e-12
    if trace is not None:
        assert len(trace) == cfg["meta_budget"]
    return child, {"initial_loss": initial, "selected_loss": final,
                   "search_seed": search_seed, "candidates": trace}


def interval(values, bootstrap_seed=7341):
    """Paired bootstrap over independent training lineages, not task rows."""
    x = np.asarray(values, dtype=float)
    rng = np.random.default_rng(bootstrap_seed)
    means = x[rng.integers(0, len(x), size=(5000, len(x)))].mean(axis=1)
    return {"mean": float(x.mean()),
            "bootstrap_95": np.quantile(means, [0.025, 0.975]).tolist(),
            "lineages": len(x), "per_lineage": x.tolist()}


def run(cfg, out):
    started = time.monotonic()
    out.mkdir(parents=True, exist_ok=True)
    source = Path(__file__).read_bytes()
    manifest = {"config": cfg, "source_sha256": hashlib.sha256(source).hexdigest(),
                "python": platform.python_version(), "numpy": np.__version__,
                "started_utc": datetime.now(timezone.utc).isoformat(),
                "base_config": BASE.tolist(),
                "train_families": TRAIN_FAMILIES, "ood_families": OOD_FAMILIES,
                "interpretation": "bounded numerical benchmark; not an LLM experiment"}
    (out/"manifest.json").write_text(json.dumps(manifest, indent=2)+"\n")
    histories = []
    development = []
    modes = ("recursive", "frozen", "random", "pattern")
    # Complete every development lineage before accessing final task cohorts.
    for lineage in range(cfg["lineages"]):
        paths = {mode: [BASE.copy()] for mode in modes}
        for generation in range(1, cfg["generations"]+1):
            feedback_seed = seed(cfg["seed"], 10, lineage, generation)
            feedback = tasks(TRAIN_FAMILIES, cfg["feedback_each"], cfg["dimension"],
                             feedback_seed)
            for mode in modes:
                target = paths[mode][-1]
                actor = target if mode == "recursive" else BASE
                child, audit = improve(
                    target, actor, feedback, cfg,
                    seed(cfg["seed"], 11, lineage, generation),
                    mode=mode if mode in ("random", "pattern") else "policy",
                    audit=True)
                paths[mode].append(child)
                development.append({"lineage": lineage, "generation": generation,
                                    "mode": mode, "feedback_seed": feedback_seed,
                                    "actor": actor.tolist(), "target": target.tolist(),
                                    "child": child.tolist(), **audit})
        histories.append(paths)
        print(json.dumps({"stage": "development", "lineage": lineage+1}), flush=True)
    (out/"development.json").write_text(json.dumps(development, separators=(",", ":"))+"\n")
    snapshots = [{k: [v.tolist() for v in vs] for k, vs in paths.items()}
                 for paths in histories]
    (out/"snapshots.json").write_text(json.dumps(snapshots, indent=2)+"\n")
    frozen_digest = hashlib.sha256((out/"snapshots.json").read_bytes()).hexdigest()

    performance, common, lookahead, crosses = [], [], [], []
    for lineage, paths in enumerate(histories):
        cohorts = {
            "id": tasks(TRAIN_FAMILIES, cfg["assessment_each"], cfg["dimension"],
                        seed(cfg["seed"], 20, lineage)),
            "ood": tasks(OOD_FAMILIES, cfg["assessment_each"], cfg["dimension"],
                         seed(cfg["seed"], 21, lineage)),
        }
        for mode, configs in paths.items():
            for generation, config in enumerate(configs):
                for cohort_name, cohort in cohorts.items():
                    scores = score(config, cohort, cfg["task_budget"])
                    performance.append({"lineage": lineage, "mode": mode,
                                        "generation": generation, "cohort": cohort_name,
                                        "scores": scores.tolist(), "mean": float(scores.mean())})
        last = paths["recursive"][-1]
        for mi in (0, 1):
            for hi in (0, 1):
                crossed = np.r_[(BASE, last)[mi][:3], (BASE, last)[hi][3:]]
                for cohort_name, cohort in cohorts.items():
                    vals = score(crossed, cohort, cfg["task_budget"])
                    crosses.append({"lineage": lineage, "m": mi, "h": hi,
                                    "cohort": cohort_name, "mean": float(vals.mean()),
                                    "scores": vals.tolist()})
        for problem in range(cfg["common_problems"]):
            rng = np.random.default_rng(seed(cfg["seed"], 30, lineage, problem))
            target = np.clip(BASE + rng.normal(0, 0.45, 6), -1, 1)
            feedback_seed = seed(cfg["seed"], 31, lineage, problem)
            feedback = tasks(TRAIN_FAMILIES, cfg["feedback_each"], cfg["dimension"],
                             feedback_seed)
            tests = {
                "id": tasks(TRAIN_FAMILIES, cfg["assessment_each"], cfg["dimension"],
                            seed(cfg["seed"], 32, lineage, problem)),
                "ood": tasks(OOD_FAMILIES, cfg["assessment_each"], cfg["dimension"],
                             seed(cfg["seed"], 33, lineage, problem)),
            }
            baseline = {name: score(target, ts, cfg["task_budget"]) for name, ts in tests.items()}
            for generation, actor in enumerate(paths["recursive"]):
                child, audit = improve(target, actor, feedback, cfg,
                                       seed(cfg["seed"], 34, lineage, problem), audit=True)
                for cohort_name, cohort in tests.items():
                    gains = score(child, cohort, cfg["task_budget"]) - baseline[cohort_name]
                    common.append({"lineage": lineage, "problem": problem,
                                   "generation": generation, "cohort": cohort_name,
                                   "target": target.tolist(), "child": child.tolist(),
                                   "gains": gains.tolist(), "mean": float(gains.mean()),
                                   "feedback_seed": feedback_seed,
                                   "candidate_trace": audit["candidates"]})

            # Two-step branch test: change first actor; both continuations use BASE.
            branch_target = paths["recursive"][cfg["generations"]//2]
            next_feedback = tasks(TRAIN_FAMILIES, cfg["feedback_each"], cfg["dimension"],
                                  seed(cfg["seed"], 35, lineage, problem))
            for name, actor in (("ancestor", BASE), ("successor", last)):
                first, _ = improve(branch_target, actor, feedback, cfg,
                                   seed(cfg["seed"], 36, lineage, problem))
                second, _ = improve(first, BASE, next_feedback, cfg,
                                    seed(cfg["seed"], 37, lineage, problem))
                for cohort_name, cohort in tests.items():
                    for horizon, child in ((1, first), (2, second)):
                        vals = score(child, cohort, cfg["task_budget"])
                        lookahead.append({"lineage": lineage, "problem": problem,
                                          "actor": name, "horizon": horizon,
                                          "cohort": cohort_name,
                                          "child": child.tolist(),
                                          "mean": float(vals.mean()), "scores": vals.tolist()})
        print(json.dumps({"stage": "assessment", "lineage": lineage+1}), flush=True)

    assert hashlib.sha256((out/"snapshots.json").read_bytes()).hexdigest() == frozen_digest
    summary = {"performance": {}, "common_target_actor_advantage": {},
               "two_step_branch_advantage": {}, "cross_interaction": {}}
    for cohort in ("id", "ood"):
        for mode in modes:
            values = []
            for line in range(cfg["lineages"]):
                rows = [r for r in performance if r["lineage"] == line and
                        r["cohort"] == cohort and r["mode"] == mode]
                values.append(next(r["mean"] for r in rows if r["generation"] == cfg["generations"])
                              - next(r["mean"] for r in rows if r["generation"] == 0))
            summary["performance"][mode+"_"+cohort] = interval(values)
        recursive_minus_frozen = []
        for line in range(cfg["lineages"]):
            rows = [r for r in performance if r["lineage"] == line and
                    r["cohort"] == cohort and r["generation"] == cfg["generations"]]
            recursive_minus_frozen.append(next(r["mean"] for r in rows if r["mode"]=="recursive")
                                          - next(r["mean"] for r in rows if r["mode"]=="frozen"))
        summary["performance"]["recursive_minus_frozen_"+cohort] = interval(recursive_minus_frozen)
        for generation in range(cfg["generations"]+1):
            effects = []
            for line in range(cfg["lineages"]):
                rows = [r for r in common if r["lineage"]==line and r["cohort"]==cohort]
                effects.append(np.mean([r["mean"] for r in rows if r["generation"]==generation])
                               - np.mean([r["mean"] for r in rows if r["generation"]==0]))
            summary["common_target_actor_advantage"][f"{cohort}_generation_{generation}"] = interval(effects)
        for horizon in (1, 2):
            effects = []
            for line in range(cfg["lineages"]):
                rows = [r for r in lookahead if r["lineage"]==line and
                        r["cohort"]==cohort and r["horizon"]==horizon]
                effects.append(np.mean([r["mean"] for r in rows if r["actor"]=="successor"])
                               - np.mean([r["mean"] for r in rows if r["actor"]=="ancestor"]))
            summary["two_step_branch_advantage"][f"{cohort}_horizon_{horizon}"] = interval(effects)
        interactions = []
        for line in range(cfg["lineages"]):
            cells = {(r["m"],r["h"]):r["mean"] for r in crosses
                     if r["lineage"]==line and r["cohort"]==cohort}
            interactions.append(cells[1,1]-cells[1,0]-cells[0,1]+cells[0,0])
        summary["cross_interaction"][cohort] = interval(interactions)
    raw = {"performance":performance, "common":common, "lookahead":lookahead, "crosses":crosses}
    (out/"assessment.json").write_text(json.dumps(raw,separators=(",", ":"))+"\n")
    summary["accounting"] = {**COUNTS, "elapsed_seconds":time.monotonic()-started,
                             "snapshot_sha256":frozen_digest}
    (out/"summary.json").write_text(json.dumps(summary,indent=2)+"\n")
    print(json.dumps({"finished":True,"accounting":summary["accounting"],
                      "recursive_minus_frozen_id":summary["performance"]["recursive_minus_frozen_id"],
                      "final_actor_advantage_id":summary["common_target_actor_advantage"][
                          f"id_generation_{cfg['generations']}"]}),flush=True)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--lineages", type=int, default=8)
    p.add_argument("--generations", type=int, default=4)
    p.add_argument("--common-problems", type=int, default=4)
    p.add_argument("--seed", type=int, default=20261018)
    a = p.parse_args()
    config = {"lineages":a.lineages,"generations":a.generations,
              "common_problems":a.common_problems,"seed":a.seed,
              "task_budget":32,"meta_budget":17,"dimension":6,
              "feedback_each":2,"assessment_each":4}
    run(config,a.output)
