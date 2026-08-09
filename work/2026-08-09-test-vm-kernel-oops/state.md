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
- The mandatory standalone review completed. Its three blocking propagation
  findings were fixed and folded into the detector commit.
- vpsAdminOS feature revision `53e7bb1a9` is published. Local unit and VM
  integration tests pass; RSpec and RuboCop GitHub workflows pass, while the
  long CI workflow is pending.
- vpsAdmin pins the exact feature revision in commit `d286413d9`. Local
  `services-up` passes and the feature branch is published; GitHub workflows
  are pending.

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
- ran the standalone `mandatory-change-review`
- full osvm and test-runner RSpec suites after resolving review findings
- changed-code test-runner runs for all `crashdump/*` tests and
  `kernel/module-autoload`
- `tools/update_vpsadminos_flake.sh` with exact vpsAdminOS feature SHA
  `53e7bb1a92e003ca79f1c2cc694dadbc5d4f46f3`
- `nix develop .#api` to prepare the API bundle required by the pre-commit
  i18n hook
- `./test-runner.sh test services-up` with a dedicated state directory and
  60-second status interval

## Results

- vpsAdminOS commits:
  - `0952edfb6 tests: serialize NixOS udev workers`
  - `53e7bb1a9 tests: fail on guest kernel failures`
- vpsAdmin commit:
  - `d286413d9 flake: vpsadminos 31b3dff43 -> 53e7bb1a9`
- Focused osvm specs: 47 examples, 0 failures.
- Focused test-runner specs: 18 examples, 0 failures.
- RuboCop inspected 9 changed Ruby files with no offenses.
- Nixfmt accepted all changed Nix files.
- Evaluated `driver/nixos` kernel parameters contain both
  `rd.udev.children_max=1` and `udev.children_max=1`.
- Mandatory review result:
  - commit split accepted;
  - fixed unconditional outcome propagation so neither test-level nor
    per-script expected-failure metadata can accept a guest kernel failure;
  - fixed the end-of-run race by checking fatal state after teardown and by
    carrying a dedicated child-process/result marker into executor summaries;
  - fixed `Machine#join` and the post-poweroff reaper wait to poll kernel state
    at intervals of at most one second;
  - added regressions for expected-failure handling, end-of-run detection,
    non-retry behavior, child-result classification, and both machine waits.
- Full osvm specs after the final integration fix: 108 examples, 0 failures.
- Full test-runner specs after review fixes: 182 examples, 0 failures.
- The initial combined RSpec command mixed the two suites' `spec_helper` load
  paths and could not load `libosctl/native`. Rebuilding the native extension
  in the generic osvm shell was also invalid because it needs the symbols
  exported by the patched vpsAdminOS Ruby. The successful workflow built it
  once in `.#vpsadminos`, then ran the suites sequentially with their own
  Gemfiles. See `notes/vpsadminos/2026-08-09-rspec-native-ruby.md`.
- vpsAdmin worktree is clean at `d286413d9`, based on `origin/master`.
- Both remotes already use the required SSH form.
- The first combined crashdump run reached successful example assertions for
  `crashdump/default`, `crashdump/inspect`, and `crashdump/nfs-inspect`, but
  the console reader raised `NoMethodError` during final empty-buffer flush.
  Ruby returns no elements for `''.split("\\n", -1)`, so `lines.pop` assigned
  `nil` to the scan buffer. The detector now retains an empty string when no
  trailing element exists and has a regression for console close without
  output. The still-running superseded default process was interrupted and no
  orphan processes remained.
- The corrected combined crashdump run passed all three test scripts. All nine
  intentional panic detections in machine logs are marked `EXPECTED: true`;
  no `NoMethodError` or unexpected kernel failure was present.
- `kernel/module-autoload` passed all 16 examples in 639.54 seconds, covering
  disabled and enabled module autoloading without a guest kernel failure.
- The vpsAdminOS branch was pushed to the required SSH remote. GitHub RSpec
  and RuboCop workflows passed on `53e7bb1a9`; the long CI workflow is queued.
- The first vpsAdmin pin commit attempt was correctly stopped by
  `VpsadminApiI18n` because the component API bundle was not present. Entering
  `nix develop .#api` installed it; the rerun passed all pre-commit and
  commit-message hooks. See
  `notes/vpsadmin/2026-08-09-overcommit-api-bundle.md`.
- `services-up` passed all 27 examples in 401.82 seconds with the pinned
  framework. It booted the NixOS services guest, brought up the complete
  application stack, and produced no detected kernel failure. Combined with
  the vpsAdminOS module-autoload test, both guest types have VM coverage.
- The vpsAdmin branch was pushed to the required SSH remote. GitHub workflows
  are in progress on `d286413d9`.

## Open questions

- None. Detection is fatal-only, uses safe cooperative fail-fast propagation,
  and intentional panic tests receive a scoped message-constrained allowance.

## Cleanup

- Pending GitHub CI completion, default-branch integration, worktree removal,
  and session cleanup.
- Feature branches must remain after merge.
