# BeforeRSI

<div align="center">

<img src="assets/beforersi-hero.svg" width="100%" alt="BeforeRSI — recursive self-improvement needs a sharper test">

<br>

[![Status](https://img.shields.io/badge/status-research%20in%20progress-111827?style=flat-square)](#status)
[![Corpus](https://img.shields.io/badge/public%20corpus-38%20works-C58B35?style=flat-square)](EVIDENCE.md)
[![Claim depth](https://img.shields.io/badge/claim%20depth-D0%E2%86%92D4-5C9C96?style=flat-square)](#claim-depth)
[![CI](https://img.shields.io/github/actions/workflow/status/Cherish0925/BeforeRSI/validate.yml?branch=main&style=flat-square&label=data)](https://github.com/Cherish0925/BeforeRSI/actions)
[![License](https://img.shields.io/badge/license-MIT-6B7280?style=flat-square)](LICENSE)

**[Research map](MAP.md)** · **[Evidence](EVIDENCE.md)** · **[Program](PROGRAM.md)** · **[Evaluation](EVALUATION.md)** · **[Experiments](experiments/)**

</div>

---

## What must be true before RSI is real?

**BeforeRSI** studies one question:

> When can we say that an AI system has improved its own capacity to improve?

A better answer after more sampling is not enough. A benchmark score obtained after repeated access to the benchmark is not enough. A fixed optimizer producing a better prompt or workflow is not enough. A model and harness updated together are not interpretable unless their contributions can be separated.

The object of study is a versioned AI system:

$$
S_t=(M_t,H_t,I_t,D_t,E_t),
$$

where **M** is the model, **H** the harness, **I** the improver, **D** persistent experience and training data, and **E** the task environment. A separate acceptance process $V^*$ decides whether a candidate becomes the next version.

<div align="center">
<img src="assets/rsi-mainline.svg" width="96%" alt="BeforeRSI research spine">
</div>

The central empirical target is stronger than task performance:

$$
S_t \xrightarrow{I_t} S_{t+1}
\qquad\text{and then}\qquad
S_{t+1}\ \text{must be a better improver than}\ S_t.
$$

That second statement is where most public evidence becomes thin.

## The research spine

The history of self-improving AI is easiest to understand as five streams that now meet:

| Stream | What it contributed | What remains unresolved |
|---|---|---|
| **Self-reference** | programs and agents that can modify their own executable description | whether self-reference produces transferable improvement rather than bounded self-editing |
| **Search** | evolutionary search, program synthesis, prompt/workflow optimization | whether the optimizer itself improves, rather than only its target |
| **Learning to learn** | meta-learning, self-play, self-training, self-generated rewards | whether repeated weight updates remain reliable and useful as models become stronger |
| **External cognition** | memory, tools, skills, context, agent control, harnesses | where durable capability should live and whether harness gains transfer across models |
| **Verification** | exact checks, learned judges, hidden tasks, selection under uncertainty | how to prevent benchmark fitting, evaluator exploitation, and metric drift |

The current technical frontier is their intersection: **model–harness–improver co-evolution under protected evaluation**.

Read the full historical and causal map in **[MAP.md](MAP.md)**.

## Claim depth

BeforeRSI does not classify whole projects as “RSI” or “not RSI.” It asks what a specific experiment actually establishes.

| Level | Claim | Minimum observation |
|---|---|---|
| **D0** | task-time adaptation | better current-task output; no persistent successor required |
| **D1** | persistent self-modification | a versioned change survives into later tasks |
| **D2** | transferable self-improvement | the change improves untouched tasks, models, environments, or cost |
| **D3** | recursive self-improvement | the successor produces better later successors under the same improvement budget |
| **D4** | open-ended RSI | D3 persists as tasks and bottlenecks change, without rapid saturation |

A technically useful D0 or D1 result remains useful. The problem is claiming D3 or D4 without the corresponding observation.

## What the public record says now

The strongest public work has already established several pieces of the puzzle:

- **persistent capability can live outside weights** — prompts, context, memory, tools, workflows and executable agent code can materially change a fixed model's realized capability;
- **self-modification can be executable** — agents can inspect, edit, test and retain changes to their own software;
- **model updates can be self-generated** — self-training, self-generated rewards and AI-generated update data can improve model behavior in bounded settings;
- **model and harness can be improved together** — recent systems expose both as editable objects and begin to test component transfer;
- **selection quality is a first-class constraint** — hidden tasks, cost accounting, lineage and independent acceptance materially change what counts as an improvement.

What is **not** yet established publicly is equally important: sustained broad transfer over many generations, frontier-scale weight-level recursion with reproducible artifacts, and a successor that repeatedly becomes better at producing later successors under matched resources.

The source-backed record is in **[EVIDENCE.md](EVIDENCE.md)** and the machine-readable corpus is in **[data/works.json](data/works.json)**.

## The system we actually want to test

A credible route to general RSI cannot optimize only one layer forever. The working program is:

$$
H_t
\rightarrow D_t^{\mathrm{verified}}
\rightarrow M_{t+1}
\rightarrow H_{t+1}
\rightarrow I_{t+1}.
$$

1. improve a **portfolio of harnesses** around a fixed model;
2. collect matched trajectories and verify them independently;
3. update the model from evidence-bearing trajectories rather than undifferentiated logs;
4. cross old/new models with old/new harnesses to locate the gain;
5. rebuild the harness around the new model instead of assuming the old optimum remains optimal;
6. improve the improver using candidate lineage, failed hypotheses and transfer results;
7. compare parent and successor **as improvers** on a new improvement problem;
8. repeat only while held-out gain survives cost, regression and contamination controls.

The detailed design is in **[PROGRAM.md](PROGRAM.md)**.

## Three experiments before stronger claims

<table>
<tr>
<td width="33%" valign="top">

### 01 · Harness transfer

Does an evolved harness still win after the parent receives the same total compute?

[Protocol →](experiments/001-harness-transfer.md)

</td>
<td width="33%" valign="top">

### 02 · Model × Harness

Evaluate the full cross:

(M0,H0) · (M1,H0) · (M0,H1) · (M1,H1)

[Protocol →](experiments/002-model-harness-cross.md)

</td>
<td width="33%" valign="top">

### 03 · Successor as improver

Under the same improvement budget, does $S_1$ produce a better descendant than $S_0$?

[Protocol →](experiments/003-successor-as-improver.md)

</td>
</tr>
</table>

These experiments are ordered. Experiment 03 is the first direct test of the word **recursive**.

## What this repository rejects

BeforeRSI does not upgrade a result because its title contains *recursive*, *self-evolving*, *autonomous* or *self-reflective*. The following are insufficient on their own:

- extra samples, retries, agents or evaluator calls;
- a fixed outer optimizer repeatedly improving a target;
- benchmark-specific prompt or workflow patches;
- self-generated data with an unchanged training rule;
- joint model/harness updates without component crossing;
- one successful parent → child update described as recursion;
- gains demonstrated only on small models and extrapolated to frontier models;
- self-evaluation used as the sole acceptance test.

These methods may be useful components or strong baselines. **[EVALUATION.md](EVALUATION.md)** specifies what stronger claims require.

## Repository

| File | Purpose |
|---|---|
| **[MAP.md](MAP.md)** | history, causal structure, knowledge tree and present frontier |
| **[EVIDENCE.md](EVIDENCE.md)** | strongest public work, claim depth, limitations and primary sources |
| **[PROGRAM.md](PROGRAM.md)** | target system, model–harness–improver co-evolution and research sequence |
| **[EVALUATION.md](EVALUATION.md)** | hidden/time-forward tests, cost controls, attribution, regression and recursion tests |
| **[data/works.json](data/works.json)** | machine-readable public research corpus |
| **[data/knowledge-graph.json](data/knowledge-graph.json)** | machine-readable causal knowledge graph |
| **[experiments/](experiments/)** | executable discriminating experiments |

The repository stays small on purpose. New files are added when they contain a new source audit, a testable claim, an experiment, or a result.

## Status

**October 2026.** The historical map and experimental program are established; the corpus is still being audited claim by claim. Author-reported results remain labeled reported until they are independently rerun or replicated.

The immediate work is deliberately narrow:

**audit → reproduce → transfer → attribute → test the successor as an improver → repeat.**

---

<div align="center">
<sub>BeforeRSI asks for stronger evidence before stronger words.</sub>
</div>
