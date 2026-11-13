# Actionable container start diagnostics and shutdown/import race

## Goal and scope
Implement actionable diagnostics for all existing start admission gates, shared by start/restart/boot where applicable. Explain recovery taint and safe inspection/recovery prerequisites without weakening host-link ownership or force safety. Investigate the reported CT1391 shutdown overlapping osctld restart/import and recommend the smallest safe race fix; broader lifecycle implementation is proposal only.

## Affected repositories
- vpsadminos: new feature branch/worktree, based on freshly verified origin/staging.
- Read-only comparison: July session records and committed vpsadminos/vpsadmin refs for 2026-07-24-ct-start-hang. Explicit user authorization permits comparison only; no mutation, resumption, repair or communication.
- Workspace: this session's tracking only. Preserve unrelated dirty files/index.

## Approach and decisions
Retained Full team with four implementers: architect owns investigation/design.md; lead assigns bounded independent packages and accepts evidence. One implementer owns narrow diagnostic source/tests/docs through commits and review fixes. Other independent packages cover July comparison, callback/import race and CLI/API/check inventory. Design precedes substantive implementation. No importing the July branch, wholesale lifecycle rewrite, production mutation, deployment or default-branch integration.

## Compatibility and recovery
Prefer no YAML/runtime-state or hook protocol schema change. Preserve every existing admission gate, identity/tenant isolation check and --force ordering. Assess CLI/API error envelope and consumers, mixed daemon versions, rollback and update coordination. Proposal must preserve shutdown versus reboot intent, stale/live/reused link safety and identity checks; distinguish evidence from unconfirmed callback response and initiator hypotheses.

## Documentation and readers
Operators: clear errors and existing recovery man page/docs. Maintainers: architect design, current race evidence, concrete July functions/tests and unresolved cases in this session. Lead applies user-facing writing skill directly before commits. Session handoff separates implementation, comparison and proposal.

## Acceptance and testing
All gates produce actionable errors; taints expose available issues with conditional safe next steps. Add proportional regressions for gates, shared entry points, force protection and error contract. All intended substantive changes committed with repository hooks and quick checks before mandatory independent final review of full base/head history and migrations. Then run required longer checks with fresh watcher, publish feature branch, inspect exact-head CI. No merge/deploy; active session remains open awaiting integration approval.
