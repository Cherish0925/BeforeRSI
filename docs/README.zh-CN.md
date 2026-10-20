# 文档与构建

[English](README.md) · [简体中文](README.zh-CN.md)

| 形式 | 中文 | English |
|---|---|---|
| 教程源文档 | [model-llm.md](model-llm.md) | [model-llm.en.md](model-llm.en.md) |
| 打印版 | [PDF](Model_LLM_Learning_Manual.pdf) | [PDF](Model_LLM_Learning_Manual.en.pdf) |
| 离线图谱 | [RSI_Field_landscape.html](../RSI_Field_landscape.html)，内置两种语言 | 同一文件切换 English |
| 研究文档 | [中文研究索引](../README.zh-CN.md) | [Project index](../README.md) |

下载 `RSI_Field_landscape.html` 后用浏览器打开。阅读、搜索和 PDF 下载可离线使用；原始来源和仓库链接在线打开。直达地址包括 `?lang=en#learn=00`、`?lang=zh#route=model`、`#work=dgm`、`#participants`、`#guide`、`#discovery`。每条路线还可通过 `&mode=papers` 进入研究关系图。

## 源文件与生成文件

| 源文件 | 用途 |
|---|---|
| `docs/model-llm.md`、`docs/model-llm.en.md` | 教程正文、公式、文献与索引 |
| `data/atlas.json` | 领域记录、来源、机制映射与阅读笔记 |
| `data/locales/en.json` | 使用相同 ID 的英文编辑层 |
| `web/atlas.html`、`web/atlas.*`、`web/landscape.*` | 页面模板、样式与交互 |
| `scripts/build_manual.py` | 单语言教程、插图和章节缓存 |
| `scripts/build_learning.py` | 两份教程与独立图谱页面 |
| `scripts/validate.py` | 数据、翻译覆盖、本地链接及源文件一致性 |
| `scripts/test_atlas.cjs` | 浏览器行为检查 |

领域图谱与 38 项研究论证索引范围不同，详见[数据说明](../data/README.md)。

## 构建

在仓库根目录、Python 3.12 环境下执行：

```bash
python -m pip install -r requirements-docs.txt
python scripts/build_learning.py
python scripts/validate.py
```

首次构建下载固定版本并校验哈希的 Noto Sans SC 字体，后续使用 `.cache/learning/`。许可证位于 `assets/fonts/OFL.txt`。数学公式通过本地 Matplotlib 渲染。

根目录 `RSI_Field_landscape.html` 与 `docs/index.html` 由同一组源文件生成，字节必须一致。前者是主下载文件，后者用于网页托管。其他生成文件包括两份 `docs/Model_LLM_Learning_Manual*.pdf` 及 `docs/figures/*.svg`，应与源文件一起提交。字体、公式图片和章节中间数据保存在 `.cache/learning/`。

只修改界面时，可复用未变化的教程构建：

```bash
python scripts/build_learning.py --web-only
python scripts/validate.py
```

如果教程源文件已经变化，此命令会要求重新完整构建。

## 浏览器与 PDF 检查

安装 Playwright 和 Chromium 后执行：

```bash
npm install --no-save --package-lock=false playwright@1.62.1
npx playwright install chromium
node scripts/test_atlas.cjs
```

也可通过 `CHROMIUM_PATH` 指定已有 Chromium。检查覆盖双语切换、三条路线的机制图与研究图、子问题展开、筛选、机构表、文献池、研究弹窗、章节搜索、参考文献、PDF 下载字节一致性与窄屏溢出，截图写入 `.cache/browser/`。

调整 PDF 排版后，用 `pdftoppm` 渲染并查看封面、目录、公式、插图、表格和末尾文献。仅提取文字不足以发现裁切与重叠。
