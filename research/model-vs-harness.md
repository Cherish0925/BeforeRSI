# Model improvement and harness improvement

The distinction between model and harness changes is one of the main unresolved questions in public RSI research.

A model can be held fixed while its surrounding software changes substantially. A harness can be held fixed while weights, training data, rewards, or optimizers change. Joint systems update both. End-to-end scores do not reveal which object caused the gain.

## Objects

For a simplified system \(S=(M,H)\):

- \(M\) contains model parameters and architecture;
- \(H\) contains prompts, context construction, memory, tools, search, agent topology, routing, control flow, validation, and stopping rules.

Suppose an improvement run yields \((M_1,H_1)\) from \((M_0,H_0)\). The minimum attribution experiment evaluates

\[
(M_0,H_0),\quad (M_1,H_0),\quad (M_0,H_1),\quad (M_1,H_1).
\]

The four measurements distinguish several possibilities:

- the gain resides mostly in the model;
- the gain resides mostly in the harness;
- both changes add independently;
- the changes interact, so neither transfers alone;
- one change compensates for damage caused by the other.

The same swap logic extends to memory, tools, training procedures, and evaluators.

## Why harness gains can be misleading

A harness can improve a benchmark by embedding task-specific logic, increasing inference calls, exposing more context, invoking a stronger hidden tool, or adapting to evaluator quirks. These are real system changes, but they support different claims.

A transferable harness result should report:

- performance under an equal total inference budget;
- held-out and time-separated tasks;
- transfer to at least one other model when model-agnostic value is claimed;
- sensitivity to model strength;
- added latency, tool use, and context cost;
- regressions caused by longer or more brittle control flow.

A harness that helps a weak model can become neutral or harmful when the base model is stronger. The harness may encode compensatory structure that the stronger model no longer needs, or it may constrain behavior that the stronger model would otherwise perform well.

## Why model gains can be misleading

A weight update can memorize the improvement set, narrow the output distribution, exploit a reward model, erase unrelated abilities, or reproduce information already present in the external training pipeline. A model-level self-improvement claim should identify how the model contributed to data generation, reward construction, curriculum, optimizer choice, or training code.

Useful controls include:

- training on matched data produced without self-generation;
- equalizing total data and training compute;
- testing unrelated capabilities for regression;
- evaluating on tasks created after training;
- transferring the update procedure to another model scale or family;
- separating the benefit of stronger labels from the benefit of the self-improvement procedure.

## Joint improvement

Joint updates can outperform either component alone, but they create an attribution problem. A system may cycle between a model adapted to one harness and a harness adapted to one model, producing local co-adaptation with weak transfer.

A joint system should therefore report a transfer matrix:

| | \(H_0\) | \(H_1\) | \(H_2\) |
|---|---:|---:|---:|
| \(M_0\) | baseline |  |  |
| \(M_1\) |  | paired successor |  |
| \(M_2\) |  |  | later successor |

Cross-generation cells show whether improvements are reusable or only compatible with their paired version.

## Research hypotheses

The following hypotheses are open and experimentally distinguishable:

1. Harness improvement dominates at current model capability because software changes are cheaper and easier to evaluate than weight updates.
2. Harness gains shrink as base models strengthen, except for tools, memory, and control structures that supply capabilities unavailable in the model.
3. Model updates transfer more broadly when they internalize strategies that were first discovered in harness search.
4. Joint improvement produces the largest short-run gains but the weakest attribution and the greatest risk of co-adaptation.
5. The long-run bottleneck moves between model, harness, evaluator, data, and environment rather than remaining fixed.

BeforeRSI will treat these as hypotheses until controlled cross-model, cross-harness, and cross-generation experiments discriminate among them.
