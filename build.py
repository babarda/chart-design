#!/usr/bin/env python3
"""Generate the chart-design skill's reference files from the vendored canon.

Reads canon/ (74 chart specs, 16 design-language tokens, engine.json,
pinned to Open Visualization Protocol v1.1, see canon/SOURCE.md) and
writes three reference files the skill loads on demand:

  skills/chart-design/references/charts.md     message -> chart, per-family map
  skills/chart-design/references/languages.md  audience -> language, constitutions
  skills/chart-design/references/honesty.md    rules that override any choice

Usage:
  python build.py           regenerate in place
  python build.py --check   regenerate to memory and fail on drift
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CANON = ROOT / "canon"
REFS = ROOT / "skills" / "chart-design" / "references"
PROTOCOL_REF = "v1.1"
PROTOCOL_URL = "https://github.com/babarda/open-visualization-protocol"

FAMILIES = {
    "RNK": "Ranking", "MAG": "Magnitude", "TIM": "Time",
    "PTW": "Part to whole", "COR": "Correlation", "DEV": "Deviation",
    "DST": "Distribution", "FLO": "Flow", "SPA": "Spatial", "TAB": "Table",
}

INTENT_LABEL = {
    "ranking": "Rank items by a value",
    "comparison": "Compare items side by side",
    "magnitude": "Show how big things are",
    "trend": "Show a trend over time",
    "change-over-time": "Show change over time",
    "schedule": "Show a schedule or plan",
    "progress": "Show progress to a target",
    "part-to-whole": "Break a whole into parts",
    "composition": "Show what something is made of",
    "share": "Show a share of the total",
    "volume": "Show accumulated volume",
    "deviation": "Show deviation from a baseline",
    "variance": "Show variance or spread",
    "flow": "Show flow between stages",
    "bridge": "Bridge a start value to an end value",
    "variance-decomposition": "Decompose a change into drivers",
    "correlation": "Show a relationship between two measures",
    "outlier-detection": "Find outliers",
    "pattern": "Reveal a pattern",
    "density": "Show density or concentration",
    "status": "Show status across items",
    "lookup": "Let the reader look a value up",
    "readiness": "Show readiness or completion",
    "uncertainty": "Show uncertainty or a range",
    "distribution": "Show a distribution",
}

UNIVERSAL_RULES = [
    "Bars and columns always start at zero. Never truncate a value axis.",
    "Pie or donut only for a part-to-whole with 3 slices or fewer; "
    "otherwise rank the categories.",
    "Never a second Y axis. Use two stacked panels or an indexed line "
    "rebased to 100.",
    "Direct-label the marks; reach for a legend only when direct labels "
    "will not fit.",
    "One message per chart. If it needs two, make two charts.",
    "Sort by the value, not the alphabet, unless the order carries "
    "meaning (time, size class, process step).",
    "Every chart states its source and, where a total is implied, "
    "reconciles it in the title.",
    "No 3D, no exploded slices, no decorative gradients. Ink serves the "
    "data or it goes.",
]


def load(p):
    return json.loads(p.read_text(encoding="utf-8"))


def build_model():
    specs = [load(p) for p in sorted(CANON.glob("specs/CH-*.json"))]
    toks = [load(p) for p in sorted(CANON.glob("tokens/DL-*.json"))]
    engine = load(CANON / "engine.json")

    intents = {}
    for s in specs:
        for it in s["meta"].get("intent", []):
            intents.setdefault(it, []).append(s["code"])
    for it in intents:
        intents[it] = sorted(intents[it])

    def split_why(why):
        if ":" in why:
            a, b = why.split(":", 1)
            return a.strip(), b.strip()
        return why.split(" ", 1)[0].strip(), why.strip()

    rules = []
    for r in engine["rules"]:
        n, w = split_why(r["why"])
        rules.append({"if": r["if"], "then": r["then"], "name": n, "why": w})
    fn, fw = split_why(engine["fallback"]["why"])

    return {
        "specs": {s["code"]: s for s in specs},
        "intents": {k: intents[k] for k in sorted(intents)},
        "rules": rules,
        "fallback": {"then": engine["fallback"]["then"], "name": fn,
                     "why": fw},
        "toks": {t["code"]: t for t in toks},
    }


def names(model, codes):
    return ", ".join(
        f'{model["specs"][c]["name"]} ({c})' for c in codes)


def ref_charts(model):
    out = ["# charts: message to chart\n",
           f"Generated from the Open Visualization Protocol {PROTOCOL_REF} "
           "canon. Do not edit; edit the canon and rebuild.\n",
           "## What is the message?\n",
           "Name the message first, then take a go-to chart for it. Check "
           "the chart's exits in the family map below before committing.\n",
           "| Message | Go-to charts |", "|---|---|"]
    for it in [k for k in INTENT_LABEL if k in model["intents"]]:
        out.append(
            f"| {INTENT_LABEL[it]} | {names(model, model['intents'][it])} |")
    out += ["", "## Family map: every chart, when it applies, when it "
            "does not\n"]
    by_fam = {}
    for code, s in sorted(model["specs"].items()):
        fam = code.split("-")[1]
        by_fam.setdefault(fam, []).append(s)
    for fam in FAMILIES:
        if fam not in by_fam:
            continue
        out.append(f"### {FAMILIES[fam]} ({fam})\n")
        out.append("| Chart | Use when | Not when |")
        out.append("|---|---|---|")
        for s in by_fam[fam]:
            use = "; ".join(s.get("use_when", [])[:2])
            no = "; ".join(s.get("not_when", [])[:2])
            out.append(f"| {s['name']} ({s['code']}) | {use} | {no} |")
        out.append("")
    out.append(f"Full specs: `canon/specs/<code>.json`. Protocol: "
               f"{PROTOCOL_URL}.")
    out.append("")
    return "\n".join(out)


def ref_languages(model):
    out = ["# languages: audience to design language\n",
           f"Generated from the Open Visualization Protocol {PROTOCOL_REF} "
           "canon. Do not edit; edit the canon and rebuild.\n",
           "If the user has run brand onboarding (`references/brand.md`) "
           "and a `BRAND.json` exists in the project, that token wins over "
           "everything below.\n",
           "## Decision table\n",
           "First full match wins, top down; every condition must hold.\n",
           "| If | Then | Because |", "|---|---|---|"]
    for r in model["rules"]:
        cond = ", ".join(f"{k}={v}" for k, v in sorted(r["if"].items()))
        out.append(f"| {cond} | {r['then']} {r['name']} | {r['why']} |")
    fb = model["fallback"]
    out.append(
        f"| (nothing matches) | {fb['then']} {fb['name']} | {fb['why']} |")
    out += ["", "## The 16 languages\n",
            "| Language | Motto | Lead occasion | Charts/page | Voice |",
            "|---|---|---|---|---|"]
    for code, t in sorted(model["toks"].items()):
        c = t["constitution"]
        v = t.get("voice", {})
        out.append(
            f"| {code} {t['name']} | {t['philosophy']['motto']} | "
            f"{t['occasions'][0]} | {c['charts_per_page']} | "
            f"{v.get('register', '')} |")
    out += ["", "## Obey the constitution\n",
            "The token file (`canon/tokens/<code>.json`) fixes palette hex, "
            "fonts, density, annotation and legend policy, highlight "
            "policy, charts per page, and the voice block (register, "
            "hedging, sentence and title caps, title grammar). The "
            "language's identity lives in the words as much as the "
            "palette: write titles with its title grammar and stay under "
            "its caps.", ""]
    return "\n".join(out)


def ref_honesty(model):
    out = ["# honesty: rules that override any choice\n",
           f"Generated from the Open Visualization Protocol {PROTOCOL_REF} "
           "canon. Do not edit; edit the canon and rebuild.\n",
           "## Always\n"]
    for r in UNIVERSAL_RULES:
        out.append(f"- {r}")
    out += ["", "## Per-chart cautions\n",
            "Charts that carry their own warnings. Honor these before "
            "using them.\n",
            "| Chart | Never |", "|---|---|"]
    for code, s in sorted(model["specs"].items()):
        if s.get("anti_patterns"):
            worst = "; ".join(s["anti_patterns"][:3])
            out.append(f"| {s['name']} ({code}) | {worst} |")
    out += ["", f"Built on the Open Visualization Protocol ({PROTOCOL_URL}).",
            ""]
    return "\n".join(out)


GALLERY_START = "<!-- GALLERY:START (generated by build.py, do not edit) -->"
GALLERY_END = "<!-- GALLERY:END -->"


def readme_gallery(model):
    """All 74 charts as her 3-per-row captioned cells, one table per
    family."""
    by_fam = {}
    for code, s in sorted(model["specs"].items()):
        by_fam.setdefault(code.split("-")[1], []).append(s)
    out = [GALLERY_START, ""]
    for fam in FAMILIES:
        if fam not in by_fam:
            continue
        specs = by_fam[fam]
        out.append(f"### {FAMILIES[fam]} ({len(specs)})")
        out.append("")
        out.append("<table>")
        for i in range(0, len(specs), 3):
            out.append("<tr>")
            for s in specs[i:i + 3]:
                use = s.get("use_when", [""])[0]
                if len(use) > 70:
                    use = use[:67].rsplit(" ", 1)[0] + "..."
                out.append(
                    f'<td align="center" width="33%">'
                    f'<img src="assets/gallery/{s["code"]}_DL-02.svg">'
                    f'<br><b>{s["name"]}</b> <sub>{s["code"]}</sub>'
                    f'<br><sub>{use}</sub></td>')
            out.append("</tr>")
        out.append("</table>")
        out.append("")
    out.append(GALLERY_END)
    return "\n".join(out)


def inject_gallery(readme_text, block):
    a = readme_text.find(GALLERY_START)
    b = readme_text.find(GALLERY_END)
    if a == -1 or b == -1:
        raise SystemExit("README.md is missing the gallery markers")
    return readme_text[:a] + block + readme_text[b + len(GALLERY_END):]


def main():
    check = "--check" in sys.argv
    model = build_model()
    files = {
        REFS / "charts.md": ref_charts(model),
        REFS / "languages.md": ref_languages(model),
        REFS / "honesty.md": ref_honesty(model),
    }
    readme = ROOT / "README.md"
    files[readme] = inject_gallery(
        readme.read_text(encoding="utf-8"), readme_gallery(model))
    drift = []
    for path, content in files.items():
        if check:
            on_disk = path.read_text(encoding="utf-8") if path.exists() else ""
            if on_disk != content:
                drift.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8", newline="\n")
            print(f"wrote {path.relative_to(ROOT)}")
    if check:
        if drift:
            print("DRIFT: " + ", ".join(drift))
            sys.exit(2)
        print(f"no drift ({len(files)} files)")


if __name__ == "__main__":
    main()
