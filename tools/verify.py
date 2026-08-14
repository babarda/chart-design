#!/usr/bin/env python3
"""Repo gate for chart-design. Exit 0 = ship, exit 2 = blocked.

Checks:
  1. reference drift (build.py --check)
  2. canon counts: 74 specs, 16 tokens, engine.json, dl.schema.json
  3. asset presence: showcase, grids, 16 language heroes, 12 examples,
     4 same-data renders
  4. no em-dashes in any .md or .py
  5. SKILL.md frontmatter (name + description)
  6. BRAND-template.json parses and lists all 13 roles
"""

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
fails = []


def check(ok, msg):
    print(("PASS " if ok else "FAIL ") + msg)
    if not ok:
        fails.append(msg)


# 1 drift
r = subprocess.run([sys.executable, str(ROOT / "build.py"), "--check"],
                   capture_output=True, text=True)
check(r.returncode == 0, "references match canon (build.py --check)")
if r.returncode != 0:
    print(r.stdout.strip())

# 2 canon
check(len(list(ROOT.glob("canon/specs/CH-*.json"))) == 74,
      "74 chart specs in canon")
check(len(list(ROOT.glob("canon/tokens/DL-*.json"))) == 16,
      "16 design-language tokens in canon")
check((ROOT / "canon" / "engine.json").exists(), "engine.json present")
check((ROOT / "canon" / "schema" / "dl.schema.json").exists(),
      "dl.schema.json present")

# 3 assets
check((ROOT / "assets" / "showcase.svg").exists(), "showcase.svg present")
for g in ("charts-grid.svg", "languages-grid.svg"):
    check((ROOT / "assets" / g).exists(), f"{g} present")
check(len(list(ROOT.glob("assets/languages/DL-*.svg"))) == 16,
      "16 language heroes")
gallery = {p.name for p in ROOT.glob("assets/gallery/CH-*_DL-02.svg")}
check(len(gallery) == 74, "74 gallery renders")
missing = [s.stem for s in ROOT.glob("canon/specs/CH-*.json")
           if f"{s.stem}_DL-02.svg" not in gallery]
check(not missing, "every spec has its gallery render"
      + ("" if not missing else ": missing " + ", ".join(missing)))
check(len(list(ROOT.glob("assets/same-data-four-ways/CH-*.svg"))) == 4,
      "4 same-data renders")

# 4 em-dashes
dash_hits = []
EMDASH = chr(0x2014)
for p in list(ROOT.rglob("*.md")) + list(ROOT.rglob("*.py")):
    if ".git" in p.parts:
        continue
    if EMDASH in p.read_text(encoding="utf-8"):
        dash_hits.append(str(p.relative_to(ROOT)))
check(not dash_hits, "no em-dashes in md/py"
      + ("" if not dash_hits else ": " + ", ".join(dash_hits)))

# 5 skill frontmatter
skill = (ROOT / "skills" / "chart-design" / "SKILL.md").read_text(
    encoding="utf-8")
fm = re.match(r"^---\nname: chart-design\ndescription:", skill)
check(bool(fm), "SKILL.md frontmatter has name + description")

# 6 template
try:
    tpl = json.loads((ROOT / "skills" / "chart-design" / "references"
                      / "BRAND-template.json").read_text(encoding="utf-8"))
    roles = ["background", "panel", "ink", "body", "hairline", "gridline",
             "primary", "primaryDark", "muted", "benchmark", "positive",
             "negative", "warning"]
    check(all(rl in tpl.get("palette", {}) for rl in roles),
          "BRAND-template lists all 13 roles")
except Exception as e:
    check(False, f"BRAND-template.json parses ({e})")

print()
if fails:
    print(f"BLOCKED: {len(fails)} failure(s).")
    sys.exit(2)
print("ALL CHECKS PASSED")


if __name__ == "__main__":
    pass
