#!/usr/bin/env python3
"""Compile explicit, source-backed selection decisions; never infer quality.

During reading this produces a transparent progress ledger. --require-complete
is the release gate: every source entry must have a review or a documented
primary-source access block. Downloading, abstracts and generated prose do not
satisfy this gate.
"""
import argparse
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DECISIONS = {
    'core': '重点研究',
    'support': '方法与证据补充',
    'mechanism_supplement': '范围外规模的机制参考',
    'redundant': '相近工作，索引保留',
    'outside': '本综述范围外',
    'insufficient': '公开证据不足',
    'blocked': '原文获取受阻',
}
READINGS = {'full_primary', 'previous_primary_rechecked', 'public_materials', 'blocked'}
ROUTES = {'harness', 'model', 'hybrid', 'crosscut', 'background', 'outside'}


def compile_corpus(entries, reviews_dir, require_complete=False):
    entries_by_id = {e['entry_id']: e for e in entries}
    assert len(entries_by_id) == len(entries), 'Duplicate source entry IDs'
    reviewed = {}
    for path in sorted(reviews_dir.glob('*.jsonl')):
        for number, line in enumerate(path.read_text().splitlines(), 1):
            if not line.strip():
                continue
            r = json.loads(line)
            eid = r['entry_id']
            assert eid in entries_by_id, f'{path}:{number}: unknown {eid}'
            assert eid not in reviewed, f'Duplicate review: {eid}'
            assert r['route'] in ROUTES, f'{eid}: invalid route'
            assert r['reading']['status'] in READINGS, f'{eid}: invalid reading coverage'
            decision = r['selection']['decision']
            assert decision in DECISIONS, f'{eid}: missing explicit selection'
            assert r['selection']['reason'].strip(), f'{eid}: selection has no reasoning'
            if r['reading']['status'] == 'blocked':
                assert decision == 'blocked', f'{eid}: blocked source given a merit judgment'
                assert r['reading'].get('unread_or_undisclosed'), f'{eid}: unexplained access block'
            else:
                assert r['reading'].get('sources'), f'{eid}: no primary-source locations'
                assert r['reading'].get('coverage'), f'{eid}: no reading coverage'
                for field in ('mechanism', 'experiment', 'contribution'):
                    assert r.get(field), f'{eid}: missing {field}'
            if decision == 'core':
                assert r['reading']['status'] in {'full_primary', 'previous_primary_rechecked', 'public_materials'}, eid
                assert {s['axis'] for s in r.get('sections', [])} == set('ABCDEF'), f'{eid}: incomplete core explanation'
            r['review_batch'] = path.stem
            reviewed[eid] = r
    rows = []
    for e in entries:
        row = {k: e.get(k) for k in ('entry_id', 'arxiv_id', 'version', 'title', 'year', 'authors', 'work_id', 'source_urls')}
        row['review'] = reviewed.get(e['entry_id'])
        rows.append(row)
    pending = [x['entry_id'] for x in rows if x['review'] is None]
    if require_complete:
        assert not pending, f'{len(pending)} entries have no completed review: {pending[:8]}'
    decisions = Counter(r['selection']['decision'] for r in reviewed.values())
    readings = Counter(r['reading']['status'] for r in reviewed.values())
    route_counts = {}
    for route in sorted(ROUTES):
        rs = [r for r in reviewed.values() if r['route'] == route]
        route_counts[route] = {'reviewed': len(rs), **{d: sum(r['selection']['decision'] == d for r in rs) for d in DECISIONS}}
    return {
        'schema_version': '1.0.0',
        'updated': '2026-10-19',
        'title': '全量原文阅读与比较取舍',
        'selection_is': '综述编辑判断：机制贡献、证据、独特性及本图范围；不将机构规模、参数量或未入主图等同于研究质量。',
        'population': '567条检索线索，加55项未被该检索池覆盖的既有目录记录；按来源记录去重。论文版本合并，后续发现同一工作的多入口另记重复关系。',
        'decisions': DECISIONS,
        'counts': {'total': len(rows), 'reviewed': len(reviewed), 'pending': len(pending), 'selection': dict(decisions), 'reading': dict(readings), 'routes': route_counts},
        'release_complete': not pending,
        'entries': rows,
    }


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--entries', type=Path, default=ROOT/'data/full-reading-entries.json')
    p.add_argument('--reviews', type=Path, default=ROOT/'data/reading-reviews')
    p.add_argument('--output', type=Path, default=ROOT/'data/corpus-review.json')
    p.add_argument('--require-complete', action='store_true')
    args = p.parse_args()
    result = compile_corpus(json.loads(args.entries.read_text()), args.reviews, args.require_complete)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(result['counts'], ensure_ascii=False))
