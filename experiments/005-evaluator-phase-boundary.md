# Experiment 005 — Evaluator fidelity and the RSI phase boundary

## Question

At what evaluator quality does additional candidate search stop producing real improvement and begin selecting noise, benchmark-specific patches, or metric exploits?

## Core model

For candidate $j$:

$$
y_j=g_j+\epsilon_j+b_j,
$$

where $g_j$ is true transferable gain, $\epsilon_j$ is ordinary evaluation noise, and $b_j$ is systematic bias or exploitability.

Define selection fidelity:

$$
\rho=\operatorname{Corr}(y,g).
$$

The working approximation predicts

$$
\mathbb E[g_{\rm selected}]
\approx
\mu_g+\rho\sigma_g\sqrt{2\log n},
$$

while candidate-generation and evaluation cost grows approximately linearly with candidate count $n$.

## Manipulations

Vary independently:

- candidate count $n$;
- evaluator sample count;
- evaluator model or verifier strength;
- injected random noise;
- access to evaluator internals;
- benchmark leakage;
- repeated exposure to the same validation tasks;
- final reevaluation with an independent evaluator.

Keep the proposer, parent system, task-time budget, and candidate-generation budget per candidate fixed within each sweep.

## Ground truth

Use a task family where a stronger external test or exact verifier can estimate true transferable gain after selection.

The search evaluator must not be the only source of truth.

## Outputs

For each condition record:

- $\rho$;
- evaluator variance;
- selected measured gain;
- selected true gain;
- winner's-curse gap;
- exploit rate;
- transfer number;
- regression rate;
- total improvement cost;
- gain per unit improvement cost;
- optimal candidate count $n^*$.

## Phase map

Estimate regions in the plane

$$
(\rho,n)
$$

or, when using a signal-to-noise measure,

$$
(\mathcal V,n).
$$

Expected regimes:

- **signal-limited:** candidate differences are below evaluation noise;
- **productive search:** more candidates increase true selected gain;
- **winner's-curse:** measured gain continues rising while true gain plateaus;
- **exploit-dominated:** true held-out gain declines as measured score rises.

## Decisive result

The hypothesis is supported if a reproducible boundary exists beyond which increasing search pressure reduces resource-normalized true gain, and if improving evaluator fidelity moves that boundary outward.

This experiment measures when more search ceases to be intelligence improvement.