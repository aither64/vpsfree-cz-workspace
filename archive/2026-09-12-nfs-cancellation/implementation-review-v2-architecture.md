# Architecture and repetition review, second pass

Reviewed the final committed series and the remediation boundary at:

- `vpsadminos` `15802517e2d92dda4ddc07ebac3d1d7ea087b430..5e586fbf6dea837849630b376442ed12607a32b1`
- retained Linux 6.12.95 `563bbb35e8753e1bb34dad19ebeec8962ee3c1cd..e232e2bdcc9a552b60b49ab8994bd49b115e1e58`
- default Linux 6.12.109 `9ccd5d6597a6ddbe5b44fb885ddf96e4dbc332dd..c099b00eafe7ced993eb6a7166876bb12bef8c72`

I used the committed OS worktree and the packet's complete
`scratch/linux-{retained,default}-reviewed.patch` files. The first-round forked
recovery finding is resolved: daemon object mutation, hooks, events, and
ownership decisions remain in osctld, while `libosctl` crosses the process
boundary only for an explicit command through `Process.spawn`. The kernel
diagnostic set is also now owned by `available-kernels.nix` metadata and derived
by the flake, workflow matrix, and test instances.

## Blocking

None.

## Important

### 1. The forced-stop deadline does not bound parent-side synchronization

Commit `ba14101abb0c1cb9a4b32c67b7d88e340b5bdc33` correctly passes one
absolute deadline to the LXC runner and to every external command used by
`Container::Recovery` (`osctld/lib/osctld/container/forced_stop.rb:28-53` and
`osctld/lib/osctld/container/recovery.rb:208-220`). It does not, however, pass
that deadline through the daemon locks which recovery must acquire before those
commands run.

`Recovery#recover_state` calls `ct.netifs.take_down` and then `ct.stopped`
(`container/recovery.rb:19-40`). `NetInterface::Manager#take_down` acquires an
inclusive manager lock, calls `Veth#is_created?`, and `Veth#down` acquires an
exclusive interface lock before the first deadline-aware command
(`net_interface/manager.rb:64-69` and `net_interface/veth.rb:190-203`).
`Container#stopped` also acquires its own exclusive lock while retiring the run
configuration (`container.rb:391-398`). All of these use
`Lockable::Lock::TIMEOUT = 90`; its acquisition methods accept no caller
deadline and can wait the full 90 seconds (`osctld/lib/osctld/lockable.rb:29,
44-71,118-165`).

The same gap exists at the cross-process sidecar lock. Forced-stop preparation
calls `NfsCancellation#capture` and `#abort`; those paths update the sidecar,
and `ct.stopped` retires it through `RunConfiguration#destroy`. The owning
`NfsCancellationState#with_lock` always calls blocking `flock(LOCK_EX)` without
a deadline (`container/nfs_cancellation_state.rb:171-176`). A stopped or wedged
peer which still owns that file lock can therefore block forced stopping
indefinitely before LXC killing or while finalizing the stopped run.

A concrete failure is a forced stop entering recovery near its reserved
50-second boundary while another live daemon thread owns the veth lock. If that
thread releases it after the forced-stop deadline, recovery only then reaches
the external command, observes the expired deadline, and fails after more than
60 seconds. If the lock is stuck, the stop can wait 90 seconds before it can
even report failure. This does not recreate the resolved post-fork dead-owner
problem, but it is a consequence of moving recovery into the parent without
making the parent's synchronization participate in the same budget.

The remediation regression holds the veth lock for only 50 ms under a two-second
deadline (`osctld/spec/osctld/container/recovery_spec.rb:80-131`), so it proves
parent state and event ownership but cannot detect this overrun. Make the
affected manager, interface, and container lock acquisitions honor the remaining
monotonic deadline, and make the sidecar owner acquire `flock` nonblocking with
the same bounded wait. A focused regression should hold each live lock beyond
the deadline and verify that forced stopping returns an error within its budget.

A scoped `Lockable` deadline is a reasonable way to avoid adding deadline
keywords to every synchronized getter, provided nested scopes keep the earliest
absolute monotonic deadline and constrain acquisition only. Release paths in
`ensure` must remain unconditional so an expired deadline cannot strand an
already-held lock. The underlying condition waits must use the remaining
monotonic time. Failure-state reporting after expiry must also avoid a fresh
90-second `ct.state=` wait and must not mask the original stop failure. The
sidecar `flock` is outside `Lockable` and still needs an explicit bounded owner;
asynchronous `Timeout` injection would be unsafe in either path. This is a
bounded follow-up and does not require a reviewer rerun if it only applies the
existing deadline to acquisition and preserves unconditional release.

## Advisory

None.

## Architecture assessment and residual test gaps

- `Utils::System` retains legacy behavior for callers without a deadline and
  delegates the new mode to one `SystemCommand` owner. Its concurrent pipe I/O,
  child wait, kill, and detach behavior has direct provider tests. `RouteList`,
  `Veth`, and AppArmor all receive the same absolute recovery deadline; only the
  Veth path has a real spawned-command consumer test, while RouteList is stubbed
  and AppArmor is disabled in that test.
- When the command acquires the exit promise, it now consumes only the remaining
  forced-stop budget and blocks accounting cleanup and ephemeral deletion on
  timeout. The separate general review should decide the current `init_pid`
  acquisition condition for restored/processless runs. The focused lifecycle
  examples mock the promise and budget; no VM test has yet exercised real
  `Console#handle_ct_stop` writeback/run-dataset completion or its timeout race.
- The explicit parent reference held until each child netns kobject release
  balances both successful publication and failed child publication in both
  kernel diffs. This still needs the planned kernel build and diagnostic VM run
  with KASAN, lockdep, fault injection, and delayed kobject release.
- Neither final kernel has been built or booted, and the exact retained
  livepatch build/load guards remain untested. Actual NFSv4 migration and SUNRPC
  transport-replacement runtime coverage is still absent.
- The corresponding lifetime code in the two independent kernel release
  branches is necessary duplication. I found no additional `shutdown_tree`
  consumer or repeated diagnostic-version catalog that needs consolidation.
