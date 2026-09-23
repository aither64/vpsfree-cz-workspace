---
lifecycle: active
---

# 2026-09-23-notification-subject-prefix

## Status

- Scope and recipient classes identified; repository worktree and edits pending.

## Next actions

- Commit initial tracking, create the dedicated notification-template worktree,
  update the rule and subjects, then verify and review the committed changes.

## Documentation

- Repository `AGENTS.md` will own the subject-authoring rule.

## Repositories

- Planned: `vpsfree-notification-templates` on
  `2026-09-23-notification-subject-prefix`.

## Commands run

- `dev-session current` matched `DEV_SESSION_SLUG`.
- Read workspace and repository guidance; inspected metadata and vpsAdmin's
  outage sender to classify the generic outage template.

## Results

- User-facing request subjects and generic outage subjects lack the site
  prefix. The user confirmed existing `Re: [vpsFree.cz] …` subjects are valid.

## Open questions

- None blocking implementation.

## Cleanup

- Leave the session open and retain its feature branch.
