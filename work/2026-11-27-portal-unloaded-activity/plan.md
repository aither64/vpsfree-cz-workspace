# 2026-11-27-portal-unloaded-activity

## Goal

Fix persistent Activity unavailable / Timing update unavailable for unloaded,
verified idle Codex conversations. Preserve fresh-thread and turn identity checks
and keep display evidence separate from execution permission.

## Affected repositories

- dev-workspace: display projection, recovery evidence, browser regressions/docs.
- workspace: exact composed runtime selection.
- vpsfree-cz-configuration: matching devWorkspace channel for aitherdev.

## Approach

Use the existing verified-idle recovery mechanism for unloaded conversation
display. Require matching fresh activity and invalidate proof after newer activity
or thread changes. Verify the full browser path, commit and independently review,
then publish, integrate and deploy the matching system/profile pair.

## Decisions

User requested implementation, authorized aitherdev deployment through
vpsfree-cz-configuration, and said "merge when done" on 2026-11-27. This authorizes
integration into the default master branches of the three affected repositories.
This is a new threadless CLI initiative because this conversation has no portal
session binding or retained team; no team settings are changed.

## Compatibility and deployment

Display-only behavior; no state schema, protocol or Codex version changes.
Unloaded status alone must never establish idle or resume a native conversation.
Select one runtime revision in the workspace and configuration. Build/review before
activation, hold the configured aitherdev machine claim, verify system/profile
and portal continuity, and release after settled deployment. Preserve current
deployed input lineage; recover forward if package activation fails.

## Documentation

Maintainers: update the existing activity display paragraph in
dev-workspace/docs/workspace-portal.md. Individual deployment evidence belongs in
this initiative's state/rollout records. No new user-facing text is planned.

## Testing plan

Quick: focused browser regressions, JavaScript syntax, diff checks. Independent
review of the complete committed change before longer package verification.
Then applicable package checks, matching-pin validator, aitherdev build/dry-activate,
and live unloaded-session activity/display proof after deployment.
