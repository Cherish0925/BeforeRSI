# Definitions under test

These definitions are operational proposals. They are meant to make claims comparable and falsifiable; they are not presented as a settled theory of RSI.

## System and improvement procedure

Let \(S_t\) be a versioned AI system. A complete description may include model parameters and architecture, harness code and configuration, persistent memory and tools, training or update procedures, and the external resources available during execution.

Let \(I_t\) be the procedure that proposes, implements, and selects changes. Given experience τ_t and improvement budget \(B_t\),

\[
S_{t+1}=I_t(S_t,\tau_t;B_t).
\]

The notation does not assume that the whole system changes. Most public systems modify only one subset.

## Test-time search or adaptation

A procedure spends additional resources on the current task and may produce a better answer, trajectory, plan, or temporary state. No persistent successor is required.

Examples include repeated sampling, tree search, reflection, debate, prompt repair, and task-local tool construction. These can be useful inputs to self-improvement, but they are not persistent self-improvement by themselves.

## Persistent self-modification

The AI system materially participates in producing a change that remains available to later tasks. The changed object may include weights, code, prompts, memory, tools, agent topology, data-selection rules, or the update procedure.

Persistence alone does not establish improvement.

## Self-improvement

A persistent self-modification that improves a stated utility under a stated evaluation budget and task distribution:

\[
\Delta_t(Q)=U_Q(S_{t+1};B_{\mathrm{eval}})-U_Q(S_t;B_{\mathrm{eval}})>0.
\]

The claim must specify \(Q\), \(B_{\mathrm{eval}}\), uncertainty, and regressions. A gain on the same tasks used to select the change supports only an in-distribution claim.

## Transferable self-improvement

A self-improvement whose gain persists outside the direct optimization setting. Transfer can be tested along several axes:

- unseen tasks from the same domain;
- time-separated tasks created after the update;
- distribution or domain shift;
- a different model family or model scale;
- a different harness or execution environment;
- a different evaluator.

Transfer is a vector, not a binary property. Every reported axis should be explicit.

## Recursive self-improvement

A sequence of self-improvements in which a successor improves the process that generates later successors.

Let \(G(I,S)\) measure the quality, breadth, reliability, or cost-adjusted rate of successors produced by improvement procedure \(I\) when operating on system \(S\). A recursive claim requires evidence such as

\[
G(I_{t+1},S_{t+1})>G(I_t,S_t),
\]

or a statistically supported positive trend across several generations.

Repeatedly applying a fixed external optimizer can yield an improving sequence \(S_0,S_1,…\) without recursive improvement. The recursive claim concerns the improvement capability itself.

## Open-ended recursive self-improvement

A process that continues to generate transferable improvements without a fixed finite menu of human-specified modifications and without rapid saturation on the target capability range.

No public result is assumed to establish this property. A credible claim would need long-horizon lineage, changing bottlenecks, broad transfer, controlled resource accounting, and evidence that progress is not supplied by repeated benchmark access or an unchanged stronger external model.

## Model-level RSI

Persistent improvement in model parameters, model architecture, optimizer, training data production, reward construction, curriculum, or training algorithm, with material participation by the AI system.

Updating weights is neither necessary nor sufficient for a model-level RSI claim. The update must improve the relevant capability, transfer, and—when recursion is claimed—improve later model-update capability.

## Harness-level RSI

Persistent improvement in the software surrounding a fixed or separately versioned model: prompts, context construction, memory, tools, skills, search, agent topology, control flow, validation, routing, or stopping rules.

Harness changes can produce large capability changes without changing weights. Their value depends on transfer, cost, robustness, and whether they survive stronger base models.

## System-level RSI

Coordinated improvement across multiple objects, such as model weights, harness, tools, memory, training procedures, and evaluator interfaces. System-level attribution requires component swaps or controlled ablations; an end-to-end score alone cannot identify where the gain resides.

## Adjacent research

The following areas can contribute to RSI but should not automatically be labeled RSI:

- automated prompt or workflow search;
- agent architecture search;
- continual learning;
- self-training and synthetic-data generation;
- automated machine learning;
- evolutionary program search;
- test-time scaling;
- memory and skill accumulation;
- model editing;
- automated curriculum generation.

BeforeRSI includes adjacent work when it changes what can be tested or built, while keeping its claim level explicit.
