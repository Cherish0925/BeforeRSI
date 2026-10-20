# 模拟与模型识别

[English](../../SIMULATION.md) · [中文入口](../../README.zh-CN.md)

模拟用于明确假设、展示定性状态和确定现实实验需要测量的量。当前数值来自示例参数，没有拟合现实 AI 系统，不作为预测。四层模型依次研究递归弹性、改进效率、噪声选择，以及能力—效率—评价的耦合。

## 1. 能力增长与递归弹性

以累计改进资源 $r$ 为自变量：

$$
\frac{dC}{dr}=aC^\epsilon.
$$

效率相对于能力的弹性定义为：

$$
\epsilon_{\rm RSI}
=
\frac{d\ln\eta}{d\ln C}
$$

当 $\epsilon\ne1$：

$$
C(r)
=
\left[
C_0^{1-\epsilon}
+
(1-\epsilon)ar
\right]^{1/(1-\epsilon)}.
$$

当 $\epsilon=1$：

$$
C(r)=C_0e^{ar}.
$$

| 弹性 | 曲线形态 |
|---|---|
| $\epsilon<0$ | 收益递减 |
| $\epsilon=0$ | 相对资源线性增长 |
| $0<\epsilon<1$ | 超线性但非指数 |
| $\epsilon=1$ | 指数增长 |
| $\epsilon>1$ | 理想方程中的有限资源奇点 |

奇点提示被省略的约束会变得重要，不应按字面外推到现实。

## 2. 改进效率

最小模型为：

$$
\frac{d\eta}{dr}
=
\lambda_{\rm RSI}\eta
-
\kappa\eta^2
+
u_{\rm ext},
$$

$$
\lambda_{\rm RSI}=g-d.
$$

$g$ 是递归设计增益，$d$ 是复杂性和验证负担，$\kappa$ 是饱和项，$u_{\mathrm{ext}}$ 是来自人工、新算法、强教师或外部数据的输入。当外部输入为零且净增益为正：

$$
\eta^*=\frac{\lambda_{\rm RSI}}{\kappa}.
$$

能力可以在效率下降、近似不变或提高的三种条件下增长；其中效率也提高才对应本模型的递归加速。

## 3. 候选搜索与评价保真度

设真实候选增益近似服从：

$$
g_j\sim\mathcal N(\mu_g,\sigma_g^2),
$$

观测分数为：

$$
y_j=g_j+\epsilon_j.
$$

保真度为：

$$
\rho=\operatorname{Corr}(g,y)
$$

最大观测值所对应的真实增益近似为：

$$
\mathbb E[g_{\rm selected}]
\approx
\mu_g+\rho\sigma_g\sqrt{2\log n}.
$$

若成本为：

$$
C(n)=C_0+n(C_{\rm gen}+C_{\rm eval}),
$$

则单位资源收益为：

$$
\eta_{\rm search}(n)
=
\frac{
\mu_g+\rho\sigma_g\sqrt{2\log n}-R(n)
}{
C(n)
}.
$$

收益项仅按 $\sqrt{\log n}$ 增长，而成本近似线性，因此模型预测有限最优候选数。保真度下降通常降低有效搜索量，并扩大观测赢家与独立真值的差距。

## 4. 能力、效率与评价的耦合

三状态模型为：

$$
\frac{dC}{dr}=\eta,
$$

$$
\frac{d\eta}{dr}
=
\left[
q\left(a_0+a_1\frac{C}{K+C}\right)
-
\left(d_0+d_1C^p\right)
\right]\eta
-
\kappa\eta^2
+
u_{\rm ext},
$$

$$
\frac{dq}{dr}
=
r_v(1-q)-s_v\eta q.
$$

$C$ 是独立测得的可迁移能力，$\eta$ 是单位资源增益，$q\in[0,1]$ 是评价与接受保真度。能力相关设计增益为：

$$
a_0+a_1\frac{C}{K+C}
$$

复杂性与验证负担为：

$$
d_0+d_1C^p
$$

评价以 $r_v$ 修复，以 $s_v\eta q$ 随更快变化的候选而退化。固定 $\eta$ 时：

$$
q^*(\eta)=\frac{r_v}{r_v+s_v\eta}.
$$

由此得到局部净递归增益：

$$
\lambda(C,\eta)
=
\frac{r_v}{r_v+s_v\eta}
\left(a_0+a_1\frac{C}{K+C}\right)
-
\left(d_0+d_1C^p\right).
$$

$$
\frac{d\eta}{dr}
=
\lambda(C,\eta)\eta
-
\kappa\eta^2
+
u_{\rm ext}.
$$

这个模型表达一个移动目标效应：改进过程变快时，评价投入若不增加，评价器可能跟不上候选变化。

## 5. 示例状态

相同累计资源下，当前参数产生以下数值：

| 状态 | 最终 $C$ | 最终 $\eta$ | 最终 $q$ | 解释 |
|---|---:|---:|---:|---|
| 饱和 | 3.156 | 0.019 | 0.986 | 复杂性负担超过设计增益 |
| 稳定改进 | 17.554 | 0.317 | 0.932 | 正但有界的改进效率 |
| 递归加速 | 167.954 | 2.925 | 0.925 | 设计增益提高，评价同步跟进 |
| 评价受限 | 40.075 | 0.535 | 0.241 | 提案能力增长快于评价 |

这些是示例方程生成的结果。完整初值和参数以 [模拟脚本](../../simulations/minimal_rsi_dynamics.py) 为准。

## 6. 状态划分

**噪声主导**：候选差异不足以从评价噪声中识别。

**基准拟合**：可见收益提高，但迁移数接近零：

$$
\mathcal T
=
\frac{\Delta J_{\rm hidden}}
{\Delta J_{\rm visible}+\varepsilon}
$$

**普通改进**：能力提高，效率不变或下降。

**递归改进**：两者同时提高：

$$
\frac{dC}{dr}>0,
\qquad
\frac{d\eta}{dr}>0.
$$

**饱和**：复杂性、验证、数据或搜索限制使效率接近有限平衡。

**不稳定增长**：观测收益提高，但评价保真度、独立能力或回退表现恶化。需要区分哪些状态变量实际变好。

## 7. 参数识别

| 参数 | 干预与测量 |
|---|---|
| $a_0,a_1,K$ | 跨能力层级比较父代和后继作为改进器 |
| $d_0,d_1,p$ | 随能力变化的更新、回退、耦合和验证成本 |
| $\kappa$ | 候选数与任务多样性扫描 |
| $r_v$ | 对评价构建或校准的受控投入 |
| $s_v$ | 固定评价器，同时提升提案能力 |
| $u_{\mathrm{ext}}$ | 移除或改变人工、教师和外部研究贡献 |
| $\rho$ | 搜索分数与独立强测试比较 |
| $\Gamma_{MH}$ | 完整模型—Harness 交叉 |

模型应预测未参与拟合的代际，而不只是拟合一条已有轨迹。

## 8. 运行

在仓库根目录执行：

```bash
python -m venv .venv
source .venv/bin/activate
pip install numpy scipy matplotlib
python simulations/minimal_rsi_dynamics.py
```

图和 JSON 摘要写入 `simulations/output/`，包括四种耦合状态的能力、效率与评价轨迹，不同递归弹性下的能力增长，以及评价保真度变化时的候选搜索效率。

## 9. 模拟的用途

模拟用于系统识别、模型批评和实验设计。成为预测之前，需要用干预估计参数、传播不确定性、预测保留代际、对同一数据拟合竞争模型，并通过任务分布或系统版本变化的检验。
