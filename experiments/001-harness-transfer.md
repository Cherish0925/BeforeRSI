# Experiment 001 — Harness transfer under equal total compute

## Question

Does a persistent harness update create reusable capability, or does it merely amortize additional search and repeated benchmark feedback?

## Systems

- fixed model \(M_0\);
- parent harness \(H_0\);
- evolved harness \(H_1\);
- second model family or scale \(M_x\).

## Conditions

1. \((M_0,H_0)\) with standard task-time budget;
2. \((M_0,H_0)\) with total compute equal to harness improvement plus successor execution;
3. \((M_0,H_1)\) with standard task-time budget;
4. \((M_x,H_0)\) and \((M_x,H_1)\);
5. fresh reevaluation of selected \(H_1\).

## Task cohorts

- \(P\): visible improvement tasks;
- \(V\): limited-exposure validation;
- \(Q\): hidden tasks;
- \(T\): tasks created after \(H_1\) is frozen.

No element of \(Q\) or \(T\) may enter candidate generation, selection, tuning, or stopping.

## Primary outputs

- held-out gain;
- time-forward gain;
- equal-total-compute gain;
- cross-model gain;
- task-level regressions;
- cost and latency;
- accepted and rejected lineage;
- tampering audit.

## Interpretation

- gain only on \(P\): benchmark fitting;
- gain on \(Q\), lost under equal compute: search amortization;
- gain on \(Q\) and \(T\), lost on \(M_x\): model-specific compensation;
- gain across \(Q\), \(T\), and \(M_x\): evidence for transferable harness improvement.
