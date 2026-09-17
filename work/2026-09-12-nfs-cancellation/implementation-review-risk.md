# Risk and compatibility review

Reviewed the complete committed series and the relevant owners/consumers for:

- `vpsadminos` `15802517e2d92dda4ddc07ebac3d1d7ea087b430..75e1d26df4acaea85f20c3ce2ac6ec6046fc1d5d`
- retained Linux 6.12.95 `563bbb35e8753e1bb34dad19ebeec8962ee3c1cd..fbe36622894dbc46f82e970dcae5da18d6e58c8c`
- default Linux 6.12.109 `9ccd5d6597a6ddbe5b44fb885ddf96e4dbc332dd..fb4ad1506c1d22ab92251b3ba167ca951d453b8e`

The default-kernel review used `scratch/linux-default-final.patch` and the
committed head worktree. I also inspected the retained kernel's corresponding
source, osctld's authenticated namespace capture and persisted sidecar, forced
stop/recovery/console sequencing, old-kernel probing, kernel selection, and the
6.12.95 livepatch image/note guards.

## Blocking

### 1. The parent netns kobject can free the allocation while its child kobject is still live

Both kernel heads have byte-identical `fs/nfs/sysfs.c` files. A single
`struct nfs_netns_client` contains the parent `nfs_net_kobj` and child
`kobject`. The child release callback still derives and accesses that shared
allocation to free `identifier` (`fs/nfs/sysfs.c:123-130`), while the parent
release callback frees the complete allocation (`fs/nfs/sysfs.c:216-222`).

Destruction deletes and puts the child, then deletes and puts the parent
(`fs/nfs/sysfs.c:273-284`). `kobject_del()` drops the reference that a child
took on its parent (`lib/kobject.c:619-629`). Consequently the final child and
parent puts are independent. With `CONFIG_DEBUG_KOBJECT_RELEASE`, each final
put schedules its embedded release work with an independent random delay
(`lib/kobject.c:701-721`). The parent release can therefore free the allocation,
including the child's queued work item, before `nfs_netns_client_release()`
runs. The same underlying bug exists without the debug option whenever another
reference delays the child beyond the parent's final put.

This initiative explicitly enables `DEBUG_KOBJECT_RELEASE` in the new
diagnostic kernels (`os/configs/nfs-cancellation-debug.nix:9-20`) and exercises
netns publication/destruction. The planned diagnostic run can turn this into a
KASAN use-after-free/panic rather than validating the intended lifetime repair.
The full default-kernel port also introduces this lifetime into 6.12.109.

Keep the shared allocation alive until both embedded kobjects have completed
their release callbacks, including the failed child-publication path, or give
the kobjects independent allocations. Apply the repair to both kernel heads and
retain a `DEBUG_KOBJECT_RELEASE` destruction/failure-path regression before the
long VM runs.

### 2. A forced stop returns before the old run's console barrier and can race its cleanup with a new run

On a successful LXC result, `Container::ForcedStop#run` returns after checking
only LXC state and recursive cgroup emptiness
(`osctld/lib/osctld/container/forced_stop.rb:32-35,99-106`). It does not execute
the recovery/finalization used by the fallback at lines 39-53. The command layer
then deliberately skips the existing run's exit promise whenever forced stop
has started (`osctld/lib/osctld/commands/container/stop.rb:87-94`) and can return
success after removing accounting cgroups.

That promise is a data-safety and lifecycle barrier, not merely another check
for live processes. `Console#handle_ct_stop` force-unmounts and remounts the
container dataset to write dirty pages by default, may release a per-run
dataset, and only then fulfils the promise
(`osctld/lib/osctld/console/console.rb:108-134`; the configuration default is
true at `osctld/lib/osctld/config.rb:177`). `ct.stopped` separately destroys the
run configuration and retires its namespace sidecar
(`osctld/lib/osctld/container.rb:391-398` and
`osctld/lib/osctld/container/run_configuration.rb:238-243`). LXC state plus an
empty cgroup does not prove either sequence has completed.

After the stop command releases its manipulation lock, a non-ephemeral
container can start a new run. A queued console event for the old run can then
call `ct.unmount(force: true)` and `ct.mount(...)` against that newly running
container. If the post-stop hook was missed or failed, the new start can also
overwrite the still-active old `run_conf` (`osctld/lib/osctld/container.rb:241-251`),
leaving its cancellation pins and other run cleanup behind. The focused test
codifies the unsafe shortcut by asserting that the promise is not waited after
forced stop starts (`osctld/spec/osctld/commands/container/lifecycle_spec.rb:603-612`);
the forced-stop success tests verify only the LXC trace and external stopped
state.

Make successful forced stop establish the old run's finalization/writeback
barrier within the same absolute 60-second budget before the command reports
success or permits delete/restart. If the console path does not finish in the
remaining budget, run a synchronous, idempotent equivalent or fail closed; the
implementation must also serialize with a concurrently arriving post-stop
hook so that it neither skips nor duplicates old-run effects.

## Important

No additional Important findings.

## Advisory

### 3. A worker inherited from a dead daemon can leave retired namespace pins without an eventual reaper

The worker lock is intentionally inherited by the cancellation child so that a
replacement daemon cannot start a duplicate worker
(`osctld/lib/osctld/container/nfs_cancellation_state.rb:102-113` and
`osctld/lib/osctld/container/nfs_cancellation.rb:291-310`). If the run stops in
the replacement daemon while that old child still owns the lock,
`NfsCancellation#close` marks the record retired but `cleanup` returns false
(`nfs_cancellation.rb:128-135`; `nfs_cancellation_state.rb:115-128`). The
replacement's attempted worker also returns immediately on the busy lock and
runs its one cleanup attempt before the old child releases it
(`nfs_cancellation.rb:276-293`). The old child only records `completed` and
exits; it has no knowledge of the replacement daemon's `closed` state.

At that point the record is retired and unlocked, but cleanup is only scanned
once during daemon setup (`osctld/lib/osctld/daemon.rb:117-121`). The namespace
bind mounts can remain until another daemon restart or reboot, retaining the
network/user namespace and its resources. Add an eventual cleanup retry for a
busy retired record, or periodically prune retired records. Cover the
dead-daemon worker, replacement close, delayed worker exit sequence rather than
only manually calling `cleanup` after releasing the test lock.

## Compatibility and residual gaps

- The `shutdown_tree` store requires `CAP_SYS_ADMIN` in the initial user
  namespace and rejects a network namespace owned by the initial user
  namespace (`fs/nfs/sysfs.c:150-170`). osctld establishes the cancellation
  root only from the authenticated pre-mount peer, verifies cgroup membership,
  rejects the initial user namespace, and checks exact network-namespace
  ownership (`osctld/lib/osctld/container/nfs_cancellation.rb:42-73,251-274`).
  I found no additional tenant authorization or sibling-selection issue.
- New userspace probes only `shutdown_tree` and does not cache a negative result
  (`nfs_cancellation.rb:146-149`), so old kernels retain ordinary killing and do
  not pay the cancellation head start. New kernels keep the ABI dormant for old
  userspace. The sidecar stays outside `config.yml`, so old daemons can read run
  configuration. As already recorded in the plan, rollback to an old daemon
  loses terminal-intent recovery and can leave non-retired pins until reboot;
  this needs to remain an explicit rollback/operator constraint.
- The 6.12.95 source pin selects the `nfs-cancel` livepatch variant
  (`os/packages/linux/available-kernels.nix:16-23`). The loader compares both
  the exact booted kernel image and kernel notes before load, unload, or status
  operations (`os/modules/services/livepatches/default.nix:315-326`), and the
  historical boot base remains documented separately. I found no mixed-image
  path that bypasses these guards.
- No repaired kernel has been built or booted, and neither diagnostic NFS VM has
  run. KASAN/lockdep/delayed-release, livepatch build/load, real namespace bind
  mounts, concurrent shutdown, and sibling isolation therefore remain runtime
  gaps. Actual NFSv4 migration and SUNRPC transport-replacement runtime coverage
  is also absent; source inspection alone cannot prove those lock/lifetime
  paths under load.
