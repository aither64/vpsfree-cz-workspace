# Profile activation verification

Package I, implementer1. Passive verification window
`2026-11-25T15:43:45Z`–`15:45:23Z`. Session/environment identity matched the exact
bound slug/workspace. Root reports all four E targets passed and utility effects
closed. No deployment watcher was started: root's existing activation was already
terminal and its tool session73258 joined before this package ran.

## Activation and effect accounting

Root ran ordinary `workspace-host switch --source
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-25-archive-failure-investigation/workspace`
at exact source `30b74dc3278728ab36197e0d2ef2cf76c66cf791`, with its exact session
and held machine claim `51ed48c0-8052-4e9b-ad36-399562a20020` environment.

`/tmp/archive-failure-profile-run-51ed48c0/result.json` records exitStatus0,
start `2026-11-25T15:38:21.822536Z`, finish `15:41:04.276579Z`, duration162.454s.
Driver164111 and command164393 are absent. Root joined original tool73258 exit0;
I did not repeat, resume, interrupt or otherwise control either process.

Switch log confirms compatible Codex0.165.0, native App Server and local semantic
observation contracts, and final packageapja. Temporary contract probes emitted
PATH-alias warnings but completed compatibly. Existing auto-archive/tracking-sync
timer links were reinstalled by ordinary activation; no lifecycle/goal/team action
was requested or inferred from that implementation behavior.

| Evidence | SHA-256 |
| --- | --- |
| `.../result.json` | `2e1424380f1c66ce9ecfc646928d75df73824104eb76c9c97a0688b58a36a118` |
| `.../switch.log` | `b4e48799fbf71f29b337e96c354300f30c990d0c9081e571fc8c0b5235ce0d60` |
| `/tmp/archive-failure-i-source-proof.json` | `8f23f01f191cfdeebeaea447bf549d86018605802c5649272cc018f73a9fa338` |
| `/tmp/archive-failure-i-health.json` | `d58e291af41dbacff9ec5d8ccee0d574fee71d0f53021fcfbf8b5afcc52e90c3` |

## Exact selected artifact and unchanged host

- Selected user profile resolves to
  `/nix/store/apjaqip0xj9cy297z2wmb8hmfqn2c8x1-dev-workspace-0.2.0`.
  Actual deriver is
  `/nix/store/m9pdsbnrrlwkyhp87d3cic5am7c10rbs-dev-workspace-0.2.0.drv`.
- Deriver runtime source is `/nix/store/hh81k6nk1r1x0jhi0v8a1l9d53jr0h4n-source`.
  Its composed workspace source `/nix/store/cv964n61y041iyi3gp4nb76rgjhnx2nc-source`
  full lock graph equals frozen G's final workspace lock, selecting exact runtime
  `f6d60bf87002fb1896599f35f0284743c16d7e6f`, NAR
  `sha256-JZJQaci1y3dGVSQwHbdHS8X0IDFpyrz+dk3rqntZJOE=`.
- Complete actual derivation input-map SHA-256
  `b8498333b3bf949119400d9f808d9150ec6b146af4cd32f1ddfa0f641d728b62`
  matches accepted G equivalence proof. No tree-only verification reuse.
- Actual runtime-contract bytes match that source, SHA-256
  `aa915624b9627cde1e0dc296d0a90247e7e63164e565aa4018d83509fede6e05`.
  Package metadata SHA-256 remains
  `d39df2dc4f9d2318ec381f5065ef36aa932c7d1e13c0d5850de74fc80c533a9e`.
  Machine policy retains exact configured repository/aitherdev profile identity
  and legacy bridge; extension, sibling/follows/native/site contracts match G.
- `/run/current-system` and `/nix/var/nix/profiles/system` both remain
  `/nix/store/k79k3l35lnhfikw65zwnacag112w7z9p-nixos-system-aitherdev-26.05.20261121.94c3211`.
  This is profile-only activation; no new configuration system derivation is
  claimed deployed. Accepted F helper/service bridge remains applicable.

## Passive health and continuity

`workspace-host status`, profile/system link reads, `nix-store -q --deriver`,
`nix derivation show`, service/proc reads and bounded local-socket HTTP reads passed.
No package build/test or mutable operation was launched by I.

| Surface | Observed result |
| --- | --- |
| Portal | active/running PID270751; actual executable is selectedapja `bin/workspace-portal` |
| Router | active/running PID270469; actual executable is selectedapja `bin/workspace-portal` |
| Coordinator | active/running PID270787 |
| Native Codex | active/running PID3138515, startTicks180371132; exact unchanged `/nix/store/2rqwqchjlv6l2nw5l491pkhvrsijn50c-codex-package-0.165.0/libexec/codex/bin/codex` |
| Native invocation | argv SHA-256 `f27189d336add4e49fb7be8c8aa7bcddbe38a030c231d9615d0fcd09a426ba0b`; retained registration digest `212f2a9e4950ed5f3c5e0aa8a00d28fccf2aa1715503bc850bdc529fdaa00cdc` |
| Naming | new portal-owned child PID271379, parent270751, exact same pinned native executable; owned `naming-994239765/app.sock` resolves to an existing native socket |
| HTTP | healthz, this session page and this session details each200/exit0 |
| Conversation | currentTarget remains active/unarchived exact slug and root thread `01a21312-83d3-7280-a1fa-b9bad876e68e`; pendingLifecycle empty, interactive=true, recovery active/executionHeld=false |
| tmux | own retained session exists, session ID `$125`, created epoch1795616312; socket remains available |

Native registration preserves its original older packagegh680/policy1/capacity0
launch provenance and the same argv/storage tuple. Selection did not relaunch
native Codex; PID/start/executable and original registration remain intact. The
actual stable switch accepted this compatibility path. The details response also
has empty conversationScope and conversationInteractive=false for this Codex
metadata view; no universal sending assertion is inferred from that field.

HTTP commands used the local portal socket, ten-second per-read limits and only
GET routes already listed in rollout. Native and naming checks inspected existing
processes/sockets; tmux used list-sessions filtered to this exact session. No
naming inference, conversation prompt/send, creation, provider change, archive,
revive, stop, recovery or cleanup was attempted. This active retained member turn
and root thread identity provide continuity evidence; they do not replace a
separately authorized functional naming/send/archive action.

## Remaining authority boundary

Passive profile/source/host/native/service/session verification passes with the
limits above. Root owns current claim status, final freshness/effect reconciliation,
approval and release. Machine remains held pending separately approved complete
deployed-lineage integration; I neither merges nor releases it. No merge approval
was present at this package's handoff. Source-owned failure/recovery would return
to root; no retry or repair is authorized here.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-25-archive-failure-investigation/
