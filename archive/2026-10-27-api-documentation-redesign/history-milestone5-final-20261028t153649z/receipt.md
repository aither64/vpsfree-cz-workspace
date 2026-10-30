# Milestone 5 final history and bounded verification

Reconstructed the accepted sidecars into five logical commits without changing
final source. All intermediate C/D runtime boundaries and Basic smoke checks
passed; fresh final extracted-gem packaging and mounted-profile checks passed.

- Base: `f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`.
- Accepted sidecar head: `83fdaffdb74cd893bf9f6c81442681dbfeb654c9`.
- Final feature head: `35c1fb964735639c0873aacf078e18569f05f9bc`.
- Both final trees: `756b61de87833d8ded478b5d7785618671b4ddcb`; old/new diff is empty.
- Identical aggregate full-index feature patch SHA-256:
  `02e7e07a75f10cd6219ca7a26416f363c8e425e7d54201cdc40c16708f900dc8`.

## Final series and ownership

- A: `4363d1114f31cbb5d61411a95f6501bda17b50c0` servers/ruby: add simple and detailed client examples
- B: `260e3ea8a469c8840164bd8a0f5044238f5472e1` clients: simplify generated SDK documentation examples
- C: `8b34aa85bec7feaf4631ca14358437894d6ef853` servers/ruby: redesign HTML documentation navigation
- D: `325825dafdb85af4ac4deb1559a07000af4114a9` servers/ruby: add optional OAuth documentation sessions
- E: `35c1fb964735639c0873aacf078e18569f05f9bc` servers/ruby: preserve documentation performance contracts

A/B are exact preserved commits. C includes final identity/navigation, shared
success headers, search presentation, detail capability and copy UI. D includes
complete optional documentation OAuth integration, R1 callback preservation,
opt-in switching, guide and synthetic optional-control tests. E retains its
performance/cache ownership. Exact five accepted messages are preserved,
including the verbatim main-authored C message. Full sidecar-to-group/path
mapping and actual changed paths are in `provenance.json`.

## Intermediate boundaries and exact source proofs

Owner0's seven `basic-pre-e/` and `restored-pre-e/` files are authoritative for
actual C/D staging and committed content. Both pre-E and separate final patches
were replayed at fuzz0 without offsets, restoring all seven files byte-for-byte.
Final-E variants were not C/D staging inputs. See `owner-projections/`,
`owner-replay-{pre-e,final}.log` and staged/committed boundary JSON.

Actual C has no optional module or optional server/helper/control/switch
references in those seven runtime files. Root and version HTML use ordinary
`authenticated?`, and the account context retains `controls: nil`. Actual D
introduces the module with complete server require/configuration/accessor/
helper/mount wiring, root/version documentation authentication and account
controls/switch/status integration. All accepted module/provider/spec/guide
bytes are restored exactly. Five contiguous synthetic controls examples are
absent from C and restored unchanged in D. C's UI guide keeps ordinary Account,
actual-username, Sign out and visibility prose; optional switch sentences near
the top and the Browser-sign-in tail enter in D. D restores the exact guide.

Clean actual C and D each ran a separate-process, source-bound Basic smoke
using unchanged prepared server/client locks and external gems. Mounted root,
version overview, selected resource and authentication page all returned200;
actual identity, native account menu, ordinary Sign out, private/no-store and
correct display-name assertions passed. The Basic provider ran once per request.
All loaded HaveAPI source files, selected0.31 server/client package paths,
method sources and template root were asserted inside that actual snapshot.
C had no optional module file/constant/loaded feature; D loaded its own module
but left OAuth unconfigured. No final-feature fallback was allowed. No network
listener, real provider, OAuth sign-in, private fixture or TLS was exercised.
See `smoke-{C,D}.json/log/execution.json` and `smoke.rb`.

## E proof boundary

The new C/D server ancestor necessarily changes whole-file blob IDs in E's
full-index patch. Main explicitly refined the proof: preserve all eight paths
and the message; all seven nonserver full-index patches are byte-identical;
server removed/added cache bytes and all context are identical, normalizing
only blob IDs and hunk positions. The raw full-index Epatch is **not** claimed
byte-identical. Old/new full/server patches and the compact staged comparison
are retained. The original cache hunk replayed with exact context/fuzz0 onto
owner restored-pre-E, reproducing owner final server. Actual replay reported no
position offset (zero); see `E-cache-replay.log`. This differs from the separate
auth projection replay proof and adds no cache design change.

C/E's complete shared-path audit is explicit: server.rb and
`spec/documentation/performance_spec.rb`. C/D retain that test file's exact
prior-C bytes; E introduces its accepted performance changes. Actual E restores
all seven final runtime blobs and the complete accepted final tree.

## Hooks and final quick checks

C/D/E ran ordinary mandatory HaveapiI18n, RuboCop and commit-message hooks;
all passed. Only the approved verbatim C message has retained >72-column
advisories; all lines remain<=80. Known unsigned new-scratch setup was handled
by verifying exact accepted hook/config bytes, reusing the frozen root tools
lock/gem home and ordinary `overcommit --sign`. Root availability proved
Ruby3.4.11/Bundler4.0.23/JSON2.21.2/Overcommit0.73.0/RuboCop1.85.1, no HaveAPI
root dependency. No install or dependency resolution occurred.

After the proof-bound atomic feature move, `make doc` and the existing
`spec/packaging_spec.rb` plus `spec/client_examples/profile_mount_spec.rb` ran
against the clean final scratch head: **10 examples,0failures**, seed50232,
10.955seconds including Nix/bundle availability. Packaging built/extracted the
actual0.31 gem and passed its source-location and route/heading matrix checks;
mounted profiles passed private schema/sample/locale/TypeScript registration
coverage. The gem SHA-256 is
`c5046feff09d90dca2db22e224aecea14e56171f78c8562ac6ddbac494e9411e`.

See `final-packaging-profile.log` and `.execution.json` for exact command/cwd/
head/tree. The ignored gem/doc outputs are in the retained final scratch,
preserving earlier original-checkout artifacts. Already successful owner unit/
asset checks were not repeated for rewritten SHAs. No long gate started.

## Inputs, reconstruction corrections and recovery

All2,148 CURRENT protected hashes match before/after, with root/Rust gem-spec
and JS artifact inventories unchanged. Compared with historical R2 evidence,
2,147 hashes match and one separately authorized preview lock refresh differs:
old7bdb6101... to current71d379b7.... Lead independently accepted its provenance;
the full `milestone4-final-receipt.json`, exact lock diff and original lock copy
were read and retained here. Only five local PATH versions/internal constraints
and label-only checksum rows changed0.30→0.31; external graph/platform/dependency/
Bundler records remain unchanged. This operation preserved the actual current
preview lock and did not touch preview services or inputs. Old receipts were
not relabelled or rewritten.

Root/server/Go/Rust/JS/Python/MSRV/published-runtime/frozen graphs and historical
exports are preserved. No metadata version bump, package/dependency refresh or
source repair occurred. Prepared input identities remain distinct from results.

One intermediate Basic-guide projection had an extra EOF blank; the guard
caught it before hooks, and only that temporary intermediate formatting was
corrected. A first scratch C/D attempt selected final E performance-spec bytes
too early. The explicit ownership audit caught this before E; its commits,
scratch, scripts/logs/proofs are retained under `attempt1-C-E-spec-mapping/`
and its original branch. A clean successor scratch uses exact prior-C spec
bytes, normal hooks and new exact-head smokes. No final source change or broad
reset/stash/clean/deletion was used. All older receipts, including historical
incorrect split claims, remain intact.

Before moving the feature ref, same-tree/empty-diff/aggregate-patch equality,
actual staged and committed seven-file boundaries, doc/test dispositions,
smokes, E comparison, protected inputs, original/active/aborted clean worktrees
and expected-old feature head were asserted. The atomic expected-old ref move
needed no original file/index writes because final trees matched. See
`proof.before-atomic-move.json` and `final-state.json`.

Backup `refs/heads/2026-10-27-api-documentation-redesign-pre-milestone5-final-20261028t153649z` retains the accepted sidecar head.
Final scratch `refs/heads/2026-10-27-api-documentation-redesign-milestone5-final-20261028t153649z-E-test-split` at
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-27-api-documentation-redesign/haveapi-milestone5-final-20261028t153649z-E-test-split` remains.

## Review handoff

The complete final feature range has no migrations/schema/seed lineage and no
feature dependency/channel update streams. There are no feature migrations to
classify as merged/released/deployed/externally consumed. Superseded UI and
followup sidecars are folded into finalC/D; generated adapters, optional auth
and performance remain distinct. Earlier runtime snapshots remain historical
review evidence without claiming nonancestor commits literally merged.

Original, active and retained aborted worktrees/indexes are clean; all owned
commands returned and no watcher/check/build remains. No fetch/push/default
integration/release/preview/provider/TLS/private-fixture/lifecycle action occurred.
Long documentation/compiler/wire/browser/performance gates await final review
and separate grants. Main owns final review/wording/state coordination; this
history-only package adds no product documentation beyond the accepted guides.
Git slot released to lead with the completed evidence report.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/
