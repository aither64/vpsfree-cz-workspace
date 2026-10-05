# Network availability and IPv4-left counter

## Goal and scope

Investigate the inflated IPv4-left value displayed by the legacy vpsAdmin PHP
WebUI and the separate vpsadmin-webui frontend, and suggest a solution. The
current request authorizes investigation and a proposal; implementation and
production changes are outside this turn.

## Affected repositories

- `vpsadmin`: authoritative API, network model, allocation paths, legacy WebUI.
- `vpsadmin-webui`: public-statistics consumer and prospective admin controls.

Inspect canonical bare repository default refs, without borrowing other sessions'
worktrees. Record inspected revisions and distinguish source evidence from the
unverified production database hypothesis.

## Approach and ownership

Architect `architect0` owns the technical investigation and proposed design in
`design.md`. Lead checks counter evidence and maintains plan, state and portal.
Trace the shared statistic, private/public network classification, allocation,
reservation, explicit selection, and network administration. Propose one backend
availability policy and additive administrative controls for both interfaces.
No implementer or reviewer is assigned for routine investigation and planning.

## Compatibility and deployment

The proposal must address additive schema/API changes, preservation of existing
assignments and routing, mixed API versions, allocation races, deployment order,
and rollback. Preserve existing data and behavior by default; retire old networks
explicitly rather than inferring inactivity from absence of current assignments.
No deployments, database changes, merges, or session cleanup are authorized.

## Documentation

Readers: developers and operators deciding how to retire networks. Current
findings, proposal and temporary rollout considerations belong in session records.
If implemented later, lasting availability semantics belong in vpsAdmin docs,
with UI documentation in the owning frontend and site rollout in session records.

## Verification plan

Use source inspection for this proposal. Implementation acceptance should cover
public/private and enabled/disabled pools, ownership and assignments, all new
allocation paths, concurrent disable/allocate, existing service preservation,
both frontend counters, additive migration and supported rollout/rollback.
Production attribution needs a read-only per-network count matching PublicStats.
