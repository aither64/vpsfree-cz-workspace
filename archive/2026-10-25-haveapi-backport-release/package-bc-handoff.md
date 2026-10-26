# Final maintenance reconstruction handoff

Final head: `321ce8256ad4704efaed04f4f2aa1ea4c2a3b4b8` on
`2026-10-25-haveapi-backport-release`; base:
`1c3c98f0d77e0b23c8da1a8937f25c5799864a3b`. Clean checkout/index, no running
handles. No push, integration, build, tag or publication performed.

The complete 12-commit series preserves the nine A commits through `b9b971b9`,
then existing `1741` backport `2bdd02f2`, integrated `39e98020` backport
`3bc2401a7231b348ea398d20c9f8858062e0b397` with its exact `-x` trailer, and
standalone 0.30.2 metadata `321ce825`. There are no redundant old B/fixup commits,
migrations, persisted-state changes or repeated dependency/pin streams.
The full inventory/messages/patch IDs are in `final-maintenance-inventory.json`;
`final-maintenance.diff` retains the complete binary diff (54 files, +7783/-49).

Final source differs from integrated master `39e98020` only in the 16 expected
release metadata/changelog paths. Those files are byte-identical to retained
`776220f3`. Source backport patch IDs match exactly: `39`/`3bc2401a`:
`4f0b89915877ade1bd3bf3b53ca9183765a126b6`; `1741`/`2bdd02f2`:
`38c31b5bfe004e5a5e6dd74cbd2ded4047783b4e`. Stable `776220-reviewed-backup`,
old C `5832`, `bdb`, `40b514`, `be520` and earlier refs/artifacts remain retained.
The release checkout already had no `dist`; no old artifact was overwritten.

Exact-head focused checks passed: 49 examples, zero failures; 31 Ruby files
passed lint; full base-to-head I18n/Python/PHP/RuboCop hooks passed. Metadata
commit hooks and commit-message hooks passed. `make version VERSION=0.30.2`,
`make release-check`, `check-inputs`, `check-clean`, shell syntax and clean guards
passed. See `final-maintenance-remaining.log` and its result JSON (exit 0,
58.397 seconds). Original session-helper failures are retained in
`final-maintenance-quick*` logs/results: inherited root Bundler context and a
missing prepared Rust store in the helper's GEM_PATH. Only those diagnostic
helper environments were corrected; source and installed versions did not change.

`final-maintenance-proof.json` proves actual published .1, fixed `b85` and
integrated `39` inputs against final .2, including raw/JSON-version/unrelated
dependency negatives and replay validation. The canonical 9,374-byte lineage
delta passed at abbreviations 4/7/12; modified metadata was rejected. Focused
specs cover footer, compact summary, source/input/auth and late-operation gates.

All nine retained input graphs are unchanged, with five frozen Ruby bundles
usable (`final-maintenance-inputs.json`). The only refresh is accepted exact
JSON direct-declaration/checksum/order metadata in root/server/Rust locks and
own .2 identities. The before bytes/hashes are in
`final-maintenance-inputs-before/`; no install or external version resolution.
Prepared gems remain at `haveapi/.gems` and `haveapi/clients/rust/.gems`.
The locks are root/server/Ruby-client/Go/Rust `Gemfile.lock`, Rust runtime
`Cargo.lock`, JavaScript `package-lock.json`, PHP `composer.lock`, Python `uv.lock`.

Requestless runtime loading confirmed native JSON 2.21.2, all 87 expected gems,
Ruby identity and no differences (`final-maintenance-runtime.json`). Master and
release have identical default development-shell derivation
`/nix/store/ms7sialdgqsap5c6fbrm4hnlmgdf1dg9-haveapi.drv`; source and flake/tool
inputs are retained in the inventory. The master's 124-example/CI receipts stay
bound to master; source/input/derivation equivalence supports reuse. No full
suite, weekly campaign, old large replay or page probe was repeated.

Ready for reviewer0's final maintenance range/history/migration gate. Lead owns
review assignment, any later feature CI/build authorization, and eventual
integration/publication. Source remains frozen.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-25-haveapi-backport-release/>

## Historical package B/C handoff (superseded heads)

# Packages B/C: implementation and quick-check handoff

Owner: implementer1. All intended A/B/C changes are committed locally. The
checkout and index are clean and stable for final review. No commands remain
running. No branch push, integration, tag or publication was performed.

## Exact final range and history

- Repository: `git@github.com:vpsfreecz/haveapi.git`.
- Checkout: `worktrees/2026-10-25-haveapi-backport-release/haveapi`.
- Feature branch: `2026-10-25-haveapi-backport-release`.
- Approved maintenance target: `haveapi-0.30`; no master integration.
- Base: `1c3c98f0d77e0b23c8da1a8937f25c5799864a3b` (published 0.30.1).
- Final head C: `5832ccc64dcf725a625c88ad440ddb631ff404b4` (0.30.2).
- Final tree: `4925bc2ddfebd100e274265400efecac8a7ac91f`.
- Final base-to-head diff: **50 files, 6,554 insertions, 49 deletions**.

The complete eleven-commit series is:

| Commit | Package / purpose |
| --- | --- |
| `17272733cd27429e1ad6ea2eac0da6050816635c` | A: automated flake ancestry guard |
| `4c12fc84e7827b97cc8c1faf8a083325c18991ea` | A: owned documentation contexts |
| `5f038aba93c341bab37a687db254cc4849fd61fa` | A: selected Rust documentation normalization |
| `48ae0d5541b97bb9bae10924b85dc13e0a6146e1` | A: context complexity contracts |
| `8b7abc097db49893da9cc8fa4395648901fec71d` | A: documentation benchmark / mapped reference |
| `89389777edac5a67f9f8d57e5d042c060c30c1ec` | A: SQLite contracts |
| `559c162316cbb23db0d84e969da029ea82354ab9` | A: endpoint fixtures |
| `6a4d0ada1ccb2133a34c638db6c48aacb2e16c36` | A: performance workflow and event resolver |
| `b9b971b929edc75ef2f11fb6e541c1e0b52c99e1` | A: paired performance gates |
| `d32aa0f35e2af0ff5053de54c3e1eae2ca385a62` | B: bounded maintenance performance adaptation |
| `5832ccc64dcf725a625c88ad440ddb631ff404b4` | C: shared 0.30.2 metadata / approved changelog |

All 22 master-side source commits remain patch-equivalent to a maintenance
counterpart. Full source/backport provenance is in
[package-a-handoff.md](package-a-handoff.md). Final inventory assertions and
the binary diff hash are in `package-bc-inventory.json`. The final diff exactly
matches the lead's `final-review.diff`, SHA-256
`39bf2db148c891a8ac3f19a1b4a3c34a0ab37b0402a36e8a72e03447098d7821`.

These are nine separately integrated upstream units, one final adaptation and
one final release-metadata commit. No superseded implementation or repeated
dependency/pin update remains in this series. No dependency/channel update
stream was introduced; flake.lock is unchanged. Published 0.30.1 history and its
metadata boundary are retained. **No database migrations or persisted-state
changes**, conversion steps or rollback schema obligations are introduced.
The independent reviewer still owns the final history/migration conclusion.

## B behavior and proof

B changes only the existing resolver, endpoint runner, comparator, relevant specs
and performance guide: seven files, 579 insertions, 19 deletions. Product runtime,
fixtures, fixed reference and budget bytes are untouched by B. C changes exactly
the sixteen expected release-metadata paths, with 30 insertions and 15 deletions.
The changelog entry is byte-identical to the lead-owned artifact.

The original reference remains `b85ec364057f536940d689b09e612512ffffaf82`.
Its mapped maintenance ancestor is
`8b7abc097db49893da9cc8fa4395648901fec71d`. Both live entry points verify literal
mapped ancestry, all four exact trees and equality of the complete reference-to-
mapped binary diff with the published .1 metadata parent-to-commit diff. The
8,350-byte delta has SHA-256
`7fe745206de33755d0388284c6afeea6e557ed96d9644f9c81419a248b05f2d1`.
Receipts bind the exact candidate and retain both raw diffs. The original
reference is not a literal ancestor of maintenance history. Only weekly
fixed-reference comparisons receive the exception; quick pairs need ancestry.

Maintenance pushes compare whole event batches; maintenance features capture
the release head. Proven maintenance pairs normalize only synchronized own
`0.30.x` identities/internal client constraints and the two documentation
templates' own-version WebUI anchor hrefs. Raw input contents, hashes, loaded
source proof, bodies, byte counts and normalized digests remain available and
are checked again during replay. Third-party requirements, Ruby/flake inputs,
other gemspec bytes, other URLs, JSON/API values, example code, authorization
markers and panels remain exact. Negative tests cover these boundaries.

The budget SHA-256 remains
`57b8d4725e76c4552e6cb2eb54982cd8d406bd2415eb99e51cb43049bae3a050`;
flake.lock remains
`a52bdf3a3b9a069175d3af298234c3cf7adeba54540833eed6ad902e9ccc0a64`.

## Final .2 quick gates

`package-bc-final-quick.sh` ran once at exact C through the fresh pinned Luna/low
watcher, exit 0 in 76 seconds. Its initial unreadable brief started no command;
the follow-up delivered the task, and one operation owned the batch thereafter.
Full output is `package-bc-final-quick.log`; its compact receipt is
`package-bc-final-quick-result.json`.

- 125 server documentation/context/performance examples pass, seed 40153.
- 147 Rust generator unit examples pass, seed 64098.
- Syntax, update-helper shell syntax, .2 release metadata, prepared inputs and
  clean-source checks pass; `make doc` preceded server specs.
- All 30 changed Ruby/gemspec files pass RuboCop. Complete-diff HaveapiI18n,
  PythonChecks, PHP CS Fixer and RuboCop hooks pass. Both B/C commits passed
  their ordinary pre-commit and commit-message hooks without bypasses.
- All nine lockfiles retain their external graphs after versioning and checks;
  final exact-head and clean-checkout guards pass.

Earlier B-only quick evidence is retained in `package-b-performance-final.log`
(96 examples). Final .2 evidence above supersedes it for readiness. Expected
negative-control error JSON and isolated packaging-fixture warnings occur within
successful assertions. The dirty-source check attempted before the B commit
refused as designed and passed after the clean commit. C's explicit staging
printed an ignored-dist warning while staging the tracked version file; actual
commit effects were reconciled: all sixteen intended paths are committed and
the checkout is clean, including `clients/js/dist/haveapi-client.js`.

## Prepared inputs and next verification

Dependency preparation passed at B in 61 seconds under its own fresh watcher:
`HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c make release-deps`. Receipt/log:
`package-c-dependencies-result.json` / `package-c-dependencies.log`. All component
installations are retained: root/server/Ruby-client/Go gems in `.gems`, isolated
Rust gems in `clients/rust/.gems`, JS/highlighter node_modules, PHP vendor and
Python .venv. Preserve these resolved third-party graphs rather than rerunning
`make release-deps` before the accepted postreview plan.

The nine actual locks remain at their ordinary checkout paths:

- `Gemfile.lock`, `servers/ruby/Gemfile.lock`, `clients/ruby/Gemfile.lock`,
  `clients/go/Gemfile.lock`, `clients/rust/Gemfile.lock`.
- `clients/rust/runtime/Cargo.lock`, `clients/js/package-lock.json`,
  `clients/php/composer.lock`, `clients/python/uv.lock`.

Raw pre-version snapshots and hashes are in `package-c-inputs-before/`.
`package-c-dependency-graph.json` records final hashes and unchanged external
graphs; `package-c-verify-inputs.py` checks the narrowly permitted own-version
substitutions. Library locks and generated documentation remain uncommitted.

One bounded preparation detail remains: server and Rust lock entries already
name own 0.30.2 packages, while `clients/ruby/Gemfile.lock` and
`clients/go/Gemfile.lock` still have the prepared .1 local-path identities.
`make version` updates the Rust lock; the final quick suite refreshed the server
lock. After review/checkout transfer, refresh only those two remaining local
locks with `bundle lock --local` from their respective component directories in
the prepared top-level shell, then rerun `package-c-verify-inputs.py` before
capturing the full-suite input receipt. This preserves the existing external
records and avoids silent lock updates during full component tests. No source
edit is needed. These ignored inputs were left stable during final review.

`package-bc-prepared-environment.json` retains actual tool realpaths/versions,
flake metadata and the default shell's 2,460-path input graph, with derivation
`/nix/store/ms7sialdgqsap5c6fbrm4hnlmgdf1dg9-haveapi.drv`. Actual Ruby is 3.4.11,
Bundler 4.0.23, Node 24.21.0/npm 11.19.0, Python 3.11.17, PHP 8.3.35, and
Rust 1.99.0. The postreview plan still captures full recursive source/derivation
receipts for every separately used component shell before its campaign.

Final review, release/full-component tests, one retained all-component build,
package smokes, exact-C quick/weekly timing acceptance and hosted CI remain.
No top-level release packages have been built. Deterministic examples make no
timing claim; minimum supported runtime versions were not independently exercised.
Continue with the accepted [final verification plan](final-verification-plan.md)
after final review and the lead's explicit checkout transfer. Source/index/Git
ownership stays stable during review; follow-up fixes remain assigned to
implementer1 through the lead. No machines were reserved. Leave the session open.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-25-haveapi-backport-release/>
