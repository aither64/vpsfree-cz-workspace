---
lifecycle: active
---

# Automatic coordination storage cleanup

Phase: design complete; implementation starting. The user explicitly authorized
tracking after initially requesting untracked diagnosis.

## Phase checklist

- [x] Attribute current disk growth and identify collector exclusions.
- [x] Record compatibility, recovery and verification design.
- [ ] Implement automatic cleanup and focused regression coverage.
- [ ] Commit changes and complete quick checks.
- [ ] Independent whole-branch review and longer verification.
- [ ] Publish; prepare coordinated rollout/integration as authorized.

## Repository

- dev-workspace: worktrees/2026-10-19-coordination-storage-cleanup/dev-workspace
- Branch: 2026-10-19-coordination-storage-cleanup
- Initial base: 8385699aabcc2cfc74b585ca653a4658ff3eef75
- No code edits or project commits yet. Shared workspace remains on master;
  preserve substantial unrelated working-tree changes and shared index contents.

## Identity and policy

Created via dev-session start coordination-storage-cleanup --no-codex --no-attach.
Both literal DEV_SESSION values and current agree. Threadless startup avoids a
second active lead conversation; team list consequently reports no valid lead
thread. Lead work uses ordinary supported resolution. Installed catalog fallback
selects final reviewer and utility watcher; no team members are invented.
The earlier untracked checkout was moved/renamed into this newly registered scope.
A start attempt using the pre-existing untracked worktree name correctly refused
missing portal metadata; no legacy tracking was repaired or bypassed.

## Findings and next action

Coordination source checkouts use 45.4 GiB and integration scratch 34.8 GiB.
All but two retained integration directories have complete journals. Large
complete examples belong to archive-worker-authorization (5.0 GiB) and
portal-session-request-fix (5.0 GiB for one run). Notification package roots,
workspace profiles 140..163, explicit candidates and processes retain Nix sources.
The latest pressure GC freed only 2.8 GiB. Implement the design, preserving all
live operation and recovery dependencies. Master integration is not authorized.

Documentation: owning docs/coordination-operations.md plus this plan/design/state.
No cleanup, deployment, master merge or unrelated session mutation performed.
