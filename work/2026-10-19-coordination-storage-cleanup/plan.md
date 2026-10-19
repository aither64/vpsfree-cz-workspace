# Automatic coordination storage cleanup

## Goal and authorization

The user requested renewed disk attribution, then instructed that workspace
snapshots and coordination checkouts must be cleaned automatically. They then
explicitly allowed tracking this session. Implementation and review are in scope;
repository master integration still requires explicit direction. No unrelated
session, cluster, VM disk or KB data may be removed manually.

## Scope and evidence

Owning project: dev-workspace. Extend its existing periodic coordination collector
rather than add a separate scheduler. At 09:32 CEST October 19 the filesystem was
95% full with 50 GiB available. Since October 17: workspace Nix source snapshots
40.7 -> 83.0 GiB; coordination 39.8 -> 80.1 GiB; feature worktrees 48.7 -> 64.7 GiB;
session records 3.5 -> 14.5 GiB. KB verification remains absent; test images fell
96.3 -> 80.8 GiB. Broad snapshots repeatedly include about 2.5 GiB of archives.
Existing documentation explicitly excludes integration scratch and owner-keyed
notification roots from collection. Profile generations also retain old packages.

## Approach

Use the design in design.md. Reuse lifecycle/profile admission, integration locks,
Git worktree removal, reference marking, process checks and periodic GC dispatch.
Add completed integration scratch and stopped worker roots to that collector.
Bound workspace profile history while preserving selected/recent generations and
live recovery dependencies. Keep compact journals, receipts, feature refs, source
revisions and user worktrees. Do not erase Git history or delete Nix store paths.

## Compatibility and deployment

No SQL/API/protocol migration. Preserve current ledger and preparation formats.
Integration GC recovery bookkeeping is additive in mutable integration journals;
older readers preserve/ignore the optional field. Existing pending source GC
format remains unchanged. Profile pruning removes rollback choices, but normal
workspace package rollback is already unsupported; current plus predecessor and
live recovery packages remain. Software rollback cannot resurrect removed
scratch data. Final deployment must use the ordinary coordinated user profile
and matching configuration contract; deployment is not master integration.

## Verification and documentation

Focused Ruby GC tests cover live references, active workers/drivers, partial
removal, changed/unknown worktrees, pending delivery, profile boundaries and
idempotence. Run quick checks before committed whole-branch independent review;
use a fresh catalog Luna watcher for longer checks/builds. Update the owning
coordination operations guide; keep compact execution evidence here.
