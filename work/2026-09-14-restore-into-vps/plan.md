# Restore a snapshot into a VPS

## Goal and current scope

Investigate restoring a VPS snapshot into a new VPS with selectable location
and resources, leaving the source untouched. Propose existing-VPS overwrite,
retention of imported snapshots and old histories, subdataset behavior, atomic
VPS snapshots, configuration capture, KB updates and configuration rollout.
This request is investigation and recommendations, not implementation.

## Affected repositories

- `vpsadmin`: API, snapshot scheduling/models, transaction chains, nodectld,
  WebUI, translations and tests.
- `vpsfree-kb-contracts`: navigation, captures, bilingual pages and runtime tests.
- `vpsfree-cz-configuration`: service/staging/production pins, backup hooks and
  retention policy.
- `vpsadminos`: runtime reference; optional support for recoverable hierarchy
  switching if existing commands are insufficient. No kernel changes intended.
- Generated Go client / Terraform: assess additive client regeneration during
  implementation; no provider changes are required for this investigation.

## Approach

Inspect fetched upstream revisions using temporary immutable source exports.
Trace creation/cloning, snapshots, rollback, transfers, configuration and
retention. Propose persistent snapshot-set membership and historical metadata,
then exact-snapshot import with destination-owned records. Separate root-only
replacement from full hierarchy replacement. Record evidence and alternatives
in `investigation.md`.

## Compatibility and deployment

Prefer additive metadata tables/actions; preserve existing dataset APIs and ZFS
layout for the first phase. Historical snapshots remain available through a
legacy recovery path; do not invent capture-time configuration or infer atomic
sets from names. Imports start independent destination histories.

Capture topology/configuration under operation locks through snapshot execution.
Atomicity covers selected datasets in one pool, not applications or remote
replication. Gate new commands by node eligibility. Roll nodes incrementally;
no coordinated fleet-wide OS/kernel update is proposed.

All central rotation/deletion workers must understand retained snapshot sets
before enabling them. Additive schema alone does not make old writers safe.
Rollback below protection/topology support needs an explicit conversion plan;
otherwise keep the additive schema and use a compatible rollback build.

Pin through `confctl inputs channel set --commit <channel> vpsadmin <rev>` for
feature revisions, or `update --commit` after integration. Relevant channels:
`staging`, `production`, `vpsadmin` (central services). Keep deployment and
configuration integration separate. Stage exact bilingual KB candidates before
requesting production publication approval.

## Testing plan for implementation

Quick API/model/transaction/nodectld checks, then committed-change review at
xhigh, then focused VM and browser tests. Verify known content in every selected
dataset, unchanged source, rollback after source deletion/rotation, configuration
fidelity, membership drift, quotas, differing topology, failure recovery,
retention, incremental history and mixed versions. Include local and remote
backup sources with the original node unavailable. Follow with KB contracts,
bilingual captures and configuration builds. No runtime tests needed for this
coordination-only investigation.

## Recommended implementation order

1. Snapshot sets, configuration capture, manual atomic snapshots and retention.
2. New-VPS restore with root-only/complete-set selection and wizard resources.
3. Root-only existing-VPS overwrite with protected pre-overwrite state.
4. Full hierarchy overwrite with recoverable topology generations; defer merges.
5. Prepare KB and configuration changes alongside each released slice.

## Policy decisions

Discuss baseline retention lifetime/storage budget, pre-overwrite recovery
window, and whether stop/snapshot/restart belongs in the first release.
Recommend retaining an existing target's identity, networking, location and
resources while restoring source OS/runtime metadata. New VPS gets fresh
networking and wizard-selected resources. No implementation decision is yet
accepted by the user.
