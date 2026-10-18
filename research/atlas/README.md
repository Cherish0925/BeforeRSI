# Research atlas v3

Open `index.html` locally. The front page gives reviewed case counts, affiliation-based sector counts, industrial goals and research questions. This is an ongoing review, not a final field census. Full evidence and the pending catalog remain searchable.

## Sources of truth

- `data/works.json`: 127 stable work IDs and sources.
- `data/quality-review.json`: 38 selected-section mechanism reviews; `core` means a reviewed claim, not main-view eligibility.
- `data/layer-review.json`: route, changed object, return path, model size and placement; unreviewed entries remain unresolved.
- `data/research-brief.json`: concise route syntheses and per-case evidence labels.
- `data/scope-review.json` and `data/mechanisms.json`: versioned relevance and mechanism records. Earlier search snapshots are preserved separately.
- `data/research-atlas.json`: generated joined dataset. `data/knowledge-graph.json`: three routes and 19 main cases.

Model/mixed main cases require an actual trained target with total parameters >=27B. A conservatively derived architecture lower bound can establish the gate without fabricating a full checkpoint count. Active MoE size is separate. Undisclosed size and low value are different judgments. Main cases also carry explicit evidence limits; the set does not mean 19 demonstrated strong-RSI systems.

## Rebuild the current deliverables

```bash
python scripts/build_scope_catalog.py
python scripts/build_mechanism_map.py
ATLAS_CJK_FONT=/absolute/path/to/chinese-font.ttf python scripts/build_research_atlas.py
python scripts/validate.py
node scripts/check_atlas_ui.cjs
```

Requires Pillow, ReportLab and a CJK TrueType font. The Node test runs real page JavaScript in a minimal DOM stub; it is not a browser layout test. The exported PDF is visually inspected separately.
