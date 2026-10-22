# Limit autostart alerts to unfinished node boot

## Goal and authorization

User requested implementation of the approved four-implementer plan. A VPS
expected at node boot remains pending until actual LXC running succeeds or an
authoritative configuration change retires it. Success never rearms this boot.
No upper uptime expiry. Include osctld successful-running history. Capture boot
inventory before nodectld admits transactions, retrying up to 300 seconds of
host uptime (user selected). Implementation does not authorize merge/deployment.

## Repositories and interfaces

- vpsadminos: generic boot-wide `(pool,id)` first-running history, boot-only
  initialization, atomic /run persistence, restart reconstruction, read-only
  `ct_boot_history` / `osctl ct boot-history` interface, tests and docs.
- vpsadmin: additive `list_vps_boot_autostart` and
  `reconcile_vps_boot_autostart(ids)` supervisor RPCs; fixed boot cohort and
  pending/fulfilled/retired ledger; boot hook, transaction admission gate,
  history consumer, new capability/state/freshness/pending metrics and tests.
- vpsfree-cz-configuration: compatible capability-selected alert, unavailable
  warning and awaiting-reboot status; preserve 30m grace, 10m debounce/freshness.
- Architect-owned [design](design.md) is being reconciled to the approved plan
  before substantive implementation. It owns exact cross-component contracts.

## Backlog and ownership

| Owner | Package | Dependencies and acceptance |
| --- | --- | --- |
| architect0 | Reconcile design/contracts and resolve questions | Approved plan; no application edits |
| implementer0 | vpsadminos history/query/tests/docs | Contract; reliable actual-running proof, sticky through restart/pool operations |
| implementer1 | vpsadmin supervisor RPCs/tests/docs | Contract; consistent inventory and explicit lock-aware dispositions |
| implementer2 | nodectld ledger/enrollment/exporter/boot module/tests/docs | Fixtures first, real provider integration after 0/1; no recapture/rearm |
| implementer3 | Config alerts/tests/docs, then vpsAdmin integration scenarios | Fixed metrics; final VM scenarios after component integration |
| lead | Tracking, coordination, acceptance inspection, user-facing prose | Serialize repository Git operations; coordinate quick/final/long checks |
| reviewer0 | Mandatory independent final review | All intended changes committed, quick checks pass, complete branch inventories |

## Invariants and compatibility

Only boot hooks initialize state. Ordinary daemon start resumes it. Missing or
corrupt runtime state is unavailable, never a fresh cohort. Mid-uptime upgrades
await next reboot, distinguished by booted-system support markers. Failures and
transaction intermediates preserve obligations. Successful history takes
precedence. No database migration, restore/swap transaction change or fleet-wide
coordinated update. Nodes can update independently. Additive RPC/provider first,
then consumer and compatible rules. Old binaries ignore separate records;
rollback can restore old noisy behavior. External starts wholly unobserved by
osctld cannot be reconstructed. No deployment/input pin change without preparation
and routed checks; integration and deployment require separate explicit approval.

## Documentation

Audience: implementers and administrators. Keep durable interface/behavior docs
in owning projects, with rollout/recovery in configuration operations docs.
Session design/contracts, source provenance, review and check evidence remain
here. Lead applies user-facing writing workflow to alert prose before commit.

## Verification

Quick specs: actual running versus failed pre-start; idempotence; atomic history;
restart/export/import retention; reboot reset; corrupt/missing state; capture
before 300s and refusal after; restart deadline; API outage/admission bound;
lock-aware retirement; late VPS exclusion; metric skew and capability selection.
Then committed final whole-branch review, including no-migration provenance,
before long integration tests. Long VM scenarios: pending failure hours later;
startup/stop missed by nodectld; daemon restarts; pool export/import; prolonged
restore/swap without rearming, with known payload integrity assertions. Use the
required fresh utility watcher. Publish feature branches; retain refs and session.
