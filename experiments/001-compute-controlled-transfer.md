# Experiment 001: compute-controlled harness transfer

## Question

Does an AI-generated harness modification produce a persistent and transferable gain beyond the benefit of spending the same total compute on the original system?

This experiment targets the most accessible public RSI claim: a fixed base model modifies the software around itself.

## Hypotheses

- **H1: reusable harness improvement.** The successor harness improves untouched tasks under the same task-time budget and transfers to another model family.
- **H2: benchmark adaptation.** The successor improves the optimization tasks but has little or negative held-out gain.
- **H3: compute substitution.** The successor's gain disappears when the parent receives the same total compute.
- **H4: model-specific compensation.** The harness helps the source model but does not transfer to another model.
- **H5: recursive gain.** The successor system produces a better second-generation harness than the parent system under the same improvement budget.

## System

Let \(M_a\) be the source model and \(M_b\) a model from another family. Let \(H_0\) be a versioned starting harness. The improver may modify only a declared subset of \(H_0\), for example:

```text
prompts
context construction
memory policy
tool descriptions and routing
control flow
stopping rules
```

Model weights, benchmark data, hidden tests, and final evaluator remain fixed.

## Task split

Create four disjoint sets:

- \(P\): improvement tasks visible during candidate generation and selection;
- \(V\): validation tasks used only for predetermined checkpoints;
- \(Q\): held-out tasks unavailable until the harness is frozen;
- \(T\): time-forward tasks collected or created after freezing the harness.

Record shared templates, data sources, and potential contamination among the sets.

## Conditions

Run at least the following conditions:

1. **Parent:** \((M_a,H_0)\) with the standard task-time budget.
2. **Parent + equal compute:** \((M_a,H_0)\) allowed to spend the total resources used to create and execute the successor, through a declared stronger inference strategy.
3. **Successor:** \((M_a,H_1)\) with the same task-time budget as condition 1.
4. **Cross-model parent:** \((M_b,H_0)\).
5. **Cross-model successor:** \((M_b,H_1)\).
6. **Second generation from parent:** use \((M_a,H_0)\) as the improver to create a descendant under budget \(B\).
7. **Second generation from successor:** use \((M_a,H_1)\) as the improver to create a descendant under the same budget \(B\).

If the improver uses a separate model, its identity and budget must remain fixed across conditions 6 and 7. A second variant may let the task system itself act as the improver, but the two variants should not be conflated.

## Candidate generation

For every candidate, save:

```text
parent commit
proposer version
improvement hypothesis
files changed
full diff
visible task evidence
compile / smoke-test result
score on P and V
resource cost
selection decision
```

Use a predetermined candidate budget and stopping rule. Do not stop immediately after a favorable random result.

## Primary outcomes

For each task set \(X\in\{P,V,Q,T\}\), measure

\[
\Delta_X = U_X(M_a,H_1)-U_X(M_a,H_0).
\]

Measure cross-model transfer:

\[
\Delta_{Q}^{(b)} = U_Q(M_b,H_1)-U_Q(M_b,H_0).
\]

Measure cost-adjusted value:

\[
A_Q = 
\frac{U_Q(M_a,H_1)-U_Q(M_a,H_0)}
{C_{\mathrm{improve}}+N\,\Delta C_{\mathrm{task}}},
\]

where \(N\) is the number of future tasks over which the improvement cost is amortized and ΔC_task is the successor's extra per-task cost.

Measure recursive gain by comparing the held-out improvement produced in conditions 6 and 7 under equal budgets.

## Decision rules

Evidence for reusable harness improvement requires all of the following:

- positive held-out gain larger than measured evaluation noise;
- no predefined critical regression;
- the successor beats the parent under equal task-time compute;
- the gain remains favorable after reporting added latency and tool cost.

Evidence for model-agnostic harness improvement additionally requires positive transfer to \(M_b\).

Evidence for recursive improvement requires the successor to produce a better second-generation descendant on held-out tasks or to reach the same gain at lower cost. A better first-generation task score is insufficient.

## Required outputs

```text
systems/
  H0/
  H1/
tasks/
  P.json
  V.json
  Q.json
  T.json
lineage.jsonl
resource_accounting.json
raw_results/
analysis.py
report.md
```

The report must include failed candidates, task-level results, confidence intervals, and every human intervention.

## Falsifying outcomes

The experiment should be considered informative when it finds any of the following:

- large \(P\) gain and negligible \(Q\) gain;
- positive \(Q\) gain that loses to the equal-compute parent;
- source-model gain and cross-model regression;
- first-generation gain with no second-generation improvement advantage;
- a successor whose aggregate score rises while a critical capability regresses.

Each outcome narrows the conditions under which harness RSI is a valid route.
