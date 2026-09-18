# NFS cancellation implementation review packet

Initiative: 2026-09-12-nfs-cancellation. Read plan.md and state.md beside this file.
Root workspace: /home/aither/workspace/ai/vpsfree.cz. All worktrees: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-nfs-cancellation/.
Follow repository AGENTS.md and mandatory-change-review SKILL.md. Review committed
changes directly, including history; do not change code or spawn nested agents.
Write findings into implementation-review-<lane>.md beside this packet and return
them to the coordinator. Severity: Blocking / Important / Advisory with evidence.

## Requested outcome and acceptance

User requested repair after reviewing NFS cancellation failures. Userspace must
work on kernels lacking cancellation. Requested kill must proceed even when NFS
cancellation/freezing fails; most workloads do not use NFS. Original namespace
identity and terminal cancellation must survive osctld restart, including init
exit or namespace departure. Bound forced stopping without falsely reporting a
live container stopped or deleting live ephemeral data. Preserve graceful timeout.

User explicitly requires fixing the existing 6.12.95 kernel, no extra entry.
Cancellation is base-kernel code. Rebuild existing matching nfs-cancel livepatch
against repaired base, preserve exact image/note guards and historical fixtures.
Port repaired full cancellation and prerequisites to default 6.12.109.

## Revisions (all intended changes committed)

| Worktree | Base | Head |
| --- | --- | --- |
| vpsadminos | 15802517e2d92dda4ddc07ebac3d1d7ea087b430 | 75e1d26df4acaea85f20c3ce2ac6ec6046fc1d5d |
| linux-6-12-95 | 563bbb35e8753e1bb34dad19ebeec8962ee3c1cd | fbe36622894dbc46f82e970dcae5da18d6e58c8c |
| linux | 9ccd5d6597a6ddbe5b44fb885ddf96e4dbc332dd | fb4ad1506c1d22ab92251b3ba167ca951d453b8e |

Linux git operations may take minutes due to shared partial clone's many packs;
prefer worktree source and saved scratch/linux-default-final.patch if necessary.
Do not manipulate shared Git object storage. OS worktree's untracked .native is
build output, not intended code. Kernel feature branches pushed; OS unpushed.

## Commit split

OS d7113acc7: userspace state/pins, async cancellation, common bounded forced-stop
orchestration, native regressions and behavior docs. Bundled because persistence,
worker lifetime and the stop deadline define one teardown contract: sharing the
forced-stop context across DistConfig, command and control avoids independent
fallbacks reapplying full budgets or skipping a kill. New classes own state and
forced-stop respectively; no API or gem dependency change.
OS ec7adfa81: kernel pins, repair/livepatch docs and explicit identity fixture.
OS 75e1d26df: VM regressions and diagnostic kernel CI/cache outputs needed by them.
Retained Linux: one lifetime repair. Default Linux: repaired full cancellation
port including its required locked NLM helper (not replay of stable history).

## Contract owners and consumers

Linux owns shutdown_tree sysfs ABI, sticky task admission/cancellation, namespace
descendant isolation, NFS sysfs lifecycle and exact module ABI. osctld is the
current shutdown_tree consumer (container/nfs_cancellation.rb). vpsadminos kernel
registry pins source archives and selects the exact nfs-cancel cumulative patch;
livepatch loader/identity module consume image and note guards. Historical
6.12.95 boot-base fixture remains a238 and selects legacy module intentionally.

osctld owns run identity, sidecar schema and pins under /run/osctl/nfs-cancellation.
RunConfiguration constructs it before monitoring; authenticated pre-mount hook
captures original namespace roots; monitor handles exiting init; forced stop
requests cancellation; run destruction retires state. DistConfig distributions,
ContainerControl stop/state, and command-level recovery share one forced-stop
budget. Existing Recovery is still also used by explicit state recovery command.
osctl/vpsAdmin consumers keep existing stop API/options. No external runner DSL,
API format, run config format, database, gem or flake-input protocol changes.
Diagnostic outputs use same registry source/config path as test machines, and the
kernel builder publishes those outputs. Existing CI discovers new test instances.

## Chosen boundaries and compatibility

- No legacy per-filesystem/per-netns cancellation fallback. Probe only tree control
  and re-probe after module loading. Unsupported runs still kill normally.
- Original authenticated user/net bind pins, boot+RunId sidecar, atomic metadata,
  namespace/type/ownership checks. Old unprovable runs do not adopt descendants;
  ordinary killing is supported with cancellation unavailable until next start.
- Cancellation headstart max 5s, worker total 30s, forced phase total 60s including
  fallback/recovery/verification. Recover immediately on LXC failure or by 50s.
  No freezer barrier, best-effort thaw. Avoid blocking worker reap/monitor waits.
- Userspace may roll out independently and before reboot. Repaired base kernels
  require incremental reboot, no coordinated fleet update. Older daemon ignores
  sidecar; rollback loses guarantees and pins can persist until cleanup/reboot.
- No production deploy, default-branch integration, new kernel entry/variant,
  livepatch delivery of base cancellation, or session cleanup authorized.

## Quick evidence and outstanding runtime coverage

213 focused native examples pass; eight daemon examples pass. RuboCop 23 changed
files clean, OS Overcommit hooks pass. C helpers compile -Wall -Wextra -Werror;
Nix-rendered diagnostic/legacy Ruby scripts parse. All seven intended test configs
and selected kernel derivations evaluate. Retained checkpatch clean; default
MAINTAINERS warning addressed. Existing cumulative patch inputs apply sequentially
to repaired 95 source, historical boot fixture unchanged. See state for commands.

No repaired kernel build or integration VM has run. Diagnostic test currently
stresses post-publication initialization failure, concurrent sysfs writes and
mount/unmount under KASAN/lockdep/delayed kobject release. Actual NFSv4 migration/
transport replacement runtime coverage is still missing. Review source paths and
coverage; do not assume native mocks prove real bind mounts or namespace behavior.

Overall risk classification: high because host-kernel behavior, tenant isolation,
persistent runtime state and mixed-version/ABI concerns apply. All four review
lanes selected with gpt-5.6-sol at xhigh as required. This is review classification,
not an approval request or a reason to defer the user's authorized implementation.
