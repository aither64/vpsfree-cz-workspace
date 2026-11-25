# Upstream memory/reclaim source audit

Owner: implementer2, 2026-10-20. This is the user-authorized upstream phase,
started only after the lead accepted the custom-phase gate. See
[design.md](design.md), [memory-audit.md](memory-audit.md),
[patch-inventory.md](patch-inventory.md), and
[packaging-audit.md](packaging-audit.md).

## Result and evidence boundary

**Not supported:** this selected upstream audit found no demonstrable new
host-wide progress, lifetime or lock-order failure that explains node24's hang.
No incident cause or new memory-safety defect is claimed. This is a bounded
negative result, not certification of all memory changes or the whole kernel.

The source comparison is strictly between upstream stable bases:

- Old: `296aabce459470a4c1b68ffd0c0c0920e563aaad` (6.12.95).
- New: `7fdb7c1824a1f9979d648d7ae28ac446bcee9c6e` (6.12.113).
- Final source/caller checks use incident input
  `1dfea587406b7dd79973831d1677fb2418e5e9aa`.

Line references below are in that final incident tree unless otherwise stated.
Commit messages were used to locate mechanisms and upstream provenance; the
conclusions below use the actual diff and final code. No build, test, production
operation, ref update or fetch ran. Reads used `GIT_NO_LAZY_FETCH=1`.

The observed tenant `CONSTRAINT_MEMCG` OOMs do not establish host exhaustion.
The last recorded tenant OOM was more than 26 minutes before the logging gap;
the logs do not contain an incident allocator/reclaim/lockup stack. Missing
forwarded messages cannot exclude a failure that stopped logging.

## Selection and configuration

Reviewed the complete upstream final delta in `mm/memcontrol.c`,
`mm/memcontrol-v1.c`, `mm/memcontrol-v1.h`, `include/linux/memcontrol.h`,
`mm/vmscan.c`, `mm/shrinker.c`, `mm/swap_cgroup.c`, `mm/swapfile.c`,
`mm/vmpressure.c`, `mm/page_alloc.c` and `kernel/cgroup/cgroup.c`.
`mm/page_counter.c`, `mm/oom_kill.c`, `include/linux/cgroup.h`,
`include/linux/cgroup_refcnt.h` and `kernel/cgroup/rstat.c` have no upstream
base-to-base delta. An unchanged file does not mean its callers cannot change.

For direct global allocation/reclaim dependencies, also reviewed the final
delta in `mm/vmalloc.c`, `mm/slab.h`, `mm/slab_common.c`, `mm/slub.c`,
`include/linux/slab.h`, `mm/compaction.c`, `mm/backing-dev.c` and `mm/zswap.c`.
Selected adjacent THP/rmap/tmpfs changes were inspected in `mm/huge_memory.c`,
`mm/rmap.c` and `mm/shmem.c`, including current callers and error exits described
below. These selections are not all 123 upstream commits touching `mm/`.
Cpuset/scheduler/RCU internals and NFS/writeback incident attribution remain
the other assigned lanes' responsibility.

Packaging evidence has several different strengths:

| Gate | Evidence and use in this audit |
| --- | --- |
| `preempt=full`, `cgroup.memory=nokmem` | Observed boot command line. Full dynamic preemption is not PREEMPT_RT. Nokmem does not disable all global shrinkers or the memory controller. |
| Hybrid cgroups, MEMCG_V1/CPUSETS_V1 | Configuration source selects these; actual historical runtime mounts were not collected. Keep v2-only explanations conditional on a different runtime setup. |
| PREEMPT_RT=n, PSI=n, PROVE_LOCKING=n | Ordinary recipe source requests/gates; PREEMPT_DYNAMIC boot banner supports the non-RT distinction. Do not equate PROVE_LOCKING=n with a complete LOCKDEP selector audit. |
| LRU_GEN=n, MEM_ALLOC_PROFILING=n; SLUB_DEBUG=y, SLUB_DEBUG_ON=n | Packaging owner derives these from unchanged Kconfig/recipe inputs and generator defaults, corroborated by an initial `.113` config from a different source revision. These are **source-inferred ordinary-recipe values**, not an attested incident `.config`. Relevant branches were still inspected instead of excluded solely by that initial config. |
| DAMON_RECLAIM | Capability requested, managed enable defaults false with no located override; manual runtime activation is unknown. The retired custom DAMON implementation is covered separately in the custom audit. |

## Core memcg and lifetime mechanisms

### Limit writers and v1 soft limits

`39ec1e4183a718f448b2e9de681dcbdda18fce42` adds a current-limit check to
the v2 `memory.high` and `memory.max` reclaim loops. Final
`mm/memcontrol.c:4156` and `:4207` break when another writer supersedes the
local target. Previously, concurrent writers could leave the first reclaiming
toward a stale target; an OOM attempt could return success against the raised
actual limit and let the stale-target loop continue. The new condition removes
that continuation, without adding a lock or wait. The named files are v2
controls; the expected v1 memory controller uses the legacy limit writer.
This is a repaired historical loop, not an uncorrected `.113` mechanism.

`72fb67f6e0e5d78e4f34cf9929d1afdb0fd54203` makes
`memory.soft_limit_in_bytes` inert. Final `mm/memcontrol-v1.c:2442–2463`
parses input, warns once and returns; reads report the maximum. Memcg allocation
and reset retain `soft_limit = PAGE_COUNTER_MAX`
(`mm/memcontrol-v1.h:78–81`). Unlike the old writable field, this interface no
longer installs a finite soft-limit policy. This is a real v1 policy/ABI behavior
change, also documented in `Documentation/admin-guide/cgroup-v1/memory.rst:705`.
It can change which groups reclaim preferentially; no new wait, lock cycle or
unbounded loop is introduced by these handlers. No evidence ties a lost soft
limit policy to host-wide progress failure in this incident.

The no-MEMCG_V1 `memcg1_oom_prepare()` stub now initializes `*locked=false`.
That stub is outside the ordinary MEMCG_V1=y recipe. It removes use of an
uninitialized result rather than demonstrating a reachable new v1 failure.

### CSS and socket ownership

The upstream `kernel/cgroup/cgroup.c` change initializes BPF revision counters;
the audited CSS get/put helpers, task-CSS acquisition and rstat core have no
upstream delta. The downstream memory-view helper and its balanced file
ownership remain as established in [memory-audit.md](memory-audit.md).

The socket changes (`184f87f256ecd11af9f77ad51063ae0dab6239ea` and
`cce9dbd1ea56891bdb7b28ef58f879d4f11f4089`) introduce the accessor/inheritance
helper used by MPTCP. Final `mm/memcontrol.c:4907–4928` leaves equal old/new
memcgs untouched; otherwise it drops the child's old reference, gets the
parent socket's memcg reference, and installs the new pointer. The parent
socket already owns that reference. Final `net/mptcp/subflow.c` invokes it
under the socket-accounting enable gate, including configurations without
SOCK_CGROUP_DATA. No unmatched reference operation was found in this changed
inheritance path.

`8efa34c2f0562b0c3b154a69cd0b36d30e2b19f8` converts socket pressure to a
64-bit timestamp. The new seqlock exists only on BITS_PER_LONG<64
(`include/linux/memcontrol.h:1685–1707`), not the x86_64 node source target.
The 64-bit path uses READ_ONCE/WRITE_ONCE. In v1,
`mem_cgroup_under_socket_pressure()` still returns the legacy `tcpmem_pressure`
value before the hierarchical timestamp walk (`:1720–1729`). A new 32-bit
seqlock stall is therefore not a supported mechanism for this node.

## New serialization: explicit lock/progress checks

### Shrinker-info teardown

`b9a280a9a454ed514636351d53fe2a233dc5054b` serializes teardown with expansion.
The previous failure chain was concurrent publication/expansion and unlocked
free of a partially initialized shrinker-info array, allowing UAF/double free.
The incident source uses these paths:

- `free_shrinker_info()` takes `shrinker_mutex` and calls the internal cleanup
  (`mm/shrinker.c:62–83`).
- `alloc_shrinker_info()` already holds that mutex; its failure exit calls
  `__free_shrinker_info()` directly, then unlocks (`:86–112`). It does not
  recursively call the locking wrapper.
- Expansion is serialized by the same mutex and iterates memcgs without
  acquiring `cgroup_mutex` (`:159–187`). Its existing GFP_KERNEL allocations
  under that mutex are not newly introduced by this patch.

`mem_cgroup_css_online():3682–3723` calls allocation and handles its failure;
the normal source does not leave a partially published array for unlocked
teardown. Nokmem alone is not a reason to skip analysis: shrinker-info
allocation is still called. No new reverse lock dependency or recursive mutex
acquisition was found in these inspected paths. The former race is repaired
in the incident code; its occurrence on the old kernel is not claimed.

### Vmalloc purge mutex

`c15ff206ba78820bf2873d0c668a882e99f4b631` adds
`vmap_purge_lock` to `vmap_node_shrink_scan()` (`mm/vmalloc.c:5250–5259`),
serializing `decay_va_pool_node()` with purge callers.

The global shrinker walker takes a shrinker reference and **drops RCU before**
the sleepable scan callback (`mm/shrinker.c:660–679`); the newly acquired mutex
does not make that callback wait inside this RCU read-side section.
In the inspected normal paths, the order is purge mutex followed by a short
pool spinlock section; `decay_va_pool_node():2188–2238` releases the pool lock
before merging into the global free tree. Tree merging frees vmap-area metadata,
without allocating a new vmap range. The purge worker
(`:2268–2300`) processes metadata and uses the pool/global-free locks, without
reacquiring the purge mutex. Thus the caller's `flush_work()` under that mutex
(`:2354–2379`) does not supply a worker→same-mutex dependency in these paths.
No complete wait cycle was found. This is not an assertion that arbitrary
instrumentation or an unrelated stuck CPU cannot stop a TLB flush.

The additional huge-vmap page-table protection uses
`mmap_read_trylock(&init_mm)` in the PMD/PUD/P4D replacement paths
(`mm/vmalloc.c:134,204,269`). Failure falls back instead of blocking on that
rwsem, and the acquired read lock is released on both success and failure.
No new blocking init_mm rwsem inversion was found there.

The provenance owner also checked that old v6's cumulative source patch
already contains the purge-mutex addition: old backport
`3fed23dbf00ab8b562eeb0f971212bbc8b168e16` and the new stable commit share
upstream `ec05f51f1e65bce95528543eb73fda56fd201d94`. Source presence is not
proof of the module actually loaded on node24, but this prevents treating it
as unconditionally new at the `.95.6`→`.113` runtime boundary.

## Reclaim and swap progress

`b5391676c61d94ffe3272dcf6723738b802f79e8` replaces `cond_resched()` with
`cond_resched_tasks_rcu_qs()` at the classic-LRU scan-loop scheduling point
(`mm/vmscan.c:5764`). Under full preemption, involuntary scheduling is not
itself a Tasks-RCU quiescent state. The helper explicitly reports that state
then calls `cond_resched()` (`include/linux/rcupdate.h:246–256`); it does not
wait for a grace period or add a mutex. The known missing-QS reclaim-stall
mechanism described by this fix is corrected in the incident source.

`a7c322137515a0ad9194ab3b1356822fb457366e` accounts dirty MGLRU file folios
and wakes flushers when the considered file set is entirely unqueued dirty
data (`mm/vmscan.c:4808–4843`). It resets per-pass statistics in the MGLRU
root-reclaim branch. The wakeup flushes the current block plug, then traverses
writeback objects and posts work; `WB_start_all` prevents duplicate pending
work (`fs/fs-writeback.c:1316–1334,2418–2453`). It does not wait for dirty-page
writeback completion. No new cycle with filesystem completion was demonstrated.
This branch also depends on MGLRU being built/enabled; the ordinary recipe
is source-inferred to have it off. A tenant-local premature OOM repaired by
this change would not by itself demonstrate host exhaustion.

The two swap scheduling changes (`60cbe67d1342f34b66df1c2ee328e3cd333767d7`
and `c8f2fe6439dc986e1f0956bca7c3e05e49690a6c`) leave one scheduling point
**before reacquiring** `si->lock` in the final loop
(`mm/swapfile.c:745–790`). The lock is dropped at line 763 and reacquired at
776. The final source does not call that new `cond_resched()` with this
spinlock held. `lookup_swap_cgroup_id()` now handles a missing map before
dereference (`mm/swap_cgroup.c:162–172`); `__swap_duplicate()` rejects an absent
swap device. Bad-entry diagnostics are rate-limited. These repairs do not
establish a new corrupted swap entry or an incident trigger.

Other reviewed progress changes include a Tasks-RCU report outside `cgwb_lock`
in offline-writeback cleanup, zswap's reschedule on a missing shrink candidate,
and compaction checking `free_pages_prepare()` before reusing a freed folio.
No newly introduced nonterminating continuation or lock inversion was found
in these final deltas.

## Slab and selected THP/rmap adjacency

`3e71bfbdd3fd81ee9fefd867fdb2be62bade4140` addresses a real historical
host-failure mechanism: slab object-extension arrays could form allocation
cycles across kmalloc sizes and recurse through free until stack overflow.
The final source routes extensions of ordinary kmalloc caches through
`KMALLOC_NO_OBJ_EXT` (`mm/slub.c:1994–2011`, `mm/slab.h:417–427`). When needed,
those caches are created with `SLAB_NO_OBJ_EXT | SLAB_NO_MERGE`
(`mm/slab_common.c:943–948`). The decision includes profiling support that is
not permanently disabled, not merely its current enable state
(`mm/slab.h:564–580`). This breaks the specific extension-cycle mechanism
rather than leaving it uncorrected in `.113`.

The companion sentinel-bit change is paired with exact-sentinel handling;
`slab_obj_exts()` masks flag bits to obtain a pointer (`mm/slab.h:593–606`),
and free clears a no-pointer sentinel (`mm/slub.c:2072–2088`). The intermediate
reset change and its revert were checked against the final source rather than
counted as two retained effects. Other slab changes inspected are aliasing,
zeroing, initialization/error cleanup and sysfs/debugfs registration. The new
fine-grained local-lock lockdep classes are PREEMPT_RT-gated; `preempt=full`
does not enable them. No supported new recursion or runtime lock cycle was
found. Incident profiling/debug state remains qualified by packaging evidence.

Selected THP/rmap checks covered:

- Huge-zero publication/reclamation uses one short `huge_zero_lock` critical
  section, with folio allocation and put outside it
  (`mm/huge_memory.c:199–293`). Provenance also finds this change in old v6
  source (`22fa8d08569ef23605a3c717fc828b861cf5eff9`, upstream
  `33192a26cddea7a7e4ca66e5c3eebd36fa8be2bb`); actual historical loading is
  unresolved.
- The split path switches active memcg before xarray allocation, restores it
  on the common exits (`:3487–3646`), and drops the mapping lock while the head
  still pins the inode, before releasing after-split folios. The inspected
  success and error exits retain the corresponding unlock/restore operations.
  Nokmem further limits the intended new kmem-charging effect.
- `anon_vma` publication is release-ordered (`mm/rmap.c:217`); the chain helper
  split retains interval-tree insertion under the write lock. The included
  barrier fix repairs the old partially initialized-root lock/UAF mechanism.
  The stable adaptation does not introduce the full upstream two-pass clone
  allocation rewrite. Tmpfs huge-order selection changes add no wait or lock.

These checks do not constitute an exhaustive hugetlb, device-memory, pagewalk,
NUMA hotplug or every THP workload audit.

## Remaining limits and next discriminator

The inventory owner reports no locally retained post-`.113` stable release;
no later-release known-fix source was fetched. Historical fixes discussed above
were verified where they appear in the actual selected range or retained old
backport source. A known bug's description is not evidence that its trigger
occurred on node24.

One redundant intermediate socket-commit patch read encountered missing
promisor objects and was stopped without lazy fetching. The complete final
old/new socket-helper diff and final incident code were readable and reviewed;
that intermediate history limitation does not substitute for a missing final
source check. The provenance owner retains object-materialization ownership.

No candidate from this audit has the source-proven failure chain needed to
justify an isolated experiment yet. A captured all-CPU/blocked-task stack,
vmcore or allocator/reclaim trace from the failure is needed to select a more
specific mechanism. Exact incident config, historical livepatch identity and
pressure/writeback telemetry would refine reachability; their absence must
remain explicit. No proposed collection or recovery operation has been run.
The reporting arithmetic defect from the custom phase remains separate from
this upstream result and remains unattributed to the host hang.
