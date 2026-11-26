# 2026-11-26-snapshot-removal-plan

## Goal

I'd like to implement vpsadmin feature to remove dataset snapshots (backups). like we have the new function to disable backups (it removes snapshots from primary/hypervisor) pools, I'd like a similar option to delete the snapshots from the backup pools. php/react UIs should handle that similarly as the disable backups feature. make it admin-only. I suppose that it should just delete all dataset snapshots (from primary/hypervisor/backup pools). optionally also disable dataset plans? not sure. look it over and suggest a solution + create an implementation plan.

## Affected repositories

- `vpsadmin`: API, snapshot transaction machinery, PHP UI and React UI.
- Generated Go, Rust and TypeScript clients and KB contracts: assess impact in
  the plan; no source changes authorized for this planning pass.

## Approach

Investigate the current disable-backups and snapshot deletion flows, propose
the smallest compatible admin-only operation, and produce an executable
implementation plan. This request ends at investigation and planning.
Application changes, snapshot deletion, deployment and integration are outside
this pass.

The retained Full team (5 implementers) roster assigns design to `architect0`.
Backend research belongs to `implementer0`; PHP/React research belongs to
`implementer1`. Other implementers and the reviewer have no assignment for this
planning-only scope. The lead owns scope, acceptance and session tracking.

The architect records the source-backed design, proposed API/UX, invariants,
package boundaries, acceptance criteria, compatibility and verification in
[design.md](design.md). Findings are linked from state.

## Decisions

- Required: admin-only access, PHP/React parity with their disable-backups flows,
  and coverage of primary/hypervisor/backup pool snapshots.
- To resolve: exact dataset/descendant boundary, handling of snapshot plans,
  transfer/clone dependencies, concurrency, partial failure and retries.
- Recommend behavior from inspected source; distinguish established facts from
  implementation-time checks and product choices.

## Compatibility and deployment

Assess persisted snapshot/plan/replication state, additive API and generated
clients, existing node commands, mixed versions, deployment order and rollback.
No configuration or production mutations are part of this pass.

## Documentation

Readers: the user deciding feature semantics and implementers executing a later
approved package. Current intent and proposal belong in this session's plan and
design. Future implemented behavior belongs with vpsAdmin's owning feature docs;
visible UI changes must also assess KB contracts.

## Testing plan

Source inspection only in this pass. The design must identify meaningful API
authorization, all-pool deletion, dataset boundary, dependency safety, retries,
plan behavior and PHP/React checks. No application tests are needed to validate
an unimplemented proposal. Planning/findings alone do not trigger mandatory
final change review.
