#!/usr/bin/env python3
"""Execute feedback-localization identification; compare with exact laws."""
import hashlib
import gzip
import json
import math
from pathlib import Path
import platform
import time
import numpy as np

ROOT = Path(__file__).resolve().parent
SEED, M, REPEATS = 2026101807, 4, 2000
DIMS, BUDGETS = (2, 4, 8, 16), (4, 8, 16, 32, 64)


def oracle(candidate, target):
    mismatches = np.flatnonzero(candidate != target)
    return None if not len(mismatches) else int(mismatches[0])


def decode(value, d):
    return np.array([(value // (M ** j)) % M for j in range(d)], dtype=int)


def local_count(target):
    candidate = np.zeros(len(target), dtype=int)
    queries = 0
    while True:
        queries += 1
        failed = oracle(candidate, target)
        if failed is None:
            return queries
        candidate[failed] += 1
        assert candidate[failed] < M


def scalar_count(target, rng, budget):
    seen, n = set(), M ** len(target)
    for q in range(1, min(budget, n) + 1):
        while True:
            value = int(rng.integers(n))
            if value not in seen:
                seen.add(value)
                break
        # Feedback intentionally exposes only the whole-candidate truth bit.
        passed = oracle(decode(value, len(target)), target) is None
        if passed:
            return q
    return None


def exact_local_cdf(d, budget):
    counts = np.array([1], dtype=object)
    for _ in range(d):
        counts = np.convolve(counts, np.ones(M, dtype=object))
    return sum(counts[:max(0, budget)]) / M ** d


def main():
    begin = time.perf_counter()
    records, summary, checks = [], [], 0
    for d in DIMS:
        rng = np.random.default_rng(np.random.SeedSequence([SEED, d]))
        targets = rng.integers(M, size=(REPEATS, d))
        group = []
        for i, target in enumerate(targets):
            local = local_count(target)
            scalar = scalar_count(target, rng, max(BUDGETS))
            assert local == 1 + int(target.sum())
            assert local <= 1 + d * (M - 1)
            checks += d * (local + (scalar if scalar is not None else min(max(BUDGETS), M**d)))
            row = {"d":d,"instance":i,"target":target.tolist(),
                   "local_queries":local,"scalar_first_success":scalar}
            records.append(row); group.append(row)
        for budget in BUDGETS:
            summary.append({"d":d,"m":M,"budget_queries":budget,
                "budget_checks":budget*d,
                "scalar_predicted":min(budget/M**d,1),
                "scalar_observed":sum(r["scalar_first_success"] is not None and
                    r["scalar_first_success"]<=budget for r in group)/REPEATS,
                "local_predicted":float(exact_local_cdf(d,budget)),
                "local_observed":sum(r["local_queries"]<=budget for r in group)/REPEATS})
    # Exact Bayes projection: H~Bernoulli(1/2), A=H; Z is H or constant.
    witnesses={"teacher_accuracy":1.0,"student_with_bit":1.0,
        "student_without_bit":0.5,"minimum_projection_KL_nats":math.log(2),
        "source_task_mass":[0.5,0.5],"task_success_rates":[0.9,0.1],
        "pooled_accepted_task_mass":[0.9,0.1],
        "interpretation":"exact finite constructions, not neural training results"}
    (ROOT/"records.json").write_text(json.dumps(records,separators=(",",":"))+"\n")
    (ROOT/"records.json.gz").write_bytes(gzip.compress((ROOT/"records.json").read_bytes(),mtime=0))
    (ROOT/"summary.json").write_text(json.dumps({"comparisons":summary,
        "witnesses":witnesses,"primitive_checks":checks},indent=2)+"\n")
    manifest={"seed":SEED,"repeats":REPEATS,"dimensions":DIMS,"choices":M,
        "budgets":BUDGETS,"python":platform.python_version(),"numpy":np.__version__,
        "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "protocol_sha256":hashlib.sha256((ROOT/"PROTOCOL.md").read_bytes()).hexdigest(),
        "records_sha256":hashlib.sha256((ROOT/"records.json").read_bytes()).hexdigest(),
        "archive_sha256":hashlib.sha256((ROOT/"records.json.gz").read_bytes()).hexdigest(),
        "elapsed_seconds":time.perf_counter()-begin,"primitive_checks":checks}
    (ROOT/"manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")
    lines=["# Executed feedback-structure results", "",
        "A finite identification experiment, not an LLM reproduction. All strategies",
        "receive the same hidden specifications and pay d checks per query.","",
        "| Dimensions | Queries | Scalar: predicted / observed | Local: predicted / observed |",
        "|---:|---:|---:|---:|"]
    for r in summary:
        lines.append(f"| {r['d']} | {r['budget_queries']} | {r['scalar_predicted']:.6f} / {r['scalar_observed']:.4f} | {r['local_predicted']:.6f} / {r['local_observed']:.4f} |")
    lines += ["",f"Executed {checks:,} primitive checks across {REPEATS:,} specifications per dimension.",
        "No parameters were fitted. Every local trajectory exactly obeyed the predicted",
        "query-count identity; scalar outcomes are finite-sample realizations of its law.","",
        "The result establishes a possible exponential-versus-linear query gap when",
        "correct local decisions compose and feedback identifies the failing component.",
        "It does not establish that any LLM trace has this structure. Removing localization",
        "returns the equality-oracle lower bound even though final correctness stays exact.","",
        "The exact inheritance witness has a perfect teacher but only 50% optimal student",
        "accuracy when the decisive input bit is removed; restoring it gives 100%.",
        "Global success filtering also changes an equally weighted easy/hard task mixture",
        "to 90%/10% when their success probabilities are 0.9/0.1.","",
        "See PROTOCOL.md and summary.json for definitions and reproduction. Full records",
        "are preserved in records.json.gz; decompress it to inspect records.json."]
    (ROOT/"RESULTS.md").write_text("\n".join(lines)+"\n")
    print(json.dumps({"primitive_checks":checks,"elapsed_seconds":manifest["elapsed_seconds"],
        "selected":[r for r in summary if r["budget_queries"]==32]}))


if __name__ == "__main__":
    main()
