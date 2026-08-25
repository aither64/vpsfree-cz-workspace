# 2026-08-24-crashdump-optimization

## Goal

Reduce synchronous crash-kernel inspection time without dropping any existing
report, and measure the improvement on a reproducible high-task-count VM
workload. Report payloads must stream directly to their destination; the crash
kernel must not stage them in tmpfs.

## Status

Superseded on 2026-08-25 at the user's request by the colleague's solution in
vpsAdminOS commit `b0e1a4dee54efda0075904b31d6b87e003aaa41b`. Stop this
implementation, do not merge or push its rewritten branches, and retain the
plan and local branches only as historical validation material.

## Affected repository

- `vpsadminos`: collector, local crash patches, streaming helper, and routine
  regression tests on the merge branch. The output-equivalence test, legacy
  collector, and benchmark remain on a separate validation branch.

No production configuration or deployment pin is in scope.

## Implementation

- Run all reports through one initialized crash session, with `ps -m` last so
  its task-array sort cannot affect another report.
- Stream each report directly through one fixed 256 KiB writer. Keep only the
  command file, raw timings, and internal completion markers in `/tmp`; report
  payloads must never be staged there.
- Collect crash essentials first, in this order: panic-task backtrace, kernel
  log, system/time/memory summary, non-idle active CPU backtraces, all active
  CPU backtraces, and uninterruptible-task backtraces.
- Call `syncfs(2)` on the final priority report and atomically publish the
  destination-side `priority-complete` marker only after the sync succeeds.
  This also flushes an earlier dmesg file on the same filesystem.
- Collect supplementary reports afterward, in this order: active-process
  summary, process-state summary, complete process list, interruptible-task
  backtraces, and `ps -m`. Keep the caller's final `sync` for the complete
  collection.
- Keep local crash 9.0.1 patches to skip inactive-task memory reads in `ps -A`,
  cache last-run timestamps before the `ps -m` sort, and wait for input-file
  pipeline children between commands.
- Preserve all eleven report names and the existing status format. Add one
  session log, phase/report timings, and collector metadata.
- Keep `--no_kmem_cache` only if normalized reports from the same vmcore match
  the legacy collector.

## Compatibility and deployment

The change adds artifacts but does not remove or rename existing reports.
Crashdump data is not loaded by a running node, so old and new dumps coexist
and mixed node versions are safe. There is no state migration or coordinated
rollout requirement. Rollback restores the former collector with no data
conversion. Collector metadata version 3 and `priority-complete` are additive;
older automation can ignore them. No coordinated node update is required.

## Validation

- Package checks cover streaming beyond the buffer, append mode, timing and
  completion markers, and write failure.
- Routine inspection creates 512 interruptible sleepers and verifies every
  report, one crash initialization, timing completeness, and sleeper evidence.
- NFS inspection observes `priority-complete` on the server while supplementary
  collection is still running, verifies all priority files and the earlier
  dmesg, then verifies final status, sync, and reboot.
- On `2026-08-24-crashdump-optimization-validation`, a manual equivalence test
  runs both collectors on the same vmcore and diffs all normalized report
  payloads.
- Six manual benchmark cases run three fresh legacy and three fresh optimized
  4-vCPU, 8-GiB VMs with 2 GiB reserved for the crash kernel, NFS output, and
  5,000 sleepers. Record medians for collector-plus-sync, panic-to-priority,
  and panic-to-shutdown in the final functional commit message.

The previous report order measured 337.230 seconds legacy versus 106.860
seconds optimized for collector plus sync, and 430.011 seconds versus 254.620
seconds from panic to shutdown. Rerun all six cases because the new ordering
and intermediate durability barrier change optimized timing.
