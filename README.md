# Zenkai Native

A native Apple Silicon port of **Dragon Ball FighterZ**. 中文：[简体中文 README](README.zh-CN.md).

Zenkai Native runs DBFZ's own code natively on Apple silicon — it is not an emulator. Metal draws
the game. This repository is **source only**: it builds the game from a copy you dumped yourself,
with keys from your own console. No game data, ROMs, keys or saves are included or downloaded.

## Status

- **Phase 0 accepted**: the port builds and runs on Apple silicon from the user's own files.
- **Mod support is experimental** and not guaranteed.
- DBFZ is the only title supported here.

## What you need

- **An Apple silicon Mac.** Building needs Xcode with the macOS SDK (see [BUILDING.md](BUILDING.md)).
- **Your own DBFZ game files** (NSP) and **your own `prod.keys`** from your own console. Nothing is
  bundled, downloaded or looked up for you.

## One build path

There is a single supported way to build the game — the by-hand script in this repository:

```bash
python3 scripts/build_ipa_from_nsp.py <path-to-your-DBFZ-NSP-folder> \
  -k <path-to-your-prod.keys> --platform mac-app
```

`--platform mac-app` produces a self-contained, double-clickable DBFZ Mac app. Setup, dependencies
and options are documented in [BUILDING.md](BUILDING.md). There is no launcher app, no release
download and no other build target in this repository.

## Repository layout

- `dm/` — native engine, host layer and renderer (vendored snapshot).
- `scripts/` — the NSP-to-app build pipeline used by the command above.
- `docs/reference/` — engine reference documentation; `docs/development.md` — development notes.
- `BASELINE_SOURCE.md` — where the code came from.

## Provenance and credits

Zenkai Native is derived from **[LNPANDY/NX2Apple](https://github.com/LNPANDY/NX2Apple)** (MIT) and
**[seedds/nxnative](https://github.com/seedds/nxnative)** (MIT). The code-rewriting toolchain, the
Horizon host layer and NVN-on-Metal come from those projects; this repository focuses them on
Dragon Ball FighterZ. The full inherited history is described in [CHANGELOG.md](CHANGELOG.md) and
[BASELINE_SOURCE.md](BASELINE_SOURCE.md); the licences and copyright notices are in [LICENSE](LICENSE)
and [NOTICE](NOTICE).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for reporting problems and sending changes.

## Legal

Not affiliated with, sponsored by or endorsed by Nintendo. "Nintendo Switch" and "Dragon Ball
FighterZ" are trademarks of their respective owners. You are responsible for making your own
backup under the law where you live, and for never distributing game files or keys. The software is
provided "as is" under the licences in [LICENSE](LICENSE), without warranty of any kind.
