# Literature atlas v4

Open `index.html` locally. The three route graphs are the main reading interface. Search covers all 127 records, including historical/background references. This reader contains public literature only.

## Current corpus

| Route | Catalog positions | Selected methods read | Abstract screens | Default graph |
|---|---:|---:|---:|---:|
| Harness | 38 | 16 | 22 | 38 |
| Model | 34 | 14 | 20 | 29 |
| Model × Harness | 25 | 8 | 17 | 22 |

Eight additional evaluation/theory references and 22 historical/background records make 127. Positions include related AI4AI mechanisms and provisional screens; they are not a count of established RSI systems. Eight known sub-27B Model/mixed references are hidden by default. Unknown size is not a passed size gate.

There are 43 explained paper-to-paper edges: 13 source-explicit relationships and 30 editorial method comparisons. Affiliation and mechanism edges have separate types and provenance. Missing edges are unfinished relationship coverage, not evidence of no connection.

## Sources of truth

- `data/works.json`: stable bibliography and primary URLs.
- `data/literature-editorial.json`: current Chinese descriptions, reading status, principal route, multiple method positions, and explained relationships.
- `data/literature-affiliation-sources.json`: the additional primary-source affiliation checks, including read versions.
- `data/literature-atlas.json`: joined current reader dataset.
- `data/knowledge-graph.json`: work, mechanism and institutional nodes, typed edges and route views.
- `data/quality-review.json`, `data/layer-review.json`, `data/research-brief.json`, `data/research-atlas.json`: earlier selected-claim and scale review. The prior 38 claim reviews/19-case shortlist are not overwritten by a broader literature landscape.

Cards use six reading angles when supported. Abstract screens remain short rather than inventing method-level detail. See `literature-cards.md` for the text companion and `references.md` for sources. `core-cards.md` and the nine-page PDF are earlier review snapshots, not current route counts.

## Rebuild and verify

```bash
python scripts/build_literature_graphs.py
python scripts/validate.py
node scripts/check_atlas_ui.cjs
```

The reader needs no network, external JavaScript, service or API key. The main build uses Python's standard library. `build_research_atlas.py` rebuilds the older evidence join and PDF first, then invokes the current graph renderer; it additionally needs Pillow, ReportLab and a CJK font.

Set `CHROMIUM_PATH` and optionally `PLAYWRIGHT_MODULE` to run the same interaction checks in a real browser. Set `ATLAS_SCREENSHOTS` to export desktop/mobile previews and the three standalone SVG views. On 2026-10-19, Chromium checks passed at 1440×1000 and 390×844, including route filters, graph selection, relationship inspection, cards, institution-aware search and page overflow. No literature experiment was independently reproduced.
