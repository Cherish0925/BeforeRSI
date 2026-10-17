# Experiment 004 — Repeated model–harness–improver co-evolution

## Question

Does the complete update cycle increase both transferable capability and future improvement efficiency across multiple generations, or do the gains saturate once easy harness and model defects are removed?

## Arms

Run equal-total-resource arms for at least three complete generations:

1. **co-evolution:** model, harness portfolio, and improver may update;
2. **model-only:** model may update; harness and improver are frozen;
3. **harness-only:** harness may update; model and improver are frozen;
4. **fixed-improver co-evolution:** model and harness may update; improver is frozen;
5. **parent-compute baseline:** no persistent update; equivalent total resource is spent at task time.

All arms share the same task-generation policy, external tools, protected acceptance tests, and accounting rules.

## Generation

For generation $t$:

$$
(M_t,\mathcal H_t,I_t)
\rightarrow
(M_{t+1},\mathcal H_{t+1},I_{t+1}).
$$

Preserve every proposed candidate, accepted and rejected lineage, model checkpoint, training dataset, evaluator version, and task cohort.

## Measurements

At each generation estimate:

- protected transferable capability $C_t$;
- improvement efficiency $\eta_t$;
- recursion number $\mathcal R_t=\eta_{t+1}/(\eta_t+\varepsilon)$;
- model main effect $\Delta_M$;
- harness main effect $\Delta_H$;
- interaction $\Gamma_{MH}$;
- transfer number $\mathcal T$;
- evaluator fidelity;
- harness-portfolio diversity;
- critical regressions;
- training, inference, evaluator, human, and wall-clock cost.

## Decisive comparisons

The central comparison is not final score alone.

Evidence for sustained recursion requires the co-evolution arm to show, on new improvement problems:

$$
\eta_{t+1}>\eta_t
$$

for repeated generations, beyond the model-only, harness-only, fixed-improver, and equal-compute baselines.

If capability rises while $\eta$ remains flat or falls, the system is improving without recursive acceleration.

## Model discrimination

This experiment distinguishes at least four explanations:

- ordinary optimization with diminishing returns;
- additive model and harness gains;
- positive model–harness co-adaptation without improved improver;
- genuine recursive gain in which the successor becomes a better improvement process.

## Stop conditions

Stop the run or change the representation if:

- hidden and time-forward gains vanish;
- evaluator disagreement exceeds candidate differences;
- critical regressions accumulate;
- external intervention supplies most accepted changes;
- lineage can no longer identify parentage and resource use;
- $\eta$ cannot be estimated with useful uncertainty.

A negative result is informative if it identifies where the recursive loop breaks.