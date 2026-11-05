# Configuration pin and system preparation receipt

Published configuration feature: `4a9be5ba5f248d9e3aa5a4119b1765503b5c95c9`, selecting reviewed and published
runtime `7302f4dc961ded7c768733e25ec39e3c603e093b`. Source/tree/lock are clean and frozen for the
fresh system build. B's one matching check passed against its final tracking-rebased
workspace `d250081c66cadbd48925ca8eb1e58f982b03c878`. The fresh system build passed;
all A command effects are settled and the config Git lane returns to the lead.
The lead owns final schema-1 mechanical-refresh review reuse proof. No copy,
claim, activation, profile switch, default integration or lifecycle is authorized
by this preparation.

## Current exact sources

| Item | Identity |
| --- | --- |
| Configuration checkout | `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-02-session-temporary-service-cleanup/vpsfree-cz-configuration` |
| SSH origin | `git@github.com:vpsfreecz/vpsfree-cz-configuration.git` |
| Branch | `2026-11-02-session-temporary-service-cleanup` |
| Original registration base / current parent / remote master | `c040c14cdbacc07998700b524996a89306188d7f` |
| Final configuration head | `4a9be5ba5f248d9e3aa5a4119b1765503b5c95c9` |
| Final tree | `70c5f4274cc76d4d729a4d330ae6d42c10973752` |
| Configuration source | `/nix/store/axyscs608hxhgqqg7grdb77sdajcyc53-source` |
| Configuration NAR | `sha256-v1zDgp6PxR/75DCvpbKjQrJi0n9ugdj8wXWTSvJoke8=` |
| Final lock SHA256 | `6107ad85467250287f1882412d89a480dbf5ef76a49ed5ec7b9867ed9338a5bd` |
| Runtime head | `7302f4dc961ded7c768733e25ec39e3c603e093b` |
| Runtime tree | `934f92ba1bc27675161f315ae0a8835ff1d7d8f3` |
| Runtime source | `/nix/store/9fsjqqji9kyflc74nrhxz4fwxb2xv2x5-source` |
| Runtime NAR | `sha256-bILeNLuxVReQbq2RvL2wvgOr5NMmlLTd+8p1mG43gz0=` |
| Unchanged runtime lock SHA256 | `fa808c04beeaf2ea5d6dfb4b76b1bd6ff1a166e298771de3756a646a5294a955` |

B's [runtime publication receipt](runtime-7302-publication-receipt.json) binds
actual SSH feature/default proof and source/NAR. The lead accepted the same
reviewer's affected UI follow-up for exact `7302f4dc`; the receipt's older
awaiting-review text is historical. No unpublished or guessed runtime was used.

## Single pin stream, graph and publication

Fresh configuration fetch found remote master unchanged at `c040c14c` and the
feature exactly at the authorized old lease `46e28111`. After retaining that
published head/ref and full receipt, ordinary Git rebase restored the clean
feature to the original baseline. The exact authorized generator ran:

```sh
nix develop --command confctl inputs channel set --commit dev-workspace devWorkspace 7302f4dc961ded7c768733e25ec39e3c603e093b
```

It passed in 16.657 seconds. Normal Overcommit pre-commit
Nixfmt and commit-message checks passed; expected generated TextWidth warnings
were retained. No manual lock edit, reconstructed changelog or hook bypass.
The complete final range is one pin commit, only `flake.lock` (3+/3-):

```text
inputs: set devWorkspace to 7302f4dc

devWorkspace: c2182254 -> 7302f4dc
git log for c2182254d29c4175c3e9fe4267e5a92dd1da6b79..7302f4dc961ded7c768733e25ec39e3c603e093b
> 7302f4d portal: expose registered services and protect lifecycle handoff
> 565e289 sessions: retire registered temporary services before file cleanup
> 19dd03b portal: group session resources and show retained counts
```

The 64-node baseline comparison differs only at `devWorkspace.locked.rev`,
`narHash` and `lastModified` (`1793653260`). Every other node, original selector,
root/child edge and follows path is preserved. Separately resolving all follows
proves the complete nine-node managed runtime subgraph matches standalone
runtime identities, original selectors and relationships. Runtime/configuration
metadata binds the exact committed graph, revision, timestamp and reviewed NAR.

Normal SSH publication used exactly
`--force-with-lease=refs/heads/2026-11-02-session-temporary-service-cleanup:46e281115294e5d45286b60c8ff862ac287d862b`.
Fresh remote verification returned feature `4a9be5ba5f248d9e3aa5a4119b1765503b5c95c9` and unchanged master
`c040c14cdbacc07998700b524996a89306188d7f`. Clean index/tree and committed source persisted. No master push,
PR, unsolicited rebase or source change occurred.

Proofs under `config-pin-7302f4dc/`:

- [Complete graph/history proof](config-pin-7302f4dc/graph-and-history-proof.json) and [resolved nine-node proof](config-pin-7302f4dc/managed-runtime-subgraph-proof.json).
- [Baseline graph](config-pin-7302f4dc/baseline.lock.json), [final graph](config-pin-7302f4dc/final.lock.json), [configuration metadata](config-pin-7302f4dc/flake-metadata.json), [runtime metadata](config-pin-7302f4dc/runtime-flake-metadata.json), and [runtime lock](config-pin-7302f4dc/runtime.lock.json).
- [Generator log](config-pin-7302f4dc/operation.log), [status](config-pin-7302f4dc/status.json), [retained-ref preparation](config-pin-7302f4dc/stream-preparation.json), and [fresh target](config-pin-7302f4dc/fresh-target.json).
- [Leased publication receipt](config-pin-7302f4dc/publication.json) and [normal push log](config-pin-7302f4dc/publication.log).

## Fresh system artifact preparation

The separately granted command runs from the exact final clean configuration:

```sh
nix develop --command confctl build --yes cz.vpsfree/machines/aitherdev
```

Build passed exit zero in **101.594 seconds**. Command/head/tree/runtime/lock/PID/process-group/timing are in
[build-status.json](config-system-preparation-7302f4dc/build-status.json), with
[CLI log](config-system-preparation-7302f4dc/build.log) and
[retained full confctl log](config-system-preparation-7302f4dc/confctl-build-full.log).
The permitted visible parent-monitoring fallback applies because the lead's CI
watcher held the sole utility slot at launch; no extra watcher or CI polling.
Confctl's normal success-log unlink/recovery behavior is unchanged: an external
read descriptor retains the complete log without changing that command.

Exact printed generation: **`2026-11-02--22-21-01`** for
`cz.vpsfree/machines/aitherdev`. The authorized local generation list confirms it
with runtime `7302f4dc`; it is a build result, not live-machine status.

| Artifact | Store path |
| --- | --- |
| Toplevel | `/nix/store/4cblp6s3wvxcnhdmzjsdnkvnifrh5zvk-nixos-system-aitherdev-26.05.20261026.718f670` |
| Toplevel derivation | `/nix/store/v7g4cf8z04ds77f75ic4jzhm4nx5mhdb-nixos-system-aitherdev-26.05.20261026.718f670.drv` |
| Auto-rollback | `/nix/store/yl9vnin9wlv04cip0sqpkisk80xmccwh-auto-rollback.rb` |
| Auto-rollback derivation | `/nix/store/za41c9rsf8k0qv0ay8svf4kc4y2x0q51-auto-rollback.rb.drv` |

[artifact-receipt.json](config-system-preparation-7302f4dc/artifact-receipt.json)
binds the exact named generation, configuration/runtime revisions and NARs,
toplevel/derivations, all four generation inputs and immutable revisions,
output/source NAR metadata, full 64-node source/flake graph and complete
6,534-node recursive derivation/source-input graph. The graph retains every input
edge without environment-value dumps. Graph SHA256:
`00f1b2d828e5ef739afb54b3414f630b183a6cad924cdba70483b8f0ff628b39`.
Full retained confctl log SHA256:
`d8ec346c783a9e93c8b9f1cf7e051556914fcbfa161bfacdd48a42d98df1ce40`.

Supporting evidence: [local generation list](config-system-preparation-7302f4dc/generation-ls.log),
[generation metadata](config-system-preparation-7302f4dc/generation.json),
[source/flake graph](config-system-preparation-7302f4dc/source-full-input-graph.json),
[recursive input graph](config-system-preparation-7302f4dc/system-derivation-input-graph.json),
[output/source NAR data](config-system-preparation-7302f4dc/output-and-source-path-info.json)
and [Nix toplevel build log](config-system-preparation-7302f4dc/toplevel-build.log).

Twelve small derivations and three fetched dependencies completed; no kernel build
or activation command occurred. Fresh remote feature/default proof and clean
source/tree/lock still match publication. No process remains running and no
uncertain effect remains. Copy, claims, activation, profile changes, reboot,
integration and lifecycle were not performed.

Old generation `2026-11-02--21-41-36` remains held and proves only
configuration `46e28111` / runtime `3d76f527`. It is not reused for the final Git
revision. Application deployment stays in the workspace user profile; the system
configuration selects the matching host/module contract. Original auto-rollback
and generation evidence remain under confctl.

## Final workspace matching result

B's ONE final checker passed exit zero in 7.624 seconds against final workspace
`d250081c66cadbd48925ca8eb1e58f982b03c878`, lock SHA256
`40d633b5de02817489bff707e399e495cf5a3d987f7a10046c346bbb84d591e2`, and
configuration `4a9be5ba`, lock SHA256 `6107ad85467250287f1882412d89a480dbf5ef76a49ed5ec7b9867ed9338a5bd`.
Exact heads, clean states and hashes were verified before and after, with actual
runtime locked identity/NAR equal and no pending operations. No intermediate
`15d` check ran. B reports exact-lease workspace publication and source NAR
`sha256-DGxAe6hjRIY7QM4Ha0JRfjOcAEv59oo8zqSp1klwfwE=`.
See [matching receipt](workspace-pin-7302-matching-receipt.json) and
[B's final source/rebase receipt](workspace-pin-7302-final-receipt.json).
A did not duplicate the checker, workspace reconstruction or CI observation.

## Historical streams and artifacts

All old configuration heads are outside the final feature ancestry, retained at
explicit refs; no repeated pin remains in the one final stream. There are no
migrations or supported deployed-state boundaries requiring intermediate pins.

| Runtime scope | Old configuration | Retained ref suffix | Historical evidence |
| --- | --- | --- | --- |
| `3d76f527` | `46e281115294e5d45286b60c8ff862ac287d862b` | `-config-pin-3d76f527` | [Exact full prior receipt](config-pin-7302f4dc/historical-3d76-receipt.md), [pin graphs](config-pin-3d76f527/graph-and-history-proof.json), [system artifact](config-system-preparation/artifact-receipt.json) |
| `e29d4d83` | `abee6aec3ade96eb902132bea11d2eba2d6c8119` | `-config-pin-e29d4d83` | [Historical receipt snapshot](config-pin-3d76f527/historical-e29-receipt.md), [graphs/source proof](config-pin-final/graph-and-history-proof.json) |
| `312d2e2a` | `7b6d1a12571507eebf59de75806cd922b666788c` | `-config-pin-312d2e2a` | Initial receipt retained inside historical snapshots above; [graph proof](config-pin-graph-proof.json), [source metadata](config-pin-flake-metadata.json) |

Each suffix is prefixed by `refs/heads/2026-11-02-session-temporary-service-cleanup`.
All old graph/source/command receipts remain intact. Their matching checks,
review ranges, native creation and artifact results retain their original scope;
no tree-only or filtered-input-incompatible reuse is claimed.

The current pin, publication and later exact system result are preparation only.
The lead retains matching-source/certificate/check gates and all later actual
copy, machine ownership and activation work. No lead-owned rollout/state edits.

Session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-session-temporary-service-cleanup/
