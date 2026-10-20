# 贡献指南

[English](CONTRIBUTING.md) · [简体中文](CONTRIBUTING.zh-CN.md)

贡献应当改善 BeforeRSI 的证据、解释、结构或实验能力。欢迎补充原始来源、纠正事实、澄清机制、整理原文、复现实验，以及提供有判别力的负结果。

## 文献与图谱

1. 链接原始论文、代码、技术发布、基准记录或原始结果。
2. 说明更新对象、固定部分、反馈、继承状态、模型角色、任务划分、资源与实测结果。
3. 同时更新 `data/landscape.json` 和 `data/locales/en.json` 中对应的英文条目。保持 ID 稳定，区分来源支持的关系与编辑性方法对照。
4. 沿用六个解读维度，量化结果与具体评价设置一起描述。
5. 机构和公司关系以署名或官方发布为依据。

141 条领域目录与较小的研究论证索引用途不同。只有工作影响理论或实验论证时，才加入 `data/works.json`，并同步修改 `EVIDENCE.md` 及其中文对应文档。

## 教程与界面

编辑 Markdown 或 JSON 源文件后重新构建。两种语言在机制、数字、来源和章节覆盖上保持一致；可以用自然的目标语言重写表达。

```bash
python -m pip install -r requirements-docs.txt
python scripts/build_learning.py
python scripts/validate.py
```

源文件与生成的页面、PDF、插图一并提交。界面修改需检查两种语言、搜索、直达链接、PDF 下载与窄屏显示，详见[构建说明](docs/README.zh-CN.md)。

## 研究与实验

明确贡献属于来源事实、推导结论、工作假设、模拟、工程方案还是实验结果。待检验命题放入 `HYPOTHESES.md`，依据证据调整状态。

实验记录干预、固定部分、任务分组、资源、父代与后继版本、候选谱系、原始结果及分析。能够区分解释或确定适用边界的负结果同样有价值。

证据状态使用 `reported`、`reproduced`、`replicated`、`contradicted`、`open`，针对具体论断标记。模型修改、推导与分歧处理遵循 [AGENTS.md](AGENTS.md)。

表达直接。保留帮助读者理解工作的事实、假设、机制和结果，删去重复铺垫与没有依据的排名。
