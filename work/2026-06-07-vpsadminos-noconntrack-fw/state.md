---
lifecycle: active
---
# 2026-06-07-vpsadminos-noconntrack-fw

## Repositories

- `vpsfree-cz-configuration`
  - Branch: `2026-06-07-vpsadminos-noconntrack-fw`
  - Worktree:
    `worktrees/2026-06-07-vpsadminos-noconntrack-fw/vpsfree-cz-configuration`
- `vpsadminos`
  - Branch: `2026-06-07-vpsadminos-noconntrack-fw`
  - Worktree:
    `worktrees/2026-06-07-vpsadminos-noconntrack-fw/vpsadminos`

## Status

Focused vpsAdminOS fix committed, merged into vpsAdminOS `staging`, and pushed.

## Commands run

- `bin/dev-session current`
- `git fetch --prune origin` in `repos/vpsfree-cz-configuration.git`
- `git fetch --prune origin` in `repos/vpsadminos.git`
- `git worktree add -b 2026-06-07-vpsadminos-noconntrack-fw ...`
- `nix develop --command nixfmt ...` in the vpsAdminOS worktree
- `./test-runner.sh test 'system/switch-to-configuration'` in the vpsAdminOS
  worktree
- `git diff --check` in the vpsAdminOS worktree
- `./test-runner.sh test 'firewall/conntrack#no-conntrack'` in the vpsAdminOS
  worktree
- `./test-runner.sh test 'system/switch-to-configuration'` rerun twice after
  the logging/failure-handling changes
- `./test-runner.sh test 'system/switch-to-configuration'` rerun after adding
  the `/dev/log` readiness wait
- `nix develop --command overcommit --run` in the vpsAdminOS feature worktree
- `nix develop --command git commit -F <tmpfile>` in the vpsAdminOS feature
  worktree
- `nix develop --command git rebase origin/staging` in the vpsAdminOS feature
  worktree
- `git worktree add --detach ... origin/staging` for a detached vpsAdminOS
  merge worktree
- `nix develop --command git merge --ff-only
  2026-06-07-vpsadminos-noconntrack-fw` in the detached merge worktree
- `git diff --check origin/staging..HEAD` in the detached merge worktree
- `./test-runner.sh test 'system/switch-to-configuration'` in the detached
  merge worktree, stopped after the user said no rerun was needed
- `nix develop --command git push origin HEAD:staging` in the detached merge
  worktree
- `git branch -f staging origin/staging` in `repos/vpsadminos.git`
- `git worktree remove ...` for the vpsAdminOS feature worktree, detached
  merge worktree, and unused `vpsfree-cz-configuration` worktree

## Results

- Active initiative is `2026-06-07-vpsadminos-noconntrack-fw`.
- Worktree creation succeeded for both repositories, but checkout hooks failed
  in the ambient shell because Overcommit gems are not installed. Use the
  repository Nix shell before committing or running hooks.
- The failing deployed command is the no-conntrack raw-table insertion using
  `-j CT --notrack`. A freshly booted `firewall/conntrack#no-conntrack` VM test
  passes, so the problem is specific to live switch/reload with required
  modules not yet loaded.
- Added a generic vpsAdminOS `kernel-modules` runit service that loads
  `boot.kernelModules`, reloads the list on configuration changes, and
  best-effort unloads removed modules.
- The `kernel-modules` service logs actions to stdout for svlogd and also to
  syslog using the `kernel-modules` tag. It starts/waits briefly for `rsyslog`
  and `/dev/log` before the initial load, but syslog failure does not block
  module loading.
- Failed module loads are logged and no longer abort the service. This keeps
  dependent services from being blocked by stale module names, dependency
  ordering issues, or disabled module loading.
- `firewall-iptables.nix` now contributes its required netfilter modules to
  `boot.kernelModules`; no firewall-local `modprobe` calls are used.
- The switch-to-configuration test now covers the kernel module service
  transition explicitly: a new module is loaded, a removed module is unloaded,
  a kept module remains loaded without being treated as removed, a missing
  module is logged as failed without stopping the service, and key action lines
  appear in both svlogd and syslog.
- `system/switch-to-configuration` passed on 2026-06-07.
- `firewall/conntrack#no-conntrack` passed on 2026-06-07, including the
  explicit `xt_CT` module assertion.
- `git diff --check` passed.
- The latest two `system/switch-to-configuration` reruns did not reach
  userspace. Both stopped at early QEMU/KVM `kvm run failed Bad address`
  console output and were terminated to avoid leaving stuck test processes.
- A later `system/switch-to-configuration` rerun got past boot. The first
  example passed, but the second exposed that `sv check rsyslog` could return
  before `/dev/log` existed, so initial syslog messages were lost.
- After adding the `/dev/log` readiness wait,
  `system/switch-to-configuration` passed on 2026-06-07 in 251.9 seconds.
- Overcommit pre-commit hooks passed before commit and during commit.
- Commit `3d65d98d7` (`os: manage configured kernel modules with runit`) was
  created after rebasing onto `origin/staging`.
- The detached merge worktree fast-forwarded from `origin/staging` to
  `3d65d98d7`.
- `origin/staging` was pushed to `3d65d98d7`.
- The extra merge-worktree `system/switch-to-configuration` rerun was started
  but intentionally stopped before completion after the user said it was not
  necessary.
- Local vpsAdminOS `staging` now tracks `origin/staging` at `3d65d98d7`.
- Initiative worktrees were removed. Feature branches were kept.

## Open questions

- None.

## Cleanup

- Completed. The durable plan/state notes remain under `work/`.

## Archival request, 2026-10-06

The workspace operator requested archival of sessions dated August 2026 or
older, retaining recorded work and branches. This checkpoint commits the
existing plan and active state before the ordinary archive transition.
