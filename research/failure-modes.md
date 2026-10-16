# Failure modes and confounders

An apparent self-improvement can be produced without a transferable increase in capability. The following alternatives should be tested before accepting a strong RSI claim.

## Improvement-set overfitting

The system repeatedly observes the same tasks, tests, traces, or evaluator feedback and acquires benchmark-specific behavior. In-distribution scores rise while held-out gains shrink or disappear.

Controls: hidden tasks, time-separated tasks, task-generation audits, contamination checks, and explicit exposure logs.

## Additional-compute substitution

The successor uses more samples, longer context, more agents, more tool calls, or more evaluator queries. The gain may come entirely from spending more resources.

Control: give the parent the same total compute, including the compute spent creating the successor when the claim concerns cost-adjusted improvement.

## Evaluator exploitation

The successor learns features that raise the measured score without improving the intended capability. This includes test leakage, reward-model exploitation, output-format tricks, verifier bugs, and manipulating self-generated tests.

Controls: independent evaluators, hidden tests, evaluator ensembles with known limitations, adversarial cases, and manual inspection of high-impact deltas.

## Selection noise

A candidate is accepted because of evaluation variance. Repeating this over many candidates creates a winner's-curse effect even when no candidate is better.

Controls: repeated trials, uncertainty intervals, sequential tests, correction for the number of candidates, and reevaluation of accepted versions.

## Capability redistribution

A successor gains on the target domain while losing unrelated capabilities. A single aggregate score hides the exchange.

Controls: per-domain results, hard regression thresholds, Pareto reporting, and evaluation on capabilities that were not optimized.

## Local co-adaptation

A model, harness, tool set, and evaluator become mutually specialized. The paired system improves, but components do not transfer to other versions.

Controls: component swaps, cross-model harness tests, cross-harness model tests, and cross-generation compatibility matrices.

## Small-model artifact

A method succeeds because a weak model has obvious, cheaply repairable defects. The same method can vanish or reverse on a stronger model.

Controls: several model scales and families, absolute and relative gains, and tests of whether the improvement procedure itself changes with scale.

## External-intelligence substitution

A stronger fixed model, human-written test suite, curated data source, or external optimizer supplies the useful innovation. The target system executes the update but does not materially contribute to discovering it.

Control: document every source of candidate generation, labels, tests, and selection. Remove or weaken the external source and measure what remains.

## Fixed-improver iteration

A fixed external procedure repeatedly improves successive systems. The sequence improves, but the ability to improve does not.

Control: evaluate whether later successors propose, select, or implement better modifications under the same outer procedure and budget.

## Memory accumulation without abstraction

The system retains more traces or facts and performs better on related tasks through retrieval. Storage grows, but the system does not acquire a more general strategy.

Controls: memory-size-matched baselines, transfer to structurally different tasks, compression tests, and deletion or substitution of retrieved items.

## Synthetic-data collapse

Self-generated training data narrows diversity, amplifies errors, or reinforces the current policy. Short-run target gains can coexist with long-run degradation.

Controls: generation-by-generation diversity measures, external reference data, calibration, error amplification tests, and unrelated-capability checks.

## Search-space restriction

The improvement method appears efficient because humans supplied a narrow menu containing effective changes. Results may not transfer to an open edit space.

Control: report the editable surface, human priors, forbidden changes, and the fraction of useful candidates discovered outside hand-designed templates.

## Infrastructure drift

Model endpoints, dependencies, datasets, tool versions, or evaluator services change during an experiment. The observed delta is then partly environmental.

Controls: pinned versions, archived task data, immutable containers when possible, timestamps, raw outputs, and reruns of the parent in the same evaluation window.

## Publication filtering

Public work disproportionately reports successful domains, seeds, and generations. Failed self-improvement runs are often absent.

Controls: publish all attempted runs, stopping rules, candidate counts, rejected lineages, and predeclared primary metrics.
