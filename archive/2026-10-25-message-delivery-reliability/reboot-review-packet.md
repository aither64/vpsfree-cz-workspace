# Affected review: reboot recovery refinement

Reuse the same independent reviewer and its gpt-6.1-sol/xhigh settings. Retain the
original review.md and its exact ranges. This is an affected-lane rerun because
missing-fence recovery expands the assessed persistence boundary; all four lanes
apply to the bounded shared lock helper, migration and restart tests. Read the
mandatory review skill and applicable lane references as needed. Remain read-only,
with no nested agents. Write only reboot-review.md in this session.

Original packet, plan/design/state and review.md remain authoritative context.
The original Important empty-attachments finding and Advisory timing-identity
finding are fixed and focused checks pass. CI fixture fixes also pass. Their
narrow-remediation evidence is in state.md; no redundant rerun was needed for them.

Parent found a further normal reboot problem before deployment: legacy import
paths are socket-adjacent under /run. Existing ready validation required the
volatile fence to exist, and source-adjacent backups would disappear with it.
The design.md refinement specifies persistent database-sibling backups, ordered
predecessor exclusion, committed-import recovery after source disappearance using
its verified backup, and ready-journal reconstruction of absent fences after
checking every present predecessor. Unexpected present files must never be
replaced or reimported. The database remains authoritative after readiness.

Affected committed library files: codex/submission_migration.go,
codex/submission_database_test.go, docs/submission-storage.md. Compare original
reviewed head 7c84dc4d29566d99d7935627920dd653565aa379, narrow-fix head
0d17f1e347c4592f5a4159ef384106ad287275a2, and refined head
f391c5e98c1cb9adab60dbe3dd5dcf019c0f3089 in the codex-web worktree. The refinement
is folded into the backend commit; final branch still has three logical commits.
No schema or migration from any intermediate feature revision has been deployed,
released, merged or externally consumed. Prior builds and CI VMs are disposable.
Native Codex remains 0.163.0. No live SQLite file, migration, profile activation,
original-attempt repair or machine claim exists yet.

Five new restart/refusal cases pass: ready, ready after old backup removal,
committed import, corrupt backup with missing source, and changed present source.
They assert private persistent backup placement, fence restoration/refusal and
preservation of the unresolved original receipt/digest. Full library Go suite
also passes (~22.7 seconds). Final mechanical downstream pins are being refreshed
and consolidated; they do not add substantive behavior. Their exact final heads
will be provided before final readiness. Inspect complete base-to-head history
for consolidation and migration conclusion against the original packet.

Assess the recovery guarantees at their actual boundaries. A crash before the
import transaction commits can retry from a persistent original source. A legacy
source that existed only under /run had no pre-upgrade reboot durability; the
new committed-import recovery uses its persistent checksummed backup. Do not
claim that the code guarantees recovery before any durable copy exists. Flag
any silent loss or unjustified reimport inside the supported committed boundary.

Earlier candidate results: composed profile build, full portal Go suite, pinned
native contracts, library CI, runtime fast CI and archive/revive CI passed.
Creation CI 40182797562 failed during fork preflight:
`initialize session: error: another dev-session command is changing
2026-10-25-explicit`. Captured browser terminal state/body and source code show
verify_creation_source! calls the pre-existing nonblocking with_slug_lock before
fork initialization. libexec/dev-session is byte-for-byte unchanged in this
feature. The identity of the competing process is unknown. This is distinct from
message admission/storage, not a basis for silently accepting a blind rerun.
Evidence: /tmp/message-delivery-reliability-2026-10-25/final-runtime-ci-failed.log.
Configuration build needed the routine --yes flag and did not activate anything.

The one-off recover-original-attempt.py implements the exact-row/claim and
consistent backup boundaries requested by the original review; it is operational
evidence, does not send messages and has only run on disposable SQLite. Inspect
it if useful to the risk lane, without treating missing history alone as proof.


Concrete persistence-boundary question for risk review: when no import journal
has committed yet, a legacy source disappears at reboot but an unreferenced
persistent checksum backup already exists. Current phase-empty initialization
will see no source. Assess whether that must fail closed instead of initializing
an empty ledger. The committed-import and ready guarantees above do not by
themselves settle the pre-commit orphan-backup case. Report it if it can permit
loss/duplicate delivery inside the promised migration path.


Final exact refreshed heads (all committed):
```json
{
  "codex-web": "f391c5e98c1cb9adab60dbe3dd5dcf019c0f3089",
  "dev-workspace": "48476400290d4d106d0d123ab0268692d3801c48",
  "vpsfree-cz-configuration": "229b8e9f4fd2d0b14e34775fecd3b3a777cab3a9",
  "workspace": "136caa22748d3d4e63e471f4b7c007ab4e58fbdb"
}
```
