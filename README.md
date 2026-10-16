# BeforeRSI

**What must be established before an AI system can be said to improve its own capacity to improve?**

BeforeRSI is a research map, evidence ledger, and experimental program for recursive self-improvement in AI models, harnesses, and complete AI systems.

The repository is organized around one sequence:

\[
S_0 \xrightarrow{I_0,V^\*} S_1
\xrightarrow{I_1,V^\*} S_2
\xrightarrow{I_2,V^\*} \cdots
\]

\(S_t\) is a versioned AI system. \(I_t\) proposes and implements changes. \(V^\*\) is a protected acceptance process that the candidate cannot freely rewrite. A higher task score is insufficient. Three distinct claims must be separated:

1. **Persistent self-modification:** the system participates in producing a change that survives into later tasks.
2. **Transferable self-improvement:** the successor is better on untouched tasks or achieves the same result at lower total cost.
3. **Recursive self-improvement:** the successor produces better later successors than its parent under a matched improvement budget.

Most work called “self-improving AI” establishes only part of this sequence.

## The main conclusion

The historical path to RSI has five branches:

- self-reference and formal self-modification;
- heuristic, evolutionary, and program search;
- meta-learning, self-play, and self-training;
- external memory, tools, skills, and harnesses;
- evaluators, verifiers, and selection under uncertainty.

The branches now converge on a system-level target:

\[
S_t=(M_t,H_t,I_t,D_t,E_t),
\]

where \(M\) is the model, \(H\) the harness, \(I\) the improver, \(D\) persistent experience and training data, and \(E\) the task environment. The acceptance process \(V^\*\) is kept separate because an editable evaluator can turn genuine improvement into metric drift or tampering.

The strongest plausible route is repeated **model–harness–improver co-evolution**:

\[
H_t \rightarrow \text{verified trajectories}
\rightarrow M_{t+1}
\rightarrow H_{t+1}
\rightarrow I_{t+1}.
\]

This route is still unproven. Public systems show useful one-step and short multi-generation gains, mainly in coding, benchmarked agent work, and bounded post-training. Public evidence does not yet establish sustained broad transfer, frontier-scale model-level recursion, or an improving rate of improvement over many generations.

## The map

[MAP.md](MAP.md) gives the historical tree, causal graph, present frontier, and the exact point at which adjacent fields become evidence for RSI.

[EVIDENCE.md](EVIDENCE.md) states what the strongest public work establishes, what it leaves unresolved, and which common claims do not count as RSI evidence.

[PROGRAM.md](PROGRAM.md) specifies the research program for model–harness co-evolution, including system state, update order, lineage, attribution, scaling tests, and the sequence of experiments.

[EVALUATION.md](EVALUATION.md) defines the acceptance standard: hidden and time-forward tasks, matched compute, cross-component swaps, tampering checks, regression limits, and successor-as-improver tests.

## Claim depth

BeforeRSI uses a five-level claim scale:

| Level | Claim | Required observation |
|---|---|---|
| **D0** | Task-time search or adaptation | Better current-task output; no persistent successor required |
| **D1** | Persistent self-modification | A versioned change survives into later tasks |
| **D2** | Transferable self-improvement | The change improves untouched tasks, models, environments, or cost |
| **D3** | Recursive self-improvement | The successor generates better later successors under matched budget |
| **D4** | Open-ended RSI | D3 persists across changing tasks and bottlenecks without rapid saturation |

A paper can be technically valuable at D0 or D1. It should not be presented as D3 or D4 without the corresponding experiment.

## Current judgment

The public literature supports four conclusions.

**First, useful persistent change can live outside model weights.** Prompt, memory, tool, workflow, and source-code changes can materially alter a fixed model’s realized capability.

**Second, harness updating and harness benefit are separate abilities.** A model may produce a useful update that another model can exploit better. Stronger base models do not necessarily receive larger gains from a given harness update.

**Third, benchmark improvement is heavily confounded.** Additional inference, repeated benchmark feedback, winner selection, evaluator exploitation, and task-specific compensation can all imitate reusable improvement.

**Fourth, model–harness co-evolution is the correct system boundary, but current public work has not closed the full loop repeatedly.** One round of harness search followed by one model update is evidence about co-adaptation; it is not yet evidence of sustained recursive improvement.

## What this repository excludes

BeforeRSI does not classify a project as RSI because it uses words such as *recursive*, *self-evolving*, *autonomous*, or *self-reflective*. The following are adjacent unless they produce a persistent, transferable successor:

- repeated sampling, reflection, debate, or tree search;
- automated prompt or workflow search by a fixed external optimizer;
- algorithm discovery whose output does not improve the producing system;
- synthetic-data training with a fixed update procedure;
- benchmark-specific prompt patches;
- more agents, tokens, retries, or evaluator calls without matched-cost controls.

These methods can be strong baselines or necessary components. The distinction concerns the claim, not their engineering usefulness.

## Repository structure

```text
BeforeRSI/
├── README.md
├── MAP.md
├── EVIDENCE.md
├── PROGRAM.md
├── EVALUATION.md
├── data/
│   ├── works.json
│   ├── works.schema.json
│   └── knowledge-graph.json
├── experiments/
│   ├── 001-harness-transfer.md
│   ├── 002-model-harness-cross.md
│   └── 003-successor-as-improver.md
├── scripts/
│   └── validate.py
└── .github/workflows/
    └── validate.yml
```

The corpus is selective. Entries are retained because they establish a necessary capability, provide direct RSI evidence, supply a strong baseline, or expose a failure mode that changes the research program.

## Evidence labels

- `reported`: stated by the original authors;
- `reproduced`: public artifacts were rerun with materially matching results;
- `replicated`: an independent implementation supports the same conclusion;
- `contradicted`: a controlled result conflicts with the claim;
- `open`: available evidence does not decide the claim.

No author-reported result is silently upgraded to independent evidence.

## Immediate work

The next useful work is not another broad survey. It is a sequence of controlled experiments:

1. reproduce one inspectable harness-evolution system;
2. compare it with the parent under equal total compute;
3. transfer the change across tasks and model families;
4. cross parent and successor models with parent and successor harnesses;
5. run a second improvement generation and compare the parents as improvers;
6. update model weights from verified harness-generated trajectories;
7. rebuild the harness for the updated model and repeat.

The repository will be judged by whether these experiments change what is known about transfer, attribution, scaling, and recursion.
