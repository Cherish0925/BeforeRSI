# Research atlas

Open `index.html` locally for the complete offline catalog. No network is used until a source link is opened. The default knowledge tree includes admitted claims only; the complete bibliography is a separate view.

## Sources of truth

- `data/works.json`: stable work IDs and source URLs.
- `data/scope-review.json`: topical relevance and earlier reading boundaries.
- `data/quality-review.json`: manually curated claim cards, admission decisions and relation provenance.
- `data/research-atlas.json`: generated joined dataset.
- `data/knowledge-graph.json`: generated core-only graph; relation provenance is in quality-review.

The atlas does not infer new literature claims, paper quality or affiliations automatically. `core` admits a specified contribution, not every claim in a paper. `pending` is not a low-quality verdict. Historical references are separate from contemporary RSI results. Paper relations distinguish explicit extensions/comparisons from this project's analytical comparisons.

## Rebuild

From the repository root, with Python, ReportLab, Pillow and a CJK-capable TrueType font:

```bash
python scripts/build_mechanism_map.py
python scripts/build_scope_catalog.py
ATLAS_CJK_FONT=/absolute/path/to/chinese-font.ttf python scripts/build_research_atlas.py
python scripts/validate.py
```

The PDF is `output/pdf/beforersi-research-atlas.pdf`. PNG/SVG diagrams are under `assets/atlas/`. The HTML template is `scripts/atlas-template.html`. It embeds all data and uses no external JavaScript, styles, fonts or data fetches. Relative PDF/Markdown links work within the repository checkout; when the HTML is downloaded alone, original-source links and all catalog interactions remain self-contained.

`schema_version: 2.0.0` of the canonical graph intentionally replaces the previous unfiltered concept-to-corpus binding. Only the 23 admitted work IDs are bound; the remaining catalog remains accessible through the bibliography. Validation prevents pending/background/low-value works from entering the core graph and checks exact HTML/data agreement.
