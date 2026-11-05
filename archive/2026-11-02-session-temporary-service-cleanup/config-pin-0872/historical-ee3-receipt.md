# Configuration pin and system preparation receipt

Published configuration feature **`59d12a3b980d46f32f694a8cc98d7e965b9b66c8`** selects reviewed and
published runtime **`ee3f1fdd0d3585a8f4fa9b952169d692e9fa3d5f`**. The fresh system build passed;
all A command effects are settled and runtime/config Git lanes return to the
lead. B's one final matching checker passed at exact workspace
`b7d8152b068009063cba7a940190722dc89c6941` and this configuration. These are
prepared artifacts: required native/check/certificate gates remain lead-owned.
No copy, claim, activation, profile switch, reboot, default integration or real
session lifecycle action was performed.

## Exact sources and publication

| Item | Identity |
| --- | --- |
| Configuration root | `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-02-session-temporary-service-cleanup/vpsfree-cz-configuration` |
| SSH origin | `git@github.com:vpsfreecz/vpsfree-cz-configuration.git` |
| Feature branch | `2026-11-02-session-temporary-service-cleanup` |
| Original registration base / unchanged remote master | `c040c14cdbacc07998700b524996a89306188d7f` |
| Configuration head / tree | `59d12a3b980d46f32f694a8cc98d7e965b9b66c8` / `d6c5d3ffffd8d9e9a385a1fcec755bcf33fbb52a` |
| Configuration source | `/nix/store/swwhax2awfh71ha1607clbpxm54j41wx-source` |
| Configuration source NAR | `sha256-rqZQjm6wykm7JB/DJt1SZSyMguAr4Oi/tUXUIiHla3E=` |
| Configuration lock SHA256 | `c4dce3d1abedd9e9dc28a186d78d38a0318d46463b9fc3fc271e1446ac0fc7fb` |
| Runtime head | `ee3f1fdd0d3585a8f4fa9b952169d692e9fa3d5f` |
| Runtime source | `/nix/store/8ygzal9j12xj6x600ws7yrhgn1ijngx2-source` |
| Runtime NAR | `sha256-5mDdLgLQl/XPjIs9Ey5l2UDxWwVKR/VWpNCQwEvqsiw=` |
| Unchanged runtime lock SHA256 | `fa808c04beeaf2ea5d6dfb4b76b1bd6ff1a166e298771de3756a646a5294a955` |

Runtime publication used the exact old `7302f4dc` lease after fresh SSH checks;
feature is exact `ee3f1fdd`, master remains `c2182254`, and source/index stayed
clean. One CI discovery identified Check41533913313 at exact ee3. The lead's
fresh Luna watcher owns observation; A did not poll or wait on CI. See
[runtime publication receipt](runtime-ee3-publication-receipt.json).
The reviewed 672-file source snapshot stays rooted for active evidence use.

Fresh configuration fetch found master unchanged at `c040c14c` and feature at
exact authorized old lease `4a9be5ba`. That old head/ref and complete receipt were
preserved before ordinary rebase removed the superseded one-commit pin stream.
The exact generator ran from the clean baseline:

```sh
nix develop --command confctl inputs channel set --commit dev-workspace devWorkspace ee3f1fdd0d3585a8f4fa9b952169d692e9fa3d5f
```

It passed in 17.086 seconds. Normal Overcommit Nixfmt and commit-message hooks
passed; the generated message's expected width warnings were retained. No
manual lock/message edits, reconstructed changelog or hook bypass. The complete
baseline-to-head range is ONE pin commit, only `flake.lock` (3+/3-). Actual message:

```text
inputs: set devWorkspace to ee3f1fdd

devWorkspace: c2182254 -> ee3f1fdd
git log for c2182254d29c4175c3e9fe4267e5a92dd1da6b79..ee3f1fdd0d3585a8f4fa9b952169d692e9fa3d5f
> ee3f1fd portal: expose registered services and protect lifecycle handoff
> f7add7c sessions: retire registered temporary services before file cleanup
> 19dd03b portal: group session resources and show retained counts
```

All 64 graph nodes are preserved; only `devWorkspace.locked.rev`, `narHash` and
`lastModified` change versus the original baseline. All other 63 nodes,
original selectors, edges and follows paths are unchanged. Resolving every
follow also proves all nine managed runtime nodes, original selectors and
relationships match standalone reviewed ee3 with its independently hashed NAR.
The [graph/history proof](config-pin-ee3f1fdd/graph-and-history-proof.json) and
[managed subgraph proof](config-pin-ee3f1fdd/managed-runtime-subgraph-proof.json)
retain complete evidence, source metadata and original/final locks.

Configuration publication used exact `4a9be5ba` force-with-lease over SSH.
Fresh remote proof returns feature `59d12a3b980d46f32f694a8cc98d7e965b9b66c8` and unchanged master
`c040c14cdbacc07998700b524996a89306188d7f`; source/index remained clean after the build.
See [publication receipt](config-pin-ee3f1fdd/publication.json).
No master push, PR or unsolicited source rebase occurred.

## Fresh named system artifact

From that exact final clean configuration, A ran:

```sh
nix develop --command confctl build --yes cz.vpsfree/machines/aitherdev
```

It passed exit zero in **110.239 seconds**,
printing generation **`2026-11-02--23-08-23`** for `cz.vpsfree/machines/aitherdev`.
Twelve small derivations and three substitutions completed; no kernel build or
activation ran. The sole utility slot belonged to the lead's exact-ee3 CI
watcher, so the announced monitor-skill parent fallback applied. Independently
accessible [status](config-system-preparation-ee3f1fdd/build-status.json) and
[CLI log](config-system-preparation-ee3f1fdd/build.log) retain command, process
identity, source, phase and exit status. A read descriptor preserved the
[complete confctl log](config-system-preparation-ee3f1fdd/confctl-build-full.log)
through its unchanged normal success unlink. No command was relaunched.

| Artifact | Store path |
| --- | --- |
| Toplevel | `/nix/store/r8465y2yiy1w727yzz9myqp8hdh34ssi-nixos-system-aitherdev-26.05.20261026.718f670` |
| Toplevel derivation | `/nix/store/j8hjacsybs2z8qghny9qxrsckpzppw8j-nixos-system-aitherdev-26.05.20261026.718f670.drv` |
| Auto-rollback | `/nix/store/yl9vnin9wlv04cip0sqpkisk80xmccwh-auto-rollback.rb` |
| Auto-rollback derivation | `/nix/store/za41c9rsf8k0qv0ay8svf4kc4y2x0q51-auto-rollback.rb.drv` |

The system's embedded configuration-info names exact final head `59d12a3b980d46f32f694a8cc98d7e965b9b66c8`
with `revisionDirty=false`; this is a fresh commit build, not tree-only reuse.
Normal [local generation listing](config-system-preparation-ee3f1fdd/generation-ls.log)
confirms the exact name. Existing confctl/auto-rollback behavior remains intact.

The [artifact receipt](config-system-preparation-ee3f1fdd/artifact-receipt.json)
binds all four generation-recorded source paths, independently hashed NARs,
actual lock identities, output/source metadata, full 64-node source graph and
**6,534-node recursive derivation graph** for BOTH toplevel
and auto-rollback roots. Every recursive derivation edge resolves; environment,
argument and structured attribute values are omitted from the graph evidence.
Graph SHA256: `b64218bda34085cd4a3e6925062b07822647988ce93d3b6447be38dc84e58903`.
Full confctl log SHA256: `1aa745af12d2caa1695d1c418e3d8d04a26d72c8ece6e7657cd5459fea6ae1be`.

A generated metadata discrepancy is explicitly retained. Home Manager's actual
source `/nix/store/qh7n70gsg3rmvyn5zi1x1vhnwbrnm5wx-source` independently hashes to
`sha256-wnV9ttf4fPWNonBIQmvlrSlNpQYgx5HgWWd007mwIFA=`, matching locked
`home-manager_2` revision `e28654b71096e08c019d4861ca26acb646f583d8`.
Raw generation `inputs_info` instead labels it `c47b2cc6`. The same source path
and stale label exist in the old7302 generation. All three nonruntime source
paths and raw input-info records are unchanged. The raw generation was not
edited; [actual source bindings](config-system-preparation-ee3f1fdd/generation-input-bindings.json)
record the correct NAR-to-lock identities separately. No unrelated confctl fix,
source change or rebuild was attempted. The actual sources match the intended
unchanged graph; the stale generated label is not used as revision proof.

No owned build process group remains; the source/head/tree/lock and fresh remote
refs were reconciled after completion. The build changed only confctl's local
named generation/current build pointer. It selected no live machine or profile.

## Final matching result and historical scope

B's ONE final matching check passed exit zero in 7.794 seconds
at exact workspace `b7d8152b068009063cba7a940190722dc89c6941`, lock
`94c9da5e27bb017551598294f22cdc79393f262f4c44928148490c480fc0dab3`, and
configuration `59d12a3b980d46f32f694a8cc98d7e965b9b66c8`, lock `c4dce3d1abedd9e9dc28a186d78d38a0318d46463b9fc3fc271e1446ac0fc7fb`.
Pre/post exact heads, hashes and cleanliness passed, and actual runtime revision
and NAR match. No intermediate checker ran. See
[matching receipt](workspace-pin-ee3-matching-receipt.json) and
[B's final workspace receipt](workspace-pin-ee3-final-receipt.json).
A did not duplicate this checker, workspace reconstruction or CI observation.

All superseded pins are outside the final feature ancestry and retained at the
explicit `refs/heads/2026-11-02-session-temporary-service-cleanup-config-pin-`
refs below. No repeated pin remains. No migrations or supported deployed-state
boundaries require intermediate pin commits.

| Historical runtime scope | Old configuration head | Ref suffix / retained evidence |
| --- | --- | --- |
| `7302f4dc` | `4a9be5ba5f248d9e3aa5a4119b1765503b5c95c9` | `7302f4dc`; [full prior receipt](config-pin-ee3f1fdd/historical-7302-receipt.md), [graphs](config-pin-7302f4dc/graph-and-history-proof.json), [system](config-system-preparation-7302f4dc/artifact-receipt.json) |
| `3d76f527` | `46e281115294e5d45286b60c8ff862ac287d862b` | `3d76f527`; [full receipt](config-pin-7302f4dc/historical-3d76-receipt.md), [system](config-system-preparation/artifact-receipt.json) |
| `e29d4d83` | `abee6aec3ade96eb902132bea11d2eba2d6c8119` | `e29d4d83`; [full receipt](config-pin-3d76f527/historical-e29-receipt.md), [graphs](config-pin-final/graph-and-history-proof.json) |
| `312d2e2a` | `7b6d1a12571507eebf59de75806cd922b666788c` | `312d2e2a`; [graphs](config-pin-graph-proof.json), earlier full receipt inside snapshots above |

Old generation `2026-11-02--22-21-01` / toplevel `4cblp6s3` remains HELD at7302;
older `2026-11-02--21-41-36` remains HELD at3d76. Their old checker, review,
creation/native and artifact results retain those exact scopes. Neither was
reused for the new configuration Git revision. All previous receipts stay intact.

The runtime review source root in
`tracking/runtime-ci-7302f4dc/review-source-ee3f1fdd/source` and configuration
source root `config-pin-ee3f1fdd/source` stay ACTIVE under this tracking directory.
Their exact root targets and ordinary retirement provenance are recorded; no
root retirement, GC policy change or session cleanup was performed.

The workspace application remains separate in its user profile. The system
configuration selects the matching host/module contract. Prepared artifacts stay
held; the lead owns remaining native verification, certificate and any later
copy/claim/activation package. No lead-owned rollout/state edit.

Session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-session-temporary-service-cleanup/
