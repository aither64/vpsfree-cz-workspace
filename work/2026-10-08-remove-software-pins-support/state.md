---
lifecycle: active
---

# Remove software pins from confctl

## Status

Repository investigation and the implementation plan are complete. The lead
reconciled architect0's detailed brief into [plan.md](plan.md) and accepted its
compatibility and verification decisions. The user's request is plan-only; no
application edits, application tests, independent final review, publication or
deployment have been performed. The confctl branch is still exactly its base.

## Phase checklist

- [x] Verify session identity and inspect retained Full-team roster.
- [x] Create/register a dedicated confctl worktree and read repository guidance.
- [x] Complete repository walkthrough and architect-owned design brief.
- [x] Reconcile and commit the initial plan/state/design checkpoint.
- [ ] Implement when requested, then run quick checks and independent final review.
- [ ] Run longer verification and prepare branch readiness when implementation exists.
- [ ] Integrate only with explicit repository/target approval.

## Next actions

Present the saved plan. If implementation is requested, recheck the retained
roster and assign the accepted brief to workspace-write implementer0. No user
clarification is needed to finish planning. Integration and any live deployment
remain separately authorized later actions.

## Documentation

Current intent and compatibility constraints are in [plan.md](plan.md); detailed
technical inventory is in [design.md](design.md). This turn changes only
coordination artifacts. No project documentation update is needed until the
planned behavior is implemented.

## Repositories

- Identity: `dev-session current`, both environment markers and the trusted thread
  binding agree on `2026-10-08-remove-software-pins-support` at
  `/home/aither/workspace/ai/vpsfree.cz`.
- `architect0`: ready design-purpose member; saved model `gpt-6-astra`, effort
  `xhigh`, access `workspace_write`; assigned walkthrough and `design.md` only.
- `implementer0`: retained implementation-purpose member, not assigned this turn.
- `reviewer0`: retained review-purpose member, not assigned for planning.
- confctl worktree:
  `worktrees/2026-10-08-remove-software-pins-support/confctl`.
- Branch: `2026-10-08-remove-software-pins-support`; target `origin/master`.
- Initial base and inspected head: `1b56616eff41e760327f3a0dbed8875e4aa9dbec`
  (`Version 3.0.0`). No feature commits or application diff.

## Commands run

- Verified session identity, retained roster and procedure/repository guidance.
- Initial `dev-session worktree add ... --no-fetch` created the branch/worktree
  but returned nonzero because its Overcommit post-checkout configuration was
  unsigned. A repeat verified the existing worktree and registered it successfully.
  No hook was bypassed. Before future hook-bearing Git operations, follow
  `notes/confctl/2026-08-04-overcommit-worktree-signature.md` and sign the reviewed
  config from the repository's Nix shell. Inspection requires no hook operation.
- Workspace `git fetch origin` succeeded; shared `master` was one commit ahead
  of `origin/master`, with no staged paths. Preserve unrelated session files.
- Canonical confctl `git fetch origin` succeeded and confirmed `origin/master`
  remains at the inspected initial base.
- Stable portal URL resolves to the deployed authentication endpoint (HTTP 401).
  The shell lacks the internal certificate issuer; an unauthenticated diagnostic
  HEAD with certificate verification disabled confirmed reachability. No
  credentials were supplied.

## Results

- `NixFlake` inherits `NixLegacy`: extract common copy, activation, rollback,
  profile, shell and GC helpers before deleting legacy evaluation.
- Generation persistence uses distinct software-pin and flake modes; old records
  need a deliberate policy, including roots and unsupported current selection.
- Option-documentation generation currently uses the legacy evaluator, while
  the flake backend returns no options. Preserve a useful generation path.
  Require generated `confctl.*`, `cluster.*`, carrier and program options;
  there are no repository `services.*` option declarations, so remove that
  existing empty documentation category rather than inventing coverage.
- Shared deploy integration fixtures exercise both modes and depend on both
  example trees. Simplify them while preserving flake coverage.
- The architect's repository-wide inventory covers CLI/Ruby backends and
  generations, Nix options/evaluators/exports, carrier metadata, package/shell
  dependencies, hidden example files, manuals/templates, specs, integration
  suites and CI. Existing hooks and payloads remain; removed pin/internal APIs
  are intentionally unsupported.
- Lead accepted strict rejected-record/current/numeric selector behavior and
  tool/configuration input coupling for the new option-documentation output.
  Retain the renamed example's developer shell because it has no pin dependency.
- Documentation/evidence reconciliation is complete; initial tracking checkpoint
  contains only this session's plan, state, design and portal manifest.
- Planning checks: session links/artifact exist, final manifest matches the
  registered confctl branch/base, and staged tracking whitespace check passed.
  No application checks were run because this turn prepares a plan only.

## Open questions

No planning blocker. Intentional compatibility break for software-pin clusters,
internal APIs and saved legacy generations is covered by the accepted plan.
Production migration status and external JSON/API consumers have not been
audited. The replacement option evaluator requires real evaluation during
implementation; the current flake backend returning empty options is not a
useful verification baseline.

## Cleanup

Leave the initiative active and open. No lifecycle action or integration approval
has been requested.
