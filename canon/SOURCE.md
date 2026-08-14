# Canon source

Vendored byte-for-byte from the Open Visualization Protocol v1.1
(https://github.com/babarda/open-visualization-protocol):

- `specs/` 74 chart specifications (CH-*.json)
- `tokens/` 16 design-language tokens (DL-*.json), including the v1.1
  voice blocks
- `engine.json` the audience/purpose/medium decision rules
- `schema/dl.schema.json` the token schema a BRAND.json must satisfy

The gallery files under `assets/` are the protocol's own golden
renders and generated site assets, copied unmodified: byte-identical
re-rendering of every golden is enforced by the protocol's gate
(3,276 checks) in the upstream repo.

Do not edit anything in this folder by hand. To move to a newer
protocol version: re-copy, update the version stamp in `build.py`,
run `python build.py`, then `python tools/verify.py`.
