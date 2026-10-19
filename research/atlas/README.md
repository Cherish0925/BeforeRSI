# RSI Field Atlas v5.1

Open **`RSI_Field_Atlas_v5_1.html`** locally. `index.html` is identical. The reader works offline, without a server, API key, external script or network connection. Source links open the original publications when a connection is available.

## Three maps, one corpus

The first screen shows the **Harness**, **Model** and **Model × Harness** field graphs. They contain 29 themes, 146 subquestions and 60 conceptual relations. Click a theme to see its research question, mechanisms, associated work and institutions. Paper-to-paper relations are a separate view: 34 source-explicit links and 35 editorial method comparisons, each with provenance.

The route is determined by what actually changes. A frozen large-model teacher is not a trained target. A learned small controller can be part of a harness. Sequential distillation is distinguished from repeated bidirectional coevolution. Training stage, data collection, objective, roles and schedule are additional descriptors rather than competing taxonomies.

| Principal route | Records | Paper main text, experiments and relevant appendices | Official public materials |
|---|---:|---:|---:|
| Harness | 52 | 43 | 9 |
| Model | 36 | 36 | 0 |
| Model × Harness | 22 | 21 | 1 |
| **Three routes** | **110** | **100** | **10** |

The catalog also contains nine cross-route evaluation/theory references and 22 historical/background records: **141 records overall**, including the previous 138 and three additions (Reflexion, ReasoningBank, HASE). Across the full catalog, 113 have paper main-text/experiment/relevant-appendix readings, 17 have explicitly bounded method/result-section readings, and 11 have official-public-material readings. These are reading scopes, not quality certifications or independent replications. Materials not disclosed by a company remain unknown.

The three routes include 70 route-research records, 37 enabling methods and three cases with insufficient mechanism disclosure. They are not 110 demonstrations of strong recursive improvement. Thirty known sub-27B Model/mixed records appear in the supplementary view; enabling it restores all 110 route records from the default 80. Small scale is a viewing preference, not a quality rejection. Undisclosed or internally inconsistent model sizes remain marked as unverified.

## Discovery pool: every disposition is inspectable

The 567 unique arXiv leads have original metadata and abstracts. Eighty-six identifiers match catalog sources; the other 481 are individually screened. A study may have multiple arXiv identifiers, and company releases may have none, so this is not a one-to-one comparison with the 141 study records.

| Current disposition | Leads |
|---|---:|
| Linked to catalog records | 86 |
| Route/method candidates; full reading pending | 240 |
| Evaluation/theory candidates | 64 |
| Enabling/background references | 133 |
| Surveys/roadmaps | 17 |
| Outside the current scope | 27 |
| **Total** | **567** |

**No lead has been excluded on a demonstrated low-quality judgment.** Absence from the map is not evidence of worthlessness. The Coverage page provides title/author/ID/abstract search, disposition filters, individual reasons and source links. [The textual ledger](discovery-ledger.md) preserves the same decisions. This is an auditable research inventory, not a claim of worldwide completeness.

## Reading and navigation

Each work has an A–F explanation: goal/value; research judgment; problem/theory; method; implementation/feedback; results/transfer. The expanded evidence panel records changed and fixed objects, feedback and inheritance, experimental comparisons, ablations, cost, generalization and exact source locations. It distinguishes author-reported results from survey interpretation.

The “读懂 RSI” guide explains how to read the feedback loop. Search supports Chinese and English names, institutions, mechanisms and company aliases. Institution and team views provide a route-by-participant matrix, collaboration filters and work lists. Academic, large-technology-company, specialist-AI-company and independent-research categories describe participants; they do not rank quality. Joint work can appear in more than one participant row.

The company index contains 27 profiles, including research-linked firms, declared directions and adjacent programs. Publication, coauthorship and hosting are separate relations. Discovery Loop is a declared direction with limited disclosed mechanism; founders' previous work is not assigned to the new company. MetaCircle, Apex, Nous, Recursive, Intology and Autoscience have explicit entries and source boundaries.

## Sources of truth

- `data/works.json`: bibliography, changed objects, sources and strongest supported claims.
- `data/literature-editorial.json`: A–F explanations, routes, reading scopes and paper relations.
- `data/primary-reading.json`: all 141 structured readings, corrections and unresolved source questions.
- `data/discovery-review.json`: all 567 original abstracts, dispositions and reasons.
- `data/field-knowledge.json`: themes, subquestions, conceptual relations and work placements.
- `data/research-actors.json`: canonical institutions, aliases and participant categories.
- `data/industry-landscape.json`: company profiles, publication roles and declared directions.
- `data/industry-reading-log.json`: company-material access and disclosure limits.
- `data/literature-atlas.json` and `data/knowledge-graph.json`: generated reader and typed graph.

[Field guide](field-guide.md) · [Research cards](literature-cards.md) · [References](references.md) · [Actors](actor-guide.md) · [Companies](industry-guide.md) · [Discovery ledger](discovery-ledger.md).

The older claim audit, 127-item scope review and nine-page PDF remain dated snapshots. They do not describe the current reading status or establish a field census. Current evidence is in the files above.

## Rebuild and verification

```bash
python scripts/build_literature_graphs.py
python scripts/check_literature_graphs.py
node scripts/check_atlas_ui.cjs
```

The Python build uses the standard library. Set `CHROMIUM_PATH`, optionally `PLAYWRIGHT_MODULE`, and `ATLAS_SCREENSHOTS` for browser checks. A CJK font is required for Chinese screenshot rendering. Checks cover exact embedded data, stable identifiers, reading coverage, routes/scale, field and paper relations, search, cards, company/institution navigation and desktop/mobile layout. Reported research experiments have not been independently reproduced.
