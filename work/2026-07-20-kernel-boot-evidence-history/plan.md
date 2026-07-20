# Kernel Boot Evidence History

## Goal

Make directly reported Node boot evidence distinguishable from reconstructed
legacy history, classify boot-time precision from the evidence actually
reported by the Node, and expose the immutable kernel parameters captured for
each reported boot in the administration WebUI.

Production is assumed to have already deployed the preceding history-backfill
release and reconstructed all eligible Node history. The data migration in this
initiative must therefore correct existing backfilled and subsequently reported
rows safely.

## Affected repositories

- `vpsadmin`: classification, corrective migration, WebUI, tests and
  translations.
- `vpsfree-cz-configuration`: exact review pin and deployment runbook updates.
- `vpsadmin-kb-captures`: exact review pin, visible WebUI captures and KB
  contract verification when the contract identifies affected pages.

All repositories use the feature branch
`2026-07-20-kernel-boot-evidence-history`. Default branches are not merged
without explicit user approval after review.

## Design

### Evidence classification

- Keep event `source` as the origin dimension:
  `node_report` or `reconstructed_node_status`.
- Keep event `confidence` as the boot-time precision dimension:
  `exact`, `inferred` or `incomplete`.
- Classify a reported boot as exact when its linked event evidence contains
  `booted_at` and has no `booted_at/estimated_from_uptime` evidence error.
- Classify a reported boot as inferred when the reporter estimated boot time
  from uptime. Preserve incomplete semantics for missing required evidence.
- Reconstructed legacy history remains inferred and does not gain evidence it
  never had.

### Existing production data

Add a new data-only migration instead of modifying deployed migrations. On
`up`, reclassify eligible existing `node_report` boot events from their linked
immutable evidence, assign their stored boot time as the effective time, and
match first-reporter bootstrap events to reconstructed boots by Node, release
and a bounded boot-time tolerance. Delete only the one matched derived
reconstructed event; retain its source `node_statuses` sample and all reported
evidence and parameter snapshots. Leave unmatched reconstructed events, events
without evidence, and unrelated runtime events unchanged. Make the migration
idempotent, including protection against deleting another nearby candidate on
a repeated direct `up`. `down` is intentionally a no-op because restoring the
misleading derived duplicate or less accurate presentation would be harmful.
Capture the exact start-of-transaction event ID set needing correction and
restrict every migration write and duplicate match to that population. An
old-supervisor event outside the captured set remains uncorrected so the new
supervisor can repair its precision and delete its matching derived duplicate
together, regardless of concurrent auto-increment allocation order. Lock the
captured incorrect reported rows until correction and deletion commit so an
already-new supervisor cannot reconcile the same event concurrently and cause
the migration to consume another nearby candidate.

### First-reporter reconciliation

- The first evidence-bearing status after a Node upgrade is not itself proof
  of a reboot. Compare its boot identity with any previous evidence, and when
  there is no previous evidence, reconcile the reported boot with a matching
  reconstructed boot instead of presenting two public system boots.
- The reported event owns the immutable evidence and becomes the
  visible/current history entry. Delete its one matching derived reconstructed
  duplicate while preserving the immutable raw status sample from which it was
  calculated.
- Set every reported boot event's `effective_at` from its reported `booted_at`
  when available, so the history row shows the actual boot time rather than the
  evidence collector deployment/observation time.
- Let new supervisors reconcile a bootstrap event written by an old supervisor
  after the migration but before the rolling application update. Also repair
  an actual same-boot reboot event from that window, but only let a bootstrap
  event delete one matching reconstructed boot. Derive repaired precision from
  the immutable evidence attached to that event.
- Prevent a later forced history backfill from recreating the reconstructed
  bootstrap that exact reporting replaced.
- Advance `updated_at` for every migration data change so event and collection
  evidence revisions invalidate. Repeated `up` runs must not churn timestamps
  or revisions.

### Administration WebUI

- Replace the ambiguous single evidence-quality presentation with separate
  Origin and Time precision columns.
- Link reported boot rows to an admin-only evidence detail belonging to the
  requested Node.
- Show observation metadata and reporter revision, raw kernel command line,
  and parameters in their captured order.
- For reconstructed legacy rows, show that detailed evidence is unavailable.
- Keep the existing current Kernel parameters page unchanged.
- Reuse existing APIs and models; do not change the Node protocol or public
  client contract unless implementation proves a missing endpoint unavoidable.

### Generic system configuration identity

- Replace the deployment-specific `vpsfree_cz_configuration` component with
  the generic `system_configuration` identity for booted/current closure
  revisions.
- Preserve enum value `3`, so existing production evidence and software-change
  rows require no rewrite. Accept the legacy reporter component as an input
  alias and normalize it before validation and storage; new reporters emit only
  the generic name.
- Move the vpsFree.cz GitHub commit prefix out of the WebUI implementation and
  into the deployment configuration. An installation without a configured
  system-configuration repository renders the revision without a link.
- Keep the generic WebUI compatible with both old and new API component names
  during a rolling application deployment. Deploy the accepting API and
  supervisors before any Node begins emitting the generic reporter value.

## Compatibility and deployment

The enum already supports `exact`, so old API and WebUI processes can read
corrected rows. The migration changes data only, and deleting the redundant
derived row is safe for old and new application processes because the
authoritative reported event and raw status sample remain. No Node daemon,
vpsAdminOS or reporter protocol change is required for the boot reconciliation
itself. The component vocabulary change is wire-compatible in the new API
because it accepts both names; Nodes may remain on the old reporter indefinitely
and be upgraded only after the new API/supervisors. Historical evidence
snapshots remain immutable and readable after application rollback. A database
rollback does not recreate corrected derived history.

Deploy both backward-compatible WebUIs first so the generic component remains
visible when APIs begin emitting it. Deploy api1 normally, apply the data-only
migration from its new application shell, then deploy api2 and its supervisor.
No schema compatibility window or service quiescence is required. Keep the new
WebUI until both APIs are old if rolling the application back; leave the
corrective migration applied because its `down` is intentionally a no-op. If
bookkeeping requires marking it down, do so from the still-new api1 shell
before rolling api1 back. No Node reboot, Node redeployment or history
reconstruction is needed. Verify corrected rows on `node1.stg`, `node2.stg`
and another Node after deployment.

## Verification

- Operation specs for exact reporter timestamps, uptime fallback, missing
  fields, reconstructed events, first-reporter reconciliation, nonmatching
  real boots, rolling-window old-supervisor writes and non-boot runtime events.
- Migration specs for data-only up/no-op down, eligible and ineligible existing
  rows, idempotency, effective boot times, single-duplicate deletion, raw-status
  and evidence preservation, current-marker ownership, and event/collection
  revision invalidation without repeated-up timestamp churn.
- API contract specs confirming stable source/confidence/evidence fields.
- WebUI/browser specs for both dimensions, admin drill-down, parameter order,
  raw command line, unavailable legacy evidence, cross-Node rejection and
  member denial.
- Focused and full vpsAdmin API/WebUI suites, migrations in both directions,
  RuboCop, gettext checks and repository hooks.
- Configuration flake checks with the exact unmerged vpsAdmin feature revision.
- Capture repository checks and the canonical WebUI/KB contract workflow.
- Mandatory fresh-context change review after commits and quick checks, before
  long integration tests.

## Review and integration

Push only feature branches for user review. Present exact heads, migration
behavior, visible changes and verification results. After explicit approval,
fetch and rebase against current defaults, refresh downstream SHA pins if
needed, repeat affected checks and review, then integrate through fresh
fast-forward-only worktrees.
