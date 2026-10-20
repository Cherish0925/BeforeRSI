# Reading and building the documentation

- [Learning guide](model-llm.md): canonical Chinese text, 29 chapters and four appendices.
- [PDF](Model_LLM_Learning_Manual.pdf): printable guide with bookmarks.
- [Interactive atlas](index.html): download and open in a browser; includes the guide, search and an embedded PDF. No server is required.

## Sources

| Source | Purpose |
|---|---|
| `docs/model-llm.md` | Guide text, formulas, references and indexes |
| `data/atlas.json` | Atlas works, relations, classification and review status |
| `web/atlas.html` | Atlas interface template |
| `web/learning.css`, `web/learning.js` | Tutorial interface |
| `scripts/build_learning.py` | PDF, figures and standalone HTML generation |

`data/works.json` is the smaller research catalog used by the theory and experimental program. It has its own schema and claim annotations. Atlas inclusion does not imply completed full-text review; consult each record and the reading-coverage fields.

## Build

From the repository root, with Python 3.12:

```bash
python -m pip install -r requirements-docs.txt
python scripts/build_learning.py
python scripts/validate.py
```

The first build downloads a pinned, checksum-verified Noto Sans SC font. Subsequent builds use `.cache/learning/`. Font licensing is in `assets/fonts/OFL.txt`. Generated outputs are `docs/Model_LLM_Learning_Manual.pdf`, `docs/index.html` and `docs/figures/*.svg`; commit them with their source changes so readers can use the project without a build environment.

Update prose in Markdown and literature records in JSON. Generated HTML and PDF are rebuilt from those sources.
