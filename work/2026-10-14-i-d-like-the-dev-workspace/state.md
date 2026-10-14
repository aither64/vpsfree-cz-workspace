---
lifecycle: active
---

# 2026-10-14-i-d-like-the-dev-workspace

## Status

- Phase: proposal in progress; no application implementation or deployment.
- Verified `dev-session current` and both environment markers match this session
  and `/home/aither/workspace/ai/vpsfree.cz`.
- Saved Full-team roster checked: `architect0` ready, design-purpose,
  workspace_write, GPT-6 Astra/xhigh. Assigned proposal and `design.md` only.

## Phase checklist

- [x] Verify session identity, read procedures, inspect retained roster.
- [x] Identify portal status/title/reservation integration points.
- [ ] Reconcile architect proposal and present recommendation.
- [ ] Application implementation, local checks, independent final review.
- [ ] Deployment and readiness for use, if subsequently requested.

## Next actions

- Reconcile architect's proposal, register it as a portal artifact, and suggest
  concrete title/notification behavior to the user.

## Documentation

- [Plan](plan.md); architect's proposed design will be in `design.md`.
- Existing dev-workspace README and relevant portal-guide sections inspected.

## Repositories

- Canonical bare `repos/dev-workspace.git` and `repos/codex-web.git`, read-only.
- No registered feature worktrees or branches.

## Commands run

## Results

- Session title is static in `portal/internal/web/templates/session.html`.
- `static/app.js` already distinguishes automatic waits, user-input/approval,
  and peer work, but its timing refresh pauses in hidden pages.
- `static/coordination.js` uses identity-bound reservation holders; its session
  refresh currently requires the Reservations section to be visible.
- Proposal must support background attention delivery without unpausing all
  expensive transcript/timing/coordination reads.

## Open questions

- Notification opt-in/default, acknowledgement scope and exact marker choice are
  proposed product choices, not accepted implementation requirements yet.

## Cleanup

- No runtime operations or cleanup requested; leave session open.
