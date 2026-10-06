# 2026-08-07-vpsfconf-gemfile-update

## Goal

Update the root development/test bundle in vpsfree-cz-configuration, align its
Ruby interpreter with vpsAdmin's Ruby 3.4 runtime, and automate future secure
lock-file refreshes in the existing daily update workflow.

## Affected repositories

- `vpsfree-cz-configuration`: Ruby/dev-shell contract, root Gemfile and lock,
  and daily GitHub Actions updater.
- `vpsadmin`: compatibility authority only; no changes. Its `.ruby-version`,
  dev shells, and all currently pinned configuration inputs use Ruby 3.4.

## Approach

- Pin the configuration dev shell to `ruby_3_4`, declare Ruby `~> 3.4.0` in
  Bundler, update RuboCop's target, and document the relationship to vpsAdmin.
- Add the Ruby 3.4 `csv` test dependency required by the vpsAdmin hook specs.
- Regenerate the root lock with the newest compatible Bundler and all gem
  updates permitted by the existing Gemfile constraints.
- Add `bundler-audit` to the dev shell and extend the existing daily workflow
  to update, test, audit, and conditionally commit the root lock before its
  existing atomic push.
- Keep future Ruby upgrades coordinated with vpsAdmin instead of deriving the
  dev-shell version from one channel that may advance before the others.

## Compatibility and deployment

- The root bundle and Ruby selection are development/CI tooling. Deployed
  vpsAdmin packages continue to come from their staging, production, and
  services channel inputs.
- The configuration-supplied hooks run inside vpsAdmin, so their tests use the
  same Ruby 3.4 line. Ruby 3.1 support for this development bundle is dropped.
- There are no schema, API, persisted-state, protocol, or service changes.
- Staging, production, and services can temporarily pin different vpsAdmin
  revisions. A future Ruby-line change therefore requires an explicit
  mixed-version compatibility decision and coordinated configuration update.
- Rollback is a Git revert followed by rebuilding the local bundle; old
  checkouts retain their own lock and ABI-specific gem cache.

## Testing plan

- Confirm all currently pinned vpsAdmin inputs declare Ruby 3.4.0.
- Verify the dev shell reports Ruby 3.4.x.
- Run `bundle check`, the complete RSpec hook suite, RuboCop, and an updated
  RubySec audit with no findings.
- Run `nix flake check --no-build` and `actionlint`.
- Re-run dependency resolution to verify the generated lock is idempotent.
- Install and run the repository's Overcommit hooks before committing.
- After quick verification and commits, run the mandatory standalone change
  review before any broader integration validation.
