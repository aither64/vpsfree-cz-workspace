# 2026-09-03-workspace-review-lifecycle

## Goal

Make mandatory change reviews use an adaptive team of fresh `gpt-5.6-sol`
reviewers with risk-scaled reasoning effort, strengthen architecture and
repeated-code analysis, and give every new initiative one consistent committed
lifecycle from `work/` to `archive/`.

## Affected repositories

- Top-level vpsFree.cz development workspace repository only.
- `AGENTS.md` defines the workspace-wide review and tracking policies.
- `skills/mandatory-change-review/` implements the adaptive review workflow.
- `bin/dev-session`, its tests, and its documentation implement safe
  finalization.
- The vpsAdmin and vpsAdminOS `devcluster` shorthands consume the canonical
  workspace-aware session resolver.

## Approach

- Always run a general mandatory reviewer. Add an architecture/repetition
  reviewer for hand-written implementation, test, build, or configuration
  logic; add a scope/proportionality reviewer for medium/high-risk work,
  abstractions, generalized mechanisms, or material review-driven growth; and
  add a risk reviewer for security, state, public or cross-project contracts,
  host operations, destructive tooling, and deployment changes.
- Launch every reviewer with fresh context using `gpt-5.6-sol`. Use reasoning
  effort `xhigh` for low- and medium-risk changes and `max` for high-risk
  changes. Give each reviewer a focused checklist and let the coordinating
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
  and keep the managed tmux session available for the explicit archive commit.
  Stop the exact managed session only after that commit.
- Store lifecycle authority in exact YAML front matter anchored at the start of
  `state.md`; treat all Markdown body content as non-authoritative prose.
- Bind tmux creation and later mutations to immutable IDs, and make shorthand
  consumers resolve identity through `bin/dev-session current`.
- Remove `remove --all`, which conflicts with durable archival, and prevent an
  exact archived slug from being reused.

## Decisions

- The review team is adaptive: one to four reviewers based on changed areas.
- The scope/proportionality lane rejects overengineering, speculative
  generalization, duplicated upstream-tool semantics, and reviewer-driven
  expansion beyond explicit user and plan boundaries.
- Reviewer reasoning is risk-scaled: low and medium use `xhigh`, while high
  risk uses `max`; uncertainty is classified upward.
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
- Cleanup is serialized per slug and preflights every worktree before removing
  any. Detached branches, symlink escapes, and tmux sessions owned by another
  workspace are safe failures. Worktree cleanliness uses
  ordinary `git status --porcelain`, then cleanup delegates to non-force
  `git worktree remove`. Git remains the authority for other refusal cases;
  resolve the refusal and retry instead of duplicating Git's recovery-state
  implementation in workspace tooling.
- Finalization preflights the required GNU `mv` atomic no-clobber options before
  cleanup. All shells, editors, builds, and background writers must be stopped;
  the per-slug lock does not serialize external worktree writers.
- Finalization requires a committed active lifecycle in initiative history,
  uses an atomic same-filesystem no-clobber archive move, and retains a stable
  tmux session identity. `stop` verifies the committed terminal archive before
  closing a finalized session.

## Compatibility and deployment

This initiative changes local development policy and tooling only. It changes
no production code, schema, API, protocol, generated client, persisted runtime
state, or deployment order.

`bin/dev-session finalize` is additive. Removing `remove --all` is an
intentional safe failure for an obsolete destructive workflow; callers must
use `finalize` to preserve tracking. Existing active sessions remain usable and
can add and commit the new lifecycle front matter while still active before
their terminal transition. Managed tmux sessions that predate workspace
identity metadata fail closed: their work must be inspected and writers stopped
before the session is manually stopped and restarted with the same active slug.
Legacy symlinked workspace paths are normalized automatically.

## Testing plan

- Run Ruby syntax checks and the complete `test/dev_session_test.rb` suite.
- Run Bash syntax checks for both changed `devcluster` consumers.
- Cover successful finalization, lifecycle validation, prior tracking commits,
  archive collisions including dangling symlinks, ordinary dirty worktrees,
  detached worktrees, symlink escapes, exact tmux targeting, identity
  replacement, workspace ownership, committed active and archived
  states, creation replacement, consumer resolution, unsafe explicit slugs,
  archive collision races, lock contention, branch retention, cleanup ordering,
  archived-slug reuse from committed history, lifecycle-looking Markdown body
  constructs, and removal of the former `remove --all` option.
- Validate the revised skill with the skill-creator validator in a Nix Python
  environment containing PyYAML.
- Run `git diff --check` and inspect CLI help and focused diffs.
- After all intended changes are committed and quick checks pass, run the new
  mandatory review with general, architecture/repetition,
  scope/proportionality, and risk reviewers. Address findings and rerun
  affected lanes before final archival.
