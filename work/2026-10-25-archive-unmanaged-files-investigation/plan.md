# 2026-10-25-archive-unmanaged-files-investigation

## Goal

Implement the accepted archive preflight and lead-assisted cleanup plan. First
repair and retry the original `2026-10-22-haveapi-release` archive, then add a
read-only readiness command and durable portal preparation before agent shutdown.
The user explicitly requested implementation after accepting preflight-only repair
and progress-based retries (stop after three completed cycles without progress).

## Affected repositories

- `dev-workspace`: archive discovery, journaled cleanup and portal feedback.
- Coordination workspace: this initiative's tracking and evidence.
- `vpsfree-cz-configuration`: starting location; no configuration changes needed.

## Approach

Preserve the investigation in findings.md. Move the verified hook cache inside
its canonical checkout and retry the retained portal operation. Implement on the
registered dev-workspace feature branch, with design in design.md. Complete quick
checks and commits, independent review, then packaged integration tests. Preserve
master branches; implementation does not authorize their integration.

## Decisions

The approved plan supersedes the earlier investigation-only scope. Repair is
limited to the reported session and its original archive intent. No generic
auxiliary-file deletion and no lead revival after partial destructive archival.
The existing threadless initiative has no retained team; implementation stays
with the lead, with catalog-resolved independent review and verification watchers.

## Compatibility and deployment

Keep archive journal formats and strict automatic archive policy unchanged.
Preparation is private portal state, never a lifecycle reservation. Package
transitions park preparation as retryable failure; supported packages must never
leave an old portal receipt permanently running because of unknown preparation.
Recheck generation, session target and native message identity at each boundary.

## Documentation

Readers: the operator deciding on repair and developers implementing prevention.
Keep the original incident findings and proposal in [findings.md](findings.md).
Supported behavior is documented in the runtime's archive and session guides;
its README describes the native lifecycle verification path.

## Testing plan

Cover structural blockers without agent shutdown or journals, lead repair
progress and no progress, uncertain delivery, restart/browser closure,
cancellation and stale identity. Verify unrelated operations remain available.
Run focused checks before independent review and packaged lifecycle tests after
review. Retain all live-recovery results in state.md and recovery.md.
