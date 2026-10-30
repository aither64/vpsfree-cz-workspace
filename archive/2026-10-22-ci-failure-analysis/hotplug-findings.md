# AMD aged-scale CPU-hotplug findings

Lane 2, implementer2. Investigation only; ready for lead reconciliation.

The test found a real scheduler teardown invariant warning during the **first
CPU127 offline under the exact v6 predecessor**, before incoming v7 insertion.
Successful offline and later activation are compatible with that warning; they
do not establish kernel health. The warning's trigger remains unresolved.
Keep this qualification envelope and its no-fault requirement; revise phase
checks and capture the missing scheduler state before selecting a kernel fix.

## What is established

Current evidence is the retained artifact from
[run 39767770407, job 119793311395](https://github.com/vpsfreecz/vpsadminos/actions/runs/39767770407/job/119793311395).
No remote observation of that run was made here. In the citations below,
`C`, `S`, `R`, and `D` mean its `machine-console.log`, `machine-shell.log`,
`test-runner.log`, and `machine-failure-diagnostics.log` in the retained case
`os-test-kernel__livepatch-qualification__amd-scale-aged-v6-0921d60d`.
[Numbered extracts](evidence/hotplug/observations.txt) preserve original paths
and line numbers; [manifest](evidence/hotplug/manifest.json) records file hashes
and exact source blobs. Times in this table are CEST (UTC+02:00).

| Phase | Observation and citation | Interpretation |
| --- | --- | --- |
| Current OS boot | `D:81,542` names current `846bb46` system; `D:3425` records GCC 15.2.0/binutils 2.46 and Linux 6.12.95. | This is current OS with a frozen kernel, not an older OS activated later. |
| Predecessor | `S:117-121` checks v6 SHA-256 with status 0; `S:4745-4752` inserts it; `C:136-144` shows enabled and patching complete. | Exact v6 fixture executes before aging/hotplug. |
| Four-hour aging | `R:251` reports `age=14404.00232966704`, 100000 tasks, 128 CPUs. | Required predecessor age is reached. |
| First offline | `S:98134-98168`: offline 17:24:42–51, status 0; readback offline 0; online 17:24:52–56; 128 CPUs restored. | Command success verifies the sysfs state transition, not every internal invariant. |
| First warning | `C:147-189`: affinity fallback at uptime 14631.988149; warning 14636.489093; `sched_cpu_dying.cold`, CPU127, PID789 `migration/127`; dump `2 total`, only migration/127 named. | Teardown failed its runnable-count/pin predicate. Neither excess entity/task owner nor pin state is recorded. |
| v7 insertion | `S:99138-99146`: 17:26:09–17:38:46, status 0. `R:252-273`: one activation, 757.9982266s <1800s, expected transition/replacement/callback counts. | Incoming v7 execution cannot cause the earlier warning. These activation checks passed. |
| Second hotplug | `S:100676-100711`: offline 17:38:56–17:39:05 and online 17:39:06–11; successful state/count checks and subsequent progress. | No second matching warning is retained; this does not clear the first. |
| First active migration | `S:101303-101307`, `141389-141393`: population moved to A, correct membership. `S:141871-141875`: progress wait succeeds 17:41:33. | This migration/progress path executed successfully. |
| Health rejection | `S:142290-142369` reads cumulative dmesg from line 548 at 17:41:34–35; `R:103-110` rejects `WARNING:`. Native result is `unexpected_failure`. | A post-transition no-fault health failure correctly retains the earlier hotplug warning. |

**Coverage limit:** this is the health check after the first A migration
(`qualification.rb:513-522`), not proof that the end-of-example checks ran.
The later migration back to B, v7 disable transition, unload, stopped-task
checks, normal complete workload teardown and shutdown probe were unexecuted.
The health helper fails on its first dmesg match, before its own 64 forks and
six-second deferred-RCU observation (`common.nix:962-984`). Failure-hook cleanup
is separate evidence and cannot stand in for those assertions.

## Source-supported mechanism and remaining cause

Frozen Linux
[`core.c:8270-8343`](https://github.com/vpsfreecz/linux/blob/a2384967b90f24d2470c9eb15f0e66d938df7e08/kernel/sched/core.c#L8270-L8343)
expects parked/unbound per-CPU threads before final teardown. Earlier
`balance_hotplug_wait` waits for `rq->nr_running == 1` and no pinned tasks
(`:8004-8010`). At teardown, under the rq lock:

```c
if (rq->nr_running != 1 || rq_has_pinned_tasks(rq)) {
        WARN(true, "Dying CPU not properly vacated!");
        dump_rq_tasks(rq, KERN_WARNING);
}
dl_server_stop(&rq->fair_server);
/* subsequent scheduler cleanup */
return 0;
```

`rq_has_pinned_tasks` means `rq->nr_pinned` (`core.c:2386-2388`), maintained by
kernel `migrate_disable`/`migrate_enable`. Userspace affinity to one CPU is a
different concept. The expected single runnable context here is the stopper.
The warning reports that either count or pinning is wrong; the later count
of two supports the count branch but says nothing about whether pins also
remained. The task dump filters the global task list by CPU and queued state
(`:8303-8319`); it does not enumerate every scheduler entity or print pin state.

The callback explicitly continues cleanup and returns zero. It is registered
as `CPUHP_AP_SCHED_STARTING` teardown in
[`cpu.c:2160-2164`](https://github.com/vpsfreecz/linux/blob/a2384967b90f24d2470c9eb15f0e66d938df7e08/kernel/cpu.c#L2160-L2164).
Teardown descends through the hotplug states: deactivation, parked smpboot
threads, wait-empty, stop-machine teardown, then low-level dying callbacks.
`take_cpu_down` uses the nofail callback range (`cpu.c:1268-1292`); these late
callbacks cannot roll back normally. The WARN is therefore compatible with
sysfs success. This is not a hardlockup detector report or a panic report.

The following candidates fit the source boundary; none is established as the
runtime trigger:

| Candidate | Source support | Missing discriminant |
| --- | --- | --- |
| Late wakeup or callback ordering | Wait-empty's comment explicitly warns about later bound wakeups. `smpcfd_dying_cpu` flushes queued callbacks/TTWU work before scheduler dying (`kernel/smp.c:86-100,578-588`; `core.c:3777-3810`). | CPU127 hotplug callback order and wake/enqueue stack after wait-empty, with TID and actual rq state. No callback is identified by the retained stack. |
| Affinity/pinning interaction | The population intentionally pins one runnable worker per CPU and restores affinity after hotplug (`task_population.c:90-149`). `select_fallback_rq` emits “no longer affine” when broadening an unusable mask (`core.c:3463-3533`). | Actual allowed masks, migration-disabled depth, `nr_pinned`, enqueue/migration events at teardown. The named population worker is context, not an identified offender. The successful second cycle also has the fallback message. |
| Deadline fair-server entity/accounting | `inc_dl_tasks` increments `rq->nr_running` for a `sched_dl_entity` (`deadline.c:2076-2093,2171-2194`); the fair server is not a `task_struct`. Its timer can enqueue it (`:1204-1245`), while `sched_cpu_dying` calls `dl_server_stop` **after** checking the predicate. | At the locked predicate: `nr_running`, `nr_pinned`, CFS/RT/DL counts, fair-server identity/on-rq/active/throttled/defer/timer state, plus the count-change stack. Count two with only stopper does not prove a second task. |
| Other accounting inconsistency | The printed rq count and filtered task list are different observations. | Loss-accounted count deltas and class/entity/task snapshots. Existing evidence does not prove stale accounting or corruption. |

The fair-server candidate is a concrete narrowing, not permission to move
`dl_server_stop`, weaken the predicate, or call the warning harmless. No broad
kernel-authorship or production-hang attribution is supported.

## Identity and causal exclusions

vpsAdminOS target is `846bb469505789ba0b2a405fa5905ba6d8253006`.
`common.nix:409,504` imports the current machine with frozen boot configuration.
[`boot-6.12.95.nix`](https://github.com/vpsfreecz/vpsadminos/blob/846bb469505789ba0b2a405fa5905ba6d8253006/os/packages/linux/boot-6.12.95.nix)
binds producing OS `c065fa2f8485399737e20e8ef9e44299d0766654`, Linux
`a2384967b90f24d2470c9eb15f0e66d938df7e08`, ZFS
`481845fca6ae3f61ca2262c1a5693a58ae364650`, nixpkgs
`21a67dc470149f337cecafbe965d8d252a390518`, original config
`/nix/store/np082gl8insab5lisjdhqlh4128jlm9m-linux-config-6.12.95` and compiler
`/nix/store/hbsz2ngi9ixbhd9na1xagh2yc8qnmj7y-gcc-wrapper-15.2.0`.
The Nixpkgs revision follows `root.inputs.nixpkgs` to `nixpkgs_2` in the
[producing lockfile](https://github.com/vpsfreecz/vpsadminos/blob/c065fa2f8485399737e20e8ef9e44299d0766654/flake.lock),
not its unrelated `nixpkgs` node; the earlier node citation was corrected during
repair preflight without changing any frozen binary identity.
Frozen boot/SDK restore byte-checked archives, retaining DWARF:

| Identity | Pinned value |
| --- | --- |
| Original boot output | `/nix/store/f3rgj3iq8z1kvkc0g64d4mgyrjhi0q6w-linux-6.12.95` |
| Original SDK output | `/nix/store/c7ckwabnv0k4yfys5jnswjz08ffmirwh-linux-6.12.95-dev` |
| GNU build ID | `7801779436291880089e3407e50e5813f80d76f1` |
| bzImage SHA-256 | `3265b29d00581f09f9f171342c24cc8c6872ac679aca01f5e3fdb33d7850c541` |
| vmlinux SHA-256 | `6e63a63c8fd2fbaa92a51fd5bbcbd002909b33e0fa70ba77163075ab2014c5ab` |
| Effective v6 module | `/nix/store/pnvkxskdja1x3gddbhphqsaqj99b2pan-livepatch_6-exact-predecessor.ko` |
| v6 SHA-256 | `960b13f1b461b95e29cccff58ddf0d3f3badf151046eb46eba36a9c8c7e5efe3` |
| Incoming v7 SHA-256 | `573e8d1e05433be7c4eab361bb733e92977496f6437b43a4af1e5d21d2452d9d` |

The module checksum is checked successfully in the guest and independently
recovered from the archived fixture during this investigation. Read-only
[ELF evidence](evidence/hotplug/v6-elf.txt) confirms `livepatch_6` and 6.12.95
vermagic; the named hotplug/deadline-server functions have no NUL-terminated
name occurrences in those bytes, narrowing direct replacement without
excluding indirect v6 effects. The boot hashes/build ID above are package
contract evidence, not newly measured guest hashes. A same-version rebuild
can change its signing certificate/build identity; `uname` alone is inadequate.

Current generic sysctl service is reachable at boot: `D:1666,1688,3328` show
supervision/logger/down state. Its output, completion/check stamps and actual
early managed values are absent. Later stress writes (including PID/thread/map
limits and namespace SCTP settings) do not reconstruct earlier values or exclude
other managed values. Historical recurrence predates that service but cannot
exclude its contribution to this particular execution. Incoming v7 execution
is excluded by timing; current OS/sysctl state and already-active v6 are not.

## Recurrence and test value

Implementer3 owns the fixed latest-15 sample, downloads and
[complete recurrence table](recurrence.tsv), with
[counts](evidence/history/counts.json). Seven ordinary-CI executions started:
three native passes, one exact warning failure, one other early failure, two
started/cancelled without an outcome. Five eligible jobs were cancelled before
execution, and three benchmark workflows did not select this test. Only four
sampled runs reached first hotplug: three passed, one had this warning. These
are distinct heads, not a controlled failure-rate estimate.

Lane 2 independently validated the exact earlier match:
[39309610523/job118261936621](https://github.com/vpsfreecz/vpsadminos/actions/runs/39309610523/job/118261936621),
head `3ae196d60b2811e52cbb75a204108df629dca42d`, artifact `12260388778`.
Its console `149-189` shows the same first-offline warning/count/sole stopper;
shell `135-139` checks the same v6 hash, `99483-99507` completes first hotplug
before v7 insertion `100541-100545`. Activation later succeeds in 780.87996s
(`R:824`). This proves recurrence, not a common cause. Seed
[39600028637](https://github.com/vpsfreecz/vpsadminos/actions/runs/39600028637)
at `b81c43ff6865a033268072f55cd94ad763d0630b` has native `expected_success`,
activation 843.0894s and disable 1207.0944s. A workflow's overall red/cancelled
status is not the test's result.

In plain terms, this test asks whether a security livepatch can replace an
already-used kernel patch on a busy, long-running container host without
stranding work or damaging kernel state. The 128-CPU, 100000-task, four-hour
envelope exercises task scanning, deferred work, affinity fallback, CPU-local
state and long-lived NFS/SCTP/TUN/network state beyond a short smoke test.
It uses 128 **guest** CPUs; CI deliberately permits CPU oversubscription and
does not assert 128 physical cores. It covers two CPU hotplug cycles around
replacement, progress/perf/wakeup/fork counters, exact modules, transition
bounds/callback counts, preexisting data/locks and eventual removal/cleanup
when the entire example succeeds. It is not a proof against every production
hang or an exhaustive CVE exploit test.

The cost is substantial: current example 15606.9s, runner 15706.7s (about 4h22m),
16-GiB guest and 128 virtual CPUs; four hours of aging is intentional. Nominal
reservation is about 558 vCPU-hours and 69.8 GiB-hours over runner elapsed,
not measured physical CPU consumption. Exact frozen SDK/module maintenance,
large population startup and long trace/log collection add setup cost. A
13-minute activation success alongside this health failure shows why timing
alone would miss a useful invariant. The roughly 17-minute delay from warning
to assertion and traces starting after first hotplug impose avoidable diagnosis
cost; they do not make the warning noise.

## Priorities, diagnostic boundary and acceptance

1. **Keep the envelope and fatal cumulative no-fault assertion.** Add a health
   checkpoint immediately after each hotplug, before v7 after the first one,
   with explicit phase labels. Preserve the original example-wide dmesg history.
   If the predecessor phase fails, report activation as unexecuted; do not
   relabel it as a replacement timeout or allowlist this WARN.
2. **Capture one first-hotplug diagnostic before choosing a repair.** The
   existing livepatch ring starts only after that hotplug (`qualification.rb:491-493`);
   the CSD ring starts after the second one, around active migration. Shutdown
   tracing is later and was unexecuted. None can identify the first-warning
   owner. The [bounded proposal](evidence/hotplug/diagnostic-proposal.md) specifies
   exact events, locked-rq/class/entity/pin fields, source identities, one
   five-hour VM, a maximum 120-second trace window, bounded buffers/output and
   loss accounting. It stops before v7 insertion. Separate execution/recorder
   authorization is required; no diagnostic was run. Eligible dynamic probes
   need no kernel build; unavailable exact locked-state sites require a
   separately authorized diagnostic kernel/ABI plan, not a silent rebuild.
3. **Repair only the proven path.** Distinguish late task enqueue, pinned-task
   escape, fair-server entity/timer accounting and missing/lost trace evidence.
   No current evidence justifies changing sysctl policy, CPU count, age,
   callback ordering or the kernel warning. Do not remove the test: no redundant
   equivalent coverage or obsolete supported transition has been established.

A later accepted repair must pass both original hotplug cycles with correct
offline/online readbacks, 128 CPUs restored and per-CPU affinity/progress/perf
advancing within the existing 60s bound. At teardown the locked rq must satisfy
one stopper and zero pins, with class/entity state explaining the count.
Retain exact fixture/boot ABI checks, all activation/disable transition bounds
(1800s for this shape), independent callback counts and zero trace loss for
claims requiring completeness. Complete A and B migrations, retained data/
locks and workload progress, clean stopped-task counts and normal teardown,
with zero new kernel faults across the full original dmesg/shutdown window.
A one-off instrumented reproduction is diagnosis; it is not full qualification.

V6 remains quarantined; v7 remains unqualified for deployment. No forced
transition/unload, mixed-ABI module use or boot-generation rollback workaround
is proposed. Investigation changes no runtime, state format or fleet and
requires no coordinated machine update. Any later diagnostic kernel or rollout
needs its own compatibility/recovery design and authorization. No Git mutation,
application change, test/build/VM, rerun, deployment or lifecycle action occurred.

Checks: original-source line/range and file hashes verified; phase ordering and
native result cross-checked; recurrence reconciled with implementer3. Findings
and evidence alone do not select automatic change review. Lead owns shared
state/index/commits and final acceptance; session remains open at
[the stable portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-ci-failure-analysis/).
