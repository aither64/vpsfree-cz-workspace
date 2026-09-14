---
lifecycle: active
---

# Portal review and recovery fixes

## Status

Implementation authorized on September 14. Shell-only session created with
dev-session start portal-review-fixes --no-codex --no-attach --json because this
existing conversation owns the work. Current session verified with matching
DEV_SESSION_SLUG and DEV_SESSION_WORKSPACE; tmux session $29. No separate Codex
thread was started. Initial substantive tracking is being committed before
project changes. Shared master contains unrelated changes which are preserved.

## Repositories

All feature branches: 2026-09-14-portal-review-fixes.
Planned worktrees beneath worktrees/2026-09-14-portal-review-fixes/:
codex-web, dev-workspace, vpsfree-dev-workspace, workspace. Registration and base
heads will be recorded after creation. No project code has changed yet.

## Investigation and commands

Read local project rules and the mandatory review, handoff, user-facing writing
and English Humanizer skills. Inspected deployed assets, GitHub's raw patch,
local Git objects and HTTP responses through the portal Unix socket. Compared
rendered line classification using an in-memory export from the deployed bundle.
Ran isolated Chromium and Firefox navigation probes through a temporary local
proxy; proxies and browsers were stopped. Inspected recent portal logs without
recording question answers or credentials. Findings and acceptance cases are in
plan.md. No production conversation was answered or interrupted by investigation.

## Validation, review and deployment

Not started. Next: create worktrees, implement bounded regression fixes, run quick
checks, commit, review, then packaged/browser/App Server tests and deployment.

## Cleanup and handoff

Keep feature branches and the session open. No archive/delete/stop authorization.
Stable portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-14-portal-review-fixes/
