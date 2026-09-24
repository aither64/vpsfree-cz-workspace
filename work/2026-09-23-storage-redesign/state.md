---
lifecycle: active
---

# 2026-09-23-storage-redesign

## Current status

Investigation complete at source-review level. Proposed physical ZFS topology
reconciliation, safe user snapshot deletion, and a later bounded backup
dispatcher are recorded in [investigation.md](investigation.md) and
[plan.md](plan.md). No project code, production data, schema or service was
changed. Implementation and live read-only inventory remain to be done.

The lead verified `dev-session current` and both environment markers as
`2026-09-23-storage-redesign` in
`/home/aither/workspace/ai/vpsfree.cz`. The older session named by the user
was not accessed or modified. The specialists' read-only shells could not
run `dev-session current` because its transition lock is on a read-only
filesystem; they inspected canonical bare repository HEADs only.

## Repositories and ownership

- `vpsadmin` canonical bare HEAD: `9fc0648accd4`; source review only.
- `vpsadminos` canonical bare HEAD: `2166e5934fe1`; reference review only.
- No session project worktree or feature branch registered yet.
- `architect0` delivered physical topology/migration and snapshot-deletion
  design; `implementer0` delivered scheduler and node-queue feasibility.
  The lead reconciled both into the investigation record.

## Evidence and checks

- Read workspace/repository guidance, vpsAdmin storage and transaction docs,
  schema, transaction chains, node code, API specs and pending storage VM tests.
- Confirmed the current snapshot DELETE endpoint categorically refuses a
  dataset with backup presence; complex deletion tests are pending.
- Confirmed daily cron enqueues per-dataset backup tasks in a burst, while
  each backup chain acquires source and destination dataset locks; nodectld
  queues constrain running send/receive operations, not admission of chains.
- Cross-checked ZFS property and destroy semantics against official OpenZFS
  documentation linked from the investigation record.
- No tests run. The report is a design proposal; it does not assert that
  any live inventory matches the proposed graph.

## Next actions

1. Start with a read-only, exact-path/GUID topology inventory and mismatch
   report on a representative sample, then the full managed estate. This
   requires separate implementation and operator access planning.
2. Decide the policy questions in the investigation record (external clones,
   intentional holds, only common send base, all-or-nothing logical delete)
   from real data before enabling deletion.
3. Implement and review the additive topology model and guarded operations;
   migrate in bounded resumable batches and verify rollback on a copy.
4. Implement the backup dispatcher as a separate phase if prioritized.

## Documentation

Current findings and rationale live in this session because no behavior was
implemented. With implementation, move lasting invariants to vpsAdmin storage
docs and repeatable operator migration/recovery steps to its operations guide;
keep the individual rollout record in this session. Update API/WebUI/KB
documentation if deletion eligibility becomes visible to members.

## Open questions and limits

The reported 20,000 snapshots have not been counted or inventoried here.
Actual mismatch classes, scan cost, GUID multiplicity within one pool, clone
locations and backup retry frequency remain unknown. No integration or
production validation has been run.

## Cleanup

No project worktree, cluster, branch or test fixture was created. Leave this
active session open for implementation and follow-up.
