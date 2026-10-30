# Proposed first-hotplug capture — not executed

This is a proposal requiring separate lead/user authorization for one disposable
diagnostic, its recorder implementation and resource reservation. No diagnostic,
VM, test, build or rerun was launched by lane 2. It is not a deployment recipe.

Use current OS `846bb469505789ba0b2a405fa5905ba6d8253006`, original frozen
Linux `a2384967b90f24d2470c9eb15f0e66d938df7e08`, the original boot-image/notes
identity, and predecessor module SHA-256
`960b13f1b461b95e29cccff58ddf0d3f3badf151046eb46eba36a9c8c7e5efe3`.
Retain the existing AMD guest envelope: 128 vCPUs, 16384 MiB, 100000 tasks,
14400 seconds aging, all original concurrent workloads, cgroup-B setup,
configured/effective memory-node masks and progress requirements. Record runner
CPU allocation/oversubscription, QEMU version/arguments, guest CPU topology,
source/input/fixture hashes and exact system/kernel/module paths. A faster
small-CPU or unaged case would be a different experiment.

Stop after the first CPU127 offline/online and its progress/health capture,
before `qualification_trace_start` or incoming v7 insertion. One five-hour
outer budget includes existing preparation and four-hour aging; reserve the
128-vCPU/16-GiB VM explicitly. Preserve the existing population-readiness bound
(1800 seconds), progress bound (60 seconds) and ordinary hotplug command bounds.
Do not add retries. Trace only the last phase: arm immediately before the first
offline, stop immediately after online/health capture, with a 120-second hard
trace-window ceiling. A timeout fails the diagnostic and preserves partial data.

## Required observations

Before aging, after aging/before hotplug, and immediately after hotplug, retain
the population report, cgroup CPU/memory masks, online/active/dying CPU masks,
module enabled/transition state and boot identity. Preserve the full original
dmesg baseline and monotonic phase markers; never clear it to obtain a pass.
For sysctl causality retain the managed input bytes/hash, `/var/log/sysctl`
output, `/run/service/sysctl/{applied,done}`, check outcome and timestamped
readbacks of **all managed keys**, plus stress-owned PID/thread/map limits,
watchdog/trace controls and relevant per-network-namespace settings. Observe
these without triggering another service apply. The earliest available boot
readback may follow service application; label it accordingly.

Create a dedicated tracefs instance
`/sys/kernel/tracing/instances/hotplug_first`, using a global trace clock and
1 MiB per virtual CPU (128 MiB total). Keep all CPUs in the tracing mask so a
remote waking context is visible. Enable only:

| Event | Filter and reason |
| --- | --- |
| `cpuhp:cpuhp_enter`, `cpuhp_multi_enter`, `cpuhp_exit` | `cpu == 127`; retain target, step/index, callback function and return value. Read the runtime hotplug state-name table to map indices. |
| `sched:sched_waking`, `sched_wakeup`, `sched_wakeup_new` | `target_cpu == 127`; distinguish waking context from activation context. |
| `sched:sched_migrate_task` | `orig_cpu == 127 || dest_cpu == 127`; identify departures and late arrivals. |
| `sched:sched_switch` | `common_cpu == 127` (the kernel's synthetic CPU filter field); retain current/next TID and prior state. Validate filter installation/readback on this binary before collection. |

These events alone do not expose `nr_pinned` or explain a counted scheduler
entity. Add a privileged BTF-aware BPF/raw-tracepoint recorder, or verified
dynamic probes, with this exact data contract:

1. Attach `sched_update_nr_running_tp` and filter on `rq->cpu == 127`. It is
   `DECLARE_TRACE`, not a normal tracefs `TRACE_EVENT`; a fictitious
   `events/sched/sched_update_nr_running_tp/enable` is not a valid plan.
   Record timestamp, delta, resulting `nr_running`, `nr_pinned`,
   `cfs.h_nr_queued`, `dl.dl_nr_running`, `rt.rt_nr_running`, `curr` TID/comm,
   and fair-server identity/on-rq/active/throttled/defer/armed state.
2. Capture the same state when `sched_cpu_wait_empty` returns and at
   `sched_cpu_dying` entry. Capture it at **core.c:8332 with the rq lock held,
   immediately before the warning predicate**, plus after `dl_server_stop`.
   Resolve this source point against the exact restored `vmlinux` DWARF and
   disassembly before selecting an instruction probe. Do not invent offsets
   from a different kernel or from the warning's post-call register dump.
3. Trace `dl_server_start`, `dl_server_stop`, `dl_server_timer` and entity
   enqueue/dequeue for `rq->cpu == 127`. Record entity pointer, whether it is
   `&rq->fair_server`, its on-rq/active/defer/timer state and rq/class counts.
   Capture a bounded kernel stack for every count increment after wait-empty
   completion and every server enqueue in that interval.
4. Trace `migrate_disable`/`migrate_enable` with task TID, migration-disabled
   depth and `rq->nr_pinned` before/after, filtered to CPU127. Snapshot task
   CPU, allowed mask, `on_rq`, state, scheduling class and per-CPU-kthread flag
   for each task implicated by a late wakeup or nonzero pin count. A bounded
   task map must expose map-full/drop counters rather than silently evict.

Confirm BPF/probe eligibility and actual event/field availability first. Source
configuration enables BTF/BPF/probing, but a source setting does not prove
every optimized function or instruction is probeable on this binary. Preserve
the boot-image/notes guard and original module bytes. Dynamic instrumentation
on eligible existing sites needs no separate kernel build; it still needs an
authorized recorder change and diagnostic run. If exact locked-rq state cannot
be captured safely with the existing binary, propose a **separate** diagnostic
kernel with a narrow tracepoint at the predicate and paired entity/pin changes.
That changes binary/build identity: use a separately validated matching ABI/SDK
and module plan, retain original artifacts, and do not substitute its result for
qualification of the frozen binary. Never bypass identity checks or quietly
load original modules into an unverified rebuilt kernel.

Use at most a 64-MiB BPF output buffer, 4096 tracked tasks, 1024 unique stack
IDs, 128-MiB tracefs rings and a 256-MiB combined output-file cap. Drain both
streams continuously during the short capture. Stop and mark incomplete at a
cap; preserve byte/event counts, tracefs `per_cpu/cpu*/stats`,
`kprobe_profile` missed-hit counts, BPF reserve/output failures, stack/task-map
capacity failures and start/end timestamps. No loss-free claim is valid without
these counters. A lost interval can prove an observed event but cannot exclude
an unrecorded wakeup or accounting change. Do not automatically rerun it.

## Discriminating outcomes

- A task enqueued after wait-empty, with callback/wakeup stack and pin state,
  identifies a task/callback path for focused repair. Merely adjacent callback
  timing is weaker than a captured waking/enqueue stack.
- `nr_running == 2`, no second queued task, `dl_nr_running == 1` and the
  fair-server entity on the deadline rq at the predicate would support the
  specific entity-accounting explanation. Pair it with the actual count delta,
  server/timer stack and state before/after stop; a lone postfailure count is
  insufficient.
- Nonzero `nr_pinned` requires an identified migration-disabled task and its
  enter/leave history. Userspace CPU affinity is not this kernel pin count.
- A class-count/task/entity mismatch without a matching event narrows an
  accounting problem only if capture completeness is established; otherwise
  the result remains unresolved.

Leave quarantine and recovery intact: no forced transition, forced unload,
production operation or boot-generation rollback workaround. The disposable
diagnostic ends through the runner's ordinary bounded failure/cleanup path.
