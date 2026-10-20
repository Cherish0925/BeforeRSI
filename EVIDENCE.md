# Evidence and judgment

[English](EVIDENCE.md) · [简体中文](docs/zh/EVIDENCE.md)

This document separates scientific value from the label attached to a project. A work can be useful without being RSI. A work can also contain a genuine result while making a broader claim than its evidence supports.

## 1. The evidence test

For a claimed update $S_t\rightarrow S_{t+1}$, ask seven questions:

1. **What changed?** Response, prompt, memory, tool, harness code, model weights, optimizer, evaluator, or improver.
2. **What supplied the change?** The system itself, a stronger fixed model, human engineering, search, or hidden tests.
3. **What persisted?** Did a versioned successor survive beyond the current task?
4. **What transferred?** Same benchmark, held-out rows, time-forward tasks, new domains, new model families, or new environments.
5. **What was the matched baseline?** Parent with equal inference, search, training, and evaluator budget.
6. **What regressed?** Task-level failures, cost, latency, reliability, calibration, or unrelated capabilities.
7. **Did the successor improve later improvement?** Was $S_{t+1}$ compared with $S_t$ as an improver?

A paper that does not answer the last question may establish self-improvement. It does not establish recursion.

## 2. What the historical branches establish

### Good and the intelligence-explosion argument

**Value:** identifies the possibility that machine-design ability could create positive feedback.

**Established:** a qualitative argument.

**Unestablished:** a realizable update process, a growth law, evaluator stability, and whether improvement accelerates rather than saturates.

Treating Good’s argument as a prediction confirmed by current agents is unsupported.

### EURISKO

**Value:** early evidence that heuristic rules can be represented as editable objects and that a system can generate heuristics affecting later search.

**Established:** self-modification of heuristics in bounded, hand-engineered representations.

**Unestablished:** scalable transfer, reproducibility under modern standards, model-level learning, and sustained improvement of the improver.

EURISKO is historically central. It is not evidence that modern open-ended RSI has already occurred.

### Gödel machines

**Value:** the cleanest formal statement of self-reference, utility-preserving self-rewrite, and modification of the proof searcher itself.

**Established:** conditional theoretical properties under the encoded axioms and proof requirements.

**Unestablished:** tractable discovery of useful proofs in realistic AI systems.

The work is conceptually important and operationally distant from current LLM agents.

## 3. Strong adjacent work that should not be called RSI by default

### Meta-learning and self-play

MAML, AlphaGo Zero, and related work establish that learning behavior can be shaped across tasks and that self-generated experience can produce capabilities beyond supervised imitation. Their objectives, update algorithms, and acceptance rules remain externally specified.

They answer “can a system learn to adapt?” They do not by themselves answer “can a successor improve the procedure that creates later successors?”

### AutoML and algorithm search

AutoML-Zero, FunSearch, AlphaEvolve, and similar systems automate parts of algorithm discovery. Their output can be scientifically or commercially valuable. The optimizer generally remains fixed while it improves an external artifact.

These systems are essential baselines for automated AI research. Calling every successful algorithm-search loop RSI erases the distinction between improving a target and improving the improver.

### Prompt, workflow, and agent search

ADAS, AFlow, GEPA, AgentBreeder, OPRO-like methods, and prompt optimizers can discover better agent configurations. They belong in BeforeRSI when they provide a strong comparison or expose transferable design principles.

Their default claim depth is D0 or D1. They reach D2 only after untouched transfer. They reach D3 only if the improved system becomes a better generator of later improvements.

## 4. Direct modern evidence

### STOP and Promptbreeder

These works are important because the update rule enters the editable state.

- STOP improves an improver program while leaving the underlying language model fixed.
- Promptbreeder evolves both task prompts and mutation prompts that generate future mutations.

They demonstrate bounded self-reference. Their evidence does not establish broad, multi-generation system improvement.

### Gödel Agent and SICA

These systems make executable agent code editable. The parent–successor relation is concrete, and modifications can affect future tasks.

The main limitations are benchmark concentration, dependence on a strong fixed model and evaluator, small numbers of generations, and limited cross-model transfer. They establish a route to persistent self-modification. General RSI remains unestablished.

### Darwin Gödel Machine and HGM

DGM contributes open lineage: unsuccessful or non-incumbent branches can later become useful ancestors. HGM raises parent selection to the level of future branch potential.

The scientific question is whether lineage and clade selection improve future transferable gain under matched cost. A richer archive can outperform greedy search simply by spending more evaluation. The comparison must control candidate count, evaluator exposure, and total compute.

### HyperAgents and HSI

Both place meta-level procedures inside editable code. [HyperAgents](https://arxiv.org/html/2603.19461v1) explicitly tests cross-domain improvement capability with imp@k; its short-budget transfer result is positive, while the longer compounding comparison is not statistically significant. HSI's separate harness/evolver updates require their own transfer analysis. These are different evidence records.

### AIDE²

[AIDE²](https://arxiv.org/html/2609.26457v1) reports repeated improvements to a research agent under a fixed outer researcher, with transfer to external AI-R&D benchmarks. Its separate ignition test asks whether a successor can replace that researcher: three seeds per arm finish at means 0.780 and 0.782, an inconclusive comparison. The study supports research-harness improvement; successor takeover has not established higher improvement efficiency.

### RRSI, Meta-Harness, RHI, and related harness systems

Harness evolution has produced the clearest inspectable gains around frozen models. RRSI explicitly addresses edit size, benchmark-specific logic, evaluation noise, token cost, and pruning. Meta-Harness exposes full source code. RHI and related methods optimize task-specific harness specifications from trajectory feedback.

The strongest limitation is portability. A harness can encode task-family structure, compensate for one model’s defects, or alter resource use. Transfer across a few related benchmarks does not imply a universal harness improvement.

### Harness Updating Is Not Harness Benefit

This result is central because it splits a vague capability into two measurable ones:

- producing a useful harness update;
- exploiting the updated harness during task execution.

The reported non-monotonic relation between base-model strength and harness benefit directly contradicts the simple belief that a stronger model will always gain more from harness evolution. It motivates separate evolver and executor models, cross-model transfer matrices, and scale-dependent experiments.

## 5. Model-level self-improvement

### SPIN and iterative self-training

SPIN shows that a model can improve through iterative interaction with previous versions under an externally specified training procedure.

The main uncertainty is long-run information quality. If each generation learns mainly from the distribution already represented by earlier generations, gains can saturate and rare capabilities can disappear. External data, verifiers, or environment interaction may be necessary to keep the loop informative.

### Self-Rewarding Language Models

These systems use the model to generate reward or preference labels and update the model from them. They test whether task ability and judging ability can improve together.

The central risk is correlated error: the same model family can make and approve the same mistake. Final evaluation must be independent of the self-generated reward process.

### SEAL and self-generated updates

SEAL makes the content of model updates an output of the model. This is closer to model-level self-improvement than ordinary self-training.

A recursive claim still requires repeated generations, cross-task transfer, retention of unrelated abilities, and evidence that later systems construct better updates.

## 6. Model–harness co-evolution

Co-Harness, OpenRSI, MASS, SIA and related work study model–system adaptation with different update schedules. [HELIX](https://arxiv.org/html/2608.13951v1) contributes harness composition and verified training records; Section 9.5 states that it does not train an updated model. Its build–update–rebuild cycle is a proposed continuation, not a completed weight-update experiment.

The core loop is sound:

$$

H_t \rightarrow D_t^{\text{verified}}
\rightarrow M_{t+1}
\rightarrow H_{t+1}.

$$

Current public evidence is early. Common limitations include one-round demonstrations, task-specific evaluators, incomplete $M\times H$ crossing, no time-forward tasks, and no comparison of parent and successor as improvers.

The direction deserves priority because it can combine cheap external adaptation with durable parameter learning. It should not be described as solved RSI until the repeated loop is measured.

## 7. Evaluation results that change the research program

### Matched-compute evaluation

Rethinking the Evaluation of Harness Evolution shows why harness search must be compared with simple task-level search under the same feedback and inference budget. Without this comparison, a persistent harness may merely amortize extra search rather than create a better algorithm.

### Statistical selection limits

Repeated candidate search creates winner’s curse and adaptive overfitting. Small gains selected from many noisy evaluations are unreliable even when the final benchmark was nominally held out.

### Harness tampering

An editable harness can alter logging, provenance, parsing, task coverage, authorization, or evaluation behavior. Apparent gains can therefore result from changing what is measured or recorded. The final acceptance path and evidence log require protection outside the editable surface.

### Scale dependence

Public evidence indicates that harness gains can be non-monotonic with base-model strength. Weak models may fail to follow a useful harness; strong models may already implement the strategy internally or be constrained by the harness. Any claimed general method needs a model-scale curve rather than one endpoint.

## 8. Claim patterns with low RSI value

The following patterns should not occupy the center of the repository.

### Reflection without persistence

The system critiques or revises its current answer but retains no reusable change. This is task-time computation.

### Best-of-$N$ presented as learning

A system samples many candidates and keeps the best output. Unless the selected information changes later behavior, no successor was created.

### Benchmark editing

A prompt, tool, or code patch exploits repeated exposure to a fixed suite. Large in-distribution gain with weak untouched transfer is task fitting.

### Compute hidden inside the harness

More retries, longer context, extra sub-agents, or more evaluator calls are counted as “architecture improvement” without matched total cost.

### Single-generation recursion

A parent produces one better child, and the work is called recursive. One persistent update is D1; transfer is D2; recursion requires comparison of parent and child as improvers.

### Joint update without attribution

Model and harness are updated together and only the paired endpoints are tested. The source of gain and co-adaptation cannot be determined.

### Self-approval

The same model generates, judges, and accepts an update with no independent final test. Correlated error and reward hacking remain uncontrolled.

### Tiny-model proof by extrapolation

A method works on a small model or toy environment and is presented as a route to frontier RSI without a scale-transfer experiment.

### Vocabulary in place of evidence

New names for loops, roles, memories, or agent layers do not change the scientific state unless they enable a new capability, prediction, or controlled result.

These patterns are not always useless. They are weak evidence for RSI.

## 9. Current evidence boundary

As of October 2026, public work supports the following statement:

> AI systems can participate in producing persistent changes to prompts, context, memory, tools, harness code, agent programs, training data, rewards, and model weights. Some changes transfer to held-out tasks, and several systems report short multi-generation improvement.

Public work does not yet support this stronger statement:

> A general AI system repeatedly improves its model, harness, and improvement process; the successors become better improvers; gains transfer broadly across tasks and scales; and the process remains stable over many generations.

BeforeRSI is organized around closing the gap between these two statements.
