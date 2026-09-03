# 2026-09-03-workspace-review-lifecycle

## Goal

Make mandatory change reviews use an adaptive team of fresh
`gpt-5.6-sol` reviewers at maximum reasoning effort, strengthen architecture
and repeated-code analysis, and give every new initiative one consistent
committed lifecycle from `work/` to `archive/`.

## Affected repositories

- Top-level vpsFree.cz development workspace repository only.
- `AGENTS.md` defines the workspace-wide review and tracking policies.
- `skills/mandatory-change-review/` implements the adaptive review workflow.
- `bin/dev-session`, its tests, and its documentation implement safe
  finalization.

## Approach

- Always run a general mandatory reviewer. Add an architecture/repetition
  reviewer for hand-written implementation, test, build, or configuration
  logic, and add a risk reviewer for security, state, public or cross-project
  contracts, host operations, destructive tooling, and deployment changes.
- Launch every reviewer with fresh context using `gpt-5.6-sol` and reasoning
  effort `max`. Give each reviewer a focused checklist and let the coordinating
  agent synthesize all findings without majority voting.
- Require the architecture reviewer to inspect component ownership and actual
  consumers. Protect compatibility and correct layering in the current work;
  record optional adoption by other consumers as follow-up work.
- Require extraction of duplicated behavioral rules when they can drift or
  fail inconsistently. Allow trivial or intentionally independent similarity
  only with concrete rationale.
- Make active tracking live in `work/<slug>/` and terminal tracking live in
  `archive/<slug>/`. Commit actionable plan/state before project changes and at
  meaningful checkpoints.
- Add `bin/dev-session finalize` to validate a terminal lifecycle, remove only
  clean worktrees, preserve branches, move curated tracking into `archive/`,
  and stop the managed tmux session. Git staging and commits remain explicit.
- Remove `remove --all`, which conflicts with durable archival, and prevent an
  exact archived slug from being reused.

## Decisions

- The review team is adaptive: one to three reviewers based on changed areas.
- Repetition findings use a risk-based DRY policy, not unconditional
  abstraction.
- Shared-component review derives consumers from real imports, dependency
  pins, wrappers, and documentation instead of a maintained consumer catalog.
- Initiatives are archived only when complete or explicitly abandoned with no
  remaining review, CI, merge, approval, deployment, or cleanup owned by the
  session.
- Archives contain plan/state plus intentionally durable artifacts. Transient,
  reproducible, sensitive, or credential-bearing files are removed first.
- Existing historical `work/` and `archive/` directories are not reconciled by
  this initiative.

## Compatibility and deployment

This initiative changes local development policy and tooling only. It changes
no production code, schema, API, protocol, generated client, persisted runtime
state, or deployment order.

`bin/dev-session finalize` is additive. Removing `remove --all` is an
intentional safe failure for an obsolete destructive workflow; callers must
use `finalize` to preserve tracking. Existing active sessions remain usable and
can add the new lifecycle marker before finalization.

## Testing plan

- Run Ruby syntax checks and the complete `test/dev_session_test.rb` suite.
- Cover successful finalization, lifecycle validation, prior tracking commits,
  archive collisions, dirty and unknown worktree contents, unmanaged tmux
  sessions, branch retention, cleanup ordering, archived-slug reuse, and the
  removal of `remove --all`.
- Validate the revised skill with the skill-creator validator in a Nix Python
  environment containing PyYAML.
- Run `git diff --check` and inspect CLI help and focused diffs.
- After all intended changes are committed and quick checks pass, run the new
  mandatory review with general, architecture/repetition, and risk reviewers.
  Address findings and rerun affected lanes before final archival.
