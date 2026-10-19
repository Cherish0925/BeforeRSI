# RSI 三路线知识图谱

[打开交互式综述](research/atlas/index.html)

以公开研究为对象；图中的关系、团队和研究卡片共同解释三条路线。本综述不讨论项目自身理论或方案。

| 路线 | 收录研究 | 方法段落已读 | 摘要初筛 |
|---|---:|---:|---:|
| Harness | 38 | 16 | 22 |
| Model | 34 | 14 | 20 |
| Model × Harness | 25 | 8 | 17 |

合计 97 项路线研究，另有 8 项跨路线评测/形式研究与 22 项历史、背景材料，共 127 项。路线数量包括相关技术和初筛候选，不等于认证的高质量 RSI 系统数。

43 条逐项解释的论文关系；机构署名与方法归类作为单独边类型。

## 阅读方式

1. 进入任一路线，沿问题与方法节点查看研究分布。
2. 点击论文，看相邻研究及团队；点击关系，看关系含义与原文定位。
3. 打开阅读卡片，按目标、思想、原理、方法、迭代、成果六个角度阅读已有内容。摘要档案不冒充完整方法审阅。
4. 使用全局检索查论文、机构、算法或任务，并定位回图。

已确认低于 27B 的 Model / 混合机制参考默认不出现在路线主图，可在补充区或搜索中读取。未公开规模与低质量不是同一判断。

## 数据与复建

`data/literature-editorial.json` 保存人工叙述、路线位置与关系；`data/literature-atlas.json` 是阅读数据，`data/knowledge-graph.json` 是带来源的多关系图。

```bash
python scripts/build_literature_graphs.py
python scripts/check_literature_graphs.py
node scripts/check_atlas_ui.cjs
```

上一轮九页 PDF 是 2026-10-18 的导读快照；当前图谱以 HTML 与上述数据为准。
