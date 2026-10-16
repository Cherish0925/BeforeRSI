# Public research landscape

BeforeRSI is not an index of everything described as *self-improving*. The corpus is deliberately selective. A work belongs here when it materially constrains at least one of the following questions:

1. **What part of an AI system can be changed by the system or by an AI-driven improver?**
2. **Does the change persist beyond the task that generated it?**
3. **Does the gain transfer to untouched tasks, later time slices, other models, or other environments?**
4. **Does a successor become better at producing later successors?**
5. **Can the gain be separated from added compute, benchmark reuse, evaluator exploitation, or external intelligence?**
6. **Are the code, tasks, model versions, traces, and evaluation procedure public enough to inspect or reproduce?**

The machine-readable catalog in [`data/systems.json`](../data/systems.json) distinguishes four relations to RSI:

- **direct candidate** — persistent self-modification or self-improvement is central to the work;
- **precursor** — the work isolates a capability likely to matter for RSI but does not by itself establish recursive improvement;
- **adjacent** — the work optimizes AI programs, prompts, workflows, or scaffolds and supplies an important comparator, while the optimizer itself need not improve;
- **evaluation** — the work mainly supplies tasks, sandboxes, accounting, or comparison infrastructure.

Every empirical claim remains **reported** until it is independently rerun or reimplemented.

## Self-reference and executable self-modification

The clearest early line is the move from improving an external artifact to making the improver or agent itself part of the editable object.

- [STOP](https://github.com/microsoft/stop) ([paper](https://arxiv.org/abs/2310.02304), 2023) uses an LM-infused improver to improve its own improver program. The authors explicitly state that the language model itself is unchanged and therefore do not claim full RSI.
- [Promptbreeder](https://proceedings.mlr.press/v235/fernando24a.html) (2023/2024) evolves task prompts and the mutation prompts that generate later prompt mutations. It is an important bounded example of self-reference: the update rule is partly inside the search state, while the underlying model remains fixed.
- [Gödel Agent](https://github.com/Arvid-pku/Godel_Agent) ([ACL 2025](https://aclanthology.org/2025.acl-long.1354/)) allows an agent to modify its own logic and behavior rather than search within a fixed hand-written agent template.
- [SICA](https://github.com/MaximeRobeyns/self_improving_coding_agent) ([paper](https://arxiv.org/abs/2504.15228), 2025) evaluates an agent, lets it work on its own codebase, and then evaluates the modified successor. It is a useful reference because the parent–successor relation is explicit and the code is public.
- [Darwin Gödel Machine](https://github.com/jennyzzt/dgm) retains a population and lineage of self-modified coding agents rather than forcing a single greedy chain. The open question is whether lineage itself increases future transferable improvement under matched cost.
- [HGM](https://github.com/metauto-ai/HGM) moves the selection problem one level upward by estimating the future potential of branches or clades.
- [HyperAgents](https://github.com/facebookresearch/HyperAgents) places task agents and meta-agents inside a self-referential program space, making the meta-level program an explicit object of optimization.
- [AIDE²](https://arxiv.org/abs/2609.26457) is currently one of the strongest public multi-generation claims. The authors report an eight-day run with seven accepted research-agent rewrites and transfer to four held-out AI-R&D benchmarks. The technical report is public; a complete end-to-end reproduction package for the reported run has not been established by BeforeRSI.

The decisive measurement for this line is not the final task score. It is whether (S_{t+1}) is a better **improver** than (S_t), under matched budgets and untouched evaluation.

## Harness and persistent context

A second line keeps model weights fixed or separately versioned and changes the software around the model.

- [RRSI](https://github.com/google-research/rrsi) ([paper](https://arxiv.org/abs/2609.24972)) evolves prompts, control flow, context management, tools, skills, memory, and sub-agents while regularizing candidate proposals and selection against benchmark fitting, evaluation noise, and token-cost inflation.
- [Meta-Harness](https://github.com/stanford-iris-lab/meta-harness) gives the improver access to harness source code rather than a small prompt-only search space.
- [HSI](https://github.com/TailinZhou/hsi) includes parts of the search procedure and meta-evolver in the modifiable state, making transfer of the improvement procedure itself a central question.
- [ACE](https://github.com/ace-agent/ace) ([paper](https://arxiv.org/abs/2510.04618), ICLR 2026) treats context as a persistent, incrementally edited playbook. It is directly relevant to the question of whether durable capability can live outside model weights.
- [EvoHarness-RL](https://arxiv.org/abs/2608.05446) learns policies for constructing and using external harness state. Its current evidence is narrower than a general RSI claim, but it tests whether state-management behavior can migrate between the model policy and external harness over training.

Harness improvement is experimentally attractive because changed code and context can be inspected and swapped across models. It is also unusually vulnerable to benchmark-specific logic, hidden inference-cost increases, and compensation for weaknesses of one particular base model.

## Model-weight self-improvement and co-improvement

Model-weight updates require a different set of controls because training data, reward construction, optimizer behavior, and model capacity all change the interpretation of a gain.

- [SPIN](https://github.com/uclaml/SPIN) ([ICML 2024](https://proceedings.mlr.press/v235/chen24j.html)) iteratively trains a model against data generated by previous model iterations. It is a precursor to model-level RSI, but the update procedure itself is externally specified.
- [Self-Rewarding Language Models](https://proceedings.mlr.press/v235/yuan24d.html) (ICML 2024) use the model as a judge to produce training rewards and report simultaneous improvement in instruction following and judging. The unresolved issue is whether self-generated reward remains trustworthy as the system moves beyond the quality of its original external supervision.
- [SEAL](https://github.com/Continual-Intelligence/SEAL) makes self-generated model updates and update data explicit research objects.
- [OpenRSI](https://github.com/FrontisAI/OpenRSI), [MASS](https://github.com/SakanaAI/mass), and [SIA](https://github.com/hexo-ai/sia) couple model updates with harness, workflow, or search updates. These systems require component crossing:
  [
  (M_0,H_0),quad(M_1,H_0),quad(M_0,H_1),quad(M_1,H_1)
  ]
  because an end-to-end score cannot identify whether the gain lives in the model, the harness, or their local co-adaptation.

The most important unresolved empirical question is scale transfer: a method that repairs a weak model may become irrelevant, harmful, or qualitatively different on a stronger model.

## Environment-mediated improvement

Some systems learn from a simulator, world model, or task environment rather than a fixed benchmark table.

- [RSI-Anything](https://github.com/Gen-Verse/RSI-Anything) exposes propose–predict–select–evaluate–learn loops across heterogeneous environments.
- [Dream-RSI](https://github.com/zhengkid/Dream-RSI) uses replay or simulation of research trajectories to improve later search behavior.
- [ScienceBuddy](https://github.com/Gen-Verse/ScienceBuddy) couples a domain-specific research workspace with model and harness updates.
- [RSIGym](https://github.com/evolvent-ai/RSIGym) is included as evaluation infrastructure rather than as an RSI claim: separating task, sandbox, budget, and evaluation services is necessary for controlled comparisons.

These systems make one fact unavoidable: an improver can only become as meaningful as the feedback it receives. A successor that learns to exploit a simulator, learned world model, judge, hidden test convention, or cheap proxy may improve the measured objective while becoming worse at the intended task.

## Adjacent optimizers that must be strong baselines

Several influential systems optimize prompts, workflows, or agent programs without establishing that the optimizer itself improves. They belong in BeforeRSI because a claimed RSI method should beat them under matched cost.

- [ADAS](https://github.com/ShengranHu/ADAS) searches agent architectures.
- [AFlow](https://github.com/FoundationAgents/AFlow) searches agent workflows.
- [GEPA](https://github.com/gepa-ai/gepa) ([paper](https://arxiv.org/abs/2507.19457)) uses trajectory-level reflection and Pareto-aware evolution to optimize textual system parameters.
- [AgentBreeder](https://arxiv.org/abs/2502.00757) performs evolutionary search over multi-agent scaffolds.

A fixed optimizer repeatedly producing better target systems is useful automated optimization. It becomes evidence for recursion only when the successor improves the process that generates later successors.

## What is intentionally outside the core corpus

Automated theorem proving, algorithm discovery, code generation, hyperparameter optimization, model editing, retrieval augmentation, and test-time search are not included merely because an AI participates in an iterative loop. If the AI system itself does not acquire a persistent reusable change, the result is not self-improvement under BeforeRSI's working definition.

Likewise, projects are not promoted into the core corpus because they use the words *recursive*, *self-evolving*, or *autonomous*. A primary source must expose enough of the changed object, update process, evaluation, or artifacts to constrain a real RSI question.

## Coverage sources

BeforeRSI uses broad surveys to find candidate work, then returns to primary papers and repositories for claims.

- [The Path to Recursive Self-Improving Agents: Foundation, Framework, and Future Directions](https://github.com/D2I-ai/awesome-recursive-self-improving-agents) maintains a 2026 survey centered on model, harness, data, trainer, and improvement-process state.
- [Self-Improving Agents in the Era of Experience: A Survey of Self- to Meta-Evolution](https://github.com/FrontisAI/Awesome-Self-Improving-Agents) maintains a broad catalog spanning harnesses, skills, memory, RL, evaluation, and meta-evolution.
- The [ICLR 2026 Workshop on AI with Recursive Self-Improvement](https://openreview.net/pdf?id=OsPQ6zTQXV) is useful for identifying the range of definitions currently used by the field.

These are coverage sources, not substitutes for primary evidence.

## What public work still does not settle

As of October 2026, the public literature still does not establish all of the following in one system:

- sustained improvement over many generations without rapid saturation;
- broad transfer across unrelated task families;
- transfer of discovered improvements across substantially different model scales;
- a successor that is demonstrably better at producing later successors under equal improvement budgets;
- separation of model gain, harness gain, evaluator gain, and added compute;
- frontier-scale weight-level self-improvement with enough public artifacts for independent replication;
- stability of self-generated data and rewards over long training horizons;
- a general answer to whether recursive improvement becomes sublinear, linear, superlinear, oscillatory, or unstable as capability increases.

Private frontier-lab systems may contain stronger results, but unavailable experiments cannot settle public scientific questions. BeforeRSI records that uncertainty instead of extrapolating from absence or corporate claims.
