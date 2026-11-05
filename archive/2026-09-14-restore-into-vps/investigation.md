# Restoring snapshots into new and existing VPSes

Investigation of upstream code fetched on 2026-09-14. This is a proposal, not
an implemented or runtime-tested feature. Exact revisions are in `state.md`.

## Recommended design

Introduce a **VPS snapshot set**: a restore point containing an immutable list
of dataset snapshots and the VPS configuration at capture time. Keep individual
dataset snapshots underneath and preserve existing dataset APIs. Use sets for
manual whole-VPS snapshots and eligible daily backups.

Make restore into a new VPS the primary flow, with destination-owned baseline
snapshots and fresh networking. For an existing VPS, offer explicit root-only
replacement and, subsequently, replacement of its complete dataset hierarchy.
Do not infer a tree merge from matching names. Existing backup DatasetTree
objects can preserve individual histories, but cannot represent a historical
VPS hierarchy on their own.

## Findings in the current implementation

1. **Restore rolls back the original logical dataset.** The dataset snapshot
   action locates the snapshot's primary dataset and owning VPS; it has no
   destination parameter. `Vps::Restore` stops the VPS, invokes dataset rollback,
   and starts it. Remote root restore receives into a temporary dataset and
   explicitly moves current children across. The descendant regression test
   asserts that present-day children survive root restoration.
   [Snapshot API](https://github.com/vpsfreecz/vpsadmin/blob/f7a17d6e512f0b11e2c908813eb2e780261e20ae/api/lib/vpsadmin/api/resources/dataset.rb),
   [restore chain](https://github.com/vpsfreecz/vpsadmin/blob/f7a17d6e512f0b11e2c908813eb2e780261e20ae/api/models/transaction_chains/vps/restore.rb),
   [node replacement](https://github.com/vpsfreecz/vpsadmin/blob/f7a17d6e512f0b11e2c908813eb2e780261e20ae/libnodectld/lib/nodectld/commands/dataset/apply_rollback.rb).

2. **Cloning supplies provisioning pieces, not historical recovery.** It
   creates destination datasets and resources, copies current settings/mounts,
   and allocates addresses. Restore can share these helpers and the creation
   wizard's location/resource validation, but must avoid copying current source
   configuration, installing a fresh template, replaying provisioning scripts,
   or stopping the source VPS.
   [Clone chain](https://github.com/vpsfreecz/vpsadmin/blob/f7a17d6e512f0b11e2c908813eb2e780261e20ae/api/models/transaction_chains/vps/clone/os_to_os.rb),
   [create chain](https://github.com/vpsfreecz/vpsadmin/blob/f7a17d6e512f0b11e2c908813eb2e780261e20ae/api/models/transaction_chains/vps/create.rb),
   [wizard](https://github.com/vpsfreecz/vpsadmin/blob/f7a17d6e512f0b11e2c908813eb2e780261e20ae/webui/forms/vps.forms.php).

3. **`from_snapshot` is not exact-point recovery.** The osctld local-transfer
   rootfs phase sends that snapshot and then a newer base snapshot. It still
   uses the current layout/configuration. Also, the clone `keep_snapshots` test
   contains a pending retention assertion because cleanup removes transfer
   snapshots. Neither option meets the requested baseline guarantee.
   [Transfer implementation](https://github.com/vpsfreecz/vpsadminos/blob/0beff55b8529b7c33992eeebab82cd9df0f5b53a/osctld/lib/osctld/commands/container/local_transfer/rootfs.rb),
   [pending assertion](https://github.com/vpsfreecz/vpsadmin/blob/f7a17d6e512f0b11e2c908813eb2e780261e20ae/tests/suite/vps/clone-remote-consistent-keep-snapshots.nix).

4. **The atomic storage primitive exists.** Group snapshot transaction 5215
   passes a dataset list to one `zfs snapshot` invocation. However, the API chain
   normally skips locked datasets; strict locking is optional. `GroupSnapshot`
   records represent scheduling membership, not a completed capture. There is
   no durable resulting set identity or VPS configuration. Node crash recovery
   checks only the first member, and saves state after creating snapshots; a
   stronger all-members/idempotency contract is necessary.
   [Group chain](https://github.com/vpsfreecz/vpsadmin/blob/f7a17d6e512f0b11e2c908813eb2e780261e20ae/api/models/transaction_chains/dataset/group_snapshot.rb),
   [node command](https://github.com/vpsfreecz/vpsadmin/blob/f7a17d6e512f0b11e2c908813eb2e780261e20ae/libnodectld/lib/nodectld/commands/dataset/group_snapshot.rb).

5. **Historical VPS configuration is absent.** Snapshot stores dataset,
   history identifier, name, label and timestamps. VPS references OsTemplate;
   that template has distribution/version/arch/vendor/variant and mutable
   configuration. These API models do not record an immutable installed image
   build. A current template/VPS row cannot reliably describe an old snapshot.
   [Schema](https://github.com/vpsfreecz/vpsadmin/blob/f7a17d6e512f0b11e2c908813eb2e780261e20ae/api/db/schema.rb),
   [template model](https://github.com/vpsfreecz/vpsadmin/blob/f7a17d6e512f0b11e2c908813eb2e780261e20ae/api/models/os_template.rb).

6. **History and snapshot identity are per dataset.** DatasetTree belongs to
   DatasetInPool and contains backup branches. It is not a subtree of VPS
   datasets. Dataset::Send mirrors the same Snapshot ID to another pool, which
   assumes the same logical Dataset. Cross-VPS import needs new destination
   Snapshot records and an explicit transfer mapping.
   [Tree](https://github.com/vpsfreecz/vpsadmin/blob/f7a17d6e512f0b11e2c908813eb2e780261e20ae/api/models/dataset_tree.rb),
   [send confirmations](https://github.com/vpsfreecz/vpsadmin/blob/f7a17d6e512f0b11e2c908813eb2e780261e20ae/api/models/transaction_chains/dataset/send.rb),
   [backup history transfer](https://github.com/vpsfreecz/vpsadmin/blob/f7a17d6e512f0b11e2c908813eb2e780261e20ae/api/models/transaction_chains/dataset/transfer.rb).

7. **Retention needs explicit support.** Production hooks set local VPS
   min/max snapshots to one. Rotation uses count and original creation time,
   so an imported old snapshot can soon be eligible for deletion. Transfer
   preservation alone is insufficient.
   [Site hooks](https://github.com/vpsfreecz/vpsfree-cz-configuration/blob/b0bb82d13159ce0da15375acf0483ab58572824a/configs/vpsadmin/api/hooks.rb),
   [rotation](https://github.com/vpsfreecz/vpsadmin/blob/f7a17d6e512f0b11e2c908813eb2e780261e20ae/api/models/transaction_chains/dataset/rotate.rb).

## Snapshot sets and atomic capture

Suggested model names are provisional:

- `VpsSnapshotSet`: durable identity, source VPS identity, capture operation,
  label, manual/daily/imported kind, capture time, metadata schema version,
  consistency mode and confirmation state.
- `VpsSnapshotSetMember`: snapshot reference, capture-time dataset identity,
  parent/relative path, required/optional status, safe properties and mount
  relationships.
- An immutable, versioned configuration manifest attached to the set. Keep it
  independent of mutable/deleted VPS/template rows. Use an allowlisted format,
  not a serialized ActiveRecord object or arbitrary host configuration.

Membership is immutable; availability is separate and can change as replicas
expire or move. Offer whole-set restore only when every selected required
member has a confirmed available copy. Members may be read from different
backup servers without changing the original capture consistency.

For user-triggered whole-VPS snapshots, lock the VPS, topology and all selected
primary DatasetInPool records, check per-dataset limits, and capture on one node
in one pool. Fail/retry the whole request when a member is locked or missing.
Use one explicit ZFS snapshot list; blind recursion could include internal
history or unrelated data. OpenZFS documents atomic snapshots and simultaneous
recursive creation.
[OpenZFS snapshot manual](https://openzfs.github.io/openzfs-docs/man/master/8/zfs-snapshot.8.html).

Capture metadata under compatible locks and hold them through execution and
confirmation. Concurrent template, feature, mount, mapping or topology edits
must not invalidate the manifest. Use an operation-derived identity, persist
intent before invoking ZFS, and verify every member on retries. Reconcile the
ZFS-success/database-confirmation crash window without creating duplicate sets.

Daily backups can still batch datasets from multiple VPSes, but record actual
membership and configuration per VPS. Skip a locked VPS as a unit or mark its
capture incomplete; never advertise a partial batch as a complete VPS point.
Storage capture and remote backup replication are separate phases.

Include only VPS-owned root/descendants initially. NAS/NFS mounts, foreign local
datasets and mounted snapshots are external dependencies. Show them in the
preview; do not claim they were captured atomically or reattach them implicitly.
Snapshots spanning nodes/pools need a separate consistency contract.

A running-VPS snapshot is crash-consistent, not a guarantee of application-level
transaction consistency. Stop/snapshot/restart can be an optional later mode,
preserving the prior running state. Application-specific quiescing is another
extension. Restoring an existing snapshot requires no source shutdown.

## Which configuration to preserve

| Setting | Recommended behavior |
| --- | --- |
| OS identity | Preserve template ID as provenance plus immutable distribution, release, architecture, vendor, variant, and relevant runtime/template configuration. |
| Exact image build | Capture build identifier/digest at installation if available; otherwise mark unknown. Restore filesystem contents from the snapshot without downloading the original image. |
| Features and host requirements | Preserve explicit feature states, cgroup requirement, map mode and UID/GID mapping provenance; reject unsupported destinations before transfer/cutover. |
| Dataset layout/mounts | Store capture-time paths and relationships; reconstruct selected destination-owned mounts, required datasets and safe ZFS properties. Derive host paths afresh. |
| CPU/RAM/swap/disk | Capture for defaults/provenance. New-VPS wizard selects allocations; existing target keeps its allocations unless explicitly changed. Check per-dataset and aggregate capacity. |
| Hostname/resolver | New VPS gets a chosen hostname and suitable resolver; existing target keeps its own by default. Respect manage-hostname behavior. |
| Boot/maintenance settings | Capture preferences and validate current policy. Make start-after-restore explicit, preferably off initially for recovery review. |
| Interfaces/IPs | Fresh allocations for a new VPS; retain existing target networking for overwrite. Never inherit source managed IPs, routes or MACs. |
| Account/site policy | Recompute ownership, entitlement, lifetime, backup placement and plans. Do not restore suspension, maintenance flags or historical resource grants. |
| Provisioning scripts/keys | Do not automatically replay user-data, cloud-init, public-key deployment or template installation. Existing guest files remain snapshot data. |

The host kernel is not a restorable VPS setting; validate host capabilities.
Do not silently replace an unavailable historical template with today's enabled
template. Historical restore eligibility is a separate check from permission to
install a fresh image.

`Transactions::Vps::Create(empty: true)` and osctl's empty-container path provide
a likely implementation route. The empty osctl CLI path does not forward
vendor/variant, so apply the full tuple separately and verify mapping behavior.
Container registration, receive and configuration ordering still need a
prototype. This investigation does not prove that no vpsAdminOS changes will
be needed.
[Empty-create transaction](https://github.com/vpsfreecz/vpsadmin/blob/f7a17d6e512f0b11e2c908813eb2e780261e20ae/api/models/transactions/vps/create.rb),
[osctl creation paths](https://github.com/vpsfreecz/vpsadminos/blob/0beff55b8529b7c33992eeebab82cd9df0f5b53a/osctl/lib/osctl/cli/container.rb).

Managed networking can be regenerated; arbitrary guest configuration cannot.
Old static addresses, application endpoints, machine identity and SSH host keys
can remain in copied files. Explain this in preview. Any optional identity reset
must affect the destination after preserving the imported baseline.

## New-VPS restore flow

Start the wizard from a snapshot/set, showing capture time, metadata availability
and selected datasets. Default to all members of a complete set. Root-only is
valid when omitted datasets are not required for the OS layout. Missing an
essential NixOS dataset, for example, should reject ordinary bootable restore
or require explicit stopped recovery mode; do not silently create empty data.

Reuse environment/location, resources and hostname steps. Replace template
selection with historical OS information, with manual compatible metadata for
legacy snapshots. Preview selected datasets, cost, networking, excluded mounts,
retention and whether to start.

Backend sequence:

1. Revalidate ownership, destination entitlement, configuration and availability.
   Hold required source copies against concurrent deletion/rotation. These are
   temporary references, not changes to source guest data or snapshot contents.
2. Reserve destination resources and stage unmounted datasets. Resolve each
   SnapshotInPool and backup branch; an available backup and manifest should be
   sufficient even if the original VPS/node is unavailable.
3. Send exactly the selected snapshot of every dataset, with no subsequent live
   sync. Prefer full send/receive even on the same pool to keep lifetimes
   independent. ZFS clone optimization can wait for deliberate dependency and
   accounting support.
4. Create destination Snapshot/SnapshotInPool records. Preserve original capture
   time and separate import time/provenance. Do not reuse source API IDs or move
   source snapshot ownership. Provenance must survive source cleanup without
   exposing another owner's objects after a later ownership change.
5. Retain the destination baseline, apply validated runtime/mount/network
   configuration, register normal destination backup plans, and finalize the
   operation. Start only if requested.

Single-snapshot sends avoid copying all source history or unwanted properties
through a replication stream. Reuse transport, queues and receive checks with
explicit source/destination snapshot identity mapping.
[OpenZFS send manual](https://openzfs.github.io/openzfs-docs/man/master/8/zfs-send.8.html).

Keep at least one complete destination-owned baseline copy protected from
ordinary rotation, normally on the backup pool. A local copy can rotate only
after that protected backup exists. Without backups, retain the local copy.
Do not falsify capture time to prevent expiry; model protection separately.

I recommend explicit baseline protection, removable by the owner with dependency
checks and a visible storage/snapshot budget. A bounded deadline measured from
import is an alternative, but must be visible and chosen deliberately. Indefinite
retention needs capacity policy and a removal API because users currently cannot
delete backed-up VPS snapshots. Protection applies to a complete set, not just
its root member.

## Existing-VPS restore and subdataset conflicts

Keep target VPS ID, owner, location, networking and allocations. Apply historical
OS/runtime settings deliberately. Do not call the existing broken-VPS Replace
flow unchanged: it alters source lifecycle and can move backup ownership.

| Mode | Root | Children | Histories |
| --- | --- | --- | --- |
| Root-only overwrite | Import selected root snapshot | Preserve current target children and their data | Keep prior histories; imported root starts a separate target history |
| Whole-hierarchy overwrite | Import selected root | Exactly the selected historical hierarchy | Retain previous root/children/topology as a recoverable generation |
| Advanced mapping/merge | Explicit per-dataset mapping | User-defined conflict rules | Defer until simpler semantics are proven |

Root-only preserves target child mounts where compatible; do not import source
mounts referencing absent children. Validate mount collisions, required OS
datasets and UID/GID mappings. A changed mapping cannot leave preserved target
children with incompatible ownership: implement an explicit supported remap or
reject the combination. The result is deliberately mixed-time data, not a
whole-VPS rollback.

For full replacement:

```text
Source snapshot: /, /db, /uploads
Existing target: /, /db, /cache
Restored target: /, /db, /uploads
Recovery state:  previous /, /db, /cache and its mount/configuration manifest
```

Replace `/db`, create `/uploads`, and retain `/cache` in the previous generation
without mounting it in the restored VPS. No silent deletion or name-based
combination. External mounts require separate review.

Receive and verify source members before stopping the target. Then stop it,
capture/protect its latest pre-overwrite state, and switch datasets, mounts and
configuration through a durable recoverable operation. Old backup trees alone
do not preserve writes since the last snapshot. After a partial cutover failure,
keep the VPS stopped until a complete old/new generation is recovered.

DatasetTree can preserve independent per-dataset histories. Full topology undo
also needs a generation/member mapping retaining removed datasets, historical
paths, mounts and quota accounting, excluded from active-descendant enumeration
and ordinary scheduling. Sequential ZFS renames and database edits are not one
atomic transaction: persist operation phases and transaction-owned paths.
Physical staging/retirement layout and osctld cutover are prototype questions.
Keep logical destination Dataset IDs stable where possible; explicitly handle
new and retired members.

Retain the previous generation for a defined recovery window. Keeping all prior
hierarchies forever is a separate capacity policy. I recommend root-only
overwrite first, with full hierarchy replacement as a separate implementation
slice. An intermediate restriction to exactly matching source/target topology
avoids path conflicts but still requires full failure-recovery handling.

## Historical snapshots without metadata

Keep existing snapshots usable through a clearly marked legacy flow with
compatible OS information and feature review. Current source settings can be
suggested, but cannot be called capture-time settings.

Equal names/timestamps do not prove one atomic operation. Today's dataset list
does not establish historical completeness after deletions or renames. Do not
backfill guaranteed sets from names. Strong surviving transaction evidence might
permit verified reconstruction, but that is a separate migration. Otherwise
keep individual-dataset recovery, or an advanced explicitly mixed/unknown-time
selection. Never substitute the latest child snapshot for a missing member.

## API, compatibility and rollout

Add snapshot-set and restore preview/execution resources/actions; names such as
`VpsSnapshotSet`, `RestoreNew` and `RestoreInto` are provisional. Preserve
existing dataset rollback semantics and transaction-chain status reporting.
Execution must revalidate the preview under locks; preview is not a reservation.

Check ownership of every member, target ownership, account state, environment
permissions, snapshot availability, quotas and node capabilities. Initially
limit this to same-owner restores. Validate paths, mount targets and allowed
properties; reject unsupported metadata rather than partially applying it.
Audit source set, destination and selection without logging secrets.

Use additive tables and preserve existing ZFS layout for the first phase.
Existing API clients keep working; assess generated-client additions separately.
No Terraform resource replacement semantics need to change as a side effect.

Old writers are a material rollback risk: they ignore protection and may not
understand retired hierarchy members. Upgrade all relevant central rotation,
deletion and scheduling workers before enabling the new states. Version/gate
new node transactions until every involved source, destination and backup
worker supports them; keep old commands accepted for mixed-version operation.

No coordinated fleet-wide OS/kernel upgrade is inherently required. Node
vpsAdmin/nodectld packages still need updating. If full hierarchy switching needs
a new vpsAdminOS capability, enable it only on upgraded eligible destinations.
No ZFS on-disk format change is proposed.

Rollback below protection/topology-aware service code is unsafe once new state
exists. Disable new actions, drain operations, retain additive schema and use
a compatible rollback build. Reverting to older code requires an explicit
tested conversion/retention procedure. Unreleased migrations should assume
their immediately preceding schema, not add guards for stale disposable DBs.

## KB and configuration scope

The public backups article currently describes dataset-level restore and says
root restoration leaves children untouched. Preserve that distinction for old
actions while documenting whole-VPS restore separately.
[Current backups article](https://kb.vpsfree.org/manuals/vps/backups).

Primary pages to update/review:

| Czech page | English page | Expected impact |
| --- | --- | --- |
| `navody:vps:zalohy` | `manuals:vps:backups` | Sets, atomic capture, destinations, overwrite modes, retention |
| `navody:vps:datasety` | `manuals:vps:datasets` | Membership, exclusions, quotas and hierarchy replacement |
| `navody:vps:sprava` | `manuals:vps:management` | Wizard and restored settings versus target identity |
| `navody:vps:playgroundvps` | `manuals:vps:playgroundvps` | Testing recovery in a separate VPS versus live cloning |
| `navody:vps:obnova_webu_zo_zalohy` | Check language mapping during source fetch | Link file recovery to complete-VPS recovery where useful |

Review storage, exports, repair, NixOS impermanence and KVM articles for affected
claims and required datasets. They do not all need rewriting merely because
they mention snapshots. Initial scope comes from source contract bindings and
public article inspection; fetch all current production sources for final impact.

Follow `vpsfree-kb-contracts/docs/webui-change-workflow.md`: semantic WebUI IDs,
exact pushed feature revision, contract drift review, CS/EN captures, all-page
`kb-contract-fetch`, `kb-contract-build`, and current schema-5 manifests from
`kb-contract-manifest --changes`. The inspected guide still mentions schema 4
in one paragraph; current workspace rules require schema 5. Apply the
user-facing writing skill when authoring candidates, then stage and verify
pages and localized revision summaries. Request production promotion approval
only once that exact bundle is reviewable. No wiki writes occurred here.

Configuration separates these channels:

| Channel | Input | Consumers |
| --- | --- | --- |
| `staging` | `vpsadminStaging` | Staging nodes |
| `production` | `vpsadminProduction` | Production nodes |
| `vpsadmin` | `vpsadminServices` | Central services |

Use `confctl inputs channel set --commit <channel> vpsadmin <rev>` for feature
pins; normal integrated updates use `update --commit`. Keep generated commit
messages intact. Check destination backup hooks, plan registration, protection
and initial full transfer into new histories. Never move the original VPS's
backups or infer incremental ancestry from names.

Suggested rollout: additive schema/compatible central services with flows
disabled; staging node and backup workers; application/KB review; compatible
production workers and all central retention consumers; enable eligible
destinations; publish approved KB content. Build/deploy configurations from the
feature worktree; configuration integration is a separate decision. No pins or
deployments changed in this investigation.

## Implementation slices and validation

1. Snapshot-set identity/configuration, manual atomic capture, daily integration,
   retention and authorization.
2. Exact restore into a new VPS with root/complete-set selection and wizard.
3. Root-only existing-target overwrite with protected pre-overwrite state.
4. Whole-hierarchy replacement with persisted topology and crash recovery.
5. Bilingual KB/captures and configuration rollout alongside each released slice.

Commit intended changes, run quick checks and mandatory xhigh review before long
VM tests. Acceptance coverage should include:

- Known contents in root and every child at capture; later source writes must
  not appear in restored data. Source running state/networking/data stay intact.
- Local, cross-pool and remote-backup restore; source node unavailable;
  interrupted send/receive with safe retry and no duplicate VPS/snapshots.
- Destination-owned baseline rollback after source deletion/rotation, later
  destination writes and normal rotation, including an old capture timestamp.
- Busy/missing datasets and capture-time topology changes; no partial set
  reported complete; crash before/after ZFS creation/database confirmation.
- Post-capture feature/template changes, disabled historical templates, missing
  metadata, unknown schema, incompatible cgroups/architecture/mappings.
- Nested/missing required datasets, mount conflicts, NAS/foreign mounts,
  NixOS layouts, target-only datasets retained for undo.
- Failure at each target switch phase; recover a complete known hierarchy and
  configuration without booting a partial state.
- Per-dataset quotas, aggregate entitlement, IP exhaustion and physical storage
  for staged plus old generations; concurrent restore/delete/migrate requests.
- Repeated restore, rollback and backup rotation: branch origins, reference
  counts, histories and incremental transfers remain valid.
- Mixed versions and supported service rollback; wizard previews/errors and
  bilingual navigation/captures. Update CI selectors and API-spec topic coverage.

These are planned tests. This pass read existing tests and source but did not
execute integration tests or establish runtime proof of the proposed flow.
