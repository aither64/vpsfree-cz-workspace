# 2026-09-23-notification-subject-prefix

## Goal

Use `[vpsFree.cz] ` before the actual subject of user-facing email templates
only when no other identifying prefix is already present. Administrator-only
templates are exempt. Remove the duplicate prefix from user request mail.

## Affected repositories

- `vpsfree-notification-templates`: ERB subject variants and authoring guidance.
- `vpsfree-cz-configuration`: update the channel that supplies the published
  notification templates to vpsAdmin on a feature branch.
- `workspace`: update its deployment procedure for all confctl-managed
  configurations, on a dedicated workspace feature branch.
- The coordination workspace holds this plan and the session state.

## Approach

- State the conditional rule in the repository `AGENTS.md`. Check for another
  identifying prefix after an optional `Re: ` reply marker.
- Audit every `templates/*/email/*.subject.erb` subject, classify recipients,
  and remove `[vpsFree.cz] ` where an existing prefix already identifies the
  mail, without changing the remaining text or ERB expressions.
- Put the rule revision and subject corrections into separate commits.
- On a dedicated configuration feature branch based on fetched `origin/master`,
  use `confctl inputs channel update --commit vpsfree-notification-templates`.
  Verify that the generated input revision is exactly `2cfd218`, review and
  check the result, then fast-forward configuration `master` after the user's
  renewed integration direction.
- Inspect the channel map and document the generic confctl channel update
  workflow, including preservation of the generated Git history in the commit
  message. Fast-forward the workspace feature branch into `master` after the
  user's renewed integration direction.

## Decisions

- The requested text is a prefix: it precedes the actual subject despite the
  word "suffix" in the request.
- The user confirmed that `Re: [vpsFree.cz] …` is the correct reply format.
- The follow-up requires an existing prefix, such as `[vpsAdmin Request #…]`,
  to take precedence. `Re: ` is a reply marker; it stays before whichever
  identifying prefix the subject uses.
- The original combined commit `675e326` was already merged and published on
  `master`. The user explicitly authorized force-pushing that `master` to
  replace it with the requested two-commit split. Rebuild from predecessor
  `f275bf3`, commit the final rule first and subject corrections second, then
  update the feature branch and `master` with explicit leases.
- The existing workspace instructions describe how to merge project branches
  but do not require a separate integration direction; this was a gap relative
  to the user's expected branch workflow. This task has explicit integration
  direction through the authorized `master` force-push.
- Generic outage mail is not demonstrably administrator-only: it is sent with
  `user: nil` and configured template recipients. Apply the user-facing rule.
- The current repository uses per-language `email/*.subject.erb` files and a
  Nix flake. The initial inspection of the bare clone's stale local `master`
  showed the former `meta.rb` format; the feature worktree is based on the
  fetched `origin/master`.
- The user subsequently requested updating the vpsAdmin notification-template
  channel in `vpsfree-cz-configuration`. The actual channel name is
  `vpsfree-notification-templates`, mapped to the
  `vpsfreeNotificationTemplates` flake input. The user withdrew permission to
  merge configuration into `master`; the feature branch remains the target.
- The API-run shell omitted `DEV_SESSION_SLUG` and `DEV_SESSION_WORKSPACE`,
  although `dev-session current` resolved this directory to this slug. The
  user explicitly instructed reuse of this original session after an
  unnecessary separate shell-only initiative was started. The portal runtime
  issue is being passed to a responsible Codex instance by the user; this
  initiative will not change the workspace runtime.
- The user clarified that the pin must use confctl's channel update and its
  generated Git history. Commit `76ce8add` already does so. They also asked
  for generic instructions across all confctl-managed configurations.
- On 2026-09-24 the user explicitly requested merging both remaining feature
  branches into their default branches. The template repository was already
  integrated. The renewed approval covers
  `vpsfree-cz-configuration/master` and workspace `master`; deployment remains
  outside scope.

## Compatibility and deployment

- Subject metadata changes only. No persisted state, schema, API, CLI, protocol,
  NixOS configuration, or body format changes are expected.
- Existing messages and their headers remain unchanged. Future messages use
  the new subjects when vpsAdmin consumes a configuration built with this
  revision. Replies retain `Re:` before their identifying prefix. The outage
  sender also sets Message-ID and In-Reply-To headers. Rolling deployment may
  briefly yield mixed subject formats. Reverting the template source revision
  restores the old subjects.
- The configuration change is limited to a downstream Nix input pin. Rolling
  deployment can briefly yield mixed old and new subject formats. Reverting
  the pin to `f275bf3` restores prior subjects. No persisted state, schema,
  API, CLI, protocol, or NixOS option changes are expected. No deployment was
  requested.
- The configuration repository's live `master` at `ba83425e` was checked
  during review; its lock still pins predecessor `f275bf3`, not the published
  `675e326` commit being replaced. Force-push with a lease against exact remote
  head `675e326`; do not overwrite an
  intervening update.

## Documentation

- Update the repository `AGENTS.md` at its subject-authoring guidance.
- Check `README.md` for any related rule or installation guidance to adjust.
  Its current build and integration guidance remains accurate.
- Update workspace `docs/agent-instructions/deployment.md` for generic confctl
  configuration updates; this is the shared procedure routed by `AGENTS.md`.

## Testing plan

- Audit every `email/*.subject.erb` against its recipient category and
  identifying prefix, including both languages and reply subjects. Verify the
  subject patch removes only the duplicate site prefix.
- Run `nix run .#check` and `nix flake check` as the repository prescribes.
- For configuration, inspect the generated lock diff and exact revision, run
  quick checks, then build the scoped vpsAdmin API consumer and inspect CI on
  the feature head. After the user's renewed merge direction, verify the exact
  pin and fast-forward the default branch.
