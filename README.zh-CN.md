# BeforeRSI

![BeforeRSI — the landscape of recursive self-improvement](assets/readme-header.png)

**递归自改进的双语研究图谱。**

[English](README.md) · [简体中文](README.zh-CN.md)

**[下载双语交互图谱 · BeforeRSI.zip](https://raw.githubusercontent.com/Cherish0925/BeforeRSI/main/BeforeRSI.zip)**

下载 ZIP → 解压 → 用浏览器打开 `RSI_Field_landscape.html`，右上角切换中文 / English。图谱、搜索和教程可离线使用；访问论文原文时才需要联网。

BeforeRSI 连接 AI 自改进的机制、文献与研究主体，沿 **Harness、Model、Model × Harness** 三条路线梳理领域。核心问题是：系统保留下来的变化，怎样影响它产生下一次改进的能力？

## 从这里开始

| 目标 | 中文 | English |
|---|---|---|
| 浏览领域图景 | [下载 ZIP](https://raw.githubusercontent.com/Cherish0925/BeforeRSI/main/BeforeRSI.zip)，解压后打开 HTML | 同一文件切换 English |
| 学习模型与 LLM 原理 | [学习手册](docs/model-llm.md) · [52 页 PDF](docs/Model_LLM_Learning_Manual.pdf) | [Manual](docs/model-llm.en.md) · [49-page PDF](docs/Model_LLM_Learning_Manual.en.pdf) |
| 阅读研究主线 | [图景](docs/zh/MAP.md) → [理论](docs/zh/THEORY.md) → [假设](docs/zh/HYPOTHESES.md) | [Map](MAP.md) → [Theory](THEORY.md) → [Hypotheses](HYPOTHESES.md) |
| 参与整理与构建 | [贡献指南](CONTRIBUTING.zh-CN.md) · [构建说明](docs/README.zh-CN.md) | [Contributing](CONTRIBUTING.md) · [Documentation](docs/README.md) |

交互式 HTML 是项目的主要入口。三张领域图并列呈现，每条路线可切换领域知识图谱与研究关系图；点击节点或箭头，查看子问题、机制、论文和来源。文件还包含机构交叉表、机制导读、文献池、搜索、完整学习手册与两份 PDF，保存后可离线阅读。

## 收录内容

| 内容 | 范围 |
|---|---|
| 研究目录 | 141 条：118 条方法记录、1 条初筛记录、22 条历史与背景记录 |
| 机制图 | 3 条路线、29 个节点、60 条概念连接 |
| 研究关系 | 69 条扩展、采用、讨论与比较关系 |
| 文献检索池 | 567 条线索，包含摘要、作者、范围判断和已匹配研究入口 |
| 机制导读 | 6 个阅读维度、6 项研究案例、4 组方法对照 |
| 研究主体 | 170 个原始机构名称归一为 157 个主体 |
| 公司条目 | 27 家公司与产业研究团队 |
| 学习手册 | 29 章、148 组术语、61 个基础主题、95 个图谱子项、43 项原始文献 |
| 研究主线 | 38 项论证索引、12 个待检验假设、5 个实验方案 |

资料快照：**2026 年 10 月 19 日**。双语整理版：**2026 年 10 月 20 日**。38 项研究论证索引服务于理论与实验主线，与 141 条领域目录用途不同，数量不能相加。

## 三条路线

**Harness**：持久提示、记忆、技能、工具、控制流、运行代码与改进程序。追踪哪些外部资产发生变化，以及变化怎样跨任务保留。

**Model**：从自生成数据、偏好、验证、交互、课程和学习到的更新策略中改变参数。实际训练对象与固定教师、评价器、基线分别记录。

**Model × Harness**：参数与外部系统之间的反馈。关注经验内化、工作流适配，以及技能、环境、评价器和训练程序的共同变化。

每条工作按六个维度解读：目标与价值、思想与洞察、结构与原理、算法与实验、反馈与演化、成果与迁移。中英文共用 ID 和来源；完整中文阅读记录可在研究卡片内展开，并保留在原始数据中。

## 从领域图景走向实验

研究主线区分任务能力与改进能力：后继系统能够完成更多任务，并不直接说明它更善于产生下一代。

| 文档 | 回答的问题 |
|---|---|
| [图景](docs/zh/MAP.md) | 历史传统与因果分支怎样连接？ |
| [理论](docs/zh/THEORY.md) | 怎样表示系统状态、更新算子与递归增益？ |
| [证据](docs/zh/EVIDENCE.md) | 公开研究已经支持哪些结论？ |
| [假设](docs/zh/HYPOTHESES.md) | 哪些预测仍需检验？ |
| [研究计划](docs/zh/PROGRAM.md) · [实验方案](docs/zh/experiments/) | 哪些干预能够区分竞争解释？ |
| [评价协议](docs/zh/EVALUATION.md) | 怎样测量迁移、资源、回退与后继质量？ |
| [模拟](docs/zh/SIMULATION.md) | 明确的示例假设产生什么动力学？ |
| [研究记录](docs/zh/RESEARCH_LOG.md) | 当前研究表示怎样形成？ |

公式与实验方案属于进行中的研究；模拟用于说明假设；文献条目依据所引用的公开材料整理。相应状态在具体内容中标明。

## 仓库结构

| 路径 | 用途 |
|---|---|
| [`BeforeRSI.zip`](BeforeRSI.zip) | 离线下载包，仅含下列 HTML 主文件 |
| [`RSI_Field_landscape.html`](RSI_Field_landscape.html) | 双语交互图谱主文件；`docs/index.html` 为同一内容的网页入口 |
| `data/landscape.json` | 领域记录、机制映射、来源、机构和阅读笔记 |
| `data/locales/en.json` | 工作、机制、关系和公司的英文编辑层 |
| `data/works.json` | 研究论证索引，见[数据说明](data/README.md) |
| `docs/model-llm*.md` | 中英文学习手册源文档 |
| `docs/zh/` | 中文研究文档 |
| `web/` | 图谱模板、样式与交互代码 |
| `scripts/` | 构建与校验 |
| `experiments/`、`simulations/` | 实验方案与动力学示例 |

## 构建

```bash
python -m pip install -r requirements-docs.txt
python scripts/build_learning.py
python scripts/validate.py
```

首次构建下载固定版本的 Noto Sans SC 字体，后续使用本地缓存。生成文件与浏览器检查见[构建说明](docs/README.zh-CN.md)。

欢迎补充原始来源、纠正机制、改进解释，或用实验回答开放问题。协作方式见[贡献指南](CONTRIBUTING.zh-CN.md)和 [AGENTS.md](AGENTS.md)。

[MIT 许可证](LICENSE)；内置字体使用 [SIL OFL](assets/fonts/OFL.txt)。
