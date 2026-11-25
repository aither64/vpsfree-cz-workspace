# Workspace successor — successful package/publication handoff

Reviewed and published source **ecefa547c2aa2c6a5e2a832774567990d51d3562**, tree **8289b332d892931ae8131f3805354af6a0a9b3b4**, remains clean/frozen on `2026-11-19-incident-policy-selector`. All seven declared checks and the ordinary default package succeeded in one native invocation, **579.58 seconds**, with one job/core and no IFD, lock writes or keep-going.

The retained candidate is `/nix/store/92rzr8gdiw9q6mkmy29hn61qapf74v98-dev-workspace-0.2.0`, deriver `/nix/store/88hdwk0lkdrr55pr24hxggw8mz8219mq-dev-workspace-0.2.0.drv`, NAR **sha256-6w9sd77Ku92U9h0RRKye+P74UYKXe+sti39kGKCkk8s=**. Eight ordinary candidate result roots and the explicit source root are retained here through approval/resource wait. The prior 97 dependency/source roots are untouched.

## Actual outputs

All eight outputs are resident; their actual derivers and NARs were read back. Full named records are in [final-targets.json](final-targets.json).

| Target | Derivation | Output |
| --- | --- | --- |
| default package | `/nix/store/88hdwk0lkdrr55pr24hxggw8mz8219mq-dev-workspace-0.2.0.drv` | `/nix/store/92rzr8gdiw9q6mkmy29hn61qapf74v98-dev-workspace-0.2.0` |
| pi-runtime-composition | `/nix/store/b5mbn6v0q5gs1cpmykgdmnq2gvsw1ksx-workspace-pi-runtime-composition-tests.drv` | `/nix/store/mzb3avpg8i8jgvjbxqc6hghqqmpsv9bq-workspace-pi-runtime-composition-tests` |
| tracking-source | `/nix/store/snmv60h59z1wd748g10p9gyvfnqmg985-workspace-tracking-source-tests.drv` | `/nix/store/xxrmpwcg27zyg4z67cwcclg5ipkac5aj-workspace-tracking-source-tests` |
| deployment-contract | `/nix/store/gvh5pdz14mvnyy91ixq1gzvyx3ndmd8w-dev-workspace-deployment-contract-tests.drv` | `/nix/store/2mhry61afmqlgf87sqf6mgcv4xz829ki-dev-workspace-deployment-contract-tests` |
| storage-retention | `/nix/store/ri4baxmxc4r7rnzhq4n9bfbp2rkvrhwb-workspace-storage-retention-tests.drv` | `/nix/store/1dznrsir1srrhmwxdm3g1kc01mcw89c8-workspace-storage-retention-tests` |
| agent-instructions | `/nix/store/vlfp43pkqrclsvhl94skfqcdh374msxc-workspace-agent-instructions-tests.drv` | `/nix/store/439daj29vpw7b5x2a85c9qkwc2xg5lb2-workspace-agent-instructions-tests` |
| agent-team-policy | `/nix/store/car64jvyx8jgkh3gs6zgp7zziidqbas8-workspace-agent-team-policy-tests.drv` | `/nix/store/xwcq24qc6wknbvcz3lwh49d87d049r1x-workspace-agent-team-policy-tests` |
| cluster-provider-composition | `/nix/store/3czfdfqqw941mn2q15r4vxr9i1z74np2-workspace-cluster-provider-composition-tests.drv` | `/nix/store/5gczlhsglqmvilz4yzprxdvmvj20hdpx-workspace-cluster-provider-composition-tests` |

## Exact source, inputs and reused work

Actual consumed source `/nix/store/kcgi2ccwn1d65wnq9gqn6adpif419i3j-source` matches all **655 committed files**, including Git modes and symlink targets, with no unexpected files. Actual metadata locks match all **38 committed nodes**, edges and follows. The complete current graph contains 6,421 derivations. The installed extension catalog references that workspace source directly. It also binds the actual ca7 tools output; its source NAR is `sha256-6nDrTg+CTDZA4ASFU4A9fohCVtUz5ARcDPZwu7i/XM8=`. The generic caba source NAR remains `sha256-nWwhjhosx3hQZlM0xK0AQQ2Gtn8n2G1hO61Y7mlaSTE=`. Pi and all protected site/team/native/provider settings remain exact. See [source proof](consumed-source-proof.json), [artifact composition](artifact-composition-proof.json) and the saved recursive derivation graph.

Nix still labels this workspace `ecefa547c2aa2c6a5e2a832774567990d51d3562-dirty`; Git HEAD/index/worktree are clean. This marker is literal. No clean Nix metadata assertion is made, and no source/history was changed to suppress it. The exact-head artifact binding comes from the complete consumed bytes, input graph and actual derivation/output/NAR identities.

The finite fresh dry-run required **11 derivations and no fetches**, and exactly those 11 built. **76 retained dependency outputs** had identical complete recipes/inputs and matching currently resident NAR/deriver records. This includes the runtime-verification aggregator and all 14 unique shards: their old 10-file/1,740-test coverage and individual skips remain literal and were reused without execution. The overall failed fdcca batch was never transferred as a PASS. The extension's accepted 3,533-second check was not repeated. Previously absent unused archive sources were not restored merely for historical proof.

New Nix Ruby summaries are deployment contract 4 tests/19 assertions, agent instructions 10/219 and storage retention 11/88, each with zero failures/errors/skips. The ordinary package reports 22 passing Go package summaries; no per-test/skip claim is inferred. The remaining four declared shell/JSON/Node checks also produced their successful outputs. Full logs and literal summaries are retained.

The existing direct H340 deployment-contract success is bound to unchanged exact inputs and this session's own immutable H340 source. Its command was not repeated. The successor Nix deployment-contract derivation changed with workspaceSource and was actually executed successfully. No previous workspace-source-dependent check PASS was substituted for these new outputs.

## Publication and remaining boundary

A fresh canonical SSH observation saw fdcca on the target branch and default 9610. Empty-refmap scoped fetch and create-only observation refs preserved both; one normal hook-respecting push with the observed fdcca lease published ecefa. Independent SSH plus **anonymous** public commit/tree proof matched. Default stayed `9610ea74a70d4b9b9d0f2d9296ea4908c0d4725b`. One finite automatic CI inventory returned no runs or obsolete active runs; this is not CI success. No polling, dispatch, rerun or cancellation occurred.

The reviewed 13-commit history and inherited W749 deployed/unmerged lineage are unchanged. Original fdcca failure c883166a, skips, dirty metadata, Minitest environment refusal, EOF exception and old publication receipts remain literal. No new source commit or default/peer mutation was made.

The selected shared profile remained the original v31 before and after. **Live preparation/admission and activation were not run.** This package gives root a concrete retained candidate for the separately authorized shared-profile decision and fresh exact machine claim. The ordinary future `workspace-host switch --source` command, shared impact and forward-recovery limits are in [activation-boundary.md](activation-boundary.md). Owner0 remains parked; no peer release, machine claim/queue/release, profile/host/demo/runtime, registry/KB/default integration, cleanup or lifecycle action ran.

Fresh installed policy was Luna/low/full_access from v31 catalog 780db421. No utility launcher was callable in the current tool surface, so the disclosed native-parent fallback owned the single operation and every join. No previous INCOMPLETE utility was reused or relabelled. All current native effects are terminal. Heavy/check/effects and source/Git/index windows are returned **to ROOT ONLY**, clean/frozen; implementer2 retains concrete fix ownership.

[Complete receipt](receipt.json) · [Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/)
