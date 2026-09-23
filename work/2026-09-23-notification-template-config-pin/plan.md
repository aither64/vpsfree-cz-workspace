# 2026-09-23-notification-template-config-pin

## Goal

Update the configuration channel that supplies vpsAdmin notification templates
to the published subject-prefix revision, then integrate the configuration
feature branch into `master` as the user requested.

## Affected repositories

- `vpsfree-cz-configuration`: update the `vpsfree-notification-templates`
  channel's `vpsfreeNotificationTemplates` input. This is the channel that feeds
  vpsAdmin's notification templates; there is no channel literally named
  `vpsadmin-notification-templates`.
- `vpsfree-notification-templates`: already published source revision
  `2cfd218d9152888feea4109f064459078ea9f76e`; read-only in this initiative.

## Approach

- Work from fetched configuration `origin/master` on the dated feature branch.
- Use `confctl inputs channel update --commit vpsfree-notification-templates`
  to advance the input. Verify the generated lock pins exactly `2cfd218` and
  contains no unrelated updates.
- Run quick checks, the applicable review procedure, scoped configuration
  evaluation/build checks, and feature CI. Save the final comparison, then
  fast-forward `master` through a temporary target worktree and verify the
  published head. Retain the feature branch.

## Decisions

- The user's request in this conversation explicitly authorizes integrating
  `vpsfree-cz-configuration` into `master`. It does not request deployment.
- The existing subject-prefix initiative is visible, but `DEV_SESSION_SLUG` is
  unset for this process. The session procedure requires a separate initiative
  unless the user explicitly selects that slug, so this pin uses its own session.

## Compatibility and deployment

- This is a lock input change only. It changes template source at subsequent
  configuration builds; no persisted state, schema, API, CLI, protocol, or
  NixOS option changes are expected.
- Mixed old/new deployments can briefly send old and new subject formats.
  Reverting the lock input to the predecessor `f275bf3` restores previous
  subjects. Existing messages are unaffected. No deployment is included.

## Documentation

- Record the pin and verification in this initiative's state. The repository's
  existing `AGENTS.md` and flake channel mapping already explain the update
  mechanism; no lasting project documentation change is needed for one pin.

## Testing plan

- Check generated `flake.lock` diff, exact revision, and `git diff --check`.
- Use a scoped `confctl build` for the vpsAdmin API consumer after review, plus
  relevant GitHub Actions on the feature and integrated master heads.
