# Focused migration repair review

Initiative: 2026-09-12-nfs-cancellation. Workspace:
/home/aither/workspace/ai/vpsfree.cz. Worktrees beneath
worktrees/2026-09-12-nfs-cancellation/. Tracking is this directory.
Read the mandatory-change-review skill and your lane reference. Review directly;
do not edit implementation or launch nested agents. Write findings to
implementation-review-v3-<lane>.md and return them. Use Blocking / Important /
Advisory, with file/line and concrete evidence.

## Scope and committed revisions

Two full adaptive review rounds already assessed the cancellation/daemon design.
This is a focused rerun of general, architecture, and risk lanes because actual
migration exposed additional RPC sysfs lifecycle behavior. Scope/proportionality
is unchanged: preserve NFS migration while fixing cancellation lifetime, with
normal and diagnostic runtime tests. Do not reopen unrelated reviewed code
without a concrete serious finding caused or exposed by this delta.

All intended handwritten changes are committed and worktrees have no tracked
dirt. Review these paired provider and consumer heads:

| Tree | Review baseline | Head |
| --- | --- | --- |
| linux | c099b00eafe7ced993eb6a7166876bb12bef8c72 | 4459e6f4f8958910fdfe5cd966450b5cab099449 |
| linux-6-12-95 | e232e2bdcc9a552b60b49ab8994bd49b115e1e58 | ec548c1a4ee1a41645fcfe84a9180ccce7a30796 |
| vpsadminos | 2bb3c251b8be913363b11809a2c0793213820ba2 | c9260bbbe68c4368e2acab1ba32ae7612a763b43 |

Linux bases for full initiative context: 9ccd5d6597a6ddbe5b44fb885ddf96e4dbc332dd
(default109) and 563bbb35e8753e1bb34dad19ebeec8962ee3c1cd (retained95). OS full base
15802517e2d92dda4ddc07ebac3d1d7ea087b430. Previous review packet-v2/reconciliation
files explain the accepted design. Linux bare clone has many packs; prefer
worktree reads and the small one-commit delta over broad git searches.

## Requested outcome and constraints

Repair existing 6.12.95, with no extra kernel entry, and carry the same repair
to current6.12.109. Cancellation is in the base kernel; preserve existing
livepatch identity guards and frozen historical fixtures. osctld must always
attempt requested killing, tolerate kernels without shutdown_tree, and retain
original namespace/terminal state across daemon restart. Userspace changes and
those contracts are unchanged in this delta.

Retaining the NFS server kobject during migration must preserve working RPC
sysfs links as well as data access. Migration must not reinitialize a published
kobject, dereference mutable/absent client state, or cross namespace identity.
The real migration test must verify successful replacement, payload checksum,
destination write, and both RPC link targets. Allocation of debug sysfs state
is optional, so failure must not crash the mount/migration path.

The kernel delta refreshes namespaced links and recreates RPC sysfs state in
transport replacement and rollback. The NFS consumer refresh and SUNRPC
provider setup remain one functional commit: refreshing a missing object is
invalid. Existing sysfs_delete_link is exported GPL for modular NFS. Discover
its consumers and call preconditions from code; do not assume registration
implicitly allocates sysfs. No new userspace ABI/state/deployment requirement.

The OS commit includes the real migration test, initial NFSD readiness wait,
and BusyBox-compatible target validation. The old candidate pins in that
commit still identify cb16974b/6090ca00. GitHub archive downloads for the corrected
provider heads are returning HTTP429. The next OS amendment will mechanically
replace those two rev/hash pairs and the documentation SHA with the exact
reviewed heads after prefetch succeeds. Review the provider HEADs above with
the consumer test HEAD; do not treat old pins as the final deployable result.
No long integration tests on the correction will start before findings are
reconciled and exact pins updated. Record this pending mechanical validation.

## Evidence and quick checks

- Full amended kernel diff: checkpatch --strict, zero errors/warnings/checks.
- Both kernel trees and OS git diff --check pass.
- Full generated Ruby test script and migration.rb: Syntax OK.
- RuboCop migration.rb: one file, zero offenses. Commit Nixfmt/RuboCop hooks pass.
- Unchanged osctld focused/native tests and old6.12.48 cgroup1/2 VMs passed.
- Previous candidate normal109: all44 protocol scenarios across NFS3/4.0/4.1/4.2
  pass, including restart, dirty init, processless namespaces and isolation.
- Clean migration on cb16974b and race setup on6090ca00 crashed at
  sysfs_delete_link+0x23, address0x30. nfs_sysfs_link_rpc_client was passed an
  absent clnt->cl_sysfs after rpc_switch_client_transport. Current source
  corrects that lifecycle. Exact traces: scratch/migration109-null-sysfs.txt
  and scratch/migration95-null-sysfs.txt. New correction runtime pending.
- Initial full-suite migration failure was separate: BusyBox lacks readlink -e.
  New fixture uses test -e && readlink -f. Initial server PID alone also did
  not guarantee the NFSD export table existed; explicit readiness now waits.
- Historical livepatch AMD and Intel lifecycle tests pass in CI. Matching
  corrected-base livepatch identity and full diagnostic kernels remain pending.

Overall risk: high (kernel lifetime, protocol, namespace/host behavior).
Use gpt-5.6-sol, xhigh. No default-branch merge or deployment is requested.
Mixed old/new daemons and kernels remain supported with rolling userspace
updates; base-kernel fixes need per-node reboot. No fleet-wide coordination.
No session lifecycle action is authorized; leave it open.
