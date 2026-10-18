# Working hypotheses

This file contains propositions that organize the research program. They are not treated as established facts. Each hypothesis must remain easy to challenge, replace, or falsify.

Statuses:

- **open** — plausible and not yet decided;
- **supported** — multiple controlled results support it, but it remains revisable;
- **weakened** — important counterevidence exists;
- **falsified** — the stated form fails a decisive test;
- **superseded** — replaced by a more precise formulation.

## H1 — Improvement behavior adds predictive information

**Status:** open.

The actor-target kernel $T'\sim K_A(\cdot\mid T,p,B)$ records how a configured system modifies a target. The hypothesis is that common-target improvement performance $G(A;\mu,B,b)$ predicts future useful changes beyond task performance alone.

**Alternative:** ordinary task capability and target properties explain most observed improvement performance.

**Decisive test:** compare actors with similar task capability on identical copies of common targets, then predict descendant quality on withheld target families. The actor-target distinction is a definition; predictive value is the hypothesis.

## H2 — Improvement performance admits a useful low-dimensional summary

**Status:** open.

A gain-versus-budget curve $G(A;\mu,B,b)$, or a vector across target families, may be a useful predictor. A scalar efficiency requires a declared scalar resource cost. It is not automatically equal to the path slope $dJ/dr$.

**Alternative:** histories, executable structure, and target-specific behavior prevent a stable low-dimensional reduction.

**Decisive test:** after conditioning on the proposed summary, test whether omitted state still predicts intervention outcomes. Then test competing mechanisms with the interventions on which their predictions disagree. THEORY.md distinguishes state sufficiency, intervention identifiability, and a conditional approximation-error bound; a sufficient state alone does not identify an untested intervention's effect.

## H3 — Model and harness optima move together

**Status:** open.

The optimal harness depends on the model:

$$
H^*=H^*(M,E,B),
$$

and the most valuable training distribution depends on the model–harness pair:

$$
D^*=D^*(M,H,E,V^*).
$$

The empirical hypothesis is that substantial model updates often alter harness rankings. Dependence in the notation does not prove this; additive separable utility is a counterexample to necessary rank change.

**Alternative:** strong models may make most harness differences negligible, producing an approximately universal minimal harness.

**Decisive test:** evaluate a harness portfolio across successive model versions and estimate rank stability, interaction effects, and transfer.

## H4 — Externalize, verify, internalize, re-externalize is an efficient long-run cycle

**Status:** open.

New strategies should often appear first in the harness because harness changes are cheap and inspectable. Stable, high-frequency, transferable behavior can later be compressed into model weights. The updated model then changes which external structures are useful.

The proposed cycle is:

$$
H_t
\rightarrow
D_t^{\rm verified}
\rightarrow
M_{t+1}
\rightarrow
H_{t+1}.
$$

**Alternative:** direct model training may dominate once models are sufficiently capable, or external computation may remain permanently more efficient than internalization.

**Decisive test:** compare long-horizon capability and total cost for harness-only, model-only, and alternating externalize/internalize schedules under equal resource budgets.

## H5 — Evaluator fidelity changes search efficiency

**Status:** open.

Feedback quality may change which candidate count is most useful under a fixed total budget. Absolute selected gain and gain per unit cost must be measured separately.

**Alternative:** candidate diversity, generation cost, or adaptive task fitting dominates fidelity; there may be no sharp threshold.

**Decisive test:** vary evaluator fidelity and candidate count independently with external final assessment. The i.i.d. joint Gaussian model predicts increasing absolute true gain at fixed positive fidelity, even when cost-normalized efficiency eventually falls. A universal phase boundary does not follow from that model.

## H6 — Portfolio plus lineage beats greedy replacement in nonstationary systems

**Status:** open.

When the model and task distribution change, a previously rejected harness branch can become useful. Maintaining a portfolio and ancestry should therefore outperform a single incumbent when the objective is nonstationary.

**Alternative:** the cost of preserving and revisiting branches may outweigh the benefit; a well-regularized greedy strategy may be sufficient.

**Decisive test:** compare greedy, beam, lineage-aware, and diversity-preserving search across several model updates under identical candidate and evaluation budgets.

## H7 — The earlier sign-only gain-versus-debt criterion

**Status:** superseded.

The earlier statement that the sign of $g-d$ determines rising improvement efficiency is false for the retained illustrative equation:

$$
\eta'=(g-d)\eta-\kappa\eta^2+u.
$$

For $\eta>0$, rising slope requires $g-d>\kappa\eta-u/\eta$. Separate gain and debt are not identifiable from their difference: adding the same function to each leaves the trajectory unchanged. The previous differential “recursive term” is also coordinate dependent; THEORY.md gives an explicit counterexample.

**Replacement question:** can a reduced, identifiable model of common-target improvement performance predict withheld interventions after state-sufficiency checks?

**Decisive test:** use separately controlled interventions and compare prediction against fixed-improver and target-headroom models. Curve fitting alone does not restore the earlier causal interpretation.

## H8 — D2 will be common; D3 will be rare

**Status:** open.

Many systems may produce persistent, transferable improvements without producing successors that are better improvers.

**Alternative:** once a system gains broad capability, improved self-improvement may arise almost automatically.

**Decisive test:** for every transferable successor, estimate the paired common-target difference

$
G(S_{t+1};\mu,B,b)-G(S_t;\mu,B,b)
$

with uncertainty. D3 is this repository's stronger evidence convention, not a requirement for increasing raw score slopes.

## H9 — Improver quality is a distinct capability

**Status:** open.

A stronger task solver is not necessarily a stronger improver. Proposal generation, experiment design, attribution, parent selection, budget allocation, and update choice form a separate capability that must be measured directly.

**Alternative:** general model capability may explain most variation in improver quality.

**Decisive test:** cross proposer/evolver models with executor models and evaluators. Measure descendant quality after controlling for task-solving ability.

## H10 — Optimal RSI is a resource-allocation problem

**Status:** open.

At each generation, resources can be allocated to model training, harness search, improver improvement, data/environment construction, or evaluation. The best allocation should depend on marginal future-improvement value rather than a fixed recipe.

For control vector $u$:

$$
\max_{u_{0:T}}
\mathbb E
\left[
J(S_T)+\lambda G(S_T;\mu,B,b)-\sum_t C(u_t)
\right].
$$

**Alternative:** model uncertainty may be so large that adaptive optimal control offers little advantage over robust fixed schedules.

**Decisive test:** compare fixed schedules, greedy one-step allocation, and model-predictive allocation on the same multi-generation budget.

## H11 — Scale transfer is non-monotone

**Status:** open.

A harness or self-improvement rule may fail on weak models, help intermediate models, and become redundant or obstructive on strong models. The effect

$$
\Delta(s)=J(M_s,H_1)-J(M_s,H_0)
$$

need not increase with scale.

**Alternative:** useful system-level improvements may transfer monotonically once normalized for cost.

**Decisive test:** evaluate identical interventions across several capability levels and model families.

## H12 — Verified causal experience is more valuable than undifferentiated success traces

**Status:** open.

Training data should retain intervention provenance, counterfactuals, failed alternatives, verifier evidence, and resource use. Such data should produce more transferable model improvement than simply training on successful trajectories.

**Alternative:** sufficiently large successful-trace corpora may dominate elaborate causal curation.

**Decisive test:** construct matched training sets with equal token budgets: successful traces only versus evidence-bearing matched trajectories. Compare transfer, calibration, and future improvement ability.

---

## What would change the theory

The current theory should be revised if experiments show any of the following repeatedly:

- task capability alone predicts descendant quality as well as the improvement kernel;
- common-target improvement summaries are unstable across domains or fail state-sufficiency tests;
- harness rankings remain invariant across substantial model updates;
- evaluator fidelity does not predict selection failure after resource controls;
- portfolio search does not beat simpler search under nonstationarity;
- parent and successor improvement ability are indistinguishable even when task capability rises;
- a proposed reduced model fails state-sufficiency checks or withheld intervention prediction.

H7's earlier sign-only criterion and coordinate-based recursion interpretation have already been superseded by mathematical counterexamples. This is a model correction, not an empirical claim about AI.

A theory that cannot lose is not useful.
