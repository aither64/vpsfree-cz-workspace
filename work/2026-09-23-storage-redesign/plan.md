# 2026-09-23-storage-redesign

## Current contract and reader map, 2026-09-26

Deliver one reconciliation engine in two milestones:

- **A — exclusive maintenance repair:** freeze vpsAdmin storage admission,
  establish and hold physical exclusion for the selected dependency closure,
  diagnose with complete DB/ZFS observations, approve provable corrections to
  existing catalog semantics, apply with a journal, verify, then resume
  compatible normal service.
- **B — continuous verification:** publish authoritative physical identities
  and origin links only after the affected writer families maintain them
  through execute, retry, rollback and whole-chain confirmation, or refuse
  before an effect. Complete strict route families and online verification
  separately from A.

A is not a promise that drift cannot recur. It does not publish restrictive
physical identity/origin FKs or mark online scopes verified. Neither milestone
adds user snapshot deletion or redesigns the backup scheduler. Disk-only
objects remain private findings: no catalog import and no ZFS repair/cleanup.

Read this plan for sequence and open decisions; the
[current design contract](storage-integrity-design.md#current-design-contract-2026-09-26)
for invariants, evidence and repair policy; [state.md](state.md) for actual
implementation/review/deployment results; [investigation.md](investigation.md)
for historical production observations; and
[g0-dev-cluster-trial.md](g0-dev-cluster-trial.md) for the disposable trial.
The design's historical packets retain rationale but are not current gates.
Lasting component behavior belongs in vpsAdmin's `docs/storage/integrity-*.md`;
site rollout steps belong in the configuration repository's
`docs/operations/vpsadmin-storage-integrity-deployment.md`. Updating this
session plan does not update those reference pages or authorize deployment.

## Present foundation and limits

Reviewed/published vpsAdmin `fe4f9b0f9` has one additive foundation migration,
authenticated API/WebUI freeze, observer admission/settlement, advisory
capture/compare/planning, test-only strict 5204/5215, NodeActivity and signed
5291 advisory reports. Its production 5204 guard/receipt may be unsigned;
production transaction signing is not a new prerequisite. Signed 5290/5291
operator requests still require the CLI's explicitly unlocked signer.
No production strict activation, executable approval/APPLY, physical identity
publication, `node_quiet` or `repair_ready` follows from this foundation.

The final schema records API user/session actors only; the removed OS launcher,
OS actor migration alternatives and preliminary approval/action tables are
historical. Approval/action persistence will be designed for the selected G2
policy. The paired effect registry is version 5; admission, per-direction
verification impact and per-direction strict support are distinct decisions.

The disposable cluster's current recorded services are `ebe4d8834` with the
reviewed osctld `gc_trash_v1` provider `dcad075a1`; its main G0 admission/
recovery path passed, while exact remaining cases are tracked in the trial
record. The published configuration `fc203cb0` pins service `fe4f9b0f9` but
leaves site staging/production OS pins unchanged. A service pin does not
upgrade osctld. A provider port onto current staging lineage is a separate
review/test/rollout gate; directly selecting `dcad075a1` would discard staging
changes. Consult state for later head changes; these are baseline facts, not
instructions to switch a host.

## Milestone A sequence and acceptance gates

### G0 — finish the disposable freeze trial

Complete remaining primary-Pool and direct/delegated/admin-action-scope
cases, both mode-direction epoch CAS races, denial of a new independent
storage chain, and normal completion/rollback of preexisting work. Verify
transition/catch-up audits and API/WebUI bounded DB-only status. Return to
`read_write` and prove an ordinary unsigned snapshot and normal service work.
G0 requires neither production signing nor full strict writer coverage.
It proves admission and recovery, not node/child/GC exclusion.

### G1a — make capture reliable and genuinely offline

Fix four source-backed capture defects before using its output as repair
evidence (details and anchors are in the current design contract):

1. A capped informational `settled_unverified_intents` count must not defeat
   a genuinely drained status; capped blocker evidence still fails closed.
2. Completed rollback uses `Transaction.done=2`. Classify overlap from
   chain/direction/terminal evidence, not that value alone.
3. Capture must not expand every scope's entire lifetime mutation history
   until its fixed row cap is exceeded. Include all live/unresolved work and
   bounded, explicitly selected historical proof; missing history blocks only
   actions that need it, never becomes proof of absence.
   Read-only source analysis found a second lifetime path: `done=2` storage
   transactions include every old completed rollback. Exact terminal proof
   reads every chain member/result, so a simple state filter would hide
   malformed or previously started skipped work. The first bounded diagnosis
   profile selects the current catalog, every pending-SIP target and its full
   intent/attempt/observation closure, and observable node work through indexed
   queries. It explicitly marks lifetime terminal coverage `unknown`; no
   absent historical row becomes settlement proof. A later maintenance-window
   checkpoint may classify all retained history under a held writer exclusion
   if a proposed action needs it. Do not add a live unresolved registry before
   all DB, API, Node and mixed-version writers can invalidate it reliably.
   Any over-budget required closure remains incomplete.
4. Normalize every captured GUID/owner GUID as an exact uint64 decimal value,
   including SIP/SIPB/filesystem/receipt fields, not just Pool GUIDs.

Also parse offline `compare|dry-run|plan` before loading the full API:
SysConfig class registration can write during startup. Require cold-process
offline operation with no DB, broker or signer access. Keep the single engine,
private HMAC IDs, bounded Rabbit transport, fsync/manual ACK, immutable seals
and reproducible offline output. Interrupted captures remain incomplete and
restart with fresh IDs; do not add capture-resume machinery to this gate.

Acceptance: ordinary completed rollback and more than 1,000 settled intents
do not poison a new run; 40k-object captures remain bounded as historical
journal volume grows; populated uint64 fields round-trip exactly; incomplete/
tampered artifacts cannot be used; cold offline startup performs no DML.
Manifest v2 keeps JSONL record and Node inventory protocol v1, makes the
bounded selection explicit, and requires offline policy v2/plan v3 to carry
the historical-coverage blocker. A sealed complete diagnosis does not grant
historical settlement or an executable action.
Land the v1/v2 offline reader and policy outputs first while Capture still
writes source manifest/policy pair `(1,1)`. Switch Capture to `(2,2)` only in
the same commit as complete bounded selectors and their indexes: the current
selector cannot truthfully claim node-wide observable-work coverage.

### G1b — exclusive maintenance interval and selected scope

Working default for milestone A: a manual storage-only maintenance profile.
Use a reviewed maintenance NixOS generation that persistently removes normal
NodeCtld and, where applicable, osctld runlevels on selected nodes. Drain
ordinary chains first; stop both services, prove their complete service cgroups
and delegated work empty, then establish a fresh physical baseline. A narrow
one-shot signed 5290 runner must execute the API-staged request and complete
its normal DB/broker result path without initializing the ordinary daemon.
An authenticated API maintenance owner prevents read_write while the interval
is held. Close apply authority before restoring services; release the owner
only after health checks and an expected-epoch read_write transition. Reboot,
configuration change, uncontained child, active export/runtime workload or an
unproved osctld route invalidates the profile. The automatic Node/osctld hold
protocol remains a later option for profiles that cannot stop these services.
Neither mechanism exists today; disposable VM proof is required before APPLY.

A quiet sample cannot exclude an effect after the sample. Define an exclusion
mechanism held through capture, approval validation, apply and final verify:
all API/scheduler writers honor admission; preexisting queued/executing/
rollbacking work drains or is explicitly settled; selected Node dispatch,
children and applicable delayed osctld GC/trash producers cannot introduce a
new effect. Prove child termination and startup-orphan handling; an empty
worker table, two equal generations or a cgroup census alone is insufficient.
Keep independent root/unrelated osctld work outside the guarantee and record
the operator's no-out-of-band-write maintenance assumption.

Bind the interval to an active maintenance owner, freeze epoch, selected
node/zpool identities, daemon boot/instance and effect generations. Future
APPLY must acquire that owner under the same singleton row lock; mode change
must reject unfreeze while its repair/verification remains active. A crash or
expired owner never silently releases exclusion or permits unfreeze. Changed
boot, epoch, scope or lost hold invalidates approval. This interlock is future
work, not a property of the current observer toggle.

Keep initial API freeze global, but select complete physical zpools plus all
cross-Pool/DB dependencies. Scan each selected (node, zpool GUID) once per
pass and project its managed roots; unrelated offline nodes need not block a
proved closed selection. Missing relevant evidence does block it. A
storage-only node may declare osctld GC/trash not applicable only from an
explicit reviewed role/capability and route audit, never from a missing socket.

Distinguish execution quiescence from catalog consistency. Fatal/resolved or
phase-5 work still blocks today's drain. Add explicit reviewed physical
resolution evidence under exclusion where needed; do not erase receipts,
declare a failed chain successful or require the anomaly to disappear before
it can be investigated. The exclusion primitive and resolution protocol need
an implementation packet and tests before any readiness claim.

### G2 — one engine, scoped approval and DB-only apply

Add a versioned maintenance policy and immutable approval/action journal to
the same capture/match/plan engine. Bind direct-admin approval to exact
run/capture/report/action-set/evidence digests, private key ID, policy version,
selected closure, freeze epoch and actor/session identity. The private HMAC
labels evidence; it is not admin authorization or physical proof.

Apply only approved existing-catalog corrections under the G1b hold, full
dependency checks, exact targeted ZFS recheck and row CAS. Commit each bounded
atomic action group with before/after images and its checkpoint. After an
uncertain commit, inspect the journal and after-state before retrying. Resume
only under unchanged evidence/exclusion; otherwise recapture and reapprove.
Final same-engine verification is required before compatible unfreeze.
Recovery uses checked inverse DB actions while still excluded, never a blind
database restore over resumed writes.

**Proposed default:** start with the smallest action type whose complete
proof is available; leave the 26 physical origins privately observed. A
current-dependency projection into legacy SIPB parent/count metadata is a
separate proposed policy, requiring semantic fixtures and explicit approval.
No blind counter resets, guessed parents, disk-only imports, ZFS corrections
or new restrictive identity/origin FKs. G2 cannot claim complete legacy repair
when an observed class remains report-only.

### G3 — rehearse repair and compatible resumption

On the disposable topology cluster, exercise real clone/promotion, rollback
and incremental backup chains, plus safely constructed catalog anomalies.
Use the same engine to capture, plan, approve, apply, interrupt after a batch
commit, resume and verify. Test changed epoch/boot/row/dependency rejection,
ambiguous evidence and valid detached/headless no-action cases. Unfreeze and
run the next backup/rollback/rotation workflow with payload checksums.
Recovery must leave the cluster usable without a physical cleanup shortcut.
A separate parent-projection policy needs fixtures proving its complete
counter/dependency semantics before inclusion.

### G4 — separately approved production maintenance window

Prepare a selected-zpool scope, dependency closure, provider/consumer
compatibility matrix, private evidence retention and checked recovery plan.
Take fresh exclusive observations, review the exact plan, approve selected
actions, apply/verify and document unresolved findings before compatible
unfreeze. The window may include the full observed approximately 22-minute
scan plus repairs; no short-freeze promise. API reads stay available.
The existing daily scheduler may skip a due task during freeze without
catch-up; arrange manual retry or explicitly accept next-day execution.
This plan authorizes no production capture, deployment or APPLY.

## Milestone B — continuous verified identities

Retain logical Snapshot IDs/history and SIP/SIPB cardinality; use exact
path/type/snapshot GUID/owner GUID plus catalog identity. Duplicate snapshot
GUIDs are valid, including within one pool. Catalog-owned filesystem identities
represent Pool roots, DIPs, trees, branches and persistent clones. Physical
origin is separate from SIPB's current dependency/history projection.

Publish these authoritative links only after compatible writer families
update them at whole-chain confirmation using durable per-attempt evidence,
or refuse unsupported routes before effects. Intermediate step success
does not publish final ownership. Full receive/promotion/recursive destroy/
rollback/osctl and delayed effects need family-specific proof; test-only
5204/5215 support does not establish this coverage. Old handles and queued
old inputs are part of the cutover gate. After publication, an incompatible
software rollback keeps storage writes disabled; selecting observer mode
does not cure a restrictive-FK confirmation failure after a ZFS effect.

Strict transfer design must cover live filesystem content as well as snapshot
victims: `recv -F` may discard unsnapshotted destination changes even with an
empty snapshot-removal set. Require a proved receive-only/disposable head or
explicitly authorized live-content rollback; prefer no-force or fresh staging
where feasible. Test a divergent live file with no extra destination snapshot.

**Open B decision:** authenticate strict production requests via a designed
trusted-DB binding or an explicitly approved multi-worker signing deployment.
A uses neither to force signing on ordinary production mutations. Keep signed
strict tests and signed 5290/5291 operator requests separate; an unsigned or
old observer receipt never acquires strict provenance retroactively.

## Finding coverage, compatibility and ownership

The [current design's finding table](storage-integrity-design.md#milestone-a-finding-policy)
covers all seven historical classes with proof requirements and no-action
outcomes. Valid detached/headless state and valid outside-capture parents are
not repairs. Historical observations alone never authorize changes.

vpsAdmin owns API/Node admission, observation and the one engine; vpsAdminOS
owns generic delayed-activity/exclusion primitives where required; site
configuration owns provider-first deployment. Do not assume a service flake's
internal OS input updates the deployed OS daemon. Old/unknown providers fail
closed for relevant proof, while upgraded inert observers permit rolling
deployment. Apply additive schema/bootstrap before new code and account for
every relevant API worker before trusting freeze. Keep new audit data on
software rollback; no down-migration or old-writer compatibility is implied by
A's ability to resume its explicitly tested legacy semantics.

Lead owns state, rollout records, verification coordination and integration
decisions; architect owns this current design/plan revision. Historical
investigation and existing unrelated edits remain intact. Use component
checks, mandatory independent review, then monitored integration tests.
No default-branch integration, session lifecycle action or shared-host switch
is authorized by completing these gates.
