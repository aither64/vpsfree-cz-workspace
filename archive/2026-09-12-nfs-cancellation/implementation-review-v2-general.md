# General change review, second pass

Reviewed the final committed revision ranges from
`implementation-review-packet-v2.md`:

- `vpsadminos` `15802517e2d92dda4ddc07ebac3d1d7ea087b430..5e586fbf6dea837849630b376442ed12607a32b1`
- retained Linux 6.12.95 `563bbb35e8753e1bb34dad19ebeec8962ee3c1cd..e232e2bdcc9a552b60b49ab8994bd49b115e1e58`
- default Linux 6.12.109 `9ccd5d6597a6ddbe5b44fb885ddf96e4dbc332dd..c099b00eafe7ced993eb6a7166876bb12bef8c72`

I inspected the final three-commit OS series, its relevant tests and
documentation, both final saved kernel diffs and source context, and the
first-round reports and reconciliation. The history is clean, the commit
messages follow the repository rules, and the final kernel lifetime fix no
longer has the child/parent embedded-kobject ownership defect reported in the
first pass.

## Blocking

### 1. The console completion barrier still disappears during a daemon-restart window

Commit `ba14101abb0c1cb9a4b32c67b7d88e340b5bdc33` obtains the exit-promise
token only when the current in-memory run configuration has an `init_pid`
(`osctld/lib/osctld/commands/container/stop.rb:55-62`). If it is nil, the
command skips the barrier and proceeds directly from the stop result to
accounting-cgroup removal and possible synchronous ephemeral deletion
(`stop.rb:87-107`). `Console#handle_ct_stop` is still the sole fulfiller, and
fulfils only after aborted-run recovery, writeback remounting, and temporary
run-dataset disposal (`osctld/lib/osctld/console/console.rb:108-149`).

`init_pid` is deliberately transient: every loaded `RunConfiguration` starts
with it nil, and neither `dump` nor `load_conf` persists it
(`osctld/lib/osctld/container/run_configuration.rb:34-43,174-223`). During pool
load, `ct.fresh_state` records only LXC's state, `Monitor::Master.monitor(ct)`
starts a background thread, and tty0 is reconnected immediately for a running
container (`osctld/lib/osctld/pool.rb:693-705`). The monitor fills `init_pid`
later in that background thread (`osctld/lib/osctld/monitor/master.rb:33-50,
91-105,132-142`). A management request can therefore stop a reloaded running
container after the pool becomes active but before that update. A reloaded
container already in `stopping` is even stronger: it is not considered
`running`, so tty0 is not reconnected and `init_pid` remains nil.

In either case the new forced-stop path can return success without proving that
the old run's console/writeback cleanup completed, and the direct-stop path can
delete an ephemeral container while that cleanup is absent or still running.
This is the restart form of the completion requirement, not a repeat of the
resolved ordinary-path finding: the added regressions always make `init_pid`
non-nil whenever they supply a promise
(`osctld/spec/osctld/commands/container/lifecycle_spec.rb:369-375,603-626`), so
they do not cover the transient state that bypasses the fix.

Acquire the completion token from the existence/identity of the active run,
not from the volatile init PID. If a restarted stopping run has no console path
that can fulfil it, complete an idempotent synchronous equivalent within the
same deadline or fail closed. Add restart regressions for both a running run
before monitor PID refresh and a stopping run after init has departed; neither
may report success, prune accounting state, or delete an ephemeral container
before old-run completion is established.

### 2. Daemon and sidecar locks can exceed the advertised 60-second forced-stop budget

The absolute deadline now correctly bounds `Process.spawn` children, pipe I/O,
and child reaping, but it does not bound the parent-side synchronization around
them. `ForcedStop#run` starts its 60-second clock and immediately calls
`prepare` (`osctld/lib/osctld/container/forced_stop.rb:27-32`). `prepare` calls
`NfsCancellation#capture` and then `#abort`; capture acquires an ordinary Ruby
mutex and performs sidecar publication, while abort acquires the same mutex and
persists terminal intent before reaching its bounded `Thread#join`
(`osctld/lib/osctld/container/nfs_cancellation.rb:42-73,82-110`). Sidecar
publication and updates use a blocking `flock(File::LOCK_EX)` with no timeout
(`osctld/lib/osctld/container/nfs_cancellation_state.rb:60-77,91-99,171-176`).
A stale/stopped worker or another daemon process holding that lock can therefore
prevent the requested kill from being attempted at all, beyond both the
five-second head start and the full forced-stop deadline.

The same gap exists after killing. `Recovery#recover_state` checks the deadline
only before entering recovery and forwards it only to external commands
(`osctld/lib/osctld/container/recovery.rb:19-45,208-219`).
`ct.netifs.take_down` first enters `Lockable` state and each veth operation takes
more `Lockable` state (`osctld/lib/osctld/net_interface/manager.rb:64-69` and
`osctld/lib/osctld/net_interface/veth.rb:190-220`). These locks can wait for the
fixed 90-second `Lockable::Lock::TIMEOUT`, already longer than the complete
forced-stop budget (`osctld/lib/osctld/lockable.rb:27-30,44-71,118-165`).
`ct.stopped` then destroys the run configuration, whose cancellation `close`
again enters an unbounded mutex and sidecar `flock`
(`osctld/lib/osctld/container/nfs_cancellation.rb:128-138`).

The real-command recovery regression holds a veth lock for only 0.05 seconds
under a two-second deadline, and the forced-stop specs replace recovery and
cancellation with nonblocking doubles
(`osctld/spec/osctld/container/recovery_spec.rb:80-118` and
`osctld/spec/osctld/container/forced_stop_spec.rb:15-48`). They prove the new
process boundary preserves parent state, but not that the boundary is bounded.
This contradicts the plan and the user documentation, which promise one
60-second forced phase and say cancellation failures do not prevent killing
(`docs/containers/administration.md:127-138`).

Make every wait reachable in forced preparation/recovery deadline-aware. In
particular, failure or contention in namespace-state capture/persistence must
stop consuming the head start and allow killing to proceed, and daemon-state
lock acquisition must fail within the remaining absolute deadline. Add focused
tests with the sidecar lock and a parent-owned `Lockable` held past the supplied
deadline, proving that killing is still attempted and the command returns or
fails closed within the single budget.

## Important

None beyond the blocking findings above.

## Advisory

None.

## Residual validation gaps

- Neither final kernel head has been built or booted. The repaired normal and
  diagnostic kernels, both NFS VM instances, cgroup-v1/v2 legacy cases, and
  exact/mismatched/historical livepatch lifecycles remain unvalidated at
  runtime.
- Actual NFSv4 migration and transport-replacement execution remains absent.
  The source changes preserve the original sysfs namespace across migration,
  but current diagnostics stress initialization and destruction rather than
  that replacement path.
- No regression covers forced stop immediately after daemon restart while
  `RunConfiguration#init_pid` is still nil, or a restart after init departure
  with an old run still awaiting finalization.
- No regression holds a cancellation-state `flock` or daemon `Lockable` beyond
  the forced-stop deadline. Current command tests cover pipe pressure, EOF,
  child exit, and direct-child reaping only.
