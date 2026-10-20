# Experiment 002 — Model–harness attribution

## Question

When model and harness are both updated, where does the gain reside?

## Required cross

$$

(M_0,H_0),\quad
(M_1,H_0),\quad
(M_0,H_1),\quad
(M_1,H_1).

$$

$M_1$ should be trained from versioned, verified trajectories. $H_1$ should be selected without access to hidden or time-forward evaluation.

## Measurements

For each pair, report:

- held-out and time-forward capability;
- per-domain results;
- execution cost;
- protected regressions;
- calibration and reliability;
- tool-use failures;
- data contribution to the next model update.

## Analysis

Estimate:

- model main effect;
- harness main effect;
- interaction;
- cross-version portability;
- scale dependence.

Repeat with at least two model capability levels when resources permit.

## Failure patterns

- $M_1,H_1$ improves but both crossed pairs fail: local co-adaptation;
- $H_1$ helps only $M_0$: checkpoint-specific compensation;
- $M_1$ helps only $H_1$: harness-conditioned training;
- all gains vanish under equal cost: compute substitution;
- average gain hides a protected regression: unacceptable update.
