#!/usr/bin/env python3
"""Render reviewed scope records without overwriting manual evidence."""
import json
from collections import Counter
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def main():
    data = json.loads((ROOT / 'data/scope-review.json').read_text())
    works = json.loads((ROOT / 'data/works.json').read_text())['works']
    entries = data['works']
    assert len(entries) == len(works)
    assert {e['id'] for e in entries} == {w['id'] for w in works}
    counts = Counter(e['scope'] for e in entries)
    assert dict(counts) == data['counts']
    labels = data['definitions']
    lines = ['# RSI 与 AI4AI 范围目录', '',
             f'当前目录 {len(entries)} 项；主题相关性不等于已证实 RSI，也不是质量排名。',
             '三条路线的重点案例、审查进度与规模条件见 [研究导读](../RESEARCH_ATLAS.md)。',
             '本文件从人工维护的 data/scope-review.json 生成；不改变阅读深度，不重写 EVIDENCE.md。', '',
             '| 范围 | 数量 |', '|---|---:|']
    lines.extend(f'| {labels[s]} | {counts[s]} |' for s in labels)
    for scope, label in labels.items():
        lines += ['', f'## {label}', '',
                  '| 工作（首次公开年份） | 改了什么、如何反馈 | 证据边界 |',
                  '|---|---|---|']
        for e in entries:
            if e['scope'] == scope:
                lines.append(f"| [{e['name']}]({e['primary_source']})（{e['year']}） | {e['operation']} | {e['boundary']} |")
    lines += ['', '## 延后与排除记录', '', '| 原始来源 | 处置 | 原因 |', '|---|---|---|']
    for e in data['deferred_or_excluded']:
        lines.append(f"| [{e['arxiv_id']}](https://arxiv.org/abs/{e['arxiv_id']}) | {e['status']} | {e['reason']} |")
    (ROOT / 'research/scope-catalog.md').write_text('\n'.join(lines) + '\n')
    print(json.dumps({'total': len(entries), 'scopes': counts}, ensure_ascii=False))

if __name__ == '__main__':
    main()
