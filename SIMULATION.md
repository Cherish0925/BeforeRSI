# Simulation and model identification

The simulations in this repository are **illustrative dynamical models**, not empirical forecasts. Their job is to make assumptions explicit, expose qualitative regimes, and identify which quantities a real RSI experiment must measure.

The current simulation stack has three layers:

1. capability growth as a function of recursive elasticity;
2. improvement-efficiency dynamics under recursive gain and complexity debt;
3. candidate-search efficiency under evaluator noise.

A fourth layer couples capability, improvement efficiency, and evaluator fidelity.

## 1. Capability growth and recursive elasticity

Let $r$ be cumulative improvement resource and let capability satisfy

$$
\frac{dC}{dr}=aC^\epsilon.
$$

The exponent

$$
\epsilon_{\rm RSI}
=
\frac{d\ln\eta}{d\ln C}
$$

measures how improvement efficiency changes with capability.

For $\epsilon\ne1$,

$$
C(r)
=
\left[
C_0^{1-\epsilon}
+
(1-\epsilon)ar
\right]^{1/(1-\epsilon)}.
$$

For $\epsilon=1$,

$$
C(r)=C_0e^{ar}.
$$

The qualitative regimes are:

| Elasticity | Predicted shape |
|---|---|
| $\epsilon<0$ | diminishing returns |
| $\epsilon=0$ | linear capability growth in resource |
| $0<\epsilon<1$ | superlinear but non-exponential growth |
| $\epsilon=1$ | exponential growth |
| $\epsilon>1$ | finite-resource singularity in the idealized equation |

The final regime is not a realistic literal forecast; it signals that omitted constraints must become important before the idealized singularity.

## 2. Improvement efficiency

A minimal model for improvement efficiency is

$$
\frac{d\eta}{dr}
=
\lambda_{\rm RSI}\eta
-
\kappa\eta^2
+
u_{\rm ext},
$$

with

$$
\lambda_{\rm RSI}=g-d.
$$

Here:

- $g$ is recursive design gain;
- $d$ is complexity and verification debt;
- $\kappa$ is saturation;
- $u_{\rm ext}$ is external improvement supplied by humans, new algorithms, stronger teachers, or new data.

With $u_{\rm ext}=0$ and $\lambda_{\rm RSI}>0$, the positive equilibrium is

$$
\eta^*=\frac{\lambda_{\rm RSI}}{\kappa}.
$$

This model separates three cases:

- capability can improve while $\eta$ falls;
- capability can improve at roughly constant $\eta$;
- capability can improve while $\eta$ also rises.

Only the third is evidence for recursive acceleration.

## 3. Candidate search and evaluator fidelity

Let candidate true gains be approximately

$$
g_j\sim\mathcal N(\mu_g,\sigma_g^2),
$$

and measured gains be

$$
y_j=g_j+\epsilon_j.
$$

Let

$$
\rho=\operatorname{Corr}(g,y)
$$

measure evaluator fidelity.

Selecting the maximum measured candidate among $n$ proposals gives the approximation

$$
\mathbb E[g_{\rm selected}]
\approx
\mu_g+\rho\sigma_g\sqrt{2\log n}.
$$

If search cost is

$$
C(n)=C_0+n(C_{\rm gen}+C_{\rm eval}),
$$

then resource-normalized search efficiency is approximately

$$
\eta_{\rm search}(n)
=
\frac{
\mu_g+\rho\sigma_g\sqrt{2\log n}-R(n)
}{
C(n)
}.
$$

The benefit grows only as $\sqrt{\log n}$ while cost is approximately linear in $n$. Therefore the model predicts a finite optimal candidate count $n^*$.

Low evaluator fidelity moves $n^*$ downward and increases the gap between measured winner score and true held-out gain.

## 4. Coupled capability–improvement–verification dynamics

The current three-state model is

$$
\frac{dC}{dr}=\eta,
$$

$$
\frac{d\eta}{dr}
=
\left[
q\left(a_0+a_1\frac{C}{K+C}\right)
-
\left(d_0+d_1C^p\right)
\right]\eta
-
\kappa\eta^2
+
u_{\rm ext},
$$

$$
\frac{dq}{dr}
=
r_v(1-q)-s_v\eta q.
$$

The state variables are:

- $C$: protected transferable capability;
- $\eta$: transferable improvement per unit improvement resource;
- $q\in[0,1]$: evaluator and acceptance fidelity.

The term

$$
a_0+a_1\frac{C}{K+C}
$$

is capability-dependent design gain. The term

$$
d_0+d_1C^p
$$

is complexity and verification debt.

Evaluator fidelity is repaired at rate $r_v$ and eroded by faster-changing candidate systems at rate $s_v\eta q$.

At fixed $\eta$,

$$
q^*(\eta)=\frac{r_v}{r_v+s_v\eta}.
$$

This creates a moving-target effect: a faster improver can outrun its evaluator unless verification investment scales with it.

Define the local net recursive gain

$$
\lambda(C,\eta)
=
\frac{r_v}{r_v+s_v\eta}
\left(a_0+a_1\frac{C}{K+C}\right)
-
\left(d_0+d_1C^p\right).
$$

Then

$$
\frac{d\eta}{dr}
=
\lambda(C,\eta)\eta
-
\kappa\eta^2
+
u_{\rm ext}.
$$

## 5. Illustrative regimes

The reference parameterizations currently produce four synthetic regimes under equal cumulative improvement resource.

| Regime | Final $C$ | Final $\eta$ | Final $q$ | Interpretation |
|---|---:|---:|---:|---|
| Saturation | 3.156 | 0.019 | 0.986 | complexity debt dominates recursive gain |
| Steady improvement | 17.554 | 0.317 | 0.932 | positive but bounded improvement efficiency |
| Recursive acceleration | 167.954 | 2.925 | 0.925 | capability-dependent design gain dominates while verification keeps pace |
| Verifier-limited | 40.075 | 0.535 | 0.241 | proposal power grows faster than evaluator fidelity |

These values are generated by the current toy parameters. They are not measurements of any real AI system.

## 6. Phase language

The simulations suggest a useful qualitative phase map.

### Noise-dominated

Evaluator signal is below candidate variation. More search mainly selects noise.

### Benchmark-fitting

Visible-task gain is positive but transfer number

$$
\mathcal T
=
\frac{\Delta J_{\rm hidden}}
{\Delta J_{\rm visible}+\varepsilon}
$$

is near zero.

### Ordinary improvement

Capability rises but improvement efficiency is approximately constant or falling.

### Recursive improvement

Capability and held-out improvement efficiency both rise:

$$
\frac{dC}{dr}>0,
\qquad
\frac{d\eta}{dr}>0.
$$

### Saturation

The system approaches a finite $\eta^*$ because complexity, verification, data, or search limitations dominate.

### Unstable growth

Measured improvement rises while evaluator fidelity, protected capability, or regression control deteriorates. This is not automatically beneficial RSI.

## 7. Parameter identification

A real system must estimate parameters from interventions.

| Parameter | Measurement |
|---|---|
| $a_0,a_1,K$ | parent-versus-successor improver comparisons across capability levels |
| $d_0,d_1,p$ | update cost, regression burden, system coupling, validation cost as capability grows |
| $\kappa$ | candidate-count and task-diversity sweeps |
| $r_v$ | controlled investment in evaluator construction or recalibration |
| $s_v$ | freeze the evaluator while proposal power rises |
| $u_{\rm ext}$ | remove or vary human, teacher-model, and external research contributions |
| $\rho$ | compare search-evaluator scores with an independent stronger test |
| $\Gamma_{MH}$ | full model–harness cross |

The model should be judged by out-of-sample prediction of later generations, not by fitting one historical trajectory.

## 8. Reproduction

Run:

~~~bash
python -m venv .venv
source .venv/bin/activate
pip install numpy scipy matplotlib
python simulations/minimal_rsi_dynamics.py
~~~

The script writes plots and a JSON summary to **simulations/output/**.

Current outputs include:

- capability trajectories for the four coupled regimes;
- improvement-efficiency trajectories;
- evaluator-fidelity trajectories;
- capability growth under several recursive elasticities;
- search efficiency as candidate count changes under several evaluator fidelities.

## 9. What the simulations are for

The simulations should be used to decide what to measure next.

They should not be used to infer a takeoff curve from arbitrary parameters.

A simulation becomes a forecast only after:

1. parameters are estimated from interventions;
2. uncertainty is propagated;
3. the model predicts withheld generations;
4. competing models are fit to the same data;
5. the prediction survives a change in task distribution or system version.

The current purpose is system identification, model criticism, and experiment design.