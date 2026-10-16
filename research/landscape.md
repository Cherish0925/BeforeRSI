# Public research landscape

This document maps public systems by the object they change and the claim that still needs to be tested. It is not a leaderboard. Descriptions are based on the linked repositories and their authors' public materials. Every result remains `reported` until BeforeRSI or another independent group reproduces it.

## Automated agent and workflow search

These systems establish that an outer model or search procedure can generate useful agent programs or workflows. Their relation to RSI depends on persistence, transfer, and whether the improver itself changes.

| Project | Public object | Primary changed object | BeforeRSI question |
|---|---|---|---|
| [ADAS](https://github.com/ShengranHu/ADAS) | Code and experiments | Agent architecture | Does the discovered architecture transfer across task families and model strengths under equal compute? |
| [AFlow](https://github.com/FoundationAgents/AFlow) | Code and experiments | Agentic workflow | Is the gain reusable beyond the optimization benchmark, and does the workflow generator itself improve? |

These projects are important adjacent work. Automated design of a target agent does not establish recursion when the outer designer remains fixed.

## Self-referential programs and self-modifying agents

| Project | Public object | Primary changed object | BeforeRSI question |
|---|---|---|---|
| [STOP](https://github.com/microsoft/stop) | Code for a self-taught optimizer | Improver program | Does self-editing improve the optimizer beyond one bounded task setting, and does the gain survive stronger fixed baselines? |
| [Gödel Agent](https://github.com/Arvid-pku/Godel_Agent) | Self-referential agent code | Agent logic / code | Which changes transfer, and how much of the gain comes from the fixed base model and evaluator? |
| [Darwin Gödel Machine](https://github.com/jennyzzt/dgm) | Self-modifying coding-agent search | Agent code and lineage | Does open-ended lineage produce better descendants than ordinary best-first or evolutionary search under matched cost? |
| [HGM](https://github.com/metauto-ai/HGM) | Lineage-aware self-improvement | Parent and branch selection | Can estimated future potential select lineages that produce broader later gains? |
| [HyperAgents](https://github.com/facebookresearch/HyperAgents) | Self-referential task and meta-agents | Agent and meta-agent programs | Does meta-level self-reference improve later optimization across unrelated computable tasks? |

The central missing measurement for this track is usually cross-generation improvement ability rather than target-task score alone.

## Harness self-improvement

A harness includes prompts, context construction, tools, memory, search, sub-agents, control flow, validation, and stopping rules around a base model.

| Project | Public object | Primary changed object | BeforeRSI question |
|---|---|---|---|
| [RRSI](https://github.com/google-research/rrsi) | Regularized harness evolution code and task adapters | Harness | How much of the reported out-of-distribution gain survives independent reruns, new time slices, and stronger base models? |
| [Meta-Harness](https://github.com/stanford-iris-lab/meta-harness) | Code-level harness modification | Harness source code | Does full-source modification outperform restricted search after equalizing candidate and evaluation cost? |
| [HSI](https://github.com/TailinZhou/hsi) | Harness and meta-level search | Harness plus parts of the search procedure | Do changes to the meta-level procedure transfer to a second improvement problem? |

Harness work offers the clearest near-term tests because changes are inspectable and can be swapped across models. It also faces severe benchmark overfitting and compute-accounting confounds.

## Model and system co-improvement

| Project | Public object | Primary changed object | BeforeRSI question |
|---|---|---|---|
| [OpenRSI](https://github.com/FrontisAI/OpenRSI) | Model-training and system-evolution components | Model plus search system | Are model and system gains additive, synergistic, or tied to one benchmark distribution? |
| [MASS](https://github.com/SakanaAI/mass) | Multi-agent search and model post-training | Model plus multi-agent workflow | Which domains improve, which regress, and what transfers when model and workflow versions are crossed? |
| [SIA](https://github.com/hexo-ai/sia) | Joint self-improvement implementation | Model plus harness | Does the controller select the right update object outside the tasks used to train or tune it? |
| [SEAL](https://github.com/Continual-Intelligence/SEAL) | Self-generated model updates and data | Model weights / update data | Does self-edit generation remain beneficial across model scale, task shift, and repeated generations? |

This track is closest to model-level RSI and the hardest to attribute. Every strong result needs component swaps, training-compute controls, and unrelated-capability tests.

## Environment-mediated and simulated improvement

| Project | Public object | Primary changed object | BeforeRSI question |
|---|---|---|---|
| [RSI-Anything](https://github.com/Gen-Verse/RSI-Anything) | Multi-domain propose-predict-select-evaluate loop | Policy, world model, and system state | Can an improvement strategy learned in one environment transfer to structurally different environments? |
| [Dream-RSI](https://github.com/zhengkid/Dream-RSI) | Research-tree replay and simulated improvement | Research or search policy | When does simulated improvement predict real improvement rather than simulator exploitation? |
| [ScienceBuddy](https://github.com/Gen-Verse/ScienceBuddy) | Domain-specific scientific self-improvement workspace | Research harness and model updates | Which results generalize beyond the scientific task and evaluator used by the system? |

These systems expose a decisive issue: the environment supplies the feedback that defines improvement. A weak or exploitable environment can produce confident but non-transferable successors.

## Evaluation infrastructure

| Project | Public object | Primary changed object | BeforeRSI question |
|---|---|---|---|
| [RSIGym](https://github.com/evolvent-ai/RSIGym) | Task, sandbox, budget, and evaluation infrastructure | Evaluation boundary | Which protocols reliably distinguish reusable improvement from task fitting and added compute? |

Evaluation is not a secondary component. Without hidden tasks, resource accounting, and versioned lineage, the field cannot compare systems or determine whether recursion occurred.

## Evidence state

BeforeRSI uses claim-level statuses:

- `reported`: stated by the original authors or repository;
- `reproduced`: public artifacts were rerun with materially matching results;
- `replicated`: an independent implementation supports the same conclusion;
- `contradicted`: a controlled result conflicts with the claim;
- `open`: available evidence does not decide the claim.

The machine-readable catalog in [`data/systems.json`](../data/systems.json) records public repositories and preliminary classifications. It deliberately does not copy benchmark numbers until the exact task split, budget, evaluator, and reproduction status have been recorded.

## Missing public evidence

Public evidence is concentrated on coding agents, benchmarked workflows, and small-to-medium post-training experiments. Frontier-scale model improvement inside major laboratories is largely unavailable for independent inspection. This limits what can be concluded about scaling. It does not justify assuming either that general RSI has been achieved privately or that it is impossible.
