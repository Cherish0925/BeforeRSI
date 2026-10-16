# Minimal RSI phase model

This note turns the abstract RSI theory into a three-state dynamical system that can be fitted to repeated model–harness experiments.

Let cumulative improvement resource be \(r\). Define

- \(C(r)\): protected transferable capability;
- \(\eta(r)\): transferable improvement per unit improvement resource;
- \(q(r)\in[0,1]\): fidelity of the evaluator and acceptance process.

The minimal model is

$$
\frac{dC}{dr}=\eta,
$$

$$
\frac{d\eta}{dr}
=
\left[
q\left(a_0+a_1\frac{C}{K+C}\right)
-
\left(d_0+d_1 C^p\right)
\right]\eta
-
\kappa\eta^2
+
u,
$$

$$
\frac{dq}{dr}
=
r_v(1-q)-s_v\eta q.
$$

## Meaning of the terms

The factor

$$
a_0+a_1\frac{C}{K+C}
$$

is the design gain available from the current system. \(a_0\) is capability-independent improvement; \(a_1\) measures how much stronger capability improves future system design; \(K\) is the capability scale at which that feedback becomes substantial.

The term

$$
d_0+d_1C^p
$$

is complexity and verification debt: coupling among components, harder attribution, more expensive training, longer regression suites, and declining availability of easy improvements.

The term \(-\kappa\eta^2\) represents saturation of the current task, data, and design distribution. The term \(\nu\) represents improvement supplied from outside the recursive process: human research, new algorithms, new datasets, or stronger teacher models.

Evaluator fidelity is repaired at rate \(r_v\) and eroded at rate \(s_v\eta q\). The erosion term captures a moving-target effect: as the system proposes more powerful or more unusual changes, the old evaluator becomes less informative.

At fixed \(\eta\), evaluator fidelity approaches

$$
q^*(\eta)=\frac{r_v}{r_v+s_v\eta}.
$$

Therefore an acceleration in improvement rate automatically lowers evaluator fidelity unless verification investment scales with it.

## Local recursive threshold

Define

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
\lambda(C,\eta)\eta-\kappa\eta^2+
u.
$$

The sign of \(\lambda\) is the local balance between recursive design gain and complexity-plus-verification debt.

- \(\lambda<0\): improvement efficiency decays;
- \(\lambda\approx0\): progress is mainly externally driven;
- \(\lambda>0\): the current system raises the productivity of later improvement;
- large \(\eta\) can still be capped by saturation and evaluator erosion.

For fixed \(C\) and \(q\), the positive stationary efficiency is

$$
\eta^*
=
\frac{\lambda+\sqrt{\lambda^2+4\kappa\nu}}{2\kappa}.
$$

This expression separates three causes of apparent progress: external input \(
u\), recursive gain \(\lambda\), and saturation \(\kappa\).

## Four illustrative regimes

The reference script produces four trajectories under equal cumulative improvement resource.

| Regime | Final \(C\) | Final \(\eta\) | Final \(q\) | Interpretation |
|---|---:|---:|---:|---|
| Saturation | 3.156 | 0.019 | 0.986 | complexity debt exceeds recursive gain |
| Steady improvement | 17.554 | 0.317 | 0.932 | bounded positive improvement efficiency |
| Recursive acceleration | 167.954 | 2.925 | 0.925 | capability-dependent design gain dominates debt while verification keeps pace |
| Verifier-limited | 40.075 | 0.535 | 0.241 | intrinsic improvement grows, but evaluator fidelity collapses and suppresses realized gain |

These numbers are demonstrations, not empirical estimates. Their purpose is to show which quantities must be measured to identify the actual regime of a real AI system.

## Reproduction

```bash
python -m venv .venv
source .venv/bin/activate
pip install numpy scipy matplotlib
python simulations/minimal_rsi_dynamics.py
```

The script writes capability and improvement-efficiency plots to `simulations/output/`.

## Empirical identification

A real experiment should estimate the parameters from interventions rather than fit a single aggregate score.

- \(a_0,a_1,K\): compare parent and successor as improvers across several capability levels;
- \(d_0,d_1,p\): measure update cost, regression burden, and failure rate as system complexity grows;
- \(\kappa\): vary candidate count and task diversity to estimate saturation;
- \(r_v\): invest controlled resources in verifier construction and measure fidelity recovery;
- \(s_v\): freeze the evaluator while increasing proposal power and measure fidelity decay;
- \(
u\): repeat the experiment with external human or teacher-model contributions removed.

Once identified, the model can be used for budget allocation, phase prediction, and model-predictive control over model, harness, improver, data, and verification investment.
