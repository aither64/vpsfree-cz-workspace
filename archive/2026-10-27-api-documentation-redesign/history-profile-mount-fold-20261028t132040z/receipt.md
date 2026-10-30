# Profile mount test history fold

Folded the one accepted test-only followup into C of the existing five logical
commits. A/B are exact preserved commits; C/D/E use unchanged accepted messages
and ordinary mandatory hooks. No application change or input refresh occurred.

- Base: `f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`.
- Prior five-group head: `a0c78d1c0e5ef84b5e746d9bba4bc51830c77139`.
- Previous final including the accepted followup: `c5badd08e10c5ac7586e2662cf97b29e6d3e0cc4`.
- Reconstructed feature head: `ab5b11188941d1c8c918951cdee162e9aa9f68cf`.
- Previous and reconstructed final tree: `c3c3e04337bcf9669dbb79611d72a65c686af9e0`.
- The previous-final/reconstructed diff is empty.
- Aggregate final feature patch SHA-256:
  `2907070a7852ee24c31fa8efe9572c0a6336ae4ac21cc8823ce8f502179039c1`.
- Prior-five-head/new-final delta is byte-identical to the accepted single-file
  patch, SHA-256 `74ddf85e523065f7a245b00e70457a76936191377986330149a38ce904e8ce23`.

Equality, empty diff, exact test-patch identity, preserved A/B, unchanged D/E
patches/messages, held OAuth objects and all 310 protected input hashes were
proven before the atomic expected-old-SHA feature ref move. The original
worktree/index needed no file writes because its final tree was identical.
See `equivalence.before-move.json`, `range-diff.txt`, `accepted-test-fix.patch`
and `prior-five-head-to-new-final.patch`.

## Final five commits

- A: `4363d1114f31cbb5d61411a95f6501bda17b50c0` servers/ruby: add simple and detailed client examples
- B: `260e3ea8a469c8840164bd8a0f5044238f5472e1` clients: simplify generated SDK documentation examples
- C: `d25dd61260a5768552bac5f6a8a201bb4c28d540` servers/ruby: redesign HTML documentation navigation
- D: `6049fc333e57baca4c97e9eb482f0c6b332041ba` servers/ruby: add optional OAuth documentation sessions
- E: `ab5b11188941d1c8c918951cdee162e9aa9f68cf` servers/ruby: preserve documentation performance contracts

## Isolation, inputs and hooks

C differs from its former tree only at
`servers/ruby/spec/client_examples/profile_mount_spec.rb`, retaining the exact
accepted 26-addition/11-deletion route assertion patch. The prior failure and
focused 7-example success/lint evidence remain untouched under
`../verification/quick-packaging-a0c78d1c/` and
`../verification/profile-mount-route-fix-a0c78d1c/`. No check chronology was
added to C's main-approved message.

D and E full-index patches are byte-identical to their predecessors. The OAuth
module/provider subtree/specs/guide and all production/performance/declaration
bytes remain unchanged. Owner0's exact four-partial Basic/final artifacts were
reused, with Basic bytes verified against the former C and current final bytes
against source; no inferred auth repair or new projection occurred. Their
restoration patch remains
`c65ea2c5c0f4c4e5c734de9c184a67e1d043faeb2c05fc6b7235d0c145708568`.
The previous zero-fuzz/no-offset restoration proof remains authoritative.
R1 and OAuth/TLS activation remain held.

The new scratch checkout reached exact B with clean source/index, then its
post-checkout hook refused the missing configuration signature. That state was
reported before intervention. Lead explicitly authorized the existing known
setup: verify exact accepted `.overcommit.yml` and custom hook bytes, link the
ignored root gem home/copy its tools lock, verify retained root availability,
and run ordinary `overcommit --sign`. See `worktree-add.log`,
`hook-configuration-hashes.json` and `hook-setup.log`. No hook bypass or
resolution/install was used. Root bundle availability passed with Ruby 3.4.11,
Bundler 4.0.23, JSON 2.21.2, Overcommit 0.73.0 and RuboCop 1.85.1, with no
HaveAPI package in that graph.

Actual C/D/E HaveapiI18n, RuboCop and commit-message hooks passed. Only C's
verbatim approved message produced the retained 72-column advisories; all lines
are within 80 columns. D/E passed without warnings. Logs, exact messages/hashes
and per-group source/path mappings are retained here. A/B retained their exact
previous hook evidence and commit IDs.

All 310 protected before/after hashes match, including current 0.31 locks,
root/Rust gem-spec graphs and JavaScript build/declarations, Python editable
metadata, independent MSRV, fixed published runtime, frozen benchmark graph,
preview graph and historical receipts/exports. Root/Rust/JS inventories also
match. See `inputs.before.json`, `inputs.after.json` and `final-state.json`.
No declaration, lock, graph, compiled artifact or source identity was refreshed.

## Recovery and review handoff

Backup `refs/heads/2026-10-27-api-documentation-redesign-pre-profile-mount-fold-20261028t132040z` retains the previous final.
Scratch `refs/heads/2026-10-27-api-documentation-redesign-profile-mount-fold-20261028t132040z` and
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-27-api-documentation-redesign/haveapi-profile-mount-fold-20261028t132040z` retain the reconstructed series.

All old refs, ranges, upstream/same-baseline proofs, auth artifacts, preview
receipts and prepared inputs remain untouched. Earlier nonancestor runtime
snapshots remain historical review evidence, without a literal-merge claim.
The final same-base range has 110 changed paths, no migrations/schema/seed
lineage and no feature dependency or channel update streams. No feature
migration needs a merged/released/deployed/external-use classification.
The existing five groups contain the final UI and test adaptation together,
with optional authentication and performance behavior separate.

Both feature and scratch full worktrees/indexes are clean. All commands have
returned and no owned watcher/test/build remains. No upstream fetch/rebase,
source repair, new test/build, dependency refresh, long gate, preview mutation,
publication, default integration, deletion or lifecycle action occurred.
The Git slot is released to lead with the completed report.

Next: owner0 resumes only its unrun packaging/gem metadata/export/frozen
availability stages against this final head, then retained final independent
review. Existing successful input refresh and unrelated quick results are not
repeated by this operation. Final review and long acceptance gates remain
pending under lead coordination.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/
