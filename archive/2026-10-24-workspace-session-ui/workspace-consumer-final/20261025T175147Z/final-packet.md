# Final workspace consumer packet

**Committed, quick-checked and feature-published; combined final review pending.**
Implementer0 owns only the workspace consumer pin. No long/native/build/candidate
run, live capture, claim, activation, default integration or lifecycle action
was performed. Source is frozen and the Git window is released.

## Exact review and publication range

- Repository `git@github.com:aither64/vpsfree-cz-workspace.git`, default `master`.
- Worktree `worktrees/2026-10-24-workspace-session-ui/workspace`, feature
  `refs/heads/2026-10-24-workspace-session-ui`.
- **Review base:** `0905143a3aa18c22a871f47afd76a47877bc32fb`.
- **Final head:** `7c3d482cf1000d5608e445b180467c968d9d1262`.
- **Final tree:** `e97914bd93346791b93d0f36709fabd7f344bd89`.
- One commit, `deps: select naming and session controls runtime`; only
  `flake.nix` and `flake.lock`, 16 insertions/15 deletions. The final
  [history](final-history.txt) and [complete own-range diff](final-base-to-head.diff)
  bind the final intended update. No superseded intermediate pin remains.
- Fresh SSH preflight observed remote master
  `a6ebab6b10a8d0806f4db9588e1433b568473990` and exact old featurecbaa. A single
  exact oldcbaa-lease feature push succeeded; fresh SSH verification proved final
  7c3 and unchanged a6 master. Own worktree/index are clean. See
  [original publication proof](publication-receipt.json) and push/verify outputs.

The current shared-master comparison baseline0905143 descends from remotea6 by
three **inherited baseline commits**:90a83a7e tracking,2082811b archive tracking,
and0905143 tracking plus the existing reusable Ruby package-layout note. Their
commit IDs, subjects and path classes/counts are recorded in
[history and preservation inventory](history-migration-preservation.json).
No foreign session record contents were opened or copied; no unfiltered
remote-base workspace diff was generated. The own feature range is0905143..7c3,
not a6..7c3. Shared root remains master with all unrelated dirty records/index
preserved. These inherited commits are baseline context rather than new consumer
feature work.

## Inputs and source preservation

The source edit changes only the existing direct nested
`inputs.vpsfree-dev-workspace.inputs.dev-workspace.url`. Normal scoped
`nix flake update vpsfree-dev-workspace/dev-workspace` generated the lock.
Exactly four nodes change, with no input-edge/follows or node-inventory changes:

| Input path below vpsfree-dev-workspace/dev-workspace | Before | Final |
| --- | --- | --- |
| runtime itself |9634151b9836311c331a58880fbb4c46133fd98f |b24164822fd33c330a6e5511e4d1580ab6590224 |
| codex-web |8b60554bc10c2a6bcbf9732a8b77ad959c317036 |975746f40fe99c77689ede064197772e2cc25c18 |
| llm-agents |e85b99217baf13a38fc887b31338b1833f1159c0 |ea188d2f072e0ec8d5b71245e228803672801a22 |
| llm-agents/nixpkgs |319e4cebef10cbb636c6ea392137b52ad105336a |f20cd90e28fe0403873f473b29e42662cd86e8c4 |

Final runtime NAR is `sha256-QgmgJ9X7LQRVbht2WyOySwO9Hd81cdRfX+AAgjXUEd8=`;
its published source is `/nix/store/69p6k5n0863zimpdb2kv3k8i4vrgpjg0-source`.
Extension remains exact767dfd587e346168e1443e65ccdb67ce748f3fe3, NAR
`sha256-om/+qNfQw6y74gjdzXfVG5AbHOQGysMefFZiqR92KP4=`. Root nixpkgs follows
`vpsfree-dev-workspace/nixpkgs` and remains d58a46e3. All other nodes, siblings and
follows are unchanged. The runtime subgraph agrees with its published immutable
lock. No extension-lock edit, top-level runtime input, incidental deduplication,
provider override or native downgrade was made.

All base source except the two pin files is inherited unchanged. The flake diff
is exactly the nested URL substitution; master4579/e914 compact source filtering,
filtered skill/check inputs and storage/retention behavior remain unchanged.
[Raw final source/lock](workspace-final.flake.nix),
[complete raw lock](workspace-final.lock.json),
[semantic paths and follows](semantic-input-graphs.json),
[semantic assertions](semantic-input-check.json) and
[full source/input graph](source-input-graph.json) retain exact identities.
The exact workspace Git source NAR/recursive derivation graph will be captured by
the future post-review watcher; no source realization/build is claimed here.

The checker was bound to owner1's clean final configuration
06351ae9dc3611d0ef5b298f5b6e5cafb4b79d4d/tree06cbb2f13ca6cb605846ea528b9b657947e60103,
whose matching lock is preserved in [configuration receipt](configuration-source-receipt.json)
and [raw lock](configuration-final.lock.json). Its later published receipt names
source `/nix/store/1lcnp25vv587zb067x9bxaj1anb4pwwf-source`, NAR
`sha256-YWbwMrgD6mOqhyjT32mjjtT0SMF5l4mwW82ICpb/wUk=`. Publication did not change
that tested configuration head or lock; no checker repetition was needed.

## History, state and earlier evidence

Original reviewed b1b86b2b..e1c21698 -> directed df1944a2..cbaa7d94 equivalence
remains in the historical workspace-input-preparation receipts. Oldcbaa is
retained at `refs/heads/2026-10-24-workspace-session-ui-reviewed-cbaa` and as
exact source/diff/history artifacts in this directory. Its sole obsolete9293 pin
was dropped during the ordinary rebase onto current0905143; one final963->b241
selection replaces it. [Old/new range-diff](old-new-range-diff.txt) is retained,
with **no claim that the new input update is patch-equivalent to old9293**.
No old9293 candidate or source-session consumer pin was replayed.

**No workspace migrations** or schema changes are introduced. The selected
runtime preserves the deployed963/codex-web8b605 SQLite/admission/reliability
boundary and the four portal fixes, with the approved naming/capacity and raw
0.164 compatibility changes. Existing supported migration/state lineage must
remain in the combined review. Actual native0.163-to0.164 persistence and old-reader
acceptance are deferred parent-owned gates; this pin does not establish safe
mixed writers, downgrade or fallback behavior. See the runtime/dependency packet
links in the source graph for their full histories and migration inventories.

No new project documentation is useful for this routine selection update;
existing workspace deployment/update procedures already own the input contract.
This session packet records only this rollout's exact revisions and evidence.

## Verification and future watcher

- Declared locked-nixpkgs Nix Ruby environment: deployment contract **4 runs,
  19 assertions, zero failures/errors/skips**. Exact commands/logs/exits are in
  [quick results](quick-results.json).
- Real cross-repository checker PASS for canonical portal identity/aliases and
  runtimeb241 against exact configuration06351.
- Nix parser and own-range whitespace PASS; semantic graph/follows/source-filter
  preservation assertions PASS. Only the two tested pin files were committed.
- No declared hook framework, core.hooksPath or active ordinary hooks. Normal
  temporary-message-file commit ran in the pinned Nix environment with no bypass;
  [commit receipt](commit-receipt.json) retains the exact command and message.
- No native/provider/CI acceptance or independent review is inferred. Earlier
  codex-web/runtime quick evidence remains in its own exact-source packets.
  Parent owns final combined review and subsequent watcher/CI coordination.

Prepared command for the parent's fresh post-review watcher, **not executed**:

```sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/workspace-consumer-final/20261025T175147Z/build-workspace-candidate.sh
```

[Runner](build-workspace-candidate.sh) SHA256 `5bf164ac7b19c005bf37663b1f35034010ea647035f960b63c2f0fb23e465dfc`;
`bash -n` PASS only. Short guards require exact session/environment, final
workspace7c3/treee979, configuration06351/tree06cb, both lock SHA256 values,
clean source, matching full runtime locked identity, extension767df,
dependency975 and nativeEA. It builds only exact committed Git source through an
explicit `composed-build/workspace-candidate` out-link/GC root and retains source
metadata, paths, deriver and recursive source/closure graph. The attempt directory
must be absent; it refuses overwriting an uncertain prior attempt. Stop/report
unexpected local kernel builds through the watcher. Keep the root through all
rollout/recovery obligations; no cleanup is authorized.

Owner2/parent separately owns actual assembled native-byte equality to rawd2af,
contract/catalog/claim/cluster checks and the new-native idle-transition preflight.
Current old0.163 selection cannot satisfy a same-native/PID acceptance criterion;
those old criteria are superseded. The runner does not launch Codex, claim a
resource, activate a profile, or alter lifecycle state. Parent owns system-before-
profile rollout after all final review/native/build gates. No default integration
is approved.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-workspace-session-ui/
