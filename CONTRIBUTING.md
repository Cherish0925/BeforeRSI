# Contributing

BeforeRSI accepts contributions that change the evidence, the map, or the experimental capability of the project.

Useful contributions include:

- a primary source missing from the corpus;
- a correction to a factual claim or project classification;
- a source audit that records exact tasks, budgets, models, evaluators, generations, and released artifacts;
- a reproducible rerun;
- an independent replication;
- a counterexample or negative result;
- code required for one of the registered experiments;
- a machine-readable update to the knowledge graph supported by primary sources.

Do not submit:

- generic summaries generated from abstracts;
- rankings based on project names, stars, or reported benchmark deltas;
- new terminology without a new measurable consequence;
- architecture diagrams unsupported by implementation or experiment;
- a claim of recursion based on one persistent update;
- benchmark numbers without exact model, harness, task split, evaluator, and resource budget;
- dozens of weakly related papers added for coverage.

Every substantive claim should link to a primary paper, repository, released artifact, benchmark record, or raw experiment. Survey papers may justify coverage, not empirical conclusions.

## Evidence status

Use one of:

- `reported`
- `reproduced`
- `replicated`
- `contradicted`
- `open`

State the claim being labeled. Do not label an entire project `reproduced` because one number was rerun.

## Work entry

A new work in `data/works.json` must specify:

- year;
- role in the RSI mainline;
- strongest public claim depth;
- changed objects;
- primary sources;
- central limitation;
- audit state.

## Experimental contribution

An experiment must include the registered hypothesis, task cohorts, resource budget, parent and successor manifests, lineage, raw results, and analysis code.

Negative results are accepted when they rule out a route, expose a confound, establish a scale boundary, or falsify a claim.
