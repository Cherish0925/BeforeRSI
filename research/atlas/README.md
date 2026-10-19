# RSI Field Atlas v5

Open **`RSI_Field_Atlas_v5.html`** locally; `index.html` contains the same reader. The homepage immediately renders three field-level graphs. The named file avoids confusing this version with the earlier downloads.

## Reading structure

The field maps contain 29 research themes, 146 subquestions and 60 conceptual relations. A theme explains its scientific/engineering question, mechanism, methods, connected themes and associated papers/teams. The full-route view can expand every subquestion. Conceptual connections are editorial structure supported by primary examples; they are not paper-citation claims. Paper-relation views remain available separately.

The three maps organize mutable external assets and improvement processes (Harness), learning-feedback mechanisms (Model), and parameter/system coupling (Model × Harness). Training stage, objective, online data collection, role and schedule are orthogonal descriptors. Sequential internalization does not establish bidirectional coevolution. The reader contains public research only.

## Corpus and scope

| Primary route | Records | Methods read | Source screens | Default paper view |
|---|---:|---:|---:|---:|
| Harness | 40 | 19 | 21 | 40 |
| Model | 35 | 15 | 20 | 29 |
| Model × Harness | 22 | 8 | 14 | 19 |

Eight cross-route references and 22 historical/background records bring the catalog to 127. Forty-five records have selected-method readings (including three cross-route references); 60 remain source screens. The route totals include adjacent AI4AI mechanisms and provisional cases, not just established recursive systems. Nine confirmed sub-27B Model/mixed references are hidden by default; unknown trained-target size remains explicit.

There are 45 paper relations: 15 source-explicit and 30 editorial method comparisons. Missing connections remain unfinished coverage. Twenty-seven A–F explanations were rewritten in this version. The older 38-claim/19-case review is retained separately and is not a field census.

## Sources of truth

- `data/works.json`: stable bibliography, changed objects, source URLs and central limits.
- `data/field-knowledge.json`: field themes, subquestions, conceptual links and paper placements.
- `data/literature-editorial.json`: paper explanations, principal routes, reading scope and paper relations.
- `data/literature-reading-updates.json`: bounded source readings and classification/scale corrections from this update.
- `data/literature-affiliation-sources.json`: title-page affiliation checks.
- `data/literature-atlas.json`: generated joined reader dataset.
- `data/knowledge-graph.json`: typed field, paper, mechanism and institution graph.

`field-guide.md` is the textual field map; `literature-cards.md` and `references.md` contain the current cards and sources. Earlier `core-cards.md`, legacy review JSON and the nine-page PDF are dated review snapshots.

## Rebuild and verify

```bash
python scripts/build_literature_graphs.py
python scripts/validate.py
node scripts/check_atlas_ui.cjs
```

No network, API key, external JavaScript or server is needed by the HTML. The build uses Python's standard library. Set `CHROMIUM_PATH`, optionally `PLAYWRIGHT_MODULE`, and `ATLAS_SCREENSHOTS` for real-browser checks and exports. A CJK font must be available for Chinese screenshots.

Chromium checks cover first-screen graphs, all three routes, expanded subquestions, topic and relation inspection, paper/field navigation, all cards, search, scale filters, keyboard interaction, desktop and mobile overflow. Data checks verify exact embedded content, provenance, classification corrections and preservation of all 127 IDs. No paper was independently replicated.
