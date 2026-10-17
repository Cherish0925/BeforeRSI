#!/usr/bin/env python3
"""Illustrative resource-normalized dynamics for model-harness RSI.

Nothing in this file is an empirical forecast. The parameter sets are synthetic
and exist to expose qualitative regimes and define quantities that future
experiments should estimate.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


@dataclass(frozen=True)
class Parameters:
    a0: float
    a1: float
    K: float
    d0: float
    d1: float
    p: float
    kappa: float
    u_ext: float
    r_v: float
    s_v: float


def simulate(
    params: Parameters,
    resource_max: float = 80.0,
    points: int = 1200,
) -> tuple[np.ndarray, np.ndarray]:
    def rhs(_: float, state: np.ndarray) -> list[float]:
        capability, efficiency, fidelity = state
        recursive_gain = (
            params.a0
            + params.a1 * capability / (params.K + capability)
        ) * fidelity
        complexity_debt = params.d0 + params.d1 * capability**params.p

        return [
            efficiency,
            (
                (recursive_gain - complexity_debt) * efficiency
                - params.kappa * efficiency**2
                + params.u_ext
            ),
            params.r_v * (1.0 - fidelity)
            - params.s_v * efficiency * fidelity,
        ]

    grid = np.linspace(0.0, resource_max, points)
    sol = solve_ivp(
        rhs,
        (0.0, resource_max),
        (1.0, 0.08, 0.90),
        t_eval=grid,
        rtol=1e-9,
        atol=1e-11,
    )
    if not sol.success:
        raise RuntimeError(sol.message)
    return sol.t, sol.y


def capability_from_elasticity(
    resource: np.ndarray,
    epsilon: float,
    a: float = 0.2,
    c0: float = 1.0,
) -> np.ndarray:
    if np.isclose(epsilon, 1.0):
        return c0 * np.exp(a * resource)
    base = c0 ** (1.0 - epsilon) + (1.0 - epsilon) * a * resource
    return np.maximum(base, 1e-12) ** (1.0 / (1.0 - epsilon))


def search_efficiency(
    candidate_count: np.ndarray,
    rho: float,
    mu_g: float = 0.02,
    sigma_g: float = 0.10,
    c0: float = 0.20,
    per_candidate_cost: float = 0.015,
) -> np.ndarray:
    n = candidate_count.astype(float)
    expected_true_gain = mu_g + rho * sigma_g * np.sqrt(2.0 * np.log(n))
    return expected_true_gain / (c0 + per_candidate_cost * n)


def save_line_plot(
    path: Path,
    x: np.ndarray,
    series: dict[str, np.ndarray],
    xlabel: str,
    ylabel: str,
    title: str,
    log_y: bool = False,
) -> None:
    plt.figure(figsize=(9.4, 5.8))
    for name, y in series.items():
        plt.plot(x, y, label=name)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    if log_y:
        plt.yscale("log")
    plt.grid(True, alpha=0.25)
    plt.legend()
    plt.tight_layout()
    plt.savefig(path, dpi=180)
    plt.close()


def main() -> None:
    regimes = {
        "Saturation": Parameters(
            0.02, 0.12, 10.0, 0.08, 0.025, 0.8,
            0.50, 0.002, 0.04, 0.02,
        ),
        "Steady improvement": Parameters(
            0.07, 0.18, 10.0, 0.06, 0.002, 0.5,
            0.35, 0.004, 0.08, 0.02,
        ),
        "Recursive acceleration": Parameters(
            0.09, 0.55, 8.0, 0.04, 0.0004, 0.4,
            0.18, 0.004, 0.18, 0.005,
        ),
        "Verifier-limited": Parameters(
            0.09, 0.55, 8.0, 0.04, 0.0004, 0.4,
            0.18, 0.004, 0.02, 0.12,
        ),
    }

    results = {name: simulate(params) for name, params in regimes.items()}
    output = Path(__file__).resolve().parent / "output"
    output.mkdir(parents=True, exist_ok=True)

    resource = next(iter(results.values()))[0]
    save_line_plot(
        output / "capability.png",
        resource,
        {name: state[0] for name, (_, state) in results.items()},
        "Cumulative improvement resource",
        "Protected transferable capability C",
        "Coupled RSI dynamics: capability",
        log_y=True,
    )
    save_line_plot(
        output / "efficiency.png",
        resource,
        {name: state[1] for name, (_, state) in results.items()},
        "Cumulative improvement resource",
        "Improvement efficiency eta",
        "Coupled RSI dynamics: improvement efficiency",
    )
    save_line_plot(
        output / "evaluator_fidelity.png",
        resource,
        {name: state[2] for name, (_, state) in results.items()},
        "Cumulative improvement resource",
        "Evaluator fidelity q",
        "Coupled RSI dynamics: evaluator fidelity",
    )

    r_elasticity = np.linspace(0.0, 10.0, 500)
    elasticities = [-0.5, 0.0, 0.5, 1.0]
    save_line_plot(
        output / "recursive_elasticity.png",
        r_elasticity,
        {
            f"epsilon={eps:g}": capability_from_elasticity(r_elasticity, eps)
            for eps in elasticities
        },
        "Cumulative improvement resource",
        "Normalized capability C",
        "Capability growth under recursive elasticity",
    )

    candidate_count = np.array([1, 2, 4, 8, 16, 32, 64, 128])
    save_line_plot(
        output / "search_efficiency.png",
        candidate_count,
        {
            "rho=0.9": search_efficiency(candidate_count, 0.9),
            "rho=0.7": search_efficiency(candidate_count, 0.7),
            "rho=0.3": search_efficiency(candidate_count, 0.3),
        },
        "Candidate count",
        "Expected true gain per improvement cost",
        "Search size and evaluator fidelity",
    )

    summary: dict[str, object] = {
        "disclaimer": "Synthetic parameter study; not an empirical forecast.",
        "regimes": {},
        "elasticity": {"a": 0.2, "C0": 1.0, "epsilons": elasticities},
        "search": {
            "candidate_count": candidate_count.tolist(),
            "rhos": [0.9, 0.7, 0.3],
            "mu_g": 0.02,
            "sigma_g": 0.10,
            "base_cost": 0.20,
            "per_candidate_cost": 0.015,
        },
    }

    for name, params in regimes.items():
        _, state = results[name]
        summary["regimes"][name] = {
            "parameters": asdict(params),
            "final": {
                "C": float(state[0, -1]),
                "eta": float(state[1, -1]),
                "q": float(state[2, -1]),
                "max_eta": float(state[1].max()),
            },
        }

    (output / "summary.json").write_text(
        json.dumps(summary, indent=2) + "\n",
        encoding="utf-8",
    )

    for name, data in summary["regimes"].items():
        final = data["final"]
        print(
            f"{name:22s} "
            f"C={final['C']:9.3f} "
            f"eta={final['eta']:7.3f} "
            f"q={final['q']:6.3f} "
            f"max_eta={final['max_eta']:7.3f}"
        )


if __name__ == "__main__":
    main()
