# Architecture and repetition review

Reviewed the complete committed series and owning components for:

- `vpsadminos` `15802517e2d92dda4ddc07ebac3d1d7ea087b430..75e1d26df4acaea85f20c3ce2ac6ec6046fc1d5d`
- retained Linux 6.12.95 `563bbb35e8753e1bb34dad19ebeec8962ee3c1cd..fbe36622894dbc46f82e970dcae5da18d6e58c8c`
- default Linux 6.12.109 `9ccd5d6597a6ddbe5b44fb885ddf96e4dbc332dd..fb4ad1506c1d22ab92251b3ba167ca951d453b8e`

The default-kernel review used `scratch/linux-default-final.patch` plus the
head worktree, as directed by the packet. Linux owns the `shutdown_tree` ABI
and the SUNRPC/NFS admission and cancellation state. The only runtime consumer
found in current workspace sources is osctld's
`Container::NfsCancellation`; vpsAdminOS owns the source pins, matching
6.12.95 livepatch composition, CI outputs, documentation, and VM consumers.

## Blocking

### 1. Forked recovery closures cross the daemon-state boundary and lose or block required effects

Commit `d7113acc7` adds a block form to
`osctld/lib/osctld/container_control/frontend.rb:168-219`; the block is
evaluated after `Process.fork`, at lines 192-214. The new callback in
`osctld/lib/osctld/container_control/commands/stop.rb:61-64` exposes that as a
generic root `host` executor. `Container::ForcedStop` then sends
`Recovery#kill_all`, parts of `Recovery#recover_state`, and all of
`Recovery#cleanup_or_taint` through it
(`osctld/lib/osctld/container/forced_stop.rb:39-52`). These closures capture
the live `ct`, `Recovery`, DB, locks, hook manager, and event manager rather
than a serialized operation contract.

This is already incorrect for the actual `recover_state` consumer. Its child
calls `ct.netifs.take_down`
(`osctld/lib/osctld/container/recovery.rb:26-36`). `Veth#down` both clears the
daemon's runtime `@veth` and publishes `:ct_netif action: :down`
(`osctld/lib/osctld/net_interface/veth.rb:190-219`). The parent sees neither:
forked object mutations affect only the child, and `Eventd.report` merely
pushes into in-process worker queues
(`osctld/lib/osctld/eventd/manager.rb:157-163`,
`osctld/lib/osctld/eventd/worker.rb:43-57`); those worker threads do not exist
in the post-fork child. The recovery fallback is needed precisely when LXC's
ordinary veth-down callback may not have repaired parent state. A forced stop
can therefore return success while the daemon still considers a deleted veth
created, omits its down event, and lets later netif operations act on the stale
name. The async `post_stop` hook is also launched from this short-lived child,
so its normal watcher thread and failure reporting are lost when the runner
exits.

The abstraction can also consume the whole forced-stop deadline. Netif manager
and veth access use `Lockable`, whose `OsCtl::Lib::Mutex` records the owner as a
Ruby `Thread` in `@thread` (`libosctl/lib/libosctl/mutex.rb:6-44`), while
`Lockable::Lock` separately records held/queued thread objects
(`osctld/lib/osctld/lockable.rb:28-82`). If another daemon thread owns one at
fork, the child inherits the recorded owner but not the owning thread. A
focused probe with the committed `OsCtl::Lib::Mutex` confirmed that a child
forked while another thread held the mutex receives
`OsCtl::Lib::Mutex::Timeout`. In production the lock timeout is 90 seconds,
longer than `ForcedStop`'s 60-second deadline, so `fork_runner` kills the child
and reports teardown failure. `Recovery#cleanup_netifs` additionally traverses
the fork-time snapshot of `DB::Containers` and each container's netif objects
(`osctld/lib/osctld/container/recovery.rb:118-158`), which is not a safe source
of current ownership decisions in a detached process.

The focused `ForcedStop` spec hides the boundary by implementing `host` as an
inline lambda that calls `operation.call` in the test process
(`osctld/spec/osctld/container/forced_stop_spec.rb:31-39`). Frontend specs test
pipe framing and deadlines, but never run recovery against parent-owned state.

Keep daemon state transitions, hooks, events, and ownership decisions in the
parent. Bound only explicit host operations in a child with immutable,
serialized inputs and return enough structured results for the parent to
apply runtime state. An alternative is to keep `Recovery#recover_state` in the
parent and split its potentially blocking syscalls into dedicated runner
operations. Add a real-fork regression which proves that forced recovery
clears the parent's veth state, delivers the down event, and cannot inherit a
held `Lockable` owner. This must be fixed before long integration tests because
it can make the repaired forced-stop path fail at its deadline and can report
an internally inconsistent successful stop.

## Important

### 2. The cancellation-capable diagnostic kernel set has no owner and is repeated in three consumers

The authoritative kernel catalog is
`os/packages/linux/available-kernels.nix:4-32`, but it has no metadata saying
which base kernels implement the repaired cancellation ABI. The same current
set, 6.12.95 and 6.12.109, is then repeated in three new consumers:

- diagnostic flake outputs in `flake.nix:341-356`;
- diagnostic CI matrix entries in `.github/workflows/kernels.yml:44-57`;
- regular and diagnostic NFS VM instances in `tests/all-tests.nix:163-176`.

A future default-kernel bump that retains 6.12.109 can update the source
catalog and normal kernel CI while silently leaving diagnostics and the NFS
suite on the previous default. That is a credible omission because the normal
matrix is already derived from `.#lib.kernelVersions`, whereas the diagnostic
rows are hand maintained. It could publish a new cancellation port without
the KASAN/lockdep/fault-injection build or its VM coverage.

Declare cancellation/diagnostic eligibility once with the owning kernel entry
(for example as kernel feature metadata), derive and export the version list
from `availableKernels`, and have the flake output, workflow matrix, and test
instances consume it. If tests intentionally cover a different finite set,
name that policy separately and check bidirectional coverage against the
diagnostic outputs.

## Advisory

No advisory findings.

## Residual gaps

- The two Linux branches necessarily carry corresponding lifetime behavior at
  different bases; no shared source owner exists across independent release
  branches, and I found no additional downstream implementation of
  `shutdown_tree` that should be consolidated.
- The SUNRPC global client index and NFS per-net index are populated and
  removed by their owning registration/lifecycle paths. Their separate roles
  cover RPC admission and NFS volume state, including initializing and
  processless namespaces; they are not hard-coded consumer catalogs.
- Architecture inspection cannot establish kernel lifetime and lock safety.
  Planned 6.12.95/6.12.109 KASAN, lockdep, fault-injection, NFSv4 migration,
  livepatch, and VM runs remain required. The packet records that actual NFSv4
  replacement runtime coverage is not yet present.
