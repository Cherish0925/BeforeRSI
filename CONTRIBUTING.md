# Contributing

BeforeRSI accepts contributions that change the accuracy of the public record, enable a controlled experiment, or produce a reproducible result.

## Useful contributions

- add a primary paper, official repository, model, dataset, trace, or evaluation artifact;
- correct a factual statement with a primary source;
- reproduce a specific reported result;
- independently replicate a conclusion with a separate implementation;
- report a controlled contradiction or boundary case;
- implement an experiment in `experiments/`;
- improve resource accounting, lineage recording, or statistical analysis;
- add a negative result that rules out a route or exposes a confounder.

## Evidence rules

Every empirical statement must identify:

- the system and version;
- the task set and split;
- the evaluator;
- the resource budget;
- the source of the result;
- whether the status is `reported`, `reproduced`, `replicated`, `contradicted`, or `open`.

Prefer primary sources: papers, official repositories, released artifacts, author-maintained project pages, and raw experiment outputs. Secondary summaries may help locate a source but should not support technical claims when the primary source is available.

## Catalog changes

For `data/systems.json`:

1. use the official repository;
2. describe changed objects as claims made by public materials;
3. keep `evidence_status` at `reported` until a specific result has been rerun;
4. keep the central question falsifiable;
5. run:

```bash
python scripts/validate_catalog.py
```

Adding a project does not endorse its RSI claim. Removing a project requires a factual reason, such as a duplicate, unavailable source, or lack of relevance to self-improvement.

## Reproduction submissions

A reproduction should include:

```text
exact commit or release
model and endpoint version
full configuration
hardware and software environment
task split
seeds
raw outputs
resource accounting
analysis code
comparison with the reported result
```

State every deviation from the original setup. A close score obtained under materially different conditions is not a direct reproduction.

## Experimental submissions

New experiments should answer a question that distinguishes competing explanations. Include the hypothesis, controls, failure conditions, and the result that would change the conclusion.

Avoid experiments that only add another benchmark score without controlling for compute, repeated task exposure, evaluator access, or regression.

## Writing

Use direct technical language. Separate facts, derived conclusions, hypotheses, assumptions, and speculation. Do not convert project descriptions into claims that the public artifacts do not support.

Generated summaries require line-by-line source checking before submission. Unsupported catalog entries, invented citations, and benchmark numbers without exact provenance will be removed.
