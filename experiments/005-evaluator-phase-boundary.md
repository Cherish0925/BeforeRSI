# Experiment 005 — Evaluator fidelity and search efficiency

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

For independent identically distributed jointly Gaussian pairs, the large-candidate approximation predicts

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

## Response surface

Estimate regions in the plane

$$
(\rho,n)
$$

or, when using a signal-to-noise measure,

$$
(\mathcal V,n).
$$

Candidate behaviors to test (not universal phases):

- **signal-limited:** candidate differences are below evaluation noise;
- **productive search:** more candidates increase true selected gain;
- **winner's-curse:** measured gain continues rising while true gain plateaus;
- **exploit-dominated:** true held-out gain declines as measured score rises.

## Decisive result

Measure absolute true gain and gain per unit cost separately. With fixed positive fidelity and i.i.d. joint Gaussian candidates, true selected gain increases with candidate count; efficiency can still peak because cost grows faster. A decline in absolute true gain requires additional effects such as changing candidate distributions or exploitation.

A reproducible efficiency optimum supports a budget-allocation claim. A sharp phase transition or a universal fidelity threshold requires separate evidence. Test whether better evaluation shifts the optimum; do not assume its direction before estimating costs and candidate distributions.
