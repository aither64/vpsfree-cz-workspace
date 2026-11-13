# Scheduled workflow fixes

## Goal and scope
Diagnose failing daily updates in vpsfree-cz-configuration and
vpsadminos-org-configuration. Inventory scheduled workflows in the workspace
project map, inspect recent run evidence, and fix confirmed relevant causes.
No production machine deployment or default-branch integration is authorized.

## Approach and ownership
Architect0 owns bounded investigation, root-cause design, and design.md.
Implementers own separate repository fixes, quick checks, commits and evidence.
Lead owns tracking, acceptance, independent review dispatch and user reporting.
Prefer minimal conventional workflow changes; avoid unrelated action upgrades.

## Compatibility and recovery
Preserve schedule, permissions, updater intent and generated data contracts.
Assess runner/action/Nix compatibility and token/authentication boundaries.
No schema or persistent runtime changes expected; recover by reverting workflow
commits after integration, without changing deployed machine configurations.

## Documentation
Readers: maintainers diagnosing automation and reviewing fixes. Root cause,
audit scope and run links belong in session evidence; lasting non-obvious
workflow constraints belong beside the owning workflow where useful.

## Validation and delivery
Inspect failed-attempt logs before reruns; verify latest compatible imported
actions from official upstreams. Pass repository hooks and focused workflow
checks, commit all fixes, then independent final review of full branch histories.
Use fresh utility watchers for long/uncertain checks. Publish feature branches;
request explicit repository/target integration approval only once reviewable.
