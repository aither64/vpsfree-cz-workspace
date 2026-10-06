---
lifecycle: abandoned
---
# 2026-08-23-node2-stg-crash

## Repositories

None modified. Read-only references:

- `repos/vpsfree-cz-configuration.git`
- `repos/vpsadminos.git`
- `repos/linux.git`

## Status

Investigation complete. Container `tank:29695` caused a long-running
`nix-daemon` process/thread storm. The resulting process teardown stalled MM
and RCU work and contended global cgroup operations, making new login sessions
and node management unresponsive. The node was manually reset.

## Commands run

- Converted the supplied Munin epoch interval to local CEST timestamps.
- Queried `/var/log/remote/cz.vpsfree/nodes/stg/node2/` on
  `log.int.prg.vpsfree.cz` for the 2026-08-22/23 incident window.
- Counted hung tasks by task name, unique PID, timestamp, and memory cgroup.
- Inspected representative systemd and `nix-daemon` kernel call traces.
- Checked for OOM, panic, lockup, RCU, allocation, hardware, storage, and
  watchdog messages.
- Retrieved and inspected Munin graphs for memory, processes, threads, forks,
  load, CPU, vmstat, file-table use, and inode-table use.
- Inspected vpsAdminOS `osctl` cgroup/process reporting and Linux overcommit
  accounting documentation from the local source checkouts.

## Results

- Supplied graph interval: 2026-08-21 22:35:45 through 2026-08-23 04:35:45
  CEST.
- The final sustained growth began around 2026-08-22 20:20 CEST, after several
  shorter bursts earlier that day.
- Munin maxima before monitoring stopped: approximately 210,710 processes,
  430,200 threads, 910,680 open files, 105.09 TiB `Committed_AS`, 45.40 GiB of
  page tables, and 295.53 GiB in the `apps` memory series. Normal/post-reset
  values were approximately 5,430 processes, 14,430 threads, 65,850 open files,
  and 228 GiB committed.
- The marginal ratios are consistent with roughly two threads, four open files,
  and about 0.5 GiB of accounted virtual memory per leaked worker process.
- At 04:01:15, RCU reported stalls in `nix-daemon` tasks 247099 and 246982 while
  they were tearing down address spaces through `unmap_page_range`,
  `exit_mmap`, and `do_exit`. Both belonged to container `tank:29695`, systemd
  session `c18833`, and had parent PID 3618201.
- The first hung-task report was at 04:04:17. Systemd tasks from otherwise
  unrelated containers were stuck in `cgroup_kn_lock_live`/`cgroup_mkdir`,
  showing that the incident had progressed into host-wide cgroup lock
  contention.
- Central syslog contains 95,676 hung-task reports for `nix-daemon`; 95,676 of
  95,678 attributed reports were in `tank:29695` session `c18833`. There were
  68,516 unique reported `nix-daemon` task IDs.
- `nodectld` first reported its daemon unresponsive for 90 seconds at 04:02:08
  and reached 810/900 seconds at 04:14:08.
- No pre-reset OOM kill, kernel panic, hardware error, or storage I/O error was
  found. RCU stalls and hung-task dumps explain the unusable host. The kernel
  produced millions of diagnostic lines, which likely added further pressure.
- The first new-boot kernel line arrived at 04:30:48 CEST. There was no orderly
  shutdown sequence.
- Linux exposes `Committed_AS` globally, not as a cgroup counter. `osctl ct ls`
  can cheaply report `nproc` (`pids.current`) and resident cgroup `memory`.
  Summed process VSZ is a useful, imperfect per-container culprit finder;
  scanning accountable VMAs in every `/proc/PID/smaps` is closer to commit but
  is expensive and racy and should not be attempted during a process storm.

## Open questions

- What client or automation repeatedly connected to the `nix-daemon` whose
  parent was PID 3618201 inside `tank:29695` session `c18833`?
- Did `tank:29695` lack an appropriate `pids.max`/process limit, or was its
  configured limit unexpectedly ineffective?
- Should alerting and a containment limit be added for per-container task
  growth before host-wide MM/cgroup contention begins?

## Cleanup

- No remote state was changed.
- A temporary local directory was used for downloaded Munin images and a
  transient SSH known-host entry, then removed after the investigation.

## Archival request, 2026-10-06

The workspace operator requested archival of sessions dated August 2026 or
older, retaining recorded work and branches. This checkpoint commits the
existing plan and active state before the ordinary archive transition.
