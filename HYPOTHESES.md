# Working hypotheses

[English](HYPOTHESES.md) · [简体中文](docs/zh/HYPOTHESES.md)

Twelve open hypotheses organize the research program. Each has a competing explanation and an experiment that can distinguish them.

Statuses:

- **open** — plausible and not yet decided;
- **supported** — multiple controlled results support it, but it remains revisable;
- **weakened** — important counterevidence exists;
- **falsified** — the stated form fails a decisive test;
- **superseded** — replaced by a more precise formulation.

## H1 — The improvement operator is the central object

**Status:** open.

Task capability alone does not identify RSI. The more informative object is the resource-normalized mapping from a current system to a distribution over successor systems:

$$
S' \sim K_S(\cdot\mid S,E,V^*,B).
$$

RSI requires a successor whose improvement kernel is better on new improvement problems:

$$
K_{S'} \succ K_S.
$$

**Alternative:** recursive improvement may be adequately characterized by a scalar capability trajectory without explicitly modeling the successor-generating operator.

**Decisive test:** compare two systems with similar task capability but different improvement kernels. If they produce systematically different descendant quality under matched budgets, the operator carries information that capability alone misses.

## H2 — Improvement efficiency is a useful macrostate variable

**Status:** open.

Define

$$
\eta(S)
=
\frac{
\mathbb E[\Delta J_{\rm transfer}-\lambda L_{\rm regression}]
}{
C_{\rm improve}
}.
$$

The working hypothesis is that $\eta$ is a useful order parameter for comparing improvement regimes across systems and generations.

**Alternative:** improvement is too multidimensional for any scalar projection to remain stable across domains; only a Pareto frontier or kernel-level description is meaningful.

**Decisive test:** measure whether $\eta$ predicts descendant quality across different task families, model scales, and editable surfaces better than current capability alone.

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

A substantial model update should therefore alter the ranking of harnesses.

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

## H5 — Evaluator fidelity is a phase variable

**Status:** open.

Let true candidate gain be $g$ and measured gain be $y$. Define

$$
\rho=\operatorname{Corr}(g,y).
$$

The hypothesis is that candidate search has a qualitative threshold: below sufficient evaluator fidelity, more search mostly selects noise or exploits the metric.

**Alternative:** robust aggregation, repeated evaluation, or search regularization may avoid a sharp evaluator threshold.

**Decisive test:** vary evaluator noise and candidate count independently while retaining an external ground-truth test. Measure true selected gain and the location of the optimal candidate count.

## H6 — Portfolio plus lineage beats greedy replacement in nonstationary systems

**Status:** open.

When the model and task distribution change, a previously rejected harness branch can become useful. Maintaining a portfolio and ancestry should therefore outperform a single incumbent when the objective is nonstationary.

**Alternative:** the cost of preserving and revisiting branches may outweigh the benefit; a well-regularized greedy strategy may be sufficient.

**Decisive test:** compare greedy, beam, lineage-aware, and diversity-preserving search across several model updates under identical candidate and evaluation budgets.

## H7 — Recursive design gain competes with complexity and verification debt

**Status:** open.

A minimal macro-dynamics is

$$
\frac{dC}{dr}=\eta,
$$

$$
\frac{d\eta}{dr}
=
[g(C,\ldots)-d(C,\ldots)]\eta
-\kappa\eta^2
+u_{\rm ext}.
$$

The sign of

$$
\lambda_{\rm RSI}=g-d
$$

is hypothesized to be more informative than capability alone for determining whether improvement efficiency grows or decays.

**Alternative:** the decomposition into recursive gain and debt may be non-identifiable or too representation-dependent to support prediction.

**Decisive test:** fit the model to multiple intervention sequences and test out-of-sample prediction of future improvement efficiency under different resource allocations.

## H8 — D2 will be common; D3 will be rare

**Status:** open.

Many systems may produce persistent, transferable improvements without producing successors that are better improvers.

**Alternative:** once a system gains broad capability, improved self-improvement may arise almost automatically.

**Decisive test:** for every transferable successor, run a matched parent-versus-successor improvement experiment on a new problem. Estimate the recursion number

$$
\mathcal R
=
\frac{\eta(S_{t+1})}{\eta(S_t)+\varepsilon}.
$$

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
J(S_T)+\lambda\eta(S_T)-\sum_t C(u_t)
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
- $\eta$ is unstable across domains and cannot be replaced by a reliable vector-valued quantity;
- harness rankings remain invariant across substantial model updates;
- evaluator fidelity does not predict selection failure after resource controls;
- portfolio search does not beat simpler search under nonstationarity;
- parent and successor improvement ability are indistinguishable even when task capability rises;
- the nonlinear phase model fails out-of-sample prediction across intervention schedules.

A theory that cannot lose is not useful.