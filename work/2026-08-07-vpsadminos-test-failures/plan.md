# 2026-08-07-vpsadminos-test-failures

## Goal

Prevent the test-runner from exhausting host memory when automatic scheduling
starts many QEMU machines, and make externally terminated QEMU processes
diagnosable and safe to clean up.

## Affected repositories

- `vpsadminos`: test-runner resource scheduling and OSVM machine lifecycle.
- `vpsadminos-org-configuration`: previously inspected for context; no change
  is planned.

## Approach

1. Base memory and `/dev/shm` scheduling on the smaller of assigned and
   initially available capacity, and keep that limit monotonic for the run.
2. Raise the default memory and `/dev/shm` reserves from 4 to 8 GiB while
   preserving explicit CLI and environment overrides.
3. Preserve run-alone behavior for oversized tests, but log a prominent
   warning with the requested and available resources.
4. Record QEMU terminating signals and synchronize QEMU process/reaper state so
   cleanup cannot signal a nil or reused PID.
5. Keep scheduler and OSVM changes in separate commits, run focused specs and
   hooks, obtain the mandatory standalone review, then run integration CI.

## Compatibility and deployment

The change affects only test scheduling and diagnostics. There are no protocol,
API, persisted-state, database, production-node, mixed-version, or deployment
ordering concerns. Existing resource options remain compatible and override
the new defaults. Machine logs gain additive signal fields. Rolling back the
commit restores the old scheduling behavior without data conversion.

## Testing plan

- Add resource-pool and executor specs for initial availability, cgroup
  headroom, monotonic limits, fallback behavior, overrides, and oversized-test
  warnings.
- Add OSVM specs for normal and signaled exits plus process-exit/cleanup races.
- Run focused RSpec suites in the repository Nix shells and mandatory
  Overcommit hooks.
- After the mandatory change review, run the full GitHub Actions VM suite and
  inspect test artifacts and runner memory metrics. Do not accept QEMU signal
  failures, cleanup TypeErrors, or memory approaching the previous 1.2 GiB
  low-water mark.

## Decisions

- Implement code-only mitigation; do not add a temporary runner configuration
  cap.
- Keep oversized tests running alone with a warning instead of failing fast.
- Do not add swap, automatic infrastructure retries, or broadly reduce guest
  memory as part of this fix.
