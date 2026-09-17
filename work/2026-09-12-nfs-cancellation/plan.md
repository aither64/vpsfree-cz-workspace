# Repair NFS cancellation and forced stopping

Abandoned at the user’s request on 2026-09-17. This plan is retained as history;
no further implementation, validation or rollout is scheduled.

## Accepted scope

User authorized implementation on September 12 after review and planning.
Fix the existing Linux 6.12.95 entry in place and port repaired cancellation
to default 6.12.109. Do not introduce another kernel entry or livepatch variant.
Cancellation is compiled into the 6.12.95 base kernel; rebuild its matching
existing nfs-cancel cumulative livepatch. Preserve original legacy fixtures and
their exact boot/livepatch inputs. This repair does not deliver cancellation
to existing boot kernels through an in-place livepatch.

Affected repositories: linux and vpsadminos. Use this initiative's registered
worktrees and retained branches. No production deployment, default-branch
integration, session lifecycle action, or other session's state is authorized.

## osctld

- Preserve the configured graceful-shutdown timeout. Forced stopping has one
  60-second budget: cancellation gets up to five seconds before killing; its
  worker may continue alongside killing for 30 seconds total. Recover at once
  on LXC failure, or by second 50, leaving ten seconds to verify termination.
- Share explicit kill, graceful fallback, and recovery orchestration. Never
  skip killing because cancellation, freezing, or thawing failed. Remove
  cancellation freezer waits; retain necessary thawing and best-effort recovery.
  Bound subprocess waits, report failure if termination is unconfirmed, and
  preserve recovery state without deleting a live ephemeral container.
- Support cancellation only with shutdown_tree. No automatic legacy per-mount
  or partial per-netns fallback. Unsupported kernels skip the worker/head start.
  Recheck capability on subsequent requests, including after module loading.
- Pin the authenticated original user/net namespaces before tenant init using
  root-owned bind mounts in /run/osctl/nfs-cancellation. Store a versioned
  sidecar keyed by boot identity and existing RunId, including namespace/init
  identities and terminal cancellation intent/result. Restore before monitoring,
  retry interrupted terminal cancellation, and retain pins while needed.
- Validate ownership and PID/run identity; never infer a root from arbitrary
  descendant processes. Unrecoverable old runs retain ordinary killing with
  cancellation unavailable until the next start. Avoid host-wide process scans,
  duplicate workers, and holding object locks while waiting for workers.

## Kernel and packaging

- Fix sysfs lifetime during NFS initialization failure and final destruction.
  Use a stable referenced namespace context before locking and accessing mutable
  client pointers; reject unready/migrating servers. Include NFSv4 replacement
  and kobject lifetime in the repair.
- Preserve sticky RPC admission/task cancellation for existing, initializing,
  processless, and future descendant namespaces, with host/sibling isolation.
  Port prerequisites carefully to 6.12.109 instead of replaying stable history.
- Update existing 6.12.95 and 6.12.109 source pins/hashes. Keep existing selectors,
  variant names, kernel release strings, exact boot-image/note guards, and
  historical legacy livepatch fixtures. Adjust existing patch inputs as needed.
- Explicitly select intended kernels in fixtures. Publish kernel/livepatch and
  required diagnostic outputs through CI/cache before integration tests.

## Verification and review

Focused Ruby regressions cover all forced-stop entrypoints, time budgets,
cancellation/worker/freezer errors, unsupported and legacy kernels, and both
cgroup versions. Restart tests include vanished/changed init namespaces,
processless descendants, interrupted pin publication, PID reuse and run reuse.
NFSv3/v4 tests cover read/write/lock outages, normal recovery and checksums,
dirty exit, initializing mounts and new-client races, fresh-run recovery and
host/sibling isolation. Stress kernel initialization/unmount/client replacement
with concurrent sysfs shutdown, fault injection, KASAN and lockdep. Verify exact
kernel selection and matching/mismatched and historical livepatch lifecycles.

Commit intended changes and run quick checks, then mandatory high-risk review
with general, architecture, scope, and risk lanes (gpt-5.6-sol, xhigh), before
long integration tests. Investigate CI failures and inspect kernel logs.

## Compatibility and rollout

Deliver userspace first, independently of running-kernel support or node reboot.
Boot repaired kernels incrementally afterward; no coordinated fleet update.
Sidecars preserve the existing run-configuration format. Old daemons ignore new
state; pins remain until reconciliation or reboot. Kernel terminal cancellation
is irreversible, and daemon rollback loses hard-NFS teardown guarantees.
Retain recovery state and account for affected workloads when rolling back.
