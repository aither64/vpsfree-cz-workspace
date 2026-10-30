# M8 CI corrections folded into Core

Base `f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`. Accepted combined sidecar
`73c1cc3cc71facf0f17c2f7f44e8e4089907a3d1`, tree
`5b9c52d0f0d81957bbca227d254e2e5b09b53373`, is preserved. Actual final:

| Group | Full commit | Tree |
| --- | --- | --- |
| Core | `9508921c21449c7cce45b1ed13b6efab8975b529` | `3fa6a9ec55a6777bd595dbcefe829a36ef3d2463` |
| Optional | `bdff6c399886a1743d4e1b694cf0b81906eebe73` | `41c3f7592009f06177ae9cc7c30e39cd0c539fbb` |
| Performance/HEAD | `5114746f3a9f87e91c704147c0d99dd4f0d32f02` | `5b9c52d0f0d81957bbca227d254e2e5b09b53373` |

Exactly three commits; all original main messages verbatim. Trusted clean
session-owned R3 scratch was reused via normal switch to a new branch, preserving
its old e5ea branch/ref and all receipts. Switch exited0/.395s without new signing
or checkout failure. The checked e5ea→73c eight-path CI binary/full-index patch
was applied to old Core9e1d and ordinarily amended. Exact old Optional15455 and
Performancee5ea patches replayed with git apply --check --index/--index and
ordinary commits. Each complete staged/committed tree and physical mode/blob
inventory matches old group plus only the eight checked paths:896/905/908 files.

Every eight-path predecessor blob was proved identical in old9e1d/15455/e5ea.
Each corresponding old→new group diff is the identical CI patch, SHA256
`516134f1d489b5d47db90cac8f58c42a23274ad5b23b9c77c198e0f7e5b2042c`.
Accepted73c→final diff is empty, with exact tree and byte-identical f6 aggregate
SHA256 `73306702233e552096108812d94e1bae723663115088c6ac8df01b62c38da458`.
Complete aggregate:147paths,+11464/-1271. Published e5ea→new:8paths,+71/-56.
range-diff.txt, final-series.txt, changed-paths.txt, group patches, staged/
committed JSON, aggregate patches and before-move.json retain full evidence.

Normal mandatory HaveapiI18n/RuboCop/all-message hooks passed on all three
commits:20.476s/4.293s/4.634s. Exact prepared immutable Ruby/Git/Bash/root frozen
bundle plus normal OS utilities retained. No setup/install/Nix/configuration/
lock/pin/source repair or bypass. All old refs were preserved, including exact
externally selected d67, published24ec/e5ea, e368/b869/18b9 and all historical
sidecars/failures. Unique new refs:
`refs/heads/recovery/2026-10-27-api-documentation-redesign-m8-ci-reviewed-20261029t002925z`
and `refs/heads/recovery/2026-10-27-api-documentation-redesign-m8-ci-accepted-20261029t002925z`.
The first preserves e5ea, the second73c. No remote ref or consumer pin changed.

Before the guarded expected-old73c→511 feature move: exact accepted tree/
aggregate, three messages/boundaries, both clean indexes, equal logical entries/
flags, all2148 inputs and preserved refs passed. update-ref exited0; readback
kept both statuses/indexes clean. Only local feature/scratch/recovery refs changed.
No reset, clean, stash, deletion, network, publication, preview or lifecycle work.

Only assigned new check: exact-final packaging_spec/profile_mount_spec,
10examples/0failures seed50232, exit0/7.225s (4.41s examples+1.43s load).
All11 generated docs remain byte-identical; no make doc repeat.
No Core/Optional smokes were rerun. scoped-reuse-and-lineage.json binds their
original successful actual commits9e1d/15455 and evidence hashes to matching new
loaded source/methods/package declarations, complete template trees, unchanged
harness and frozen root/server graph inputs. Old execution labels remain exact.
All900 other final tracked native modes/blobs equal e5ea: application, fixtures,
assets, runtime, adapters/emission sources and generation documentation unchanged.
This is scoped input evidence, not a new full-head/derivation or emitted-program
execution claim. Main owns later acceptance reuse decisions.

Owner0 focused server6/0/lint2 and owner2 Rust161/0+fixture2/0/lint2 are reused at
their exact eight checked hashes, from verification/m8-server-ci-remediation
and verification/milestone8-rust-ci-correction. No Ruby/PHP, compiler, installed,
native browser, all-client, wire/MSRV or performance check repeated. Original
CI failures and every earlier command/result remain preserved for actual scope.

Afterward all908 physical file hashes/modes in original and scratch equal the
accepted preflight; both indexes/statuses clean, logical entries equal and
original flags unchanged/allH. All2148 protected hashes and original root/server/
Rust lock hashes match before/after; scratch root/server locks match original.
See source.original.before.json, locks.before/after.json, inputs.before/after.json,
final-preservation.json and final-lineage.json. Every owned handle completed;
no active runner/utility or uncertain effect remains.

Review lineage: original full product/risk/history review f6..b869 remains
accepted; R3-only b869→e5ea was main-accepted direct step9 remediation. e5ea→73c
contains owner0's two assertion corrections and owner2's six test-placement/
wiring/technical-doc paths; this fold preserves that accepted sidecar exactly.
The new verification boundary still awaits main's bounded affected-lane review
at actual f6..511. No broader review/pass/readiness conclusion is invented.
Three-group bundling, no obsolete fixup ancestry, NO MIGRATIONS and NO repeated
dependency/channel/input/version update streams remain unchanged. Action refs,
runtime/lock inputs and R3/UI contracts remain exact. The full147path inventory
is available for the pending review.

SOURCE/Git/hooks/utility slot explicitly RELEASED. Main next assigns retained
reviewer0's short general/architecture/scope review, then separately grants any
remaining exact-head acceptance/publication/source binding. No gate auto-started.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/
