# languages: audience to design language

Generated from the Open Visualization Protocol v1.1 canon. Do not edit; edit the canon and rebuild.

If the user has run brand onboarding (`references/brand.md`) and a `BRAND.json` exists in the project, that token wins over everything below.

## Decision table

First full match wins, top down; every condition must hold.

| If | Then | Because |
|---|---|---|
| audience=executive, purpose=decide | DL-01 AGRAW | one governing message, authority through restraint |
| purpose=prove | DL-14 EVIDENTIA | numbered exhibits, proof over persuasion |
| audience=legal | DL-06 LEX | every statement referenced, looks like evidence |
| purpose=alert | DL-12 NOROSHI | verdict first, exceptions only, owner on every row |
| medium=screen, purpose=monitor | DL-08 SENTINEL | dark panels, one amber watch metric |
| audience=field | DL-05 OBEYA | readable from 3 meters on a bad projector |
| medium=projector | DL-05 OBEYA | contrast survives washed-out rooms |
| audience=technical | DL-04 SHILPA | title blocks, monospace IDs, stamps |
| audience=analyst, purpose=explain | DL-03 LOGOS | the chart is the page, annotation over legend |
| purpose=explain | DL-03 LOGOS | evidence before opinion |
| purpose=navigate | DL-09 ATLAS | geography drives layout |
| purpose=celebrate | DL-10 BASIRA | the photograph carries the page |
| medium=print, purpose=brief | DL-11 SUTRA | two pages, recommendation last |
| purpose=brief | DL-11 SUTRA | complexity distilled |
| purpose=archive | DL-07 SAGA | every report becomes history |
| purpose=document | DL-04 SHILPA | precision before aesthetics |
| purpose=monitor | DL-02 KATA | the recurring status register, repeatable structures |
| audience=operations | DL-02 KATA | default for recurring operational reporting |
| audience=executive | DL-16 TELOS | answer first, action emphasized |
| (nothing matches) | DL-02 KATA | KATA is the workhorse default when nothing sharper matches |

## The 16 languages

| Language | Motto | Lead occasion | Charts/page | Voice |
|---|---|---|---|---|
| DL-01 AGRAW | Lead with wisdom. | board packs | 1 | measured, formal-plain |
| DL-02 KATA | Perfect through repetition. | weekly status decks | 2 | clipped, telegraphic |
| DL-03 LOGOS | Evidence before opinion. | deep-dive analysis | 3 | analytic prose |
| DL-04 SHILPA | Craft every detail. | technical packs | 4 | technical, impersonal |
| DL-05 OBEYA | See together. Decide together. | stand-up boards | 4 | spoken, direct |
| DL-06 LEX | Everything must be traceable. | claims | 2 | legal-neutral |
| DL-07 SAGA | Every report becomes history. | weekly digests | 2 | journalistic |
| DL-08 SENTINEL | Watch without distraction. | live dashboards | 4 | label vocabulary, closed set |
| DL-09 ATLAS | Always know where you are. | route progress | 2 | positional, kinetic |
| DL-10 BASIRA | Look deeper than sight. | photo progress reports | 2 | spare, documentary |
| DL-11 SUTRA | Complexity distilled. | briefing notes | 1 | formal, dense |
| DL-12 NOROSHI | Signal only what matters. | escalations | 1 | urgent-terse |
| DL-13 MIZAN | Balance creates clarity. | cultural projects | 1 | warm, literary-plain |
| DL-14 EVIDENTIA | Proof over persuasion. | evidence-led strategy decks | 1 | quantified, footnoted |
| DL-15 ABRID | Everything is connected. | framework decks | 2 | structural, relational |
| DL-16 TELOS | Every page serves a purpose. | results decks | 2 | direct, conclusive |

## Obey the constitution

The token file (`canon/tokens/<code>.json`) fixes palette hex, fonts, density, annotation and legend policy, highlight policy, charts per page, and the voice block (register, hedging, sentence and title caps, title grammar). The language's identity lives in the words as much as the palette: write titles with its title grammar and stay under its caps.
