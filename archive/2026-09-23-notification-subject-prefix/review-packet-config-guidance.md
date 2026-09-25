# Confctl channel guidance review packet

## Requested outcome

The user requested a notification-template channel pin in
`vpsfree-cz-configuration` and a generic instruction ensuring future
confctl-managed configurations use channel updates with generated Git history.
They withdrew approval to merge configuration into `master`; no approval to
merge the workspace instruction was given. No deployment is requested.

## Scope and commits

- Initiative: `2026-09-23-notification-subject-prefix`.
- Plan/state: `work/2026-09-23-notification-subject-prefix/{plan,state}.md`.
- Workspace worktree: `worktrees/2026-09-23-notification-subject-prefix/workspace`.
  Initially reviewed at base `d6ba1cae`, head `67f27b7`. The final feature
  branch is based on remote workspace master `7787ee79` with head `fd615bba`.
  `git range-diff` proved the rebase was patch-equivalent. One documentation
  commit changes only `docs/agent-instructions/deployment.md`.
  After review, remote master advanced; a second patch-equivalent rebase
  produced final integrated head `5b7946cc` on `1acf69b1`.
- Configuration worktree:
  `worktrees/2026-09-23-notification-subject-prefix/vpsfree-cz-configuration`.
  Base `ba83425e`, head `76ce8add`. The generated `flake.lock`-only pin commit
  is separately reviewable and falls under mandatory review's dependency-only
  exception. It preserves confctl's Git history for template commits `1cadd74`
  and `2cfd218` in its message.
- The template source is already published at `2cfd218`; its prior review and
  verification are recorded in the state. No template source change is part of
  this follow-up.

## Evidence and decisions

- `vpsfree-cz-configuration/flake.nix` maps
  `vpsfree-notification-templates` to `vpsfreeNotificationTemplates`; other
  channels include staging, production, vpsadmin, os-staging, system and
  service channels. `vpsadminos-org-configuration` also defines channels.
- `nix develop -c confctl inputs channel update --commit
  vpsfree-notification-templates` generated `76ce8add`, moving the lock from
  `f275bf3` to exactly `2cfd218`. The generated history is retained.
- `git diff --check` passed for both commits. Configuration Overcommit hooks
  passed. The scoped vpsAdmin API build passed with `confctl build --yes`;
  evidence is in `config-api-build-confirmed.log`.
- The first build invocation without `--yes` stopped at the interactive
  prompt before any build; the existing workspace note covers this behavior.
- The configuration repository has no push-triggered CI workflow.
- The documentation lives in the workspace procedure already routed by its
  `AGENTS.md`. No additional project documentation was changed; the config
  repository already documents confctl channel updates.

## Review focus

Risk classification: medium, because a cross-project deployment procedure can
affect future input changes, though this commit changes no runtime behavior.
Review general, scope/proportionality, and risk/compatibility lanes. Check that
the generic wording fits multiple channels and repositories, preserves
confctl-generated history, avoids manual lock editing, and does not imply
permission to deploy or integrate. Existing target deployments can continue to
use old pins; this instruction changes no persisted state, schema, API,
protocol, or rollback format.

No hand-written configuration logic changed. No default-branch integration or
deployment is authorized for these follow-ups.
