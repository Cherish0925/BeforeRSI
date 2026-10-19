#!/usr/bin/env python3
"""Render canonical mechanism reviews; do not regenerate editorial decisions."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def main():
    rows = json.loads((ROOT / 'data/mechanisms.json').read_text())['works']
    works = json.loads((ROOT / 'data/works.json').read_text())['works']
    assert len(rows) == len(works)
    assert {r['id'] for r in rows} == {w['id'] for w in works}
    lines = ['# Per-work mechanism map', '',
             f'All {len(rows)} current bibliography entries are indexed. Indexing is not a full-paper review.',
             'Mechanism interpretations and proposed interventions are not independently reproduced results.',
             'Exact reading boundaries are preserved in data/mechanisms.json; selected claim reviews are in data/quality-review.json.',
             'Use [the concise research guide](../RESEARCH_ATLAS.md) for current route counts and screening status.', '',
             '| Work | Causal operation | Condition or failure | Separating intervention |',
             '|---|---|---|---|']
    for r in rows:
        lines.append(f"| [{r['name']}]({r['sources'][0]['url']}) | {r['mechanism_interpretation']} | {r['condition_or_failure']} | {r['separating_intervention']} |")
    lines += ['', 'The separating interventions are proposals, not claims that those experiments were performed.']
    (ROOT / 'research/mechanism-map.md').write_text('\n'.join(lines) + '\n')
    print(f'Rendered {len(rows)} mechanism records; manual data unchanged.')

if __name__ == '__main__':
    main()
