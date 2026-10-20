# Custom memory-source audit

Owner: implementer2. Read-only investigation on 2026-10-20, following
[design.md](design.md) and the lead's memory assignment. Exact session slug and
both environment markers matched before source reads. Only this artifact is
written; no kernel source, refs, production state, builds or tests were changed.

## Bounded conclusion

**No supported custom-patch explanation for the host hang was found in this
lane.** The memory-view lifetime helper is byte-identical in all three requested
trees. The virtual `/proc/swaps` reference ownership remains balanced. The final
incident tree removes the custom DAMON/proactive-swap implementation rather
than retaining a partially converted version of its principal interfaces.

There is a **source-proven reporting defect, incident attribution unresolved**:
the restored ordinary view leaves two cgroup-v1 swap calculations vulnerable to
inconsistent counter snapshots. They can return incorrect unsigned values.
This is an output defect; no chain from those values to kernel memory corruption,
reclaim failure, deadlock or host-wide loss of progress is established.

This conclusion covers the assigned downstream delta and immediate dependencies.
It does not certify the memory subsystem or exclude an upstream regression.
The conditional upstream lane has not been started.

## Exact source identities

All paths and line numbers below refer to canonical `repos/linux.git`; current
line numbers mean the full current SHA in this table.

| Role | Linux revision |
| --- | --- |
| Old 6.12.95 source pin | `a2384967b90f24d2470c9eb15f0e66d938df7e08` |
| Initial 6.12.113 pin | `11058eb4fe1cba30653e8e643546c13bc8bcd792` |
| Current/incident 6.12.113 pin | `1dfea587406b7dd79973831d1677fb2418e5e9aa` |
| Current upstream baseline | `7fdb7c1824a1f9979d648d7ae28ac446bcee9c6e` |

[log-evidence.md](log-evidence.md) records boot OS `2abbe3cc`, build timestamp
2026-10-18 17:47:47 UTC and generation 144 before and after the incident. The
design/provenance lane maps that OS to the current Linux pin. The previous
running version was `.95.6`; this audit compares the requested `.95` source
tree and does not independently reconstruct every previously applied livepatch.
Direct runtime/livepatch inspection was unavailable in the log package.

## Memcg lifetime: consolidation preserves the fixed source

`kernel/vpsadminos.c` has the identical complete blob
`062ad3f5617ddea097566d69b46006ce452aa003` at **all three** requested revisions.
Consequently folding old `f69b960f6ed027c407b38bd38a25caaf995428b4` plus
`a2384967b90f24d2470c9eb15f0e66d938df7e08` into
`def4b8a2613fd958daf882cfd4a9ff7a7e7ac1f0` introduces no helper-source delta.

The actual ownership chain in `get_current_most_limited_memcg()` is:

1. Lines 33–41 return NULL without a reference when the controller is disabled
   or the early task CSS is absent.
2. Lines 36–48 protect `task_css(current, memory_cgrp_id)` with RCU and retry
   until `css_tryget(css)` obtains one reference. The RCU section ends after
   that reference is obtained.
3. Lines 50–60 walk the parent chain while retaining that CSS reference.
   `init_and_link_css()` takes a reference on `css->parent`
   (`kernel/cgroup/cgroup.c:5603–5605`). Its matching put occurs only after
   the child's `ss->css_free(css)` (`:5464–5474`). Thus retaining the child
   also preserves the ancestors visited by this helper.
4. Lines 65–67 get the chosen CSS before dropping the initial CSS. If they
   are the same CSS, the extra get and put leave exactly one caller reference.
   If no finite limit is selected, lines 69–71 drop the initial reference and
   return NULL.

The old pre-fix helper could return a pointer after failed `css_tryget()` and
then have its caller drop a reference never obtained. That historical defect is
visible in the f69b960f diff, but **none of the three assigned final trees has
that behavior**. The earlier commit's mention of a 6.12.87 rstat crash is not
incident evidence for this `.113` hang.

The retry loop is the same acquisition algorithm as upstream `task_get_css()`
(`include/linux/cgroup.h:437–465`), with the additional disabled/NULL guards.
`css_tryget()` accepts an offline CSS while its count is nonzero
(`include/linux/cgroup_refcnt.h:30–47`); it is not `css_tryget_online()`, whose
use could continually reject an exiting task's offline CSS. No newly added lock,
RCU grace-period wait or progress dependency appears in this consolidation.
An infinite retry would require a continuously ungettable task CSS; this audit
has no source proof or runtime evidence of that condition. Byte equality also
excludes this loop as a newly changed downstream helper in the upgrade.

Immediate callers retain their expected puts: `fs/proc/meminfo.c:241–242`,
`kernel/sys.c:2910`, and `mm/shmem.c:142–160`. Adjacent
`__invalidate_reclaim_iterators()` NULL-nodeinfo checking and the RCU-protected
ancestor walk (`mm/memcontrol.c:1110–1143`) are also present in all three trees;
the retirement did not remove those protections.

**Outcome:** a newly introduced helper reference imbalance or helper-source
retry regression is **excluded within this comparison**, with high confidence.
That does not prove the entire cgroup core cannot fail for another reason.

## Virtual /proc/swaps: file lifetime owns the reference

The following same control flow is present in old `mm/swapfile.c:3092–3134`,
initial `.113` `:3093–3135`, and current `:3071–3113`:

| Path | Reference owner and release |
| --- | --- |
| Helper returns NULL | Native `seq_open()` path; no memcg reference |
| Helper returns memcg; `single_open()` fails | `swaps_open()` puts it immediately |
| Successful virtual open | `seq->private` owns the one helper reference |
| Read, repeated read, seek/re-read | `fake_swap_show()` reads the pinned memcg; no put |
| Final release, including a file never read | `swaps_release()` puts it once, clears private, calls `single_release()` |

`single_open()` stores its private data only on success
(`fs/seq_file.c:572–589`). `single_release()` also frees its allocated
operations structure (`:611–617`). The native path uses `seq_release()` and
does not have a private memcg to drop. The new zero-capacity early return in
`fake_swap_show()` still reaches the ordinary file release later; it does not
own the reference and does not leak it.

Before f69b960f, putting from `show()` could over-release on repeated show calls
or leak on an unread open. That defect is already fixed in the old `.95` pin
and remains fixed in initial and current `.113`.

**Outcome:** reintroduction of that known seq-file lifetime defect is
**excluded within this comparison**, with high confidence. No new lock cycle
or unmatched put was found on the audited success/error/close paths.

## Proactive DAMON/swap retirement

Old and initial `.113` contain the experimental proactive accounting, per-node
scope and free-memory quota extensions. Current `.113` does not contain the
custom `system_proactive_swap`, `proactive_map`,
`mem_cgroup_proactive_swap*`, `DAMON_RECLAIM_SCOPE*`,
`quota_free_mem_rate` or `quota_free_mem_bytes` symbols in the audited
`include/`, `mm/`, proc-memory and sysinfo source.

Whole-blob comparison to the current tree's **own** upstream baseline proves
exact upstream equality for:

- `include/linux/damon.h`, `include/linux/swap.h`,
  `include/linux/swap_cgroup.h`, `include/trace/events/vmscan.h`;
- `mm/damon/core.c`, `paddr.c`, `reclaim.c`, `sysfs-schemes.c`, `sysfs.c`;
- `mm/swap_cgroup.c`;
- `Documentation/admin-guide/mm/damon/reclaim.rst` and `usage.rst`.

The remaining custom diff in `mm/vmscan.c` is the pre-existing
`cgroup_memory_kmem_enabled()`/kswapd condition around `shrink_slab()`
(`:5963–5966`), not a residual proactive-swap branch. The custom additions in
`include/linux/memcontrol.h` are unrelated existing virtualization/debug/kmem
declarations; the proactive counter and altered charging signatures are absent.
Current `__mem_cgroup_try_charge_swap()` uses ordinary checked charging and
the matching ID-reference failure path (`mm/memcontrol.c:5107–5145`).

This is not removal of upstream DAMON itself. Upstream DAMON_RECLAIM remains;
the retired code supplied the additional policy/accounting behavior. Enabling
DAMON still requires its configuration and runtime parameters. A `.113`
version string alone cannot distinguish the initial experimental pin from the
incident pin.

The old over-limit swap-charging bypass was below the early
`do_memsw_account()` return (`old mm/memcontrol.c:5108–5137`), so the explicit
bypass was a v2 path. Its removal does not demonstrate newly enforced ordinary
v1 swap charging. The design's v1/nokmem applicability must be respected.

The proactive bit map and memcg counters were in-memory kernel bookkeeping.
Current `swap_cgroup_swapon()` allocates its own fresh map
(`mm/swap_cgroup.c:175–205`), and swapoff clears/frees it (`:212–238`). There is
no source chain here in which a fresh normal boot interprets an old proactive
map from disk. This does not assert that an arbitrary live replacement of
different kernel structures would be safe; no such replacement is authorized
or demonstrated.

Loss of a formerly enabled proactive policy could change pressure/latency, but
calling it the host-hang cause would additionally require evidence that the old
policy was active, that relevant pressure existed, and that ordinary reclaim
then lost progress through an identified path. None is established here.
The log package found tenant memcg OOMs, with the last more than 26 minutes
before the gap, and no forwarded host OOM/allocation failure. Missing messages
cannot exclude a hang that stopped logging.

**Outcome:** a surviving custom proactive worker/metadata implementation in
the incident source is **excluded within the audited interfaces**. The broader
claim that retiring proactive policy caused a global reclaim hang is
**not supported**.

## Ordinary swap v3: reporting defect, no demonstrated host failure

The complete `1dfea587` patch touches only `fs/proc/meminfo.c`, `kernel/sys.c`
and `mm/swapfile.c`. It corrects capacity/free reporting and suppresses an empty
virtual device. It introduces no new charging, reclaim, reference ownership,
lock acquisition or wait. Its finite v2 saturation and v1 unlimited reporting
are separate from the remaining edge cases below.

Two calculations in the current ordinary view lack the saturation retained by
old/initial proactive wrappers:

1. **Finite v1 sysinfo free swap:** `kernel/sys.c:2892–2893` computes
   `S - (M - U)`, where `S = memsw.max - memory.max`, `U` is an earlier memory
   usage sample, and `M` is a later combined usage sample (`:2873–2877`).
   `page_counter_read()` is an individual atomic read, not a common snapshot
   (`include/linux/page_counter.h:63–66`). For a concrete legal interleaving,
   keep memory limit 1024 pages and memsw limit 1280 pages, giving S=256. Read
   U=0, then charge 512 resident pages before reading M=512. Both limits are
   respected and actual swap usage can be zero, but the reported free value is
   unsigned `256 - 512`. Old `kernel/sys.c:2896–2900` clamps this derived free
   value at zero; initial `.113` retains that guarded implementation.
2. **v1 /proc/swaps used swap:** current `mm/swapfile.c:3027–3037,3043–3047`
   reads memory usage before combined usage and computes
   `(M - U) * PAGE_SIZE` without saturation. Read U=512, free 256 resident pages,
   then read M=256, with a nonzero finite swap allowance. The subtraction wraps
   and the printed used value is huge. Old `:3064–3067` and initial
   `:3065–3068` bound the ordinary used value to the displayed capacity.

These examples prove arithmetic/output behavior from source; they are **not
executed reproductions**. They require a selected finite memory cgroup, the v1
accounting branch and concurrent usage changes. Relevant per-container limits,
sampling interleavings and values returned immediately before the incident were
not collected. v1 source applicability is part of the design/package lane;
`cgroup.memory=nokmem` alone would not prove the cgroup hierarchy mode.

The unsigned results are passed to proc formatting or returned in the sysinfo
structure. They are not used here as allocation sizes, array indices, memcg
charges or reclaim targets. There is no direct kernel memory-safety or
nontermination consequence in these paths. A hypothetical userspace reaction
would require a named consumer, actual input and a separately demonstrated
failure chain; this audit has none.

**Outcome:** **source-proven reporting defect, incident attribution unresolved**,
high confidence in the arithmetic, no confidence claim for incident occurrence.
It is a regression in output bounding relative to the two requested
proactive-enabled trees, not evidence that v3 adds a kernel hang.

## Verification and limits

Performed source-only checks: exact blob identities, corresponding old/new
success and error paths, upstream-baseline comparisons for retired interfaces,
remaining custom vmscan/header diff, exact-symbol searches, and incident-log
cross-reference. Later reads explicitly set `GIT_NO_LAZY_FETCH=1`; no fetch/ref
update was requested. No build, runtime experiment or production operation ran.

No source-proven host-hang candidate warrants a reproduction from this lane.
To attribute a future memory candidate, obtain a discriminating lockup stack,
crash dump, allocator/reclaim trace or a bounded isolated old/new/fix comparison
with the exact configuration. A reporting-only reproduction would settle the
observable output defect but would not settle this incident. Source and runtime
scope remain separate, and the session stays open for the lead's synthesis.
