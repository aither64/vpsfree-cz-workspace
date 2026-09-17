# Scope and proportionality review, second pass

Reviewed the final committed ranges from
`implementation-review-packet-v2.md`:

- `vpsadminos` `15802517e2d92dda4ddc07ebac3d1d7ea087b430..5e586fbf6dea837849630b376442ed12607a32b1`
- retained Linux 6.12.95 `563bbb35e8753e1bb34dad19ebeec8962ee3c1cd..e232e2bdcc9a552b60b49ab8994bd49b115e1e58`
- default Linux 6.12.109 `9ccd5d6597a6ddbe5b44fb885ddf96e4dbc332dd..c099b00eafe7ced993eb6a7166876bb12bef8c72`

I inspected the committed OS series, first-round findings and reconciliation,
the saved final kernel diffs, and the focused tests around the changed
process/deadline and completion boundaries. Uncommitted remediation that
appeared in the shared OS worktree during this review is outside these exact
heads and is not assessed here.

## Blocking

### 1. The run-completion barrier is still narrowed by volatile init PID state

The remediation in `ba14101abb0c1cb9a4b32c67b7d88e340b5bdc33` restores the
console exit-promise wait after forced stopping, but the command obtains that
promise only when `run_conf.init_pid` is non-nil
(`osctld/lib/osctld/commands/container/stop.rb:55-62`). When it is nil, the
command can proceed from successful stop/termination checks to accounting
cgroup removal and synchronous ephemeral deletion without any completion
barrier (`stop.rb:87-107`).

That condition is narrower than the accepted restart contract. Every loaded
`RunConfiguration` starts with `@init_pid = nil`, and the PID is absent from
its persisted representation
(`osctld/lib/osctld/container/run_configuration.rb:34-43,174-186`). Pool load
starts the monitor asynchronously after refreshing LXC state
(`osctld/lib/osctld/pool.rb:693-705`), while the monitor populates the PID only
later in its worker thread
(`osctld/lib/osctld/monitor/master.rb:91-105,132-142`). A stop can therefore
arrive for a restored running run before PID refresh. A restored stopping run
whose init already departed also keeps the live run configuration but has no
PID from which this condition can recover.

The completion barrier protects console/writeback and temporary-run-dataset
cleanup, so this is inside the explicit requirement to avoid reporting stop or
deleting ephemeral data before old-run completion. The new lifecycle examples
do not cover the missing boundary: their promise-bearing fixture also supplies
a non-nil init PID
(`osctld/spec/osctld/commands/container/lifecycle_spec.rb:369-375,603-626`).

Make completion depend on the existing run identity/configuration rather than
the transient PID. If no console path can fulfil a restored run's token, perform
the existing cleanup synchronously within the remaining deadline or fail
closed. This does not require a new durable promise framework: a run-owned token
plus focused restart tests for pre-refresh `running` and post-init `stopping`
states is the smallest credible contract.

### 2. The deadline abstraction bounds child commands but not the forced-stop operation

`Container::ForcedStop` starts its one 60-second clock before `prepare`, then
calls namespace capture and terminal cancellation before it attempts the LXC
kill (`osctld/lib/osctld/container/forced_stop.rb:27-32,70-82`). Capture and
abort enter an ordinary Ruby mutex, and abort persists terminal intent while
holding it
(`osctld/lib/osctld/container/nfs_cancellation.rb:42-73,82-110`). The state
writer then takes a blocking cross-process `flock` with no deadline
(`osctld/lib/osctld/container/nfs_cancellation_state.rb:91-99,171-176`). A
paused or stuck holder can therefore consume the head start and the complete
budget before the requested kill is attempted, despite cancellation being an
optional best-effort prelude.

The changed parent-side recovery has the same boundary mismatch. It checks the
deadline between operations and passes it to external commands, but
`ct.netifs.take_down` enters the manager and veth `Lockable` locks before those
commands, and `ct.stopped` later takes the container lock
(`osctld/lib/osctld/container/recovery.rb:19-40`,
`osctld/lib/osctld/net_interface/manager.rb:64-69`,
`osctld/lib/osctld/net_interface/veth.rb:190-200`, and
`osctld/lib/osctld/container.rb:391-398`). `Lockable` has a fixed 90-second
acquisition timeout and accepts no caller budget
(`osctld/lib/osctld/lockable.rb:28-30,44-71,118-165`). Thus a recovery beginning
at the reserved 50-second boundary can wait beyond the advertised 60 seconds
before it reaches any deadline-aware command or reports failure. The real
recovery regression holds a veth lock for only 0.05 seconds under a two-second
deadline, while the forced-stop specs replace both recovery and cancellation
with nonblocking doubles
(`osctld/spec/osctld/container/recovery_spec.rb:80-131` and
`osctld/spec/osctld/container/forced_stop_spec.rb:15-48`).

This directly contradicts the accepted single-budget contract and the user
documentation at `docs/containers/administration.md:127-133`. Keep the fix
narrow: cancellation-state contention must expire within its five-second share
and still reach killing, while only locks on the forced recovery path need to
honor the remaining absolute deadline and fail closed. Threading the existing
deadline through those waits would be a bounded correction and would not need
another scope-review rerun.

## Important

None beyond the blocking findings above.

## Advisory

### 3. Deadline cleanup changes the legacy no-deadline EOF path

The new `ContainerControl::Frontend#read_fork_result` keeps the old blocking
wait after a valid response when no deadline is supplied, but its `EOFError`
branch now returns directly and lets the common `ensure` call
`terminate_runner(pid)`
(`osctld/lib/osctld/container_control/frontend.rb:219-239,262-268`). Before this
commit, the no-response branch called `Process.wait(pid)` and allowed the runner
to finish. The new behavior can kill a still-running runner that closed its
result descriptor while unwinding or completing its operation. It applies to
ordinary `fork_runner` consumers such as GetHostname, VethName, WithMountns,
WithRootfs, and non-forced stop, although only forced stop and deadline-bound
state queries require kill-on-timeout behavior.

Preserve the previous EOF wait when `deadline` is nil and keep termination for
the bounded branch. A focused child test that closes the result pipe before a
delayed normal exit is enough; this narrow compatibility correction does not
need a reviewer rerun.

## Proportionality assessment and residual test gaps

The new `libosctl` absolute-deadline command path is otherwise proportionate.
Recovery currently needs both shell and argv forms, and `SystemCommand` covers
the existing option shape while testing concurrent stdin/stdout pressure,
output EOF, child exit, and nonblocking reap. Callers without `deadline` retain
the old `syscmd`/`syscmd_argv` implementation. Keeping daemon objects and state
transitions in osctld while spawning only explicit external commands resolves
the rejected forked-callback design without adding another generic host runner.

The first-round scope findings are resolved: diagnostic kernels run only the
fault-injection/lifetime stress, cancellation-capable versions are owned by the
kernel registry, and unrelated `flake.nix` changes no longer trigger the full
kernel workflow. The retained-kernel lifetime repair and default-kernel full
cancellation port remain tied to the requested exact versions and ABI; no
superseded compatibility fallback or extra kernel variant remains.

Residual validation gaps:

- Neither exact kernel head has completed a build or boot in the evidence
  available to this review; compilation was running, and no VM integration had
  started.
- Actual NFSv4 migration and SUNRPC transport-replacement runtime coverage is
  still absent.
- No committed regression covers completion immediately after daemon restart
  with a nil init PID, a cancellation-state lock held through the head start, or
  a parent `Lockable` held beyond the forced-stop deadline.
- The real recovery test exercises the veth external-command path, but stubs
  route discovery and disables AppArmor. No VM test has yet exercised the real
  console writeback/run-dataset completion barrier or its timeout race.
