---
lifecycle: abandoned
---
# 2026-08-04-nodectld-crash

## Repositories

- `vpsadmin`
  - branch: `2026-08-04-nodectld-crash`
  - feature and integration worktrees removed after publication
  - base: `origin/master` at `3f9b68adb`
- `vpsfree-cz-configuration`
  - branch: `2026-08-04-nodectld-crash`
  - investigation worktree removed after confirming it had no source changes
  - read-only incident reference; no source change is planned
- `vpsadminos`: inspected through `repos/vpsadminos.git` only; no branch or
  worktree was created.

## Status

- Commit `50f8223c` was pushed on the retained feature branch, fast-forwarded
  into `master`, and pushed to `origin/master`. Requested worktree cleanup is
  complete. Exact-commit GitHub Actions unit workflows are green; the longer
  integration CI runs remain in progress.

## Commands run

- Verified `bin/dev-session current` and `VPSFREE_DEV_SESSION_SLUG` both equal
  `2026-08-04-nodectld-crash`.
- Inspected the shared workspace status; unrelated existing changes were left
  untouched.
- Fetched `origin` in `repos/vpsadmin.git` and read repository-local
  `AGENTS.md` from `origin/master`.
- Traced `NodeCtld::ExportMounts`, `OsCtlContainer`, the periodic update worker,
  nodectld thread handling, and the corresponding osctld container-state code.
- Confirmed that restarting osctld on `node5.brq` repopulated the missing init
  PID and stopped the immediate incident trigger.
- Created initiative worktrees for `vpsfree-cz-configuration` and `vpsadmin`.
- Read `skills/mandatory-change-review/SKILL.md` for the required post-commit
  review workflow.
- Changed `read_vps_mounts` to return an empty array when the container init PID
  is unavailable and added focused reader/update regression coverage.
- Ran the focused export-mount spec in `nix develop .#libnodectld`; the first
  run exposed that `Singleton` makes `.allocate` private, so the spec was
  corrected to allocate through `send` without starting background workers.
- The first RuboCop attempt in the libnodectld component shell failed because
  RuboCop is not in that component bundle. The successful root-shell workflow
  is recorded in
  `notes/vpsadmin/2026-08-04-libnodectld-rubocop-root-shell.md`.
- Verified that the stale Overcommit signature warning concerned an unchanged
  `.overcommit.yml` and unchanged `VpsadminApiI18n` plugin, then re-signed the
  verified pre-commit plugin in the root Nix shell.
- The first hook-backed commit attempt reached the hook suite but
  `VpsadminApiI18n` could not load Active Record from the fresh API component
  bundle. Populated it with `nix develop .#api -c bundle check` and retried with
  `RUBYOPT` unset as documented for component hook isolation.
- Committed the implementation and regression coverage as `50f8223c`
  (`libnodectld: handle missing container init PID`).
- Pushed `2026-08-04-nodectld-crash` to `origin`, retaining the feature branch
  for post-merge reference.
- Created a fresh `vpsadmin-master` worktree from the current `origin/master`,
  fast-forwarded it to the feature commit with `git merge --ff-only`, and ran
  the full component suite from the integrated tree.
- Refetched immediately before publication, confirmed `origin/master` still
  pointed to the reviewed base, and pushed the fast-forwarded `master`.
- Confirmed both vpsAdmin worktrees were clean at `50f8223c`, removed them,
  and removed the resulting empty initiative worktree directory.
- Verified after cleanup that local and remote `master` and feature-branch refs
  all resolve to `50f8223c`.

## Results

- Before the fix, `read_vps_mounts` returned nil when `ct.init_pid` was nil,
  while `update_vps_keys` unconditionally called `mounts.empty?` outside its
  rescue block.
- `Thread.abort_on_exception = true` propagates the resulting `NoMethodError`
  and exits nodectld; the NixOS module restarts it on failure.
- osctld can cache a container as running without an init PID when its runtime
  state query does not produce one. Its normal list output includes both fields,
  so this is not a missing-column compatibility issue.
- `osctl ct recover state` refreshes only the state in the current vpsAdminOS
  implementation. Restarting osctld restarts its monitors and repopulates
  `run_conf.init_pid`, which was confirmed operationally on node5.
- The smallest compatible fix is to return `[]` from `read_vps_mounts` for a
  nil init PID, preserving the existing no-publication behavior.
- Focused verification after the final spec adjustment:
  - `nix develop .#libnodectld -c bundle exec rspec
    spec/nodectld/export_mounts_spec.rb`: 2 examples, 0 failures;
  - root-shell RuboCop on the two changed files: no offenses;
  - `git diff --check`: passed.
- All declared pre-commit hooks passed on commit `50f8223c`: Nixfmt,
  MigrationSpecs, VpsadminWebuiI18n, RuboCop, and VpsadminApiI18n. Commit
  message hooks passed with only a 72-column advisory; all lines comply with
  the workspace's 80-column requirement.
- Before integration, the vpsAdmin worktree was clean and the feature branch
  was one commit ahead of `origin/master` at `3f9b68adb`.
- Mandatory standalone review of `3f9b68adb..50f8223c` found no Blocking,
  Important, or code/commit/compatibility Advisory findings. The reviewer
  confirmed the change preserves the array contract and no-publication path,
  and that the single commit is focused and rolling-deployment safe.
- The review's tracking-only advisory was resolved by updating stale status and
  pre-fix wording in this file. Its residual low-risk test gap is that the spec
  invokes internal methods on an allocated singleton instead of a real worker
  thread and RabbitMQ channel; direct coverage of the changed branch and sole
  publication boundary was considered sufficient, with the full component
  suite as the next check.
- Full libnodectld verification passed in the component Nix shell: 422
  examples, 0 failures, randomized with seed 5592.
- Refetched vpsAdmin `origin`; `origin/master` remained at `3f9b68adb`, so the
  clean feature branch at `50f8223c` requires no rebase.
- Target-branch verification in the fresh master worktree passed: 422
  examples, 0 failures, randomized with seed 20089.
- `origin/master` and `origin/2026-08-04-nodectld-crash` both point to
  `50f8223c`; the integration was a fast-forward with no merge commit.
- RuboCop and libnodectld Specs succeeded on both the feature branch and
  `master` for exact commit `50f8223c`. The two longer integration CI runs were
  still executing their test steps at cleanup time with all setup steps green.
- Exact-commit integration runs to follow:
  - feature branch: <https://github.com/vpsfreecz/vpsadmin/actions/runs/30983548379>
  - `master`: <https://github.com/vpsfreecz/vpsadmin/actions/runs/30983690308>
- A final fetch after cleanup confirmed that local and remote `master` and
  feature refs still point to `50f8223c`, with no initiative worktree left
  registered.

## Open questions

- None.

## Cleanup

- Removed the clean vpsAdmin feature and master integration worktrees. The
  feature branch is retained locally and remotely as required by workspace
  policy.
- Removed the investigation-only `vpsfree-cz-configuration` worktree with its
  untracked `.bin/` and `.bundle/` Nix-shell caches; its feature branch was
  retained.

## Archival request, 2026-10-06

The workspace operator requested archival of sessions dated August 2026 or
older, retaining recorded work and branches. This checkpoint commits the
existing plan and active state before the ordinary archive transition.
