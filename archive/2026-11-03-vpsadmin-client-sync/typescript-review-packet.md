# TypeScript final history remediation packet

Final head `c53cb4dabb0b3aac8d05834478872d2cfa698fa7`; final product tree remains
`c85e30b1fc1ae27bba9c08884e11fa78bbb15f7b`. Native current-head CI41668853169
passed and retained its own exact-source artifact/receipt. Lead directly
inspects this narrow history ownership remediation; no product-content review
rerun or local suite/build is requested.

## Complete range and ownership

Repository `vpsfreecz/vpsadmin-typescript-client`, target `main`, feature
`2026-11-03-vpsadmin-client-sync`, worktree
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-vpsadmin-client-sync/vpsadmin-typescript-client`.
Base `d354491537f8b654b4d2c33a705cad84474f95d6`.

1. `ec08ec18c4d9ba9f4f311cfb9e5af12fd4f01c97` — Generated schema/provenance/
   input refresh and inventory docs, plus the existing schema-hash assertion
   required by that schema. 18 files. Package/lock stay0.3.0 and their hash pin
   stays the actual0.3.0 hash.
2. `2071a164eab6a7681c5ba35542768c8a5e16251b` — New HTTP/strict-type consumer
   coverage only. 2 files/62 insertions. No existing schema-assertion change.
3. `c53cb4dabb0b3aac8d05834478872d2cfa698fa7` — Release metadata/prose:
   package/lock0.4.0, changelog/README and single corresponding package-lock
   hash-pin update. 5 files.

Generated commit message contains no future-release dependency excuse.
`tools/generator.json` schema/provenance keys belong to generated refresh and
package-lock key belongs to release. Distinct logical keys/streams can change
in separate commits without introducing a redundant generated/input update.
No intermediate schema/generation, runtime update, compatibility shim, obsolete
content or migrations. No feature revision is merged/tagged/deployed/published.

Read-only Git-object checks pass at base and every final commit: actual
package-lock SHA256 equals its pin, package/lock root versions agree, and existing
consumer schema assertion equals generated export and raw schema bytes SHA256.
[Full per-commit proof](typescript-history-proof.json),
[history receipt](typescript-history.md),
[focused prior-split/final range-diff](typescript-history-ownership-range-diff.txt).

## Original decisions, findings and exact content preservation

Original tested range ends at a4fc2449a1b5255b93b0c669ea9c454fac990536. The user
challenged its combined history; lead/owner accepted the split requirement. First
split ended at2256ea46a8d8d135f352a524fbf048869d6eddf4 but retained a future
release-lock hash and delayed an existing assertion update. Reviewer flagged
that as Blocking; lead accepted its instruction was wrong. These are retained
historical decisions, not current rationale. See original
[review result](typescript-review-result.md), rejected
[first-split packet](typescript-review-packet-2256ea4.md),
[receipt](typescript-history-2256ea4.md),
[proof](typescript-history-proof-2256ea4.json) and
[range-diff](typescript-history-range-diff-2256ea4.txt).

All three old/current final trees are identical. Final diff old/current is empty;
complete current base-to-head diff remains23files/987insertions/40deletions.
[Original-to-final range-diff](typescript-history-range-diff.txt) partitions the
one commit; it is not claimed as ordered one-to-one patch equivalence.
Old heads remain locally anchored. Exact prior-head force-with-lease succeeded;
new feature remote/capture match c53cb4d. Default and clean detached integration
target remain at d354491; no claim/default mutation.

Content review, compatibility and source provenance remain unchanged: two added
advisory actions and seven optional non-null state inputs, no existing values/
types/routes/defaults changed or removed. API942c6ea, generator1ef9b204,
runtime0.32.0, schema d6ec6176..., raw full fixture, six plugins and coverage151/521
plus authentication1/5. No Phase2/WebUI WIP/source API/generator change. Lead
approved existing prose. New calls need compatible deployed API and permissions;
publication alone does not establish availability. Matching inputs/pins/output
must be restored together on rollback; preserve published versions.

## Actual verification and archive identity

Old local checks and archive/receipt remain tied only to old tested a4fc244.
Original executed command retained as typescript-checks-tested-a4fc244.sh.
Current checks.sh is an unexecuted current-head template; no local setup,
regeneration, build or test suite repeated for history. Tree equality proves
unchanged content, not new Nix verification.

Native CI41668853169 independently passed on exact current c53cb4d, including
its existing regeneration/build/type/unit/packed-consumer matrix. Fresh CI-only
Luna/low utility completed, full-access/never, expected utility identity; no
operation remains and slot released. [CI result](typescript-ci-c53cb4d-result.md),
[metadata](typescript-ci-c53cb4d.json),
[artifact metadata](typescript-ci-c53cb4d-artifacts.json),
[downloaded receipt](typescript-ci-c53cb4d/receipt.json).
Artifact13245379341 is bound to run/current head, package0.4.0/tag null. Package
archive SHA256 `3a6f2a2a6f4eaeb31f490035b312e9b5403cf21589d649dc1fd31d60b64e1906`
verified against receipt. GitHub container-artifact digest is separately
`25f7599abbea7ffda2da1c8b21a9ab21156994f92caec03aa813437b7b8dcc13`.
Later publication requires its own exact tagged workflow artifact/receipt;
old local tarball must never be relabeled as new provenance. No tag/publication
or default integration approval is supplied by this packet.
