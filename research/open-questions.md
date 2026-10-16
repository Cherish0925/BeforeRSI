# Open questions

The questions below are prioritized because their answers would change which routes to general RSI remain plausible.

## Does improvement transfer with model scale?

A method discovered on a small model may repair limitations that a stronger model does not share. The reverse can also occur: a weak model may be unable to discover improvements that become accessible only beyond a capability threshold.

Required experiment: hold tasks and resource accounting fixed across several model scales and families; measure absolute gain, relative gain, cost-adjusted gain, regression, and the kinds of modifications discovered.

## Where does durable improvement live?

Weights, harness code, memory, tools, training procedures, and externalized skills can all retain useful changes. Their persistence, portability, and update cost differ.

Required experiment: component swaps and ablations across model and harness versions, followed by transfer to untouched tasks.

## Can an improved system improve itself better?

Most work measures the task performance of \(S_{t+1}\), not the improvement ability of \(S_{t+1}\).

Required experiment: run at least two improvement generations under matched budgets. Compare candidate quality, acceptance rate, transfer, and improvement per unit cost across generations.

## What compounds and what saturates?

Some changes remove one-time defects. Others may increase the rate at which later changes are found. The difference determines whether improvement is linear, saturating, unstable, or superlinear.

Required experiment: maintain full lineage over many generations and fit competing growth models to held-out, cost-adjusted capability rather than optimization-set score.

## How should improvement be valued under multiple capabilities?

A successor can improve one domain and regress elsewhere. A scalar objective embeds an arbitrary exchange rate among capabilities, cost, latency, and robustness.

Required experiment: report a capability vector and Pareto changes; define hard regression limits before the run.

## Can RSI proceed with imperfect evaluators?

Real tasks often have sparse, delayed, partially gameable, or unknown success signals. Strong evaluators may themselves be more difficult to build than the candidate system.

Required experiment: inject controlled evaluator error, hide parts of the objective, and measure whether the improvement process remains beneficial under independent tests.

## Can an AI improve the update procedure rather than only the target system?

Candidate generation, experiment selection, credit assignment, parent selection, data construction, and optimizer design are potential objects of meta-improvement.

Required experiment: freeze the target task family while allowing one update component to change; test whether the new component transfers to a second improvement problem.

## How much improvement comes from external intelligence?

Human task design, curated datasets, stronger teacher models, hidden unit tests, and fixed optimizers can supply the decisive information.

Required experiment: quantify performance as each external source is removed, weakened, or replaced by a matched baseline.

## Can self-generated data avoid long-run collapse?

Self-training can amplify current errors and narrow the data distribution. Selection and external grounding may prevent this, but the conditions are not established.

Required experiment: track diversity, calibration, rare-skill retention, factual error, and transfer over many data-generation and training generations.

## Does open-ended search outperform carefully designed search spaces?

Open edit spaces allow unforeseen improvements but sharply increase evaluation cost and failure probability. Restricted spaces can hide how much intelligence was supplied by the designer.

Required experiment: compare open and restricted edit spaces under equal candidate and evaluation budgets, then test transfer of the discovered changes.

## What remains when frontier-lab results are unavailable?

Large-model RSI work may exist privately, while public evidence is concentrated on smaller models and benchmarked agents. This creates an identification problem: absence of public results does not establish impossibility, and private claims cannot support scientific conclusions.

Required response: state which conclusions follow from public evidence, which depend on scale extrapolation, and which remain underdetermined.
