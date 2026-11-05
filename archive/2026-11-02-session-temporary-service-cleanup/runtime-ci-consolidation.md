# Corrected runtime consolidation and publication

Owner: implementer1, retained Sol/xhigh/workspace_write. Bound session identity
matched; both DEV_SESSION markers were absent. Settings/access are unchanged.

The corrected feature is published at
`e29d4d83fc62e0dc929aca332f324336c9c8b034`, exact accepted tree
`9b93683362e149ba6f2599232bc1fbbbe4694a17`. The runtime index/worktree are clean,
no command remains running, and the Git lane is returned to lead. CI observation
belongs to lead; workspace/configuration pins still select stale312 and are held.
No default integration, PR, pin change, build, deployment, claim or lifecycle
action occurred in this package.

## Complete series and retained provenance

Fresh SSH fetch and remote checks confirmed base/master
`c2182254d29c4175c3e9fe4267e5a92dd1da6b79` and previous published feature
`312d2e2a8994c136f96938d2f2a71ae8e2f16f33`. Only accepted correction
`d13751ffb615ef2af930ea8a22979d04394bd4a5` was autosquashed into its owning
core commit, in the normal repository Nix shell with declared hooks preserved.
No source or commit-message edits were made. The complete final series is:

1. `e5c26680a8c91cb7db31dab695453be054475e1c` — Resources navigation/counts.
2. `c59ad3206f06fc3bf75947efbc6d19d13961fd54` — registered service lifecycle.
3. `e29d4d83fc62e0dc929aca332f324336c9c8b034` — projection/host compatibility.

The full base-to-head diff is 47 files, 4,065 insertions/119 deletions.
Range-diff against the published312 series reports UI and dependent patches `=`;
the core differs only by the lead-accepted three-file, 71+/5- CI correction.
The unpushed fixup is folded; no obsolete follow-up commit remains. Exact tree
comparison with pred137 passed. See [CI remediation](ci-remediation.md) for cause,
direct lead inspection and correction evidence. No design/API/schema/ownership
boundary expanded, so the existing final review and direct narrow-fix acceptance
remain applicable; no redundant whole-content review was launched.

Retained local recovery refs:

- `2026-11-02-session-temporary-service-cleanup-published-312d2e2a` at old312.
- `2026-11-02-session-temporary-service-cleanup-pre-ci-consolidation` at d137.
- Existing `2026-11-02-session-temporary-service-cleanup-pre-consolidation`
  retains all earlier unpublished fixup history.

No DB migrations, new persisted formats or consumption boundary changes were
introduced by this correction. Old312 publication, failed CI and the two stale
unpublished downstream pin snapshots are retained as provenance. No new runtime
dependency/pin stream exists. Each later workspace/configuration replacement
must consolidate its existing logical stream into one final pin update.

## Exact source, graph and verification reuse

- Source: `/nix/store/snbsx4bqra8nkr8qsy6h13mydriq79sj-source`.
- Source NAR: `sha256-f3UjSBS9+zyEULhOdBjiBG04aDiqTKNsjzuwokIYzJ4=`.
- flake.nix SHA256: `124305e752c69b6c0fbe9a635793c7dee38beaf3f0503b53d02445d6c04bedc9`.
- flake.lock SHA256: `fa808c04beeaf2ea5d6dfb4b76b1bd6ff1a166e298771de3756a646a5294a955`.
- Filtered Ruby source:
  `/nix/store/032kq2fwxbidrsaavf38vwskkrckd3v6-dev-workspace-ruby-source`.
- Filtered source NAR: `sha256-YofCVP7YhwSMX2ynV8e/hD0vh4y1dPARm0uXvr2cxgQ=`.
- Complete recursive derivation receipt SHA256:
  `d5ff3b20d01f39941cbbc7301d7fb43b27297dade73e7fa87a3048af03028898`.

The complete runtime input graph, nodes, originals and follows are unchanged.
Exact-revision Nix evaluation at the final committed head reproduces A's three
exported shard derivations and outputs. Recursive derivation structures and
their receipt bytes match A's proof exactly; the filtered Ruby path and NAR
also match. This rebinds the successful affected shards0/2/3 result of 390 tests,
5,281 assertions and 11 configured skips (224.761 seconds) to the final head.
Tree equality alone is not used for reuse. Shard1, complete four-shard coverage
and native VM acceptance are not claimed by this component result.

Only necessary quick checks ran at final e29: syntax for the three changed Ruby
files, whole-range whitespace, exact head/tree/source/input identity and clean
index/worktree. All passed in the repository Nix environment. No build or long
suite was repeated. The source and lock remained unchanged.

## Publication and CI handoff

SSH publication used an explicit lease for the observed old312 feature ref.
Fresh remote evidence confirms final e29 and unchanged masterc218; only the
feature ref changed. [Check41509697499](https://github.com/aither64/dev-workspace/actions/runs/41509697499)
was in progress at exact e29 when captured. Old Check41503878011 is completed
failure. No superseded queued/in-progress run existed; nothing was cancelled.
No current-head run was cancelled and B did not launch a watcher or await CI.

## Evidence and next action

- [Complete receipt, graph and shard identities](runtime-ci-consolidated-receipt.json)
- [Before refs, series and graph](runtime-ci-consolidation-before.json)
- [Published312 to final range-diff](runtime-ci-consolidation-range-diff.txt)
- [Pred137 to final range-diff](runtime-ci-consolidation-fixup-range-diff.txt)
- [Accepted correction diff](runtime-ci-accepted-correction.diff)
- [Complete final diff](runtime-ci-consolidated-base-to-head.diff)
- [Final exact source metadata](runtime-ci-consolidated-metadata.json)
- [Final recursive derivations](runtime-ci-consolidated-recursive-derivations.json)
- [Quick check output](runtime-ci-consolidated-quick.log)
- [Remote refs](runtime-ci-consolidated-remote.txt)
- [CI run inventory](runtime-ci-consolidated-runs.json)
- [A's successful shard receipt](ci-remediation-shards/verified-result.json)

Lead owns fresh CI monitoring. B is source/Git idle and awaits separate exact-SHA
workspace pin assignment. Old312 pin and matching-check evidence remain held.
Final mechanical-pin/history conclusion still waits for both corrected pins.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-session-temporary-service-cleanup/
