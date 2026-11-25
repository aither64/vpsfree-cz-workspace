# Scheduler lifetime runtime audit: b361 / 41951210319

Owner: implementer3, retained Sol/xhigh/workspace-write. Session/env/roster and
current workspace verification/documentation and repository instructions were
reverified. This is a local evidence audit only; no source, Git, runtime or CI
action was performed. All read clients are terminal and C owns no process.

**Result: CI RED; the scheduler snapshot is COMPLETE and healthy at the sampled
pre-transition point.** Early enable/readback and recording now succeed. CPU127
hotplug and its cumulative health checks pass; the former scheduler warning is
not reproduced there. The example later fails on candidate insertion timeout,
with an earlier actual loader/TLB/SMP soft-lockup stack. Observer release is
separately INCOMPLETE because workload drain cannot be confirmed. This neither
qualifies the lifecycle nor establishes the fair-server hypothesis or a loader
root cause.

## Evidence and identity

Run `41951210319`, attempt 1, exact reviewed/published source
`b361b8c600bc1d50c237a68ca5413d38be9a0e99`, completed/failure at
2026-11-05 02:53:01Z. Build `126995322871` succeeds in 14m18s;
target `127000418471` fails on gh-runner4 / 2.338.0,
02:04:48Z–02:53:00Z; native is skipped. Only
`kernel/livepatch-qualification@amd-scale-aged-v5/default` runs: one script,
one test, one example; example 2627.69s, test 2743.95s, unexpected_failure.
See [raw target job](ci-scheduler-lifetime-41951210319/target-job.log),
[run](ci-scheduler-lifetime-41951210319/run.json) (`headSha`/`updatedAt` camelCase),
and [case summary](package-c-scheduler-lifetime-runtime-evidence/test.log:19).

Independently verified the sole local ZIP, artifact `13383648809`:
**1,103,445 bytes**, SHA256
`b89675e797d0179d93d7beb60506aa766ea11f437b712c4c5d2a87ee4a7535f3`.
All 16 members are unique safe relative regular files; no symlink/traversal.
The [inventory](package-c-scheduler-lifetime-runtime-evidence/safe-inventory.txt)
and selected evidence preserve original member line numbers. Only small
runner/result/identity files and bounded numbered console/shell/diagnostic
windows were saved; no whole shell, console, case or archive extraction.

The [captured identity](package-c-scheduler-lifetime-runtime-evidence/livepatch-identity.txt)
binds source b361 and lock SHA256
`604e01bde4cf21e1532e9ed6e6cfb993da28439355ad7dceb5560447827c5baa` to:

- Normal producer `/nix/store/qi47yi2g9kp89dv0h8jxwndm89vbq6az-livepatch_7-6.12.95`,
  module `lib/modules/6.12.95/extra/livepatch_7.ko`, SHA256
  `7c4da9d643d45ad9c07bde72b0180175519c5e7a15a6f2aec9e54831aee8455f`.
  The guest corrected.ko checksum command succeeds (original shell:98–102).
- Sites `/nix/store/aiqijlwh2w2wz79d6hvcqm1p9kzl4lv3-livepatch-candidate-sites`;
  extracted and guest-checked JSON SHA256
  `093cf255a38db5275b62370da8bac1297781e48e2ae3245c1c5b5e1ceeb23ed1`
  (shell:107–111). Schema 1/module digest match; ELF64 EM_X86_64 build ID
  `fd8cbfe4c314ddac8f35d87bee4bb8b909e479d5`.
- Exact released v5 SHA256
  `b31f64403d9d55f62e3d59e4bbefcbddcbda4fa66a2dc0689f9bb7cd7e927984`
  and v6 `960b13f1b461b95e29cccff58ddf0d3f3badf151046eb46eba36a9c8c7e5efe3`
  pass guest checks (shell:116–129). Active predecessor guard is 6.12.95.5.
- `/sys/kernel/notes` SHA256
  `1e4432629c0f1a1e9c6b175495217859279f98ded2beca091834ec059e42108a`
  passes (shell:4872–4876), binding the retained frozen ELF notes/type/site
  metadata. This is not an independent guest boot-image byte SHA proof.

[Machine launch record](package-c-scheduler-lifetime-runtime-evidence/machine-log.log:7):
02:07:08Z, QEMU PID **1234464**, start ticks **147659508**, direct boot,
128 CPUs/cores, one thread/socket, 16384 MiB. Actual launch paths:

- QEMU `/nix/store/kanckc6ljipqzjsrvj4aqaf87a4rhswr-qemu-host-cpu-only-for-vm-tests-10.2.4/bin/qemu-kvm`
- Kernel `/nix/store/050sh2hfrnpc8j5abr2npp7bnlxvpb8a-linux-6.12.95-frozen-boot/bzImage`
- Initrd `/nix/store/h3v4nwmsn39wph7apj7q6bg8hn58rv3x-initrd/initrd`
- System `/nix/store/hxkzvnc6awzsmb7d6q9c6w1bvq50c8c9-vpsadminos-system-vpsadminos-26.05.git.b361b8c`
- Squashfs `/nix/store/nsbnshk5qfs7c1vrjmdkqba9hd5c23fd-squashfs.img`

The diagnostic profile is 300s / 100000 tasks, not final four-hour policy.
Recorded ages under v5 are 116.392, 217.798 and **319.705s**. Primary feature
645927/original14400 is outside this diagnostic result.

## Successful preparation, capture and health

[Numbered shell excerpts](package-c-scheduler-lifetime-runtime-evidence/shell-phase-excerpts.txt)
show exclusive absence, exact native NF3/name/U-u-excluding lookup, notes guard,
CPU127 mask, `rq_cpu == 127` filter, 64-KiB private buffer, mono clock and
no-overwrite configuration. Native base is `0xffffffff842ed060`; registered
address is **0xffffffff842ed123**, the retained validated CALL at +0xc3.
The frozen 493-byte ELF bound and five-byte call/type proof remain as recorded
in [preparation](package-c-scheduler-hotplug-preparation.md); displayed span
is presentation only.

At **02:08:36Z**, nop/OFF checks, event enable write/readback and final OFF/nop
readbacks all return status 0 (shell:4935–5056). The first state setup follows
at :5061; stress starts at :5178 and population at 02:09:53Z (:5416).
Thus preparation precedes workload creation. No prior 13b enable-timeout
recurrence is present.

Recording ON/readback succeeds at **02:17:41Z** (:8529–8542); CPU127 offline
succeeds at 02:17:44–50Z (:8957–8961), followed by its online sequence and
original progress/health helpers. Both cumulative dmesg checks and the fork/
exec and sleep helpers return status 0 (:9083–9123). Runner explicitly reports
pre-transition hotplug complete. Recording OFF/readback and trace reads succeed
at 02:18:51–53Z (:9142–9171).

[Actual runner record](package-c-scheduler-lifetime-runtime-evidence/test-runner.log:44):

```text
migration/127-789 [127] d.Z1. 604.432532: scheduler_dying:
(sched_cpu_dying+0xc3/0x1f0)
server=0xffff95886fdf0fa8 rq=0xffff95886fdf0640
entity_rq=0xffff95886fdf0640 parent_color=0xffff95886fdf0fa8
nr_running=1 nr_pinned=0
cfs_nr=0 cfs_queued=0 cfs_runnable=0 cfs_delayed=0
rt_nr=0 dl_nr=0 rq_cpu=127 rq_online=0 flags=0xf1
```

Independent [field decoding](package-c-scheduler-lifetime-runtime-evidence/field-decoding.json)
using retained pinned a238/BTF semantics confirms RDI server minus RBX rq is
`0x968`, entity->rq equals rq, and all pointers are nonzero. Entity rb_node is
at offset 0; raw parent/color equals its own node address, so RB_EMPTY_NODE is
true and **on_dl_rq is false** (`deadline.c:87–90`, `rbtree.h:33–36`). Flags
0xf1 decode throttled=1, server=1, active=1, defer=1, armed=1, running=0 from
the recorded 32-bit container/bit offsets. Active alone is not queue membership.
CPU/header/site/relationships and every required class/pinned field are present;
there is no faulted-pointer substitute. `/0x1f0` is now actually observed and
accepted only as well-formed hexadecimal presentation.

Trace entries/written **1/1**, profile **1 hit / 0 misses**, overrun=0,
commit-overrun=0, dropped-events=0, bytes=96, read-events=0; oldest mono
604.432532, now 669.018507 (runner:34,47–55). The later pre-cleanup snapshot
retains this record. These are complete loss-free observations of one healthy
pre-dequeue instant, not evidence of the old uncaptured warning state or a
successful full lifecycle.

## Later primary failure and actual kernel evidence

Host logs below originally use +0100; this table is UTC. The unchanged
activation helper shares one **1800s cumulative budget**, not 1800s per attempt.

| Operation | UTC window | Recorded result / original shell lines |
| --- | --- | --- |
| Activation 1 | 02:20:01–02:31:04 | 663.09s, status 1 / EBUSY; 10156–10164 |
| Activation 2 | 02:31:14–02:34:05 | 170.91s, status 1 / EBUSY; 10332–10340 |
| Activation 3 | 02:34:13–02:49:56 | 942.5s, status -1, empty output; 10514–10531 |
| Failed-transition diagnostic | 02:49:56–02:52:09 | 132.91s, status 0; shell1:3–10 |
| Example failure | 02:52:09 | original insmod timeout retained; runner:4–9 |

[Activation evidence](package-c-scheduler-lifetime-runtime-evidence/activation-attempt-context.txt)
records protocol-timeout phase `replies_consumed` and a reply buffer ending
`:124`; it does not prove the guest insmod syscall returned. The command's
elapsed value is not a separate precise measurement of the remaining host
budget/reserve. Generic runner exception/evaluation failure are secondary.

The earliest selected kernel fault is **guest uptime 765.904211**, console:167,
under **6.12.95.5**, CPU114 / `insmod:142433`: watchdog soft lockup, RIP
`smp_call_function_many_cond+0x110/0x4c0`. Its actual chain is
`on_each_cpu_cond_mask -> flush_tlb_kernel_range -> __purge_vmap_area_lazy ->
_vm_unmap_aliases -> change_page_attr_set_clr -> set_memory_rox ->
module_enable_text_rox -> load_module -> finit_module`.
[First fault window](package-c-scheduler-lifetime-runtime-evidence/console-first-fault.txt)
preserves registers and console:163–261. At :211 it requests NMI from CPU114
to 0–113,115–127; RCU stall and selected responding CPU stacks follow.
This is later activation/loader liveness evidence, not the original CPU127
scheduler warning or a new observation setup/decoder failure.

PID attribution has a bounded basis: the callback trace read immediately after
first EBUSY (:10165–10271) contains `insmod-142433` only; the corresponding
second-attempt trace (:10341–10453) contains `insmod-147541` only. This
associates the soft-lockup PID with the first returned-rejected attempt.
The shell start blocks themselves do not log PID; **third-attempt PID is
unknown**. Do not assign the soft-lockup PID directly to the timed-out third
command. The selected all-CPU NMI context identifies a kernel-range-flush wait
path but no target-correlated CSD enqueue/entry/exit progress. RDX=0x26 is not
accepted as proof of a particular target CPU. Later D-task stacks are separate
snapshots, not the missing CSD progress proof.

[Console progress](package-c-scheduler-lifetime-runtime-evidence/console-livepatch-index.txt)
shows first ip_set and then nf_tables pre-patch rejections with unpatching
complete, followed by a third enabling at mono1700.607512, transition start
1877.395831 and patching complete **2529.197143**. Later diagnostics show
`enabled=1, transition=0` and uname **6.12.95.7**. The task scan reports all
101293 read/undefined(-1), coverage_complete=1, pending=0. These later facts do
not make the insertion deadline pass, erase the kernel fault or establish all
normal callback/migration assertions. Host wall, guest printk uptime and trace
mono are distinct clocks; no shared calibration/vCPU mapping/runqueue deltas
were captured, so exact wall time of the console completion is unproven.

## Failure recovery, release and completion scope

[Recovery/drain evidence](package-c-scheduler-lifetime-runtime-evidence/order-and-recovery-status.txt)
shows the existing recovery batch completes **status 0** at 02:52:30Z
(shell1:17447–17502), including existing stop/release/CPU/probe operations.
The following single read-only postcondition command returns **status 1**
(:17507–17514): `/run/livepatch-qualification/exit` does not exist. Later
conjuncts short-circuit, so population stopped/tasks=1, sctp/tun exit and stress
stop/pid absence are **unconfirmed**, not measured false or zero. Stop requests
are not proof of successful population/stress drain.

The pre-cleanup ownership snapshot is owned instance/event, armed, recording
OFF, prepared, release_attempted=false/released=false (runner:58). Recording
OFF is also acknowledged by actual readbacks. The scheduler observer's
**destructive disarm/delete/removal is skipped** for unconfirmed drain; its
incomplete message is a follow-on safety outcome, preserving the primary
insmod timeout. No event removal or eventual in-kernel disarm is inferred from
the Ruby flags. Normal late release was not exercised, and normal post-transition
hotplug, migration, disable/recovery and final health acceptance were not reached.

Native VM stop starts 02:52:39Z; QEMU exits status 0 at 02:52:51Z, kill action
uses SIGNAL NONE and destroy completes. [Console teardown](package-c-scheduler-lifetime-runtime-evidence/console-teardown.txt)
shows ordinary runit shutdown/KILL-all/powerdown. This confirms failed-VM
teardown, not successful in-guest observer release or qualification.

## Limits and minimum next ownership

The lifetime remedy now has real early-enable/record/read/healthy-hotplug
acceptance; safe late removal remains untested. The current activation is RED
with an actual loader/TLB/SMP stall signature and eventual kernel transition.
It is analogous in subsystem to old 5235's loader fault, but no common cause,
whole-input equality or historical scheduler explanation is established.

Minimum next package is architect-owned pinned loader/TLB/SMP interpretation
using this timeline and retained stacks, followed by a lead/user decision.
Missing incident facts are target/function-associated CSD progress and aligned
host QEMU-vCPU scheduling facts, not another post-recovery memory dump. Existing
later-migration CSD facilities were not reached for this loader interval. No
new diagnostic implementation, retry, timeout increase, scheduler write, health
waiver, production correction or four-hour escalation is authorized here.
Prior 13b setup-INCOMPLETE, bda1 scheduler-warning and old5235 loader evidence
remain distinct; [preparation/history](package-c-scheduler-hotplug-preparation.md)
and the original 44/20 host controls retain their actual scopes.
