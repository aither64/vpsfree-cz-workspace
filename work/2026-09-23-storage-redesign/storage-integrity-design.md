# Storage integrity foundation (proposal)

Status: first-phase design proposal, revised 2026-09-24. This is an implementation
contract, not evidence that the code has shipped or that production data has
been changed. This phase builds the schema, guarded vpsAdmin write paths and one
rerunnable reconciliation engine. Initial legacy backfill/correction uses that
same engine in a later approved production window. User snapshot deletion and
backup scheduler changes are outside this phase.

The integrity boundary covers operations initiated by vpsAdmin, including
nodectld calls to osctl and their rollback paths. Independent osctld work and
direct root ZFS commands are outside the prevention guarantee. Inventory can
detect their effects later. No shared vpsAdminOS fence is required under this
boundary; an osctl operation with unbounded or unobservable effects must be
refused in strict mode until its vpsAdmin wrapper can prove them.

## Evidence and design goals

The corrected read-only comparison in [investigation.md](investigation.md#read-only-production-inventory-2026-09-24)
found 39,576 physical snapshots on one backup node and took about 22 minutes
for two ZFS passes. The DB and ZFS observation windows were separate. Its 660
findings therefore identify questions, not proven permanent defects. Important
classes are 26 reciprocal physical clone edges without DB parent pointers,
five ZFS-only snapshots, four extra filesystems, one DB-only empty branch, 195
reference counts above a one-node lower bound, one parent ID outside that
capture, 251 Dataset rows in confirm-create state and 150 headless backup DIPs.

The first implementation must make new vpsAdmin writes explainable and
reconcilable. A successful or normally rolled-back transaction settles through
the existing confirmation system. Only an unexpected physical outcome that
cannot be safely proved or compensated enters needs_reconcile. A complete
unmatched ZFS object stays in private findings; it never becomes a catalog row
merely because it exists, and reconciliation never destroys it.

## Existing catalog and physical cardinality

Snapshot is the logical object and retains its ID, history, name, label and
confirmation semantics. SnapshotInPool (SIP) is unique by
(snapshot_id, dataset_in_pool_id). On primary/hypervisor pools, one SIP
represents one physical snapshot. On backup pools, SIP represents a logical
placement that can have several SnapshotInPoolInBranch (SIPB) rows. SIPB is
unique by (snapshot_in_pool_id, branch_id); each SIPB represents one physical
snapshot on one branch. Its existing parent-entry pointer describes logical
branch history, not the ZFS origin property of a clone filesystem.

For example, logical Snapshot 700 has one backup SIP 800 in DIP 20. Its
physical A@S is SIPB 901 in Branch A. A rollback creates Branch B by cloning
A@S, so ZFS temporarily reports B.origin = A@S; the intermediate attempt
receipt links that observation to SIPB 901. No current catalog origin field
is published at this step. B does not yet have a second B@S occurrence. Branch
creation then promotes B. In the current Dataset::Rollback chain, the
existing SIPB 901 is reassigned from A to B for snapshots at or before the
rollback target; it is not necessarily replaced by a new SIPB. If final
postflight shows B@S and A.origin = B@S, whole-chain confirmation makes
SIPB 901 record B@S, filesystem A gets
origin_snapshot_in_pool_in_branch_id = 901 and B has
no origin. The SIPB.parent pointer remains
separate logical history. Never predict ownership from names or create a
second row solely because a promotion occurred.

Another logical Snapshot 701 may later have one backup SIP 810 and two
physical SIPBs, one for A@T and one for B@T. A received copy can give both
occurrences the same snapshot GUID; GUID is never unique by itself, even
within one pool. Exact path, owning filesystem GUID, row identity and
operation lineage distinguish them. A nonbackup DIP can also have its own
SIP for Snapshot 701.

A filesystem origin pointing to a disk-only or ambiguous snapshot has status
unresolved and no source FK; its exact raw path remains only in the private
finding.

The working assumption is at most one physical snapshot per nonbackup SIP and
per (SIP, Branch). Validate it on the full estate and promotion/receive
fixtures before claiming verified scopes. A counterexample requires a revised
physical occurrence representation before strict protection, not a guessed
many-to-one match.

## Additive relational schema

The following is a conceptual schema; migration DDL must check existing data
and MariaDB index/constraint behavior. Existing catalog keys and transaction
confirmations stay in place. GUID columns use an unsigned-safe representation
such as DECIMAL(20,0) or canonical 16-digit hexadecimal text. Paths compare
case-sensitively. A unique digest key must be checked against the full path on
collision and fail closed.

| Table | New fields or role | Key and validation |
| --- | --- | --- |
| snapshots | No physical GUID and no deletion or visibility state in this phase | Preserve logical ID/history and existing confirmation. |
| snapshot_in_pools | Nullable zfs_path, zfs_guid, zfs_owner_fs_guid, physical_presence and storage_observation_run_id for nonbackup occurrences | Keep unique (snapshot_id,dataset_in_pool_id). Backup SIP physical fields remain null because its SIPBs carry occurrences. |
| snapshot_in_pool_in_branches | Same nullable physical fields per backup occurrence | Keep unique (snapshot_in_pool_id,branch_id) and self parent FK. SIP and Branch must belong to the same DIP. |
| pools | Nullable zpool_guid; existing filesystem is the expected managed-root path | The zpool GUID anchors the actual zpool root. The managed root uses an owner_pool_id filesystem identity row, even when its path equals the zpool root. Validate nested ancestors as evidence, not invented catalog rows. |
| storage_filesystem_identities | One row per catalogued or pending Pool managed root, DIP, DatasetTree, Branch or SnapshotInPoolClone; node_id, pool_id, exactly one owner FK (owner_pool_id or the four existing owner kinds), zfs_path, path_digest, zfs_guid, origin_state, nullable origin_snapshot_in_pool_id and origin_snapshot_in_pool_in_branch_id, storage_observation_run_id, physical_presence | Unique nonnull owner FK and unique (node_id,path_digest), with full-path collision check. Exactly one owner FK; owner_pool_id requires owner_pool_id = pool_id. Other owners must resolve through their hierarchy to pool_id, and node_id must equal Pool.node_id. Linked origin requires exactly one source FK, other states require none. Both origin FKs are real FKs with ON DELETE RESTRICT; SET NULL would erase a proved dependency. No row for a disk-only filesystem. |
| storage_mutation_intents | UUID token, unique transaction_id, chain_id, node and scope links, protocol version, sealed manifest digest and final phase | Intent commits before node effect. Phases distinguish normal success/failure/rollback from needs_reconcile. Retain for retry and audit. |
| storage_mutation_targets | Surrogate PK and unique (storage_mutation_intent_id,command_key,sequence), action, catalog kind/copied ID and exact expected path/GUID/owner GUID | Immutable, bounded, page-readable effect manifest for multi-object commands; no giant transaction input/output. The signed command carries mutation ID and digest. Expected target rows never acquire mutable observed fields. |
| storage_mutation_attempts and storage_mutation_target_observations | Unique (storage_mutation_intent_id,command_key,direction,attempt_number) receipt with timestamps, result and pre/post digest; per-target observed path digest/GUID/owner/origin and effect outcome keyed by (attempt ID,target ID) | Each completed attempt seals its target observations and digest as append-only evidence. Following chain steps read these observations, not prematurely changed catalog identity. A retry or corrected observation appends a new attempt after re-reading ZFS; it never overwrites an earlier observation. |
| storage_integrity_scopes | Unique pool or DIP scope key, mutation_epoch, state, validator_version and blocker_code | States: unverified, verified, needs_reconcile. Unverified covers legacy rows, stale proof and old/unguarded writes. Needs_reconcile is only for an unexpected physical outcome that cannot be safely proved or remediated. No raw unknown paths. An unassignable object escalates to pool scope. |
| storage_freeze_controls | Singleton row: mode read_write/read_only, monotonic epoch, requested_by_user_id, reason and requested_at | This is an admission gate, not a separate node-ack system. Both mode directions compare the caller's expected epoch under the row lock. |
| storage_freeze_transitions and storage_observer_catch_up_audits | Append-only application audit of mode edges and bounded catch-up requests/results; retain old direct-root/sudo rows. Add nullable `api_user_id`, `api_user_session_id` (both copied unsigned integer IDs) and `api_user_login`; make `operator_uid` nullable. | Append `api=2` to existing actor-source enums without renumbering OS values. For an API row, require all copied API identity fields and null OS UID/login; for an OS row, require OS UID and null API fields. Copied IDs have no cascading FK, so history survives user/session deletion. A DB CHECK can cover these non-FK fields. |
| storage_observation_runs | DB run ID plus private run token; scope FK (whose immutable copied catalog IDs survive deletion), collector version, DB/ZFS capture windows, mutation epoch, counts/report digest, complete/stale state | No raw unknown object rows. A partial or overlapping capture cannot approve repair or mark a scope verified. Retained after catalog or live scope deletion. |
| storage_reconciliation_decisions | (storage_observation_run_id,finding_key) unique; finding/evidence digest, actor, approve/disregard, reason and time | Admin decision binds to immutable evidence. Disregard does not waive physical safety. Retained with its run. |
| storage_reconciliation_actions | (storage_observation_run_id,action_key) unique; finding/approval refs, copied target kind/ID, before/after JSON and digests, state and checkpoint | Idempotent DB-only repair journal; action and checkpoint commit together. Retained with its run and decision after target deletion. |

The filesystem identity row combines physical identity and its optional origin.
It is simpler than repeating identical identity and origin fields on Pool, DIP,
DatasetTree, Branch and SnapshotInPoolClone, and it can enforce one filesystem
path claim across their owners on the same node. For example, Pool 10 on node 3
with filesystem `tank/managed` and zpool GUID 111 has an identity row with
owner_pool_id = pool_id = 10, path `tank/managed` and filesystem GUID 222;
a DIP beneath it has a separate identity row at `tank/managed/dip`, also with
pool_id 10. If Pool.filesystem is `tank`, its owner row has GUID 111 and the
same observed object also supplies the Pool zpool GUID anchor. An intermediate
ancestor such as `tank` in the nested example is inventory evidence without
another managed-root row. A separate storage_origin_edges table would create an independent
edge lifecycle that could drift from its clone owner; it is not proposed.
Snapshot identity remains on SIP/SIPB rather than a second table of roughly
40,000 snapshot occurrences. A SnapshotInPoolClone remains physically present
when its existing state is inactive. Its existing SIP FK is logical; if its
source is on a backup branch, origin_snapshot_in_pool_in_branch_id records
the exact chosen SIPB.

Cross-table validation checks that a filesystem identity's owner hierarchy
resolves to its Pool, a SIPB's Branch and SIP share one DIP, a snapshot path
belongs to its observed owner filesystem GUID, and origin source/target belong
to the same pool. It compares ZFS origin and reverse clones evidence with
the exact source path, GUID and owner GUID. One clone filesystem has at most
one observed origin; one snapshot may have several clones. A null origin FK
with unverified status means no conclusion; status none requires an observed
ZFS no-origin result. A GUID collision is not a defect. Path/GUID/owner or
lineage ambiguity is a finding and blocks the affected dependency closure.
During mixed-version observer mode, observed physical identities and origins
stay in immutable attempt receipts and private reconciliation evidence; do
not create owner-linked filesystem identity rows or publish
origin_snapshot_in_pool_id and origin_snapshot_in_pool_in_branch_id. Those FKs
and the filesystem owner's RESTRICT FKs could make
an old chain's catalog deletion fail at confirmation. The reconciler may
propose identities and links, but does not apply them while old API writers
can execute. An observed origin remains unverified, never none. After strict
cutover, a new
writer may publish a uniquely proved origin link only at whole-chain close.
To delete a linked source SIP/SIPB, the new writer must first prove the physical
dependency ended and atomically remove or update the dependent identity and
source catalog rows in the final confirmation transaction. A failed RESTRICT
check is a safe refusal, not permission to clear the FK or mark no origin.
The Pool managed-root identity is required once its create confirms; a pending
create can hold a path claim with no observed GUID. When the managed root and
zpool root are the same ZFS object, their GUIDs must agree. A nested managed
root needs its own GUID plus the separately observed zpool GUID and ancestor
chain. Two Pool rows on one node cannot claim the same current or pending
path, even though their pool_id values differ.

Reconciliation run, decision, action and mutation receipt history must survive
deletion of the catalog row, Pool or live scope that they describe. Keep copied
original IDs, scope keys and before/after evidence in journals; use nullable
catalog references with SET NULL or retained tombstones, and never cascade
catalog deletion into a journal. Journal-to-run/decision/attempt relations
must also avoid cascading away completed evidence. Completed per-attempt target
observations are immutable; a later check records a new attempt and links it
to the prior receipt instead of updating its observed fields.

SIP.reference_count remains the legacy compatibility projection. Its expected
value, after all chains settle, includes all live SIPB parent references to
that SIP across the full DB plus persistent SnapshotInPoolClone rows, including
inactive clones until purge. It is not the count of physical ZFS clone edges.
Keep it synchronized on new writes, but never reset it from a one-node lower
bound or use zero alone as a physical destruction certificate.

## Node inventory and one reconciliation engine

An operator CLI using the API model runtime under the Supervisor service
identity owns each run. It opens a restricted
private spool and a unique durable per-run Rabbit queue bound to the node direct
exchange before issuing a small signed read-only transaction on a dedicated
inventory queue. The transaction carries run/attempt ID, node/pool, scope,
deadline, protocol version and manifest nonce; it returns only a compact
status/count/digest. Existing signing is optional in source, so the new handle
must reject a missing or invalid signature and the CLI must require an
unlocked signer. A scan may take over 20 minutes and holds no DB transaction.

Node collection emits canonical rows for filesystems and snapshots: exact
name/type, GUID, owning filesystem GUID, origin, reverse clones and available
creation time/TXG. It streams chunks bounded by both count and bytes (initial
limits 100 rows and 64 KiB), with run/attempt, sequence and digest. The CLI
has bounded prefetch and a small unacknowledged window, fsyncs each chunk and
its sequence checkpoint before broker manual ACK, and deduplicates exact
replays within the live attempt. A conflicting duplicate, gap, oversize
chunk, missing final marker, count/hash mismatch or queue overflow makes the
attempt incomplete. Use a durable quota/TTL longer than the scan plus a
bounded live connection-recovery margin; never silently drop messages. A CLI
process interruption or producer crash without a proved final result ends
that attempt and requires a fresh capture; the old queue expires. Operator
restart of the same capture is an optional later feature. Generic API
Supervisor instances do not own the private spool.

The DB side uses keyset pages from one consistent read-only DB snapshot and
records its capture interval. It does not hold that snapshot transaction
during ZFS collection. An unfrozen run with overlapping chains or changed
mutation epochs is advisory/stale. Only a complete frozen/drained observation
can approve DB repair and certify a verified scope. Findings containing disk-only
paths live solely in private spool/report files with restricted access and
retention; database run and decision rows store counts, digests and opaque IDs.

Exactly one engine performs capture, match, classify, plan, approve, apply and
verify. Bootstrap and steady are policy modes, not separate scripts or
algorithms. Bootstrap accepts missing legacy physical fields as input and
proposes identity backfill at volume; steady flags them as unresolved. Both
use the same exact matcher, action types, evidence and safety checks. An
immutable plan has finding/action IDs, target PK/version, before and proposed
after values, evidence digest, dependency closure and reason. Admin approval
selects exact actions or bounded batches and binds to the run/report digest,
scope epoch and row versions. Disregard retains the finding and never turns
an unproved dependency into safe state.

Apply requires global read_only and a drain of preexisting relevant staged,
queued, executing and rollbacking chains, node subprocesses and unresolved
fatal work. The toggle alone does not make a capture frozen. Apply uses small
DB transactions (initially 200-500 rows, benchmarked), orders roots and
catalog-linked filesystem identities before SIP/SIPB identities and origin
links, and commits each action with its checkpoint and before/after journal.
On restart under the same freeze, already-applied actions are skipped only
after checking their after-state; the baseline DB capture plus committed
action journal defines the expected current DB state. Any unrelated DB/ZFS
change or lost freeze invalidates remaining approval and requires a fresh
capture/plan. Re-run the same audit after apply. Initial production legacy
apply is a separately approved rollout window, not a different tool. This
phase does not execute it.

### Reconciler implementation contract

The API-model CLI uses one engine for `capture`, `plan`, `decide`, `apply` and
`verify`; operator resume of an interrupted capture is an optional, separate
later feature. `mode=bootstrap` accepts absent legacy physical fields as
candidates for evidenced backfill;
`mode=steady` reports those same absences as defects. Both modes use the same
capture format, matcher, finding keys, action types and apply code. A run has
one DB observation-run ID and one immutable private capture UUID, one
pool/node/zpool scope, collector and policy versions, and a private spool
manifest binding those IDs. An audit can capture while writes run, but is
advisory. `decide` and `apply` require a complete frozen run; an admin approves
specific action keys and evidence digests, or disregards specific findings.
Disregard never changes verification or dependency safety. The CLI creates no
catalog row from an on-disk-only object and has no ZFS mutation action.

#### First delivery: advisory capture, compare and dry-run

Ship these three operations through the same reconciler library that later
implements approval and apply. The initial API-model CLI surface is
`vpsadmin-storage-reconcile capture --pool-id ID --mode bootstrap|steady
--private-dir ABS`, `compare --run-id ID --private-dir ABS`, and
`dry-run --run-id ID --private-dir ABS`. The latter two consume a completed,
checksummed capture without rescanning; a changed classification policy can
therefore be rerun. They refuse partial, mismatched or unsupported artifacts.
Neither mode changes catalog rows. Do not expose `decide`, `apply`, `resume`
or `verify` as working commands in this delivery. Exit 0 means a valid
advisory report even if it has findings, 2 means incomplete/stale evidence,
and 3 means invalid input/protocol; inspect manifest status and finding counts
rather than interpreting 0 as storage safety.

`capture` may create a Pool `StorageIntegrityScope` and one
`StorageObservationRun` as audit metadata, never a disk-object/catalog row.
Use an absolute private directory owned by the Supervisor service identity
(0700, files 0600); publish versioned JSONL
files and manifest atomically only after fsync. The manifest binds DB run ID,
random run/attempt UUIDs, Pool/Node IDs, exact zpool and managed-root
identities, collector/policy versions, mode, scope/freeze epochs, DB and two
node scan windows, row counts, ordered SHA-256 digests, capabilities and
completion status. The DB run stores only versions, times, counts, digest and
failure code. In observer mode `complete` means both artifacts passed integrity
checks; the manifest/report say `advisory_unguarded`. A known epoch change or
overlapping chain makes it `stale`. Old uninstrumented writers mean a run
without known overlap remains advisory. No audit alone changes a scope to
verified or needs_reconcile or creates decision/action rows.

Canonical records are `db_object` (table, decimal-string PK/FK IDs, exact
persisted fields, confirmation/chain state, row digest), `zfs_object`
(filesystem/volume/snapshot type, exact UTF-8 path, decimal-string GUID,
owning filesystem path/GUID, origin, sorted clones, userrefs,
deferred-destroy, optional creation/TXG with an explicit unavailable marker),
and `finding` (versioned code, stable key, subject catalog ID or opaque disk
key, evidence digest, scope, confidence, blockers and private exact evidence).
JSON null is a known absence, while unavailable is explicit and cannot
satisfy a proof condition. Never use floating-point JSON for 64-bit GUID/TXG,
case-fold paths or reject a pool-local duplicate GUID by itself. Unknown
disk objects and their opaque keys occur only in private files; DB run rows
carry aggregate counts and digests, with no per-object import. `dry-run`
writes a versioned, checksummed private `candidate_action`
with action key, target kind/ID, exact before/after image/digests, proof
requirements and `advisory_unapproved` status, or a reason no action is
provable. It cannot execute an action and writes no decision/action DB row.

The new read-only node transaction handle requires a valid signature over
version, run/attempt UUIDs, node/Pool IDs, zpool/managed roots, nonce,
deadline and per-run routing key. Reject a missing signature or unsupported
scope/version before scanning. List the whole named zpool to close
origin/clone edges outside the selected managed root; include other cataloged
roots as context, but attribute claims only to the selected Pool. Publish at
most 100 records and 64 KiB per chunk to the CLI-owned durable, quota-bound
Rabbit queue, with sequence, counts and SHA-256; a final marker binds both
full scan passes, ordered chunk digests, counts, zpool/roots and windows.
Publish persistent messages with mandatory routing and broker confirms; set
the queue byte limit to reject publishers on overflow rather than discard old
chunks, and set its expiry beyond the scan deadline plus a bounded margin for
live connection recovery. An interrupted capture's old queue expires. A
node-side publish failure fails the read-only transaction; a node-side
success never substitutes for the CLI's verified final manifest.

There is no reverse node-facing application ACK. One ordered node publisher
retries an ambiguously confirmed publish with the identical
`(run, attempt, sequence, payload, digest)`; it never changes a sequence's
bytes. The CLI validates a delivery, appends and fsyncs it, then persists
and fsyncs the contiguous sequence/digest checkpoint before broker manual
ACK. Within the same live attempt, an identical redelivery after checkpoint
matches the stored sequence and digest and is ACKed; a conflicting replay
fails the attempt. This first delivery has no CLI process restart resume.
If the process stops before complete-manifest publication, the attempt is
incomplete regardless of checkpoint fsync or broker ACK, and no partial
artifact can be compared. A hard kill may leave its DB run labelled
`collecting`, but without a complete manifest it is unusable. The operator
starts a new capture with a fresh DB run, run/attempt UUIDs, DB snapshot and
two ZFS passes. Old chunks are never spliced in and the old queue expires.
The final marker is ACKed only after the local digest and pre-ACK seal are
durable. Mark the DB run complete and publish the complete manifest only after
that marker and the matching successful compact result from the signed
read-only transaction are known; either alone is insufficient. An ambiguous
publisher-confirm retry is harmless, but producer crash, missing final
result, queue expiry or an
unrecoverable CLI checkpoint ends the attempt incomplete. Operator resume
would need its own request/nonce/queue/deadline and evidence-validity contract
before it could be added later.

Gaps, oversize/overflow, wrong node/root/GUID/signature, volatile passes and
timeout also make the attempt incomplete. The node uses its existing publish
permission on its own exchange; the CLI requires configure/bind/read/consume
on its queue. No reverse binding or node queue-read ACL is added. Existing
`NodeBunny.publish_wait` handles connection recovery, not consumer
durability. The CLI, not a generic Supervisor, owns the consumer and spool.

The DB side uses one API-model read-only consistent transaction and keyset
pages (initially 1,000 rows), without `.live` filters, including the complete
inbound DB reference closure and transaction evidence specified below. Close
SQL before the long node scan. DB server capture times and connection ID prove
one DB snapshot; cross-host wall clocks are diagnostic. Failed query,
connection replacement, incomplete closure or unsupported capability makes
the run incomplete; detected epoch/chain overlap makes it stale. A complete
physical mismatch is a finding, not a capture failure.

The first compare/dry-run must classify all seven production classes in the
disposition table below: pair 26 reciprocal origins once without guessing
SIPB parent; keep five snapshots and four filesystems private with no action;
keep the DB-only empty Branch report-only until frozen absence plus completed
destroy proof; treat 195 count surpluses as a one-node lower-bound clue until
full DB closure and settled confirmations; resolve the outside parent by
full-DB primary key; examine all 251 pending Datasets with chain proof; and
classify 150 headless backup DIPs against detachment history while suppressing
nonhead branch-head false positives. Unproved cases yield explicit blockers,
never guessed links or refcount resets. Unknown disk objects later block only
their established dependency closure; this observer delivery makes no
deletion decision.

Acceptance tests: API-model DB capture holds one connection and consistent
read-only snapshot while paging more than 40,000 occurrences; node streaming
keeps chunk/prefetch memory bounded for that fixture and a simulated scan
longer than 20 minutes. Missing/conflicting/replayed chunks, ambiguous
publisher confirm with identical retry, producer crash before final result,
CLI crash before/after checkpoint but before broker ACK, crash after final ACK
but before complete-manifest publication, final digest failure,
two-pass volatility, queue overflow and mismatched signed scope produce the
specified outcomes. Matcher fixtures cover duplicate GUIDs in received
copies, same-name occurrences in two branches, clone promotion and reciprocal
origin, all seven finding classes
including valid detached heads and an external parent, and disk-only objects
whose exact paths appear only in private output. Epoch overlap is stale;
findings alone are complete/advisory. For each CLI crash, assert the old run
has no accepted complete manifest, compare/dry-run reject it, and a fresh
capture starts at sequence zero with new run/attempt IDs and new DB and
two-pass ZFS evidence. Assert no catalog mutation, no
decision/action rows, no scope verification and no callable repair. An old
NodeCtld without the new handle yields unsupported/incomplete; never fall
back to an unsigned command or usage-status stream.

This coherent delivery needs a dedicated inventory transaction queue (the
current Transaction and NodeCtld queue lists lack one), a signed read-only
handle, an unlocked signer in the CLI process and broker permission for
the CLI-owned durable run queue. Check the actual `sign_base64` result and
node verification rather than `TransactionSigner.can_sign?`, which currently
reports true without an unlocked key. Put API capture/compare/dry-run and
consistency cases in
`api/spec/models/storage_reconciler_spec.rb`, and signed scope, bounded
stream/replay and overflow cases in
`libnodectld/spec/nodectld/storage_inventory_spec.rb`; use the seven finding
fixtures in both bootstrap and steady policy tests. Deploy those capabilities
together. Mixed-version nodes report unsupported while existing writers stay
in observer mode. Strict mutation guards, frozen certification, approvals
and repair remain disabled pending the later writer coverage and freeze/drain
gates. Legacy production correction is a separately approved run of this
engine, not another tool.

#### Next delivery: one plan-only ProofPlanner

After the committed advisory capture/compare delivery, add `plan --run-id ID
--private-dir ABS` to the same CLI and reconciler library. `dry-run` may delegate
to the same ProofPlanner for compatibility. This slice reads artifacts only:
it does not query a live DB or node, create decision/action/catalog rows, change
scope state, approve a finding, or apply a repair. Every output remains private.
Use a separate plan-policy version and filenames (for example
`candidate-actions-v2.jsonl` and `dry-run-v2.json`), leaving existing v1
dry-run artifacts and stable finding keys intact. Do not make a second legacy
correction algorithm.

Input is the complete manifest, `db.jsonl`, `zfs.jsonl`, matching
`findings-v1.jsonl` and `report-v1.json`, all read through the existing
checksummed private store. Require matching run ID, capture/report digests,
scope, mode, policy versions, key ID, advisory confidence, row counts and
record digests. Recompute the findings from the captured DB/ZFS records with
the named comparator policy and require the exact finding-file digest; a
self-consistent but edited report is not proof. Reject an incomplete/stale
capture, unsupported version, missing finding, changed record or conflicting
catalog claim. Retain the current 300,000-record bound; never turn unavailable
evidence into null or infer absence from uncaptured history. The planner
rejoins exact DB primary keys to path, object type, GUID and owning filesystem
GUID in the node rows;
GUID alone never identifies an occurrence. The fixed Pool::Create support
filesystems at `<Pool.filesystem>/vpsadmin` and its exact `config`,
`download`, and `mount` children are expected structural node objects,
not catalog owners or actionable disk-only objects. Classify only those exact
filesystem paths after checking the selected Pool/root and observed type;
do not suppress snapshots, nested unknown children or clone filesystems
beneath `mount`. Pool::Create can reuse an existing dataset, so its creation
time alone is not an ownership proof. The plan carries an explicit proof
coverage vector: selected DB closure, selected-chain-only confirmations,
whole-zpool two-pass scan, observer mutation epoch, and absent freeze/drain
and strict-writer proof.

A 5204 Snapshot row can retain the logical ` (unconfirmed)` suffix while the
signed target names the physical snapshot without it. Correlate those paths
only through the same SIP ID, transaction/chain and staged 5204 intent and
target: exact `expected_path`, node/Pool/owner, manifest digest, attempt
direction/state and target observation. Require observed ZFS path, GUID and
owning filesystem GUID to agree with a completed, settled receipt before
calling it a proved occurrence. The current DB artifact omits transaction
input/signature, so it cannot independently verify signature authenticity;
record that proof gap. A fatal, started-but-unsettled or uncertain attempt
remains an explicit unresolved intent and blocks identity/name backfill and
any deletion-related inference. Never pair by timestamp, stripped name or
GUID alone, and never turn that pair into an ordinary disk-only import.

Each canonical `candidate_action` record has `plan_policy_version`,
`finding_key`, `finding_code`, `evidence_digest`, `action_key`, `disposition`
(`no_action` or `blocked_candidate`), `possible_operation` (restricted DB-only
enum or null), `target_kind` and decimal-string `target_id` (null for an
unmatched disk object or proposed insert), `owner_kind` and decimal-string
`owner_id` for an insert, exact `before_values` and `after_values` for proposed
columns when derivable (otherwise null), their canonical digests or null,
sorted catalog `preconditions`, sorted `proof_blockers`, `capture_digest`,
`report_digest`, and `executable: false`. A proposed insert uses a null
before-image plus exact owner/path uniqueness preconditions; it is still
blocked. `blocked_candidate` requires a uniquely identified catalog target
or insert owner and exact proposed column values; when these cannot be
derived, emit
`no_action`, null operation/images and explicit proof blockers. Multiple
proposed row changes for one finding have distinct action
keys and explicit dependencies, never an implicit multirow update. The
summary carries run ID, plan policy, capture/report digests, sorted action
digest, disposition/code counts and `executable_count: 0`.

The finding key remains stable across runs under one private HMAC key epoch.
The action key is the private-key HMAC of canonical plan-policy version, run
ID, finding key and evidence digest, operation, target, exact before/after
digests, sorted precondition/dependency digest and capture/report digests. It
is deterministic for the same sealed input but changes when evidence or a
proposed edit changes. This avoids an unkeyed hash of private physical paths.
Sort records by finding key, operation and target before hashing. A repeated
`plan` validates and returns an identical existing artifact; after a crash
between the checksummed action file and summary, it may finish only if the
existing action digest exactly matches recomputation. A mismatch fails
closed. No plan from this advisory slice is an approval token; later apply
requires a fresh frozen/strict run and an approval bound to its exact plan.
Apply the same replay rule to existing offline `compare` and `dry-run`: for
one complete capture, recompute and byte-check already published immutable
files, reuse an identical complete result, and publish only a missing final
summary after verifying its action/finding file. An interrupted file pair is
not a valid report. Do not overwrite a differing file or require a new ZFS
capture merely because offline publication was interrupted. This artifact
replay fix is a prerequisite to publishing ProofPlanner outputs.

| Observed class | Planner disposition in this advisory slice |
| --- | --- |
| Reciprocal physical clone origins | One physical edge per reciprocal ZFS origin/clones pair. If exact clone owner and source SIP or SIPB occurrence uniquely match path, type, GUID, owning filesystem GUID, Pool and existing catalog claims, propose blocked `set_filesystem_origin` (and separately blocked identity backfill if required) with exact row preconditions. Missing/conflicting source or owner is report-only. The physical origin FK belongs on the clone owner's `storage_filesystem_identities` row. Never derive a logical SIPB.parent from this edge. A logical `set_sipb_parent` candidate requires unique completed send/promotion/rollback lineage, which selected-chain-only capture normally lacks. |
| Disk-only snapshots and filesystems | `no_action`, null catalog target and no before/after. First remove the four exact Pool::Create support filesystem paths from this class after type/root checks. Keep other exact paths only in private evidence and opaque finding keys elsewhere; never insert a catalog row or propose ZFS destruction. Mark the affected dependency closure unknown, with Pool fallback if unbounded. |
| DB-only empty Branch | `no_action` now: missing completed intended-destroy confirmation, fresh frozen absence and full inbound/outbound dependency proof. An empty selected branch or absent path is not a delete proof. `remove_branch` becomes a candidate only after all three proofs exist. |
| SIP reference-count surplus | A lower bound is not the exact count. `no_action` unless exact full-DB count semantics, all inbound SIPB and persistent clone rows, pending confirmations and concurrent writers are proved; this capture cannot satisfy them. Never propose `stored := observed minimum`. |
| Out-of-scope SIPB parent | A parent resolved by captured cross-scope PK and hierarchy is `no_action`; an unresolved parent remains blocked pending full-DB lookup. Never relink from ZFS origin. Only unique completed logical chain lineage could support a later parent edit. |
| Pending Dataset create | `no_action` now: completed execute or rollback confirmation, all intended Pool/DIP physical states and full descendants/dependents are needed before a confirm or removal candidate. Selected-chain-only history is insufficient; snapshots or live descendants bar a guessed removal. |
| Headless backup DIP | Zero heads can be valid after DetachBackupHeads: report `no_action` when its completed lineage is proved; otherwise blocked pending lifecycle evidence. Do not elect the highest tree or synthesize a head. Check branch-head cardinality only inside a head tree; nonhead tree alerts are not defects. |

This policy can classify all seven classes without promising that every finding
is repairable. Its most useful candidate is a uniquely matched physical-origin
metadata edit; even that is not executable from an observer capture. Add
fixtures for both capture modes, two SIPBs under one SIP, duplicate received
GUID, promotion changing occurrence owner, reciprocal and one-sided edges,
missing/conflicting owner, a resolved cross-scope parent, valid detachment,
all seven classes, exact Pool support filesystems with an unexpected child,
an unsettled 5204 with logical/physical name difference, and a disk-only
object. Assert physical origin and
SIPB.parent are independent; no disk-only target or catalog import; all
`executable` values false; no DB/node/mutation calls; byte-identical replay;
changed evidence, policy or key changes the action digest; and incomplete,
stale or tampered artifacts reject without publishing a plan. No node
protocol, schema migration or old-writer cutover is required for this slice.
Exercise compare/dry-run/plan twice on one complete capture and crash after
the first output file; identical replay completes, changed replay refuses.
The existing action journal requires nonnull catalog ID and a decision FK,
so it cannot persist a proposed identity-row insert. Leave plan records in
private artifacts; adjust approval/action schema only in the later apply
slice after its exact multirow and freeze contract is settled.
Freeze/drain, strict writer coverage, full historical proof, immutable
approval binding and apply/verify remain separate gates before any repair.

#### Protected operator startup for capture

Run the installed CLI through the existing `vpsadmin-supervisor-ruby` runner
from an authorized interactive operator shell. That wrapper starts a transient
unit as the configured Supervisor user/group, in its package working directory
with its database configuration. The Supervisor package contains the same API
models and `TransactionSigner` as the API package. Production config supplies
a distinct Supervisor DB account and Rabbit account; the runner does not
inherit an API web worker's in-memory signing key. `compare` and `dry-run`
need only the private artifact and do not prompt for a signing passphrase or
connect to RabbitMQ.

For `capture`, require a controlling TTY and read the existing transaction-key
passphrase without echo into the CLI process; pass it directly to
`TransactionSigner.unlock`. The encrypted key comes from
`SysConfig.get(:core, :transaction_key)` through the Supervisor DB connection.
If that account cannot read the key row, abort; the checked configuration does
not prove live database grants.
The admin-only API unlock endpoint unlocks whichever API worker handled that
request; it cannot unlock this separate CLI process. Never accept the
passphrase as an argument, environment variable, report field, queue message
or persistent file. Refuse noninteractive capture until a separate reviewed
secret-input contract exists. Fail before collection if unlock fails or the
actual signed request is blank; `can_sign?` currently returns true even when
the key is locked. Erase transient passphrase buffers where practical and
never log signatures, credentials or config contents.

Read Rabbit hosts/vhost/username/password from the already generated
`VpsAdmin::API.root/config/supervisor.yml` using the Supervisor CLI's existing
safe YAML loader, selecting only connection fields. The Nix Supervisor
service creates that file from its configured password file and sets mode
0440 under its protected state directory. The API Ruby runner has no broker
config, and the API service user has no reason to read the Supervisor file;
do not copy the password into API config, CLI arguments, environment or a new
shared secret. Use Bunny directly for this one run, not
`VpsAdmin::Supervisor.start`, which starts general consumers.

Before inserting the signed inventory transaction, the CLI must declare its
unique durable `node:<node-domain>:storage_inventory:<run-uuid>` queue,
configure its reject-on-overflow quota and expiry, bind it to the existing
`node:<node-domain>` direct exchange with a unique routing key, and start a
manual-ACK consumer. Abort cleanly if any step fails. The node publishes only
to its own exchange; it needs no queue read permission. The repository's
`rabbitmqcfg` Supervisor role grants configure/write/read on all names, and
its node role can write its own node exchange, but the checked production
Nix config records credentials and hosts, not the deployed broker ACL. The
CLI's successful queue declaration, binding and consumer setup is the
Supervisor ACL preflight; a node publish failure is an incomplete attempt.
Never assume the test fixture's permissions describe production. Existing Rabbit
TTL policies for status queues do not cover this per-run queue, so it carries
its own bounded arguments. Failure to load config, read the key, bind/consume
the queue or sign the control request aborts before the node scan; if a run
row has been opened, record `incomplete` with a nonsecret failure code. No new
broker user or credential distribution is required if the deployed Supervisor
permission matches the repository's role contract.

Startup specs must cover an absent TTY, incorrect passphrase, missing key or
DB grant, locked signer's misleading `can_sign?`, unreadable/malformed
Supervisor config, rejected queue declaration/binding and an old node handle.
Each refuses collection without logging secret values or creating catalog
rows. A successful test loads the protected config as the Supervisor identity,
unlocks in that process, signs the exact control payload and receives one
bounded chunk through its own bound queue.

The DB capture pins one API-model ActiveRecord connection and one read-only,
repeatable-read snapshot, paging by primary key without `.live` or other
confirmation filters. It records Pool/Node and zpool/managed-root identities;
all DIPs, Datasets, Trees, Branches, Snapshots, SIPs, SIPBs and persistent
SnapshotInPoolClones in the selected scope; their physical identity and origin
fields; confirmations, involved chains/transactions/attempt receipts,
resource locks and active exports/downloads/mounts. It also reads the full DB
reference closure across other pools: every SIPB pointing to a selected SIPB,
every clone pointing to a selected SIP, and the ancestors and transactions
needed to interpret them. The full DB, not a one-node subset, is required to
compute `reference_count` or resolve an apparently missing SIPB parent. Capture
these exact minimum field groups, in addition to each row's ID, confirmation,
`updated_at` where present, and canonical row digest:

| Capture group | Fields needed for matching or decisions |
| --- | --- |
| Pool and owner hierarchy | Pool node_id, role, filesystem, zpool_guid; DIP pool_id, dataset_id; Dataset ancestry, full_name, current_history_id, object_state; Tree dataset_in_pool_id, index, head; Branch dataset_tree_id, name, index, head. Read all ancestors needed to derive each exact expected path. |
| Snapshot occurrences | Snapshot dataset_id, name, history_id; SIP snapshot_id, dataset_in_pool_id, reference_count, mount_id, zfs_path, zfs_guid, zfs_owner_fs_guid, physical_presence, storage_observation_run_id; SIPB snapshot_in_pool_id, branch_id, snapshot_in_pool_in_branch_id and the same physical fields. |
| Filesystem and dependents | Identity node_id, pool_id, all five owner FKs, zfs_path, path_digest, zfs_guid, origin_state, both origin FKs, physical_presence and storage_observation_run_id; Clone snapshot_in_pool_id, name, state, confirmed; all incoming origin links, mounts, exports and downloads with their owner IDs and status. |
| Transaction proof | Chain ID/type/state/progress/size; Transaction ID/chain/handle/node/status/done/reversible; Confirmation transaction_id, table_name, row_pks, confirm_type, done, attr_changes; mutation intent/target/attempt/immutable observation IDs, phases, digests and relevant paths/GUIDs; resource-lock target and owning chain. |

Record DB server capture window, frozen
toggle epoch and scope mutation epochs; release the DB snapshot before the
long ZFS scan. Cross-host wall-clock order is diagnostic, not a proof of
simultaneity. During frozen capture and apply, recheck the same epoch and
drained chain/child-process state at every stage.

The signed node request includes run/attempt UUID, exact node and Pool IDs,
the audited zpool name, expected zpool GUID when already known, managed-root
paths, nonce, protocol version and deadline. In bootstrap mode a null catalog
zpool GUID is an expected unknown: the node reports its observed GUID in both
passes, and only a unique stable result can be proposed for backfill. The
collector lists the whole named zpool, including paths outside managed roots,
so an origin or reverse clone escaping a managed root is observable. It emits
sorted filesystem/volume/snapshot records with exact case-sensitive path,
type, GUID, owning filesystem path/GUID for snapshots, origin path, reciprocal
clone paths, userrefs, deferred-destroy state, and creation time/TXG where
available. An escaped or unknown object stays only in the private spool. Two
full passes must agree. Each bounded chunk has run/attempt/sequence, row and
byte counts and digest; a final marker binds ordered chunk digests, object
counts, zpool/roots and both scan windows. The CLI ACKs only after fsync and
accepts an exact replay; gaps, conflicting replay, missing fields or final
marker, scan volatility, wrong node/zpool/roots, unclosed origin/clone
references, timeout, queue overflow or missing signature mark the attempt
incomplete. A complete run can still contain findings and cannot by itself
mark every scope verified. A full scan may exceed the earlier 22-minute
managed-root inventory, so the accepted read-only period lasts through scan
and repair. Two matching scans detect ordinary concurrent drift but cannot
prove that an independent privileged actor made no transient change between
passes; such actors are outside the vpsAdmin prevention boundary.

Matching starts with node ID, exact zpool name/observed GUID and managed-root
path/observed GUID. A populated catalog GUID must match; a null legacy GUID
needs the same uniqueness and stability proof as other identity backfills.
For each catalog filesystem owner, derive its expected path from Pool/DIP/
Tree/Branch/Clone relations, then require one object of the right type at
that exact path. Existing identity must also match GUID. For a legacy null
identity, backfill needs unique path ownership and complete owner lineage;
a same-path different-GUID object is replacement evidence, not an automatic
relink. A nonbackup SIP is one snapshot occurrence; a backup SIPB is one
occurrence on its Branch. Match exact `filesystem@snapshot` path, snapshot
GUID and the observed owning filesystem GUID to the unique owner row. A GUID
may legitimately occur in several received copies on one pool; never key a
match or reject a run by GUID alone. Promotion may move an existing SIPB to a
new Branch; require the confirmed chain/attempt lineage before changing its
catalog owner. Match a clone filesystem's ZFS `origin` to one matched SIP or
SIPB using exact source path, GUID and owner GUID, and require the source
snapshot's `clones` list to reciprocate. SIPB.parent is separate logical
history. Any conflicting owner, ambiguous candidate, out-of-scope edge or
missing reciprocal observation remains a finding; it is never guessed into
an FK. An unknown disk path blocks only its proved dependency closure, or
the pool when that closure cannot be bounded.

Finding IDs use a versioned canonical encoding of code, scope, catalog
subject kind/ID and counterpart occurrence or edge key; they exclude run ID
and timestamps so the same problem retains its ID across audits. An unknown
disk object's key is a stable HMAC-SHA256 of node/zpool, exact path, type and
GUID, with a durable key identifier recorded in the private manifest: database
decisions store only that opaque key, while raw paths stay in
the private report. A separate evidence digest binds exact observed rows,
chain proof, capture digests, policy version and scope epoch. Action IDs hash
action version, finding ID, operation, target PK, exact before-image digest
and proposed after-image digest. Approval binds action ID, run/report digest,
evidence digest and freeze epoch. New evidence requires a new approval, even
when the finding ID is unchanged. Sort by keys before hashing; an origin and
its reciprocal clone report form one physical edge finding rather than two
repair actions.

Treat `--private-dir` as a persistent 0700 Supervisor-owned root with separate
per-run directories. On the first capture of an empty root, atomically create
and fsync one 0600 key file containing 32 random bytes; reject symlinks,
unexpected owner/mode and concurrent creation. Its manifest key ID is a
hex fingerprint of the first 16 SHA-256 digest bytes of that random key, not
the key itself. Never put the raw key in
DB rows, reports, argv, environment or logs. Back it up under the same private
retention policy, separately from exported reports. Compare and dry-run load
the manifest's exact key ID and fail closed on a missing or mismatched key;
never silently generate a replacement when prior runs exist. Later approval
and replay bind the finding/action to the run and evidence digests plus that
manifest key ID, not to an opaque finding ID alone.

Rotation is a **later explicit operator action**, not part of initial capture.
It creates a new active key and retains old keys read-only for replay during
their retention period. New captures use the new key ID; findings and pending
approvals do not carry across key IDs without fresh capture and approval.
Suspected compromise invalidates pending approvals under the old key. If a
key is lost, restore a protected backup matching its ID or explicitly start
a new key epoch and recapture; old comparisons, approvals and applies remain
blocked without the original key.

`apply` first checks approved action/evidence keys, complete spool and stable
freeze epoch, then locks the target and relevant graph rows. It validates
model rules and uses conditional updates/deletes whose WHERE clause includes
the exact before-image fields (null-safe comparisons), not `updated_at` alone;
one affected row is required. A create also relies on unique owner/path
claims and locked owner preconditions. For ZFS-derived metadata, make a
targeted fresh node read of the object, source and reciprocal clone edge
immediately before the DB batch. A DB-only catalog deletion additionally
rechecks full physical absence, completed transaction proof and all incoming
and outgoing dependencies. Each bounded batch commits changed rows, the
action's before/after journal and checkpoint atomically. On restart under the
same freeze, an applied action is skipped only when its after-state matches;
a planned action runs only when its before-state and graph digest still match.
Any third state, changed epoch, lost spool, new chain or changed ZFS evidence
blocks the remaining plan and requires a fresh run. A final complete scan
verifies effects; a successful DB commit alone is not verification.

#### First apply pilot: backup SIPB physical identity only (proposal at 662e906b8)

This is the first DB-only policy of the **same** capture→compare→plan→decide→
approve→apply→verify engine, not a legacy script. Its only update is one live
backup `SnapshotInPoolInBranch` (SIPB) from null path/GUID/owner GUID,
unknown physical_presence and null storage_observation_run_id to exact
path/GUID/owner GUID, present and the baseline run ID. These five columns
belong in the frozen v2 plan's exact before/after images and CAS. Reject
partial/missing identity, pending confirmation, unsettled intent, ambiguous
path/owner or conflicting filesystem identity. A Branch filesystem identity
may be absent: prove its expected path from the live catalog hierarchy and
its GUID on ZFS, without inventing an identity row. Do not edit SIPB.parent,
SIP.reference_count, origin FKs, other catalog rows or ZFS. Disk-only objects
remain private report-only findings.

Minimum **forward** schema migration (existing rows remain advisory):

| Table | Additions and constraints |
| --- | --- |
| storage_observation_runs | capture_confidence (advisory/frozen), nullable unsigned freeze_epoch, drain_digest (64 hex), writer_policy_version. Frozen-complete requires all four plus existing complete evidence. Its existing digest is the private manifest digest. |
| storage_reconciliation_approvals (new) | PK; required baseline run and scope FKs; unique baseline run ID for this pilot; immutable manifest_digest, report_digest, finding_digest, v2 plan_digest (summary), action_file_digest, selected_action_set_digest, selected_evidence_set_digest, key_id, freeze_epoch, scope_mutation_epoch and apply_policy_version; copied authenticated admin user ID and local UID/login, nonempty reason and approved_at; state approved/applying/verified/invalidated, nullable final verification_run_id FK/time and failure_code. Retain history with restrictive rather than cascading FKs. |
| storage_freeze_controls | Nullable active_reconciliation_approval_id FK. Under singleton row lock, only one approval owns the global freeze. Refuse read_write while active; a crash retains ownership. Clear only after successful verification or explicit audited invalidation. |
| storage_reconciliation_decisions | Existing unique (run,finding_key), evidence_digest, actor, reason and state suffice. decide inserts once; an exact repeat is idempotent, a conflicting choice needs a new run. Seal approved decisions when the approval references them. |
| storage_reconciliation_actions | Keep existing required catalog kind/ID and before/after JSON/digests for this SIPB update. Add nullable approval FK for migration (required by pilot service), operation, finding_key, evidence_digest, immutable v2 plan_record_digest and precondition_digest, ordinal, immutable targeted_recheck_digest/time, nullable verification_run_id FK/time. Unique (approval_id,ordinal) plus existing unique (run_id,action_key). planned/applied/verified/blocked is the checkpoint; target update and planned→applied commit together. Validate action/decision/approval/run agreement in the service. A future insert policy can relax target-ID/before-image nullability in another forward migration; it uses this engine, not another correction script. |

Avoid MariaDB CHECK expressions over FK columns; use actual FKs, unique
indexes and model/service cross-row validation. Store no raw unknown disk
paths or HMAC key in these rows. The protected API-runtime CLI gains
`capture --frozen --mode bootstrap`, then existing `compare` and v2 `plan`;
`decide --run-id --finding-key --choice approve|disregard --reason`;
`approve --run-id --plan-digest --action-keys-file --reason`;
`apply --approval-id --batch-size`, `resume --approval-id` and
`verify --approval-id`. Record authenticated local operator identity and a
validated admin user ID; read action keys from a protected 0600 file. CLI
output contains opaque IDs/counts, not member paths.

An old `advisory_unguarded` v2 plan never becomes approvable merely because
read_only is enabled later. A **new frozen** capture starts after a complete
node-inclusive drain, records read_only/freeze and scope epochs, strict writer
registry/protocol version and drain attestation, and seals a stable DB snapshot
plus two same-digest whole-zpool passes with root/zpool GUID checks. Its
manifest, DB run, findings, report and v2 plan must match byte for byte.
The v2 proposal itself remains `executable: false`; the pilot approval
service independently discharges only the specific freeze/strict/drain and
fresh-graph blockers. Require a live confirmed SIPB, SIP, Branch, Tree,
Dataset and Snapshot; selected-chain history alone does not prove that.
Any other blocker refuses approval. Preserve advisory v2 bytes and behavior.

`approve` reopens the exact private HMAC key ID and recomputes the sealed
manifest, report/finding digest, full v2 action file/summary digest and sorted
selected full-action/evidence digests. Every selected action must be the
allowed SIPB operation, have an approved matching decision, exact target and
five-column images, no dependencies on another operation and a dischargable
blocker set. Under the freeze row lock, require read_only, approved epoch,
unchanged scope epoch, complete drain and no active approval; atomically
insert the immutable approval plus ordered planned actions and claim the
freeze. An identical retry returns the same approval. A changed plan, set,
evidence, key, actor decision or epoch fails closed. Disregard retains the
finding and never waives safety.

`apply` additionally requires all API/scheduler/NodeCtld mutation writers
upgraded, old queued/executing/rollbacking handles and children drained, and
strict legacy-handle refusal active. The present DB-only drain command is
insufficient; node-attested quiescence, including attributable osctl
children/delayed effects, is a blocking prerequisite. Immediately before
each DB batch, a new signed **read-only** NodeCtld exact-path inspection
uses bounded request/reply pages, tied to nonce, transaction ID, node, Pool,
zpool GUID and selected SIPB IDs. Require terminal success and exact
snapshot path/type/GUID, owner path/type/GUID and root GUID. Same name with
a different GUID is name reuse; duplicate GUID at another path is valid.
Fsync each immutable private recheck artifact before a DB batch references
its digest. This does not replace whole-zpool baseline/final scans.

Start with at most 32 SIPBs per SQL batch, benchmark before increasing it.
Lock freeze row, approval and SIPB targets in PK order. Re-resolve and check
SIP, Snapshot, Branch, Tree, DIP and Pool hierarchy/confirmation and unique
physical-path claims against the plan; require the same freeze/scope epochs
and recheck evidence. A null-safe conditional UPDATE of exactly the five
approved columns must affect one row. Update action before/after journal,
recheck digest and applied state in the **same** transaction. A failed batch
rolls back; after an uncertain COMMIT, read action state and exact target
after-state rather than replaying blindly. No `updated_at`-only CAS.

`resume` opens the same approval and private key under the unchanged
read_only epoch and repeats drain. A fresh complete two-pass physical scan
must match a canonical object-state digest of the baseline inventory,
including paths, types, GUIDs, owners and clone edges. Exclude run/attempt
IDs and observation timestamps from this comparison while sealing each
scan's own manifest separately. A fresh relevant-catalog DB view
must equal baseline projected through exactly the committed action journal
(exclude the engine's own new run/journal metadata). Applied actions are
skipped only after five-column after-state and sealed recheck proof match;
planned actions require original before-state. Any third state, unrelated
catalog/ZFS change, missing artifact, new chain, changed epoch or key
invalidates remaining work and requires a new capture/plan/approval.
Never blindly undo a proved identity.

`verify` uses the same full capture/compare engine with a new run under the
same freeze. The final stable scan must show exact target after-images and
no corresponding legacy-identity findings before actions become verified and
the approval closes. Other findings remain visible; this pilot cannot mark
the entire Pool verified. Verification failure retains applied journals and
freeze ownership for operator-directed reconciliation.

All seven investigated classes remain in this same engine for later policy
gates: physical origins need exact owner links and full-node claims;
disk-only objects never import; Branch deletion needs completed destroy and
full absence; counters need exact global semantics; SIPB.parent needs logical
lineage; pending Datasets need completed confirmation proof; detached headless
DIPs can be valid no-action findings. No second legacy algorithm appears.
Test altered/advisory/tampered artifacts, action/evidence/key/epoch binding,
operator decisions, duplicate GUID versus name reuse, hierarchy/owner
conflict, old-writer or live child, batch rollback and crash after COMMIT,
partial 40k-row resume, final verification failure, and exact no-ZFS-write/
no-disk-only-import/no-origin-or-parent-edit boundaries. An old API may read
published metadata but must remain storage read_only until a compatible
strict writer returns; additive schema alone never enables apply.

### Disposition of the captured finding classes

| Class | Evidence and permissible action |
| --- | --- |
| 26 reciprocal clone origins, 52 report lines | One physical-edge finding per reciprocal pair. After unique path/GUID/owner/source SIPB matching, approved bootstrap may create/confirm the filesystem identity and its origin FK. Do not infer SIPB.parent from ZFS; change that logical pointer only with unique completed send/rollback confirmation evidence. Ambiguous or disk-only source is report-only. |
| Five ZFS-only snapshots and four extra filesystems | Targeted repeat with GUID, owner, origin/clones, creation time/TXG and transaction overlap. Classify proven structural ancestors separately. All stay private, report-only: never import or destroy them. Unknown dependencies block the affected closure, or the pool if closure is unbounded. |
| One DB-only empty Branch | Approved row removal is possible only with complete frozen physical absence, a completed intended destroy transaction/confirmation, no SIPB, clone origin, export/download/mount or other dependent in the full DB, and a fresh targeted absence check. If any proof is missing, report-only. |
| 195 SIP count surpluses versus one-node lower bound | Recompute from all pools' live SIPB parent references and persistent clone rows, including inactive clones until purge. Settle or explain pending confirmations first. Approved per-SIP CAS update is possible only if the exact full-DB count semantics and value are proved; one-node surplus alone is report-only. |
| One parent ID outside the node capture | Resolve by primary key in the full DB and validate branch/pool/history. A valid external row closes a capture-scope finding with no repair. Relink/clear only with unique completed transaction lineage; physical origin alone cannot prove a logical pointer. Otherwise report-only. |
| 251 Dataset confirm-create rows | Inspect creating chain, transaction status, `TransactionConfirmation.done`, exact physical DIPs on every Pool, descendants and dependencies. Approved confirm-create is possible only when completed execute proof and all intended DIPs agree; approved removal requires completed failed/rollback proof, full physical absence and zero dependencies. Existing backup snapshots rule out blind removal. Otherwise report-only. |
| 150 headless backup DIPs | A completed DetachBackupHeads can make zero head trees valid; record that classification with no repair. For a proven active DIP, approved head-flag correction needs unique lifecycle proof of the intended tree and branch and matching physical state. Otherwise report-only; do not select highest index. The 161 original no-head-branch alerts on nonhead trees were false positives: a nonhead tree need not have a head branch. |

An action that changes a reference count, parent pointer, head flag or
confirmation state is a DB metadata correction. No reconciliation action
modifies ZFS. A DB-only catalog removal needs completed transaction proof,
complete frozen physical absence and full inbound/outbound dependency
validation. Unresolved findings remain visible to operators.

## Guarded vpsAdmin write flow and ordinary outcomes

TransactionChain.fire2 is the normal API chain admission point. In the same
short SQL transaction that stages/queues a storage-mutating chain, lock the
singleton freeze row, reject read_only, acquire existing resource locks in a
stable order and seal the mutation target manifest. Classify nested chains and
every vpsAdmin-initiated command that can change topology, including execute
and rollback through osctl wrappers. Read-only inventory is exempt. A mutation
advances the affected scope epoch so an overlapping capture becomes stale;
the epoch is an audit generation, while exact row/GUID preconditions and
resource locks control command execution. Do not reject an unrelated queued
operation solely because the pool epoch advanced.

NodeCtld requires a signed guarded command and checks its sealed manifest,
live identities and dependency closure immediately before each effect.
Command.save runs after EACH step. It commits that step's transaction status
and an immutable attempt receipt with exact postflight identities, including
intermediate clone/promote or rename state. Following steps read those
receipts under the chain's locks. They must not publish a new SIP, SIPB or
filesystem identity as current catalog state merely because an intermediate
step succeeded: a later step may fail and roll the chain back. The affected
scope's mutation epoch makes concurrent inventory stale during this interval.

At whole-chain execute success, or after a completed rollback whose physical
poststate is proved, the final Command.save transaction applies or reverts
catalog identity fields together with TransactionConfirmations and chain
closure. It derives the final identity from the attempt receipts and checks
the expected closure, row versions and operation lineage. A fatal/unsettled
rollback does not publish a guessed final identity or run confirmations.
The normal failure path leaves existing current identity fields intact or
restores their staged before-images. A long ZFS command holds no DB
transaction. If DB save is lost after a physical effect, the committed
intent remains; retry by token re-reads ZFS before acting and appends a
new receipt, never repeats a name-only effect blindly.

Existing on_save methods are narrow exceptions: Snapshot 5204 and
GroupSnapshot 5215 write generated logical Snapshot name/time during an
intermediate Command.save because later legacy steps need them; their
created rows still depend on end-of-chain confirmation and rollback cleanup.
DownloadSnapshot 5004 writes size/checksum, and VPS password handling
scrubs transaction input. These do not license early publication of physical
identity or origin. The guarded flow should pass generated physical identity
to following steps through attempt receipts and explicitly test later
rollback of each early logical attribute. Before strict mode, new writes
record observed identities in receipts without publishing catalog physical
identity fields or owner-linked filesystem rows. A mixed fleet cannot assert
verified state while old writers can act without the gate.
Once such an unguarded effect is detected, invalidate its affected scope
to unverified (pool fallback if the scope is unknown); strict mode rejects
legacy handles before they execute.

| Observed result | Transaction and scope outcome |
| --- | --- |
| Preflight refuses before effect | Normal failed chain/rollback and confirmation cleanup; no needs_reconcile. |
| Execute succeeds and exact postflight matches | Normal continuation and end-of-chain confirmation. Preserve verified state when the full dependency closure remains proved; otherwise mark unverified. A previously unverified scope stays so until a complete audit. |
| Command returns error/timeout but re-read proves no effect, or the exact intended effect | Settle normally as failure or verified success, respectively; return code alone does not quarantine. |
| Partial effect, then identity-bound compensation restores recorded prestate | Normal failed/rolled-back chain and confirmation cleanup. Preserve verified state when the exact prior closure is proved restored; otherwise mark unverified, not needs_reconcile. |
| Postflight differs and safe compensation or observation cannot establish an expected final state; rollback fails unresolved; or an osctl effect is unbounded | Mark only affected closure needs_reconcile, retain intent/receipt and stop dependent destructive work. |

Current Confirmations.run uses per-transaction status and final chain
direction: a successful create is confirmed, a failed or rolled-back create
is removed, and a failed destroy returns to confirmed. A failed rollback
closes the chain fatal without confirmations and retains locks. Fatal chain
state alone is an operational problem; needs_reconcile is reserved for a
physical outcome that cannot be safely proved or remediated. Never classify
every ordinary failed chain as topology drift.

The global toggle is simple: switch storage_freeze_controls to read_only
under its row lock and atomically reject all new mutating admissions. Existing
chains finish or roll back. Do not park a partially executed chain and call
the system frozen; never-started queued chains must drain or be cancelled
before repair. The repair CLI verifies no relevant staged/queued/running/
rollbacking chain, child process or unresolved receipt remains. API reads
continue. A final full scan/repair may keep storage writes read-only for
22 minutes or longer. No per-node ACK table or scoped freeze is necessary
for the first cutover.

During read_only, a due daily backup task may be logged and skipped when its
storage chain is rejected; this phase does not add automatic catch-up. The
maintenance-window procedure must check for skipped due backups after
unfreeze and arrange a manual retry when needed, or record that they will run
on the next day's normal schedule. Scheduler catch-up policy belongs to the
later scheduler redesign.

### Incremental transfer and implicit destruction

The source, base and end snapshots must be exact SIP/SIPB occurrences with
known GUID/owner, pinned through existing chain locks and queue reservations.
The destination common base must have matching identity. Network receive
handle 5220 invokes zfs recv -F; local send handle 5223 reaches the same
flag through libosctl Zfs::Stream.send_recv. Both can discard destination
snapshots, and both rollback by snapshot name. Strict mode permits -F only
when a complete live preflight proves its victim set empty and its origin/
clone dependency closure known. A nonempty or unbounded victim set needs a
separately designed staging/branch route; until that route exists, reject
that transfer form. Postflight verifies exact received identities. Rollback
may remove only objects proved created by that token and GUID, never a reused
name. A destructive -F result cannot be called rolled back by deleting its
new snapshots.

The same effect-bound rule covers local rollback with zfs rollback -r,
branch clone+promote, dataset rename/replace, recursive/trash operations,
group snapshot and export-clone cleanup. A wrapper that cannot bound its
effect set and await completion is unsupported in strict mode, even if its
legacy handle currently reports success.

### Guarded-writer coverage after the observer reconciler

Build a versioned effect registry shared by API manifest creation and the
NodeCtld strict dispatcher. Classify every transaction handle, including
rollback and nested `call_cmd` effects, as bounded topology, proved no
topology, or unsupported. Unknown handles fail closed in strict mode. A test
enumerates API transaction types, node handlers and all direct `zfs`, `osctl`
and stream call sites, so a new command cannot silently inherit a no-topology
classification. Treat the groups below as the initial registry, not proof
that an osctl command's implementation has a bounded footprint.

| Handles | Physical contract in execute **and rollback** |
| --- | --- |
| 5204, 5215 | Snapshot/create group: pin each owner filesystem GUID and prove every target path missing; receipt each created snapshot GUID. Rollback destroys only token-created GUIDs. Group recovery checks every member, not only the first. |
| 5212 | Snapshot destroy: exact path/GUID/owner, zero holds/userrefs, known reciprocal clone/origin graph and no dependency or active use before ZFS; prove absence afterward. It is irreversible and has no name-only retry. |
| 5201, 5209, 5213, 5250 | Filesystem, rollback staging, tree and Pool-root creation: list all `-p` ancestors/work datasets, distinguish preexisting GUIDs from token-created objects, observe each new GUID. Rollback may destroy only created objects with an empty dependency closure; 5250 may reuse a root and must not delete it. |
| 5203, 5207, 5214, 5218 | Dataset/branch/tree/export-clone removal: inventory complete recursive contents and inbound/outbound clone edges. For 5203, an osctl trash move is a GUID-preserving path change until its destination and asynchronous cleanup are proved; do not report plain absence as destruction. Clone removal must also prove the source's reciprocal clone edge cleared. |
| 5206, 5217, 5230 | Branch clone+promote, export clone and rename: bind source snapshot or filesystem GUID, target absence and affected descendant paths. Postflight checks target GUID, every moved snapshot owner/path and both sides of origin/clones; rollback uses those receipt identities, never the old name alone. Promotion can reassign an existing SIPB rather than create a new one. |
| 5208, 5211 | Local `rollback -r` and apply rollback: enumerate possible snapshot victims before effect; require the victim set empty in this phase. Apply rollback also needs exact child move, original-to-trash and replacement GUID/path receipts. If the trash/child effect cannot be bounded and compensated, reject this operation in strict mode. |
| 5220, 5223 | Network and local receive: pin source/base/end and destination common-base occurrence GUIDs, owner GUIDs and locks; prove the `-F` victim set empty immediately before spawn. Record every produced snapshot GUID and postflight edge. On failure inspect the actual destination before any compensation; rollback may remove only token-created GUIDs. A nonempty or unknown victim set is unsupported until a staging design exists. |
| 5221, 5222, 5290 | Send and inventory are read-only; send pins exact source/base/end through the chain and RecvCheck 5222 must check GUID/owner rather than name alone. |
| 5224; 5216, 5219, 5225-5228; 5229; 5004-5005 | 5224 changes logical Snapshot metadata only and must follow chain-close/receipt rules. The next group changes ZFS properties/mount state, 5229 changes file contents, and downloads create/remove files rather than ZFS catalog objects; prove their no-topology classification and retain source snapshot locks where needed. |
| 3001-3003, 3040, 3030-3035, 2029 | VPS create/destroy/reinstall/copy/send/cancel/cleanup/boot through osctl: require command-specific source/destination root GUIDs, exact created/moved/removed snapshots and filesystems, complete osctl effect, and guarded rollback. Nested `call_cmd` destroy, forced `ct del`, `ct send cancel` and `ct send cleanup` are effects, not cleanup exceptions. Until osctl supplies bounded completion/evidence, mark these routes unsupported in strict mode. |
| 1001-1003, 8001, 2020, 2034, 3041 | Start/stop/restart and the feature, network-interface rename, map-mode and chown routes that invoke `ct stop` or `ct restart` need osctl topology contracts. Boot/impermanence can create random temporary datasets, and stop/restart can trigger asynchronous trash GC, so name-pattern exclusion alone is insufficient. Until delayed effects can be observed, these routes are unsupported in strict mode. |
| 3303, 5301-5303; other osctl wrappers | The inspected osctld recover-cleanup 3303 acts on cgroups/network rather than ZFS, but its invoked route still needs a parity test. Mount operations and remaining osctl wrappers need proved no-topology classifications; do not infer one from their vpsAdmin command name. Unknown effects fail closed. |

The current API admission checks only transaction classes tagged
`storage_effect`. Start/stop/restart 1001-1003 and network-interface rename
2020 are untagged despite their osctl calls, so the registry/parity gate must
correct admission as well as NodeCtld dispatch before read_only or strict
mode claims full vpsAdmin-initiated topology coverage.

#### Next writer/freeze delivery boundary (vpsAdmin 10819d32c)

At this head, 5204 has an observer receipt for a guarded nonbackup SIP, but
`StorageMutationJournal.strict_mode?` is false. `StorageMutationAdmission`
checks only tagged chains/transactions. The existing singleton read_only row
is a real SQL admission lock for those tagged writers, not yet a complete
vpsAdmin storage freeze. The following statuses describe what can be made
exact with current ZFS observations, not what is already safe to enable.
Strict dispatch must default-deny every unlisted handle in **both** execute
and rollback, including an old queued handle with no guard.

| Priority and handles | Bound needed for execute and rollback; strict status until proved |
| --- | --- |
| First: 5204 | Extend its existing signed intent, started attempt and path/GUID/owner postflight to a strict nonbackup create. Preflight missing at exact owner GUID; postflight one new GUID; rollback only that token-created GUID. A missing/ambiguous prior attempt, live child or failed observation is uncertain. Backup 5204 currently has no bounded subject and remains unsupported. |
| Next direct creates: 5201, 5209, 5213, 5215, 5217 | Feasible with a complete per-target manifest: enumerate `-p` ancestors and `.rollback` stage; group snapshot checks **every** owner/member; clone records exact source SIP/SIPB, reciprocal edge and clone FS GUID. Receipt created bit and old GUID for each target. Rollback removes only token-created GUIDs after dependency checks. Until each handle has these checks, it remains unsupported, not a generic safe create. |
| Next graph changes: 5206, 5230, 5250 | Feasible only with full before/after descendant snapshot and origin/clone graph. Promotion can invert the origin and reassign an existing SIPB; rename `-p` may create ancestors. Pool creation must record which of root and four support filesystems preexisted and their GUID/property values; rollback must never destroy a reused root or support filesystem. Existing unconditional 5250 rollback is unsupported. |
| Direct removals: 5207, 5214, 5218; 5212 | Branch/tree/export-clone removal can be bounded by exact empty/dependency closure, GUID-bound postflight and no name-only retry; an irreversible successful destroy is normal success, not a rollbackable operation. Snapshot destroy 5212 is explicitly unsupported in this first phase because snapshot deletion is not being implemented. Existing internal callers must fail admission rather than reach its legacy destroy. |
| Rollback/replacement: 5208, 5211, 5203 | 5208 `zfs rollback -r` is supportable only after a live exact victim enumeration proves the newer-snapshot set empty, the target GUID/owner is pinned, and postflight preserves the snapshot graph; until then unsupported. 5211 moves children, trashes origin and renames replacement; 5203 moves to osctl trash and may be pruned later. Their delayed or multi-object effects are unsupported until each moved GUID and asynchronous completion is proved. |
| Transfer: 5220, 5223 | Both reach `zfs recv -F`. Strict mode rejects full receive into an existing destination and every incremental receive with an unknown or nonempty rollback victim set. Pin source/base/end and destination common-base occurrence by exact path/GUID/owner, lock them, prove no later destination snapshots or clone dependents immediately before spawn, and record produced GUIDs after child completion. Existing rollback destroys by name and is unsupported; compensation may remove only token-created GUIDs after fresh dependency checks. No nonempty-victim `-F` route is designed in this phase. |
| Read/no-topology candidates: 5221, 5222, 5290; 5224; 5216, 5219, 5225-5229; 5004-5005 | Send and inventory only observe ZFS; RecvCheck 5222 still needs GUID/owner for transfer proof. 5224 edits logical name, not ZFS, but must obey chain-close identity semantics. Property/mount and data/file operations need tested no-topology classifications; 5229 and download writes are still storage writes for read_only admission. Classify rollback separately. No `storage` queue or read-only name implies safety by itself. |
| Opaque osctl: 3001-3003, 3030-3035, 3040, 2029, 1001-1003, 2020, 2034, 3041, 8001, 3303, 5301-5303 and other wrappers | Explicitly unsupported in strict mode until each invoked osctl route and rollback has a bounded effect set, synchronous completion or an attributable delayed-effect receipt. Start/stop/restart can create or release impermanence/boot datasets; trash-bin and run-dataset GC can move or recursively destroy them after the command returns. Even 3303 and mount wrappers need a proved no-topology classification. The registry must include nested `call_cmd`, forced delete, send cancel/cleanup and rollback calls. |

The minimum common contract is a versioned effect registry with
`handle`, `execute_class`, `rollback_class`, `scope_resolver`, and
`guard_protocol`; API chain staging and NodeCtld dispatch must agree by a
parity test. API `Transaction.fire_chained` checks the registry inside the
staging transaction even when a class lacks `storage_effect`; top-level and
nested chain effects are checked before commit. A signed guard binds token,
transaction/chain, handle/direction, node, Pool/DIP scope epochs and the
canonical paged target-manifest digest. NodeCtld checks that guard and a
persisted started-attempt row before the child. Each target row needs catalog
owner ID, exact path/type/GUID/owner GUID, intended created/moved/removed
effect and relevant source/base or origin edge. Immutable observations record
before/after presence, path/GUID/owner, origin and reverse-clone graph digest,
child process-group identity, reaped completion, and a result code. A shell
or pipeline leader PID alone does not prove that its ZFS/osctl descendants
stopped. Existing attempt/observation columns do not yet store child
completion, so guarded child-bearing handles need an additive durable receipt
field or row before strict support. The digest must cover the enumerated
target rows, not replace them; large manifests are paged from DB rather than
embedded in the signed input. A retry must reobserve the same token and
attempt history before another effect.

Normal outcomes follow physical proof: a refused preflight or failed child
with proved no effect settles the chain normally; exact intended postflight
continues to whole-chain confirmation; identity-bound compensation restoring
the full prior graph settles as ordinary rollback. Those paths leave a
verified scope verified only when its entire dependency closure remains
proved; otherwise it becomes unverified. Fatal/needs_reconcile is reserved
for a started attempt whose prior effect cannot be inspected, a possibly
live hard-killed child, changed GUID/name reuse, incomplete postflight,
unbounded osctl effect or failed compensation. Keep the intent and locks;
never run final confirmations or publish SIP/SIPB/filesystem identity during
intermediate Command.save. The chain-close SQL transaction publishes the
final identity together with confirmations only after whole execute or
rollback proof. Existing 5204/5215 early logical name/time `on_save` updates
need explicit rollback tests; they are not physical identity publication.

The first small code slice is registry/admission parity plus the authenticated
API `storage_freeze` control/status interface described below. Make every known topology or
possibly topology-changing osctl handle pass the singleton admission check,
including 1001-1003 and 2020, and classify its rollback; keep strict dispatch
activation disabled. The toggle serializes with staging, rejects new API and
scheduler storage chains, and leaves existing chains to execute or settle.

Implement the versioned registry as explicit per-handle API and NodeCtld
declarations with one canonical effect-class vocabulary and a parity spec;
do not infer effects from a queue, command name or `storage_effect` tag. Each
entry states execute and rollback classes separately (`no_storage`,
`read_only`, `data_or_property_write`, `bounded_topology`, or
`opaque_topology`), whether read_only admission is required, a separate
per-direction verification impact (`none`, `dependency`, `catalog_identity`,
or `physical_topology`), scope resolver, and guard protocol/version. The
effect class alone does not decide whether a command invalidates a verified
physical graph. An impact of `none` has resolver `none`; every other impact
requires admission and an explicit resolver. The parity spec enumerates every
loaded API `Transaction.registered_types` handle and NodeCtld `Command` handler,
checks paired handle/direction classifications, and fails for an
unclassified handle or nested `call_cmd`/osctl route. Explicit unmatched
entries require a documented unsupported classification: at this revision,
API handle 5225 (`EnsureUgidOffset`) has no NodeCtld handler and must not be
treated as a successful paired property writer. Catalog-only chain
classes also need explicit admission classification. A missing entry cannot
default to read-only. Carry the registry version in any future signed guard
and its persisted manifest digest; NodeCtld must refuse an unknown strict
version before dispatch. Observer-mode version mismatch invalidates touched
scope verification, but does not claim guarded execution.

| Verification impact | Admitted handles and required observer behavior |
| --- | --- |
| `none` | Gate proven content, configuration and runtime-only handles under read_only without a physical mutation intent or scope epoch change: 2002-2005, 2013, 2016-2019, 2022-2023, 2027-2028, 2030-2033, 2035-2036, 4005-4006, 5005, 5261-5264 and 5229. A completed 5004 download also leaves the ZFS object graph intact. Its temporary snapshot mount and source SIP/SIPB locks remain active-use evidence until the chain and child drain; read_only rejects a new download, and frozen repair waits for an existing one. Do not mark every Pool unverified after it finishes. |
| `dependency` | 5216, 5219 and 5226-5228 change ZFS properties, mounts or sharing; 5301-5303 change configured or active mounts; 5401-5407 change NFS export server state or references to a DIP/SIP clone. These affect use and deletion eligibility even if path/GUID/origin do not change. Record a distinctly typed dependency intent and advance the affected owner Pool scope(s), using node-wide fallback only when exact owners cannot be proved. The export server uses host files, tmpfs and bind mounts (`osctl-exportfs/operations/server/{create,delete,spawn}.rb`); do not infer a ZFS dataset create from its server name. |
| `catalog_identity` | 5224 edits logical Snapshot name/time. Record catalog invalidation for its exact SIP/SIPB owner scope; no physical ZFS postflight is implied. Catalog-only DetachBackupHeads has its own admitted chain effect. |
| `physical_topology` | 5204 retains its exact Pool/DIP subject and target; 1001-1003, 2020 and other still unproved osctl/ZFS topology handles retain conservative node-Pool invalidation in observer mode. Their strict command support remains disabled until bounded effect receipts exist. |

The 7001/7002 osctl user new/delete route remains conservatively
`physical_topology` with node-Pool scope until its osctld implementation proves
it cannot change managed ZFS objects; do not put it in `none` by name alone.
API-only 5225 is unsupported on the
node: gate and refuse it rather than issuing a fictitious physical receipt.
Dependency or catalog intents must have their own kind and scope, not claim a
physical effect. A settled `none` operation may still need an in-flight chain
or resource lock in the drain query; lack of an intent is not a drain exemption.

The API insertion points are `TransactionChain.fire2` for top-level chains,
`TransactionChain.use_in` and `do_append` for nested chains, and
`Transaction.fire_chained` as the final per-handle check before params, intent
staging or signing. All checks run in the chain's staging SQL transaction and
lock singleton `storage_freeze_controls` row 1 before its commit; an admission
refusal rolls back any earlier staging rows in that SQL transaction. The
read_only switch takes the same row lock.
The registry drives `StorageMutationJournal.stage!` only when verification
impact is not `none`; admission alone never calls it. An absent
`storage_mutation_subject` on a physical-topology handle remains an opaque
node-wide observer intent, not a strict manifest. On NodeCtld, inspect the
registered handle and actual direction before handler execution and again
before an internal
rollback; strict mode requires matching signed registry version, manifest,
started attempt and exact effect contract. The next delivery adds parity and
admission only: strict dispatch and catalog identity publication remain off.

Generic observer intents, including positively proved opaque backup 5204,
need a terminal **settled_unverified** phase (append its enum value without
renumbering existing phases). A generic command
result does not prove the ZFS graph. Wait until the whole chain closes normally
as `done` or `failed`: in the same SQL transaction as `Command.save` runs all
confirmations and closes the chain, require every member transaction final,
every confirmation done, and no started or uncertain physical attempt. The
coarse NodeCtld completion receipt is the saved transaction direction,
done/status/output and finish time; a follower skipped by chain failure must
be marked as skipped in that close path. Then settle all generic intents for
the chain, retaining their target journal and unverified scope. An ordinary
failed command, completed rollback or keep-going failure can meet this rule;
none becomes `needs_reconcile` solely from its status. Per-command completion
while a chain can still roll back, fatal/administratively resolved chains,
unfinished confirmations and uncertain 5204 attempts cannot meet it.

An old NodeCtld cannot perform this new transition. A bounded API-runtime
catch-up may apply the same final-chain, transaction-result and confirmation
predicates to old prepared generic intents, using an idempotent phase CAS and
recording settlement provenance. An opaque backup 5204 may also settle only
when its persisted input identifies one backup Pool on the command's node,
contains no storage guard, and it has at least one linked scope and target,
including that Pool. Every target must belong to this intent and its scope,
have command key 5204 and kind `observer_unbounded`, and have no catalog link;
there must be no attempt row of any state. A guarded or
receipt-bearing 5204 never enters generic catch-up; its signed attempt and
physical receipt control its phase. Missing, conflicting or malformed 5204
evidence remains prepared, appears as a blocked catch-up chain, and keeps
`db_drained` false. Even after generic settlement, an old NodeCtld
child may outlive its saved result: `db_drained` proves only DB control-flow
quiescence; frozen repair separately needs node worker/child quiescence and a
fresh full scan. This transition must ship with the drain command. The prior
registry/admission commit may run independently only as observer
instrumentation; it cannot claim a usable drain or repair gate.

Catch-up must page fairly through prepared chains: a fixed first page of
blocked chains must not hide later eligible chains. It must report oversized
or malformed terminal chains as blockers rather than silently leaving them
prepared. A successful catch-up proves terminal DB control flow, not the
physical graph. Deploy the nullable settlement-provenance column before a new
NodeCtld writes it at chain close; otherwise a schema error can roll back the
command's DB close after its physical effect. Run catch-up only through the
separate authenticated `settle_observer` action while read_only is held;
`show` performs no settlement.

Replace both storage-freeze CLIs and the fixed sudo/Nix launcher with one
singular authenticated `storage_freeze` API resource. `show` returns one
bounded `StorageFreezeStatus.snapshot`; `read_only`, `read_write` and
`settle_observer` are explicit POST actions. The API's normal action-scope
hook must authorize each action, including `show`. Its action authorization
and mutating service both require the authenticated session's own user to be
active with API role `admin`, the session to be open and owned by that user,
and `admin_id` to be null. Re-fetch and lock that session and user in the
mode-change transaction before recording the actor. An admin-created detached token, borrowed WebUI
token or other impersonated session cannot act for the creator. The WebUI
also suppresses controls during its PHP-only `context_switch` state. Never
trust a submitted actor ID or a WebUI privilege flag as API authority:
WebUI `isAdmin()` includes support-level users whom API `role == :admin`
excludes. Authorize again after entering the service transaction so a stale
role/session cannot switch mode. A direct admin token can use these API
actions when it meets the same session and scope predicates.

Both mode actions require a nonempty, control-character-free reason of at
most 255 characters and `expected_epoch`. Under
the singleton row lock, compare the epoch and the action's required prior
mode (`read_write` for `read_only`, `read_only` for `read_write`), reject stale/already-changed
state without a new event, then update mode, increment epoch, set
`requested_by_user_id` from the authenticated user and append one transition
with old/new mode, epochs, copied API user/session IDs and login, reason and
timestamp in the same SQL transaction. Return mode/epoch; a stale request is
a conflict, including a stale `read_only` request. Preserve existing OS audit
rows unchanged: append `api` to the actor-source enum, make OS UID nullable
only for new API rows, and require copied API identity only on API rows. The
copied IDs survive user/session removal; do not place a cascading FK on history.
The actor alternatives need model/service validation and a compatible DB
CHECK over the copied, non-FK actor columns. The audit remains
application-append-only, not tamper-proof against
direct SQL or host root.

`settle_observer` requires a reason, `expected_epoch`, an integer cursor and
page limit 1..100. It is the only catch-up entry point. Require read_only at
the same expected epoch; create a requested audit event with copied API actor,
request UUID, epoch and page bounds before work, and retain it on interruption.
Run only one bounded page through `StorageObserverSettlement.catch_up!`;
each committed batch rechecks mode and epoch. Append a completed event with
the bounded outcome after the call. An epoch change aborts the remaining
page without undoing already settled intents; retry uses a fresh request and
the returned cursor after inspecting the prior audit. `show` never calls
catch-up or performs settlement.

The Cluster admin WebUI offers the same mode actions through POST forms with
CSRF, reason and the displayed epoch, and polls `show` for the complete
bounded DB status. It does not offer catch-up. Expose mode, epoch,
`stable_epoch`, `db_drained`, `repair_ready=false`, every named blocker count,
the capped-count names and bounded opaque chain/intent ID samples; state when
counts hit their cap. Never show member paths or interpret DB drain as node
worker, live child, ZFS or repair-readiness proof. A page refresh obtains a
new bounded DB observation; there is no long-running API `drain` poll. Normal
API authentication may update session bookkeeping, but the `show` action
does no storage-state write. The DB drain predicate checks relevant
staged/queued/rollbacking chains (including
formerly untagged handles), waiting transactions, nonterminal intents
(`prepared`, `executing`, `needs_reconcile`), started/uncertain attempts and
retained chain resource locks. A relevant `fatal` or `resolved` chain remains
a blocker by state even if its transactions have finished, its locks were
released and it has no intent. `resolved` is currently only an admin state
change, not proof; only an explicit reviewed resolution record could later
exempt it. `done=2` is a completed rollback, not waiting work. An ordinarily
failed, fully compensated chain closes as `failed` and may drain. Join by
transaction handle **or**
intent/chain identity so an old unguarded command is not invisible. Count
normal in-flight confirmations as part of its chain; do not stop an already
started rollback. Report settled_unverified intent counts separately without
counting them as in-flight or treating their scopes as verified. The API
reports `db_drained=true` only when those DB blocker counts are zero at a
stable read_only epoch; otherwise it reports false.
NodeCtld's current worker/subprocess status route is local to the node, so
the API leaves `repair_ready=false`, never inferring it
from DB zeroes. A later frozen repair run needs independent fresh node evidence
of no workers, queued transactions or live children. Missing node evidence,
unknown child lifetime or unattributable delayed osctl GC blocks repair
readiness. Each poll is a fresh bounded read, not one long SQL transaction.
Avoid repeated full scans of historical transactions, intents and attempts;
make selective predicates and supporting indexes part of the status delivery.

Deploy an additive actor-audit migration before any API worker writes an API
actor event. Existing OS CLI code must still be able to append its legacy
events during a rolling upgrade; do not renumber its actor enum values or
rewrite prior rows. Ship the new API actions on every API instance before
showing the WebUI controls or relying on them as the sole operator path:
an old instance lacks the resource and can still admit storage work. Retain
the old launcher only during that controlled upgrade, then remove both
`api/bin/vpsadmin-storage-freeze*` programs, the read-only CLI support file,
the `storage-freeze.nix` import/module/option/sudo rule, its Nix flake check,
launcher VM test and stale CI selections. Do not leave a hidden alternative
mode-changing CLI. Schema rollback to a version that cannot represent API
actor rows is unsafe after the first API event; restore a compatible API or
hold storage read_only during a rollback. No interface rollout enables
production strict dispatch, repair APPLY or verified-scope publication.
The WebUI caches the API description in its PHP session; exercise an existing
admin login across the API rollout so the new resource is discovered or the
page handles an unavailable action without misleading mode state.

The NodeCtld admin `chain` route currently locks the freeze row for `retry`
and forced `confirm`, but `release` deletes resource locks and `resolve`
updates chain state without that gate. In this first slice, put both inside a
DB transaction that locks row 1 before their mutation and refuse them during
read_only; conservatively gate all admin chains until storage-chain
classification is complete. Read-only `confirmations` inspection and normal
in-flight `Command.save` confirmation/rollback continue. In read_write,
release/resolve must still preserve any unresolved intent/attempt as a drain
blocker and must not change `needs_reconcile` merely by changing chain state.
In `read_write`, retry of a storage chain must either re-admit and advance its
affected scope epochs with a fresh attempt/intent or be refused. Reopening a
settled chain with its old journal would let a later physical replay evade
verification invalidation. This is a hard gate before any scope is treated as
verified or repair/apply relies on its epoch. During the observer-only slice,
all affected scopes remain unverified and `repair_ready` remains false;
read_only already refuses retry during a frozen window. If retry remains
available in read_write observer mode, record that limitation explicitly.
Never park an already started chain and call it frozen. A full global
read_only period may last through the final scan and repair. No new node ACK
table or fleet-wide deployment is part of this slice.

Test registry parity against every API transaction handle, NodeCtld handler,
direct ZFS/osctl call and nested rollback; missing classification fails.
Assert read_only refuses 2002/2003/5004/5005 before params, while read_write
2002/2003/5005 and a settled 5004 leave verified Pool epochs unchanged and
create no physical intent. An active 5004 must still appear in drain. Test
5216 and 5405 with only their referenced Pool dependency scope, 5224 with a
catalog-identity scope, 5204 with its exact Pool/DIP target and 1001 with its
conservative node-Pool closure. Check impact and resolver parity in both
execute and rollback, including no-op rollback directions and conservative
7001/7002 classification.
Race a read_only switch against top-level, nested, scheduler and formerly
untagged admissions; assert one side wins atomically and no rejected chain
persists. Verify a queued/preexisting chain still appears in drain, fatal
and started receipts block repair-ready, force retry/confirm/release/resolve
cannot erase that blocker, and a settled chain clears it.
For the replacement interface, test all four resource action scopes,
unauthenticated/user/support/suspended-admin/delegated-session refusal,
direct active admin success, and a WebUI context switch using a borrowed
token. Test both mode directions with concurrent/stale epoch requests,
same-mode refusal, atomic control/event rollback, preservation of old OS
audit rows, and a fresh-schema plus upgraded-schema migration. Test bounded
`show` counts/caps and `repair_ready=false`, no catch-up side effect from
status, CSRF-protected WebUI POSTs, an interrupted catch-up requested audit,
epoch change between catch-up batches, and cursor replay without double
settlement. WebUI access must match API admin level, not its broader
`isAdmin()` flag. Exercise the upgraded API behind a mixed-version load
balancer before enabling the page; the old instance must never be mistaken
for a successful control endpoint.
Simulate old API/NodeCtld versions and an old signed or unsigned 5212/5220
handle: this first observer slice may record/invalidate but must not claim
strict safety. Strict refusal activates only after all writers/nodes are
upgraded, old queued/executing/rollbacking commands and children drain, and
the NodeCtld dispatcher refuses every unguarded legacy mutation before any
effect. After origin FKs are published, rollback to old API remains read_only
with strict node refusal; it cannot safely resume writes. Later per-handle
tests inject pre-spawn, mid-child, post-effect/pre-save and rollback failures,
name reuse, root reuse, promotion inversion, empty/nonempty `-F` victims and
delayed GC, and verify normal versus needs_reconcile outcomes.

Every bounded command seals affected Pool/DIP scope, exact path/GUID/owner,
before graph digest, allowed created/moved/removed set, incoming dependency
closure, and expected rollback state before any child starts. The started
attempt commits first. On each execute or rollback step, an immutable receipt
records full observed before/after identities and the child/osctl completion
result. A retry reobserves the exact token's effect; an ambiguous prior start,
hard kill with a possibly live child, or unbounded delayed osctl effect fails
to needs_reconcile without blind compensation. Proven refusal before effect,
ordinary failure with proven no effect, and exact compensated rollback settle
normally. No catalog identity or origin FK is published during an intermediate
Command.save: following steps use receipts, and the final Command.save locks
the graph then applies final identity changes or restores before-images in
the same SQL transaction as TransactionConfirmations and chain close. Existing
Snapshot/GroupSnapshot early logical name/time updates remain narrow legacy
exceptions and require rollback tests. A fatal/unproved chain does not run
final confirmations or release its dependency locks.

For the next **test-only** strict dispatcher checkpoint, keep observer mode as
the production default and give each handle and direction an explicit support
state, separate from admission and verification impact:

| Initial support state | Execute/rollback directions |
| --- | --- |
| `proved_no_storage_effect` | Existing `no_storage` or `read_only` directions, including the explicit no-op overrides: rollback 1003, 2029, 3031, 3034, 3303, 5212, 5221, 5222, 5228, 5229 and 5290, and execute 3035. This proves only absence of a managed-storage effect in that direction; it does not excuse an earlier unproved step in the chain. |
| `guarded_5204_v1` | Execute and rollback of a nonbackup 5204 only with the exact two-target Pool/DIP manifest, one SIP-linked physical snapshot target, a current registry version, and its existing started-attempt/preflight/postflight receipt. An opaque backup 5204 remains unsupported. |
| `unsupported` | Every other mutating direction, including data and dependency writers with `admission_required` even when their verification impact is `none`, group snapshots, receive `-F`, osctl wrappers and all unknown handles or versions. A guard-shaped hash cannot upgrade an unsupported entry. |

Bump the paired API/Node registry version from 2 to 3 when adding these states
and put version 3 inside the signed `storage_guard` and its manifest digest;
keep the separate guard protocol version 1. For `guarded_5204_v1`, test-only strict
evaluation requires a nonempty valid signature, matching relational command
options, exact local registry version and supported direction before handler
construction or any child. Proved no-storage directions retain their existing
wire authentication rules, but cannot settle earlier unproved physical work.
New observer nodes may still accept old signed or unsigned commands under
their existing rules. Strict evaluation refuses old mutating wire without a
registry version even when its old signature is valid. Do not expose a
production strict activation setting in this checkpoint.

The earlier 5204 receipt lookup accepted the first matching target and permitted
a null expected owner GUID. Those were hard blockers to **executing** 5204 as
strict-guarded, even in a test-only mode: require exactly one SIP-linked physical
target within the two-target manifest, its catalog owner and a nonnull matching
filesystem GUID before allowing it.
Execute requires no earlier attempt in that direction; rollback requires the
specific successful execute identity and no earlier rollback attempt.
The existing early Snapshot name/time `on_save` also prevents a claim of
chain-atomic catalog identity or verified scope; test-only dispatch must not
publish either. A pre-dispatch refusal must not reuse the current
`rollback_without_execute` path as an ordinary completion: it can save a
rollback `done` value without a matching terminal rollback output or finish
time. Until a distinct proved-before-start refusal receipt and matching
confirmation direction are implemented, close rejected mutating commands
fatal, retain locks, skip confirmations and refuse compensation. A later
proved-before-start refusal may settle as an ordinary failed execute only if
all earlier effects in its chain are independently proved or safely rolled
back. A prior started attempt, unsupported rollback or hard-killed child that
may still run stays fatal; mark `needs_reconcile` only for an actually uncertain
physical outcome. Old wire alone cannot prove an earlier old-node attempt had
no effect. Check the policy before `Command#safe_call` and before
`Commands::Base#call_cmd` can invoke a nested effect.

The next bounded writer slice should persist strict provenance for 5204 and
prove it again when a later, harmless chain member closes the chain. Adding a
second guarded handle first would leave the current-member-only closure rule
in place. Add nullable `strict_dispatch_registry_version` and
`strict_signed_input_digest` to `storage_mutation_attempts`; both are null for
old nodes and observer dispatch. A test-only strict 5204 writes version 3 and
the SHA-256 digest of the exact signed transaction input in its started-attempt
INSERT, after validating the signature, relational options, guard, exact
two-target shape and owner identity, and before starting ZFS. The marker columns
are an internal DB receipt extension: the existing signed guard already carries
registry version 3, so no new wire field or production strict switch is needed.
An execute and its rollback need separate marked attempts. At the trusted
DB-writer boundary, ActiveRecord rejects updates to either marker even while
started (so observer nulls cannot be promoted); no database trigger is required.

The reviewed API producer emits sequence 0 `observer_unbounded` on the Pool
scope and sequence 1 `snapshot_create` on the DIP scope, with exactly two
corresponding intent-scope links. Preflight and final closure require those
two rows and links with the correct sequence, kind and scope; extra, missing or
malformed rows refuse closure. Only sequence 1 links the SIP and receives a
physical observation; the Pool observer row does not prove an effect. This
corrects the earlier one-total-target assumption from producer/consumer review.

At every test-only strict chain close, under the same DB transaction as final
confirmations, lock the bounded chain and accept either all members whose
execute and rollback directions prove no storage effect, or one 5204 anywhere
in the chain plus such harmless members. For the 5204, verify its retained
signature against exact input, registry/guard/intent/two-target binding, both
attempt markers and input digests, and the full persisted terminal observations:
phase 2 proves one created snapshot; phase 3 proves its exact compensation;
phase 4 proves no physical change. Require the phase, transaction direction,
attempt count and status to agree. The current member has no special proof
exemption. Unknown, observer, old-node or incomplete attempts, an unsupported
prior effect, a second guarded 5204, and a changed signed input refuse normal
closure, keep locks and signatures, and skip confirmations. A started or
otherwise uncertain physical outcome enters `needs_reconcile`; a completed
observer receipt without strict provenance leaves the scope unverified. Hard
kill or failed postflight never manufactures a terminal strict proof.

Deploy the additive nullable migration before upgraded NodeCtld. An old node
ignores the columns; a new observer node leaves them null. Old and observer
attempts cannot be retroactively marked strict. Keep production strict off
through mixed versions, and do not claim verified scopes or repair readiness
from these receipts. Software rollback can read the additive schema, but it
cannot preserve strict multi-step closure; any eventual strict cutover must
freeze and drain before a rollback to old writers. Test a strict 5204 followed
by a no-storage tail for success and rollback, plus observer/null provenance,
changed input, missing receipt, hard kill, and an unsupported earlier member.

This slice has deliberately narrow chain coverage. Direct `Dataset::Snapshot`
appends one 5204 with Snapshot/SIP creation confirmations; `Dataset::GroupSnapshot`
uses 5215, and `Dataset::Backup` composes transfer and rotation without a 5204.
Non-rsync `Dataset::Migrate` uses `Dataset::Snapshot` within its larger chain;
one observed shape embeds four 5204 steps plus transfer handles. A single-5204
provenance rule does not prove that migration, group snapshot, backup or restore
chain. The 5209 temporary rollback filesystem is part of restore before
send/apply-rollback, and its rollback destroys by name, so guarding 5209 alone
adds no complete strict chain. `Command.save` persists each step's `on_save`
and attempt result, while confirmations and normal close run only at the final
step. A later harmless tail may use the earlier strict receipt at that close;
no new catalog physical identity field is published on an intermediate step.
An observer or old-node phase-2 receipt remains unproved even if its API input
was signed with registry version 3: only the strict Node's started-attempt
marker establishes strict dispatch provenance.

### Next test-only writer gate: bounded 5215 group snapshot

Choose paired execute/rollback support for **5215** before another single-object
handle. `Dataset::GroupSnapshot` is a real one-command chain, including the
scheduled `DatasetAction` route; strict support can therefore close a useful
chain. Restrict this first contract to 1-32 distinct DIPs on one nonbackup Pool
and node. Reject an empty group, duplicate DIP/path, mixed Pool/node, absent
owner identity or larger group before ZFS. Before the handler or started
attempt, require a persisted chain of exactly one transaction: this 5215
member, with signed chain ID/handle matching its stored row and the current
command ID equal to that sole transaction ID.
Repeat the sole-member check at final chain proof; a harmless tail cannot
make an embedded 5215 eligible. The 5215 embedded in VPS replace remains
unsupported.
These limits govern test-only strict dispatch; observer production keeps its
current behavior.

The API must stage one Pool observer target plus one SIP-linked physical target
per selected DIP, with deterministic SIP-ID order, exact intent-scope links and
no extra targets. It must sign the complete ordered snapshot IDs/paths, pinned
owner filesystem GUIDs and one planned timestamp name taken from the logical
Snapshots (without ` (unconfirmed)`). Current 5215 stages only opaque node-Pool
observer targets, sends no planned name and can select DIPs across nodes; the
Node chooses its own name. The strict Node must verify the signed list against
every catalog link, owner and path, then prove every target path missing before
a durable started attempt and before the multi-path `zfs snapshot`. The strict
branch refuses a preexisting state file, uses only the signed planned name,
and neither reads nor writes the legacy first-snapshot recovery file; that
file is unresolved evidence, not a no-effect receipt.

Observe all targets after the command, including failure. Each observation
binds path, presence, snapshot GUID, owner filesystem GUID, clone list,
userref count and deferred-destroy state; unavailable dependency evidence
refuses strict proof. Store one immutable observation row per target and
direction; hash the canonical SIP-ordered set into the existing attempt
before/after/receipt digests, including target IDs and graph digests.
Phase 2 requires every target newly present with a positive GUID, its exact
path and the pinned owner; GUID uniqueness across targets is not assumed. For
a known partial create, rollback may destroy only the subset proved created by
this attempt. Reobserve the exact path/GUID, owner and empty dependency set
immediately before **each** sequential destroy, including after earlier group
members have been removed; refuse if any member changed or was reused. Never
use name-only `destroy`, `valid_rcs: [1]`, `destroy -d` or recursive destroy.
A returned ZFS command can be observed and its proved partial-create
subset compensated in the same process; a hard-killed child may outlive it, so
skip compensation and leave the started attempt unresolved.
Phase 3 requires that subset exactly compensated and all other targets still
absent. Phase 4 requires no target changed. A live child, uncertain inventory,
changed/reused GUID or dependency that prevents exact compensation refuses
normal close, preserves locks/signatures and enters `needs_reconcile` only when
the physical outcome cannot be proved or safely settled. Do not retry a started
attempt automatically. Final chain proof rechecks the signed input, strict
attempt markers, complete target set, per-target observations, aggregate
digests and phase before confirmations. Strict 5215 defers its logical
Snapshot name/time `on_save` update until the whole chain is proved. Apply
that update after proof and before confirmations in the same SQL transaction;
on fatal refusal, leave the logical name/time unchanged. Ordinary observer
5215 retains its existing `on_save` behavior.

Use existing target, observation and attempt columns; add no catalog table or
production strict switch. Add a bounded 5215 manifest builder and explicit
planned name in API input, and a paired `guarded_5215_v1` registry state plus
multi-target receipt/proof on Node. Bump both registries to version 4; deploy
Node observer first, then API observer. Keep ordinary production 5215 on its
existing payload, generated-name/state-file behavior and opaque observer
targets throughout rolling deployment: a new Node accepts old API input only
as observer work, and a new API must not emit a v4 planned-name guard to an old
Node that would ignore it and create a different name. Stage the v4 exact
manifest only for isolated test-only strict traffic to a positively upgraded
Node; defer any production emission until all target nodes have proven live v4
capability in a later cutover, rather than relying on version text. One
internal, default-false test-only opt-in must govern both 5215 parameter
ordering/planned-name emission and exact journal manifest/guard staging; the
ordinary path retains its old wire and opaque observer intent. A planned name
alone cannot activate the guard, and an opted-in group with incomplete exact
evidence fails staging instead of silently falling back to observer targets.
API specs may stub the default-false hook within one real
`Dataset::GroupSnapshot.fire` example and assert that an unmodified call
retains the old wire; no environment, configuration, user API or scheduler
control may enable it in production.
Test-only strict rejects old wire before the handler. Keep closure limited to
one guarded 5204 plus harmless directions, or a sole 5215 member, with no
mixed guarded chain. Test the real API group
chain, target cap and shape, partial create/compensation, phases 2/3/4,
name/GUID reuse, clone/hold blockers, crash/kill/retry, tampered digest, and
final confirmation/lock behavior; retain 5204 parity tests. Fleet freeze,
verified scopes, scheduler redesign and user snapshot deletion remain outside
this gate.

Alternatives are less useful now: 5217 clone is one physical origin edge but
normally sits in Export::Create with later unsupported export/network effects
and optional mount/uidmap steps; 5209 is followed by Send/ApplyRollback and its
rollback destroys by name; 5201 `zfs create -p` may create parent filesystems
and perform mount/private-directory work inside longer create chains. Property
and dependency handles require their own pre/post dependency receipts but do
not by themselves establish a new physical snapshot chain.

Implement in reviewable gates: (1) registry parity and default-deny strict
dispatcher tests while observer mode remains active; (2) generic effect
manifest, started-attempt and postflight receipts for simple direct ZFS
create/destroy/clone/rename paths, then atomic chain-close publication; (3)
transfer/rollback `-F` empty-victim guard and identity-bound compensation;
(4) osctl route effect and asynchronous-child contracts, including temporary
run datasets and trash GC; (5) mixed-version cutover rehearsal. For gate 5,
upgrade all API/scheduler writers and nodes, set global read_only, stop old
writers, drain all queued/executing/rollbacking chains and child processes,
enable strict node refusal while frozen, then prove every node refuses a
signed or unsigned legacy mutating handle without a valid current guard
before approved backfill and unfreeze. An old API cannot safely regain
storage writes after origin links are published. A missing route contract,
routine nonempty `-F` victim set or unobservable osctl/GC effect blocks strict
cutover; it is not excused by a passing read-only reconciliation.

Gate tests inject failure and hard kill before spawn, during ZFS/osctl, after
physical success but before Command.save, and during later-chain rollback.
Assert exact receipts, no early catalog identity, normal failed-chain
confirmations for proved outcomes and needs_reconcile only for unproved ones.
Use same-name/different-GUID objects, duplicate received GUIDs, clone
promotion inversion, preexisting Pool roots, partial group snapshot, trash
moves, asynchronous osctl GC, and 5220/5223 nonempty `-F` refusal fixtures.
Full transfer/restore tests check user payload integrity. A mixed-version VM
test submits old 5212/5220 and osctl handles against a strict node and proves
refusal before effect; rollback to old API stays read_only after FK publication.

## G1: node-inclusive observation during a global storage freeze

This is the next design gate after the disposable-cluster API freeze trial. It
adds **bounded evidence about node and delayed work**, not a new freeze mode,
strict production dispatch, repair APPLY, physical identity publication, or
`repair_ready=true`. The present `StorageFreezeStatus.snapshot` is deliberately
DB-only (`api/models/storage_freeze_status.rb:44-108`); zero DB blockers cannot
prove that a NodeCtld worker, child, or osctld GC has stopped. An observation
is usable only for the exact global `read_only` epoch it names. API reads may
continue throughout the maintenance window.

At the current vpsAdmin revision, NodeCtld has distinct general, storage,
inventory, VPS, send, receive and rollback queues
(`libnodectld/lib/nodectld/queues.rb:5-18,42-47,151-158`). The daemon loop
saves completed workers before dispatching more transactions
(`daemon.rb:127-165,274-310`); `TransactionQueue` exposes workers and
reservations (`transaction_queue.rb:146-174,195-237,253-266`). The existing
local UNIX `status` route lists queue workers, reservations, one subtask PID
per command, blocked-chain subprocesses and a DB waiting count
(`remote_control.rb:9-45`, `remote_commands/status.rb:5-74`). It is not a
remote API barrier or a complete child-lifetime proof. In particular,
`Worker#kill` kills its Ruby thread and sends TERM to one PID without waiting
for the process group (`worker.rb:19-33`); `blocking_fork` registers a child
group but other libosctl system calls use `IO.popen`/`Open3` at pinned
vpsAdminOS `8e44a5124439b1f3048ffc56b1717614a5360358`
(`libosctl/lib/libosctl/utils/system.rb:18-53,73-94`). A dead worker is not
proof that its child or descendant is dead.

The same pinned vpsAdminOS has per-pool asynchronous run-dataset GC and
trash-bin threads. `garbage_collector.rb:90-125,157-207` queues a free/prune
job and may move a filesystem to trash; `trash_bin.rb:26-46,88-132` periodically
prunes and recursively destroys trash objects. Its `OsCtl::Lib::Queue` has
locked `empty?`/`length` but no active-job counter (`libosctl/.../queue.rb:3-93`).
The `garbage_collector_prune` and `trash_bin_prune` commands only enqueue work,
and `self_status` returns startup/initialized state, not GC completion
(`osctld/lib/osctld/commands/{garbage_collector/prune,trash_bin/prune,
self/status}.rb`). Therefore the pinned interface cannot assert GC quietness.
G1 needs a small read-only osctld per-pool activity/status command and
instrumentation at **job enqueue, start and finish**, including timer-driven
prunes and synchronous trash moves. This is a vpsAdminOS interface update on
every relevant node before a node-inclusive result can be called complete;
it is not a shared vpsAdminOS write fence. A mixed or old osctld reports
`unsupported/unknown` and blocks the complete result.

Use one signed, versioned, read-only NodeCtld probe per relevant node, with
`request_uuid`, nonce, node ID, bounded Pool ID set, expected freeze epoch and
deadline. A dedicated handle may use the existing persisted `storage` queue
name for old-node compatibility; an upgraded NodeCtld can route that handle
to `inventory`. Unlike inventory 5290, the result is small enough for its
normal transaction output: no Rabbit stream or raw paths. Reject unsigned,
expired, wrong-node or wrong-epoch requests **before** reporting success.
Read the freeze row at the node and return the observed mode/epoch, protocol
version, fresh response nonce, node daemon boot UUID, monotonic mutation
activity generation, all-queue worker/reservation counts, blocked child
count, child-supervision status, and per-pool osctld boot UUID/generation,
pending/running GC, trash and active storage-command counts. Exclude only this
exact probe transaction from its own worker count. Include every queue,
including rollback and inventory, and conservatively count unknown worker
handles or unclassified child effects as blockers. Cap every list and report
overflow as `unknown`, never as zero. The API validates the signed request's
nonce/epoch against this transaction output; unsupported old NodeCtld or
osctld versions, unreachable nodes, timeout and parse errors are `unknown`.

This is a *sampled barrier*, not queue ordering. A probe running in its own
queue cannot itself wait for all other queues, and a local UNIX status reply
does not order their work. NodeCtld must increment its activity generation
before dispatch of any potentially mutating handle and at worker/child
start, completion, hard kill or loss of supervision; osctld must do likewise
before/after all tracked per-pool delayed or active storage work. A daemon
restart changes boot UUID and invalidates earlier samples. A hard kill with
unreaped or untracked descendants is `unknown` until positive process exit
proof; clearing it on daemon restart alone is forbidden. Read-only probe
traffic does not advance mutation generation. Queue/reservation and DB counts
must be sampled with synchronization that can only yield conservative false
busy, never false idle. Instrument the actual child spawn/reap boundaries;
do not infer child exit from `Worker#working?` or a saved transaction alone.

For an observational maintenance report, sample `StorageFreezeStatus` first:
require `read_only`, `stable_epoch`, `db_drained`, and zero fatal/unknown
blockers. Probe every node hosting a selected managed Pool; require all
responses idle, complete and bound to the same epoch. Take the bounded full
two-pass inventory, then repeat DB and node/osctld probes. Accept only the
same freeze epoch, node/osctld boot UUIDs and mutation generations, no
pending/running workers/children/GC, and a complete inventory. Any difference
or missed deadline makes the interval `unknown` and requires a fresh capture.
The status is private and bounded, with IDs/counts rather than member paths.
Periodic GC can start after a sample; its generation must change if it runs
during the observed interval. This evidence is not a lease over future work
and does not by itself authorize APPLY. A later executable repair must also
prove no conflicting mutation can enter between its final check and DB CAS,
or keep the action restricted to facts whose dependencies remain safe.
Independent root ZFS and independent osctld operations are outside the
vpsAdmin-initiated guarantee; their effects may invalidate a scan but this
barrier cannot claim to prevent them.

The reviewed vpsAdminOS `pool_storage_activity` v1 response is a per-zpool
`gc_trash_v1` signal. It returns the osctld daemon boot UUID, pool instance
UUID, a daemon-wide generation, active/absent/stopping state, bounded pending
and running GC/trash counts, worker liveness, unknown reasons and `idle`
(`osctld/lib/osctld/storage_activity.rb`,
`osctld/lib/osctld/commands/pool/storage_activity.rb` at vpsAdminOS
`9eef7f310`). Its coverage excludes NodeCtld workers,
reservations and child lifetimes and general osctld storage commands. In
particular, an `idle` osctld response cannot itself become `node_quiet` or
`repair_ready`. A managed Pool on a storage-only node may have no imported
osctld zpool; `absent` remains unknown until a complete, reviewed
not-applicable rule is proved for that role and all vpsAdmin osctl routes.

The next bounded NodeCtld commit adds a local read-only `node_activity_v1`
observer, without a transaction, API result or `repair_ready` claim. It owns a
new daemon boot UUID and an effect generation that advances before and after
an execute or rollback with `dependency`, `catalog_identity` or
`physical_topology` impact can run, and on the corresponding reservation,
child and worker lifecycle edges. An unclassified handle is effectful for
this purpose. The queue snapshot enumerates every declared queue, including
general, inventory, send, receive and rollback, and counts workers and
reservations without paths or PIDs in the future API output. Only the exact
observer transaction may be omitted from its own worker count. The observer
reports its coverage version, daemon boot UUID, generation, monotonic sample
time, bounded per-queue counts, detached blockers, tracked children, child
coverage and bounded unknown reasons. Missing or duplicate queues, negative
or capped counts, lock timeout and an unstable generation make the snapshot
unknown, not empty. Hook before `Worker.new` starts its thread and retain the
worker as busy through `Command.save`; worker removal without a completed
save, including `clear!`, is unknown. Snapshot queue, blocker and child
registries with a generation-before/after check rather than treating the
existing local status response as an atomic barrier
(`libnodectld/lib/nodectld/{queues,transaction_queue,daemon,worker}.rb`,
`libnodectld/lib/nodectld/remote_commands/status.rb`).

Do not advance this **effect** generation for read-only inventory 5290 or
probe 5291: the planned pre/post probes must be able to bracket the two-pass
inventory without invalidating themselves. Current workers and reservations
in all queues still appear in each sample. An unobserved child possibility is
`child_coverage=unknown` even when those counts are zero. In particular,
`Worker#kill` kills a Ruby thread and sends TERM to one PID without reaping
it; `blocking_fork` waits for its leader but can leave descendants;
`Commands::Base#subtask` holds only one PID; libosctl `IO.popen`/Open3 and
direct forks need an audited spawn/reap boundary. A kill, failed wait,
uncertain descendant, uninstrumented child path or daemon restart without
predecessor-child exclusion remains unknown. The vpsAdminOS runit unit uses
`killMode = "process"` (`nixos/modules/vpsadmin/nodectld/vpsadminos.nix`), so
a new NodeCtld boot UUID alone cannot prove old children gone. This first
observer may report useful queue evidence while explicitly returning
incomplete child coverage; it must never derive `node_quiet` from a missing
worker. A later child-supervision or isolation change must close every
storage-affecting spawn path and startup orphan gap before complete G1 proof.

The subsequent vpsAdmin consumer commit adds one signed read-only 5291
activity-probe transaction and chain, its NodeCtld handler, API report
orchestration and focused tests. It combines the Node observer with osctld
`gc_trash_v1`, retaining each coverage status separately. Persist the existing
`storage` queue so an
old NodeCtld rejects an unsupported handle on a known queue; upgraded nodes
route 5291 to `inventory` as they do 5290
(`api/models/transactions/storage/inventory.rb`,
`libnodectld/lib/nodectld/queues.rb:151-158`). Both effect registries
classify its execute as read-only and rollback as no-storage; it creates no
mutation intent and advances no storage epoch. The signed request contains
protocol version, request/attempt UUID, nonce, expected global freeze epoch,
deadline, node ID and a bounded, sorted set of exact Pool ID, managed-root and
zpool claims. The API derives every relevant `(node_id, zpool)` from the
frozen catalog and retains every Pool claim even when multiple managed roots
share a zpool. The Node requires and verifies the signature, rechecks the
claims against its DB, reads `read_only` and the expected epoch before and
after the local osctld request, and returns a bounded result echoing the
request digest, nonce, epoch and exact node/zpool identity. The API binds the
result to its retained signed request digest; it does not rely on a signature
surviving normal chain close. Wrong, missing, duplicate or truncated scope
claims and output are `unknown`.

Call osctld's `pool_storage_activity` over its local UNIX socket, with a
receive deadline and byte cap enforced while reading; the current generic
`OsCtl::Client#receive` concatenates unbounded chunks and cannot by itself
meet that limit (`osctl/lib/osctl/client.rb:50-74`). A normal transaction
output suffices; no Rabbit stream or new osctl CLI is needed. Treat an old
NodeCtld, old osctld, missing pool, bad response, socket timeout or overflow
as `unknown`. The first consumer report distinguishes
`node_activity_observed` from `gc_trash_observed`, and leaves
`node_quiet`/`repair_ready` false while child coverage is incomplete.
Sample stable `read_only` and DB drain, probe every relevant node/zpool,
perform the existing complete two-pass inventory, then repeat the DB sample
and probes. Require the same epoch, selected set, daemon boot UUID, pool
instance UUID and generation across the bracket, plus active/idle v1 results
with live workers, zero pending/running counts and no unknown reasons. Any
change or incomplete inventory requires a fresh attempt. This interval is
observational and does not reserve quietness after the last sample.

Unit and contract tests cover real API-signed request to Node validation with
a fake bounded osctld socket; wrong signature/nonce/epoch/scope; old versions;
timeout, oversized and truncated replies; changed boot, pool instance or
generation across the two probes; multi-Pool same-zpool deduplication; and an
incomplete or stale two-pass inventory. An osctld v1 update may deploy first,
then the Node-local observer, then 5291 and the API report; mixed versions
return unknown. The Node-local observer tests enumerate all queues, including
rollback and reservation waits; prove the dispatch marker precedes the worker
thread; distinguish 5290 from effectful and unknown handles; exercise
save-before-remove, concurrent snapshot races, hard kill with a surviving
child, failed waits, daemon restart and capped counts. They use fake workers
and children, without host ZFS or cluster access.
Keep the existing DB-only freeze status and `repair_ready=false`. Full G1
still needs independently verified NodeCtld all-queue and child-lifetime
generation coverage, a resolution for storage-only nodes, and a final
recheck/DB-CAS boundary before any repair APPLY claim. Rollback of either
component removes evidence and never widens authority.

## Delivery, compatibility and verification gates

1. Add nullable schema, the one reconciler and private bounded collector.
   Origin and filesystem-owner FKs use RESTRICT; observer mode creates no
   filesystem identity rows and leaves origin FKs null, so old chains do not
   encounter newly linked catalog rows. Old binaries ignore new columns; old
   rows remain unverified. No production backfill or correction occurs merely
   by deploying schema.
2. Ship central admission/freeze classification, mutation manifests, node
   pre/post checks and receipts for ALL vpsAdmin topology writers now,
   including rollback and osctl routes. Observe first; fully known new
   operations can use guards immediately. Enumerate unsupported opaque
   operations and reject them in strict mode. The change must not defer
   writer coverage until legacy backfill.
3. Upgrade all API/scheduler writers and nodectld instances, retire old writer
   processes, and drain all old queued, executing and rollbacking chains before
   publishing owner-linked filesystem identities or origin FKs. Prove old
   instances cannot submit unguarded
   commands, including direct old API workers outside the new admission gate.
   A new guarded handle is insufficient while old handle 5212 or 5220 can
   still run. Node strict mode refuses missing signatures/guards on legacy
   mutating handles before link backfill. The current TransactionSigner.can_sign?
   can report true with no key and Command verifies only a present signature;
   fix that gate
   for new handles before asserting protection.
4. In a separately approved production window, use this same reconciler
   in bootstrap mode for bounded backfill/approved DB-only corrections.
   Preparatory scans may run with writes; overlapping runs are stale, and
   affected scopes remain unverified throughout mixed-version observer mode.
   Switch the global gate to read_only, drain, enable strict legacy-handle
   rejection, complete final scan/apply/verification (including approved origin
   links), then unfreeze. If unresolved scopes remain, keep their destructive
   operations blocked; do not assert
   global verification. Later audits and approved repairs use steady mode.
5. Software rollback during observer mode, before any owner-linked filesystem
   identity or origin link is published, can ignore additive data but
   invalidates affected validation. Once those rows or links have been
   published, an old API may serve reads only. Storage-mutating
   ingress and old worker processes must stay disabled, the node must keep
   refusing legacy mutation handles, and the global storage gate stays
   read_only until a compatible writer is restored. Merely selecting observer
   mode cannot make an old writer safe: RESTRICT may fail its confirmation
   after an effect, while SET NULL would discard dependency evidence. A return
   to old write behavior requires a separately designed and proved downgrade;
   it is not part of this rollout.
   Retain new columns/journals and legacy SIP/SIPB/reference_count values;
   do not drop state created by upgraded writers. No user-visible API or
   client deletion contract changes in this phase.

Acceptance tests need two SIPBs for one backup SIP, duplicate GUIDs, clone
promotion and origin inversion, DatasetTree and nested Pool roots, known
and unknown structural filesystems, all listed production finding classes,
normal success/failure/compensated rollback versus needs_reconcile, fatal
rollback recovery, Rabbit replay/gaps/overflow/40k-row bounded memory,
freeze/admission races, old-handle refusal, osctl completion, and receive
and local-send -F victim-set gates. Exercise full transfer/restore with a
payload checksum. Rehearse bootstrap, partial batch restart, approval
invalidation, mixed API/node versions and software rollback on a
representative copy. Test an old destroy chain during observer mode with no
new owner/origin FK publication; after publication, verify legacy node handles
are refused before effect and old catalog deletion cannot silently clear a
linked origin. A strict cutover is blocked if any required writer
route is unclassified or a routine transfer still needs an unsupported
destructive -F path.

## Source audit gates and open assumptions

The earlier vpsAdmin source audit used base 486350466. Storage documentation
is under docs/storage/README.md and docs/storage/branching.md; the older
doc/storage/*.mdwn paths were removed. A scoped diff from the still earlier
9fc0648 audit found no changes to the core Dataset/Branch/SIP chains or
storage commands at that base. Subsequent observer writer work has changed
transaction admission, Command.save and snapshot receipts; use the current
worktree head for implementation, not that historical diff.

Relevant vpsAdmin source paths include api/db/schema.rb;
api/models/{transaction_chain,transaction,transaction_confirmation}.rb;
api/models/transaction_chains/{dataset/send,dataset/rollback,dataset/transfer,
snapshot_in_pool/destroy,snapshot_in_pool/use_clone,
snapshot_in_pool/purge_clones,dataset_in_pool/detach_backup_heads}.rb;
libnodectld/lib/nodectld/{command,confirmations,storage_status,
node_bunny,zfs_stream,dataset}.rb; and command classes under
libnodectld/lib/nodectld/commands/{dataset,dataset_tree,branch,pool,vps}.
The inherited local-send receiver is in vpsAdminOS
libosctl/lib/libosctl/zfs/stream.rb.

The implementation audit must include indirect effects: Dataset::Destroy
handle 5203 uses osctl trash-bin, so a successful call may move a filesystem
outside its catalog path rather than destroy it. ApplyRollback 5211 moves
children and trashes/replaces a filesystem; LocalRollback 5208 uses
zfs rollback -r. Pool::Create 5250 can reuse an existing root via ensure_ds,
yet its rollback destroys root/work paths without a created-by-this-command
record; identity-bound rollback must distinguish pre-existing objects.
GroupSnapshot 5215 recovers from a local state file after checking only the
first snapshot, so recovery must check every intended member. CloneSnapshot
5217 can leave a physical export clone after logical use becomes inactive.
RecvCheck 5222 checks a snapshot name, not its GUID. Dataset::Transfer chooses
an incremental common base by logical Snapshot ID, not by both physical GUIDs.
VPS create/destroy/reinstall/copy/send/replace and their cancel/cleanup/
rollback osctl routes need command-specific effect bounds and completion
checks. Audit other helpers for generated ZFS commands before declaring route
coverage.
The existing transaction signature is optional and its save/confirmation
path is shared across handles; a guard must explicitly handle old queued
commands rather than relying on a new command name.

Open validation questions: whether SIPB cardinality holds everywhere,
whether every invoked osctl command settles all ZFS effects before it
returns, whether all managed-root ancestors and clones are covered by
pool-wide inventory, and whether a routine incremental transfer needs
nonempty -F victim deletion. Each unresolved answer is a cutover gate,
not permission to infer safety.
