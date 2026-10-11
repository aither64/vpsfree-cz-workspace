# Compact Codex status row

## Goal and accepted decisions

Use one status row instead of showing focused-member state above a separate
other-member paragraph. Idle plus known other work becomes “Other team members
are working: architect0.” beside the existing elapsed timer. The user chose
one line with ellipsis, full hover/accessibility text, and both automatic-wait
context and other-member work inline. Explicit approval/answer requests stay
first. The user requires approval before any merge.

## Affected repositories and approach

Implement in dev-workspace, with workspace composition and
vpsfree-cz-configuration selecting the published exact runtime. Use fresh
2026-10-11-codex-status-row branches/worktrees from current master. codex-web and
the vpsFree extension need no changes. A shared presentation function supplies
the row and tab labels. Remove the separate paragraph; keep the timer readable
while text shrinks with ellipsis. Preserve three-name summaries, freshness,
attention, membership and polling behavior.

## Compatibility and deployment

This is browser presentation only: existing activity/team-statistics HTTP
contracts and stored formats remain compatible. No migration, native Codex,
roster, lifecycle or host option changes. Existing browser assets can keep using
the same server APIs. Bump static asset versions. Keep the selected extension
and sibling/follows inputs stable. Workspace and configuration must select the
same exact runtime. Build the composed package and aitherdev host, then deploy
configuration with guarded confctl activation and switch the workspace user
profile. Native launch identity must match for the live switch. Application
recovery stays forward-only: retry the same candidate or a newer compatible one;
record concrete rollout and recovery proof separately. Merge is not authorized.

## Documentation and verification

The portal guide owns the supported display behavior; session records own
source heads, review and rollout evidence. Quick checks: JS syntax, existing
browser contracts and focused Go package checks from the runtime Nix shell.
Commit the complete deliverable and obtain independent final review of the full
three-repository series before long checks. Chromium/Firefox acceptance covers
idle, sleep/subagents, explicit requests, stale/failed reads, member switching
and removal, completion and polling. Assert one line, full accessible text,
readable timer and no overflow at 1280 and 420 px. Package/composition/host
contract/build and exact-head CI precede deployment. Inspect the actual deployed
row and unchanged native/tmux identity. Leave branches published and unmerged.
