#!/usr/bin/env python3
"""Render explicit human/assistant scope decisions; never infer RSI from titles."""
import json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
LABELS={'direct':'直接自进化研究','enabler':'直接支撑的 AI4AI/学习机制','evaluation':'评测与反例','theory':'RSI 理论','foundation':'历史/机制基础','background':'移出核心的背景'}
LEGACY_GROUPS={
 'theory':'good-1965 godel-machine',
 'foundation':'eurisko maml alphago-zero automl-zero funsearch learned-optimizer-2016 poet self-training-optimizer-2020 expert-iteration dreamcoder selecting-computations levin-tree-search policy-guided-heuristic-search lts-context-models',
 'background':'openai-o1 deepseek-r1 qwen3 muzero xland co-scientist',
 'evaluation':'statistical-limits harness-updating-benefit rethink-harness-eval harness-tampering',
 'enabler':'spin adas aflow gepa agentbreeder evoharness-rl ace alphaevolve opro star rest-em alphaproof constitutional-ai eureka automated-alignment-researchers seed-for-seed',
 'direct':'stop promptbreeder self-rewarding-lm godel-agent sica dgm seal hyperagents sia rhi co-harness helix hsi harnessdev rrsi meta-harness aide2 openrsi mass rsi-anything dream-rsi hgm sima2 self-taught-evaluators gpt-red',
}
LEGACY_CLOSURE={
 'stop':'self_reuse','promptbreeder':'self_reuse','self-rewarding-lm':'self_reuse',
 'godel-agent':'self_edit','sica':'self_edit','dgm':'self_reuse','seal':'self_reuse',
 'hyperagents':'self_reuse','sia':'coevolution','rhi':'self_reuse',
 'co-harness':'coevolution','helix':'proposed_weight_return','hsi':'self_reuse',
 'harnessdev':'unclear','rrsi':'self_reuse','meta-harness':'unclear',
 'aide2':'fixed_outer_proposer','openrsi':'coevolution','mass':'coevolution',
 'rsi-anything':'unclear','dream-rsi':'learned_improver','hgm':'self_reuse',
 'sima2':'self_reuse','self-taught-evaluators':'self_reuse','gpt-red':'coevolution',
}
def load(p):return json.loads((ROOT/p).read_text())
def save(p,x):(ROOT/p).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def marked(p,marker,body):
 text=(ROOT/p).read_text();text=text.split(marker)[0].rstrip()
 (ROOT/p).write_text(text+'\n\n'+marker+'\n'+body.rstrip()+'\n')
def main():
 works=load('data/works.json')['works']; reviews=load('data/expansion-reviews.json')['works'];new={r['id']:r for r in reviews}
 mechanisms={r['id']:r for r in load('data/mechanisms.json')['works']}
 legacy={wid:s for s,ids in LEGACY_GROUPS.items() for wid in ids.split()}
 assert len(legacy)==67 and len(new)==56
 assert set(legacy).isdisjoint(new)
 assert set(legacy)|set(new)=={w['id'] for w in works}
 entries=[]
 for w in works:
  wid=w['id'];m=mechanisms[wid];r=new.get(wid)
  scope=r['scope'] if r else legacy[wid]
  entries.append({'id':wid,'name':w['name'],'year':w['year'],'scope':scope,
   'closure_assessment':r['closure'] if r else LEGACY_CLOSURE.get(wid,'not_claimed'),
   'operation':r['reported_operation'] if r else m['mechanism_interpretation'],
   'boundary':w['central_limit'],'reading_scope':m['review_scope'],
   'primary_source':w['sources'][0]['url'],
   'provenance':'2026-10-18 expansion' if r else 'previous corpus; reclassified, not all freshly re-read'})
 counts=Counter(e['scope'] for e in entries)
 deferred=[
  {'arxiv_id':'2606.29871','status':'defer','reason':'人工构造训练故障上的有界控制案例；暂未显示控制器本身学习，先保留为候选，非断言无价值。'},
  {'arxiv_id':'2606.28374','status':'defer','reason':'摘要中的 held-out 接受集实际参与反复选择；单调安全的外推需核全文，不据摘要认证。'},
  {'arxiv_id':'2606.21090','status':'defer','reason':'有限模型/任务上的退化案例，需核完整协议与资源；当前以 Aspire 等覆盖此问题，暂不重复扩容。'},
  {'arxiv_id':'2610.11613','status':'defer','reason':'与2025 AgentEvolver同名但不同工作；保留最新候选，独立任务迁移和总开发成本未明确。'},
  {'arxiv_id':'2406.18532','status':'defer','reason':'符号优化的早期机制候选；需进一步区分目标代理优化和改进器自身更新。'},
  {'arxiv_id':'2609.33867','status':'retrieval_incomplete','reason':'检索得到摘要线索但原始正文/摘要页面重复获取失败，本轮不升级为正式证据。'},
  {'arxiv_id':'2608.20290','status':'retrieval_incomplete','reason':'原始页面未成功获取，不用二手摘要代替原文核查。'},
  {'arxiv_id':'2608.27287','status':'retrieval_incomplete','reason':'检索到工业部署线索，原始页面未成功取得，待核。'},
  {'arxiv_id':'2605.15034','status':'excluded_wrong_query','reason':'本轮把RL Tango的2505误输入为2605，实际是社会观察语境研究；已更正为2505.15034，排除误检项。'},
 ]
 save('data/scope-review.json',{'updated':'2026-10-18','definitions':LABELS,
  'warning':'Scope is topical relevance, not proof of successful RSI or a quality ranking. Closure labels are evidence-qualified interpretations. A broad bibliography is not a denominator for coverage.',
  'counts':dict(counts),'works':entries,'deferred_or_excluded':deferred})
 lines=['# RSI 与 AI4AI 分层研究目录','',f'共 {len(entries)} 条。56 条为本轮新增原始来源初筛，其中 10 条选读关键方法、定义或结果段落；不是 123 篇全文审查或独立复现。',
 '旧条目保留原有阅读深度；范围重新分类不提升证据等级。直接自进化研究是主题标签，不等于已证实更强的递归改进能力。',
 '完整阅读边界见 data/scope-review.json；新增工作的任务、资源和干预见 data/expansion-reviews.json。','',
 '| 分层 | 数量 |','|---|---:|']
 lines.extend(f'| {LABELS[s]} | {counts[s]} |' for s in LABELS)
 for s in LABELS:
  lines+=['',f'## {LABELS[s]}','', '| 工作（首次公开年份） | 改了什么、如何反馈 | 尚不能推出什么 |','|---|---|---|']
  for e in entries:
   if e['scope']==s:lines.append(f"| [{e['name']}]({e['primary_source']})（{e['year']}） | {e['operation']} | {e['boundary']} |")
 lines+=['','## 延后与排除记录','','| 原始来源 | 处置 | 原因 |','|---|---|---|']
 lines.extend(f"| [{r['arxiv_id']}](https://arxiv.org/abs/{r['arxiv_id']}) | {r['status']} | {r['reason']} |" for r in deferred)
 (ROOT/'research/scope-catalog.md').write_text('\n'.join(lines)+'\n')
 ev=['## Scope-focused expansion: 56 primary-source screens','',
 'The operation column paraphrases author reports. Scope, limits and counterfactuals are our judgments. These entries have not been independently reproduced. Ten have selected primary sections read; the other 46 remain abstract-level screens. Full GPU/API cost accounting is not inferred where it is absent from the inspected passage.',
 'Read RSI_SCOPE.md and research/scope-catalog.md before interpreting the corpus count as a count of RSI systems.','',
 '| Work | Reported changed operation | Tasks / resource boundary | Scope / limitation |','|---|---|---|---|']
 for r in reviews:ev.append(f"| [{r['name']}]({r['sources'][0]['url']}) | {r['reported_operation']} | {r['tasks_and_resources']} | {LABELS[r['scope']]}：{r['limit']} |")
 marked('EVIDENCE.md','<!-- scope-expansion -->','\n'.join(ev))
 comp=['## Scope-focused expansion mappings','',
 'These mappings preserve named artifacts; they neither prove recursion nor supply a predictive theory. See RSI_SCOPE.md for distinctions.','',
 '| Work | Artifacts requiring representation | Boundary |','|---|---|---|']
 for r in reviews:comp.append(f"| [{r['name']}]({r['sources'][0]['url']}) | {', '.join(r['changed_objects'])} | {r['limit']} |")
 marked('COMPATIBILITY.md','<!-- scope-expansion -->','\n'.join(comp))
 print(json.dumps({'total':len(entries),'scopes':counts,'new':len(reviews),'new_2026':sum(r['year']==2026 for r in reviews)},ensure_ascii=False))
if __name__=='__main__':main()
