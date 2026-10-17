# Experiment 003 — Successor as improver on common targets

## Competing explanations

The successor may be a better improver, may merely start from a stronger target, or may have different remaining headroom. The intervention must separate these explanations.

## Construction

Record a persistent lineage $S_0\to S_1$, including the contribution of the parent and any human or external-model assistance. Freeze both complete improver snapshots.

Sample previously unused target/problem pairs $(T,p)$ from a declared distribution $\mu$. Supply identical target copies, editable surfaces, visible data, tool permissions, feedback access, and improvement budgets $B$ to the two actors:

$$
T'_0\sim K_{S_0}(\cdot\mid T,p,B),
\qquad
T'_1\sim K_{S_1}(\cdot\mid T,p,B).
$$

Use the same descendant execution budget $b$ on reserved test tasks $Q_p$. Failed runs and no accepted edit return the unmodified target with the costs still recorded. Repeat complete improvement runs, not only scoring of selected descendants. Randomize actor/run order and block by target; use common random seeds where they give meaningful paired comparisons.

The actors' private persistent information is part of the treatment. If isolating policy versus information is important, add a separate shared-data arm instead of silently erasing learned state from only one actor.

## Primary quantity

$$
\Delta_{\rm rec}
=
\mathbb E\!\left[J_{Q_p}(T'_1;b)-J_{Q_p}(T'_0;b)\right]
=
G(S_1;\mu,B,b)-G(S_0;\mu,B,b).
$$

Report an uncertainty interval over targets and complete improvement runs, domain-specific gains, critical regressions, and the gain-versus-budget curve. Retain proposal validity, useful-child rate, costs, and feedback failures as explanatory measurements.

A positive result is a scoped D3 result if the lineage and actor intervention identify the successor's contribution. It is not an estimate of an unlimited growth exponent.

## Causal reuse

Continue later generations with a refreshed successor improver versus a pinned ancestor improver, both operating on the same current targets. Freeze the ancestor's model, code, data, and service versions, not just its orchestration code. This tests whether using the new improver adds benefit beyond simply improving the target.

For adaptive target curricula, compare both actors on each common new cohort. Use an anchored cohort when comparing effect sizes over generations; increasing task difficulty can reduce raw gains even for a better improver.

## Decisive outcomes

- Positive common-target difference: improved improvement performance on the declared distribution and budgets.
- A self-versus-self gain without a common-target gain: target changes/headroom remain an alternative explanation.
- Improved task performance without improved $G$: better solving has not yet yielded a better improver on this test.
- Gains only with stronger external assistance: attribute that assistance explicitly.
- Continued actor-refresh gains across later cohorts: evidence for useful recursive reuse over that observed horizon.

No requirement is imposed that every round improve, both model and harness change, or the outer optimizer code rewrite itself.

## Required artifacts

Preserve actor and target snapshots separately, lineage, target/problem manifests, task splits, all proposals, feedback exposure, selection/stopping decisions, descendant checkpoints, raw test outcomes, and per-run resource records. The result must be reproducible from these artifacts.

**Status:** protocol; no real-system run is claimed here.

