# Working on BeforeRSI

## Sources and build

- Edit `web/`, `data/landscape.json`, `data/locales/en.json` and the manual Markdown sources. Generate the HTML, ZIP, PDFs and figures with `python scripts/build_learning.py`; use `--web-only` when manuals are unchanged.
- Preserve stable IDs, source links and the original review notes. Keep Chinese and English aligned on mechanisms, numbers, references and coverage.
- Run `python scripts/validate.py`. For interface changes, also run `node scripts/test_landscape.cjs` with Playwright and Chromium available. Inspect both languages and narrow screens.
- Commit generated deliverables with the changes that produce them. Build details: [docs/README.md](docs/README.md).

## Research model

Before changing the model, read README → MAP → THEORY → EVIDENCE → HYPOTHESES → PROGRAM → EVALUATION → RESEARCH_LOG → SIMULATION.

Identify whether a claim is a source fact, derived consequence, working hypothesis, simulation result, engineering proposal or empirical result. Keep that status attached to the claim.

A revision to the theory should provide assumptions, a derivation, measurable variables and a falsifiable prediction. Update affected hypotheses and simulations together. Replace existing formulations when a counterexample, primary evidence, cleaner derivation or competing model supports the change.

## Literature

Use primary papers, repositories, technical releases, benchmark records or raw results. Record:

- the changed object and inherited state;
- fixed components and model roles;
- visible and held-out tasks;
- feedback, resource budget and measured result;
- the authors' claim and any additional inference.

Update the landscape and English entry together. When a work changes the research program's argument, also update `data/works.json`, `EVIDENCE.md` and its Chinese counterpart.

## Experiments and simulations

An experiment specifies the competing explanations, intervention, fixed variables, task cohorts, resource accounting, primary and regression metrics, decisive outcome and reproduction artifacts.

A simulation specifies its equations, initial conditions, parameters, arbitrary or fitted quantities, qualitative prediction and the empirical measurements needed to identify the model. Synthetic trajectories illustrate the stated assumptions; empirical forecasts require fitted parameters and out-of-sample validation.

## Writing

Use direct language, exact source links and concrete mechanisms. Remove repeated framing, unsupported rankings and prose that adds no fact, explanation, assumption or decision.

Use `RESEARCH_LOG.md` for material changes in representation, evidence or research direction, with alternatives and the experiment that would distinguish them. Keep raw conversation transcripts out of the repository.
