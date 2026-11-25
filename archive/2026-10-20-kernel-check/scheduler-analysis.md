# Fake-affinity scheduler analysis

## Result

The fake-affinity mask intersection is **excluded as a newly introduced custom
code change** between the .95 boot source and the incident .113 source. Its
patch changes only its subject between those stacks. The complete syscall
source and custom helper source are byte-identical at both final revisions.
There is no source-supported hang candidate from this patch.

This conclusion is narrower than certifying the scheduler: upstream scheduler
code changes exist, and unchanged custom code can interact with other changes.
No such interaction or incident stack has been established by this check.

## Exact comparison

| Item | Old | Incident |
| --- | --- | --- |
| Final Linux revision | `a2384967b90f24d2470c9eb15f0e66d938df7e08` | `1dfea587406b7dd79973831d1677fb2418e5e9aa` |
| Mask-intersection owner | `b9c9c0ed09699ad89751b21459c8abf99550a84e` | `b7609ccb76dabcb146356ea4c318715d1e9332bf` |
| `kernel/sched/syscalls.c` blob | `3c93c4aeabc6c1ed727d2da82a2e6e72ae475333` | Same |
| `kernel/vpsadminos.c` blob | `062ad3f5617ddea097566d69b46006ce452aa003` | Same |
| `include/linux/vpsadminos.h` blob | `74b3b19ac0a7c1bf339df69cf557476a546e3d30` | Same |

`git range-diff b9c9c0ed^! b7609ccb^!` reports only this message difference:

```text
- sched: intersect vpsadminos fake affinity masks
+ [vpsAdminOS] sched: intersect fake affinity masks
```

The complete final-tree diff for all three files is empty. These checks used
`repos/linux.git` read-only; no branch, ref, index or source edits were made.

## Source behavior and reachability

All line references below are to incident commit
`1dfea587406b7dd79973831d1677fb2418e5e9aa`; the same lines and contents occur
at the old final revision.

- `kernel/sched/syscalls.c:1267` acquires a task reference through
  `CLASS(find_get_task, p)`. At lines 1274–1290 the custom branch applies to
  callers outside the initial cgroup namespace when `fake_online_cpumask()`
  returns a nonempty virtual mask. It intersects the requested mask with
  that mask, rejects an empty intersection, stores the fake mask and returns.
- That branch returns before the normal `__sched_setaffinity()` call at line
  1322. Its mask-intersection change does not migrate the target task or call
  the real affinity setter.
- `kernel/vpsadminos.c:153` derives the virtual CPU count from the target
  task's cgroup namespace and CPU quota hierarchy. It uses RCU, the task lock,
  namespace references and online cgroup references, and walks upward through
  parents. The mask helpers at lines 228, 250 and 263 use this count and store
  or report `fake_cpu_mask`.
- `kernel/sched/syscalls.c:1363` reads affinity; it takes the task's `pi_lock`
  and uses the fake mask when available. This entire path and the helper
  locking are unchanged across the two final source revisions.

The behavioral motivation in both owner commits is accepting a broad,
intersecting userspace CPU mask, including crun's affinity reset, instead of
requiring the request to be a strict subset of visible virtual CPUs. That
behavior was already in the old .95 source.

## Verification and limits

Completed quick checks:

1. Read both owner commit messages and file statistics.
2. Compared the two owner patches with `git range-diff`.
3. Compared complete final source blobs and an empty file diff.
4. Traced the caller, early-return path and immediate custom helpers.

No runtime reproduction or kernel build was needed to prove source identity.
The old incident predecessor was reported as 6.12.95.6 and therefore also has a
livepatch overlay; its exact effective source is tracked separately in the
inventory/packaging lanes. The identity result above expressly compares the
.95 boot source with the .113 native source.
