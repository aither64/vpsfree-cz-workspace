# node24 kernel investigation synthesis

**No cause of node24's hang has been established. The assigned source
investigation is complete.** The full custom Linux patch inventory and selected
package overlays were accounted for; the subsequent targeted upstream audits
found no source-supported host-wide failure chain. This is a bounded negative
result, not proof that the kernel was healthy.

Three definite source defects were identified: a pre-existing syslog namespace
allocation-error NULL dereference, new swap-reporting arithmetic errors, and
an NFS FREE_STATEID allocation-error reference leak. None has a demonstrated
connection to this incident. The configured hard-lockup panic policy is
disabled, so a hard lockup without a crash upload is consistent with policy;
that does not establish that a hard lockup occurred.

## What the incident evidence establishes

Node24 stopped forwarding logs at **2026-10-20 18:58:26.658330 CEST**. Boot
output resumed at **19:12:04.761663**, a gap of **13m 38.103333s**. Other
nodes continued reaching the collector. Node24 SSH health-check and host
control traffic completed within the last three seconds before the gap.
The gap establishes lost node24 logging followed by a boot; it does not itself
identify the failed kernel subsystem or the exact moment of reset.

The affected boot identifies vpsAdminOS `2abbe3cc`, generation 144, Linux
6.12.113 built on October 18. That OS revision selects Linux
`1dfea587406b7dd79973831d1677fb2418e5e9aa`, the later .113 source after
proactive-swapping removal. The pre-upgrade kernel reported 6.12.95.6, which
includes a livepatch overlay and must not be equated with the .95 boot source
alone. Exact source and livepatch provenance belong to
[the inventory](patch-inventory.md); runtime observations belong to
[the log evidence](log-evidence.md).

The **blinking cursor does not prove that the scheduler was alive**.
Pre-incident boot logs identify a VGA text console and no framebuffer takeover
in the checked boot interval. In the exact incident source,
`drivers/video/console/vgacon.c:475` programs cursor start/end registers and
`vgacon_cursor()` at line 506 sets the cursor position and shape. This is a
hardware-cursor path, so continuing visible blinking is compatible with a
stalled host CPU. There is no live confirmation of the console driver at the
incident. A different driver can behave differently: `fbcon.c:369` flashes a
cursor from delayed work with `console_trylock()`. Consequently the observation
alone neither proves progress nor distinguishes a hard lockup from other hangs.

The completed log scan found no post-upgrade kernel panic, Oops, RCU stall,
lockup, blocked-task, global OOM, storage-fault or hardware-error signature.
That is an evidence limit, not exclusion of those failures: the failure itself
may prevent forwarding diagnostics.

A container NFS timeout appeared **8.420016 seconds** before the final log.
It is a useful discriminator for targeted follow-up, but temporal proximity
does not prove a host-wide failure mechanism. The 174 memory-cgroup OOM records
are tenant-scoped; the last was over 26 minutes earlier. The older NFS blocked
tasks at October 19 02:15 ran on **6.12.95.6**, before the upgrade, while host
control traffic continued. Do not attribute those stacks to the October 20 hang.

## Missing crash upload and configured policy

The user reports that the normal crash-kernel/upload recovery did not happen,
and confirms that sysctls were defined by the configuration and vpsAdminOS
repositories with **no runtime changes**. The final source/precedence trace
therefore supplies incident policy; these values are not left unknown merely
because no live `/proc/sys` read was possible.

| Policy | Incident value and consequence |
| --- | --- |
| Hard-lockup panic | **0**. The NMI watchdog can detect/report a hard lockup without calling panic or entering kdump. |
| Soft-lockup panic | **1**, explicitly set by the crashdump module and observed on the command line. Its timer callback must execute to detect the stall and call panic. |
| Watchdogs | General watchdog and PMU NMI watchdog enabled; threshold **10 seconds**, with soft-lockup detection using twice that threshold. Enabled at boot does not prove NMIs/timers continued at the failure. |
| Other panic controls | Panic timeout **0**; panic on warning, Oops, RCU stall and hung task **0**; crash post-notifiers **false**. Panic timeout 0 does not disable the earlier crash-kexec attempt. |
| SPL assertion policy | Configured `spl_panic_halt=1` calls Linux `panic()` at the exact ZFS pin. It does not select the assertion-thread sleep loop. |

There is **positive evidence that a crash image was loaded**:
`log:1279760` at **18:31:57.333383** and `log:1279973` at
**18:31:59.183362** both say `Kdump: loaded` on 6.12.113. At incident Linux,
`lib/dump_stack.c:62` prints that marker only when `kexec_crash_loaded()` is
true; `kernel/crash_core.c:94–96` tests `kexec_crash_image`.
This establishes image presence about 26.5 minutes before the final log,
stronger than the 4096M reservation or loader parameters alone. There is no
evidence that it was unloaded afterward; presence at the hang and successful
execution are not directly observed.

The missing upload does not distinguish no panic, failure before crash
transfer, or failure within crash-kernel capture/upload. The configured crash
script mounts its NFS destination before saving crash metadata, so absence
of uploaded metadata alone cannot identify which stage was reached. This is
a source-based explanation of the inference limit, not a claim that NFS
caused this failure. Bounded boot scans found no explicit loader failure or
capture/upload result.

The seven upstream printk changes preserve the inspected panic predicates
and ordering: initial printing/optional stack precede early crash kexec;
CPU stop and explicit legacy flush remain afterward. No new namespace/global
wait or pre-kexec regression was demonstrated. Exact source and configuration
proof is in [the platform audit](upstream-platform-audit.md),
[the printk audit](upstream-printk-audit.md), and
[the crash-state excerpts](node24-crash-state-excerpts.txt).

## Accepted custom-source conclusions

| Area | Proven result | Incident implication |
| --- | --- | --- |
| Fake scheduler affinity | Owner patch differs only in subject; complete syscall/custom helper files have identical blobs in .95 and incident .113. | Excluded as newly introduced custom behavior; no supported hang chain. See [source analysis](scheduler-analysis.md). |
| Syslog v20 to v21 port | Normalized additions/removals match; namespace ownership source is identical. Differences in surrounding printk code come from upstream. | No new namespace lock/lifetime regression established. See [syslog/NFS audit](syslog-nfs-audit.md). |
| Syslog namespace allocation failure | A newly allocated namespace's `prb` stays NULL until all setup allocations succeed, but the failure cleanup dereferences it. The exact namespace source blob is identical in both kernels. | A source-proven **pre-existing** defect, with no incident allocation-failure or namespace-creation evidence. Do not name it as the cause or a regression. |
| NFS cold-client guard | Adds only a NULL return before an existing client cancellation path. It adds no wait or lock and does not skip the enclosing server shutdown. Successful NFSv2/v3 mounts already bind the NLM client eagerly. | No supported new hang mechanism. NFS timeout records do not establish use of this shutdown callback. See [syslog/NFS audit](syslog-nfs-audit.md). |
| Memory-view lifetime | Helper source is identical; `/proc/swaps` keeps one CSS reference from successful open through final release, including unread and repeated-read paths. | No reintroduced reference imbalance or new helper lock/progress change. See [memory audit](memory-audit.md). |
| Proactive swap/DAMON retirement | Custom policy/accounting and principal interfaces are removed; selected DAMON/swap files exactly match the new upstream base. Old proactive bookkeeping is in-memory, not state reused by the new boot. | No residual custom worker or persisted-map transition explains the hang. A pressure effect from removing an active policy is unproven. |
| Ordinary swap reporting | Two v1 calculations can wrap from inconsistent counter samples after old bounding code is removed. Results are formatted/returned, not used here for allocation, reclaim or indexing. | Source-proven output regression; no demonstrated kernel hang or userspace escalation chain. See below and [memory audit](memory-audit.md). |
| Packaged ZFS free accounting | Removes a conditional dbuf-mutex → hash-lock edge opposed by lookup's hash-lock → dbuf-mutex order. Existing holds and sync ownership protect accounting reads; BP publication stays locked. Both package modes at the incident OS apply it. | No replacement deadlock/lifetime/writer failure found in the bounded audit; not supported as an introduced regression. See [ZFS audit](zfs-patch-audit.md). |
| Package/config overlays | Exact OS and observed Nixpkgs inputs account for patch selectors; bridge-helper patch changes a path macro, other version-specific NFS/NMI patches do not apply, and default livepatch/eBPF payload selection is empty for .113. | No additional unexamined selected runtime patch in this package scope. Exact binary config and loaded module identity remain uncollected; configured sysctl policy is resolved above. See [packaging audit](packaging-audit.md). |

The complete Linux inventory accounts for 60 old, 61 initial .113,
and 55 incident .113 custom commits: 52 retained bodies, one consolidation of
two old memcg fixes, six removed proactive/DAMON owners, and two added owners
(NLM guard and swap reporting). A potential NFS teardown/callback lifetime concern in the lane
record remains unproven and pre-existing; it is not a supported incident
candidate and does not delay the downstream-delta conclusion.

## Targeted upstream conclusions and coverage

The exact stable range is `296aabce459470a4c1b68ffd0c0c0920e563aaad`
through `7fdb7c1824a1f9979d648d7ae28ac446bcee9c6e`, comprising 7,278
commits and 5,291 touched paths. The upstream phase intentionally examined
selected mechanisms and their final incident-tree callers; it did **not**
audit every commit. [Upstream provenance](upstream-provenance.md) also maps
74 old v6 backport/prerequisite commits into the stable window, preventing
raw stable membership from being mistaken for a newly introduced runtime
change.

| Completed lane | Accepted result |
| --- | --- |
| [Memory/reclaim](upstream-memory-audit.md) | Selected memcg, shrinker, vmalloc, swap, slab and adjacent lifetime/progress paths yielded no new host-wide failure chain. The vmap purge-mutex change already occurs in documented old v6 source. Tenant OOMs do not establish host exhaustion. |
| [NFS/SUNRPC](upstream-nfs-audit.md) | FREE_STATEID has the precise reference leak below. TLS cancellation, transport destruction and inspected NFS/lockd/cache/VFS lock changes yielded no demonstrated host-wide cycle. TLS/RDMA/pNFS use remains unknown. |
| [Scheduler/RCU/locking](upstream-scheduler-audit.md) | 33 selected commits across 17 files, including immediate custom affinity/load-average/cgroup intersections, yielded no concrete new host-progress failure. Core-scheduling wait releases locks/IRQ exclusion; inspected selection counts balance; RCU changes add no new blocking dependency. |
| [Printk/panic](upstream-printk-audit.md) | All seven changes in the selected printk path and their custom namespace intersection were inspected. No new lock/wait cycle or panic-to-kexec regression was found. |
| [Platform/watchdog](upstream-platform-audit.md) | Selected x86 NMI/APIC/TSC/watchdog/crash-transfer files have no direct stable delta; inspected timer-broadcast, ACPI idle and AMD changes yield no concrete new progress failure. Hardware is EPYC 7H12, family 0x17; Zen5-specific changes do not apply. |

Config gating uses explicit recipe values and unchanged Kconfig/build
lineage, corroborated by the initial .113 config. CORE, EXT, PREEMPT_RT,
PSI, LRU_GEN and MEM_ALLOC_PROFILING exclusions are **source-inferred recipe
conclusions**, not recovered incident binary attestation. Observed full dynamic
preemption is not PREEMPT_RT. See [packaging](packaging-audit.md) for exact
strength and limits. Unchanged source or a disabled branch excludes only
that stated mechanism, not the subsystem as a whole.

## Pre-existing syslog defect: precise confidence boundary

At incident Linux `1dfea587406b7dd79973831d1677fb2418e5e9aa`,
`kernel/syslog_namespace.c:128` zero-allocates the namespace.
`syslog_ns_setup_log_buf()` assigns `ns->prb` only at line 70, after the
ringbuffer, data, descriptor and information allocations succeed. An allocation
failure returns to `clone_syslog_ns()` cleanup at line 160;
`syslog_ns_log_buf_free()` dereferences `ns->prb` at line 90.
This is a definite NULL dereference if that setup failure path executes.

The complete source blob is
`e55346ef9a374d12966d4c10ae3d81fb0d9949c1` at both old and incident revisions.
Later cleanup also has stale freed pointers in some failure branches, but the
earlier NULL dereference occurs first; no separately observed double-free is
claimed.

No captured incident trace ties the host hang to this path. Tenant memcg OOM
messages do not establish failure of these `GFP_KERNEL` allocations. A
dedicated fault-injection test could reproduce the error handling defect, but
would not by itself prove that node24 exercised it. Such a test or remediation
would be separate work; neither has been run.

## Swap reporting regression: precise confidence boundary

The final memory audit supplies concrete legal counter interleavings in the
cgroup-v1 branch. With a 1024-page memory limit and 1280-page memsw limit, read
memory usage as zero, then charge 512 resident pages before reading combined
usage as 512. Actual swap may remain zero, but `kernel/sys.c:2892` reports free
swap as unsigned `256 - (512 - 0)`. Conversely, freeing resident memory between
the two reads can make `mm/swapfile.c:3043` compute a wrapped used-swap value.
The earlier wrappers bounded these values.

This proves incorrect output is possible in the source under the stated
conditions. It does not prove that the interleaving occurred on node24, and
the outputs do not feed a kernel allocation or reclaim operation in these
paths. No consumer reaction or host-wide failure chain has been demonstrated.
Keep this actionable reporting defect separate from the hang attribution.

## FREE_STATEID leak: precise confidence boundary

Stable commit `ed1161ab6239761958b38d5667225634fc2be894` adds an active-server
pin to `nfs41_free_stateid()`. In incident `fs/nfs/nfs4proc.c:10630–10643`,
the function holds client and active-server references when its calldata
`kmalloc()` can fail; the immediate `-ENOMEM` return drops neither. No RPC
exists to run the release callback. The proven effect is retained
server/superblock/client resources, with no lock held by the return and no
demonstrated host-wide wait.

The documented old v6 adapter and the old NFS boot variant both clean up those
references on this failure path. This is a source regression relative to those
correct old effective paths; actual historical module/control state remains
qualified. The pristine old stable path's client-reference leak was already
present and must not be confused with those effective alternatives. A later
RPC-task allocation failure invokes cleanup and is **not** this leak.

NFSv4.1 FREE_STATEID activity and failure of this particular allocation are
unestablished at the incident. The nearby timeout does not prove either.
The [NFS audit](upstream-nfs-audit.md) records the complete reference chain
and old-path comparison. Reproducing this leak would verify the leak, not
attribute the host hang without an additional progress mechanism.

## Remaining evidence and next useful step

No kernel build, reproduction, configuration change, deployment or production
mutation has been performed by this investigation. The source identity checks
and source-path checks support the bounded conclusions above. Investigation
and evidence alone require no automatic change review.

Direct recovery-runtime inspection has not been possible through an existing
trusted SSH identity. Current runtime state would still need to be reconciled
with the historical boot. The exact failed liveness probes and recovery/reset
method remain unconfirmed in this evidence record. Sysctl policy and positive
pre-gap crash-image presence are resolved and must not be included among
those unknowns.

The next useful evidence is a trace that distinguishes the failure stage:
all-CPU/NMI or blocked-task stacks at a recurrence; console/BMC evidence of
whether panic and crash-kernel entry occurred; and crash-kernel
device/network/capture output if entry occurred. Exact affected NFS mount
options and operation context would refine the adjacent NFS symptom.
Any future instrumentation or policy change is a separate proposal, not an
operation performed or authorized by this investigation.

Without a concrete source mechanism and trigger, a generic passing stress
test, broad additional release audit, or speculative patch change would not
settle attribution. The assigned source work stops here with the incident
unattributed, the definite defects separated, and the session left open.
