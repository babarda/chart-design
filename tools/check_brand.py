#!/usr/bin/env python3
"""Validate a BRAND.json brand token for the chart-design skill.

Stdlib only. Checks the shape a design-language token must have, hex
discipline, and WCAG AA contrast. Exit 0 = usable, exit 2 = fix it.

Usage:
  python tools/check_brand.py BRAND.json
"""

import json
import re
import sys
from pathlib import Path

REQUIRED_TOP = ["code", "name", "ovp_version", "philosophy",
                "constitution", "occasions", "palette", "fonts"]
REQUIRED_ROLES = ["background", "panel", "ink", "body", "hairline",
                  "gridline", "primary", "primaryDark", "muted",
                  "benchmark", "positive", "negative", "warning"]
REQUIRED_CONST = ["narrative_style", "density", "annotation_policy",
                  "legend_policy", "highlight_policy", "decision_style",
                  "reading_time", "charts_per_page"]
HEX = re.compile(r"^#[0-9A-Fa-f]{6}$")


def srgb(c):
    c /= 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminance(hex_color):
    r, g, b = (int(hex_color[i:i + 2], 16) for i in (1, 3, 5))
    return 0.2126 * srgb(r) + 0.7152 * srgb(g) + 0.0722 * srgb(b)


def contrast(a, b):
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    path = Path(sys.argv[1])
    fails = []

    try:
        tok = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"FAIL cannot parse {path}: {e}")
        sys.exit(2)

    for k in REQUIRED_TOP:
        if k not in tok:
            fails.append(f"missing top-level key: {k}")
    pal = tok.get("palette", {})
    for role in REQUIRED_ROLES:
        v = pal.get(role, "")
        if role not in pal:
            fails.append(f"missing palette role: {role}")
        elif not HEX.match(str(v)):
            fails.append(f"palette.{role} is not 6-digit hex: {v!r}")
    for k in REQUIRED_CONST:
        if k not in tok.get("constitution", {}):
            fails.append(f"missing constitution key: {k}")
    for f in ("display", "body"):
        fam = tok.get("fonts", {}).get(f, {}).get("family", "")
        if not fam or "REPLACE" in fam:
            fails.append(f"fonts.{f}.family not filled in")
    leftovers = [r for r in REQUIRED_ROLES
                 if "REPLACE" in str(pal.get(r, ""))]
    if leftovers:
        fails.append("REPLACE placeholders left in palette: "
                     + ", ".join(leftovers))

    hex_ok = all(HEX.match(str(pal.get(r, ""))) for r in REQUIRED_ROLES)
    if hex_ok:
        bg = pal["background"]
        checks = [
            ("ink on background", contrast(pal["ink"], bg), 4.5),
            ("body on background", contrast(pal["body"], bg), 4.5),
            ("primary on background", contrast(pal["primary"], bg), 3.0),
            ("negative on background", contrast(pal["negative"], bg), 3.0),
        ]
        for name, ratio, floor in checks:
            if ratio < floor:
                fails.append(f"contrast {name} = {ratio:.2f}, "
                             f"needs {floor} (darken it and rerun)")
        if pal["positive"] == pal["negative"]:
            fails.append("positive and negative are the same hex")

    if fails:
        for f in fails:
            print(f"FAIL {f}")
        print(f"\n{len(fails)} problem(s). Fix the token, not the checker.")
        sys.exit(2)
    print(f"OK {path.name}: shape, hex discipline, and AA contrast all "
          "pass. Every chart will now render in this identity.")


if __name__ == "__main__":
    main()
