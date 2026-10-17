# Experiment 004 — Repeated improvement and recursive reuse

## Question

Does model–harness adaptation improve later improvement ability, and does reusing the successor contribute beyond target improvement alone?

## Arms and intervention

Under equal total improvement-resource budgets, compare joint/alternating updates, model-only updates, harness-only updates, and a frozen-ancestor-improver arm. Record the exact schedule. Maintaining several harnesses is an optional treatment with a single-incumbent control.

In the frozen-ancestor arm, pin the complete actor $A_0=(M_0,H_0,D_0)$ and let it improve the same target versions as the refreshed-actor arm. Freezing only an “improver” function while changing the model it calls does not freeze the improver.

Shared variables include target cohorts, visible data/feedback, external tools, execution conditions, resource accounting, and final assessment. Parent task-time search is a separate lifecycle-cost comparison over a declared deployment horizon.

## Generation and measurements

Preserve each target, acting improver, accepted/rejected candidate, training dataset, model checkpoint, and evaluation version. At each generation:

- evaluate task performance at matched execution budget;
- run Experiment 003 on identical copies of common reference targets;
- estimate the paired common-target gain difference and uncertainty;
- cross compatible old/new models and harnesses with data held fixed;
- record regressions, feedback exposure, and all resource use.

Use the same reference distribution for comparisons, or evaluate both actors on each new cohort and retain anchors. Ratios near zero and raw score slopes across changing task distributions are not recursion measurements.

## Competing explanations and outcomes

Compare independent component gains, useful interaction during execution, improved training-data production, and better future improvement behavior. Interaction sign alone does not identify which explanation is correct.

Repeated positive common-target actor effects and a benefit of refreshing the actor support recursive reuse over the observed horizon. Flat or declining within-lineage score gains do not alone disprove improved improvement ability: targets may become harder or approach ceilings. A few generations cannot establish open-endedness.

Model-only or harness-only success is a valid result. A failure of alternation should change the schedule hypothesis rather than be excluded by the definition of RSI.

## Reproduction and stopping

Preserve the Experiment 003 artifacts plus matched cross-component results and full generation costs. Stop or redesign when target equivalence, budget matching, test independence, or uncertainty estimation fails. Negative results remain informative when they distinguish the competing explanations.

**Status:** protocol; no real-system run is claimed here.

