# Blocking R2: restore loadable C/D history boundaries

Corrected the narrow history defect using original-owner server snapshots.
C contains the Basic server without optional references; D introduces the
optional module together with its complete server wiring. The final feature
source is unchanged. This is focused direct remediation under the mandatory
review skill's narrow-fix rule; main owns finding resolution.

- Base: `f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`.
- Previous head: `ab5b11188941d1c8c918951cdee162e9aa9f68cf`.
- New head: `9f68dad5436799d82e9c9e1c69e73866a279e9a6`.
- Both final trees: `c3c3e04337bcf9669dbb79611d72a65c686af9e0`; old/new diff is empty.
- Identical aggregate feature patch SHA-256:
  `2907070a7852ee24c31fa8efe9572c0a6336ae4ac21cc8823ce8f502179039c1`.

## Final five commits

- A: `4363d1114f31cbb5d61411a95f6501bda17b50c0` servers/ruby: add simple and detailed client examples
- B: `260e3ea8a469c8840164bd8a0f5044238f5472e1` clients: simplify generated SDK documentation examples
- C: `0f0399141d23cfecc33f7ba209e5acacc81e60c2` servers/ruby: redesign HTML documentation navigation
- D: `aafcfa0975ee0d19a57797b5e7c4c9150a8a38a5` servers/ruby: add optional OAuth documentation sessions
- E: `9f68dad5436799d82e9c9e1c69e73866a279e9a6` servers/ruby: preserve documentation performance contracts

A/B retain their exact commit identities. C retains the verbatim main-approved
message; D/E retain their accepted messages. E's full-index patch is byte-for-
byte unchanged. D's final pre-E tree equals the previous D tree; its patch now
includes the 11 server wiring lines that previously appeared incorrectly in C.

## Cause and preserved historical evidence

The milestone4 reconstruction driver removed D hunks, then undid E. Its
whole-file shortcut compared E's original blob with a fixed OLD_FINAL and
returned E's entire parent blob, ignoring already-transformed content. That
reintroduced OAuth references into C. D produced those same server bytes and
therefore had no server delta. Later exact replays preserved that bad split.
The old final-tree/patch checks were accurate for the final source, but earlier
claims that they proved correct intermediate isolation were wrong.

Every earlier receipt, script, proof, range and ref remains untouched, including
the incorrect split and claims. No old evidence was rewritten to conceal the
finding. The new driver uses exact owner snapshots and checks actual index and
committed blobs; it has no whole-blob undo shortcut.

## Actual C/D boundary and runtime proof

Authoritative original-owner server artifacts are copied into
`server-projection/` from
`/tmp/2026-10-27-api-documentation-redesign-server-auth-history-5jm3gd78`.
Only its pre-E C-basic/C-original bytes were used for staging; separate final
snapshots containing E's cache were not staging inputs.

- Actual staged and committed C server SHA-256:
  `dc4a98da8e8af08105c3da39ec5784f630c40927c770fbe7e0c6501a357d0be8`.
- Actual staged and committed D pre-E server SHA-256:
  `bccf92fbdef347c0e1c55312358da9eb71db6c3ecf9865339fb56f89d837c317`.
- Owner server restoration patch SHA-256:
  `dfeb48afca1bcf477d4f990f88a7df86bc5380fb3dbce8a5852e7808acd1e07c`.

The exact patch replayed in a new copy with fuzz 0 and no offsets, reproducing
D bytes. Actual C has no optional module and no optional require, complete
configuration/accessor, helper registration or mount reference in server.rb.
Its documentation helper calls ordinary `authenticated?`. Actual C-to-D diff
introduces the module and all four complete wiring blocks, and switches that
helper to `documentation_authenticated?`. See staged/committed JSON proofs,
`C-to-D-server.patch`, `C-to-D-helper.patch` and `C-to-D-full.patch`.

The existing four-partial Basic/final artifacts were reused exactly and remain
unchanged. Their previous zero-fuzz restoration proof remains authoritative.
The optional module, authentication-provider subtree, OAuth specs and guide
objects are unchanged. No OAuth source redesign or R1 repair occurred.

Each actual clean committed C/D snapshot ran a short, separate-process require
and mounted Basic documentation smoke using its copied server lock and the
retained external gem store. Bundler selected server and Ruby client 0.31.0
from that snapshot's paths. Every loaded HaveAPI file, server/helper source
location and template root was asserted to belong to that snapshot. C loaded
no optional file or constant; D loaded its own module, with OAuth unconfigured.
There was no final-feature module fallback. Both overview/resource requests
returned 200, showed the Basic identity and retained private/no-store caching;
the ordinary provider ran twice in each smoke. Transport was in-process Rack
HTTP with no socket, external service, sign-in or TLS activation.

Successful C/D smoke took 3.821/7.288 seconds including Nix/bundle availability.
The initial temporary fixture omitted the mount's trailing slash, producing a
route-miss406; after that correction, raw Rack mock omitted HTTP_HOST, which
existing renderer code requires. Both causes were demonstrated and reported
before temporary corrections. Original scripts/logs are retained; only fixture
mount/Host changed, without weakening status/body/auth/source assertions.
See `smoke-C.original-mount-406.log`, `smoke-C.missing-host.log`, final
`smoke-{C,D}.log/json` and the saved smoke script. No app source was repaired.

## Hooks, inputs and atomic move

New C/D/E commits ran ordinary HaveapiI18n, RuboCop and message hooks in the
repository Nix shell; all passed. Only C's unchanged approved message produced
the retained >72-column advisories; all lines are within 80 columns. Known
new-scratch signature setup was performed as explicitly authorized: verify
accepted custom/config bytes, reuse frozen root tools lock/gem home, ordinary
`overcommit --sign`. No bypass, install or dependency resolution occurred.
Root tools availability proved Ruby3.4.11/Bundler4.0.23/JSON2.21.2,
Overcommit0.73.0/RuboCop1.85.1 and no HaveAPI package in that graph.

All 2,148 protected hashes match before/after, including the earlier310 set,
refreshed0.31 locks/graphs, JavaScript build/declarations, Python editable
metadata, independent MSRV, fixed published runtime, frozen benchmark/preview
graphs and historical evidence/exports. Root/Rust gem-spec and JS artifact
inventories are unchanged; copied scratch root/server locks equal retained
inputs. No component resolution or refresh occurred.

Before the atomic expected-old-SHA feature move, both worktrees/indexes were
clean, actual intermediate proofs and smokes passed, protected inputs matched,
and the final tree/aggregate patch equalled the previous final. The ref move
needed no original worktree/index writes because those trees are identical.
See `proof.before-atomic-move.json` and `final-state.json`.

New backup `refs/heads/2026-10-27-api-documentation-redesign-pre-R2-server-split-20261028t135920z` retains the old head.
Scratch `refs/heads/2026-10-27-api-documentation-redesign-R2-server-split-20261028t135920z` and
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-27-api-documentation-redesign/haveapi-R2-server-split-20261028t135920z` retain the corrected five-commit series.

## Handoff

The same-base final feature range has110 changed paths, no migrations or schema/
seed lineage, and no feature dependency/channel update streams. There are no
feature migration versions to classify as merged, released, deployed or
externally consumed. Final runtime/source behavior and historical preview
snapshots retain their existing scope; no nonancestor is called literally merged.

Both feature and scratch full worktrees/indexes are clean. All owned commands
returned; no watcher/test/build remains active. No fetch/rebase, final-source
change, dependency work, long gate, preview/service change, publication/default
integration, deletion or lifecycle action occurred. OAuth/R1 remains held and
unfixed. Git slot released to lead with the completed report.

Main can inspect these exact staged/committed boundaries and focused smoke
results to resolve R2 under the narrow-fix rule, without a broad review rerun.
Later non-OAuth gates remain under separate lead grants. No product-guide edit
was useful for this history-only correction; this receipt preserves diagnosis,
verification and recovery, and lead owns the session state/review summary.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/
