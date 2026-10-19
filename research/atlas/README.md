# RSI Field Atlas v5.1

Open **`RSI_Field_Atlas_v5_1.html`** locally; `index.html` contains the same reader. The homepage immediately renders three field-level graphs. The named file avoids confusing this version with the earlier downloads.

## Reading structure

The field maps contain 29 research themes, 146 subquestions and 60 conceptual relations. A theme explains its scientific/engineering question, mechanism, methods, connected themes and associated papers/teams. The full-route view can expand every subquestion. Conceptual connections are editorial structure supported by primary examples; they are not paper-citation claims. Paper-relation views remain available separately.

The three maps organize mutable external assets and improvement processes (Harness), learning-feedback mechanisms (Model), and parameter/system coupling (Model × Harness). Training stage, objective, online data collection, role and schedule are orthogonal descriptors. Sequential internalization does not establish bidirectional coevolution. The reader contains public research only.

## Corpus and scope

| Primary route | Records | Methods read | Source screens | Default paper view |
|---|---:|---:|---:|---:|
| Harness | 49 | 25 | 24 | 49 |
| Model | 36 | 16 | 20 | 30 |
| Model × Harness | 22 | 8 | 14 | 19 |

Nine cross-route references and 22 historical/background records bring the catalog to 138. Fifty-three records have selected-method/mechanism readings (including four cross-route references); 63 remain source screens. The route totals include adjacent AI4AI mechanisms and provisional cases, not just established recursive systems. Nine confirmed sub-27B Model/mixed references are hidden by default; unknown trained-target size remains explicit.

There are 48 research relations: 18 source-explicit and 30 editorial method comparisons. Missing connections remain unfinished coverage. The preceding v5 rewrote 27 A–F explanations; v5.1 adds 11 company research records. The older 38-claim/19-case review is retained separately and is not a field census.

## Companies within the three maps

The company index has 27 profiles: 24 linked to specific research, one declared direction (Discovery Loop), and two adjacent programs whose RSI loop is not established. The profiles link 34 distinct study records. Route counts by a linked work's principal route are {'harness': 18, 'model': 5, 'hybrid': 3}; company counts overlap and are not a census of RSI companies.

MetaCircle, Apex, Nous, Recursive, Intology and Autoscience receive direct company entries. Existing industrial affiliations are also exposed, including Sakana, Weco, iGent, Frontis, Prime Intellect, DeepWisdom, MemTensor, Hexo, IQuest, Langboat, Flower, Bespoke, Etude, TokenWave, Einsia, DeepSeek, Moonshot and Zhipu. Each public work retains its own route, scale and reading status. Startup status, financing and founders' prior employers are not substitutes for method evidence.

Publication, joint authorship and repository hosting use distinct edges. Declared company directions use a different edge from observed study mechanisms. The search accepts Chinese company aliases and project names, and company/study/topic navigation works in both directions.

## Sources of truth

- `data/industry-landscape.json`: companies, names, publication roles, sources and declared directions.
- `data/industry-reading-log.json`: the 11 added releases and source access limits.
- `data/review-snapshots.json`: immutable legacy review membership and hashes.
- `data/works.json`: stable bibliography, changed objects, source URLs and central limits.
- `data/field-knowledge.json`: field themes, subquestions, conceptual links and paper placements.
- `data/literature-editorial.json`: paper explanations, principal routes, reading scope and paper relations.
- `data/literature-reading-updates.json`: bounded source readings and classification/scale corrections from this update.
- `data/literature-affiliation-sources.json`: title-page affiliation checks.
- `data/literature-atlas.json`: generated joined reader dataset.
- `data/knowledge-graph.json`: typed field, study, mechanism, institution and company graph.

`industry-guide.md` lists company–work associations. `field-guide.md` is the textual field map; `literature-cards.md` and `references.md` contain the current cards and sources. Earlier `core-cards.md`, legacy review JSON and the nine-page PDF are dated review snapshots.

## Rebuild and verify

```bash
python scripts/build_literature_graphs.py
python scripts/validate.py
node scripts/check_atlas_ui.cjs
```

No network, API key, external JavaScript or server is needed by the HTML. The build uses Python's standard library. Set `CHROMIUM_PATH`, optionally `PLAYWRIGHT_MODULE`, and `ATLAS_SCREENSHOTS` for real-browser checks and exports. A CJK font must be available for Chinese screenshots.

Chromium checks cover first-screen graphs, all three routes, expanded subquestions, topic and relation inspection, paper/field navigation, all cards, search, scale filters, keyboard interaction, desktop and mobile overflow. Data checks verify exact embedded content, provenance, classification corrections and preservation of all 127 earlier IDs and coverage of all 138 current records. No paper was independently replicated.

The company checks cover all 27 dialogs, Chinese/English/name alias searches, company-to-work and work-to-company navigation, directions without studies, related-company topic links, and mobile dialog overflow.
