# Contributing

[English](CONTRIBUTING.md) · [简体中文](CONTRIBUTING.zh-CN.md)

Contributions should improve the evidence, explanations, map or experimental capability of BeforeRSI. Useful changes include missing primary sources, factual corrections, clearer mechanism descriptions, source audits, reproducible experiments and informative negative results.

## Literature and landscape

1. Link a primary paper, repository, technical release, benchmark record or raw result.
2. Identify the changed object, fixed components, feedback, inherited state, model roles, task splits, resource budget and measured result.
3. Update `data/atlas.json` and the matching English entry in `data/locales/en.json`. Preserve stable IDs and distinguish source-supported relationships from editorial comparisons.
4. Describe each work through the six existing sections. Keep quantitative claims tied to their evaluation settings.
5. Add an institution or company relationship only when authorship or an official release supports it.

The 141-record landscape and the smaller research claim index serve different purposes. Add to `data/works.json` when a work changes the theoretical or experimental argument, and update `EVIDENCE.md` and its Chinese counterpart together.

## Manuals and interface

Edit the Markdown or JSON sources, then rebuild. Keep both languages aligned on mechanisms, numbers, references and chapter coverage; idiomatic editing is preferable to literal sentence matching.

```bash
python -m pip install -r requirements-docs.txt
python scripts/build_learning.py
python scripts/validate.py
```

Commit the generated page, PDFs and figures alongside source changes. For interface changes, check both languages, search, deep links, PDF downloads and a narrow viewport. See [build documentation](docs/README.md).

## Research and experiments

A research contribution should identify its status: source fact, derived consequence, working hypothesis, simulation, engineering proposal or measured result. Hypotheses belong in `HYPOTHESES.md` until evidence changes their status.

Experiments record the intervention, fixed components, task cohorts, resource use, parent and successor versions, candidate lineage, raw outcomes and analysis. A negative result is useful when it distinguishes explanations or identifies a boundary.

Evidence labels are `reported`, `reproduced`, `replicated`, `contradicted` and `open`; apply them to a specific claim. For model changes, derivations and disagreement handling, follow [AGENTS.md](AGENTS.md).

Write directly. Keep the facts, assumptions, mechanisms and results that help readers understand the work; remove repeated framing and unsupported rankings.
