# Evaluation protocol

This protocol specifies the minimum information needed to compare a parent system with a self-modified successor. Individual experiments may add stricter requirements.

## 1. Version the complete system

Record a system manifest for every evaluated version:

```text
system_id
parent_system_id
model provider / checkpoint / weights hash
harness commit and configuration
prompts and context-construction code
memory, tools and external services
training or update procedure
runtime and dependency versions
evaluator version
creation timestamp
```

A model name alone does not identify an AI system. A harness commit alone does not identify one either.

## 2. Declare the editable surface

Before the run, list every object the improver may change and every object held fixed. Examples:

```text
editable: prompts, tool descriptions, control flow
fixed: model weights, task data, evaluator, token budget
forbidden: benchmark identifiers, answer keys, evaluator code
```

If the editable surface changes during the run, record when and why.

## 3. Separate task sets

Use at least three sets:

- **improvement set \(P\):** visible to candidate generation and selection;
- **validation set \(V\):** used sparingly for model or procedure choices;
- **held-out set \(Q\):** never used to generate, select, stop, or tune the successor.

For long-running projects, maintain a **time-forward set \(T\)** created after the successor is frozen. Report any task overlap, shared templates, common data sources, or likely contamination.

## 4. Equalize resources

Report resources for both improvement and evaluation:

- input and output tokens by model;
- number of model calls;
- number of candidates;
- evaluator calls;
- tool calls;
- CPU and accelerator time;
- wall-clock time;
- API and external-service cost;
- human interventions.

Run an **equal-total-resource parent baseline**. If producing and evaluating the successor costs \(C\), give the parent a comparison strategy that may spend the same \(C\) through additional search, sampling, or task-time computation. Report both one-task and amortized comparisons.

## 5. Preserve the candidate lineage

For each candidate, record:

```text
candidate_id
parent_id
proposer and proposer version
hypothesis
changed files or parameters
visible evidence
evaluation results
resource use
accept / reject decision
selection rule
```

Keep rejected candidates. They are required to estimate selection bias, search efficiency, and the contribution of lineage policies.

## 6. Repeat evaluation

Use multiple seeds or repeated trials whenever task execution or judging is stochastic. Report:

- sample count;
- mean or median as appropriate;
- uncertainty interval;
- task-level outcomes;
- paired differences when the same tasks are run by parent and successor;
- the number of candidates considered before selecting the winner.

Reevaluate accepted successors to reduce winner's-curse effects. A result smaller than evaluation noise should be treated as unresolved.

## 7. Test transfer

Select transfer axes that match the claim:

- new tasks from the same distribution;
- time-forward tasks;
- domain shift;
- another base model;
- another model scale;
- another harness;
- another evaluator;
- another tool or environment version.

Do not summarize these axes into one statement such as “generalizes.” Report the transfer matrix.

## 8. Attribute the gain

For model \(M\) and harness \(H\), evaluate the component cross:

\[
(M_0,H_0),\quad(M_1,H_0),\quad(M_0,H_1),\quad(M_1,H_1).
\]

Use analogous swaps for memory, tools, data, optimizer, and evaluator when those objects changed. If a component cannot be swapped, state the coupling and limit the attribution claim.

## 9. Measure regressions

Choose regression tasks before the improvement run. Report every task or capability that crosses a predefined loss threshold. Aggregate gains do not erase hard regressions.

Recommended outputs:

- per-task delta;
- per-domain delta;
- worst-case delta;
- cost and latency delta;
- calibration or reliability delta;
- failure-rate delta.

## 10. Test recursion

When recursion is claimed, run another improvement generation:

\[
S_0\xrightarrow{I_0}S_1\xrightarrow{I_1}S_2.
\]

Compare \(S_0\) and \(S_1\) as improvers under matched budgets. Measure:

- quality of proposed modifications;
- fraction of valid candidates;
- accepted gain on held-out tasks;
- improvement per unit cost;
- breadth of transfer;
- regressions;
- time to a useful successor.

A repeated outer loop does not establish recursion unless later systems improve these quantities.

## 11. Use independent acceptance tests

The candidate should not be able to modify the final acceptance test. When this is impossible, disclose the access and add an external evaluator. Self-generated tests are useful for search but cannot alone establish the final claim.

## 12. Publish a result bundle

A complete result bundle should contain:

```text
manifest.json
task_split.json
lineage.jsonl
resource_accounting.json
raw_results/
analysis script
environment lockfile or container specification
summary.md
```

The summary must distinguish author-reported results, direct reproduction, independent replication, and inference.
