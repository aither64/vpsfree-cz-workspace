# 2026-10-07-lead-review-defaults

## Goal

Make a two-member lead/reviewer team the default and show exact lead model and
reasoning selections in the portal's new-session form. Deploy on aitherdev.

## Affected repositories

- aither64/vpsfree-cz-workspace: site catalog, instructions, checks and runtime pin.
- aither64/dev-workspace: catalog validation, portal defaults and documentation.
- vpsfreecz/vpsfree-cz-configuration: matching runtime channel pin and deployment.

## Approach

Add the `lead_reviewed` development preset with lead-owned design and application
implementation. Extend Nix/Go validation to permit a lead to satisfy implementation
policy only when no implementation-purpose member is present and the lead owns
design. Preserve requirements for teams with implementers. Use existing catalog
metadata to render concrete settings and preserve saved creation recovery.

## Decisions

- Lead: gpt-6.1-sol/xhigh, workspace-write, allowed efforts high/xhigh.
- Reviewer: gpt-6-astra/xhigh, read-only, fresh context, session lifetime.
- Both default-team selectors use lead_reviewed; one specialist slot.
- Preserve other presets and the separate Luna/low verification watcher.
- User selected resetting both lead controls to the selected team's defaults.
- User selected deploying on aitherdev. Default-branch integration is not approved.
- Tracking-only initiative has no Codex roster; parent owns implementation.

## Compatibility and deployment

Keep catalog schema 4, roster/receipt schemas and HTTP request fields unchanged.
Existing sessions, forks and submitted retries preserve settings and prompts.
Normalize empty settings only for unsent drafts; preserve catalog-change approval.
Older validators cannot consume the new catalog composition: deploy matching
runtime and catalog together through the forward-only package workflow. No database,
daemon protocol, generated client or node configuration changes; only aitherdev
needs deployment. Preserve package/cluster ownership and transition refusals.

Publish feature branches, select the exact generic revision in the workspace's
existing nested runtime input and the configuration's dev-workspace/devWorkspace
channel, and check the deployment contract. Build/dry-activate/deploy aitherdev's
host configuration, then select the composed workspace application from its user
profile. Recovery uses a newer corrected package, not a backward profile switch.

## Documentation

Update site team ownership/model guidance and generic installed-team/portal
creation behavior. Keep exact deployment evidence and temporary branch status in
session records. Apply the writing skill directly to visible English labels.

## Testing plan

Focused Nix/Go validation and runtime projection checks; browser tests for concrete
defaults, switching teams, overrides, delayed/failed models, draft restoration,
locked requests and catalog acknowledgement. Verify exact two-member creation and
retained policy. Commit all changes and pass quick checks before independent final
whole-branch review. Run longer package checks/CI with fresh catalog-resolved
watchers afterward, then inspect installed catalog and live portal defaults.
