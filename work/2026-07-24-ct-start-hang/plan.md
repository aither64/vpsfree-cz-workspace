# 2026-07-24-ct-start-hang

## Goal

Find and fix the osctld lifecycle race that left an external `ct start`
waiting indefinitely when it overlapped a reboot requested from inside the
container.

## Affected repositories

- `vpsadminos`: osctld container start/reboot coordination and regression
  coverage.

## Approach

- Correlate the supplied node log and `osctl debug threads ls` screenshots.
- Trace container state, run-configuration, console stop, reboot, and
  manipulation-lock ownership.
- Treat a stopped container with unfinished run cleanup as not yet startable.
  Wait for the previous run's exit promise without holding the manipulation
  lock, then reacquire the lock and retry the normal start path.
- Mark managed starts as pending in memory before launching their wrapper.
  Bind the console listener and attach a reserved client before a wrapper can
  exist, then pass the listener descriptor to the wrapper. Have the wrapper
  report the exact event at which its PTY child is ready, without a deadline or
  process termination policy. Keep client input disabled until that event while
  observing EOF from the start.
- Join a replacement run which the queued reboot has already begun instead of
  launching another wrapper or waiting for that replacement run to exit.
- Reconstruct the in-memory pending marker from a live console socket when
  osctld reconnects after restart. Retain the existing run-configuration file
  until exact-generation console cleanup completes. A connectable prebound
  listener identifies a surviving wrapper; an unconnectable stale listener
  authoritatively resumes cleanup. Do not add a persisted lifecycle barrier
  that cannot be reconciled.
- Associate console connections and EOF cleanup with the exact run
  configuration. This prevents a late EOF from an old wrapper from cleaning up
  a replacement run.
- Persist only the reboot intent in the existing runtime file so daemon restart
  during retained stop cleanup still performs the requested reboot.
- Make exit promises persistent so cleanup completion cannot be missed between
  inspecting the run configuration and subscribing to it.
- Preserve existing wait semantics: `--wait infinity` remains unbounded, while
  finite cleanup and RUNNING waits share the caller's existing deadline. The
  wrapper readiness handoff is event-driven and unbounded because it must not
  be abandoned while a live wrapper may still establish the console socket.
  `wait: false` skips old-run cleanup and RUNNING waits, but still completes
  this exact wrapper handoff, as it completed console handoff before the change.
- Retry temporary descriptor and thread-allocation failures with bounded
  backoff but no lifecycle cutoff. During daemon shutdown, leave the retained
  runtime file and listener identity for the next daemon to reconcile.
- Add focused unit coverage for wrapper readiness, the in-memory lifecycle
  marker, persistent promise, lock-release/retry sequence, no-wait behavior,
  replacement-run joining, and the reentrant lock guard.
- Run osctld unit tests and the relevant vpsAdminOS integration test.
- Run the mandatory fresh-context change review after committing and quick
  verification, before the longer integration test.

## Compatibility and deployment

- No API, database, or persistent container configuration changes are
  introduced. The transient runtime file gains an optional `reboot` boolean;
  old readers ignore it and new readers default it to false when absent.
- osctld and its packaged `ctptywrapper` gain internal listener and readiness
  descriptors. They are deployed together in one vpsAdminOS system generation;
  the wrapper remains backward-compatible when either descriptor is absent.
- The fix must be safe during a rolling vpsAdminOS update: old and new nodes do
  not exchange lifecycle state, so mixed versions require no coordination.
- Existing clients keep the same `ct start` and in-container reboot behavior.
- Rollback requires no state conversion, but it is not lifecycle-safe while a
  container is in the retained stopped or pre-readiness window. An older daemon
  ignores the optional reboot flag and cannot reconstruct the new in-memory
  pending barrier, so it can re-enter the original overwrite/orphan race.
  Before rolling a node back, let its starts, stops, and reboots settle. For an
  emergency rollback caught in this window, roll that node forward again to
  reconcile the retained runtime; use manual state recovery only after
  verifying that no wrapper still owns the console listener.
- No coordinated update of all nodes is required.

## Testing plan

- Run the focused osctld RSpec regression.
- Run the affected osctld specs, including console and monitor coverage that
  requires a test-only LXC load stub in the generic development shell.
- Run the repository hook suite before committing.
- Run the existing `osctl/ct-console` RSpec-style vpsAdminOS test to verify
  normal start, stop, console, and daemon-restart behavior.
