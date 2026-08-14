# brand: render every chart in the user's own identity

Sixty seconds from a website to a validated brand token. After this,
every chart the skill renders uses the user's colors, fonts, and voice
instead of a built-in language.

## The flow

1. **Collect.** Ask for (or fetch, if you have browsing) one of:
   the user's website URL, a style guide, a logo file, or an existing
   deck. From it, extract:
   - one background color (usually white or near-white)
   - one ink color (headings and strong text)
   - one primary accent (the brand color)
   - optional: a second accent, a positive green, a negative red
   - the heading font and the body font, with installed fallbacks
2. **Fill the template.** Copy `BRAND-template.json` from this folder
   to the project root as `BRAND.json` and replace every `REPLACE`
   value. Leave the `constitution` block alone unless the user asks
   for a different reading discipline; the defaults are safe.
3. **Derive the missing roles.** Most brands define 2 or 3 colors, the
   token needs 13. Derive the rest, do not invent freely:
   - `panel`: background mixed 4% toward ink
   - `hairline`: background mixed 12% toward ink
   - `gridline`: background mixed 8% toward ink
   - `body`: ink lightened 25% toward background
   - `primaryDark`: primary darkened 25% toward black
   - `muted`: primary mixed 70% toward background
   - `benchmark`: pure neutral gray near #AAAAAA
   - keep `positive` green-family and `negative` red-family even if
     the brand palette has neither; status colors are semantic, not
     decorative.
   Mixing rule (deterministic): channelwise linear mix,
   `round(a + (b - a) * t)` per RGB channel.
4. **Validate.**

   ```
   python tools/check_brand.py BRAND.json
   ```

   It checks the required roles, hex discipline, and WCAG AA contrast
   (ink on background at 4.5 or better, primary on background at 3 or
   better). Exit 2 means fix the token, not the checker. If contrast
   fails, darken the failing color toward black in 5% steps and rerun.
5. **Show proof.** Render one chart the user cares about in the new
   token and show it next to the same chart in a built-in language.
   The "that one is ours" moment is the point of this flow.

## Rules

- Never print the extraction guesswork; deliver the finished token and
  the proof render.
- The brand token changes palette, fonts, and chrome. It never changes
  geometry: specs still fix every px, so output stays deterministic.
- If the user's brand color IS red or green, keep `negative` and
  `positive` clearly distinct from `primary`; shift hue, not just
  lightness.
