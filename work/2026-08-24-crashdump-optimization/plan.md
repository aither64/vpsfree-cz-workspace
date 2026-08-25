# 2026-08-24-crashdump-optimization

## Goal

Reduce synchronous crash-kernel inspection time without dropping any existing
report, and measure the improvement on a reproducible high-task-count VM
workload. Report payloads must stream directly to their destination; the crash
kernel must not stage them in tmpfs.

## Affected repository

- `vpsadminos`: collector, local crash patches, streaming helper, regression
  tests, output-equivalence test, and benchmark.

No production configuration or deployment pin is in scope.

## Implementation

- Run all reports through one initialized crash session, with `ps -m` last so
  its task-array sort cannot affect another report.
- Stream each report directly through one fixed 256 KiB writer. Keep only the
  command file, raw timings, and completion markers in `/tmp`; retain the
  caller's single final `sync` for durability.
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
conversion.

## Validation

- Package checks cover streaming beyond the buffer, append mode, timing and
  completion markers, and write failure.
- Routine inspection creates 512 interruptible sleepers and verifies every
  report, one crash initialization, timing completeness, and sleeper evidence.
- NFS inspection verifies direct output, status, telemetry, sync, and reboot.
- A manual equivalence test runs both collectors on the same vmcore and diffs
  all normalized report payloads.
- Six manual benchmark cases run three fresh legacy and three fresh optimized
  4-vCPU, 8-GiB VMs with 2 GiB reserved for the crash kernel, NFS output, and
  5,000 sleepers. Record medians for collector-plus-sync and panic-to-reboot in
  the final functional commit message.

The accepted three-run medians are 337.230 seconds legacy versus 106.860
seconds optimized for collector plus sync (68.3% less, 3.16x faster), and
430.011 seconds versus 254.620 seconds from panic to shutdown (40.8% less,
1.69x faster).
