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
  failures in generated NixOS guests. The implementation will use udev
  serialization and shared guest-kernel failure detection; no kernel patch.

## Commands run

- `bin/dev-session current`
- `bin/dev-session start 2026-08-09-test-vm-kernel-oops --as-is --new
  --no-attach --no-codex` (rejected because `--as-is` and `--new` conflict)
- `bin/dev-session start 2026-08-09-test-vm-kernel-oops --as-is
  --no-attach --no-codex`
- fetched `origin` in the canonical vpsAdminOS and vpsAdmin bare repositories
- added vpsAdminOS and vpsAdmin worktrees with `bin/dev-session worktree add`
- read both repository-local `AGENTS.md` files

## Results

- vpsAdminOS worktree is clean at current `origin/staging`.
- vpsAdmin worktree is clean at current `origin/master`.
- Both remotes already use the required SSH form.

## Open questions

- None. Detection is fatal-only, uses safe cooperative fail-fast propagation,
  and intentional panic tests receive a scoped message-constrained allowance.

## Cleanup

- Pending implementation, integration, worktree removal, and session cleanup.
- Feature branches must remain after merge.
