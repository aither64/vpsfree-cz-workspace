# 2026-10-14-stale-archive-status

## Goal

## Affected repositories

## Approach

## Decisions

## Compatibility and deployment

## Documentation

## Testing plan
# Stale archive status

Prevent an old session page from retaining ARCHIVE PENDING and Retry archive
after archival has finished and its operation receipt has expired. The selected
2026-10-11-diagnose-vpsadmin-api-exception is correctly archived and needs no
record or recovery repair.

Affected projects: dev-workspace (details API, browser, regressions, portal
guide), workspace (nested runtime selection), vpsfree-cz-configuration (matching
devWorkspace channel). Use new feature worktrees from current masters and keep
the completed archive-policy initiative intact.

Add pendingLifecycle to session details using the validated journal reader.
Empty means confirmed absence; failed inspection fails the read. Reconcile
initial reads, polling, details refresh and Retry against fresh archived tracking
and journal absence. Reload once, without sending another archive mutation.
Keep target and receipt checks for genuine unfinished operations. Missing fields
from older servers remain unknown.

No persisted state, database, CLI, daemon protocol, generated client or module
option changes. Old browsers ignore the additive field. New browsers keep their
last state when older servers omit it. Recovery remains forward-only under the
existing provider and coordinator contracts; preserve current native Codex and
provider selections. Deploy the matching system module before the user profile.

Readers: runtime maintainers and workspace operators. Lasting browser semantics
belong in docs/workspace-portal.md; exact rollout and evidence stay here.

Complete quick checks and independent review before longer browser/package
checks and builds. Publish feature refs over SSH without awaiting CI. Coordinate
final merge and activation jobs using prepare/approve/submit/status with actual
applicable user authorization. Merge first, then reserve target aitherdev in
integrated mode for system and profile activation. Keep ownership through
requested UI review/iterations; finish only after exact integration and settled
acceptance. Refresh stale snapshots; reconcile original uncertain attempts.
Never bypass jobs or another owner's reservation with direct pushes/deployments.
