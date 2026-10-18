# Evaluation standard

This document specifies the repository's operational evidence standard for empirical claims. D3 refers to improved improvement ability; it does not require accelerating scores or a separately mutable improver module. Formal results are assessed by their assumptions and proofs; exact verification establishes its stated specification. The empirical task-splitting protocol is not a mandatory architecture for every method.

## 1. Register the complete system

Each evaluated version must identify:

```text
system_id
parent_system_id
model provider and checkpoint
model weights hash when available
harness commit and configuration
prompts and context policy
memory and skill state
tools and external services
improver version
training or update procedure
evaluator versions
runtime and dependencies
creation timestamp
```

A model name does not identify a system. A harness commit does not identify a system. The pair and its execution conditions are the evaluated object.

## 2. Freeze the claim before the run

Declare:

- changed objects;
- fixed objects;
- forbidden changes;
- primary metric;
- protected regression metrics;
- improvement budget;
- task-time budget;
- task splits;
- stopping rule;
- number of candidates and generations;
- transfer axes;
- recursion claim, if any.

Post hoc changes belong in a new experiment.

## 3. Separate task cohorts

For the proposed empirical transfer experiments, use four cohorts:

- $P$: improvement tasks visible to candidate generation and selection;
- $V$: validation tasks with limited exposure;
- $Q$: hidden tasks inaccessible during modification;
- $T$: time-forward tasks created after the candidate is frozen.

Record template overlap, shared source data, common generators, and likely contamination. A nominally hidden split from the same public benchmark is weaker than a time-forward cohort.

## 4. Account for total resources

Record:

- input and output tokens by model;
- model calls;
- candidates;
- evaluator calls;
- tool calls;
- CPU and accelerator time;
- wall-clock time;
- API and external-service cost;
- human interventions;
- failed runs and retries.

Separate matched-execution, matched-improvement, and lifecycle-cost comparisons. Declare the deployment horizon for amortized cost; a one-task total-cost comparison does not settle the value of a reusable update.

If producing $S_1$ costs $C_{\text{improve}}$, compare lifecycle alternatives over the same future tasks and report both creation and execution cost. Resource types require a declared conversion before they can be added. For improver comparisons, match improvement budget $B$ and separately fix descendant execution budget $b$.

## 5. Use the required baselines

At minimum:

1. parent, standard task budget;
2. parent, equal total budget;
3. successor, standard task budget;
4. random or restricted edit search;
5. strongest fixed optimizer available for the same editable surface;
6. stronger-model baseline when relevant;
7. human-designed change when a natural comparison exists.

A self-improvement method that loses to a fixed external optimizer under matched cost has not yet shown that self-reference adds value.

## 6. Preserve candidate lineage

For every candidate:

```text
candidate_id
parent_id
proposer
proposer_version
hypothesis
diff or parameter change
visible evidence
task results
resource use
selection score
accept or reject
rejection reason
later transfer
```

Keep rejected candidates. They are needed to measure search efficiency, selection bias, lineage value, and whether an early branch becomes useful after later model changes.

## 7. Reevaluate selected winners

Selecting the best of many noisy candidates produces optimistic estimates.

Required controls:

- repeated evaluation of the unchanged parent;
- repeated evaluation of accepted successors;
- paired task outcomes;
- uncertainty intervals;
- number of candidates searched;
- correction or fresh evaluation after selection;
- external replication for small deltas.

A gain inside the parent’s repeat-evaluation noise is unresolved.

## 8. Decompose observed gain

Observed score change can contain:

$

\Delta_{\text{obs}}=
\Delta_{\text{compute}}
+\Delta_{\text{selection}}
+\Delta_{\text{task-fit}}
+\Delta_{\text{transfer}}
+\Delta_{\text{measurement}}
+\epsilon.

$

This is an experimental decomposition, not an identity recoverable from one run.

Estimate the terms through:

- equal-compute baselines;
- fresh candidate reevaluation;
- untouched and time-forward tasks;
- model and harness swaps;
- evaluator replacement;
- component ablation;
- parser and logging invariance checks.

Only $\Delta_{\text{transfer}}$, net of unacceptable regressions and cost, supports a general improvement claim.

## 9. Cross components

For target model $M$, target harness $H$, and configured improver $A$, evaluate a feasible factorial subset of:

$

M_i\times H_j\times A_k.

$

The minimum model–harness cross is:

$

(M_0,H_0),\quad
(M_1,H_0),\quad
(M_0,H_1),\quad
(M_1,H_1).

$

Interpretation:

- $M_1,H_0$ gain: model contribution;
- $M_0,H_1$ gain: harness contribution;
- excess gain of $M_1,H_1$: interaction or co-adaptation;
- failure of $H_1$ on other models: possible model dependence, compensation, or interface incompatibility;
- failure of $M_1$ on other harnesses: possible harness conditioning or interface incompatibility.

Hold data and task-time resources fixed and record adapters. Interaction sign alone cannot distinguish synergy, redundancy, conflict, or portability; see THEORY.md. If improver and target share components, pin a separate snapshot to realize the intended intervention.

Apply analogous swaps to memory, tools, data filters, reward models, and evaluators.

## 10. Measure transfer as a vector

Report separately:

- same-distribution held-out transfer;
- time-forward transfer;
- domain transfer;
- model-family transfer;
- model-scale transfer;
- harness transfer;
- tool or environment transfer;
- evaluator transfer.

Do not collapse these into the word “generalizes.”

## 11. Measure regressions

Predeclare protected capabilities and unacceptable loss thresholds.

Report:

- per-task delta;
- per-domain delta;
- worst-case delta;
- calibration and reliability;
- cost and latency;
- tool error and recovery rate;
- safety and authorization violations;
- provenance completeness.

Average improvement does not erase a critical regression.

## 12. Audit tampering and metric drift

The editable system must not be able to silently:

- alter answer keys or hidden tests;
- skip difficult tasks while changing the denominator;
- rewrite logs or provenance;
- increase retries without accounting;
- change parsers to accept invalid outputs;
- call unauthorized tools;
- modify the final evaluator;
- suppress failures;
- leak benchmark identifiers into prompts or code.

Run invariant checks over task count, raw outputs, logs, costs, and evaluator inputs. Store raw evidence outside the candidate workspace.

## 13. Test model scale

Use several model capability levels when the claim concerns general harness or improver behavior.

Report:

$

\Delta(s)=U_Q(M_s,H_1)-U_Q(M_s,H_0)

$

and the corresponding cost. A single small-model result cannot support a frontier-model claim. A single frontier-model result cannot reveal whether the method depends on capabilities absent from smaller systems.

## 14. Test improvement ability on common targets

Record how $S_0$ produced a persistent $S_1$. Then use old and new versions as improvers on identical copies of each target $T$:

$$
T'_0\sim K_{S_0}(\cdot\mid T,p,B),
\qquad
T'_1\sim K_{S_1}(\cdot\mid T,p,B).
$$

Estimate the paired difference $G(S_1;\mu,B,b)-G(S_0;\mu,B,b)$ using common target/problem distribution $\mu$, improvement budget $B$, and descendant execution budget $b$. Include rejected candidates and failed runs in costs. Repeat whole improvement runs; repeated scoring of a single selected child does not estimate search variability.

Do not substitute a comparison of $S_0$ improving itself against $S_1$ improving itself: that also changes the target and remaining headroom.

For recursive reuse, continue with the current successor as improver versus a pinned ancestor improver, giving both the same current target. Freeze all ancestor dependencies, not only its outer code. Compare under equal feedback access and external assistance.

Report gains, important regressions, uncertainty, transfer axes, and the deployment scope. If new task cohorts change difficulty, do not interpret an uncalibrated cross-generation score slope as acceleration. Use common anchors or compare both systems on the same new cohort.

See Experiment 003 for the full protocol.

## 15. Publish a result bundle

```text
manifest.json
task_cohorts.json
lineage.jsonl
resource_accounting.json
raw_results/
raw_evidence/
analysis.py
environment lockfile or container
report.md
```

The report must state:

- what was author-reported;
- what was directly reproduced;
- what was independently replicated;
- what failed;
- what remains unresolved.

## 16. Acceptance language

Use the strongest statement supported by the experiment.

- **D0:** “Additional search improved current-task performance.”
- **D1:** “The system produced a persistent successor.”
- **D2:** “The persistent change improved specified untouched distributions under the stated budget.”
- **D3:** “The successor improved common reference targets more effectively than its parent under matched budgets.”
- **D4:** reserved for sustained D3 evidence across changing task distributions and bottlenecks.

Do not use “recursive self-improvement” as shorthand for one iteration of automated optimization.

