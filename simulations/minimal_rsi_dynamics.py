#!/usr/bin/env python3
"""Minimal resource-normalized dynamics for model-harness RSI.

State variables
---------------
C : protected transferable capability
eta : transferable improvement per unit improvement resource
q : evaluator fidelity

The model is intentionally small enough to identify from experiments:

    dC/dr = eta

    deta/dr = [q * (a0 + a1*C/(K+C)) - (d0 + d1*C**p)]*eta
               - kappa*eta**2 + u_ext

    dq/dr = r_v*(1-q) - s_v*eta*q

Here r is cumulative improvement resource rather than wall-clock time.
"""

from __future__ import annotations

from dataclasses import dataclass
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

        d_capability = efficiency
        d_efficiency = (
            (recursive_gain - complexity_debt) * efficiency
            - params.kappa * efficiency**2
            + params.u_ext
        )
        d_fidelity = (
            params.r_v * (1.0 - fidelity)
            - params.s_v * efficiency * fidelity
        )
        return [d_capability, d_efficiency, d_fidelity]

    grid = np.linspace(0.0, resource_max, points)
    solution = solve_ivp(
        rhs,
        (0.0, resource_max),
        (1.0, 0.08, 0.90),
        t_eval=grid,
        rtol=1e-9,
        atol=1e-11,
    )
    if not solution.success:
        raise RuntimeError(solution.message)
    return solution.t, solution.y


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

    plt.figure(figsize=(9.4, 5.8))
    for name, (resource, state) in results.items():
        plt.plot(resource, state[0], label=name)
    plt.xlabel("Cumulative improvement resource")
    plt.ylabel("Protected transferable capability C")
    plt.title("Minimal RSI dynamics: capability")
    plt.yscale("log")
    plt.grid(True, alpha=0.25)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output / "capability.png", dpi=180)
    plt.close()

    plt.figure(figsize=(9.4, 5.8))
    for name, (resource, state) in results.items():
        plt.plot(resource, state[1], label=name)
    plt.xlabel("Cumulative improvement resource")
    plt.ylabel("Improvement efficiency eta")
    plt.title("Minimal RSI dynamics: improvement efficiency")
    plt.grid(True, alpha=0.25)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output / "efficiency.png", dpi=180)
    plt.close()

    for name, (_, state) in results.items():
        print(
            f"{name:22s} "
            f"C={state[0, -1]:9.3f} "
            f"eta={state[1, -1]:7.3f} "
            f"q={state[2, -1]:6.3f} "
            f"max_eta={state[1].max():7.3f}"
        )


if __name__ == "__main__":
    main()
