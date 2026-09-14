# Portal reliability and session recovery

## Goal and decisions

Implement the accepted September 13 plan: recover failed session creation and retain its prompt in the portal; quiet brief conversation reconnections; report cluster operations accurately and stop development VMs concurrently; retain exact repository comparisons after integration. Deploy the workspace user profile and matching aitherdev configuration. User explicitly authorized deployment through vpsfree-cz-configuration. On September 14 the user explicitly requested integration into all default branches, including configuration. Preserve the open session and retained branches; archival is not requested.

User choices: ten-second background reconnection grace; saved prompt visible with copy, no editing of accepted requests; fix shutdown and status together; parallel VM shutdown.

## Affected components

- aither64/codex-web: browser synchronization.
- aither64/dev-workspace: recovery policy, creation prompt/drafts, cluster status, comparison capture CLI and portal.
- vpsfreecz/dev-workspace (local vpsfree-dev-workspace): concurrent bounded shutdown, nonblocking status, package pins.
- workspace: integration capture workflow and user-profile source pin in a dedicated feature worktree.
- vpsfree-cz-configuration: matching devWorkspace input and aitherdev deployment through confctl.

Use branch/worktree group 2026-09-13-portal-reliability throughout. Bootstrap the initiative with --no-codex because ordinary initialization is broken; do not reuse another session. Recover 2026-09-13-auth-email through its existing journal and receipt using the reviewed candidate portal with the installed generation; then activate the profile through workspace-host.

## Implementation

Keep authoritative Codex thread discovery, preserving loaded/unmaterialized, recorded identity, ambiguity and pagination checks. A measured filtered scan takes 61.265 seconds, beyond the old 60-second deadline. Allow 180 seconds for the thread command, 210 for dev-session and 240 for receipt reconciliation. Reject the indexed shortcut: even a nonempty index can omit existing rollout history and cannot prove uniqueness. Render accepted initial prompt in the creation page with copy. Preserve form drafts through validation/network failures and clear only after confirmed acceptance.

Keep healthy event streams across tab focus; background recovery warnings appear only after ten visible seconds. Access errors appear immediately. Preserve conversation/drafts/send receipts.

Stop independent VMs concurrently with a 120-second complete per-machine grace, 10-second forced reaping and 20-second cleanup margin. Share provider-owned budgets between Ruby and shell; validate the 150-second wrapper budget against the published 180-second portal release deadline. Reset uses the same routine. The additive runtime contract publishes busy exit code 75 and the release deadline. Nonblocking status returns the dedicated busy exit status; show busy/errors per session/provider without a global generic cluster warning. Verify processes are gone before clearing runtime markers.

Add dev-session worktree capture-comparison <slug> <name> --as-is [--base SHA --head SHA]. Persist validated immutable base/head pairs using existing private comparison storage. Capture after final rebase and before integration via workspace workflow, plus observed unmerged heads during status refresh. Preserve historical review links. Recover password-reset pairs from its merge-revisions-20260913.json using previous_default and feature_head. Clearly label fallback when no trustworthy pair is available.

## Compatibility and deployment

Retain Codex 0.154.0, validate its generated request schema. Keep manifests/lifecycle journals/comparison formats readable by prior generations. New portal recognizes dedicated provider busy status; package deploys reader and providers together. Old runners remain stoppable; no coordinated node updates, database migrations, API-client/CLI changes outside the new optional interfaces, guest format changes, or kernel changes are planned. Respect profile transition locks. Dependency order: codex-web -> dev-workspace -> vpsfree-dev-workspace -> workspace profile and matching configuration host module. Configuration pins use confctl. Build/dry-activate/deploy from feature worktrees; do not merge configuration to deploy. Preserve prior profile/system generations for rollback and other sessions.

## Verification

Run focused Go/Ruby/browser tests for authoritative lookup, ambiguity/retry/prompt preservation, ten-second reconnection grace, slow/stuck concurrent guests and busy probes, and capture/rebase/merge/archive comparisons. Apply writing skill before committing. Commit all intended changes, quick verify, mandatory general/architecture/scope/risk review with gpt-5.6-sol xhigh, reconcile findings, then packaged/live integration checks. Monitor pushed branch CI. Retry auth-email exactly once via receipt, verify single original prompt submission, verify password-reset comparisons and cross-tab cluster behavior. Record deployment and rollback compatibility, keep initiative open, include stable portal URL.

## Default-branch integration

Fetch each default branch, preserve the reviewed implementation, capture the final exact comparison, and integrate with fast-forward-only merges. Use fresh temporary target worktrees for independent repositories and the shared master checkout for workspace integration. Rebase the workspace feature over the latest coordination commits; confirm its two functional patches are unchanged. Run packaged checks and aitherdev configuration build from the integration worktrees, push defaults, monitor CI, and prove every final feature head is contained in its remote master. Keep deployment generations because the application and configuration revisions remain unchanged. Remove only temporary integration worktrees and generated files.
