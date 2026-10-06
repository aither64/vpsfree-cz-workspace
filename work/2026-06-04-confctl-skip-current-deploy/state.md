---
lifecycle: active
---
# confctl skip current deploys state

Last updated: 2026-06-05T11:13:06+02:00

## Workspace

- Initiative: `2026-06-04-confctl-skip-current-deploy`
- Repository: `confctl`
- Branch: `2026-06-04-confctl-skip-current-deploy`
- Worktree: `worktrees/2026-06-04-confctl-skip-current-deploy/confctl`
- Base: `eb26c22 flakes: build machine metadata JSON`
- Remote: `git@github.com:vpsfreecz/confctl.git`

## Commands Run

- `git --git-dir repos/confctl.git fetch origin`
- `git --git-dir repos/confctl.git worktree add -b 2026-06-04-confctl-skip-current-deploy worktrees/2026-06-04-confctl-skip-current-deploy/confctl origin/master`
- Inspected `AGENTS.md`, `lib/confctl/cli/cluster.rb`,
  `lib/confctl/machine_status.rb`, `lib/confctl/generation/host_list.rb`,
  deploy integration tests, and Overcommit config.
- `bundle exec rspec spec/confctl/cli/cluster_skip_current_deploy_spec.rb`
  failed in the ambient shell because bundled gems were not installed there.
- `nix develop -c bundle exec rspec spec/confctl/cli/cluster_skip_current_deploy_spec.rb`
  passed: 8 examples, 0 failures.
- `nix develop -c bundle exec rubocop` passed: 117 files, no offenses.
- `nix develop -c bundle exec rspec` passed: 29 examples, 0 failures.
- `./test-runner.sh test deploy/swpins` passed in 591.22 seconds.
- `./test-runner.sh test deploy/flakes` passed in 1246.18 seconds.
- `./test-runner.sh test carrier/deploy` passed in 1878.5 seconds.
- `nix develop -c bundle exec overcommit --install` installed hooks.
- First commit attempt failed because Overcommit required signing
  `.git-hooks/pre_commit/nixfmt.rb`.
- Ambient Git hook execution failed because ambient PATH had no `rubocop` or
  `nixfmt`; committing from `nix develop` was required.
- Commit created with `git commit -F <tmpfile>`:
  `56d67a0 deploy: skip machines already on target generation`.
- `nix develop -c git push -u origin HEAD` pushed branch
  `2026-06-04-confctl-skip-current-deploy`.
- GitHub Actions after push:
  - `RSpec` run `26980621192`: success.
  - `RuboCop` run `26980621187`: success.
  - `Tests` run `26980621213`: success.
- Merge to master:
  - `git --git-dir repos/confctl.git fetch origin`
  - `git --git-dir repos/confctl.git worktree add --detach worktrees/2026-06-04-confctl-skip-current-deploy/confctl-merge-master origin/master`
  - `git merge --ff-only origin/2026-06-04-confctl-skip-current-deploy`
    fast-forwarded `eb26c22..56d67a0`.
  - `nix develop -c bundle exec rspec` passed: 29 examples, 0 failures.
  - `nix develop -c bundle exec rubocop` passed: 117 files, no offenses.
  - `git push origin HEAD:master` pushed `origin/master` to `56d67a0`.
- Cleanup:
  - `git --git-dir repos/confctl.git worktree remove --force worktrees/2026-06-04-confctl-skip-current-deploy/confctl-merge-master`
  - `git --git-dir repos/confctl.git worktree remove --force worktrees/2026-06-04-confctl-skip-current-deploy/confctl`
  - Removed the empty
    `worktrees/2026-06-04-confctl-skip-current-deploy` directory.
  - Confirmed remote `master` and remote feature branch both point at
    `56d67a0`.

## Findings

- `confctl deploy` resolves/builds `host_generations`, copies closures, then
  activates each target; `--reboot` is only allowed with action `boot` and
  reboots after activation.
- Existing manual activation skips are already propagated to reboot and health
  checks; a no-op-current skip can reuse that shape by filtering hosts before
  copy/activation.
- `MachineStatus#query` already reads `/run/current-system` for standalone
  machines and the managed profile for carried machines.
- `Generation::HostList.fetch` marks the active Nix profile generation, which
  can protect `boot`/`switch` from skipping when only runtime state matches.
- The repository declares Overcommit hooks in `.overcommit.yml`:
  `Nixfmt`, `RuboCop`, and commit-message subject handling.

## Current Status

- Implementation changes are complete, committed, pushed, merged to master,
  and cleaned up. GitHub CI passed on the feature branch before merge.
- Hooks were installed and ran successfully from `nix develop`.

## Review Decisions

- Proposed skip predicate: for `boot`/`switch`, require both current runtime
  and active profile to match the target generation; for `test` and
  `dry-activate`, require only current runtime to match.
- Proposed scope: keep `--copy-only` unchanged.
- Carried machines use the carrier-managed profile as their deployed state; a
  carried deploy is skipped when that profile already points at the target
  generation.

## Implementation Notes

- Added skip pre-filtering in `ConfCtl::Cli::Cluster`.
- Added focused RSpec coverage for standalone, carried, missing-status, and
  `--copy-only` cases.
- Extended deploy integration tests for repeated `--reboot boot` and repeated
  carried profile deploys.
- Updated `man/man8/confctl.8.md` deploy description.

## Cleanup Notes

- Removed ignored `.confctl/` test cache after RSpec. A repeated RSpec run had
  failed in `spec/generation/build_modes_spec.rb` because that spec reuses a
  fixed generation name and does not tolerate leftover `.confctl` state.
- Ignored dev-shell/cache directories remain in the worktree:
  `.bin/`, `.bundle/`, `.gems/`, and `.rubocop_cache/`.
- Removed worktrees:
  `worktrees/2026-06-04-confctl-skip-current-deploy/confctl-merge-master`
  and `worktrees/2026-06-04-confctl-skip-current-deploy/confctl`.
- Keep local and remote feature branch refs unless the user explicitly asks
  for branch deletion.

## Archival request, 2026-10-06

The workspace operator requested archival of sessions dated August 2026 or
older, retaining recorded work and branches. This checkpoint commits the
existing plan and active state before the ordinary archive transition.
