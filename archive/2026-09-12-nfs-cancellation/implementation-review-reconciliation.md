# Review reconciliation

Reviewed packet heads: OS 75e1d26df, Linux default fb4ad1506, retained fbe366228.
All four mandatory lanes used gpt-5.6-sol / xhigh with fresh context. Reports
are implementation-review-{general,architecture,scope,risk}.md.

## Blocking findings

- Architecture: forked Recovery closures lose daemon network state, events and
  hook watchers, and can inherit locks owned by vanished threads. Accepted.
  Removed the generic fork-runner block/host callback. Recovery stays in osctld;
  its IP/AppArmor commands use optional absolute deadlines in libosctl's command
  owner. A real spawned-command regression checks parent veth state/events/hooks
  while another daemon thread briefly holds the interface lock. This changes the
  process boundary design, so affected review lanes must rerun before integration.
- General/risk: forced stops skip Console's exit promise and can return before
  old-run writeback/unmount cleanup. Accepted. Restored waiting using only time
  remaining from the original forced-stop deadline. Timeout taints state and
  blocks accounting pruning/ephemeral deletion; no second 60-second wait.
- General: freezer-only termination proof misses processes stranded in another
  cgroup-v1 controller. Accepted. Verify recursive cgroup.procs in every active
  controller; regression keeps freezer empty while a CPU controller has a task.
- Risk: two embedded NFS netns kobjects can release the containing allocation
  before child cleanup with delayed release. Accepted in both kernels. Explicit
  parent reference survives hierarchy deletion until child release, including
  failed child publication. Folded into both kernel commits.

## Important findings

- Architecture: diagnostic-capable kernel versions repeated in registry
  consumers. Accepted. Mark nfsCancellation in kernel metadata, derive eligible
  versions and CI matrix once, consume them in flake outputs and VM instances.
- Scope: diagnostic builds repeat full functional/restart matrix. Accepted.
  Keep full coverage on normal kernels; diagnostic instances exercise lifetime
  stress. Actual NFSv4 migration validation remains to be added/run.
- Scope: global flake.nix path triggers all kernel builds for unrelated changes.
  Accepted. Kernel workflow tracks kernel configuration/catalog/workflow paths.

## Advisory decision

Risk: a foreign worker inherited from a dead daemon may finish after replacement
close and leave retired namespace pins. Accept until the next daemon startup's
retired-state reconciliation or reboot. The persistent worker lock still prevents
duplicate stuck workers and run/boot identities prevent adoption by another run.
No periodic background cleanup or extra lifecycle service is introduced.

## Verification

After remediation: 201 daemon examples pass (seed 6236), including real external
command/parent-state proof; 19 libosctl System tests pass (seed 37358). RuboCop
corrected seven style offenses and passes the commit hook. Nix matrix evaluation
shows three regular retained kernels and two diagnostic cancellation kernels.
Further exact-head checks and affected-lane reruns precede long integration.

## Second pass (OS 5e586fbf6, Linux e232e2bdc/c099b00ea)

All four fresh gpt-5.6-sol/xhigh reviewers completed. Duplicate findings are
merged at the highest supported severity:

- Blocking, all lanes: init_pid is transient after restart, so it cannot decide
  whether Console completion is required. Accepted. Container now selects an
  exit token from the active or past run atomically. Promise completion is
  sticky and synchronized, so late tokens cannot miss an already completed run.
  A run with no reconnected console fails closed within the same budget instead
  of pruning accounting/deleting an ephemeral container. No new cleanup service.
- Blocking, all lanes: parent Lockable, cancellation mutex and sidecar flock
  acquisition can outlive the forced-stop deadline. Accepted. An explicit
  Lockable deadline scope bounds nested attribute/object acquisitions, keeps the
  earliest nested deadline and always releases held locks. Bounded acquisitions
  use nonblocking attempts rather than joining condition-variable queues whose
  cleanup/reacquisition could itself block. Ordinary lock callers are unchanged.
  Cancellation has explicit per-call deadlines for its existing timeout-capable
  libosctl mutex and nonblocking sidecar flock. Its head start includes capture,
  persistence and worker wait. Failure-state reporting uses the remaining budget;
  inability to acquire the container state lock still returns failure and skips
  accounting/deletion. libosctl mutex relative timeouts now use monotonic time.
- Advisory, scope: common EOF cleanup changed no-deadline frontend behavior.
  Accepted and removed: no-deadline callers retain their existing blocking reap.

Architecture reviewer confirmed these narrow owner-level threading remediations
need focused checks rather than another review rerun. The final changes stay
within the reviewed process boundary and existing 60s contract. Focused tests
cover live lock holders, state flock contention still reaching LXC killing,
nested deadline restoration, post-timeout lock reuse and late exit tokens.
Exact final test/commit results follow in state.md; VM validation is still pending.

## Integration fixes after review

Legacy 6.12.48 VM tests found that pool import reconnects tty0 only in RUNNING.
After osctld restart with a frozen container, process termination succeeds but
no console handler completes writeback or fulfils its exit promise. Extended
that existing import path to FREEZING/FROZEN. This restores the reviewed
completion owner rather than weakening the barrier or adding another owner.
The existing cgroup v1/v2 frozen integration examples reproduce the issue.

The diagnostic build rejected DEBUG_KOBJECT_RELEASE because timer object
tracking was disabled. Explicit DEBUG_OBJECTS and DEBUG_OBJECTS_TIMERS satisfy
the exact source Kconfig dependencies. These are narrow implementation/test
remediations, with no new contract or design requiring another review round.

## Migration runtime follow-up

The advisory about RPC sysfs links was reproduced by actual migration on
repaired 6.12.95. The server kobject correctly remains initialized, but the state
link reports EEXIST and the mount transport recreates its target object. Both
kernel branches now refresh namespace-tagged links and export sysfs_delete_link
for modular NFS. Checkpatch reports no warnings. The new common VM regression
requires successful replacement, payload integrity, destination writes and valid
links. This directly closes the earlier migration advisory; it does not change
the cancellation scope, ABI contract, ownership model, or lifecycle policy, so
no new review lane is opened. Final compiled validation remains required.

The first broad VM run passed twenty examples before its custom prebuilt
harness lost unrooted Nix helper outputs to garbage collection. This does not
satisfy final integration acceptance. The harness now retains a configuration
GC root and prints individual exceptions; standard runner validation remains
required. No product behavior is changed to accommodate the harness failure.

## Focused migration review, round3

High-risk classification is unchanged. Fresh gpt-5.6-sol/xhigh general,
architecture and risk lanes reviewed the committed migration delta using
packet-v3; the scope lane was not repeated because the accepted migration
contract did not grow. General: no findings. Architecture: one Important
finding about split RPC sysfs setup/registration ownership, accepted and fixed.
Static rpc_client_register now accepts the active switch and owns optional
sysfs setup plus its existing failure cleanup for all three callers. Both
versions compile the amended SUNRPC object without warnings; checkpatch passes.
No new public interface, protocol, namespace policy or state format was added.
This direct remediation needs focused checks rather than another completed-lane
rerun. Risk review inspected the amended exact7c66ab3c/a2bdcc5b heads and found
no issues. No unresolved Blocking or Important findings remain.

Residual validation: exact provider archive hashes/pins await GitHub HTTP429;
full kernel/module linking and normal/diagnostic VM tests remain pending.
Successful migration, rollback, optional sysfs allocation failure, v4.0 migration
and concurrent replacement/shutdown have not passed on these corrected heads.
The earlier candidate's44 protocol passes do not prove the migration correction.
