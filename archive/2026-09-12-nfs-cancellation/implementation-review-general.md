# General change review

Reviewed the complete committed revision ranges from the packet:

- `vpsadminos`: `15802517e2d92dda4ddc07ebac3d1d7ea087b430..75e1d26df4acaea85f20c3ce2ac6ec6046fc1d5d`
- retained Linux 6.12.95: `563bbb35e8753e1bb34dad19ebeec8962ee3c1cd..fbe36622894dbc46f82e970dcae5da18d6e58c8c`
- default Linux: `9ccd5d6597a6ddbe5b44fb885ddf96e4dbc332dd..fb4ad1506c1d22ab92251b3ba167ca951d453b8e`

This review used the committed `vpsadminos` head for line references because remediation was already in progress in its worktree. I inspected the full OS diff and history, both complete kernel patches and their affected source context, the focused specs and VM scenarios, and the recorded verification results.

## Blocking

### 1. A successful forced stop bypasses the lifecycle completion barrier

`Commands::Container::Stop` creates an exit promise before stopping the container, but waits for it only when `forced_stop.started?` is false (`osctld/lib/osctld/commands/container/stop.rb:55-59,87-94`). It then immediately removes accounting cgroups and can synchronously delete an ephemeral container (`osctld/lib/osctld/commands/container/stop.rb:96-105`). The new spec explicitly requires this bypass by asserting that the promise is not waited after forced stop starts (`osctld/spec/osctld/commands/container/lifecycle_spec.rb:603-612`).

That promise is not merely a second process-exit check. `Console#handle_ct_stop` fulfils it only after stop-side effects have completed, including aborted-run recovery, CPU scheduling and hint updates, optional dataset writeback, and destruction of temporary run datasets (`osctld/lib/osctld/console/console.rb:68-99,108-133`). Commit `1187c712f4f145cad84e53e0b9b13517efdcbb34` introduced this synchronization specifically to make `Container::Stop` wait for console closure before continuing.

Every successful `ForcedStop#run` has `started? == true`, including the fast path where LXC reports success (`osctld/lib/osctld/container/forced_stop.rb:27-34`). The command can therefore return success, prune cgroups, or delete an ephemeral container while console cleanup still owns the past run configuration and its datasets. A daemon failure in that interval can also lose deferred cleanup after the caller was told the stop completed.

Keep the total operation bounded, but include console/run-configuration completion in that same deadline. Forced-stop success must not permit accounting cleanup, ephemeral deletion, or a successful reply until the exit promise has been fulfilled (or equivalent stop-side effects have synchronously completed). Add a regression test that delays `fulfil_exit` and proves the command neither reports success nor deletes/prunes early.

### 2. Termination proof can miss a live process stranded outside the freezer controller

`ForcedStop#cgroups_empty?` scans only `freezer/<container>/**/cgroup.procs` (`osctld/lib/osctld/container/forced_stop.rb:99-119`). On cgroup v1, a process can remain in a container path in one controller while no longer belonging to its freezer hierarchy. The repository already treats this as a real recovery case: `OsProcess#ct_id` checks every `/proc/<pid>/cgroup` entry because a process can remain only in some of the container's cgroups after an incorrect shutdown (`libosctl/lib/libosctl/os_process.rb:115-145`).

The other half of the predicate does not close this gap. `ContainerControl::Commands::State` uses existence of the memory cgroup only as a shortcut and otherwise returns LXC's state (`osctld/lib/osctld/container_control/commands/state.rb:12-31`). Thus LXC can report `stopped` and the freezer hierarchy can be empty while a task is still attached under another container controller. The fast path then returns success without running recovery cleanup (`osctld/lib/osctld/container/forced_stop.rb:32-34`). The only focused test models a PID in the freezer `cgroup.procs` file (`osctld/spec/osctld/container/forced_stop_spec.rb:41-53,110-119`), so it cannot detect this false-success case.

Verify absence across every supported cgroup hierarchy, or repeatedly rediscover container processes from all `/proc/<pid>/cgroup` memberships using the same ownership rules as `Recovery#kill_all`. Add a cgroup-v1 regression in which freezer is empty while another controller still contains a container process, and require forced stop to fail or continue recovery rather than report success.

## Important

None beyond the blocking findings above.

## Advisory

None.

## Residual validation gaps

- Neither kernel tree has had its final reviewed commit built. The helper programs establish ABI shape and namespace assumptions but cannot catch compilation or linkage mistakes in the kernel ports.
- The NFS cancellation VM scenarios, retained-kernel compatibility scenario, livepatch exact-match/mismatch checks, default-kernel reboot check, and diagnostic stress workflow remain unrun. These are the first end-to-end checks of the new daemon/kernel contract and should run only after the blocking lifecycle defects are repaired and the affected review lanes are rerun.
- Runtime coverage for the default-kernel NFSv4 server migration/client-replacement path remains absent. The source review found no separate defect in that port, but compile-only and ordinary mount tests would not exercise that lifetime transition.
- No focused test models forced-stop completion racing `Console#handle_ct_stop`, nor mismatched cgroup-v1 controller membership. Those gaps directly correspond to the two findings above.
