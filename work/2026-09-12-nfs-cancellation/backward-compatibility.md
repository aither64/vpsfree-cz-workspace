# Userspace compatibility with kernels lacking NFS cancellation

This is the original review, before implementation. For the fixes and current
test results, see [implementation validation](runtime-validation.md).

The explicit requirement is that new osctld must continue working with an old
kernel. An osctld upgrade must not require a kernel update or reboot merely
because the new cancellation feature was added.

**Verdict: missing cancellation controls are tolerated, but the change is not
fully backward compatible in its lifecycle behavior.** A new mandatory freezer
wait can prevent forced termination even when cancellation is unavailable.
The automatic per-filesystem fallback also exposes the known old-kernel crash.

Reviewed vpsadminos `1a6c9980cf6e8c7eb8c73f063788708f5c93d447`, specifically
userspace change `3f1639b303b320c98c6098d5fbf88deb8ecbd9b0` and its parent.
No product changes were made.

## What currently works

Constructing/loading a run configuration does not require an NFS kernel
interface. The new class initially contains empty namespace handles, and its
state adds no serialized kernel-specific fields or schema migration. Namespace
capture uses procfs/nsfs, not the new cancellation ABI. Successful graceful
shutdown does not require a cancellation write; terminal-state handling later
attempts cancellation but catches userspace errors so the monitor can continue.

The cancellation selector itself tolerates all three absent-feature layouts:

| Kernel-visible layout | Current selector result |
| --- | --- |
| No `/sys/fs/nfs` | Returns zero without a write. |
| NFS sysfs exists, no namespace or filesystem shutdown controls | Returns zero without a write. |
| `server-N` or `major:minor` entries exist, but no `shutdown` attributes | Missing attributes are skipped; returns zero and creates no files. |
| Only legacy filesystem shutdown controls | Writes them; does not classify cancellation as unsupported. |
| Namespace `shutdown`, no `shutdown_tree` | Uses single-namespace cancellation. |
| Full new interface | Uses authenticated tree cancellation when available. |

See [selector and legacy fallback](https://github.com/vpsfreecz/vpsadminos/blob/3f1639b303b320c98c6098d5fbf88deb8ecbd9b0/osctld/lib/osctld/container/nfs_cancellation.rb#L304).
The checks occur after the worker has scanned processes, entered retained
network namespaces and mounted sysfs. Returning zero therefore is not an
early bypass of all new teardown machinery, nor an explicit capability result.

This explains why normal operations can work with the current old default
kernel. It is not sufficient to establish compatible failure handling.

## Regression: unsupported cancellation still adds a prerequisite to kill

The previous forced-stop frontend thawed the container and invoked the LXC kill
runner. The new frontend always freezes the payload, calls cancellation, waits
for freezer completion, calls cancellation again, and only then invokes LXC.
There is no branch around that barrier when cancellation returns zero because
the kernel has no support.

If a task does not freeze within the 30-second deadline, the new frontend
raises and thaws without invoking the kill. The old frontend still invoked it.
This affects both explicit `--kill` and graceful-timeout fallback. It does not
require an NFS mount: an unrelated task that cannot freeze is sufficient.
Recovery `force_kill` similarly gained a freezer-completion requirement before
`recovery.kill_all`.

[New frontend](https://github.com/vpsfreecz/vpsadminos/blob/3f1639b303b320c98c6098d5fbf88deb8ecbd9b0/osctld/lib/osctld/container_control/commands/stop.rb#L58),
[new freezer wait](https://github.com/vpsfreecz/vpsadminos/blob/3f1639b303b320c98c6098d5fbf88deb8ecbd9b0/osctld/lib/osctld/cgroup.rb#L461),
[recovery path](https://github.com/vpsfreecz/vpsadminos/blob/3f1639b303b320c98c6098d5fbf88deb8ecbd9b0/osctld/lib/osctld/commands/container/stop.rb#L108).

Nine review-only characterization examples passed, including a direct
comparison with the exact parent commit's frontend. For both cgroup versions
and both stop modes, an absent-control selector returned zero; with freezer
completion withheld, the previous frontend invoked kill and the current one
did not. The probe executes the real `wait_frozen` against temporary files,
with its timeout reduced to zero. LXC calls and freeze/thaw requests are mocked;
no host cgroup, namespace, workload or kernel was modified.

The positive cases confirm all three absent-interface layouts are tolerated,
legacy controls are actively written, and forced stop reaches LXC without
cancellation support when freezing succeeds. Result: **9 examples, 0 failures**,
seed 28483. Passing these characterization examples confirms the observed
regression; it does not mean the desired compatibility requirement passes.

## Regression: an old control is not necessarily a safe compatibility path

The current default 6.12.109 lacks namespace cancellation but provides
per-filesystem controls. New osctld invokes those automatically during teardown,
including init exit. The downloaded CI artifact records a kernel oops in that
path. The earlier [review](review.md) explains the independently verified
sysfs/client lifetime window.

Supporting old kernels must not mean invoking every historical interface that
happens to exist. The recommended default is to leave the unsafe legacy
filesystem interface unused until its implementation has been repaired and
validated. This would preserve the old kernel's retry policy; it would not
change its NFS mounts to hard retries.

## Required repair contract

1. Treat cancellation as an optional capability, detected from the running
   interface rather than the configured generation or kernel release string.
   Distinguish unsupported, no relevant clients, successful cancellation and
   failed cancellation where the caller needs that distinction. Do not cache
   absence permanently when the NFS module may be loaded later.
2. On kernels without supported cancellation, preserve the previous stop/kill
   and recovery behavior. The new NFS worker and freezer-completion barrier
   must not become prerequisites for delivering the requested kill. Do not
   make daemon startup or ordinary container operations fail due to missing
   cancellation files.
3. On capable kernels, preserve the cancellation sequence on success, and still
   attempt bounded termination/recovery when cancellation or freezing fails.
   Keep enough run identity for retries after partial terminal cancellation.
4. Keep the unsafe per-filesystem fallback disabled unless its specific kernel
   implementation is verified safe. Absence of cancellation is a supported
   operating mode, not an error that requires upgrading the kernel.
5. Leave mount retry policy to the old kernel and existing mount options. Do
   not promise newly bounded NFS teardown on an unsupported kernel. In
   particular, a hard mount can retain its historical outage behavior.

Early capture of the original run identity should remain compatible with later
NFS module loading; blindly skipping it at boot just because `/sys/fs/nfs` is
absent would reintroduce the namespace-recovery problem.

Acceptance coverage should boot a supported old kernel with no cancellation
controls, a kernel with the legacy controls, and the new kernel. Exercise daemon
startup/restart, container start, normal shutdown, `--kill`, timeout fallback,
recovery, init exit and ordinary restart on cgroup v1/v2. Include no-NFS
containers, unavailable NFS servers, and freezer/cancellation failures. Require
the legacy configuration to make no unsafe writes and check kernel logs after
cleanup. No fresh old-kernel VM boot was performed in this review.

The rollout remains daemon-first and kernel-optional. Nodes may continue running
an unsupported kernel; only enabling the hard-retry/cancellation guarantee
requires the capable boot kernel and matching modules.

## Upstream boundary checked during implementation

Upstream Linux provides RPC task cancellation and per-filesystem NFS sysfs
shutdown. Its current fs/nfs/sysfs.c does not expose the vpsAdminOS per-network-
namespace shutdown or shutdown_tree controls. The latter add sticky admission
barriers across a user-namespace subtree, including processless and future
namespaces. They are our container-teardown extension, not a straight backport
of an upstream container cancellation feature.

Checked against https://github.com/torvalds/linux/blob/master/fs/nfs/sysfs.c
and net/sunrpc/clnt.c on September 12. The local implementation's provenance is
Linux commit 563bbb35e8753e1bb34dad19ebeec8962ee3c1cd. The sysfs object lifetime
and migration findings include older code; reproducing a kobject reinitialization
warning on our 6.12.48 kernel proves that issue predates the new extension.
