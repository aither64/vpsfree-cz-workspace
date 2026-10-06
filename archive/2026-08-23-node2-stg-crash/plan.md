# 2026-08-23-node2-stg-crash

## Goal

Determine why `node2.stg.vpsfree.cz` became unresponsive before its manual
reset on 2026-08-23 and establish how to identify a container responsible for
large host-wide `Committed_AS`, process, thread, and file-table growth.

## Affected repositories

None. This is a read-only production/staging incident investigation using
central syslog, Munin, and local source/configuration checkouts as reference.

## Approach

- Correlate the supplied Munin interval with central logs from
  `log.int.prg.vpsfree.cz`.
- Attribute blocked or stalled tasks using the memory-cgroup paths present in
  kernel diagnostics.
- Cross-check process, thread, file-table, memory, load, and CPU graphs.
- Determine which per-container cgroup counters are inexpensive enough for
  incident use and how to approximate virtual commit when necessary.

## Compatibility and deployment

No code, schema, protocol, state-format, or deployment change is planned.
There are no mixed-version or rollback concerns for this investigation.

## Testing plan

- Verify the reset boundary from the first kernel message of the new boot.
- Count blocked task names, PIDs, cgroup attribution, and watchdog messages.
- Check logs for OOM kills, kernel panics, hardware errors, and I/O errors.
- Compare log attribution with independent Munin maxima and timing.
