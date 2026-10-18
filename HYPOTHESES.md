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

**Derived boundary:** one-step gain cannot determine multi-step route quality,
even if it is larger at every target and both routes preserve current utility.
THEORY.md Proposition 5 gives the exact witness and continuation comparison.
This does not decide whether G has incremental statistical predictive value.

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

## H4 — Execution advantage can be inherited at a useful total cost

**Status:** open.

Harness exploration can produce behavior worth learning, but the execution
advantage must survive projection into the learner, preservation of decision
inputs, and transfer to future tasks. The total generation and training cost
must be amortized. MECHANISMS.md derives a sufficient bounded-utility condition
and an exact missing-input obstruction. The strongest executing harness and
the most useful teaching harness need not coincide.

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

**Decisive test:** compare execution-selected and post-update-value-selected
training sources under equal generation/training budgets. Independently vary
preserved decision inputs and source-task weights. Then compare their full
continuation value with model-only and harness-only alternatives.

**Bounded result:** Experiment 006 compares update orders in a numerical
optimizer. It finds an M-then-H advantage over H-then-M on new instances but
does not establish an advantage over joint search or across new families.
It does not implement weight distillation from LLM trajectories.

**Further bounded result:** Experiment 008 executes search-generated context
policy learning. Reusing the learned policy improves held-out search and the
value of data it generates for common fresh learners in the 8-puzzle. Shared
pop caps do not equalize training arithmetic or CPU time; both are reported.
This supports a particular inheritance mechanism, not the general hypothesis
across language models and research domains.

## H5 — Feedback correctness and localization change different mechanisms

**Status:** open.

Feedback quality may change which candidate count is most useful under a fixed total budget. Absolute selected gain and gain per unit cost must be measured separately.

An exact final pass/fail bit need not identify how to repair a candidate.
MECHANISMS.md gives an exponential-versus-linear query separation when local
decisions compose and feedback identifies the first failed component.
Experiment 007 executes that construction. Whether agent traces supply
similarly useful localization remains an empirical question.

**Alternative:** candidate diversity, generation cost, or adaptive task fitting dominates fidelity; there may be no sharp threshold.

**Decisive test:** vary evaluator fidelity and candidate count independently with external final assessment. The i.i.d. joint Gaussian model predicts increasing absolute true gain at fixed positive fidelity, even when cost-normalized efficiency eventually falls. A universal phase boundary does not follow from that model.

Also hold final correctness and query cost fixed while removing diagnostic
localization; this distinguishes better judgment from more actionable feedback.

## H6 — Portfolio plus lineage beats greedy replacement in nonstationary systems

**Status:** open.

When the model and task distribution change, a previously rejected harness branch can become useful. Maintaining a portfolio and ancestry should therefore outperform a single incumbent when the objective is nonstationary.

**Alternative:** the cost of preserving and revisiting branches may outweigh the benefit; a well-regularized greedy strategy may be sufficient.

**Decisive test:** compare greedy, beam, lineage-aware, and diversity-preserving search across several model updates under identical candidate and evaluation budgets.

SEARCH.md distinguishes preserving complete computations from locally mixing
their action probabilities. Fair interleaving has a scoped constant-overhead
completion guarantee. Experiment 008 finds whole-search preservation better
than local mixing but usually worse than the best learned search at equal pops.
This does not settle H6's nonstationary archive hypothesis.

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

For a declared terminal objective, compare admissible policies by

$$
\max_{\pi:\,\sum_t c_t\preceq B}\;
\mathbb E_\pi[J(X_\tau)].
$$

Here $c_t$ and $B$ may be resource vectors; $\tau$ is the declared stopping
time. A scalar cost penalty or an extra reward for G is a chosen objective,
not a necessary law. THEORY.md Proposition 5 decomposes the difference between
two feasible policies without assuming a universal growth equation.

**Alternative:** model uncertainty may be so large that adaptive optimal control offers little advantage over robust fixed schedules.

**Decisive test:** compare fixed schedules, greedy one-step allocation, and model-predictive allocation on the same multi-generation budget.

SEARCH.md adds established value-of-computation reasoning and an alternative
to expensive winner prediction: preserve a complete baseline with a fixed
budget share. Experiment 008 records build-plus-deployment CPU costs and shows
that the cost comparison changes with the deployment cap. It does not test a
general learned allocation controller or establish that adaptive selection wins.

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

## H13 — Research-production conditions add predictive information

**Status:** open.

For comparable AI-development tasks, measurements of experience generation,
feedback error, learning procedure, adopted infrastructure changes and workflow
bottlenecks improve out-of-family predictions of useful research output beyond
solver scores, model/harness identifiers and nominal compute alone.

**Alternative:** those simpler summaries predict sufficiently well; extra
production detail merely fits each observed project separately.

**Decisive test:** estimate a mechanism on one set of systems, then predict
the effects of freezing curricula/opponents, changing training feedback or
adopting a computation improvement in withheld systems. Charge human input,
generation, training, failed trials, integration and assessment. Measure useful
adopted results and successor performance, not code volume alone. No separate
free parameter for each held-out outcome is permitted.

THEORY.md Section 10 gives an exact score-change decomposition and conditional
Amdahl accounting. Neither establishes this hypothesis or predicts indefinite
recursion. The source coverage change is not empirical validation of H13.

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

Experiment 006 now provides an empirical record within one bounded numerical
search class. Recursive reuse and direct improver-objective training did not
establish the intended improvement advantage. No broad hypothesis is promoted
to established on the basis of that experiment.

A theory that cannot lose is not useful.
