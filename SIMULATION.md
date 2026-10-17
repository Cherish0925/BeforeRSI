# Illustrative trajectories and model identification

These simulations integrate chosen equations. They are not measurements of AI systems, evidence for recursive self-improvement, or forecasts. See THEORY.md for counterexamples to the previous causal interpretation.

The plotted slope $\eta_{\rm path}=dC/dr$ is a trajectory statistic. It is distinct from $G(A;\mu,B,b)$, which compares improvers on common targets. Rising $\eta_{\rm path}$ alone does not identify an improved improver.

## 1. Assumed capability-growth law

The equation

$$
\frac{dC}{dr}=aC^\epsilon
$$

has, for $\epsilon\ne1$, the solution

$$
C(r)=
\left[C_0^{1-\epsilon}+(1-\epsilon)ar\right]^{1/(1-\epsilon)}
$$

while the bracket remains positive. For $\epsilon=1$, $C=C_0e^{ar}$.

| Assumed exponent | Consequence within this equation |
|---|---|
| $\epsilon<0$ | diminishing slope |
| $\epsilon=0$ | linear growth |
| $0<\epsilon<1$ | superlinear non-exponential growth |
| $\epsilon=1$ | exponential growth |
| $\epsilon>1$ | finite-resource divergence; no continuation through the singularity is supplied |

The exponent determines the curve by assumption. These plots do not estimate an exponent for RSI. A bounded benchmark score cannot follow an unbounded curve indefinitely.

## 2. Slope dynamics

The illustrative equation is

$$
\frac{d\eta}{dr}=(g-d)\eta-\kappa\eta^2+u.
$$

For $\eta>0$, rising slope requires

$$
g-d>\kappa\eta-\frac{u}{\eta}.
$$

The sign of $g-d$ alone is insufficient. For constant coefficients, $u=0$, $g-d>0$, and $\kappa>0$, positive solutions approach $(g-d)/\kappa$; the asymptotic logarithmic growth rate of $\eta$ is zero.

Replacing $g,d$ with $g+q,d+q$ leaves the equation unchanged. Estimating one trajectory therefore cannot separately identify these two quantities. Their names do not assign causal meanings.

## 3. Search and evaluator noise

Under i.i.d. jointly Gaussian candidate/score pairs $(g_j,y_j)$, selecting the maximum observed score yields

$$
\mathbb E[g_{\rm selected}]
=\mu_g+\rho\sigma_g a_n,
\qquad
a_n=\mathbb E[\max_{j\le n}Z_j]
\sim\sqrt{2\log n}.
$$

The plotted function uses the large-$n$ approximation, with $a_1=0$, and divides by $C_0+nC_{\rm candidate}$. With fixed $\rho>0$, absolute expected selected gain increases with $n$; gain per unit cost can peak and fall. There is no universal sharp fidelity threshold in this model. Non-Gaussian, adaptive, or exploitative search requires a different conditional selection model.

## 4. Coupled illustrative equations

The script integrates

$$
\frac{dC}{dr}=\eta,
$$

$$
\frac{d\eta}{dr}=
\left[
q\left(a_0+a_1\frac{C}{K+C}\right)
-(d_0+d_1C^p)
\right]\eta-\kappa\eta^2+u,
$$

$$
\frac{dq}{dr}=r_v(1-q)-s_v\eta q.
$$

Initial conditions are $(C,\eta,q)=(1,0.08,0.90)$ over resource interval $[0,80]$. Parameters are declared in the script; none are fitted. All four reference scenarios have nonzero external forcing $u$, so none isolates autonomous improvement.

At fixed $\eta$, the evaluator variable has equilibrium

$$
q^*(\eta)=\frac{r_v}{r_v+s_v\eta}.
$$

Substituting this into the other equations is a quasi-steady approximation, not an exact reduction of a time-varying run. It requires a justified separation of timescales and an error check.

Reference outputs, unchanged numerically by relabeling:

| Synthetic scenario | Final $C$ | Final $\eta$ | Final $q$ |
|---|---:|---:|---:|
| Low final slope | 3.156 | 0.019 | 0.986 |
| Bounded slope example | 17.554 | 0.317 | 0.932 |
| Rising slope example | 167.954 | 2.925 | 0.925 |
| Declining fidelity example | 40.075 | 0.535 | 0.241 |

These are consequences of arbitrary parameters on a finite interval. They do not identify an RSI phase or a real-system acceleration regime.

## 5. Identification requirements

Before using a low-dimensional law, test whether its state variables predict intervention responses after conditioning on history, code structure, and task type. THEORY.md gives the exact state-sufficiency condition and an approximate error bound.

Measure improver changes on common targets. Independently vary proposal, selection, feedback, data production, and update resources where the implementation permits it. Use measured quantities to fit competing laws; preserve uncertainty and distinguish shared parameters from method-specific ones.

Prediction requires withheld interventions, methods, generations, and task cohorts. Fitting each historical curve with its own free parameters does not establish a transferable theory. Separate causal terms require interventions that distinguish them; otherwise report only identifiable combinations.

## 6. Reproduction

~~~bash
python -m venv .venv
source .venv/bin/activate
pip install numpy scipy matplotlib
python simulations/minimal_rsi_dynamics.py
python scripts/check_model_counterexamples.py
~~~

The simulation writes plots and parameter summaries under simulations/output/. The counterexample script checks deterministic mathematical witnesses using only the Python standard library. Neither command runs a model or establishes empirical RSI.

