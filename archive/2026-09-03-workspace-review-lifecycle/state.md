---
lifecycle: complete
---

# 2026-09-03-workspace-review-lifecycle

## Repositories

- Workspace repository
  - Branch: `master` (shared top-level checkout)
  - Path: `/home/aither/workspace/ai/vpsfree.cz`
  - Initiative base: `b75bc65f436aa58221055162298f3fbebf681dd0`
  - Final rule and implementation head: `05c72b0`
- No independent project worktrees were created.

## Status

- The requested review and session-lifecycle rules are implemented, reviewed,
  verified, and committed.
- Mandatory review is complete. The final general and scope reviewers found
  two remnants of the rejected Git-internals direction; both were removed and
  verified directly because the fixes only reduced behavior and surface area.
- No review, implementation, test, approval, deployment, or project-worktree
  work remains. Tracking is terminal and ready to move to `archive/`.

## Decisions

- Mandatory review is an adaptive team of one to four fresh standalone
  reviewers using `gpt-5.6-sol`.
- Low- and medium-risk changes use reasoning effort `xhigh`. High-risk changes
  use `max`; uncertain changes are classified upward. Discovery of high-risk
  scope during an `xhigh` review requires every applicable lane to rerun at
  `max`.
- General review is always required. Architecture/repetition,
  scope/proportionality, and risk/compatibility reviewers are selected by
  explicit triggers.
- The scope reviewer owns overengineering, speculative generalization,
  duplicated upstream-tool behavior, disproportionate tests or documentation,
  and reviewer-driven expansion beyond the user-approved boundary.
- A narrow requested review fix is inspected and tested by the coordinating
  agent, not sent through a recursive review loop. Only a remediation that
  creates unreviewed design, expands the boundary, or changes a public contract
  reruns the affected lane.
- Architecture review discovers actual consumers from imports, wrappers,
  manifests, dependency pins, documentation, and current repository state. It
  does not maintain a static consumer registry.
- Repetition is evaluated by maintenance and divergence risk; abstraction is
  not automatic.
- Active initiatives keep committed tracking in `work/<slug>`. Complete or
  abandoned initiatives keep committed tracking in `archive/<slug>` and have
  no remaining worktrees or managed tmux session.
- Cleanup deliberately owns only exact workspace/repository paths, registered
  worktrees, an attached shared branch, and ordinary clean status. It delegates
  removal to non-force `git worktree remove`.
- Git and the caller own repository recovery internals. The helper does not
  scan pseudorefs, reflogs, lock files, ref formats, gitlinks, ignored files,
  alternate indexes, Git environment variables, or index flags.
- A later Git refusal can leave earlier worktrees already removed. Their
  branches and tracking remain; resolve the refusal and retry. This recoverable
  partial cleanup is accepted in exchange for the simpler contract.
- Existing historical `work/` and `archive/` contents are outside this
  initiative and are not reconciled.

## Implementation

- `skills/mandatory-change-review/SKILL.md` owns review selection, risk
  classification, model/effort, packets, findings, and reruns. `AGENTS.md`
  contains only the trigger and canonical pointer.
- `references/architecture-review.md` covers component ownership, actual
  consumers, compatibility, shared benefit, and repetition. The vpsAdminOS
  test framework is its canonical workspace example.
- `references/scope-review.md` adds a focused proportionality lane distinct
  from architecture and DRY.
- `bin/dev-session` gives managed tmux sessions stable IDs and validates the
  exact workspace. Both direct `devcluster` consumers resolve the current
  initiative through `bin/dev-session current`.
- `bin/dev-session finalize` validates committed terminal tracking, checks the
  supported worktree boundary, delegates to ordinary Git removal, and performs
  an atomic no-clobber move to `archive/`. The archive move is committed before
  `bin/dev-session stop` closes the managed session.
- Lifecycle authority is exact YAML front matter at byte zero in `state.md`;
  Markdown body examples have no authority.
- `remove --all` was removed because tracking is retained through finalization.

## Consumer Evidence

The vpsAdminOS runtime test framework has seven distinct current consumers:

- `confctl` and `vpsfree-irc-bot` pin `67fcc173`;
- `vpsadmin` and `terraform-provider-vpsadmin` pin `8e44a512`;
- `vpsfree-kb-contracts` pins `6bdf458f`;
- `vpsf-status` and `web` pin `837baf04`.

`vpsadminos-org-configuration` is a separate documentation/manual consumer at
`2f0f8b6a`. `vpsadmin-kb-captures` is an alias of the contracts repository, not
another consumer identity.

## Commits

- `606cca5` — stable tmux identity and exact workspace ownership.
- `952980b` — unified cleanup, finalization, lifecycle, tests, and guidance.
- `9eec7d9` — canonical mandatory-review procedure ownership.
- `6a662a8` — risk-scaled reasoning effort.
- `6bbcba0` — scope and proportionality review lane.
- `b22d29c` — plan, decisions, review evidence, and verification state.
- `84535d2` — remove remaining lock and ignored-file policy duplicated from
  Git.
- `5258b78` — compact tracking around durable decisions and dispositions.
- `05c72b0` — prevent recursive reviewer confirmation loops.

## Verification

Current head after the proportionality fix:

- `ruby -c bin/dev-session`: passed.
- `ruby -c test/dev_session_test.rb`: passed.
- `ruby -Itest test/dev_session_test.rb`: 79 runs, 671 assertions, no
  failures, errors, or skips.
- `bash -n dev-clusters/vpsadmin/bin/devcluster`: passed.
- `bash -n dev-clusters/vpsadminos/bin/devcluster`: passed.
- `bin/dev-session --help`: exposes `finalize` and not `remove --all`.
- Skill-creator `quick_validate.py`: `Skill is valid!`.
- `git diff --check`, staged diff checks, per-commit whitespace checks, and
  commit-message line-length checks: passed.
- The repository declares no hook framework and has no active non-sample Git
  hooks.

## Review Record

Overall risk is **high** because finalization removes worktrees. Every
applicable lane therefore uses a fresh standalone `gpt-5.6-sol` reviewer at
reasoning effort `max`.

Earlier reviews targeted unpublished, subsequently rewritten local heads:
`f040054`, `66bb4a8`, `4ba9880`, `af764e6`, `63162c2`, `3915206`, `7d1657b`,
`a4179a3`, `7223df7`, `26b4dc9`, `5597eb9`, and `8ae8ca9`. Their supported
findings led to exact tmux/workspace identity, canonical path checks, committed
lifecycle transitions, atomic archival, actual-consumer evidence, direct
consumer tests, and coherent commit ownership.

Those rounds also drove cleanup into custom Git recovery-state inspection. The
user rejected that product boundary. The unpublished advanced commits and
their pseudoref, reflog, Git-lock, ref-backend, gitlink, ignored-file, and
index-flag scanners were removed. Findings that require restoring those
scanners are explicitly superseded; correctness remains required within the
smaller supported boundary above.

The first scope/proportionality review at `d2f0e0f` found 27 obsolete
CommonMark-form scenarios from a discarded lifecycle parser. They were replaced
with three representative boundary scenarios while retaining direct exact
front-matter validation. The suite fell from 938 to 690 assertions without losing
supported behavior. Its documentation/status advisory was also fixed.

The four-lane review of `b22d29c` found two Blocking proportionality remnants:

- a locked-worktree preflight duplicated a later Git refusal;
- archive closure explicitly scanned ignored files despite the ordinary-status
  contract.

Both are removed in `84535d2`, along with the dedicated lock-preflight test and
the corresponding guarantees. The scope reviewer also advised compacting this
state file; superseded round-by-round narrative was replaced by this decision,
head, finding, and disposition summary.

The general reviewer reported no other finding. Architecture/repetition had
already found the simplified ownership and consumer model coherent. Risk
findings that required duplicating Git recovery internals were superseded by
the user's explicit boundary decision. The coordinating agent inspected the
two deletion-only remediations and reran syntax, unit, skill-validation, help,
and diff checks. No new design or contract was introduced, so further reviewer
reruns were stopped as disproportionate.

## Open Questions

None.

## Cleanup

- No independent repository worktrees were created.
- `bin/dev-session finalize` moved terminal tracking to `archive/` after all
  checks passed; the exact move was committed as `c1f34c4`.
- `bin/dev-session stop` closed the managed tmux session after that commit.
