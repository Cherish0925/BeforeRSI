# AGENTS.md

BeforeRSI is intended to be worked on by multiple human and AI researchers. Agreement with the current repository is not a contribution requirement. The repository should become more correct by making disagreements explicit and testable.

## Read before changing the research model

Use this order:

1. README.md — project question and current mainline;
2. MAP.md — historical and causal map;
3. THEORY.md — current mathematical model;
4. EVIDENCE.md — public evidence and its limits;
5. HYPOTHESES.md — propositions still under test;
6. PROGRAM.md — proposed system and experimental sequence;
7. EVALUATION.md — measurement rules;
8. RESEARCH_LOG.md — how the current representation evolved;
9. SIMULATION.md — illustrative dynamical models.

## Epistemic contract

Every substantive contribution should identify what kind of statement it contains:

- **source fact** — directly supported by a primary paper, repository, benchmark record, released artifact, or raw result;
- **derived consequence** — follows mathematically or logically from stated assumptions;
- **working hypothesis** — plausible but undecided;
- **simulation result** — follows from an explicitly parameterized toy or fitted model;
- **engineering proposal** — a design that has not yet been validated;
- **empirical result** — produced by an experiment with preserved artifacts.

Do not silently convert one category into another.

## How to disagree

A contribution may replace a central assumption if it supplies at least one of:

- a counterexample;
- a competing model with different predictions;
- primary evidence inconsistent with the current claim;
- a cleaner derivation;
- an experiment that discriminates between the alternatives.

Do not preserve a formulation merely because it already appears in several files.

## Theory changes

When changing THEORY.md:

1. state the assumptions;
2. derive the result rather than only naming it;
3. identify measurable variables;
4. state at least one falsifiable prediction;
5. update HYPOTHESES.md if the change alters a working hypothesis;
6. update SIMULATION.md when the change alters simulated dynamics.

A notation change alone is not research progress.

## Evidence changes

When adding or editing public work:

1. use a primary source;
2. record the exact changed object;
3. identify the visible and hidden task distributions;
4. record model, harness, evaluator, and resource budget when available;
5. separate the authors' claim from BeforeRSI's inference;
6. state the strongest claim depth actually supported.

Update data/works.json and the relevant section of EVIDENCE.md together.

## Experimental changes

A new experiment must answer a question that changes the viable RSI models or routes.

Required fields:

- hypothesis or competing models;
- intervention;
- held-fixed variables;
- task cohorts;
- resource accounting;
- primary metric;
- regression metric;
- decisive outcome;
- artifacts required for reproduction.

If a proposed experiment cannot distinguish competing explanations, redesign it before running it.

## Simulation changes

Synthetic simulations are not evidence about real AI systems.

Every simulation must specify:

- equations;
- initial conditions;
- parameter values;
- which quantities are arbitrary;
- which quantities are fitted from data, if any;
- qualitative prediction being illustrated;
- empirical measurements required to identify the model.

Do not describe a synthetic trajectory as a forecast until the parameters have been estimated and validated out of sample.

## Multi-agent workflow

When several agents work in parallel, divide work by claims or experiments rather than by arbitrary document sections.

Useful roles include:

- primary-source auditor;
- mathematical model critic;
- alternative-model builder;
- simulation and system-identification researcher;
- experiment designer;
- reproduction engineer;
- adversarial reviewer.

Each role should leave a compact record of:

- what claim was examined;
- what evidence or derivation was added;
- what changed in the current belief;
- what remains unresolved;
- what next experiment would decide it.

Use RESEARCH_LOG.md only for material changes in representation, evidence, or research direction. Do not dump raw chain-of-thought or chat transcripts into the repository.

## Style

Prefer equations, measured quantities, causal comparisons, exact source links, and executable experiments.

Delete prose that does not change a fact, model, assumption, prediction, experiment, or decision.

The project is allowed to be wrong. It is not allowed to hide which parts are uncertain.