# Notification subject prefix review packet

## Outcome and acceptance

Every user-facing subject variant in vpsfree-notification-templates includes
`[vpsFree.cz] ` before the actual subject. Replies use `Re: [vpsFree.cz] ` per
user clarification. Admin-only subjects are exempt. Record the authoring rule
in repository instructions, preserving all subject ERB expressions and prose.

## Scope and commits

- Initiative: `2026-09-23-notification-subject-prefix`.
- Plan/state: `work/2026-09-23-notification-subject-prefix/{plan,state}.md`.
- Repository: `vpsfree-notification-templates`.
- Worktree: `worktrees/2026-09-23-notification-subject-prefix/vpsfree-notification-templates`.
- Base: `f275bf35abc0dc501881b5af78b1e19fb98aec68` (`origin/master` when worktree was created).
- Head: `675e326`.
- Commit split: one focused project commit combines the authoring rule with the ten
  subject variants it governs. The instruction and corrections share one
  convention and can be reviewed and reverted together. Workspace initial
  tracking is separately committed as `ae65e51`.

## Decisions and boundaries

- The user's word "suffix" means a prefix before the subject, as the requested
  order makes clear. The user explicitly confirmed `Re:` precedes the prefix.
- Generic outage mail uses configurable recipients with `user: nil`; it is not
  demonstrably admin-only, so both generic outage subjects received the prefix.
- Admin-only alert, request, and report subjects were left untouched. No body
  wording, sender metadata, template behavior, Nix inputs, or downstream
  configuration was changed. There is no dependency pin change.
- This repository is the owning template source; vpsAdmin consumes its flake
  package. The public output affected is the rendered mail Subject header.
  Reverting the source revision restores old subjects. Mixed versions may send
  both formats during rollout. Existing messages are unchanged. Outage replies
  retain Message-ID and In-Reply-To headers; no state, schema, API, protocol,
  CLI, generated configuration, or migration change is involved.

## Documentation

- Updated repository `AGENTS.md` with the subject authoring rule and admin
  exception. Checked repository `README.md`; its integration guidance remains
  accurate. No separate rollout or upgrade document is useful for this
  subject-only change; the session plan records deployment and rollback scope.

## Quick verification

- Audited all 136 subject variants, excluding only 12 admin-only directories;
  no user-facing variant lacks the prefix after optional `Re: `.
- Compared each of ten modified subject files with `HEAD`: its only content
  change is insertion of the required prefix.
- `git diff --check`: passed.
- `nix run .#check`: passed, 73 templates and 363 template files checked.
- `nix flake check`: passed, all checks passed.
- Logs: `work/2026-09-23-notification-subject-prefix/nix-run-check.log` and
  `nix-flake-check.log`.

## Review assignment

- Overall risk: low. This is a reversible subject text and authoring-guidance
  change. It does not change persisted state, authorization, public API,
  protocol, or deployment mechanics.
- Reasoning effort: xhigh.
- Lane: general only. The change contains no hand-written implementation,
  reusable abstraction, or new compatibility/deployment mechanism.
