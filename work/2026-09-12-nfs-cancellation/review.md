# NFS cancellation review

This is the original review, before implementation. For the fixes and current
test results, see [implementation validation](runtime-validation.md).

Reviewed September 12, 2026. This is an investigation and repair proposal;
project source, deployments and fallback policy have not been changed.

Follow-up requirement: osctld must remain usable on kernels without NFS
cancellation. The [backward-compatibility review](backward-compatibility.md)
adds nine targeted probes and confirms that absent controls are tolerated,
but forced-kill failure handling and the unsafe legacy fallback prevent a
full compatibility sign-off.

Five issues need attention. The default-kernel mismatch and legacy teardown
fault are confirmed. The retained cancellation kernel improves the main
synchronization paths, but still has an unsafe initialization-error path.
osctld recovers a normal running container after restart by rediscovery; it
does not persist the original cancellation handles. Its forced-stop error path
can also abandon the kill after terminal cancellation has begun.

## Sources and verification

- vpsAdminOS remote `staging`, fetched and independently checked through GitHub:
  `1a6c9980cf6e8c7eb8c73f063788708f5c93d447`.
- Daemon change: `3f1639b303b320c98c6098d5fbf88deb8ecbd9b0`.
- OS integration: `c3f219a385e605ac00f2864c9c311902620271cd`, compared with its
  earlier candidate `36589f99162c65ff3aaea0b60df92d78ddecb0dc`.
- Default Linux source: `9ccd5d6597a6ddbe5b44fb885ddf96e4dbc332dd`, also the
  remote `vpsadminos-6.12` branch head at review time.
- Retained cancellation Linux source:
  `563bbb35e8753e1bb34dad19ebeec8962ee3c1cd`, reviewed as a complete commit and
  against relevant surrounding NFS, NLM, SUNRPC and namespace code. Its parent
  is `68f3357add6ad462a99b99f4e76c6441f34b05ba`.
- Downloaded and inspected the NFS and identity artifacts from
  [CI run 34630335805](https://github.com/vpsfreecz/vpsadminos/actions/runs/34630335805).
  The NFS console contains the recorded `rpc_cancel_tasks` oops.
- Native Nix evaluation independently confirms both kernel selections and
  patch lists: [kernel-selection.json](kernel-selection.json).
- **123 focused osctld RSpec examples passed**, using the repository's patched
  Ruby. These cover cancellation, run configuration, monitor, stop/recovery,
  pre-mount capture and freezer behavior. They do not boot a cancellation
  kernel or reproduce kernel races. No kernel build or VM suite was run.

## 1. High: the default kernel still exposes the unsafe legacy teardown path

The current daemon deliberately falls back to individual filesystem controls
when namespace controls are missing:
[nfs_cancellation.rb, line 322](https://github.com/vpsfreecz/vpsadminos/blob/3f1639b303b320c98c6098d5fbf88deb8ecbd9b0/osctld/lib/osctld/container/nfs_cancellation.rb#L322).
That is the path selected by the default 6.12.109 kernel.

In that kernel, `nfs_free_server()` releases the ACL, mount and shared NFS
clients **before** removing and draining the server's sysfs object.
`shutdown_store()` can therefore still run against released client pointers.
It also dereferences the NLM RPC client directly, without the retained
kernel's locked helper and readiness checks.
See [old client.c, line 1087](https://github.com/vpsfreecz/linux/blob/9ccd5d6597a6ddbe5b44fb885ddf96e4dbc332dd/fs/nfs/client.c#L1087)
and [old sysfs.c, line 281](https://github.com/vpsfreecz/linux/blob/9ccd5d6597a6ddbe5b44fb885ddf96e4dbc332dd/fs/nfs/sysfs.c#L281).

CI recorded a host-kernel NULL dereference through `shutdown_store()` into
`rpc_cancel_tasks()`, with a NULL task-list link and fault address `0x28`.
The source proves an unsafe lifetime window; the crash does **not** prove
which particular NFS/ACL/NLM pointer caused this instance. A NULL check or
an extra lock around the task-list walk cannot repair a freed client.

**Recommendation:** disable the per-filesystem fallback on unverified legacy
kernels while retaining their existing soft-mount policy, or backport and
validate the complete lifetime repair before continuing to invoke it.
Disabling the fallback is a proposed compatibility decision, not an action
taken in this review. Preserve forced-kill attempts when cancellation is
unavailable, and report the reduced teardown guarantee honestly. A kernel
fault cannot be contained by osctld's worker timeout.

**Regression:** race legacy shutdown writes with mount initialization,
failed mounts, unmount and shared-client/NLM teardown under KASAN and lockdep.
Check kernel logs after failure cleanup as well as successful examples.

## 2. High: initialization-error cleanup remains unsafe in the new kernel

The new `shutdown_store()` first evaluates
`server->nfs_client->cl_net`, and only then takes `nfs_server_lock` and checks
whether the server was published in the volume list.
See [new sysfs.c, line 355](https://github.com/vpsfreecz/linux/blob/563bbb35e8753e1bb34dad19ebeec8962ee3c1cd/fs/nfs/sysfs.c#L355).

There is a concrete conflicting path in `nfs_init_server()`:

1. It publishes the `server-N` sysfs object at line 779.
2. Subsequent lockd/RPC-client initialization can fail.
3. Its error path sets `server->nfs_client = NULL` and drops the reference at
   lines 843–845, while the sysfs object still exists.
4. A concurrent shutdown callback dereferences that NULL pointer before
   reaching the new `-EAGAIN` check.

[Initialization and error path](https://github.com/vpsfreecz/linux/blob/563bbb35e8753e1bb34dad19ebeec8962ee3c1cd/fs/nfs/client.c#L778).
Moving sysfs removal to the beginning of `nfs_free_server()` fixes ordinary
destruction ordering but is too late for this earlier reference release.
This is a source-proven race window, **not a newly reproduced kernel oops**,
and is distinct from the recorded 6.12.109 crash. Normal osctld operation on
the new kernel selects namespace controls, so this finding concerns the
still-exposed per-filesystem interface.

**Recommendation:** make the client reference remain valid for the entire
published sysfs lifetime, including failed initialization; alternatively,
defer publication until it is safe. Drain callbacks before clearing/releasing
their referenced state, and make locking independent of an unprotected,
mutable client pointer. Checking NULL alone is insufficient for the lifetime
race. Include NFSv4 migration in this repair audit: `nfs4_update_server()` and
`nfs4_set_client()` replace/release `server->nfs_client` outside the new
volume-list critical sections.

**Regression:** inject failure after sysfs publication but before volume-list
insertion, race shutdown with the error unwind, and require a clean error
return and clean KASAN/lockdep logs. Exercise migration separately.

## 3. High: restart rediscovery does not preserve the original run identity

`RunConfiguration#dump` persists the run ID and normal boot configuration;
it does not persist `init_pid`, namespace handles or cancellation progress.
Loading creates a fresh `NfsCancellation` with empty owner/netns/init handles.
[Run configuration](https://github.com/vpsfreecz/vpsadminos/blob/1a6c9980cf6e8c7eb8c73f063788708f5c93d447/osctld/lib/osctld/container/run_configuration.rb#L175).

`Monitor::Master#update_state` asks LXC for the current init PID and recaptures
namespaces from it. This is useful recovery for an ordinary running container.
The existing restart test covers that case, with a writer blocked while init
is still alive:
[restart test](https://github.com/vpsfreecz/vpsadminos/blob/1a6c9980cf6e8c7eb8c73f063788708f5c93d447/tests/suite/osctl/nfs-cancellation.nix#L385).

The gaps are:

- If init has gone, or has already released its network namespace while LXC
  is still tearing down mounts, there is no retained handle to recover from
  its `/proc` entry. Missing owner causes `abort` to return zero; descendant
  discovery is inside the worker and is not even entered without an owner.
- If init moved into a descendant user/network namespace before daemon
  restart, recapture describes its current namespaces, not necessarily the
  original run root. Sibling/processless namespaces may be outside the
  recovered subtree. Even retaining the original user namespace alone is
  insufficient if no recovered netns is owned by it: osctld only chooses
  `shutdown_tree` for an exact owner match.
- Restart during a partially completed terminal cancellation loses the
  daemon's knowledge of the operation and its original retained authority.
  Kernel barriers already installed remain active, so forgetting them does
  not restore successful NFS service.

[Capture and abort](https://github.com/vpsfreecz/vpsadminos/blob/3f1639b303b320c98c6098d5fbf88deb8ecbd9b0/osctld/lib/osctld/container/nfs_cancellation.rb#L36),
[root selection](https://github.com/vpsfreecz/vpsadminos/blob/3f1639b303b320c98c6098d5fbf88deb8ecbd9b0/osctld/lib/osctld/container/nfs_cancellation.rb#L297).

**Recommendation:** retain authenticated original user/net namespace handles
outside the restarted daemon, for example in root-owned bind mounts under a
per-run `/run/osctl` directory, or an independently surviving descriptor
store. Key them by the persisted run ID and boot identity; namespace inode
numbers or a saved PID alone cannot replace live references. Restore these
before monitor/stop processing. Persist terminal intent before the first
irreversible write and retry it idempotently. Release the references only
after verified teardown. Do not infer an ancestor teardown root from arbitrary
tenant namespace handles. Existing runs need authenticated adoption while
their original root is still available, or a controlled container restart.

**Regression:** combine daemon restart/SIGKILL with PID1 exit, processless
namespaces, PID1 namespace changes, and interruption between cancellation and
kill. Keep the current live-init restart case. Verify another container still
reads/writes, and that a new run has fresh, uncancelled namespaces.

## 4. Important: cancellation/freezer failure prevents forced kill

Both `with_forced_teardown` and recovery `force_kill` perform cancellation and
wait for freezer completion before invoking LXC stop or sending SIGKILL. Any
exception jumps straight to thawing. The kill is skipped, including for a
user-requested `--kill`.
[Normal stop](https://github.com/vpsfreecz/vpsadminos/blob/3f1639b303b320c98c6098d5fbf88deb8ecbd9b0/osctld/lib/osctld/container_control/commands/stop.rb#L58),
[recovery stop](https://github.com/vpsfreecz/vpsadminos/blob/3f1639b303b320c98c6098d5fbf88deb8ecbd9b0/osctld/lib/osctld/commands/container/stop.rb#L108).

This can leave a running container whose NFS was already terminally cancelled,
or prevent killing a container with an unrelated unfreezable task. Existing
unit tests explicitly expect no kill after a cancellation exception; their
green result confirms this behavior rather than ruling it out.

**Recommendation:** preserve the quiesce/cancel/kill sequence on success, but
make cancellation failure a reported teardown failure that still attempts
bounded process termination. Thaw as needed for exit, retain recovery identity
until cleanup is proven, and never report a clean stop just because the
cancellation worker returned. Do not replace this with an unbounded wait on
LXC or an uninterruptible worker.

**Regression:** cancellation timeout, sysfs error, second-pass failure after
partial cancellation, and freezer timeout must all attempt the requested kill
and preserve enough state for retry.

## 5. Important: the two fixtures select a kernel without the feature

`available-kernels.nix` selects 6.12.109 for stable and unstable, with no
registered livepatch. The cancellation source and patchVersion 6 are retained
under 6.12.95/`nfs-cancel`.
[Kernel selections](https://github.com/vpsfreecz/vpsadminos/blob/1a6c9980cf6e8c7eb8c73f063788708f5c93d447/os/packages/linux/available-kernels.nix#L4).

Neither the NFS nor identity fixture selects its kernel. The NFS fixture
correctly rejects the old kernel's forced-soft default. The identity fixture
reads a monitor JSON that is correctly omitted when patchVersion is zero.
Their contents are unchanged between the original candidate and rebased
integration; the inherited default changed.

**Recommendation:** explicitly select 6.12.95/`nfs-cancel` for the retained
identity/lifecycle regression. Maintain separate NFS coverage for the retained
kernel and the actual default; port cancellation and its prerequisites onto
the current default before claiming default hard-retry/cancellation support.
Assert the exact boot source/variant in each job. Merely pinning both failing
tests to the old retained kernel would hide the production-default gap.

Do not add `hard`, accept `soft`, fabricate the monitor JSON, or treat passing
legacy Intel/AMD livepatch jobs as validation of default-kernel cancellation.

## What is sound in the design

- Kernel tree cancellation installs a sticky user-namespace barrier before
  walking clients. Client registration checks that barrier under the global
  registration lock; future descendants inspect ancestors. This is the right
  mechanism for processless and concurrently created namespaces.
- Activation and restart handling use the client lock so an RPC cannot simply
  miss the cancellation walk or erase cancellation during restart. Ordinary
  `nfs_free_server()` now drains sysfs callbacks first, and volume-list
  locking protects the usual shutdown/removal paths.
- New namespace controls require initial-user-namespace CAP_SYS_ADMIN and
  reject host-owned namespaces. The NLM helper and shared-volume checks
  improve lifetime handling and avoid cancelling an active sibling mount's
  lock client through the per-filesystem path.
- osctld authenticates the hook peer PID, verifies payload cgroup membership,
  compares namespace device/inode identity, walks ownership ancestry, mounts
  its own sysfs view, and refuses to recapture a closed run. It avoids tenant
  mount paths and retains a proc directory against PID reuse.
- PF_EXITING precedes `exit_files()` in this kernel. Checking it addresses the
  dirty-PID1 deadlock before LXC can emit STOPPING. The code checks all init
  threads, not just the group leader; the current test for this is synthetic.
- The cancellation child has a monotonic timeout, bounded output and
  asynchronous reaping. These bound the daemon's wait for that child; they
  cannot bound kernel spinlock execution or guarantee a successful stop.
- Pending-write loss is accurately described as terminal-teardown behavior.
  Normal-outage tests check the payload and server checksum after recovery.
- Exact boot notes/image checks and the separate livepatch variant are
  necessary: the cancellation source changes structure/module ABI despite
  retaining the 6.12.95 release string.

These observations are source review conclusions, not a proof of race freedom.
Further stress coverage should include single-netns shutdown independently of
tree shutdown, same-owner sibling mounts, non-leader thread namespaces, real
multithreaded PID1 exit, and mount/unmount/cancellation concurrency. Also watch
per-run handle growth: repeated capture retains each distinct init netns until
run destruction, although a retained original root can already cancel its tree.

## State and rollout contract

| Situation | Current behavior |
| --- | --- |
| Daemon restart, original init still accessible | Handles are rediscovered; existing VM test covers a live-init outage case. |
| PID1 blocked in `exit_files()` | Namespace release occurs later, so recovery can still work if LXC supplies its PID; restart at this exact point is not tested. |
| Init gone or original namespace root no longer discoverable | No durable handle recovery; terminal teardown is not assured. |
| Kernel cancellation followed by daemon restart | Existing namespace barriers remain; restarting osctld does not undo cancellation. |
| Ordinary container stop/start | Creates a new run; the existing tests verify subsequent mount/write recovery. |
| Host reboot | Old kernel namespaces disappear; ordinary container configuration persists. |

Recommended repair order: first contain the legacy fallback and fix forced-stop
failure handling; then preserve run authority across daemon restart; repair
the remaining kernel lifetime hole and port the full cancellation dependency
set to the current supported stable kernel. Freeze retained identity tests and
add explicit default-kernel coverage. Run required committed-change review
before long integration tests, then publish matching kernels/modules through
CI and validate the full NFS version matrix and failure cleanup.

Deploy the capable daemon before rebooting a node into a hard-default kernel.
The structure changes require a matching boot kernel and rebuilt modules;
the 6.12.95 `nfs-cancel` livepatch must not be loaded into another source build.
Nodes can be rolled independently: no cross-node protocol/schema change calls
for a simultaneous fleet update. Preserve legacy boot/livepatch artifacts.
Rolling a daemon back to one without cancellation support while retaining
hard mounts loses the teardown guarantee. Rolling back the kernel requires
reboot, which removes the old namespace state. Host-created NFS mounts passed
into a container remain outside this ownership contract.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-12-nfs-cancellation/
