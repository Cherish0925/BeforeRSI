# Experiment 003 — Successor as improver

## Question

Is the successor better at producing later successors?

## Construction

First create a persistent successor:

$

S_0 \xrightarrow{I_0} S_1.

$

Then give $S_0$ and $S_1$ the same unseen improvement problem, editable surface, tools, evaluator access, and total improvement budget $B$:

$

S_0 \xrightarrow[B]{} C_0,\qquad
S_1 \xrightarrow[B]{} C_1.

$

Evaluate $C_0$ and $C_1$ on hidden and time-forward tasks.

## Primary quantity

$

R(S)=
\frac{
U_Q(C)-U_Q(S)
}{
C_{\mathrm{improve}}
}.

$

Also report valid candidate rate, transfer breadth, regressions, time to useful descendant, and evaluator exploitation.

## Claim rule

A D3 claim requires repeated evidence that descendants generated from $S_1$ are better, broader, cheaper, or more reliable than descendants generated from $S_0$.

A higher task score for $S_1$ is insufficient. A fixed external optimizer repeatedly improving both parents is insufficient unless the successor changes the quality of later improvement.
