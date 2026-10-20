#!/usr/bin/env python3
"""Build the bilingual manuals and self-contained research atlas."""
from pathlib import Path
import argparse
import base64
import hashlib
import json
import subprocess
import sys
from fontTools import subset

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / ".cache/learning"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--web-only",
        action="store_true",
        help="Reuse current manual builds; fail if their Markdown changed.",
    )
    args = parser.parse_args()
    manuals = {}
    for lang in ("zh", "en"):
        if not args.web_only:
            subprocess.run(
                [sys.executable, str(ROOT / "scripts/build_manual.py"), "--lang", lang],
                check=True,
            )
        guide = json.loads((CACHE / f"manual-{lang}.json").read_text())
        suffix = ".en" if lang == "en" else ""
        source = (ROOT / f"docs/model-llm{suffix}.md").read_bytes()
        if guide["source_sha256"] != hashlib.sha256(source).hexdigest():
            raise ValueError(f"{lang} manual is stale; run a full build")
        manuals[lang] = guide

    atlas = json.loads((ROOT / "data/atlas.json").read_text())
    english = json.loads((ROOT / "data/locales/en.json").read_text())
    template = (ROOT / "web/atlas.html").read_text()
    css = (
        (ROOT / "web/atlas.css").read_text()
        + "\n"
        + (ROOT / "web/landscape.css").read_text()
    )
    js = (
        (ROOT / "web/atlas.js").read_text()
        + "\n"
        + (ROOT / "web/landscape.js").read_text()
    )
    texts = json.dumps([atlas, english, manuals], ensure_ascii=False) + js + template
    options = subset.Options()
    options.flavor = "woff"
    options.desubroutinize = True
    font = subset.load_font(str(CACHE / "NotoSansSC-Regular.ttf"), options)
    sub = subset.Subsetter(options=options)
    sub.populate(text="".join(sorted(set(texts))))
    sub.subset(font)
    font_path = CACHE / "AtlasSC.woff"
    subset.save_font(font, str(font_path), options)
    fontcss = (
        "@font-face{font-family:AtlasSC;src:url(data:font/woff;base64,"
        + base64.b64encode(font_path.read_bytes()).decode()
        + ') format("woff");font-weight:400;font-display:swap;}'
    )

    def embedded(value):
        return json.dumps(value, ensure_ascii=False, separators=(",", ":")).replace(
            "</", r"<\/"
        )

    replacements = {
        "{{FONT_CSS}}": fontcss,
        "{{ATLAS_CSS}}": css,
        "{{ATLAS_JS}}": js,
        "{{ATLAS_DATA}}": embedded(atlas),
        "{{LOCALE_EN}}": embedded(english),
        "{{MANUAL_DATA}}": embedded(manuals),
    }
    for marker, value in replacements.items():
        if template.count(marker) != 1:
            raise ValueError(f"Expected one template marker: {marker}")
        template = template.replace(marker, value)
    # Build inputs are hashed so validation catches stale generated UI as well as data.
    paths = [
        "web/atlas.html",
        "web/atlas.css",
        "web/atlas.js",
        "web/landscape.css",
        "web/landscape.js",
        "scripts/build_manual.py",
        "scripts/build_learning.py",
    ]
    manifest = {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in paths}
    template = template.replace(
        "</head>",
        '<script id="build-manifest" type="application/json">'
        + embedded(manifest)
        + "</script>\n<!-- Noto Sans SC: SIL OFL 1.1; assets/fonts/OFL.txt -->\n</head>",
    )
    (ROOT / "docs/index.html").write_text(template)
    (ROOT / "RSI_Field_landscape.html").write_text(template)
    stats = {
        "manuals": {
            k: {"pages": v["pages"], "chapters": len(v["chapters"])}
            for k, v in manuals.items()
        },
        "works": len(atlas["works"]),
        "english_works": len(english["works"]),
        "html_bytes": len(template.encode()),
    }
    (CACHE / "build_stats.json").write_text(json.dumps(stats, indent=2) + "\n")
    print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    main()
