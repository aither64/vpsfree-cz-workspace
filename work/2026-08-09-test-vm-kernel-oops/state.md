# 2026-08-09-test-vm-kernel-oops

## Repositories

- `vpsadminos`
  - branch: `2026-08-09-test-vm-kernel-oops`
  - worktree: `worktrees/2026-08-09-test-vm-kernel-oops/vpsadminos`
  - base: `origin/staging` / `837baf040`
- `vpsadmin`
  - branch: `2026-08-09-test-vm-kernel-oops`
  - worktree: `worktrees/2026-08-09-test-vm-kernel-oops/vpsadmin`
  - base: `origin/master` / `63c2c44f6`

## Status

- Separate development session and both repository worktrees prepared.
- Root cause evidence identifies recurring Linux 6.18 parallel module-loading
  failures in generated NixOS guests. The implementation uses udev
  serialization and shared guest-kernel failure detection; no kernel patch.
- vpsAdminOS implementation is committed and ready for standalone review.
- vpsAdmin input update and integration validation are pending the review and
  publication of the vpsAdminOS feature revision.

## Commands run

- `bin/dev-session current`
- `bin/dev-session start 2026-08-09-test-vm-kernel-oops --as-is --new
  --no-attach --no-codex` (rejected because `--as-is` and `--new` conflict)
- `bin/dev-session start 2026-08-09-test-vm-kernel-oops --as-is
  --no-attach --no-codex`
- fetched `origin` in the canonical vpsAdminOS and vpsAdmin bare repositories
- added vpsAdminOS and vpsAdmin worktrees with `bin/dev-session worktree add`
- read both repository-local `AGENTS.md` files
- `git diff --check`
- `nix develop .#vpsadminos --command nixfmt --check` on the changed Nix files
- `nix develop .#vpsadminos --command bundle exec rubocop` on the changed Ruby
  files
- focused osvm and test-runner RSpec suites in their supported environments
- built the evaluated `driver/nixos` test JSON and inspected the machine kernel
  parameters
- committed from `nix develop .#vpsadminos`; Overcommit ran Nixfmt and RuboCop

## Results

- vpsAdminOS commits:
  - `0952edfb6 tests: serialize NixOS udev workers`
  - `976187b30 tests: fail on guest kernel failures`
- Focused osvm specs: 47 examples, 0 failures.
- Focused test-runner specs: 18 examples, 0 failures.
- RuboCop inspected 9 changed Ruby files with no offenses.
- Nixfmt accepted all changed Nix files.
- Evaluated `driver/nixos` kernel parameters contain both
  `rd.udev.children_max=1` and `udev.children_max=1`.
- The initial combined RSpec command mixed the two suites' `spec_helper` load
  paths and could not load `libosctl/native`. Rebuilding the native extension
  in the generic osvm shell was also invalid because it needs the symbols
  exported by the patched vpsAdminOS Ruby. The successful workflow built it
  once in `.#vpsadminos`, then ran the suites sequentially with their own
  Gemfiles. See `notes/vpsadminos/2026-08-09-rspec-native-ruby.md`.
- vpsAdmin worktree is clean at current `origin/master`.
- Both remotes already use the required SSH form.

## Open questions

- None. Detection is fatal-only, uses safe cooperative fail-fast propagation,
  and intentional panic tests receive a scoped message-constrained allowance.

## Cleanup

- Pending standalone review, full specs, VM integration tests, vpsAdmin input
  update, `services-up`, CI, integration, worktree removal, and session cleanup.
- Feature branches must remain after merge.
