# Evaluation standard

This document defines the minimum experiment needed to claim self-improvement or recursive self-improvement.

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

Use four cohorts:

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

Every claimed persistent improvement needs an equal-total-resource parent baseline.

If producing $S_1$ costs $C_{\text{improve}}$, compare it with a parent strategy allowed to spend the same total resource through additional search, sampling, or task-time computation. Report immediate and amortized cost.

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

$$

\Delta_{\text{obs}}=
\Delta_{\text{compute}}
+\Delta_{\text{selection}}
+\Delta_{\text{task-fit}}
+\Delta_{\text{transfer}}
+\Delta_{\text{measurement}}
+\epsilon.

$$

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

For model $M$, harness $H$, and improver $I$, evaluate a factorial subset of:

$$

M_i\times H_j\times I_k.

$$

The minimum model–harness cross is:

$$

(M_0,H_0),\quad
(M_1,H_0),\quad
(M_0,H_1),\quad
(M_1,H_1).

$$

Interpretation:

- $M_1,H_0$ gain: model contribution;
- $M_0,H_1$ gain: harness contribution;
- excess gain of $M_1,H_1$: interaction or co-adaptation;
- failure of $H_1$ on other models: model-specific compensation;
- failure of $M_1$ on other harnesses: harness-conditioned model update.

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

$$

\Delta(s)=U_Q(M_s,H_1)-U_Q(M_s,H_0)

$$

and the corresponding cost. A single small-model result cannot support a frontier-model claim. A single frontier-model result cannot reveal whether the method depends on capabilities absent from smaller systems.

## 14. Test recursion directly

For D3, compare parent and successor as improvers on a new improvement problem.

$$

S_0 \xrightarrow{I_0} S_1,\qquad
S_0 \xrightarrow[\text{new problem}]{B} C_0,\qquad
S_1 \xrightarrow[\text{same problem}]{B} C_1.

$$

Evaluate $C_0$ and $C_1$ on hidden tasks. Match the improvement budget $B$.

Measure:

- quality of proposed modifications;
- fraction of valid candidates;
- accepted gain on held-out tasks;
- improvement per unit cost;
- breadth of transfer;
- regressions;
- time to a useful successor;
- evaluator exploitation rate.

A repeated outer loop with a fixed stronger optimizer does not establish recursion unless $S_1$ improves these quantities.

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
- **D3:** “The successor produced better later successors on a new improvement problem under matched budget.”
- **D4:** reserved for sustained D3 evidence across changing task distributions and bottlenecks.

Do not use “recursive self-improvement” as shorthand for one iteration of automated optimization.
