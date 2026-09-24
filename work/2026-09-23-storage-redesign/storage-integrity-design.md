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
| storage_freeze_controls | Singleton row: mode read_write/read_only, monotonic epoch, requested_by_user_id, reason and requested_at | This is an admission gate, not a separate node-ack system. |
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
replays. A conflicting duplicate, gap, oversize chunk, missing final marker,
count/hash mismatch or queue overflow makes the attempt incomplete. Use a
durable quota/TTL longer than the scan plus recovery window; never silently
drop messages. CLI restart can replay a broker delivery against its durable
checkpoint; a producer crash without a proved final result ends that attempt
and requires a fresh scan. Generic API Supervisor instances do not own the
private spool.

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

The API-model CLI ultimately exposes one engine with `capture`, `plan`, `decide`,
`apply`, `resume` and `verify` operations. `mode=bootstrap` accepts absent
legacy physical fields as candidates for evidenced backfill;
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
chunks, and set its expiry beyond scan plus recovery time. A node-side
publish failure fails the read-only transaction; a node-side success never
substitutes for the CLI's verified final manifest.

There is no reverse node-facing application ACK. One ordered node publisher
retries an ambiguously confirmed publish with the identical
`(run, attempt, sequence, payload, digest)`; it never changes a sequence's
bytes. The CLI validates a delivery, appends and fsyncs it, then persists
and fsyncs the contiguous sequence/digest checkpoint before broker manual
ACK. On crash before checkpoint, recovery discards any uncheckpointed tail
and accepts broker redelivery; on crash after checkpoint but before ACK, it
checks exact replay and ACKs. A conflicting replay fails the attempt. The
final marker is ACKed only after its local digest/manifest is sealed. Mark
the DB run complete only after both that sealed marker and the matching
successful compact result from the signed read-only transaction are known;
either alone is insufficient. An ambiguous publisher-confirm retry is
harmless, but producer crash, missing final result, queue expiry or an
unrecoverable CLI checkpoint ends the attempt incomplete; a new attempt
rescans and never splices chunks.

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
CLI crash before/after checkpoint but before broker ACK, final digest failure,
two-pass volatility, queue overflow and mismatched signed scope produce the
specified outcomes. Matcher fixtures cover duplicate GUIDs in received
copies, same-name occurrences in two branches, clone promotion and reciprocal
origin, all seven finding classes
including valid detached heads and an external parent, and disk-only objects
whose exact paths appear only in private output. Epoch overlap is stale;
findings alone are complete/advisory. Assert no catalog mutation, no
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

The current vpsAdmin worktree base is 486350466. Storage documentation is
under docs/storage/README.md and docs/storage/branching.md; the older
doc/storage/*.mdwn paths were removed. A scoped diff from the earlier
9fc0648 source audit found no changes to the core Dataset/Branch/SIP
transaction chains, storage transaction definitions or libnodectld
production commands. The intervening VPS-chain edits inspected here concern
IP/resource accounting and network cleanup, not the storage topology
algorithm. Recheck the worktree head if it changes during implementation.

Relevant vpsAdmin source paths at base 486350466 include api/db/schema.rb;
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
