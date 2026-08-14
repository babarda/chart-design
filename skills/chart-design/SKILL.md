---
name: chart-design
description: Editorial-quality charts instead of chart slop. Use when the
  user asks for a chart, graph, dashboard, data visualization, slide
  visual, KPI page, or says "make this look professional". Picks the
  right chart for the message, the right visual identity for the
  audience (or the user's own brand), then renders from exact
  specifications. No improvised colors, no lying axes, no legend soup.
---

# chart-design

You are holding 74 chart types and 16 complete visual identities, every
one specified to the pixel by the Open Visualization Protocol. Your job
is resolution, then obedience to the spec. Never invent geometry,
colors, or chart choices.

## Workflow

1. **Name the message.** Open `references/charts.md`. Match what the
   user wants to show (rank, trend, share, deviation, flow...) to a
   go-to chart. Check the family map's "not when" column and take the
   exit if it names one.
2. **Pick the identity.** If the project has a `BRAND.json` (see step
   6), use it. Otherwise open `references/languages.md` and resolve
   audience + purpose + medium to a design language.
3. **Read the two files that fix everything.**
   `canon/specs/<chart>.json` fixes canvas, layout px, scales, rules,
   and QA. `canon/tokens/<language>.json` (or `BRAND.json`) fixes
   palette hex, fonts, density, annotation, legend and highlight
   policy, and the voice.
4. **Render SVG.** Follow the spec literally: exact canvas, exact px,
   colors only by resolving the spec's roles against the token palette
   (a role chain like `benchmark -> muted` resolves to the first role
   the palette defines). Numbers: max 2 decimals, trailing zeros
   stripped, never `-0`. No randomness, no timestamps. Deterministic
   output: the same spec + token + data must give the same SVG.
5. **Obey `references/honesty.md`.** Its rules override the user's
   chart request politely: draw the asked-for pie from its spec if it
   passes its caps, and mention the better alternative once.
6. **Write like the language.** The token's `voice` block sets
   register, hedging, sentence and title caps, and the title grammar.
   Titles carry a number. The words are part of the identity.
7. **QA before delivering.** Run the spec's own `qa` list. If a check
   fails, fix the render, not the checklist.

## Brand onboarding (the "make it OURS" step)

When the user wants charts in their own brand instead of a built-in
language, follow `references/brand.md`: extract palette + fonts from
their site or style guide, fill the `BRAND.json` template, and validate
it with `python tools/check_brand.py BRAND.json`. From then on every
chart renders in their identity, deterministically.

## Hard rules that survive user pressure

- Zero baselines on bars and areas. Always.
- Direct labels; a legend only where a spec explicitly allows a key.
- One highlight unless the constitution says dual.
- Declared inputs only: no silent trend lines, no silent smoothing.
- No em-dashes in any prose this skill produces.

## Token efficiency

Load only what the step needs: one reference file, one spec, one token.
The `assets/` galleries and README are for humans; never load them.

Built on the Open Visualization Protocol
(https://github.com/babarda/open-visualization-protocol), which
specifies and gate-checks every object this skill uses.
