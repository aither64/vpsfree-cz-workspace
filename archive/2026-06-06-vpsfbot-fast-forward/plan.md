# 2026-06-06-vpsfbot-fast-forward

## Goal

Improve `vpsfree-irc-bot` GitHub push announcements for fast-forward and
force-push events. The current fast-forward message says only:

```text
[vpsfree-cz-configuration] aither64 fast-forwarded master to b413ab093
```

This gives readers no link and no source revision. The desired behavior is:

- mention both the old and new commit when GitHub provides them;
- link to the GitHub comparison between those revisions;
- when a comparison URL cannot be determined, at least link to the target
  commit;
- make sure forced updates are announced as force-pushes even when the commits
  in the payload are all non-distinct.

## Affected repositories

- `vpsfree-irc-bot`
  - Worktree: `worktrees/2026-06-06-vpsfbot-fast-forward/vpsfree-irc-bot`
  - Branch: `2026-06-06-vpsfbot-fast-forward`
  - Base: `origin/master` at `a7393bbe514958ad76ccd5ba86406b0270511297`

## Approach

The relevant code is `VpsFree::Irc::Bot::GitHubWebHook::PushEvent#to_s` in
`lib/vpsfree-irc-bot/github_webhook/event.rb`.

Current behavior:

- `PushEvent` extracts `before`, `after`, `forced`, and `compare` from the
  GitHub payload.
- `fast_forward?` is true when all commits are non-distinct.
- `forced` identifies force-pushes, but the current fast-forward branch is
  checked first.
- The fast-forward branch returns early after writing
  `fast-forwarded <branch> to <after-short>`, so it skips the existing
  `compare` URL used for normal push announcements.

Planned implementation:

1. Handle `forced` before `fast_forward?`, so forced updates cannot be
   mislabeled as fast-forwarded.

2. Change the concise ref-update text to include both ends when `before` is
   present, for example:

   ```text
   [vpsfree-cz-configuration] aither64 fast-forwarded master from 123456789 to b413ab093
   ```

   Force-pushes should use the same shape:

   ```text
   [vpsfree-cz-configuration] aither64 force-pushed master from 123456789 to b413ab093
   ```

3. Add a second line containing the best URL available:

   - prefer the payload-provided `compare` URL;
   - otherwise build `#{repository.html_url}/compare/#{before}...#{after}`
     when both SHAs are present and `before` is not the all-zero creation SHA;
   - otherwise use `#{repository.html_url}/commit/#{after}` when `after` is
     present.

4. Keep ordinary non-forced push formatting unchanged.

5. Add focused specs for `PushEvent#to_s`, preferably in a new
   `spec/vpsfree/irc/bot/github_webhook/event_spec.rb`:

   - fast-forward with payload `compare` includes `from <before-short>`,
     `to <after-short>`, and the compare URL;
   - fast-forward without `compare` falls back to a commit URL when a compare
     cannot be safely formed;
   - force-push with non-distinct commits is announced as `force-pushed`;
   - normal push output still includes commit summaries and the compare URL.

## Compatibility and deployment

This is a presentation-only change in IRC announcements. It does not change:

- persisted state or on-disk formats;
- database schemas or migrations;
- API contracts, generated clients, CLI behavior, or Terraform behavior;
- protocols between services and daemons;
- NixOS/vpsAdminOS module options or generated configuration.

Deployment is compatible with rolling updates. Old bot instances will continue
to emit the old one-line fast-forward message until restarted or replaced. New
instances can be deployed independently and will emit two-line messages for
fast-forward events when a URL is available.

Rollback is safe. State created by the new version is not persisted, and old
versions can continue processing the same webhook payloads.

## Testing plan

Run from the repository dev shell:

```sh
nix develop -c bundle exec rspec
nix develop -c bundle exec rubocop
```

Before committing, install and run the declared Overcommit hooks from the Nix
development shell, because `.overcommit.yml` enables RuboCop for pre-commit:

```sh
nix develop -c bundle exec overcommit --install
nix develop -c bundle exec overcommit --run
```
