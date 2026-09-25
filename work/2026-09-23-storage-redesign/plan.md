# 2026-09-23-storage-redesign

## Completion decision, 2026-09-25

The user requested completion of the guarded writer and one repair engine,
an early disposable dev-cluster trial of authenticated storage freeze, a
reviewable vpsAdmin history and migration set, a prepared configuration
channel pin and site runbook, and permanent lead/reviewer instruction fixes.
No feature migration has been deployed. The reviewed observer branch is not
repair-ready: production strict dispatch and APPLY remain disabled.

First, consolidate unpublished vpsAdmin history and schema. Replace the five
transitional migrations with one final additive foundation migration, retain
fresh-schema singleton bootstrap, and remove superseded host-operator code and
unused approval/action schema. Keep project documentation about lasting
behavior separate from the dated rollout record. The dedicated reviewer must
review the complete rewritten branch, including the migration inventory,
before the early trial.

Next, start the session's disposable storage-topology dev cluster on bridge
networking. Verify schema setup, authenticated API/WebUI mode changes,
read-only admission, audit and bounded catch-up. Return it to read_write and
leave it available to the user. This demonstrates DB admission, not node
quiescence or repair readiness.

Complete strict signed execute/rollback receipts, child and delayed-osctld
quiescence, whole-chain identity publication, and a frozen approval/apply/
resume/verify path in the same reconciler. A non-linking DB repair policy may
be exercised first; publishing physical identity or origin links and then
resuming writes requires full strict coverage. No production APPLY is
authorized. Prepare the vpsadmin channel pin on a configuration feature
branch after the reviewed vpsAdmin SHA is fetchable, but do not deploy shared
int hosts. Add the site deployment and rollback runbook there.

Update workspace and repository instructions and the canonical independent
review skill so leads report done/remaining/blockers/next action and final
branch-wide reviews explicitly reject obsolete unmerged history and schema.
The lead supplies the review packet and resolves findings; the dedicated
reviewer performs the independent assessment. No default-branch integration
is authorized by this plan.

## Approved implementation scope

Improve the vpsAdmin-owned storage catalog so it records and checks the ZFS
state that vpsAdmin commands create. Deliver one rerunnable reconciliation
engine. Its first approved production apply will backfill and correct legacy
metadata; later runs use the same capture, matching, planning, approval,
application and verification code. Ship the code and exercise audit/dry-run
before a separately approved production maintenance window. Do not add a
standalone legacy correction script.

This implementation does not add user snapshot deletion or change daily backup
scheduling. Those improvements follow only after the storage model and
reconciliation are verified. The user-data boundary covers commands initiated
by vpsAdmin, including its osctl wrappers. Independent osctld and root ZFS
changes are outside the guarantee, but a later audit can detect them.

The previous `2026-06-08-vpsadmin-storage-redesign` session was not accessed;
this conversation is bound to the verified current session. The read-only
operator inventory and its findings are in [investigation.md](investigation.md).
The owning vpsAdmin implementation rationale is being reconciled in
[storage-integrity-design.md](storage-integrity-design.md).

## Data model and invariants

- Preserve `Snapshot` as logical user/history identity, `SnapshotInPool` (SIP)
  as one placement per snapshot and dataset in pool, and
  `SnapshotInPoolInBranch` (SIPB) as one backup-branch occurrence. Add nullable
  exact physical path, ZFS snapshot GUID, owner filesystem GUID and verification
  provenance to nonbackup SIPs and backup SIPBs. Null means unverified, not
  absent. GUID is not unique, including within a pool after receive.
- Add `storage_filesystem_identities`, each row owned by exactly one existing
  Pool managed root, DatasetInPool, DatasetTree, Branch or SnapshotInPoolClone.
  It stores node/pool, current path, filesystem GUID, verification evidence
  and the filesystem's
  ZFS clone origin as either none, unverified, unresolved or a real FK to the
  source SIP/SIPB occurrence. This replaces the earlier standalone origin-edge
  proposal. Claim exact current paths uniquely per node, comparing the full
  path when its indexed digest matches. Pool rows retain managed-root path;
  its filesystem identity records the managed-root GUID and Pool records the
  actual zpool-root GUID. SIPB's parent pointer remains logical history, not ZFS
  origin. A known catalog row and an unknown disk-only object must never share
  an invented catalog identity.
- Retain `SIP.reference_count` for old chains. Reconciliation calculates its
  established logical semantics using inbound SIPB references across all
  pools, persistent clone rows and confirmation state. It never resets counts
  to a one-node lower bound. ZFS clone dependencies are checked separately.
- Scope status is unverified, verified or exceptional needs_reconcile.
  Successful commands and ordinary failures with proven no effect or exact
  rollback preserve verification; only an unexpected or unprovable physical
  result enters needs_reconcile.

## One reconciler and mutation contract

- An API-runtime CLI captures a consistent read-only DB view and bounded,
  signed nodectld ZFS inventory. Stream private numbered, hashed chunks to a
  CLI-owned durable spool; incomplete, stale or conflicting captures cannot
  authorize a repair. Report disk-only objects privately and never import or
  destroy them. Bootstrap and steady policies share one matcher and action
  implementation: bootstrap expects null legacy identity; steady treats it as
  unresolved.
- Deterministic plans contain exact target IDs, row versions, before/after
  values, evidence and dependency proof. Admin approval binds selected actions
  to a complete run digest. Apply uses a durable journal and bounded CAS
  transactions; restart verifies committed after-states before resuming. A
  changed freeze epoch or disk/DB evidence requires a new run and approval.
  Reaudit after apply; only complete matching closures become verified.
- Implement a durable global storage-read-only toggle. All new vpsAdmin
  storage-mutating chain admissions and retries check it atomically while
  queuing. Already admitted chains finish or roll back. Authoritative apply
  waits for no relevant queued, executing, rollbacking or unsettled chain or
  invoked subprocess. API reads and signed inventory continue.
- Every vpsAdmin topology command gets a durable intent/token and bounded
  permitted-effect manifest. The node checks exact path, GUID, owner, origin
  and clones before execution and observes the result afterward. Receipts and
  identity changes participate in normal command confirmation. Retry observes
  state before repeating any effect. Strict mode rejects old unguarded mutating
  handles and opaque osctl effects whose footprint cannot be bounded.
- Incremental send/receive pins exact source, base, end and destination
  occurrences. Existing `zfs recv -F` is allowed in strict mode only when a
  complete preflight proves its removal set empty and the destination tip is
  the confirmed common base. Rollback removes only objects proved to have been
  created by that attempt. Preserve normal incremental transfer payloads.

### Storage freeze operator interface correction

The user chose the normal authenticated API and WebUI path instead of the
local root/sudo launcher. A singular admin-only `storage_freeze` API resource
will show the complete bounded DB status, switch modes with a reason and
expected epoch, and run explicit bounded observer catch-up. The Cluster WebUI
will show the same status and allow freeze/unfreeze with CSRF protection; it
will poll the status action for DB drain progress. Catch-up remains API-only.
Retire both storage-freeze CLIs, the launcher, and its sudo policy. The API
must derive the actor from the active admin session and reject impersonated
sessions. Since this feature was never deployed, consolidate the schema to
record only supported API-user transitions. Neither the WebUI nor a true
`db_drained` response claims node
quiescence or physical repair readiness.

Apply the consolidated additive foundation migration before new API code. All API workers
must be upgraded before operators rely on the freeze: old workers can still
admit writers. Removing the CLIs leaves no
supported mode switch while the API is unavailable. No production strict
dispatch, verified scope publication, or repair APPLY is enabled by this
interface change. Review WebUI labels and screenshots through the separate KB
contract workflow; do not publish KB changes without exact approval.

## Production finding contract

The supplied DB/ZFS observations were minutes apart; none alone authorizes a
correction. On a complete frozen run, the same engine must:

- map the 26 reciprocal branch clone origins to filesystem-origin FKs when
  uniquely proved, without inferring SIPB logical parent pointers;
- list five disk-only snapshots and four disk-only filesystems privately,
  classify proven structural ancestors, and keep unknown objects unresolved;
- remove the one DB-only empty branch only with completed-destroy proof,
  physical absence and no incoming/outgoing dependencies;
- resolve the one parent ID against the full DB, treating a valid out-of-scope
  row as a capture artifact;
- investigate 195 counter surpluses using full cross-pool refs and clones,
  correcting individual counts only when exact semantics are proved;
- reconcile 251 pending Dataset confirmations against chains and physical
  state, never using descendant snapshots alone as proof; and
- accept proven detached headless backup placements among the 150 findings;
  restore a head only when unique lifecycle evidence identifies it. Nonhead
  trees need no head branch.

Ambiguous findings have no automatic DB action. Any DB-only catalog removal
requires completed transaction evidence, complete frozen disk absence and
full dependency checks. Reconciliation never changes ZFS.

## Compatibility, delivery and verification

`vpsadmin` owns schema, API, nodectld, CLI, tests and durable design/operations
documentation. `vpsadminos` is reference material for invoked osctl effects;
no vpsAdminOS on-disk format or all-node OS change is currently planned.
`vpsfree-maintenance-tasks` retains the already-published standalone read-only
inventory feature branch, awaiting separate merge approval.

Deploy additive schema and observer-mode readers/writers first. Old API and
node versions ignore new nullable fields; their writes cannot certify a scope.
Do not publish owner-linked identities or origin FKs while old writers can
execute: those FKs could block an old chain's DB confirmation after its ZFS
effect. Before strict enforcement, upgrade all API/scheduler/nodectld writers,
drain old queued work, activate strict legacy-handle refusal, freeze storage
writes, then perform the first approved reconciliation and verify closures.
After linked identities are published, an old-version rollback remains
read-only until a compatible writer returns; observer mode cannot safely
re-enable old writes. No feature content is merged into a default branch
without explicit repository/target approval; implementing and reviewing this
plan are not merge approval.

Test schema cardinality and cross-table identity, promotion, duplicate GUIDs,
clone origins, every observed finding class, ordinary transaction failure,
exact rollback, exceptional unresolved effects, manifest retry, freeze races,
legacy-handle rejection, signed inventory chunk loss/replay at about 40,000
snapshots, and full/incremental transfer payload integrity. Use required hooks,
quick component checks, mandatory independent review, then longer integration
tests with a verification watcher. Rehearse bootstrap on a representative
database/ZFS copy before an operator authorizes production apply.
