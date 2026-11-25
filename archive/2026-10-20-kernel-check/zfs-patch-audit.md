# ZFS free-accounting patch audit

## Outcome

**Not supported as a newly introduced hang or as the node24 incident cause.**
The patch removes a concrete, conditional dbuf/hash lock cycle from the
unpatched source. Its accounting reads use existing holds and syncing ownership;
the pointer updates that readers must not observe partially remain locked.
The inspected callers do not demonstrate a new deadlock, use-after-free,
concurrent writer, double accounting, or nonterminating loop introduced by the
split. This is a bounded source result, not a certification of all ZFS paths.
There is no incident stack, dump or reproduction tying the patch to the hang.

Source confidence is high for the removed lock-order edge. Confidence in the
negative regression conclusion is limited to the inspected helpers, callers and
normal ownership rules below. Incident attribution remains unsupported.

No source, refs, build products, runtime settings, services or production
workloads were changed. No builds or tests were run. Canonical repository reads
used `GIT_NO_LAZY_FETCH=1`; all necessary source blobs were already available.

## Exact versions and packaging boundary

- Incident OS: `2abbe3cc1c102a4b39022d3f73ef4a432ad4d616`.
- ZFS source in both retained 6.12.95 and incident 6.12.113 tuples:
  `481845fca6ae3f61ca2262c1a5693a58ae364650`.
- Additional OS patch:
  `os/packages/zfs/zfs235-free-account.patch`, introduced by
  `9bca43d32a84d0f76e2e497f68840143fa9bbbab`, unchanged through the incident OS.
  Both revisions contain patch blob
  `9cfc5041877462bcad0be25f89f06e66d904af74`. The base `dnode_sync.c` blob is
  `713c62417a85e7d4b5e2e216cece18aad6f6da1f`, matching the patch's old index.
- At the incident OS, `os/packages/linux/available-kernels.nix:47` selects the
  patch for 6.12.113 (`patches` at line 53); the 6.12.95 tuple at line 80 has
  the same ZFS source and no additional patch list.
- Builtin-source preparation forwards that list at
  `os/packages/linux/packages.nix:66` (assignment at line 76). The external
  `configFile = "kernel"` branch also forwards it at
  `os/modules/config/kernel.nix:39` (assignment at line 49). The shared ZFS
  derivation uses `patches = extraPatches`.

The latter recipe change is commit
`358cd303ca236957054e6cc110c52a050a4ce448`, **already an ancestor of the exact
incident OS**: `git log 2abbe3cc -- os/modules/config/kernel.nix` lists it before
the older changes, and the exact incident file contains the assignment. This
corrects a reported chronology discrepancy; it does not attest loaded module
bytes. Implementer4 owns actual mode/configuration/provider and runtime identity
reconciliation. The conclusions about patch semantics are independent of that
runtime result. Nor does an unpatched .95 boot recipe establish the effective
old .95.6 livepatch state.

Immutable entry points:
[OS patch](https://github.com/vpsfreecz/vpsadminos/blob/2abbe3cc1c102a4b39022d3f73ef4a432ad4d616/os/packages/zfs/zfs235-free-account.patch),
[ZFS source](https://github.com/vpsfreecz/zfs/tree/481845fca6ae3f61ca2262c1a5693a58ae364650).
All ZFS line references below use that source **before** the additional patch;
patch references use the 96-line patch file at the incident OS.

## What changes

Original `dnode_sync.c:136` implements one `free_blocks()` loop: for every
non-hole BP it calls `dsl_dataset_block_kill(..., B_FALSE)`, retains hole-birth
metadata, and zeroes/publishes the BP as a hole. It then applies the cumulative
`dnode_diduse_space()` decrement.

The patch separates this into a read/accounting pass and a hole-publication
pass, keeping each non-hole accounted once and decrementing dnode space once:

| Path | Before | After |
| --- | --- | --- |
| Level-one indirect range, `free_children()` (`dnode_sync.c:406`, patch lines 73–96) | Hold original `db_mtx` and writer `db_rwlock` across accounting and hole publication | Account first; acquire the same mutex/writer lock for hole publication; decrement space after unlocking |
| Final indirect BP, `free_children_free_indirect()` (`dnode_sync.c:350`, patch lines 59–70) | Hold parent writer lock across accounting and BP clearing | Account first; retain parent writer lock around BP clearing; decrement after unlocking |
| Direct dnode/spill BPs (`dnode_sync.c:474`, `:901`, patch lines 50–57) | Interleave accounting and holes in one pass | Run two passes under the same syncing owner; no new lock or reference drop |

The new helper asserts syncing context and takes a `const blkptr_t *`. Hole
birth/type/size preservation is unchanged. Neither pass adds a retry or waits
for a condition newly dependent on hole publication.

## Concrete cycle removed

Let **A** be the indirect dbuf being freed, **M** its `db_mtx`, and **H** a dbuf
hash mutex. Hash locks are selected by a masked index
(`include/sys/dbuf.h:326`), so distinct dbufs can share H.

1. The unpatched syncing worker acquires M and A's writer `db_rwlock` in
   `free_children()` (`dnode_sync.c:410–416`). While retaining them it calls
   `free_blocks()` → `dsl_dataset_block_kill(..., async = B_FALSE)`.
2. A BP still referenced by a snapshot takes the synchronous deadlist branch
   (`dsl_dataset.c:330–343`). `dsl_deadlist_insert()` can load metadata and
   enqueue a BP (`dsl_deadlist.c:464–502`). For example, `bpobj_enqueue()` on a
   cache miss calls `dmu_buf_hold()` (`bpobj.c:911–918`), which reaches
   `dbuf_hold()`/`dbuf_hold_impl()`/`dbuf_find()` (`dmu.c:197–219`, `:243–251`;
   `dbuf.c:4062–4063`). That lookup needs H.
3. Concurrently, a lookup of A enters `dbuf_find()`. It first acquires H, then
   waits for M **without releasing H** (`dbuf.c:354–359`).
4. If that H is the mutex needed by the worker's nested lookup, the worker
   waits on H while owning M; the lookup thread waits on M while owning H.

Thus the conditional prepatch cycle is **worker: M → H; lookup: H → M**. It
requires the relevant freeing/accounting path, a nested metadata lookup and
the shared hash mutex at the overlapping schedule; a generic delete alone does
not prove those conditions. The deadlist snapshot condition is one concrete
reachable route, not a claim that it is the only accounting route.

After the patch, the accounting call runs before `free_children()` acquires M
or its writer lock. The accounting worker therefore does not retain the M
needed by the concurrent lookup. The later publication critical section only
examines/clears BPs; it does not call deadlist/accounting lookup. It removes this
specific cycle. The final-indirect helper similarly stops retaining its parent
writer lock over potentially blocking accounting.

This proves a defect in the **unpatched source under the stated schedule** and
a removed dependency in the patched path. It is not evidence of a new defect
in .113, nor proof that the old .95.6 runtime exercised the old path.

## Why the unlocked reads do not establish a new race

The generic dbuf declaration says `db_data` is protected by `db_mtx`
(`include/sys/dbuf.h:199–203`). The patch relies on a narrower, checkable case:
it reads held indirect buffers in syncing context before starting their writes.
The inspected source supports that ownership exception:

- **Dbuf and backing buffer lifetime:** `dnode_sync_free_range_impl()` obtains
  a dbuf hold before `free_children()` and releases it afterward
  (`dnode_sync.c:487–492`). Recursive calls do the same for every child
  (`:425–431`). `dbuf_hold_impl()` increments `db_holds` (`dbuf.c:4141`);
  destruction requires zero holds (`:3335–3346`), and normal final release
  evicts only at zero (`:4300`). The new helper releases none of these holds.
  Child dbufs also hold their indirect parents (`dbuf.c:3629–3630`).
- **No normal open-context indirect data replacement:** range freeing only
  processes level-zero dbufs (`dbuf.c:2051`), and the COW clear path
  `dbuf_fix_old_data()` requires level zero (`:1723–1726`). ARC buffer
  assignment requires level zero (`:3252–3254`). Data-block resizing obtains a
  level-zero dbuf (`dnode.c:2003–2005`); the other resize caller is a spill
  buffer (`dbuf.c:4182–4194`). Dirtying indirects changes dirty records and
  explicitly notes that indirect contents are only modified while syncing
  (`dbuf.c:2413–2419`, `:2428–2432`). A reference alone would not prove safety
  for arbitrary level-zero data; this argument is specific to indirects.
- **Same-dnode writes have not started:** `dnode_sync()` processes frees at
  `dnode_sync.c:907–938`, before indirection increase (`:949`) and before
  `dbuf_sync_list()` (`:992`). The indirect write path sets pending data and
  starts its write/children only in `dbuf_sync_indirect()`
  (`dbuf.c:4649–4661`). BP publication by `dbuf_write_ready()` happens later
  under the parent writer lock (`:5159–5161`). The current dnode is removed
  from its dirty sublist before syncing (`dmu_objset.c:1593–1604`), and dataset
  sync waits for root I/O (`dsl_pool.c:713–723`). The TXG sync thread calls
  `spa_sync()` serially before advancing the synced TXG (`txg.c:589–608`).
- **Readers still see protected updates:** clearing an indirect's BP array
  retains both original locks; clearing its parent BP retains the original
  parent writer lock. Accounting does not modify the inspected BP, and no
  competing writer to that BP was identified before these writes start.
- **Space accounting:** `dnode_diduse_space()` retains its own `dn_mtx`
  (`dnode.c:2593–2609`). The same accumulated byte total is applied once,
  before recursive freeing completes and before `dnode_sync_free()` verifies
  zero space (`dnode_sync.c:704–711`). The split creates a temporary interval
  between accounting and hole publication; it does not demonstrate duplicate
  freeing or lost accounting because the BP owner does not change in it.

No error path in the split drops the hold and continues with the BP pointer.
Both scans are bounded by the existing validated free range. These checks
reject the simple claim that moving outside `db_mtx` necessarily causes
eviction/UAF, and the simple claim that open-context file writers can replace
these indirect BPs during accounting. They do not exclude an unrelated
ownership bug elsewhere in ZFS.

## Rationale and provenance limits

The introducing OS commit explicitly describes this hash/dbuf inversion and
the use of syncing ownership. It reports native style checks and an isolated
four-CPU comparison completing twelve fallocate release-delay cases with hash
collisions amplified. Those are **historical claims in the commit message**;
this audit did not run or independently inspect those experiments.

The existing ZFS locking lineage includes
`e25d939ee039f3fc9cc24b279a8d3604244caf76` ("Be more careful with locking around
db.db_data") and `fb85c957fd04c414d655038c8674a9de87682ebd` (bounded child-ID
snapshots). Both precede the common ZFS source used by the two kernel tuples.
Their existence does not by itself prove a .95-to-.113 regression.

No upstream origin/fix is cited by `9bca43d3`. A bounded primary GitHub commit
metadata search in `openzfs/zfs` for `free_blocks_account`, `free accounting`,
`free_blocks deadlock`, `deadlist hash` and the older locking subject found no
corresponding accounting-split repair; hits concerned different mechanisms.
That is a provenance search limit, not proof that no upstream discussion or
equivalent change exists. No unrelated upstream fix was adopted as a candidate.

## Incident relevance and remaining evidence

[Central logs](log-evidence.md) show the deployed OS boot identity, then loss
of logging at October 20 18:58:26 CEST and recovery boot at 19:12:04. They have
no ZFS/dbuf lock stack or I/O fault tying this path to the incident. Adjacent
tenant NFS timeouts do not establish this local ZFS cycle. Even a demonstrated
pool-sync deadlock would need a separate progress chain to explain every
reported host symptom.

Attribution would require a matching thread/lock dump showing the actual
accounting and competing owners on the deployed code, or a discriminating
old/new and patch/revert reproduction under a concrete candidate schedule.
No such candidate survives this bounded audit, so no test/build is proposed or
started merely to seek a generic pass. Any newly identified competing indirect
writer should be referred to the architect before expanding verification.

As a small supplementary log query for packaging, adjacent October 19 boot
records are `log-20261020:215495` input `nixpkgs=26f4107e`, `:215496` input
`vpsadmin=ff730be4`, `:215497` input `vpsadminos=2abbe3cc`. The bounded
`:215450–215530` range contains no configuration-revision input. Implementer4
received these facts separately. No further broad log scan was performed.
