# GitHub notifications analysis

## Goal and scope

Analyze GitHub notifications from vpsfree-irc-bot as configured by
vpsfree-cz-configuration. Propose additions to #vpsadminos routing, verify the
mail-to-notification-template rename, and suppress GitHub Actions noise in
#vpsfree. This request authorizes analysis and a proposal, not application
implementation, deployment, or default-branch integration.

## Approach

Inspect current upstream bot and configuration sources, inventory public
vpsfreecz repositories and configured routing, and check representative GitHub
webhook/event identities. Assign technical design to retained architect0;
the lead reconciles evidence and presents the proposal. No application edits.

## Compatibility and deployment

The proposal must retain existing routing on every configured IRC network and
human-triggered notifications. Define filtering separately for event sender,
push pusher and individual commits, including mixed human/automation pushes.
Prefer optional configuration that preserves behavior when absent. Identify
bot pin/module changes and deployment order without executing a rollout.
No persistent-state or database changes are expected; confirm in analysis.

## Documentation

Session design.md holds findings, policy choices, acceptance criteria and
verification recommendations for the user and a future implementer. Project
documentation updates belong with any later implementation.

## Verification

Read-only source and GitHub metadata comparison. Recommend focused webhook
fixtures for human, automated and mixed pushes and routing on all networks.
Implementation, tests, independent change review and deployment are deferred.
