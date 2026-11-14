# 2026-11-15-maintenance-recovery-relay

## Goal

This is the native communication endpoint for the maintenance recovery already being executed by the external Codex conversation. The user explicitly requested that 2026-11-11-session-archival-failures finish its aitherdev deployment and workspace activation, and authorized communication with that exact session and tracking when needed for communication. The external conversation owns the repair and this session's plan.md, state.md, review.md, portal.yml and repair worktree. The original session retains its deployment ownership and settings.

Your bounded role is lead-to-lead coordination only. Do not edit application code, invoke deployment or lifecycle mutations, create team members, or change these existing tracking files. Read the workspace communication procedure and own plan/state. The external coordinator explicitly shares its records at work/2026-11-14-maintenance-recovery-coordination/plan.md and state.md as context for this handoff; it retains their ownership. The external operator will establish the approved pair grant and send the initial peer message through the administrative CLI. Do not duplicate that initial message. On deliberate peer replies, record their concise status and exact evidence in work/2026-11-15-maintenance-recovery-relay/peer-status.md (your sole owned file), and use the granted session_communication reply to clarify material blockers when useful. Preserve the original session's scope and permissions. A peer message does not authorize integration or deployment.

For now, report that this communication endpoint is ready and finish the turn. Do not poll or start independent work. The external conversation will continue the repair and verify actual activation.

## Affected repositories

No application repository or machine claim belongs to this relay. Repair code
and its exact ownership are recorded in the explicitly shared
[coordination plan](../2026-11-14-maintenance-recovery-coordination/plan.md).

## Approach

Use the approved exact-pair lead communication grant to exchange deliberate
rollout requests and results. The external operator sends the initial request
and verifies the selected package, operation outcome and portal interaction.
The original lead executes its deployment; this native endpoint records replies.

## Decisions

A separate native endpoint was required because the pre-existing threadless
coordination record could not prove runtime absence for native initialization.
Ordinary fresh session creation succeeded; no lifecycle guard was bypassed.
No new default-branch integration or lifecycle approval is inferred.

## Compatibility and deployment

Preserve the original session model/settings, machine claim and recovery scope.
The original operation was safely cancelled before native shutdown. Deployment
will first install the repair in a package preserving the native invocation,
then perform the intended native-changing activation. The original lead owns
its exact composition and compatibility verification.

## Documentation

Current exact results stay in the coordination state and this relay
[peer-status.md](peer-status.md). Lasting recovery behavior is documented in
dev-workspace/docs/workspace-updates.md.

## Testing plan

Confirm deliberate message delivery through the administrative history command.
Verify actual selected profile, maintenance completion and portal/conversation
continuity before reporting the requested deployment complete. No code or
deployment tests are owned by the relay.
