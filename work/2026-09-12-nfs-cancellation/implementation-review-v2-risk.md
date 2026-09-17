# Risk and compatibility review, second pass

Reviewed the final committed revision ranges from
`implementation-review-packet-v2.md`:

- `vpsadminos` `15802517e2d92dda4ddc07ebac3d1d7ea087b430..5e586fbf6dea837849630b376442ed12607a32b1`
- retained Linux 6.12.95 `563bbb35e8753e1bb34dad19ebeec8962ee3c1cd..e232e2bdcc9a552b60b49ab8994bd49b115e1e58`
- default Linux 6.12.109 `9ccd5d6597a6ddbe5b44fb885ddf96e4dbc332dd..c099b00eafe7ced993eb6a7166876bb12bef8c72`

I inspected the final OS series, the first-round findings and reconciliation,
the final kernel sources and saved diffs, and the focused remediation tests.
The rejected forked-Recovery design is absent: daemon state, hooks, events and
ownership decisions now remain in osctld, while only explicit commands cross
the `Process.spawn` boundary. The two findings below concern behavior newly
exposed by that final boundary and an unhandled restart case; they do not repeat
the resolved child-process state-loss finding.

## Blocking

### 1. A daemon restart can still remove the console completion barrier from a forced stop

Commit `ba14101abb0c1cb9a4b32c67b7d88e340b5bdc33` obtains an exit-promise
token only when `run_conf.init_pid` is non-nil
(`osctld/lib/osctld/commands/container/stop.rb:55-62`). When it is nil, a
successful stop proceeds directly to accounting-cgroup removal and may
synchronously delete an ephemeral container (`stop.rb:87-107`). The promise is
the only barrier for `Console#handle_ct_stop`, which fulfils it after aborted-run
cleanup, dataset writeback, temporary run-dataset destruction and related
old-run effects (`osctld/lib/osctld/console/console.rb:108-149`).

`init_pid` is transient across daemon restart. `RunConfiguration` initializes
it to nil and does not include it in `dump` or restore it from `config.yml`
(`osctld/lib/osctld/container/run_configuration.rb:34-43,174-223`). During
pool import, `ct.fresh_state` records only the returned LXC state. The pool then
starts `Monitor::Master` asynchronously, reconnects tty0 for a running
container, and publishes the container in `DB::Containers`
(`osctld/lib/osctld/pool.rb:693-705`). The monitor fills `init_pid` later in
its worker thread (`osctld/lib/osctld/monitor/master.rb:91-105,132-142`). A
stop request can therefore find a restored running container after DB
publication but before the PID refresh and skip the barrier. A restored run
already in `stopping` is stronger evidence: pool import does not reconnect tty0
because the run is not `running`, and state refresh has no live init PID to
store.

In both cases forced stopping can report success and permit cleanup or deletion
without proving the old run's writeback and dataset effects completed. In the
stopping case there may be no reconnected console which can perform them at
all. This leaves the first-round data-safety requirement unsatisfied for the
explicit restart/init-departure compatibility boundary.

Acquire the completion token based on the active run identity rather than the
volatile init PID. When a restored stopping run has no console that can fulfil
the token, perform an idempotent synchronous equivalent within the same
absolute deadline or fail closed. Add regressions for a restored running run
before monitor PID refresh and a restored stopping run after init departure;
neither may prune accounting state, delete an ephemeral container, or return
success before old-run completion is established.

### 2. Cancellation and parent-state locks can prevent killing or exceed the forced-stop deadline

The new `SystemCommand` correctly bounds direct-child pipe I/O, exit waiting,
killing and reaping with an absolute monotonic deadline. That deadline does not
cover all synchronization which precedes and surrounds those commands.

`ForcedStop#run` starts its 60-second clock and calls `prepare` before invoking
the LXC stop callback (`osctld/lib/osctld/container/forced_stop.rb:27-32,
70-82`). `prepare` enters `NfsCancellation#capture` and `#abort`; those methods
take an ordinary Ruby mutex and persist state before the bounded worker join
(`osctld/lib/osctld/container/nfs_cancellation.rb:42-73,82-110`). Sidecar
pinning, updates, retirement and cleanup use a blocking
`flock(File::LOCK_EX)` with no deadline
(`osctld/lib/osctld/container/nfs_cancellation_state.rb:60-77,91-99,
115-145,171-176`). Contention or a wedged holder can therefore consume more
than the five-second cancellation head start, or wait indefinitely, before the
requested kill is attempted. The rescue which intentionally treats
cancellation as optional cannot run until lock acquisition returns.

After LXC/recovery killing, `Recovery#recover_state` forwards the deadline only
to external commands (`osctld/lib/osctld/container/recovery.rb:19-45,
208-220`). `NetInterface::Manager#take_down`, `Veth#is_created?`/`#down`, and
`Container#stopped` first acquire daemon `Lockable` state
(`osctld/lib/osctld/net_interface/manager.rb:64-69`,
`osctld/lib/osctld/net_interface/veth.rb:190-223`, and
`osctld/lib/osctld/container.rb:391-398`). `Lockable::Lock::TIMEOUT` is 90
seconds and its acquisition methods accept no caller deadline
(`osctld/lib/osctld/lockable.rb:29,44-71,118-165`). Recovery normally starts
near the reserved 50-second boundary, so one contended lock can make the
advertised 60-second operation take roughly 140 seconds before failing. A
failure can overrun again while `ForcedStop` assigns `ct.state = :error`.

This is distinct from the resolved fork bug: the owner is now a valid live
daemon thread, but the parent wait still does not participate in the one
forced-stop budget. It is both a bounded-operation defect and, on the
pre-kill sidecar path, a way for optional cancellation to prevent the required
kill. The remediation test holds the veth lock for only 50 ms under a
two-second deadline (`osctld/spec/osctld/container/recovery_spec.rb:80-131`),
while forced-stop tests replace cancellation and recovery with nonblocking
doubles.

Make every lock acquisition reachable from forced preparation, recovery and
failure reporting honor the earliest absolute monotonic deadline. Cancellation
lock contention must consume at most its head-start allowance and then allow
killing to proceed. Keep release/cleanup `ensure` paths unconditional; avoid
asynchronous exception injection into critical sections. Add focused tests
which hold the sidecar lock and representative daemon locks beyond the supplied
deadline, proving both that the kill callback is still attempted and that the
operation fails closed within its single budget.

## Important

None beyond the blocking findings above.

## Advisory

None.

## Compatibility assessment and residual test gaps

- The final kernel allocation-order remediation is source-consistent in both
  branches. The child netns kobject owns one explicit parent reference until
  its release callback, while the ordinary hierarchy reference is dropped by
  `kobject_del`; failed child publication is balanced by the child cleanup and
  the remaining parent put. The server sysfs object separately retains
  `sysfs_net` until its deferred release. No new reference imbalance was found.
- New userspace re-probes only `shutdown_tree`; an older or not-yet-loaded
  kernel therefore skips cancellation and still reaches ordinary killing. New
  kernels remain dormant for old userspace. Rollback to an old daemon still
  loses terminal-intent recovery and can retain sidecar namespace pins until
  later reconciliation or reboot, as already accepted in the plan.
- Neither final kernel has been built or booted. KASAN, lockdep, fault-injected
  initialization, delayed kobject release, concurrent sysfs access and
  mount/unmount lifetime stress remain required on both diagnostic kernels.
- The repaired 6.12.95 livepatch has not been built, loaded or exercised
  against exact, mismatched and historical boot images. Sequential source
  patch application and Nix evaluation do not validate module ABI or runtime
  image/note guards.
- The normal repaired-kernel NFS VMs and old-kernel cgroup-v1/v2 forced-stop
  VMs have not run. Native mocks do not validate real namespace bind mounts,
  LXC transitions, cgroup membership or console/writeback ordering.
- Actual NFSv4 migration and SUNRPC transport-replacement runtime coverage is
  absent. Source inspection shows the server sysfs object retains its original
  network namespace, but does not prove the migration and cancellation lock
  paths under load.
- Deadline-provider tests cover direct child I/O, exit, kill and detach. The
  recovery integration test exercises one spawned veth command with AppArmor
  disabled and RouteList stubbed; real AppArmor/route timeouts and descendant
  processes inheriting command pipes remain untested.
