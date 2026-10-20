# Targeted upstream scheduler, RCU and locking audit

Status: source audit complete. No source-supported new host-progress failure
chain was established in this bounded lane. No reproducer, kernel build,
runtime change or production action was performed.

## Exact scope and method

The stable comparison is
`296aabce459470a4c1b68ffd0c0c0920e563aaad` (6.12.95) to
`7fdb7c1824a1f9979d648d7ae28ac446bcee9c6e` (6.12.113). Final behavior was
checked in incident Linux `1dfea587406b7dd79973831d1677fb2418e5e9aa`.
The old runtime reported 6.12.95.6 and included a livepatch overlay; these
stable boundaries describe source changes, not a claim that every change was
new relative to that effective runtime. See [provenance](upstream-provenance.md).

The path-limited log contains 33 commits, with a final diff across 17 files:
`kernel/sched/`, `kernel/rcu/`, `kernel/locking/`, and
`kernel/cgroup/{cgroup,namespace,cpuset,rstat}.c`. The final diff and selected
caller/error paths were inspected, including downstream affinity, load-average
and cgroup intersections. This is targeted source analysis, not verification
of all 7,278 stable-window commits or all possible scheduler executions.

Reads used `GIT_NO_LAZY_FETCH=1` against the canonical bare repository.
Object retrieval remained the inventory owner's responsibility. Reproduce
the scope with:

```sh
GIT_NO_LAZY_FETCH=1 git --git-dir=repos/linux.git log --format='%H %s' \
  296aabce459470a4c1b68ffd0c0c0920e563aaad..7fdb7c1824a1f9979d648d7ae28ac446bcee9c6e \
  -- kernel/sched kernel/rcu kernel/locking kernel/cgroup/cgroup.c \
  kernel/cgroup/namespace.c kernel/cgroup/cpuset.c kernel/cgroup/rstat.c
```

All line references below refer to the incident tree unless stated otherwise.

## Progress-sensitive changes

| Change | Source result | Applicability and limit |
| --- | --- | --- |
| Core scheduling in-flight guard, `3e2511bffa93a639774a99e392181e21d28677e2` (upstream `f3629c63a4af3e491381780bc6c123cb498c4c40`) | `kernel/sched/core.c:390–434`, especially 411–415, drops sibling runqueue locks and restores IRQ flags while waiting for in-flight selection. `pick_next_task()` returns for disabled/offline cases before incrementing at 6111; both fast paths reach the common decrement at 6307, before the normal return at 6312. Hotplug transfers the count at 6508 and clears the old leader at 6509. No leaked count or lock-held waiting cycle was demonstrated. | Requires core scheduling. Source-inferred recipe has `SCHED_CORE=n`; exact incident binary config was not recovered. Inspection does not prove starvation impossible under every hypothetical enabled workload. |
| Previous-task/donor change, `81ebe9ddd972988fc11ffe57b6aa58e19203b972` (upstream `7a3a6bfbd62a2ba3e0ef1e92d6b71abb66890825`) | This backport aliases `donor` and `curr` in a union; it does not introduce proxy execution. `__schedule()` takes `prev=rq->curr` at core.c:6654, selects at 6710 and publishes `next` only at 6724. The current donor remains on-CPU across the balancing lock drops. The unchanged custom load-average hooks do not expose a new reference ownership mismatch here. | No source-proven new progress failure was found. |
| RT mutex wake queues, `fb45361ffc4812a92345db58acc65548ca524fd0` | The changed `kernel/locking/rtmutex.c` path drains `wake_q` after releasing `wait_lock`, before possible scheduling; preemption stays disabled until the pending wakes complete. | Repairs the delayed-wakeup dependency described by the patch; no replacement wait cycle found. Ordinary PI paths remain relevant even on non-RT kernels. |
| Futex scheduling helpers, `9309e22a088a8b2e8ae5f7a0a6c3991e69fd346b` | New pre/post helpers bracket `rt_mutex_wait_proxy_lock()` scheduling without `sched_submit_work()`; the old surrounding brackets are removed from `futex_lock_pi()`. This avoids work-submission/PI recursion rather than introducing a new submission dependency. | No new lock cycle demonstrated through the inspected caller. |
| RT spin unlock lifetime, `1f0d56d3f1e88f20f6e46109402f8c15d59bac37` | `kernel/locking/spinlock_rt.c` keeps RCU protection until unlocking, fixing the premature lifetime release. | Requires PREEMPT_RT, source-inferred disabled. Observed `preempt=full`/PREEMPT_DYNAMIC does not mean PREEMPT_RT. |
| RT push IPI default, `89237c8fc15d8016a194076e648ccb57d75e65ae` (upstream `dd29c017aed628076e915fe4cdfb5392fd4c5cab`) | `kernel/sched/features.h` defaults `RT_PUSH_IPI` off for non-RT. This contains the repair for a reported heavy-networking RT-push IPI livelock. | The fixed problem cannot be presented as an introduced regression merely because its description resembles a hang. No incident evidence establishes a relevant feature override. |
| RCU flags and boot wake, `5615fe34fd658c7314626b057ed9888298c0b8bb`, `d09cf80011809a3552f30d9f98c03182e7ce459d` | The first marks urgent/heavy quiescent-state flag accesses with READ/WRITE_ONCE; the second supplies a boot callback wakeup. Neither adds a blocking operation or grace-period dependency. | No new deadlock chain found in the two changed RCU paths. This does not exclude RCU stalls caused elsewhere. |
| PSI timer teardown, `806fcff98c1d7cb3c1dc0015e55ebdbe819e6b08` | `psi_cgroup_free()` changes to `timer_shutdown_sync()`. | PSI is explicitly disabled in the configured recipe, so this new wait is excluded within that source-config boundary. |

## Other changes and downstream intersections

The fair-scheduler changes widen runnable arithmetic, adjust CPU-util
subtraction placement, filter statistics by allowed CPUs and change
asymmetric-capacity/misfit selection. The inspected changes add no new
blocking operation or lock order. The boot's `nosmt` and homogeneous EPYC
evidence further narrow the asymmetric-SMT case; neither is a generic
scheduler correctness proof.

The schedutil changes initialize all per-CPU state before publishing hooks,
widen the rate-limit multiplication and correct a comment. Deadline changes
bound the revised wakeup rule to a running deadline server, reject debugfs
writes for offline CPUs and stop the server before changing its parameters.
The fork-policy change restores timer slack when resetting RT policy. No new
host-wide dependency was demonstrated in these final changes.

Cpuset changes separate temporary-mask allocation and safely roll back
successful allocations, make deadline task accounting atomic, rebind memory
policy to effective memory nodes, and change remote-partition hierarchy
updates. Remote-partition masks are published before recursive hierarchy
iteration; the hotplug mode check is moved inside `cpuset_mutex`. No complete
reverse lock dependency or lifetime failure was established. Source selects
hybrid/v1 cgroups, but runtime mount flags and partition operations are not
fully observed; v1 with `cpuset_v2_mode` must not be silently equated with
legacy semantics.

The two sched_ext changes use a per-task sequence counter and fix the
core-scheduling comparator direction. They are excluded by the
source-inferred `SCHED_CLASS_EXT=n` recipe. Lockdep changes invalidate stale
class-cache entries and guard a NULL class pointer. `PROVE_LOCKING=n` is known;
this is not a claim that every possible LOCKDEP selector is disabled.
The cgroup BPF revision field is initialization/bookkeeping, with no new wait
in the inspected cgroup path.

The incident custom diff retains load-average hooks around
`ttwu_do_activate()` and `__block_task()`, custom helper definitions later in
`core.c`, and cgroup namespace/rstat additions. Inspection of their immediate
upstream intersections did not find a new lock, wait or lifetime dependency.
The complete fake-affinity syscall file and its custom helpers are
byte-identical between the old and incident custom trees, as documented in
[scheduler-analysis.md](scheduler-analysis.md). That identity alone would
not exclude an upstream interaction; the intersection checks above address
the selected changed paths separately.

Config exclusions are **source-inferred recipe facts**, corroborated by the
initial .113 config and unchanged Kconfig/build recipes, not an attestation
of recovered incident config bytes. See [packaging-audit.md](packaging-audit.md).

## Conclusion and verification boundary

This lane establishes no new source failure chain that explains node24's
host-wide unresponsiveness, inability to forward diagnostics, or missing crash
upload. It does not prove that scheduling, RCU or locking remained healthy
during the incident. The VGA cursor can continue blinking without scheduler
progress; missing watchdog output cannot supply an absent stack.

No generic stress test or source change is justified as verification of an
unidentified mechanism. Discriminating evidence would be a stalled CPU/task
stack, NMI/IP context, held locks and waiters, or a repeatable operation tied
to an enabled changed path. A proposed reproduction would then need exact
old/new or fix/revert controls and an observable matching failure signature.
The printk/panic intersection and platform/watchdog policy are separate
owners' packages; see [upstream-printk-audit.md](upstream-printk-audit.md) and
[packaging-audit.md](packaging-audit.md).
