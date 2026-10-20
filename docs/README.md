# Documentation

[English](README.md) · [简体中文](README.zh-CN.md)

| Format | English | 中文 |
|---|---|---|
| Manual source | [model-llm.en.md](model-llm.en.md) | [model-llm.md](model-llm.md) |
| Printable edition | [PDF](Model_LLM_Learning_Manual.en.pdf) | [PDF](Model_LLM_Learning_Manual.pdf) |
| Offline landscape | [BeforeRSI.zip](https://raw.githubusercontent.com/Cherish0925/BeforeRSI/main/BeforeRSI.zip) — both languages in one file | 同一文件内切换语言 |
| Research documents | [Project index](../README.md) | [中文研究索引](../README.zh-CN.md) |

Download and extract the ZIP, then open `RSI_Field_landscape.html` in a browser. GitHub file and Raw URLs display source code; they are not a hosted reading page. Reading, search and PDF downloads work offline. Primary-source and repository links open online. Direct entries include `?lang=en#learn=00`, `?lang=zh#route=model`, `#work=dgm`, `#participants`, `#guide` and `#discovery`. Each route also has a `&mode=papers` view.

## Sources and outputs

| Source | Purpose |
|---|---|
| `docs/model-llm.md`, `docs/model-llm.en.md` | Manual text, formulas, references and indexes |
| `data/landscape.json` | Landscape, source links, mappings and review notes |
| `data/locales/en.json` | English editorial layer with matching IDs |
| `web/app.html`, `web/app.*`, `web/landscape.*` | Page template, styles and behavior |
| `scripts/build_manual.py` | One language edition, figures and cached chapter data |
| `scripts/build_learning.py` | Both manuals and the standalone landscape |
| `scripts/validate.py` | Data, translations, local links and source/output consistency |
| `scripts/test_landscape.cjs` | Browser behavior checks |

The landscape and the 38-work research claim index have different scopes. See [data documentation](../data/README.md).

## Build

From the repository root, with Python 3.12:

```bash
python -m pip install -r requirements-docs.txt
python scripts/build_learning.py
python scripts/validate.py
```

The first build downloads a pinned, checksum-verified Noto Sans SC font. Later builds use `.cache/learning/`. The font license is in `assets/fonts/OFL.txt`. Mathematical expressions render locally through Matplotlib.

The root `RSI_Field_landscape.html` and `docs/index.html` are generated from the same sources and must be byte-identical. The build also packages the root HTML as `BeforeRSI.zip` for direct download; `docs/index.html` is available for static hosting. Other generated deliverables are both `docs/Model_LLM_Learning_Manual*.pdf` files, and `docs/figures/*.svg`. Commit them with their source changes. Intermediate fonts, equation images and chapter data remain in `.cache/learning/`.

For interface-only changes, reuse unchanged manual builds:

```bash
python scripts/build_learning.py --web-only
python scripts/validate.py
```

This command rejects stale manual sources.

## Browser and PDF checks

With Playwright installed and Chromium available:

```bash
npm install --no-save --package-lock=false playwright@1.62.1
npx playwright install chromium
node scripts/test_landscape.cjs
```

Set `CHROMIUM_PATH` to use an existing Chromium executable. The check disables network access and exercises both languages, all three mechanism maps and research graphs, subquestion expansion, filters, participant tables, discovery, study dialogs, chapter search, references, exact PDF download bytes and narrow-screen overflow. Screenshots go to `.cache/browser/`.

For PDF layout changes, render representative pages with `pdftoppm` and inspect the cover, contents, formulas, diagrams, tables and final references. PDF text extraction alone does not detect clipping or overlap.
