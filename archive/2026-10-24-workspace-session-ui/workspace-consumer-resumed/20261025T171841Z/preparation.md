# Workspace consumer refresh preparation

Prepared read-only on 2026-10-25 by implementer0. No rebase, source/input edit,
commit, publication, test, build, native launch, claim or activation was performed.
Ordinary origin fetch completed successfully over the existing canonical SSH
remote. The runtime publication milestone is still required before input edits.
These observations need a fresh check when that milestone arrives.

## Source and input baseline

- Verified session/environment: `2026-10-24-workspace-session-ui`, workspace
  `/home/aither/workspace/ai/vpsfree.cz`.
- Exclusive feature worktree: `worktrees/2026-10-24-workspace-session-ui/workspace`,
  branch `2026-10-24-workspace-session-ui`, clean at
  `cbaa7d949eb4e9061cda7ff896dc6d97f2e0c2aa`, tree
  `01c2fd8a84cedaed51d75823582b917935df9e69`.
- Canonical SSH origin: `git@github.com:aither64/vpsfree-cz-workspace.git`.
  Fresh cached remote master: `a6ebab6b10a8d0806f4db9588e1433b568473990`.
  Published feature still equals cbaa. Shared checkout stayed on master at
  `2082811b37e7c8d5144e857d33cdd379d8d25844`, tree
  `beeefc2b955c261f00aa35dc6081601837588cca`.
- Shared master descends from remote master by two tracking-only commits. Their
  paths are entirely under work/archive, and their complete flake/input identity
  is equal. Existing unrelated dirty files and the empty shared index were
  preserved; no root checkout/index/branch mutation occurred.
- cbaa is not an ancestor of current master. Their merge-base is the directed
  historical base `df1944a2004282d5eb988323e25c9c3010791b8d`.
  The old `b1b86b2b..e1c21698` -> `df1944a2..cbaa7d94` equivalence and review
  receipts remain in `../../workspace-input-preparation/`. The old9293 candidate
  is historical and must not be deployed.
- Current defaults select nested runtime
  `9634151b9836311c331a58880fbb4c46133fd98f`, NAR
  `sha256-tJ3kHzGpdNKat4bC7Th/Q6O3gUSTjrmVQU2A9gxVjsw=`, and codex-web
  `8b60554bc10c2a6bcbf9732a8b77ad959c317036`, NAR
  `sha256-bkEZSKkVAYbthaiyI4onS5eYQXuDj3YV8nbQlzDBeHE=`.
- Extension remains `767dfd587e346168e1443e65ccdb67ce748f3fe3`, NAR
  `sha256-om/+qNfQw6y74gjdzXfVG5AbHOQGysMefFZiqR92KP4=`. Root nixpkgs still
  follows `vpsfree-dev-workspace/nixpkgs`; effective revision
  `d58a46e3bc02d91ebe04667f8397752a749c0024`. All follows edges, extension and
  sibling nodes are unchanged. Only dev-workspace and codex-web nodes differ
  between the historical base/cbaa and current default graph.
- Current runtime native input remains e85b99217baf13a38fc887b31338b1833f1159c0.
  The approved final runtime will intentionally advance its native subtree to
  frozen ea188d2f072e0ec8d5b71245e228803672801a22 / raw Codex0.164. Preserve
  unrelated nodes; retaining old e85 in the final runtime is superseded by the
  governing native/naming amendment.
- Current master includes source-filter/storage commits4579b97f and e9144243,
  then runtime selection a6ebab6b. Preserve its cleanSourceWith exclusion of
  work/archive, filtered skills/check inputs, tracking-source check, and all
  other merged source. This worktree currently has no sparse-checkout setting;
  no sparse or registration mutation was attempted.

[Source baseline](source-baseline.json), [raw and semantic graphs](semantic-input-graphs.json),
[graph assertions](graph-comparison.json), [source changes](default-source-change.diff)
and [current reusable Git blobs](shared-master-source-blobs.json) bind these facts.
Raw locks and flake source for each exact revision are retained alongside them.
No foreign session records, private claims, team or worktrees were opened.

## Selected baseline, observed only

Profile189 resolves to `/nix/store/48011krllhj3428878a8h55sb6x4wky0-dev-workspace-0.2.0`;
deriver `/nix/store/dzjigbrkh0lxn9ybr2dhh23w2awx99dp-dev-workspace-0.2.0.drv`.
Its composition source `/nix/store/d2b3y1raszch3ach8r3l4gw9wdds9bjf-source` has the
same complete lock as current master. Runtime source is
`/nix/store/d1cnw1bqr3byn3bx4c01grdvm22xa6kw-source`.
System and system profile both resolve to
`/nix/store/1bnl145ln79094l10j60cp4631a69vww-nixos-system-aitherdev-26.05.20261021.da6dc0e`;
configuration metadata is clean2d33a9ca715d305d7b4003e17bbf3e31f1be1d60.
Selected native link resolves to
`/nix/store/jrsm1rzxm1ak23j1f2vn0lil9qgxblym-codex-package-0.163.0/bin/codex`,
SHA256 `8d733334a9ce033fd57f0e3c08064d2b1ec549d7b7f29949ae44b24e87a7c15a`.
This is selection evidence, not a new actual-daemon identity/launch observation.
No native executable or version command ran. See [selected baseline](selected-baseline.json)
and its raw contracts, catalogs, locks and metadata receipts.

## Bounded refresh plan after runtime publication

1. Receive owner1's canonical published final runtime and configuration milestone.
   Reverify exact session/owned clean worktree, fresh SSH refs and current shared
   master. Assess any new reusable source drift before changing the branch.
2. Retain original cbaa objects/diffs/review and old/new ranges. Refresh the owned
   feature onto fresh current master with ordinary rebase. cbaa's sole obsolete
   pin overlaps only flake.nix/flake.lock with master: resolve this superseded pin
   to the new published final runtime, using current-master lock/source as the
   preservation basis. Stop/report any conflict outside the two owned pin paths.
   Do not replay old9293 or discard current master filtering/storage behavior.
3. Keep one final logical runtime-selection commit: change only existing
   `inputs.vpsfree-dev-workspace.inputs.dev-workspace.url`, then run normal
   `nix flake update vpsfree-dev-workspace/dev-workspace`. No top-level input,
   extension-lock edit, native/provider override or incidental deduplication.
   Generate final nested transitive graph from the published runtime; retain
   extension767df, sibling inputs and follows. The new lock must select the same
   runtime as configuration and the reviewed dependency975746f4/rawEA0.164 graph.
4. Capture exact old/new raw locks, semantic follows/input graph, source graph,
   full base-to-head history and explicit no-migrations inventory. Check normal
   hooks/environment, parser/diff and existing deployment-contract quick tests;
   run `bin/check-dev-workspace-deployment` read-only against owner1's final owned
   configuration worktree. Commit with the normal hooks and temporary message
   file, publish only the feature under exact lease/fresh target proof, and
   refresh comparison after final head. Parent owns combined final review.
5. Bind a fresh watcher runner to that exact committed head/tree, runtime and
   configuration heads. Preserve the explicit out-link below through rollout.
   Parent owns review disposition, watcher launch and all activation/claims.

The new final input update is substantive dependency succession from oldcbaa;
its patch is not represented as equivalent to the old9293 selection. Original
mechanical rebase equivalence remains historical evidence only.

## Future rooted build recipe — not launched

Replace and validate the required final identities after publication/commits;
there is deliberately no current oldcbaa executable build runner. Parent launches
this batch through a fresh watcher only after the applicable final review.

```sh
set -euo pipefail
: "${WORKSPACE_FINAL_HEAD:?exact committed reviewed workspace head required}"
: "${CONFIGURATION_FINAL_HEAD:?exact committed configuration head required}"
: "${RUNTIME_FINAL_HEAD:?published final runtime required}"
workspace_wt=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-workspace-session-ui/workspace
configuration_wt=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-workspace-session-ui/vpsfree-cz-configuration
workspace_build_evidence=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/workspace-consumer-resumed/final-composed-build
[ "$(git -C "$workspace_wt" rev-parse HEAD)" = "$WORKSPACE_FINAL_HEAD" ]
[ -z "$(git -C "$workspace_wt" status --porcelain)" ]
[ "$(git -C "$configuration_wt" rev-parse HEAD)" = "$CONFIGURATION_FINAL_HEAD" ]
# Final runner also validates both semantic runtime pins and the recorded tree/lock digests.
mkdir "$workspace_build_evidence"
workspace_flake="git+file://$workspace_wt?rev=$WORKSPACE_FINAL_HEAD"
nix flake metadata --json --no-write-lock-file "$workspace_flake" > "$workspace_build_evidence/flake-metadata.json"
nix build --out-link "$workspace_build_evidence/workspace-candidate"   --print-out-paths --print-build-logs --no-write-lock-file   "$workspace_flake#packages.x86_64-linux.default"   > "$workspace_build_evidence/output-paths.txt" 2> "$workspace_build_evidence/build.log"
readlink -f "$workspace_build_evidence/workspace-candidate" > "$workspace_build_evidence/root-resolved.txt"
workspace_output=$(cat "$workspace_build_evidence/root-resolved.txt")
nix-store --query --deriver "$workspace_output" > "$workspace_build_evidence/deriver.txt"
nix derivation show --recursive "$(cat "$workspace_build_evidence/deriver.txt")" > "$workspace_build_evidence/recursive-derivations.json"
nix path-info --recursive --json "$workspace_output" > "$workspace_build_evidence/output-closure.json"
```

The final runner must retain command exits, before/after head/tree and raw locks,
all source/input graph receipts, package contracts/catalogs, assembled native
canonical path/SHA and all outputs/root paths. Stop/report unexpected local
kernel builds. No --no-link-only retention and no root removal during active
rollout/recovery. Do not overwrite an uncertain prior attempt; parent diagnoses
and assigns any retry with fresh receipts.

Candidate acceptance must prove actual assembled raw0.164 executable bytes equal
prerequisite SHA d2af1cd0ea4187d413c237e80204e94ffcd5c7d8142840a662156b89750f54ae,
not version/source equality. Current jrsm0.163 differs intentionally: ordinary
new-native idle transition is required, and old same-native/PID pass criteria are
superseded. Owner2 owns final candidate-vs-selected contract/native/catalog/
claim/cluster preflight; no candidate is observed or accepted here. System/profile
activation remains parent-owned, system first, after review/long gates and fresh
ordinary claim checks. No default integration approval or lifecycle action.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-workspace-session-ui/
