# Conditional notification subject prefix: replacement review packet

## Requested result

The user clarified that `[vpsFree.cz] ` should appear only when a user-facing
subject lacks another identifying prefix. Existing `[vpsAdmin Request #…]`
subjects must keep that single prefix. `Re: ` remains before the identifying
prefix, per the earlier user clarification. Admin-only mail remains exempt.
The final change must be two commits, one for the rule and one for template
subjects. The user explicitly authorized force-pushing this repository's
published `master` to replace the earlier combined commit.

## Scope and exact commits

- Initiative: `2026-09-23-notification-subject-prefix`.
- Plan/state: `work/2026-09-23-notification-subject-prefix/{plan,state}.md`.
- Repository: `vpsfree-notification-templates`; worktree:
  `worktrees/2026-09-23-notification-subject-prefix/vpsfree-notification-templates`.
- Pre-change base: `f275bf35abc0dc501881b5af78b1e19fb98aec68`.
- Previously published combined commit, currently on both remote refs:
  `675e3264279225c52b1b87b51652fd0966bcd031`.
- Replacement commit 1: `1cadd74`, `AGENTS.md` only, conditional prefix rule.
- Replacement commit 2: `2cfd218d9152888feea4109f064459078ea9f76e`, six
  subject files only. Four request subject variants match the base and
  therefore have no new diff.
- Intended history: `f275bf3 -> 1cadd74 -> 2cfd218`; exact two commits.
  The two concerns are independently reviewable and revertible.

## Decisions and rollout boundary

- Generic outage mail has configurable recipients and is not demonstrably
  admin-only, so its two subjects receive the site prefix. IP release mails
  receive it in both languages. User request mails keep their existing
  `[vpsAdmin Request #…]` prefix, including after `Re: `.
- No body, sender, ERB expression, API, database, protocol, Nix module, or
  downstream configuration is changed. The rendered Subject header is the
  affected output. There is no new reusable logic or dependency update.
- The prior `master` merge was premature for the user's feature-branch workflow.
  Workspace instructions describe merge mechanics but do not require a separate
  project-branch integration direction. The user's current force-push
  authorization supplies that direction for this repository and head.
- The configuration repository's live advertised `master` was checked at
  `ba83425e`; its `flake.lock` still pins predecessor `f275bf3`, not published
  `675e326`. No deployed or configured consumer of the to-be-replaced commit
  was found in the inspected current configuration.
  Another collaborator could have fetched published master; changing its
  history is deliberate and user-authorized.
- Preserve old head locally at
  `refs/backup/2026-09-23-notification-subject-prefix-before-master-rewrite`.
  Push feature branch and `master` with explicit `--force-with-lease` values
  against `675e326`; stop and reassess on any lease failure. Capture the final
  branch comparison before integration. Do not touch configuration pins or
  deploy. Reverting master to old head is possible from the backup ref if the
  rewrite has to be reversed.

## Documentation

- Repository `AGENTS.md` is the authoritative authoring rule. Its new wording
  says another identifying prefix wins and `Re: ` stays before that prefix.
- Repository `README.md` was checked; its Nix integration guidance remains
  accurate. Session plan records the one-off master rewrite and rollback.

## Verification before review

- Audited all 136 subject variants: no missing or doubled prefix among
  user-facing variants; 12 admin-only template directories exempt.
- Compared six changed subject files with base: each adds only the site prefix
  after optional `Re: `. Request subject variants are byte-for-byte identical
  to base.
- `git diff --check`: passed.
- `nix run .#check`: passed, 73 templates and 363 files checked on final head.
- `nix flake check`: passed on final head.
- Feature worktree is clean at `2cfd218`.

## Review assignment

- Overall risk: high because the planned force-push rewrites already-published
  `master`, even though template behavior itself is a low-risk text correction.
- Effort: xhigh. Lanes: general, scope and proportionality, risk and
  compatibility. Architecture and repetition is not triggered: no handwritten
  implementation, reusable abstraction, or configuration logic changed.
- Please inspect both replacement commits and the proposed guarded rewrite,
  including the source and consumer evidence. Do not review only the final diff.
