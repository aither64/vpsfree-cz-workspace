# 2026-09-04-workspace-tracking-cadence

## Goal

Reduce tracking-only commit churn in the shared workspace repository while
retaining useful recovery checkpoints for initiatives that span multiple
active working days.

## Affected repositories

- Top-level vpsFree.cz development workspace repository only.
- `AGENTS.md` defines the authoritative tracking cadence.
- `docs/dev-sessions.md` documents the lifecycle for workspace users.
- `test/dev_session_test.rb` protects the existing two-commit finalization
  path.

## Approach

- Make short initiatives use two tracking commits: the initial committed active
  plan/state and the final committed archive.
- Let unfinished multi-day initiatives make at most one consolidated
  tracking-only checkpoint per active day when material progress occurred.
- Permit an additional same-day checkpoint only for a genuine ownership
  handoff, an explicit user request, or a pause until a future working day when
  resumability matters.
- Do not make separate tracking commits for individual reviews, remediations,
  tests, CI observations, rebases, deployments, commands, or status polls.
- Keep ordinary functional commits outside the tracking-only cadence.
- Document that terminal tracking can remain uncommitted until `finalize` moves
  it into `archive/`, where the exact move and final state are committed once.
- Update the main finalization test to exercise and count this two-commit path.

## Compatibility and deployment

This changes local development policy, documentation, and regression coverage
only. It does not change `bin/dev-session`, production code, schemas, APIs,
protocols, persisted state, or deployment ordering. Existing initiatives and
published workspace history remain unchanged.

## Testing plan

- Run `ruby -c test/dev_session_test.rb`.
- Run `ruby -Itest test/dev_session_test.rb`.
- Run `git diff --check` for the changed paths.
- Run the mandatory change review at `xhigh` after the functional commit and
  quick verification.
