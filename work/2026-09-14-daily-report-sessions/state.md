---
lifecycle: active
---

# 2026-09-14-daily-report-sessions

## Repositories

- Read-only source inspection of canonical bare repositories:
  `repos/vpsadmin.git` and `repos/vpsfree-notification-templates.git`.
- Inspected vpsAdmin `origin/master`:
  `791ab3aa89e2f613979da6090b89785c78245db5`.
- Inspected templates `origin/master`:
  `f944ba03eba5d0d6b58b7eb856f251d1c96f2c11`.
- No feature branches or worktrees created. Portal registrations remain empty.

## Status

- Proposal prepared in `plan.md`; implementation has not started.
- Verified current session using matching `dev-session current` and
  `DEV_SESSION_SLUG=2026-09-14-daily-report-sessions`.
- Read both repository-local AGENTS.md files and applied the handoff and
  user-facing writing skills.
- Keep this session active and open for discussion and follow-up work.

## Commands run

- Fetched `origin` in both project bare repositories; remotes already use SSH.
- Inspected report generator, built-in text report, external HTML report,
  session/login/refresh/cleanup paths, password-change logs and counters,
  recovery models and completion/cleanup paths, migrations/schema, and existing
  report specs through `git show` and `git grep` on `origin/master`.
- Inspected shared workspace status and index; preserved unrelated changes.
  Fetched workspace `origin`; local master was ahead by four commits with no
  remote-only commits at the pre-commit check.
- `dev-session url 2026-09-14-daily-report-sessions --as-is` returned the portal
  URL below. Use top-level `dev-session --help`; `worktree --help` is not a
  supported subcommand. A stray `git status` in a bare repository refused as
  expected; ran the tracking status check from the shared root instead.

## Results

- Existing storage supports the proposed core metrics without new event
  logging. Query indexes may be needed after checking plans and data volume.
- Session auth types are Basic, token, and OAuth2. Login factors are not stored
  with successful sessions. Basic creates one closed session per request.
- Active counts need token expiry and OAuth2 refresh validity checks;
  `closed_at IS NULL` alone can overcount before cleanup.
- Password-change sources already distinguish authenticated, forced_reset,
  recovery, administrator, and other changes.
- Recovery requests and account attempts have different cardinalities.
  Pending, unavailable, expired, invalidated, and completed outcomes need
  distinct definitions. Completion can coexist with invalidation.
- Per-day rate-limit/queue-full counts cannot be recovered from cumulative
  counters. Recovery request records have 30-day retention; public submissions
  have one-day retention.
- No application code or templates changed, and no tests/CI or deployment ran.
  Mandatory code review does not apply to this proposal-only tracking change.

## Open questions

- Optional user clarification pending: auth-type breakdown only, or successful
  login factors as well? Proposal assumes Basic/token/OAuth2 unless answered.
- The recommended active count means open sessions with usable credentials at
  generation, subject to account restrictions. It differs from the existing
  API's purely open/closed filter; the proposal records this explicitly.
- Next step: discuss metric scope, then implement within this same initiative
  if requested. No implementation approval question has been imposed.

## Cleanup

- No temporary worktrees, clusters, services, or generated captures created.
- Do not archive, delete, stop, or otherwise retire this session without an
  explicit request for that action.

## Portal

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-14-daily-report-sessions/
