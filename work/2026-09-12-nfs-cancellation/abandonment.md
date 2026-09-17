# Abandoned NFS cancellation repair

Abandoned on 2026-09-17 at the user's request. No default-branch integration or
production deployment occurred. The development session remains open, with
branches and source worktrees preserved.

## Retained revisions

| Worktree | Local head | Remote feature head at abandonment |
| --- | --- | --- |
| vpsadminos | 18332a06dda48702d0421eff8d9dc31fdd298b85 | af42c679c5a91aa2b5b0158f24d1a8b4ffcb00cf |
| linux | 7c66ab3c284a5fb5b615f874a99cb16501d6de23 | Same as local |
| linux-6-12-95 | a2bdcc5b5067dcb7b8f36ef955cd6ee29c9c215a | Same as local |

All three worktrees have no tracked modifications. The OS branch still pins
6090ca00 for 6.12.95, a candidate with the reproduced migration crash. The final
95 provider correction was committed and reviewed, but its archive could not
be fetched and hashed. These branches are unfinished and must not be treated
as release-ready.

## Verification preserved

- Focused daemon/library tests and legacy 6.12.48 cgroup v1/v2 compatibility tests
  passed, including ordinary/frozen kills after osctld restart.
- All 44 protocol examples passed on the preceding 6.12.109 candidate across NFS 3,
  4.0, 4.1 and 4.2. Its migration example failed on unsupported BusyBox readlink
  syntax before triggering migration.
- Focused probes then exposed our RPC sysfs refresh regression on both kernels.
  The fix restores sysfs setup through its owning RPC registration helper and
  guards optional allocation. Focused reviews and object compilation passed.
- The corrected 6.12.109 normal and diagnostic kernel/system builds and external-ZFS
  fixture subsequently completed. Corrected-head migration and cancellation
  runtime validation did not run.
- Historical AMD/Intel livepatch lifecycle tests passed. The rebuilt livepatch
  and identity tests for the final corrected 6.12.95 base remain unverified.
- CI run 34701121709 finished with failure. No branch CI is still running.

See [runtime-validation.md](runtime-validation.md) and the review reconciliation.
Small supporting logs and the first crash traces are retained in evidence/.
Original scratch paths in historical records were removed during cleanup.

## Cleanup performed

Removed 15 recorded disposable VM directories, the scratch/build trees and Nix
output roots, and generated .native, .gems and result directories in the OS
worktree. Stopped one stale read-only review search. Builds and VMs had already
finished. Shared Nix store entries were not deleted and global garbage
collection was not run. Exact removed paths are in cleanup-record.json.

No further work or delayed cleanup is scheduled. Source worktrees, local and
remote branches, review reports and reusable development notes remain intact.
