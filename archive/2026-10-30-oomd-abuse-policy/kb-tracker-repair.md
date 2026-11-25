# KB tracker repair — current implementation contract

2026-10-31. **Current, lead accepted; owner3 implementation released.** User
directed “well find the root cause and fix it”. The earlier user-choice hold and
supervision-only/no-schema proposal are superseded by this contract. In particular,
full executable/argv equality is retained for control authority, **not** required
for a proved wait-only descendant across legitimate exec/credential transitions.
No old receipt conversion or exceptional recovery is authorized.

Owner3 exclusively owns KB application source, Git and native operations.
Architect owns this brief and the completed no-guest prototype/evidence.
No additional design approval is needed for this bounded package.

## Proven cause and evidence

Exact subject: KB7bdee285d62343c653b5a8c5cfdeab2d97ef7f4d, appf60d41a4,
source /nix/store/ay80icp9ic32kiz768w8h1h72w1p0wxa-source.

[Diagnostic plan](kb-capacity-evidence/helper-diagnostic-plan.md) and
[actual result](kb-capacity-evidence/helper-proc-diagnostic.json) prove the current
host compatibility failure. One ordinary invocation of the installed setuid
helper with an unknown argument was held at its usage write on a private pipe:
initial UIDs1000/0/0/0 and proc owner0; after privilege drop all UIDs1000 with
CAP_NET_ADMIN only. Both stages denied exe read with EACCES. Stat/start ticks,
cmdline and all task child lists remained readable. The helper exited1 with usage,
the readable Ruby control exited0, and both direct children were reaped and absent.
No guests, network allocation, ptrace, sudo or permission changes occurred.
An initial prototype syntax error happened before spawn; it was corrected before
this single helper invocation.

Installed wrapper is root:wheel mode4550 and embeds QEMU10.2.4's store helper.
Upstream v10.2.4 qemu-bridge-helper.c rejects the diagnostic argument before
ACL/network socket/TUN/ioctl; installed derivation patches affect other files.
Its normal privilege transition makes executable-link access unsuitable as a
mandatory lifetime observation. Dumpability/capability access restrictions are
the mechanism; proc status did not directly expose a dumpability value.
QEMU net/tap.c forks/execs its configured helper and waits for that exact child.
The pinned KB/OSVM launch fixes the root-managed helper path and QEMU bridge argv.
This source-owned launch explains the supported transition; cmdline is never
used as executable authentication or as a process whitelist.

Historical PID2989738 remains unidentified: its complete tuple was never saved.
The old tracker failed on exe EACCES, startup nevertheless returned0/ready,
then tracker join rethrew during stop and prevented complete finalization.
Mechanism proof does not retrospectively identify that PID.

## Frozen process receipt and readers

New writes use **process receipt schema2** with exactly these top-level keys:

| Key | Value |
| --- | --- |
| schema | integer2 |
| instance_id, run_id, artifact_id, artifact_sha256 | existing exact launch/artifact bindings |
| control | existing full runner tuple: pid,start_ticks,boot_id,owner_uid,executable,argv |
| descendants | array of the lifetime records below |
| complete | boolean |
| tracking_error | null, or first failure object with exactly class,message; bounded strings |

A descendant has exactly kind,boot_id,pid,start_ticks,parent. kind is
`descendant-lifetime`; parent has exactly boot_id,pid,start_ticks. IDs use existing
UUID/boot validation, pid>1 and existing bounded integer checks. No owner_uid,
executable or argv in lifetime authority. Parent is first **proved** ancestry,
not a claimed executable or a current-PPid authorization. Parent tuples must
resolve to control or another retained descendant in this receipt, with matching
boot, no cycles/duplicates/self-reference. Retained records grow monotonically.
Different start times for one reused PID are distinct lifetimes; the old lifetime
cannot authorize observing/signaling the replacement.

Use one source-owned validation/access boundary for this existing format, not a
new state framework. Reject malformed, mixed, unknown-version and wrong-run forms.
Bound error class to256 bytes and message to2048 bytes; preserve the first error,
with native detail in the existing owned runner log. Complete requires no error.

**Old-reader discriminator is key shape, not schema alone:** schema2 intentionally
has `control/descendants` and omits `runner/children`. Old7bdee fetches runner
before authentication, so ready/control fails before socket action; gone and
shutdown-handoff cannot certify it. Do not emit legacy alias keys. Add an exact
old-source fixture proving that refusal, including the legacy ready marker.
The marker can remain schema1 because old live/control lookup already refuses.
State/launch/artifact schemas and immutable source binding remain unchanged.

New readers explicitly dispatch schema1 to its original strict full-runner/full-
child validation and exit rules, and schema2 to this contract. They never convert
or relabel schema1. A valid old complete receipt retains only its original
ordinary recovery eligibility, including source/socket/launch checks. A live old
runner retains original authentication; a dead incomplete old run stays refused.
No new schema2 fallback for malformed/incomplete schema1. Unknown versions refuse.

## Authority and observation algorithm

1. Keep full runner executable/argv/UID/boot/PID/start authentication and socket
   peer checks unchanged. Lifetime records cannot enter matches?/runner_matches?,
   any signal path, control-peer validation or private-path deletion authority.
   Existing machine objects/reapers remain the only machine stop authority.
2. Begin each discovery from the fully authenticated runner. For descendant
   traversal read stable boot/PID/start lifetime plus all-task child lists.
   Bracket each child's admission with unchanged parent lifetime and the actual
   parent task-child relation; check the child's PPid against that proved parent.
   Read again to reject replacement during observation. Never admit an unrelated
   PID from a name, argv, cached PPid or a guessed helper identity.
3. Enumerate every task for every reached process; retain all positively observed
   children, including unexpected descendants. Task-set changes/disappearance make
   the pass inconclusive under the existing retry contract. Missing child-list
   data for a still-live task, denied stat/task access, malformed data or changed
   root identity are failures, not empty sets. Preserve partial proved records.
4. Retain and revisit every live observed lifetime during drain, including a
   previously proved descendant that reparented. Reparenting does not remove an
   obligation or authorize a new parent; continue its child discovery and wait.
   A child that reparented before ancestry was proved is not admitted by guess.
   Neither an unexpected child nor a reparented live child permits completion.
5. Legitimate exec, UID or capability changes do not change an already proved
   descendant lifetime. Do not read exe/argv as mandatory descendant authority.
   This explicit change replaces the previous all-descendant-exec-refusal rule.
   An executable change of the fully authenticated **runner/control** still
   refuses. No catch-and-ignore EACCES, helper exception or first-full-tuple trick.
6. A wait-only lifetime is gone only under the same boot when its PID is absent,
   zombie, or has a different start time; unreadable/malformed observations refuse.
   Use stable stat reads/open proc handles as needed to avoid mixed PID samples.
   Never follow a reused PID as the former descendant. This is exit observation,
   never permission to kill the current PID.
7. Complete requires joined machine reapers, a successful quiesced all-task pass,
   every retained lifetime gone, tracker quiesced without failure, then existing
   finalization and a fresh successful proof. Controller release/socket cleanup
   additionally retains all existing complete-receipt, strict runner-gone, exact
   launch, authenticated handoff and namespace checks. A lifetime record by itself
   supplies none of those permissions.

Procfs polling is not an atomic fork history. Preserve the documented limit:
a process that both forks and escapes before any observation cannot be reconstructed.
This repair does not claim stronger containment or reconstruct old missing history.
QEMU's configured helper is synchronously reaped by QEMU; it does not daemonize in
the inspected source. Its observed lifetime/children must still pass the same
rules. No helper success is inferred from its command line.

## Tracker supervision and orderly failure

Latch the first tracker/discovery error, preserve proved records, publish failed
tracking_error/complete=false where safe, withdraw readiness under the same mutex,
and notify the existing one-shot shutdown path. Gate ready on healthy tracker and
a successful current observation; a concurrent failure cannot republish ready.
Engine ready? also rejects tracking_error. Do not treat an unexpected normal
tracker termination as healthy.

Discovery/publication/join errors must not skip one graceful stop of each started
machine or its existing reapers. Repeated stop requests only acknowledge that
drain. Catch/report join failure explicitly; no thread exception may accidentally
unwind the graceful-stop sequence. An unresolved tracking failure cannot later be
cleared by a readable pass or PID disappearance and cannot publish complete,
finalize ownership, release claims or clean ambiguous paths. Keep the owner and
control/drain machinery alive while effects remain uncertain; preserve the first
diagnostic. Controller timeouts remain observation budgets, without force authority.

## One owner3 implementation package

| Files | Boundary |
| --- | --- |
| cluster/lib/kb_process.rb | strict control identity remains; separate lifetime observation, traversal and exact receipt validation |
| cluster/lib/devcluster_runner.rb | schema2 producer, monotonic lifetime inventory, supervised readiness and drain |
| cluster/lib/kb_runtime.rb | process_record/live?/ready?/gone?/control/check_shutdown_exit use explicit version and authority dispatch |
| tools/verify-live-lease.cjs | inline Ruby and JS observer validate new shape, full control stable, descendant lifetimes monotonic; no lifecycle authority |
| tools/fixtures/fake-kb-runner.rb; tools/test-runtime.rb; tools/test-machine.rb; tools/test-ip-inventory.cjs | producers/fixtures and deterministic process/runner/lease controls |
| tools/runtime-verify.rb; tools/test-runtime-verify.rb | any process-proof consumer follows exact receipt contract |
| cluster/runtime-contract.md | supported lifetime vs control semantics, source compatibility and retained failure |

No OSVM fork, new helper/proxy, transport, host wrapper modification, permission
change or general process framework. Other files only when a concrete consumer
requires the same mechanical contract update.

## Acceptance and shortest validation

Quick deterministic controls, using existing seams/barriers:

- Actual helper exec/privilege transition survives lifetime discovery; same-UID
  child exec also remains a tracked obligation. Both refuse complete while live
  and allow positive exit accounting after ordinary exit/reap.
- Unknown live PID, unproved parent, missing/denied live task children, changed
  root executable/argv/UID/boot, mixed PID samples, forged/cyclic/duplicate parent
  records and wrong boot/version/run refuse. Reused PID is never signaled or
  traversed as the old identity. Known reparented and late children remain held.
- Inject failure before/after/concurrent with ready and during drain/join:
  no false ready, first error retained, one graceful stop per started machine,
  reapers continue, incomplete proof/unknown namespaces cannot finalize/release.
- Healthy startup/ordinary stop, task-disappearance retry, quiesced and
  post-cleanup rechecks, lease cancellation/contention and socket ownership stay
  covered. Test schema1 complete compatibility and incomplete refusal, malformed
  forms and exact old7bdee reader versus schema2 refusal.
- Keep the earlier post-exit argv assertion failure separate; under new wait-only
  records tests assert stable lifetime retention, not invented argv stability.
  Do not relabel original failed checks green.

Owner3 runs syntax/focused checks, commits all intended source, then mandatory
independent safety/compatibility/history review before long suites. Fresh watchers
run affected complete source suites and exact required strict checks. The existing
no-network helper evidence can be reused; no repeated diagnostic guests.

Final real acceptance, after review and fresh dedicated bridge capacity/resource
admission: exact fixed source starts healthy, source/guest attestation and capture
lease succeed, the four intended CS/EN list PNGs are captured/strictly validated,
and ordinary public stop proves complete exit and ordinary resource release.
No supervision-only pass substitutes for healthy bridge operation. Use disjoint
owned resources if the old claim cannot be reconciled. Lead/owner3 own that finite
native package; no automatic replay after a failed attempt.

## Old run and compatibility remain separate

Old instance f66a2056-c6e7-4300-904a-c7d2758addae, run
ea841826-207a-4419-8e21-ea61bf3ea678, artifact
18190571-ae21-4206-94ef-c774e04f188c remains under original source/receipts.
[Terminal stop](kb-capacity-evidence/public-stop-result.json) exited1/900.30199s.
All four QEMU exits were0 and all29 recorded PIDs absent, but complete=false,
the exact matching claim and control.sock remained. The
[10:37 owned-state receipt](kb-capacity-evidence/repair-initial-owned-state.json)
confirms those retained effects. Native commands are terminal.

**No supported native reconciliation is established for that dead incomplete
runner.** Mechanism proof supplies no missing historical lifetime/descendant
proof. Retain evidence, disks, claims and socket; do not rewrite receipt fields,
replay stop/reset, force, infer release or apply the new schema retroactively.
Exceptional recovery needs separate positive evidence and operator disposition;
it does not block implementing the future-runtime correction.

New source does not migrate old run/artifact records. Old source must refuse new
process proof; rollback to it cannot manage schema2 runs. Finish new-run ordinary
stop with its owning source before changing controller generation. Immutable
guest/source/artifact attestation remains required. No application deployment,
default-branch integration, production KB write or session lifecycle action is
authorized by this brief.
