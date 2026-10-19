# 反馈优化尾部六篇：比较阅读综合

范围为从 feedback_optimization 明确交接的六个 entry：URPO、DERL、VLAW、MetaEvolve、SEED、Iterative RPO。全部完成主文、实验与相关附录阅读或原有阅读的完整复核；四篇 catalog/previous 项重新检查关键原文，没有把旧卡片作为最终证据。结果为 1 core、5 mechanism_supplement，均以 Model 为主要路线；DERL 另记录 Hybrid 的奖励程序—内层学习互作。小模型定位与科学贡献分开，不由教师大小或 self-evolving 名称决定。

## 被改进的对象决定路线

| 工作 | 实际继承/改变 | 固定的外部锚点 | 本轮决定 |
| --- | --- | --- | --- |
| Iterative RPO | 70B 生成者参数；每轮重新采样的正负推理 | 固定题目与人工参考答案，GSM 另有人工 CoT | Model / core enabler |
| URPO | 同一 7B/8B actor/judge 参数 | 外部偏好排序及可验证题答案 | Model / mechanism_supplement |
| DERL | 0.5B 奖励提议器、至多 3B 内层策略、被选择的奖励表达式 | 验证集终局表现、固定奖励原语与内层算法 | Model 主位置，secondary Hybrid / mechanism_supplement |
| VLAW | VLA 策略与视频世界模型；首轮训练后固定的 4B 成功分类器 | 真实机器人反馈和人工成败标记 | Model / mechanism_supplement |
| MetaEvolve | 14B 程序改进策略；部署时更新候选程序 | 执行测试与运行时间、固定 OpenEvolve 搜索 | Model / mechanism_supplement |
| SEED | 至多 7B 共享 actor/analyzer 权重，最新轨迹及训练期技能 | 环境终局奖励；启动时固定 GLM-5.2 标注 | Model / mechanism_supplement |

VLAW 的世界模型是学习到的动力学模型，更新它的权重不自动变成 Harness 演化。MetaEvolve 的程序档案和岛屿种群也不是执行/训练 harness 的自动改写。SEED 在测试时移除技能、分析器调用和检索；应归参数内化，而非持久记忆路线。DERL 的奖励表达式确实改变后续内层学习，因而与只更新 replay 数据不同；但奖励原语和外层优化算法仍固定，也不能称自主发明整个学习器。

## 三条闭环分别解决什么

第一条是“当前模型提供更有用的训练样本”。Iterative RPO 在固定题目上用新模型刷新正确/错误 CoT，再由前一轮权重继续训练。与 STaR/ReSTEM 的正确样本 SFT 相比，它显式利用错误样本；与单独 DPO 相比，正例 NLL 防止只拉开相对间隔却降低正确轨迹概率。第一轮 DPO 61.8 与 DPO+NLL 73.1，以及双倍首轮新数据 74.8 与两轮 78.0 的 GSM 对照分别支持目标和迭代的作用。新数据、模型继承和计算开销没有被全部独立隔离；完整多轮 STaR 也不是其等预算对照。70B 四轮贪心 55.6→81.6、后轮收益递减，使它成为清楚的大规模使能节点，不代表无限递归。

MetaEvolve 则先用静态同题候选池合成历史，训练“比当前程序更好”的提议器，部署到固定进化搜索。它没有在训练中运行完整在线多轮演化，也没有在部署后继续更新模型；价值是后训练后的程序改进能力能迁移到新的代码来源和 AlgoTune。其“AlphaEvolve”基线是同 Qwen3-14B+OpenEvolve，不是 Google 原版。多数代码来源和 7/8 算法任务改善支持机制；Codeforces、卷积和错误起点恢复的失败限制域外自演化宣传。它与 TTT-Discover 的目标任务在线 RL 互补，不能推定直接继承。

第二条是“反馈来源随学习改变”。URPO 让同一模型兼做生成与判断，利用外部偏好排名、可验证推理和开放任务共同训练；它并非去除了外部监督。SEED 通过当前轨迹事后技能改变每个动作 token 的辅助训练权重，但技能分析本身没有独立质量奖励。其教师/学生重评分均使用当前可训练模型，旧快照仅负责采样、分析和重要性比率；教师数值及 gate 停止梯度。实现等价于采样 token 的门控加权 NLL，不是显式全词表 KL 匹配。附录给出的重加权目标解释、奖励齐平时的非零梯度与陈旧性界均是局部结构结论：技能支持与动作价值正相关，才具有更高价值的解释。同步分析器不等于分析器必然更准确。

DERL 在这一条上更进一步：先让候选奖励实际训练内层策略，再用留出验证集表现更新奖励提议器。base 模式每次从初始策略重启，full 模式在搜索期间继承最佳策略，但最终又从初始模型重新训练并使用选出的奖励/奖励序列。不得把这三个阶段混为连续继承。其同预算 random/Eureka 风格候选对照和去除/翻转原语等检查，比只显示奖励文本变好更直接；同时，full 搜索约 8 个内层训练当量加最终 1 次，不能只列最终训练预算。

第三条是“现实反馈改善环境模型，再改善训练分布”。VLAW 用当前策略的真实成功和失败校正视频世界模型，后者产生更多模拟轨迹训练策略。真实采集量相同的 FBC 两轮平均 75.2%，VLAW 两轮 86.8%，为合成数据的额外价值提供直接证据。奖励分类器仅首轮训练；高阈值提高成功样本精确率，也显著降低召回率。两轮、五个接触密集任务仍不足以声称开放世界长期共同进化。核原 π0.5/ CtrlWorld 架构后，实际训练对象都不满足 ≥27B 主线偏好；最大的明确名义规模是 4B 奖励模型，冻结教师/家族名不用于抬高规模。

## 影响定量表述的原文复核

URPO 的摘要把生成任务与 RewardBench 放在一起，但 44.84 Alpaca、35.66 数学来自 P:R:I=1:1:1，而 RewardBench 85.15 来自 1:1:0。Table 5 未报告主配置 1:1:1 的 judge 分数，因此不能说同一 checkpoint 已完整证明两种能力同时达到这些数值。Qwen3-8B 数学也未超过其冻结 RM 对照。模型共用、训练目标联动与同 checkpoint 双能力改善是三个不同强度的主张。

VLAW 摘要写相对 base 提升 39.2 个百分点，Appendix Table 2 五任务均值却为 46.0→86.8，算术上是 40.8 点；相对 FBC 的 11.6 点一致。记录采用逐任务表格并明确差异，不选择更好看的单一数字。

SEED 的 §4.1 和 Appendix B.4 明确 ALFWorld 按六类任务等权平均，但 Table 1 多数 baseline 的 Avg 不符合其六列数值。原 PDF 第 9 页与 HTML 一致，已经排除提取错误：

| Table 1 行 | 报告 Avg | 按已披露分项重算 |
| --- | ---: | ---: |
| 3B GRPO / ALF | 75.0 | 70.70 |
| 3B SDAR / ALF | 84.4 | 80.12 |
| 3B SEED / ALF | 91.8 | 91.77 |
| 7B GRPO / ALF | 81.2 | 79.80 |
| 1.7B GRPO / ALF | 46.1 | 42.10 |
| 3B SEED / Search | 45.7 | 45.86 |

这不由四舍五入解释。Table 2 静态技能的 84.4 复用了同样的口径问题，另两项消融 86.0/87.0 可重算；ALF unseen 的 70.9/86.2 也一致。因而保留报告数与复算数，降低精确主表增益、样本效率比较的确定性；不把聚合错误扩展为所有任务实验无效。WebShop、正确复算的分项/消融和 unseen 结果仍支持可借鉴机制。SEED 没有在同一当前轨迹上只冻结分析器的隔离对照，静态技能库还改变经验来源，故“分析器与actor一起变强”的因果表述应进一步收窄。

Iterative RPO 的旧 arXiv v2 Eq.1 确实把 DPO 写成 log 概率之比；新核到的 NeurIPS 正式版已修为标准 log(Mθ/Mt)，不能把旧版错误延续为当前缺陷。正式版还披露生成 8×V100、训练 64×A100，基线共用调参范围，并明确每个实验只运行一次、当时未释放代码/数据。硬件可核，GPU 小时和研究总算力仍未知。正式版全主文、Appendix A/B 与相关 Checklist 已补读，卡片采用其更新。

## 关系与证据边界

关系中的 uses 仅用于原文明说复用的 DPO、GRPO、π0.5、CtrlWorld、OpenEvolve 等方法；基于综述者横向对读的关系只记 complementary/compares。Self-Rewarding、STaR、ReSTEM 与 IRPO 的差别在方法节有明确陈述，记录 compares 即可，不需要强行建立扩展链。没有因为 Related Work 出现名称就添加 extends。

六篇中最值得主图新增详细位置的是 Iterative RPO：实际 70B、当前分布的正负样本、正例巩固和连续继承构成一个有对照的代表机制。其余五篇各有独立用途，均应在可检索全文卡片保留：URPO 代表 actor/judge 联训，DERL 代表真正内层训练反馈驱动奖励设计，VLAW 代表现实锚定的策略/环境模型互促，MetaEvolve 代表可迁移程序改进提议器，SEED 代表训练期经验内化。它们的机制价值不要求被提升为 ≥27B 主线，也不因暂时未满足该规模而被称为无价值。

## 完成文件与来源补充

本组六条完整记录：`self_training_extra_feedback.jsonl`。原 87 条与额外 theory 16 条在各自文件，共 109 条唯一 entry。原 `self_training.jsonl` 在最后阶段不再覆盖，保留 root 对 ReST-meets-ReAct→RAFT 的关系修正。

额外核查的正式论文及图形保存在本地工作材料中，并已在记录的 reading.sources 记入原始 URL、SHA 和路径：`/tmp/iterative-rpo-neurips.pdf`、`/tmp/iterative-rpo-neurips.txt`、`/tmp/iterative-rpo-v2.pdf`、`/tmp/seed-v1-review.pdf`、`/tmp/seed-v1-review.txt`、`/tmp/vlaw-source-pi05.html`、`/tmp/vlaw-source-ctrlworld.html`。SEED prompt/案例原图为 `/tmp/seed-*.svg(.png)`；MetaEvolve 定性图为 `/tmp/metaevolve-qual.png`。没有未恢复原文的 blocked 项；未披露实验信息按每张卡片明确保留。
