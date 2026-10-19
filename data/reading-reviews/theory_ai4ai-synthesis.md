# AI4AI 补充组全文比较（原 theory 90–105）

16/16 已完成正文与全部技术附录，必要图表用原 PDF 补核。取舍为 core 1、support 8、mechanism_supplement 5、insufficient 2；路线为 Model 1、crosscut 15。不是按保留比例筛选。唯一新增核心为 AIDE；它的机构是 Weco AI，Runway ML 只是作者现地址，不能计入共同实施机构。

## 被优化的对象决定闭环边界

AIDE、FT-Dojo、AutoTrainess、TREX 与 SMCEvolve 都能自动形成更好的外部训练程序、数据方案或模型；研究 LLM 冻结时，外部模型变强不等于研究者的模型参数变强。节点档案、固定 Thompson/UCT 状态、固定提示下生成的实验总结，不能单独把所有搜索改称 Harness 自进化。AIDE 的价值在固定代码树中组织可执行实验；与 AlphaEvolve 的区别是后者原文确有另一个被共同演化的 meta-prompt 数据库与去除消融。不能把该事实扩张为 AlphaEvolve 所有控制逻辑都可自改。

SPARD 是本组唯一 Model 路线：实际训练到32B，reward维度与数据类别的动态权重形成训练反馈，外部调度公式固定。它有跨规模实验，但并非每个指标都提升，也未与所列动态reward方法直接匹配比较。小型外部训练任务则保留自己的机制价值：JF-HPO用同族小proxy做多保真搜索，FT-Dojo用训练专用工具和明确blindtest核对外部3/7B训练，TREX细化数据流水线与实验树，但预算和多个任务的val/test边界不及FT-Dojo清楚。

## 奖励生成不等于奖励部署

REvolve让人类偏好或自动环境反馈筛选奖励程序种群，RF-Agent以祖先路径与跨路径记录改善奖励搜索；两者主要继承reward code，新奖励下的策略训练没有明确父策略warm-start。CARD进一步先用成功/失败轨迹一致性筛reward，从而减少昂贵完整训练，但查询预算不匹配使“46.7倍token节约”不能只归因机制。

ROSKA与LLM-ALSO则真实继承外部策略checkpoint和reward状态。ROSKA用原策略与随机参数混合保留可塑性，再改写reward程序；LLM-ALSO只在六个人工PBRS basis内挑权重、模式和尺度。这是外部奖励—策略双向反馈，不是冻结语言研究器的Model×Harness协同。RHyVE把同一checkpoint分叉验证与phase profile分开，提醒reward排名依赖当前策略能力；其主峰值差未显著，且多张更新表与旧图仍冲突，宜保留诊断机制而不采用通用scheduler结论。

## 控制与成本会改变结论

AIDE的核心价值不依赖跨任务自我继任成立；原报告和独立MLE研究支持其研究自动化意义，但成本、holdout设置与表内标签问题必须保留。FT-Dojo的12h/单B200与盲测试设计比只报轮数更容易解释。TREX的每轮训练配置数量可从3–5到11，20轮不是统一GPU预算。LLM-ALSO的最终曲线排除了初筛和未选分支，且单LLM基线从头训练，不能据最终horizon宣称总成本公平。ROSKA的89% epoch预算可复算，统一搜索2.2倍及部分提升百分比不可照抄。RF-Agent匹配reward训练数且用新seed重训最终奖励，是更完整的搜索比较，但5个训练seed不是5次独立reward搜索。

## 需要明确留存的反证与证据缺口

CliffSearch公开最好nanoGPT代码把(B×S,T,D)直接view成(B,T,S,D)，把时间位置当作stream混合，存在未来token信息泄漏；这足以限制其.0073 CE主张，但不能推定其他节点都失效。LERO正文local观测与附录跨agent读取位置/目标/通信不一致；若接actor会改变信息条件，若只接critic则接线未披露。两者记insufficient，不用机构或小模型规模代替技术判断。

SMCEvolve的有限样本分析针对理想MH核和额外桥正则/混合假设下固定统计量的期望近似。实际reward-only acceptance省略prior/proposal概率比，ESS终点不是全局最优或混合完成证书；高acceptance本身也不能检验被省略概率比接近1。它在多数程序任务的best-of3结果仍有支撑价值，理论边界必须和经验搜索收益分列。

所有16条完整记录及原文定位在 theory_ai4ai.jsonl；未发现需标blocked的来源。没有原文仓库复现、缺失参数和评测细节均逐项标明，不能用“已阅读全文”替代重现实验。
