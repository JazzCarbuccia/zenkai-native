# Zenkai Native — Dragon Ball FighterZ focused native Apple Silicon port. Baseline provenance.

## Base repository

- Upstream project: **LNPANDY/NX2Apple** (`https://github.com/LNPANDY/NX2Apple`), MIT.
- Baseline commit: `e9c351d6b4ae74c482d6f040893256f5d40aa7bb`, branch `main`.
- Imported upstream baseline: e9c351d6b4ae74c482d6f040893256f5d40aa7bb (local history intentionally not published).
- The sole remote is `upstream`, fetching from `https://github.com/LNPANDY/NX2Apple`; its push URL
  is `no-push`. No public remote exists yet and nothing has been pushed.
- A public push must use `git push <remote> main` only — never `--tags` or `--all`, which would
  republish the unclean imported history. `upstream/*` remote-tracking refs are local bookkeeping
  and are not published by a branch-only push.

## Upstream relationship

NX2Apple is **not** a git fork of `seedds/nxnative`: the two repositories have
independent lineages with no shared commit objects inside the history available locally
(no common ancestor can be computed). It is a *derived* project, and the derivation is
recorded rather than inherited:

- `NOTICE` states the derivation: NX2Apple grew out of `seedds/nxnative` (MIT,
  Copyright (c) 2026 seedds), which itself grew out of `jhaizhou`'s `d2r-mobile`
  (MIT, Copyright (c) 2026 jhaizhou). LNPANDY's own contribution is the RomFS archive
  subsystem.
- `.upstream-ref` = `ee6648cb2bb46c19255c1d04f88e9c40d36ef6b4`, the nxnative commit this
  tree was synchronized against. That object is not in this repository's history; it is a
  reference point, not an ancestor.

## Licence

- MIT. `LICENSE` is retained verbatim, including the seedds and jhaizhou copyright
  notices the MIT terms require.
- `NOTICE` is retained verbatim.
- Third-party components keep their own licences under `dm/third_party/README.md` and are
  unchanged by this baseline: `flip/` and `libvpx/` (BSD 3-Clause; libvpx also carries
  `PATENTS`), `stb_vorbis/` (MIT or public domain), `ryujinx/` (MIT), `vulkan-headers/`
  (Apache-2.0 or MIT), `bcdec/`, and outside that directory `dm/gfx/nvn/include/nvn.h`
  (MIT), the deko3d layout-size algorithm (zlib) and two pieces adapted from
  MacNativeGames (MIT, `dm/third_party/macnativegames/LICENSE`).

## What this baseline carries

The local uncommitted work of the source tree at `e9c351d6`, 25 files (+317 / −54969):

- **0x771 audio fix** — `dm/host/dm.h`, `dm/host/hle_audren.c`, `dm/host/hle_thread.c`.
- **Save-sync safety** — `dm/host/hle_fs.c`, `dm/host/save_sync.c`,
  `dm/host/save_sync.h`, `dm/host/tests/t_save_sync.c`.
- **Present-latency diagnostics** (`DM_LATLOG`) — `dm/gfx/nvn/nvn_mtl.m`.
- **Input polling diagnostics** (`DM_POLLLOG`) — `dm/host/hle_hid.c`.
- **DBFZ benchmark route** — `dm/games/0100A250097F0000/bench.tsv` (untracked in the
  source tree; copied in, not committed there).
- **Mario Kart 8 Deluxe split-screen 60 fps** — `fps_target 60` in
  `dm/games/0100152000022000/game.tsv`.
- **Dark Souls Remastered 1.0.0 60 fps patch offsets** —
  `dm/games/01004AB00A260000/patches.py`.
- **Frontend / IPA builder** — `frontend/Sources/NSPortBuilder/AppUpdate.swift`,
  `frontend/Tests/NSPortBuilderTests/AppUpdateTests.swift`,
  `scripts/build_ipa_from_nsp.py`, `dm/tools/tests/test_nsp_incremental.py`.
- **`.gitignore`** — the source tree's own ignore entry, plus the data-boundary block
  below.

It also **removes another title's game configuration** — the nine files under
`dm/games/0100F43008C44000/` (the bulk of the 54,969 deleted lines). That removal is
intended, not an accident of the import.

## What it deliberately excludes

No game data, saves, keys, romfs archives, mods or benchmark artefacts: `*.pak`,
`*.nsp`, `*.xci`, `*.nsz`, `*.kip`, `*.romfs`, `*.wad`, `*.keys`, `prod.keys`,
`title.keys`, `*.sav`, `*.fslog`, `*.pso`, `*.ipa`, `*.dmg`, `.env`,
`gen/*/game_profile.h`, `snapshots/`, `mods/`, `.unlazy/`, `research/` are ignored as of
this commit. Generated `game_profile.h` files name local ROM paths and stay out of git.

The upstream-tracked fuzz corpus `dm/tools/fuzz/corpus/uepak/*.pak` (hand-crafted malformed
archives, not game data) and the 16 KB self-built `probe-out/DmProbe.ipa` remain on disk but are
not published. The same applies to the app's own icons and UI screenshots under
`frontend/icon.iconset/` and `frontend/screenshots/`.

## Build

See `BUILDING.md`. The benchmark harness is `scripts/bench.py`.

## Known gaps

- No recorded performance baseline yet: prior bench runs collected 0 frames, so there is
  nothing to compare against.
- Only a title-stand benchmark route exists (`title-stand`, DBFZ title screen, idle, no
  scripted input — good for controlled A/B of host switches). There is no combat route;
  one has to be recorded with `DM_REC` once a repeatable fight path exists.
- The imported upstream history is intentionally not published: the product branch is a single
  clean root commit. The `upstream/*` refs remain locally for reference only.
