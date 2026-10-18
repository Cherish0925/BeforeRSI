# Research atlas v2

Open `index.html` locally. The three primary routes are Harness, Model, and Model × Harness. The standalone HTML contains all records and needs no network until a source link is opened. Repository-relative PDF/Markdown links require the companion files.

## Sources of truth

- `data/works.json`: stable work IDs and source URLs.
- `data/scope-review.json`: earlier topical relevance and reading limits, preserved separately.
- `data/quality-review.json`: 24 claim reviews, contribution/admission judgments and relation provenance. `core` now means reviewed claim, not main-view eligibility.
- `data/layer-review.json`: independent layer, scale, return-path and placement review; all 123 entries receive a disposition, unresolved entries remain unresolved. This is manually reviewed data.
- `research/atlas/classification.md`: boundary conventions and the distinction between representation, explanation and prediction.
- `data/research-atlas.json`: generated joined dataset, including all sources and references.
- `data/knowledge-graph.json` v3: three route nodes and exactly the 12 eligible main-view works. Relationships are filtered to these endpoints without deleting the underlying reference records.

Model/mixed admission uses actual trained-target total parameters >=27B; active MoE parameters and adapter training are separately disclosed. Teacher sizes cannot satisfy this gate. A mixed paper may retain only its eligible scale branch. Main-view inclusion still does not certify sustained recursive improvement; one-pass joint adaptation is explicitly labeled.

## Rebuild

```bash
python scripts/build_mechanism_map.py
python scripts/build_scope_catalog.py
ATLAS_CJK_FONT=/absolute/path/to/chinese-font.ttf python scripts/build_research_atlas.py
python scripts/validate.py
node scripts/check_atlas_ui.cjs
```

Requires Python, Pillow, ReportLab and a CJK TrueType font. The builder creates the PDF, PNG/SVG figures, Markdown and offline HTML from the same evidence. It does not infer paper quality, parameter counts or novelty automatically.

Validation checks complete unique dispositions, actual >=27B trained targets for Model/mixed main entries, core/scale/main separation, graph membership and exact HTML/data agreement. The 18 research-space positions are analytical design coordinates, not an exhaustive mechanism taxonomy or claims of worldwide gaps.

The Node check executes the page’s actual JavaScript with a minimal DOM stub. It verifies navigation, filters and 123 work dialogs; it is not a browser rendering or responsive-layout test. The exported PDF is visually inspected separately.
