# Research principles

BeforeRSI treats recursive self-improvement as a scientific question whose answer is currently unknown.

1. **Name the changed object.** State whether the update changes weights, architecture, prompts, context construction, memory, tools, code, agent topology, data selection, optimizer state, training procedure, evaluator, or another component.

2. **Name the improver.** Identify the model, program, human input, search process, or mixed procedure that proposes, implements, and selects the change. A system has not improved itself merely because an automated pipeline changed it.

3. **Account for compute.** Report training and inference tokens, samples, evaluator calls, wall-clock time, accelerator time, API cost, and external tool use. Compare against the parent system given the same total resources.

4. **Measure persistence.** The changed system must remain available to later tasks. Temporary reasoning traces and one-task search results count as test-time computation unless they alter a persistent successor.

5. **Measure transfer.** Separate gains on the improvement distribution from gains on untouched tasks, later time slices, different environments, and different model families.

6. **Measure regressions.** Report task-level or domain-level losses. A scalar average can conceal the destruction of useful capabilities.

7. **Test recursion directly.** A recursive claim requires evidence that a successor produces later improvements more effectively. Repeated execution of an unchanged outer procedure is insufficient.

8. **Preserve lineage.** Record parent versions, candidate changes, rejected candidates, seeds, data provenance, software versions, and resource budgets. A reported winner without its search history cannot support causal analysis.

9. **Keep the evaluator outside the claim when possible.** If a candidate can modify or infer the acceptance test, evaluator exploitation becomes a competing explanation. Hidden and time-separated tests reduce this ambiguity.

10. **Separate author reports from independent results.** Use `reported`, `reproduced`, `replicated`, `contradicted`, and `open` for specific claims. Do not attach one status to an entire project.

11. **Prefer experiments that distinguish explanations.** Component swaps, equal-compute controls, cross-model transfer, held-out distributions, and later-generation tests are more informative than another score on the optimization benchmark.

12. **Retain negative results that constrain the search.** A failure belongs in the record when it identifies a scale boundary, invalidates a causal explanation, exposes an evaluator weakness, or rules out a route.

13. **Do not promote terminology to progress.** A new name, diagram, decomposition, or notation matters only when it enables prediction, implementation, measurement, transfer, or falsification.

14. **Keep confidence proportional to evidence.** Distinguish facts established by public artifacts, conclusions derived from those facts, working hypotheses, and speculation.
