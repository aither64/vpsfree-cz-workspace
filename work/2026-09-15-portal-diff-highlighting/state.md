---
lifecycle: active
---

# Portal changed-character highlighting investigation

## Current summary

- Confirmed this process owns `2026-09-15-portal-diff-highlighting`.
- Screenshot shows fragmented stronger addition/deletion backgrounds, separate
  from syntax foreground colors.
- Current portal source imports the raw `diff` from `@codemirror/merge` and
  compares complete Git replacement blocks as strings. Investigating the exact
  reported payload and deployed assets before concluding.

## Next actions

Reproduce the reported character ranges and record the cause and repair options.

## Repositories

- `dev-workspace`: inspecting canonical bare repository, currently known
  `origin/master` at `9a1b16464e45d722110b448a79315a0f3ce134aa`.
- Configuration source is evidence only. No feature branches or worktrees created.

## Documentation

Read runtime `AGENTS.md`, `README.md` (Repository review), and
`docs/workspace-portal.md`. Investigation findings will be linked here.

## Verification and commands

- `dev-session current` matches `DEV_SESSION_SLUG`.
- Inspected user screenshot outside version control.
- Inspected review model, editor decorations and existing projection tests.
- Public web tool cannot access the internal portal; direct HTTPS requires the
  configured private CA and Basic authentication. No credentials disclosed.

## Review and deployment

No code changes, push, integration, or deployment. Mandatory change review does
not apply to a read-only investigation with session records only.

## Cleanup

Session remains open. User attachment remains outside Git. Shared workspace has
unrelated staged and unstaged changes; commit only this initiative's records.
