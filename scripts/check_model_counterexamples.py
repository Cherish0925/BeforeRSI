#!/usr/bin/env python3
"""Finite witnesses for THEORY.md; no empirical AI results are simulated."""
from fractions import Fraction as F
import json
import math


def main():
    # Same deterministic process x'=x, same score J=x, new coordinate y=log x.
    coordinate = []
    for x in (0.25, 1.0, 2.0, 8.0):
        y = math.log(x)
        recursion_x = 1.0 * 1.0 * x
        curvature_x = 0.0
        recursion_y = math.exp(y) * 0.0 * 1.0
        curvature_y = math.exp(y) * 1.0 ** 2
        assert recursion_x > 0 and recursion_y == 0
        assert math.isclose(recursion_x + curvature_x, recursion_y + curvature_y)
        coordinate.append({"x": x, "term_in_x": recursion_x, "term_in_y": recursion_y})

    # Positive net coefficient does not ensure rising path slope.
    eta, net, kappa, external = F(2), F(1), F(1), F(0)
    slope = net * eta - kappa * eta ** 2 + external
    assert net > 0 and slope == -2

    # Separate gain/debt cannot be recovered from their difference.
    g, d, shift = F(3, 2), F(1, 2), F(7)
    assert g - d == (g + shift) - (d + shift)

    # Both component changes are harmless but interact negatively.
    j00, j10, j01, j11 = 50, 60, 60, 60
    assert j10 >= j00 and j01 >= j00 and j11 >= max(j10, j01)
    gamma_redundant = j11 - j10 - j01 + j00
    assert gamma_redundant == -10
    # Positive interaction can coexist with degraded cross-pairs.
    j00, j10, j01, j11 = 50, 40, 40, 80
    gamma_incompatible = j11 - j10 - j01 + j00
    assert gamma_incompatible == 50 and j10 < j00 and j01 < j00

    # Better improver: captures a larger fraction of a target's remaining room.
    gain = lambda quality, target: quality * (1 - target)
    parent_quality, child_quality = F(1, 2), F(4, 5)
    parent_target, child_target, common_target = F(1, 5), F(9, 10), F(1, 2)
    own_parent = gain(parent_quality, parent_target)
    own_child = gain(child_quality, child_target)
    common_delta = gain(child_quality, common_target) - gain(parent_quality, common_target)
    assert own_child < own_parent and common_delta == F(3, 20)

    # Exact failure of a Markov summary: phi(a)=phi(b), distinct next laws.
    phi = {"a": 0, "b": 0, "c": 1, "d": -1}
    transition = {"a": {"c": F(1)}, "b": {"d": F(1)},
                  "c": {"c": F(1)}, "d": {"d": F(1)}}
    def summary_law(x):
        law = {}
        for nxt, prob in transition[x].items():
            law[phi[nxt]] = law.get(phi[nxt], F(0)) + prob
        return law
    law_a, law_b = summary_law("a"), summary_law("b")
    assert phi["a"] == phi["b"] and law_a != law_b
    states = set(law_a) | set(law_b)
    tv = sum(abs(law_a.get(z, 0) - law_b.get(z, 0)) for z in states) / 2
    assert tv == 1

    # A task distribution can concentrate on a regression.
    task_gains = [F(1, 10), F(-1, 5)]
    average_gain = F(9, 10) * task_gains[0] + F(1, 10) * task_gains[1]
    assert average_gain > 0 and task_gains[1] < 0

    # Same observed controlled dynamics, opposite unobserved reuse effects.
    # States encode utility; every keep-ancestor transition is a self-loop.
    utilities = {"baseline": F(1, 2), "high": F(1), "low": F(0)}
    keep = {state: state for state in utilities}
    mechanisms = [
        {"keep": keep, "reuse": {**keep, "baseline": "high"}},
        {"keep": keep, "reuse": {**keep, "baseline": "low"}},
    ]
    assert mechanisms[0]["keep"] == mechanisms[1]["keep"]
    effects = [
        utilities[k["reuse"]["baseline"]] - utilities[k["keep"]["baseline"]]
        for k in mechanisms
    ]
    assert effects == [F(1, 2), F(-1, 2)]
    half_range = abs(effects[0] - effects[1]) / 2
    midpoint = sum(effects) / 2
    assert max(abs(midpoint - effect) for effect in effects) == half_range == F(1, 2)

    print(json.dumps({
        "status": "all mathematical witnesses passed",
        "coordinate_dependence": coordinate,
        "positive_net_coefficient_but_negative_slope": float(slope),
        "gain_debt_shift_invariant": True,
        "negative_interaction_without_harm": gamma_redundant,
        "positive_interaction_with_bad_cross_pairs": gamma_incompatible,
        "self_target_gains": [float(own_parent), float(own_child)],
        "common_target_improver_advantage": float(common_delta),
        "same_summary_different_next_laws_tv": float(tv),
        "positive_average_with_task_regression": float(average_gain),
        "same_observations_opposite_reuse_effects": [float(x) for x in effects],
        "unidentified_effect_minimax_absolute_error": float(half_range),
    }, indent=2))


if __name__ == "__main__":
    main()

