# Disable VPS backups: investigation and proposal

## Goal and scope

Investigate how vpsAdmin can stop VPS backups, remove backup-related snapshots
from hypervisor/primary pools, detach backup tree/branch heads, and preserve
existing backup-pool snapshots. Reenabling must start a new tree with a full
transfer. Recommend the API contract and placement in the existing web UIs.
This request authorizes investigation and a proposal, without implementation.

## Affected repositories

- vpsadmin: API, scheduler, storage transactions, node operations and legacy UI.
- New WebUI repository, if confirmed by the architect, for UI placement only.
- Generated clients and KB contracts: assess future implementation dependencies.

## Approach and decisions

Architect owns bounded source investigation and `design.md`; lead owns scope,
tracking, acceptance and user-facing explanation. Use canonical bare sources
without creating worktrees. Cite exact revisions and relevant source paths.
Separate scheduler cessation from primary-snapshot cleanup and lineage closure.
Confirm locking, partial failure/retry, recursive dataset scope and preservation
of unrelated snapshots before recommending an operation.

## Compatibility and deployment

Assess API/client compatibility, persisted lineage and snapshot state, mixed API
and node versions, migration needs, ordering and recovery. No deployment planned.

## Documentation and readers

The proposal lives in `design.md` for the requester and future implementers.
Current execution and evidence live in `state.md`. No product docs change is
needed for investigation of a feature that does not exist yet.

## Verification

Source-backed analysis and evidence acceptance only. No runtime checks, source
commits, integration or deployment. Routine findings/design records do not trigger
automatic independent final change review.
