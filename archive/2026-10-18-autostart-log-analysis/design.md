# node1.stg osctld autostart fix: accepted design

Implementation authorized on 2026-10-18 by the user's "Implement the plan",
after narrowing the request to the osctld error. The deliverable is a reviewed,
tested, published feature branch ready for deployment. Merging, deployment,
node recovery and reboot are not authorized in this pass. **Kernel, swap,
swap-service and histfile changes are deferred.** The independent-fault findings
below are retained investigation evidence, not implementation assignments.

Architect0 owns this design; implementer0 owns the helper and unit regression,
and implementer1 owns the focused VM regression. The lead owns coordination,
acceptance, tracking and review. The original investigation was read-only;
no recovery was performed. Implementation/check status belongs in `state.md`.

## Baseline and scope

Use vpsAdminOS `origin/staging`, last verified at
`d531fc90888e3eabf17889b0dff94c648866cea4`, after the lead fetches/revalidates it.
`origin/HEAD` selects staging; stale `origin/master` and the bare repository's
local HEAD are not implementation bases. Deployed `eb5c39c` is an ancestor,
and the relevant helper/start files are unchanged at the verified staging ref.
Route a changed relevant baseline through the lead before adapting this brief.

Production edits are confined to `osctld/lib/osctld/switch_user.rb` and any
strictly necessary osctld packaging metadata. Existing kernel selection and
kernel derivation must remain unchanged. Do not modify `AutoStart::Plan`,
`commands/container/start.rb`, executor retries, configured process limits or
autostart state. If a focused regression exposes a required caller correction,
report the evidence and obtain the lead's design decision before expanding.

## Findings and evidence boundary

The immediate autostart failure is **child EMFILE while closing inherited file
descriptors**, followed by **parent EOF reading the missing wrapper PID**.
There were 48 queued starts, 25 RUNNING/success records and 23 matching child
EMFILE/parent EOF failures. This is partial autostart failure, not failed pool
import or a daemon crash. There is no evidence establishing a daemon FD leak.

All timestamps below are 2026-10-18 CEST (+02:00), matching Europe/Amsterdam.
The log server reported `10:28:02+02:00`; runit embeds UTC `08:xx` timestamps.
The requested 10:15 reboot started shutdown at 10:15:32; new boot messages
arrived at 10:21:08. Shutdown errors must not be attributed to the new boot.

Evidence files in this directory:

| File | Coverage and limit |
| --- | --- |
| `node1-host-since-1014.log` | 10:14–10:21:45; hit the 10,000-line cap, supplemented below |
| `node1-host-since-102109.log` | 10:21:09–10:29:14; 12,560 lines, below 20,000 cap |
| `node1-runit-since-1014.log` | 10:14–10:28:15; 954 lines, below 15,000 cap |

Remote sources: `/var/log/remote/cz.vpsfree/nodes/stg/node1/log` and
`/var/log/remote/localhost/log` on `log.int.prg.vpsfree.cz`. The second contains
node-tagged runit output. The host extraction excludes container-kernel noise.
Counts describe this capture, not current live container state. Architect SSH
was blocked by the tool sandbox; lead SSH to the log server succeeded. Direct
read-only SSH to node1 was denied, so current FD counts, limits and swap state
were not inspected.

Deployed OS source: `eb5c39c0789401117c48cd124e47b7a401fb91b6`, identified by the
boot command line. Relevant autostart files also match the explicitly verified
`origin/staging` revision above; the former local HEAD `0081fc01` is not a base.
Deployed Linux source: `11058eb4fe1cba30653e8e643546c13bc8bcd792` (6.12.113).
Its relevant source is retained as `deployed-swap_cgroup.c` and
`deployed-page_alloc.c`. Exact deployed configuration revision is unverified.

## Autostart failure and accepted fix

Timestamped excerpts (host follow-up file unless otherwise noted):

```text
10:15:32.081795 Received command 'self_shutdown' [first host file:615]
10:21:08.349682 Linux version 6.12.113 [first host file:5817]
10:22:07.275824 [tank:auto-start] Auto-starting containers, 8 containers at a time [5564]
10:22:07.300020 [tank:auto-start] 48 containers to start [5565]
10:22:07.353479 [pool=tank] Pool imported in 40.21 seconds [5674]
10:22:53.239004 Dir.open: Too many open files @ dir_initialize - /proc/self/fd (Errno::EMFILE) [8531]
10:22:53.282220 [cont] Exception raised during command execution: end of file reached [8556]
10:23:07.051955 [cont] Exception raised during command execution: end of file reached [10112]
```

The child stack is `SwitchUser.walk_fds:221` → `close_fds:199` → `fork:35` →
`fork_and_switch_to:62` → `Commands::Container::Start#start_now:181`.
The parent fails at `start.rb:208`, reading the wrapper PID. This is before
the child switches identity, creates a syslog namespace or launches LXC.
The generic executor catches the exception and discards that work item;
the five-attempt autostart loop retries returned error statuses, not this
exception. No retry/exhaustion records accompany these 23 failures.

**Source-supported cause:** `switch_user.rb:93` lets the parent apply the
container's process limits while the child is still closing inherited FDs.
The child first scans/disarms Ruby IO owners, then opens `/proc/self/fd`.
The existing parent-to-child `ready` signal is read only *after* that cleanup
and does not order the limit change. The daemon sets NOFILE to 131072
(`daemon.rb:129`); default container soft NOFILE is 1024
(`prlimits/manager.rb:24–27`). Lowering the child's limit before cleanup can
make opening the directory fail. Actual live limits and inherited FD counts
are unknown, so the race is strongly supported by source, not reproduced or
runtime-proven here. EMFILE itself and its downstream EOF are confirmed.

Add a child-to-parent preparation acknowledgement in
`SwitchUser.fork_and_switch_to`, after inherited descriptor cleanup and the
existing child setup, immediately before the child's existing ready wait.
The parent must receive the valid acknowledgement before `apply_prlimits`,
then send the existing ready release. The workload block runs only after
successful limit application and release. This is a private helper protocol;
keep the helper's public method signature, successful PID return and caller
ownership of that PID unchanged.

Retain the acknowledgement descriptor through `close_fds`, close each pipe
end in its owning process, and close all helper-owned endpoints on every
error path, including pipe/fork/setup failure. Missing/invalid acknowledgement,
failed limit application and failed release must free the peer from its wait.
Before successful handoff, failure cleanup must reap only this helper PID;
terminate it if required to avoid an unbounded wait. Do not call a generic
wait/reap, kill unrelated children, or hide the initiating exception behind a
cleanup exception. After successful handoff, the existing caller remains
responsible for reaping. Child exit/setup failure must be detectable by the
parent, and parent failure must not permit workload execution.

Preserve retained FDs, Ruby IO owner invalidation, duplex-pipe handling and
IO-GC safety. Never shut down an inherited socket in a way that affects the
parent or flush inherited buffered writes into the parent's pipes. Keep
privilege, cgroup and namespace behavior; do not raise configured limits.

Broader caller error reporting, Eventd cleanup and retry redesign considered
in the initial investigation are deferred. They are not part of this fast
fix unless the lead approves a concrete required correctness deviation.

IDs with an autostart attempt but no RUNNING or success marker in this capture:

```text
101 1274 10796 11352 11644 12196 13592 13707 13764 14118 14241
14722 14877 20158 25511 25994 26244 26427 27276 27593 28557 29028 29043
```

The IDs are a set difference because generic EOF messages omit CT IDs.
`started-cts.txt` is volatile under `/run/osctl/pools/tank/auto-start`; it can
be marked by `ct_pre_start`, not only full boot success. These particular
failures precede that hook. Do not delete autostart state as a repair.

## Deferred independent boot findings (not implementation scope)

| Fault and evidence | Proposed correction |
| --- | --- |
| Swap activation: 10:21:09.918 kernel warning in `__alloc_pages_noprof`, order `0xb`; stack `swap_cgroup_swapon`; `couldn't allocate enough memory for swap_cgroup` (first host file:8475–8525). At 10:21:09.929 both `/dev/sda` and `/dev/sdb` swapon report `Cannot allocate memory` (runit:145–146). | Exact deployed `mm/swap_cgroup.c:211` uses `bitmap_zalloc(max_pages, GFP_KERNEL)` for the proactive bitmap. The contiguous allocation reaches order 11 (8 MiB with 4 KiB pages); deployed `mm/page_alloc.c:4818–4823` rejects orders above `MAX_PAGE_ORDER`. Use `kvcalloc(BITS_TO_LONGS(max_pages), sizeof(*proactive_map), GFP_KERNEL)` and replace **both** matching bitmap frees with `kvfree`, or an equivalent consistently paired virtual allocation. This is an allocation-size defect, not evidence of physical RAM shortage. |
| Swap service falsely reports success immediately afterward (runit:147–148). | `os/modules/config/swap.nix` calls bare `swapon`; the oneshot wrapper continues to success. Propagate failure explicitly, e.g. `swapon ... || fail ...`. Do not introduce global shell `set -e` behavior changes. Verify `/proc/swaps`, not just the service done marker. |
| `histfile-tank ./run: line 8: getent: command not found`, 10:21:09.571 through 10:21:15.253 (runit:137,164,168,170,172,217); then `Restoring /.bash_history from /tank/.bash_history` and `Monitoring /.bash_history` (218–219). | In `os/modules/programs/bash.nix` pool history service, supply `pkgs.getent` in PATH or use its absolute store path. Validate account lookup success and a nonempty absolute HOME before constructing the history path. Preserve both `/.bash_history` and root's actual history when reconciling recovery; do not overwrite one blindly. |

The swap fix does not require `swapaccount=0`, repartitioning or changing the
on-disk swap format. Those workarounds are not recommended by this analysis.
History and swap faults are independent of the EMFILE autostart failure.

Early `tank` missing, osctld socket ENOENT and initial RabbitMQ connectivity
messages recover during startup; pool import/hooks completed. Other observed
warnings (NixOS hostname application, NFS recovery tracking, IRQ affinity,
Munin plugin access/parsing, missing local tracing receiver) are not evidence
for the autostart cause. Their specific effects need separate confirmation;
this brief does not claim every host warning is resolved. The nodectld parser
error at 10:20:17 belongs to shutdown before the new boot.

## Accepted implementation packages

| Owner | Independent files and responsibility | Acceptance |
| --- | --- | --- |
| implementer0 | `osctld/lib/osctld/switch_user.rb`, `osctld/spec/osctld/switch_user_spec.rb` and directly relevant existing helper specs; necessary final osctld gem metadata | Child preparation precedes target limits, which precede workload execution. Failed handshakes close owned pipes, release the peer and reap only the failed helper. Existing FD/socket/duplex/IO-GC invariants pass. |
| implementer1 | One focused VM regression under `tests/suite/`, plus its `tests/all-tests.nix` registration | Exercise the actual packaged helper with more than 1024 inherited FDs and soft NOFILE 1024, then normal parallel autostart of a small pair of test containers. Check RUNNING, console/exec and clean stop without EMFILE/EOF. |

The VM test depends on package A's agreed helper behavior and final packaged
osctld source; its authoring can proceed independently. Use the same unchanged
cached kernel derivation. The lead serializes all shared repository staging,
commits, rebases and publication; only owned paths are staged. Implementer1
owns test registration, implementer0 the final gem metadata refresh if required.
Neither implementer duplicates the other's edits. Route material deviations
through the lead and architect before changing the scope.

## Verification and completion order

1. Implement a deterministic unit regression that holds the child before FD
   cleanup with more than 1024 inherited descriptors. The old ordering must
   demonstrably permit premature lowering; the fixed parent cannot apply
   soft NOFILE 1024 until preparation acknowledgement. Confirm the workload
   receives the configured limits. Do not rely on probabilistic stress alone.
2. Test child setup failure before acknowledgement, invalid/closed handshake,
   parent limit-application failure and failed release: no workload on failed
   preparation, no pipe/FD leak, no zombie or unbounded wait, no reaping of an
   unrelated child. Rerun existing FD ownership/socket/duplex/IO-GC specs.
3. Run focused RSpec, Ruby lint, Nix formatting/evaluation for the new VM test
   and declared hooks in the repository environment. Commit all intended code,
   tests and required final packaging metadata; consolidate caused follow-ups.
4. Run mandatory independent final review on exact committed heads after quick
   checks pass. Include complete base-to-head history, final diff, no-migration
   conclusion and an explicit check that deferred files/kernel pins did not
   change. Review precedes long integration execution.
5. Launch one focused VM check through a fresh prescribed verification watcher.
   Prove it uses the new packaged osctld and unchanged cached kernel. Exercise
   the real fork/prlimit helper and the small normal-container smoke path above.
   Stop and investigate any unexpected kernel build; it is outside this scope.
   Fixes require affected quick checks and independent review before long retest.
6. Publish the exact reviewed/tested feature branch under normal SSH/hook policy,
   and provide its SHA, review, quick-check and VM results. No default-branch
   integration, deployment or node recovery follows automatically. The session
   remains open; current status and any remaining limits belong in `state.md`.

## Compatibility and future rollout (not executed or authorized here)

Only a private parent/child protocol within one daemon changes. No database,
migration, persistent-state, API, CLI, generated-client, Terraform or inter-node
protocol change is required. Existing caller method/PID contracts and process
limits remain intact. Mixed old/new nodes are supported; there is no fleet-wide
update requirement. Rollback can read existing state but restores the race.
No kernel change or host reboot is needed for this osctld fix.

A later separately authorized rollout should select node1.stg explicitly,
record current intended-running/stopped containers and active queue, update
osctld through the supported service/package procedure, and verify daemon
health. Retry only confirmed intended-running stopped containers, for example
`osctl --pool tank ct start --wait 120 29028`, then verify RUNNING and absence
of EMFILE/EOF. The ID list above is historical evidence, not a current restart
list. Avoid force pool trigger, blanket restarts, autostart-state deletion or
changing container limits as substitutes for this correction. No swap/history
recovery is included in that checklist.
