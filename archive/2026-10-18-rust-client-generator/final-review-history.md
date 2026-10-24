# Final history and patch-equivalence addendum

No new findings or scope expansion. The complete final histories and retained
verification inputs support carrying the completed reviews forward to HaveAPI
`9e4c29a0412a25256ce944641f60ba13e9f03c2b` and client
`62753f006d7bd3e5befe1033c49a2c630ca3ff02`. This is a history and evidence
assessment; it does not repeat the source audits or verification runs.

2026-10-19, retained independent reviewer0, thread
`01a1508b-81fd-7ab2-b787-a7adb733a710`, model `gpt-6.1-sol`, effort `xhigh`,
saved access `read_only`. The live roster and bound session identity match;
`dev-session current` prints `2026-10-18-rust-client-generator`, with both
environment identity markers absent. No override, fallback or subreviewer.
Applied mandatory-change-review's general/history lane and workspace Git
procedure. Read the full [packet](review-packet-final-history.md), prior
[source review](final-review.md), [DELETE review](final-review-delete.md),
consolidation/range-diff records and input receipts. Prior conclusions and
revision references are preserved.

## Complete final series

| Repository | Base and final logical commits |
| --- | --- |
| HaveAPI | Comparison base `526648131af45df68c25ac0042a52f22c7a81df5`; `930a5f3f9ceca9586a4d89d72514d72f00f04d21` runtime, `8701baa51effcc90900a4c146d0fb27c31ec7db9` generator/tooling, `9e4c29a0412a25256ce944641f60ba13e9f03c2b` fixtures |
| vpsadmin-rust-client | Neutral empty root `b67a3ba5eef89b2bd6533050aa8769aaa0574114`; `f88d86ae97d335e4c89464a004e882fc7032720e` handwritten package/schema/tests, `62753f006d7bd3e5befe1033c49a2c630ca3ff02` generated source/runtime |

Independently inspected actual complete commit series, messages, per-commit
ownership, final diff inventories and range-diffs. HaveAPI retains exactly three
feature commits; the client retains exactly two. The runtime, generator and
fixture ownership split and handwritten/generated client split remain sound.
Both application worktrees/indexes are clean. HaveAPI's registered initial base
remains `c14e7d3158b91c134c2817b489cd29772fc09f82`; the new comparison base is
its actual descendant, not a replacement historical registration.

## Reconstruction and rebase evidence

Independent Git checks confirmed that actual passing HaveAPI
`41bbb37e40fe87851d327c4e986800071afd6277` and folded old-base head
`5f532ee8d5d3066b1264c276c1606ea3fca52105` have the identical tree
`dc8825b99a3394cbd401d92331409e0c8a4befd7`.

Regenerated range-diff from the folded series onto comparison base `5266481...`
maps all three patches with `=`. Independently recomputed stable patch IDs
match old and final commits and the history receipt:

- Runtime: `9e95bfe266bc0d720ee7c9435827738273db2be4`.
- Generator: `b77b459dd0c0fe4fcb92a628e69b53f5d53c1a08`.
- Integration: `1f40718e4469c6d53d991c398b3659d47b163448`.

The entire accepted-to-final tree delta is byte for byte the upstream
`c14e7d3...5266481` patch, touching only `utils/release/publish.rb` and
`utils/release/spec/release_spec.rb`, with 53 additions and three deletions.
Their final blobs equal upstream. The computed patch SHA-256 matches
`85c60bb23e5356ab2c41012bd9d5a7fdceff36f1f61ff097c359a57a04db2901`.
Final HaveAPI tree: `3ed0da056fbaa0d68c55e5fab635e3ea2105dc61`.
There is no conflict resolution or additional feature edit hidden in the rebase.

The post-DELETE-review source delta to the accepted fixture head is limited to
the lead-inspected fixture/test fixes: correct DNS ownership through its zone,
exact legal encoded path assertions, a valid WebUI setting namespace/key, and
one canonical recent-node-status seed before readiness. Actual code confirms
these do not alter runtime, generator, server behavior, auth policy or snapshot.
The client test changes add static stage labels and optional numeric HTTP
status while retaining the existing assertions and secret-safe diagnostics.
No public boundary expansion was found; these remain within the narrow-fix
policy already applied by the lead.

Independent client comparison from passing
`7279dd9916651c68f60123c9164ec74c1a2d9c31` to final `62753f0...` changes
exactly one line in `schema/provenance.json`, selecting HaveAPI `9e4c29a...`
instead of `e9173e2...`. All 686 generated Rust files, ownership manifest,
library, acceptance tests, schema/inventory, manifests, locks and configuration
are unchanged. Final client tree: `7a3167614dae9abd5c73a85df1c0746d18838a32`.
The diagnostics and revision refresh are folded into the original two commits.

## Verification input boundary

Independently validated 44 tested/final component Git-object identities in
[the HaveAPI input receipt](haveapi-final-input-receipt.json), its source/lock
hashes, all retained result hashes and the unchanged-input/Rust source hashes in
[the client receipt](client-final-input-receipt.json). The scopes distinguish:

- Runtime/default/blocking/Clippy, client/default/blocking/docs/package and
  Rust 1.95 checks at reviewed HaveAPI `e9173e2...` / client `1a818c4...`.
- Generic root/mounted acceptance at `3aaf7cf...`, whose actual runner, fixture,
  Rust cases, generator, runtime and server/client inputs match final source.
- Actual disposable vpsAdmin acceptance at HaveAPI `41bbb37...` / client
  `7279dd9...`, including both passing token lifecycle tests. Its final fixture
  and actual client tests match the tested Git objects. It uses unchanged
  vpsAdmin source `fb2f51222503a45f2e5a42af505f719e44279ed0`.

Read completed result records and relevant log conclusions. They report exit
zero for the corrected runtime/client/package matrix, exact Rust 1.95 checks,
root and mounted generated acceptance, and both actual vpsAdmin tests. The
client matrix excludes its ignored disposable-server tests; their execution is
separately evidenced by the later actual-server pass. Reuse does not relabel
old result records as runs on the rebased heads.

[The Nix receipt](haveapi-final-nix-inputs.json) explicitly reconstructs tested
shell derivations retrospectively. Tested/reconstructed and pre-rebase shell
identities agree; their derivation files and referenced compiler/interpreter
store paths exist. Actual final/tested flake and lock blobs are equal, as
independently checked. This assessment read those identities and records; it
did not run Nix evaluation, compilation or tests. The separate MSRV result/log
identifies Rust/cargo 1.95.0 and both locked feature checks.

All 26 retained extracted-generator package source-byte hashes match final
HaveAPI. The 697-entry retained client archive, hash and original VCS stamp
were independently verified; its ordinary payload and `Cargo.toml.orig` match
final inputs. The normalized manifest and VCS metadata are treated separately,
and `schema/provenance.json` is excluded by the package include list. A fresh
archive can have different VCS metadata; no equality of a future archive's
bytes is claimed. Final-head CI/package construction remains the next external
verification step, not a missing local input-equivalence proof.

## Final conclusions

**Obsolete-history conclusion:** neither final series retains an obsolete
approach, separate fixup, transitional shim or superseded correction. The
rebase preserves all accepted feature patches and adds only the identified
upstream baseline change. No concrete conflict or contract expansion was found.

**Migration conclusion: no migrations.** Neither full feature diff introduces
a database or persisted-format migration; existing generated migration-action
bindings are API methods. There is no merged, released, deployed or externally
consumed intermediate feature/schema boundary requiring retention. The rebase
adds no migration and does not rewrite the upstream default history.

**Repeated-update conclusion:** no repeated dependency/channel/input pin,
lockfile, schema-capture, generated-output or provenance update stream remains.
All accepted corrections and refreshes are folded into their owning logical
commits. No release or supported-consumer exception is needed.

The final history/patch-equivalence gate is satisfied for HaveAPI `9e4c29a...`
and client `62753f0...`. Within the explicit scopes above, unchanged source,
dependency and Nix identities support the retained local verification evidence.
Prior source reviews and the lead's direct narrow-fix checks remain applicable.
Feature publication and CI are pending; this addendum grants no default-branch
integration, registry release, deployment or session lifecycle authority.

Only this review evidence was written. No application, Git or session-state
mutation, build, server or live request was performed. The session remains open:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-18-rust-client-generator/>
