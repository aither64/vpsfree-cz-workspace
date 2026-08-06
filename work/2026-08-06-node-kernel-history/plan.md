# 2026-08-06-node-kernel-history

## Goal

Make node kernel history describe effective live-patch lifecycle changes instead
of treating live-patch inventory as a public kernel change. Record newly verified
application completion, preserve legacy activation timestamps as "enabled", and
record removals. Make inferred time ranges compact and readable throughout the
kernel, system, software deployment, and sysctl history tables without losing the
full interval or its boundary semantics.

## Affected repositories

- `vpsadminos`: create a verified timestamp only after the kernel reports that a
  newly loaded live patch has completed its transition.
- `vpsadmin`: collect the verified timestamp, classify lifecycle and inventory
  events, migrate existing history, expose the lifecycle action through the API,
  and update WebUI history rendering and translations.
- `vpsadmin-kb-captures`: pin the feature revision and update the WebUI contract
  and captures if the canonical workflow detects visible drift.
- `vpsfree-cz-configuration`: pin the exact reviewed feature revisions with
  `confctl` and add deployment/rollback guidance where needed.

## Approach

### vpsAdminOS evidence

- Keep `applied_at` as the legacy timestamp at which a live-patch module became
  enabled.
- When `live-patches load` loads a previously absent module, wait with a bounded
  timeout until sysfs reports `enabled=1` and `transition=0`, then atomically
  create a persistent runtime `verified-at` timestamp. Treat a timeout or
  marker-write failure as a failed load and attempt bounded cleanup.
- Never synthesize `verified-at` for a module that was already present, because
  the actual completion time is not known. Remove stale timestamps before a new
  load and remove both timestamps when unloading.
- Report `verified_at` only while the module is loaded, enabled, and no longer in
  transition.

### vpsAdmin event model

- Keep the existing public wire event type `livepatch` and database event type
  `livepatch_change` for compatibility. Add nullable lifecycle action values
  `enabled`, `applied`, and `removed`.
- Add an internal `livepatch_inventory_change` event type. Availability,
  metadata, and transition-only changes remain auditable but do not become the
  public/current kernel state.
- Compare reports to the latest stable public kernel event, not to a transient
  inventory report. Treat a patch as effective only when loaded, enabled, and
  not transitioning.
- Classify a new effective patch with `verified_at` as `applied` and use that
  exact time. Classify legacy evidence with only `applied_at` as `enabled` and
  preserve that exact time. Classify loss of the previously effective patch as
  `removed` with inferred time.
- Coalesce a simultaneous reported kernel release change into the lifecycle
  event. Keep a release-only change as `reported_release_change`.
- Reconcile a later verified observation of the same current patch with its
  current legacy-enabled event rather than adding duplicate public history.

### Existing data

- Add a nullable action column without changing existing enum values.
- Reclassify only safely identifiable historical availability-only rows as
  internal inventory events. Preserve their evidence records.
- Mark exact legacy live-patch rows backed by `applied_at` as `enabled`. Promote
  a stable row backed by `verified_at` to `applied` only when the event's exact
  effective time matches that evidence's application time; leave later metadata
  observations and other ambiguous rows generic.
- Recompute public `current` markers for affected nodes and invalidate cached
  revisions with monotonic update times. The corrective data migration is
  idempotent and has a no-op rollback because the semantic classification
  cannot be reconstructed safely.

### WebUI

- Label public rows as “Live patch enabled”, “Live patch applied”, or “Live
  patch removed”, with the existing generic label as a fallback.
- For a bounded inferred interval `(observed_after, observed_before]`, display
  only `after <observed_after>`. Put both endpoints, their meaning, and boundary
  notation in a keyboard-accessible detail/tooltip.
- If only an upper bound exists, display `by <observed_before>`.
- Reuse the compact interval renderer in kernel, software deployment, and
  sysctl history tables. Compact system-history observation spans separately as
  `observed since <first>` with the last observation in accessible detail.

## Compatibility and deployment

- Persisted evidence remains additive: the action column is nullable and the
  internal event enum is appended, so old enum values keep their meaning.
- Old reporters remain supported and produce legacy `enabled` events. Old API
  processes can ignore `verified_at` and the nullable action. Existing API
  consumers continue to receive `event_type=livepatch`.
- New reporters may be rolled out before or after the new API; only the new API
  promotes verified completion to `applied`. The new runtime marker is ignored
  by older vpsAdminOS code.
- No coordinated all-node vpsAdminOS update is required. Mixed node and API
  versions are expected during rolling deployment.
- The reporter and API protocol supports either mixed-version direction. The
  selected rollout deploys WebUI/API and its migration first, with old
  supervisors quiesced during classification, then updates vpsAdminOS nodes
  gradually. Do not rely operationally on new exact `applied` rows until the
  node has the verified-completion reporter. Configuration pins prepare those
  builds but do not deploy them.
- The data reclassification preserves rows and evidence, but rollback does not
  restore the former public interpretation. Record a database backup before the
  migration if that presentation must be recoverable.
- After an application rollback, old supervisors must remain paused until the
  new recorder is restored or an explicit semantic-regression plan is approved.
  Old admin event endpoints that enumerate the appended enum value can fail and
  must stay out of service during such a rollback.
- Production deployment and production KB publication require separate explicit
  operator approval and are outside this implementation request.

## Testing plan

- vpsAdminOS unit/evaluation tests for verified marker creation, transition
  waiting, legacy module handling, stale marker cleanup, unload cleanup, and
  reporter gating.
- vpsAdmin operation/model/API tests covering inventory-only changes, verified
  application, legacy enablement, removal, transition samples, simultaneous
  release change, reconciliation, public filtering, and serialization.
- Migration tests for safe reclassification, legacy/applied action backfill,
  ambiguous-row preservation, current-marker repair, and repeat execution.
- PHP regression tests and an actual browser hover/focus check for lifecycle
  labels and accessible compact time rendering across all affected history
  tables; regenerate translations.
- Run quick repository checks and hooks before commits. Then run the mandatory
  fresh-context change review before long integration tests.
- Run the relevant vpsAdminOS/vpsAdmin integration suites, the KB contract and
  capture workflow, and configuration evaluation after reviewed exact pins.
