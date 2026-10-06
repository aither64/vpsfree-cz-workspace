# GitHub event verbosity

## Goal

Reduce GitHub event noise from vpsfree-irc-bot in `#vpsfree`.

Desired behavior:

- `#vpsfree` should keep receiving default-branch change notifications.
- `#vpsfree` should keep receiving issue and pull request notifications as it
  does now.
- `#vpsfree` should stop receiving push notifications for non-default
  branches.
- `#vpsadminos` should keep receiving all GitHub event notifications as it does
  now.

## Affected repositories

- `vpsfree-irc-bot`: bot behavior, tests, RuboCop/Overcommit setup, flake
  development shell, and GitHub Actions.
- `vpsfree-cz-configuration`: deployment configuration and package/input pin if
  needed after the bot change is merged or pinned.

## Compatibility and deployment notes

- The bot now supports both legacy channel repository lists and the new
  per-channel policy object.
- Legacy configs keep the previous behavior: all globally announced GitHub
  events for all branches of listed repositories.
- The `#vpsfree` production channel uses the new policy object with:
  `repositories`, `event_types = [ "push" "issues" "pull_request" ]`, and
  `default_branch_only = true`.
- The `#vpsadminos` production channel remains on the legacy repository-list
  policy and receives all supported GitHub events as before.
- The package pin in `vpsfree-cz-configuration` targets final bot branch head
  `c6913e184993de4cbbdc7039ac56ba528c050e98`, so the deployed source matches
  the reviewed branch. This also means the source includes development tooling
  metadata; the targeted `int.vpsfbot` build was validated after the pin.
- Replacing `shell.nix` with `flake.nix` changes local and CI development
  tooling only. The deployed bot package still builds from `Gemfile.lock` and
  `gemset.nix` through the configuration repository.
- Bot `master` also contains direct prompt-only commit
  `3e26dfe0a5a57f2202d9bad92a887b08643c16a3`, which prefixes interactive
  flake development shells with `(vpsfree-irc-bot)`. The configuration package
  pin intentionally remains at `c6913e184993de4cbbdc7039ac56ba528c050e98`
  because the prompt change affects local development only.
- New bot with old config is backward-compatible.
- Old bot with new policy config would not interpret the policy object
  correctly, so deploy the package pin and `int.vpsfbot` config together.
- No persisted state, database migration, wire protocol, or vpsAdminOS
  coordinated node rollout is involved.

## Testing plan

- `vpsfree-irc-bot`: run `nix develop -c bundle exec rspec`.
- `vpsfree-irc-bot`: run `nix develop -c bundle exec rubocop`.
- `vpsfree-irc-bot`: run `nix develop -c bundle exec overcommit --run` after
  signing local hook config.
- `vpsfree-irc-bot`: run `bash -n tools/update_nixpkgs_flake.sh`,
  `git diff --check`, and `actionlint` for the GitHub workflows.
- `vpsfree-irc-bot`: confirm the GitHub Actions RSpec workflow passes on the
  pushed branch.
- `vpsfree-cz-configuration`: format changed Nix files with
  `nixfmt-rfc-style`.
- `vpsfree-cz-configuration`: run
  `nix develop -c confctl build -y cz.vpsfree/containers/int.vpsfbot`.
