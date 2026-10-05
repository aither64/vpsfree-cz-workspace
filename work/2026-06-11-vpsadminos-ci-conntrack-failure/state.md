---
lifecycle: active
---
# 2026-06-11-vpsadminos-ci-conntrack-failure

## Repositories

- `vpsadminos`
  - Worktree: removed after merge
  - Branch: `2026-06-11-vpsadminos-ci-conntrack-failure`
  - Base: `origin/staging` at `11a751d028bce0a0a2e85ed2a51e06743585d1bf`

## Status

- Investigated failed CI run `27363633690`.
- Implemented a fix in `vpsadminos`:
  - custom runit `check` scripts now inherit service `path` and `environment`;
  - the iptables firewall service now has a readiness check for installed
    `INPUT -> nixos-fw` rules and absence of the temporary `nixos-drop` gate;
  - `system/boot/runit` covers service `path` and `environment` in `run`,
    `check`, `finish`, and `control` scripts using RSpec-style examples and
    expectations.
- Targeted tests and hooks passed.
- Commits:
  - `8da4eaed6 runit: pass service environment to checks`
  - `5c3876223 firewall: check installed iptables rules`
- Restored `origin/staging` to `11a751d028bce0a0a2e85ed2a51e06743585d1bf`
  after an accidental early push.
- Corrected branch CI run `27379904757`, attempt 2, passed.
- Merged to `staging` with a fast-forward and pushed. `origin/staging` now
  points to `5c387622316aa04058b9b333e1eafb241caa13f9`.
- Staging CI run `27386586427` started after the push.

## Commands run

- `bin/dev-session current`
- `gh run view 27363633690 --repo vpsfreecz/vpsadminos --json ...`
- `gh run view 27363633690 --repo vpsfreecz/vpsadminos --job 80867091383 --log-failed`
- `gh api repos/vpsfreecz/vpsadminos/actions/runs/27363633690/artifacts ...`
- `gh run download 27363633690 --repo vpsfreecz/vpsadminos --name os-test-logs-27363633690 --dir work/2026-06-11-vpsadminos-ci-conntrack-failure/artifacts`
- `git --git-dir=repos/vpsadminos.git fetch origin`
- `git --git-dir=repos/vpsadminos.git worktree add -b 2026-06-11-vpsadminos-ci-conntrack-failure worktrees/2026-06-11-vpsadminos-ci-conntrack-failure/vpsadminos origin/staging`
- `nixfmt ...` failed in the ambient shell because `nixfmt` was not installed.
- `nix develop --command nixfmt os/modules/system/boot/runit/default.nix os/modules/services/networking/firewall-iptables.nix tests/suite/driver/vpsadminos.nix`
- `./test-runner.sh test firewall/conntrack#conntrack`
- `./test-runner.sh test driver/vpsadminos` was stopped after the newly added
  assertion passed because the broad driver lifecycle later stopped making
  progress after `destroy_disks`; the regression coverage was moved to a
  focused boot test instead.
- `./test-runner.sh test system/boot/runit`
- `git diff --check`
- `nix develop --command overcommit --install`
- `nix develop --command overcommit --run`
- `nix develop --command git commit -F <tmpfile>` initially committed with
  72-column commit-message warnings.
- `nix develop --command git commit --amend -F <tmpfile>` rewrote only the
  commit message; all Overcommit hooks passed without warnings.
- `git reset --mixed HEAD~1` split the original combined commit.
- `./test-runner.sh test system/boot/runit`
- `nix develop --command git commit -F <tmpfile>` committed the runit change;
  the first message had one 72-column warning.
- `nix develop --command git commit --amend -F <tmpfile>` rewrapped the runit
  commit message; all hooks passed.
- `nix develop --command git commit -F <tmpfile>` committed the firewall
  readiness change; all hooks passed.
- `gh run cancel 27374519615 --repo vpsfreecz/vpsadminos`
- `nix develop --command git push --force-with-lease origin 2026-06-11-vpsadminos-ci-conntrack-failure`
- `gh run watch 27375198335 --repo vpsfreecz/vpsadminos --exit-status`
- `gh run view 27375198335 --repo vpsfreecz/vpsadminos --json status,conclusion,jobs ...`
- `git push --force-with-lease ... 11a751d028bce0a0a2e85ed2a51e06743585d1bf:staging`
- `gh run cancel 27379461629 --repo vpsfreecz/vpsadminos`
- Refactored `tests/suite/system/boot/runit.nix` to RSpec-style examples and
  expectations.
- `./test-runner.sh test system/boot/runit`
- `git reset --mixed origin/staging`
- `nix develop --command git commit -F <tmpfile>` for the corrected runit
  commit.
- `nix develop --command git commit -F <tmpfile>` for the firewall readiness
  commit.
- `nix develop --command git push --force-with-lease origin 2026-06-11-vpsadminos-ci-conntrack-failure`
- `gh run view 27379904757 --repo vpsfreecz/vpsadminos ...`
- `gh run download 27379904757 --repo vpsfreecz/vpsadminos --dir work/2026-06-11-vpsadminos-ci-conntrack-failure/artifacts/run-27379904757`
- `gh run rerun 27379904757 --repo vpsfreecz/vpsadminos --failed`
- `git worktree add -b 2026-06-11-vpsadminos-ci-conntrack-failure-merge-final ... origin/staging`
- `git merge --ff-only origin/2026-06-11-vpsadminos-ci-conntrack-failure`
- `nix develop --command overcommit --run`
- `nix develop --command git push origin HEAD:staging`
- `git worktree remove .../vpsadminos-staging-merge`
- `git worktree remove .../vpsadminos`
- `git branch -D 2026-06-11-vpsadminos-ci-conntrack-failure-merge 2026-06-11-vpsadminos-ci-conntrack-failure-merge-final`

## Results

- CI failed in job `Run test suite`, step `Run tests`.
- The failing script reported by the current-run log was
  `firewall/conntrack#conntrack`.
- Artifact evidence:
  - `os-test-firewall__conntrack-6b3aaf56/test-runner.log` shows example
    `firewall with conntrack drops unconfigured service ports` failed with
    output `open-tcp`.
  - `conntrack_server-shell1.log` shows `sv check firewall` returned success at
    `2026-06-11 20:18:08 +0200`, the client netns appeared at `20:18:10`, the
    unconfigured TCP port `8081` was reachable at `20:18:10`, and only then did
    `iptables-save` show the final `-A nixos-fw -j nixos-fw-log-refuse` rule at
    `20:18:11`.
- Root cause: `sv check firewall` reported the runit process as ready while the
  firewall run script was still waiting for dependencies and installing the
  ruleset. The test then raced ahead and connected to an unconfigured service
  port before default-deny rules were installed. While fixing this, we found the
  runit generator also did not propagate service `path`/`environment` into
  custom `check` scripts.
- `./test-runner.sh test firewall/conntrack#conntrack` passed on the fixed
  tree, including the previously failing negative-port example.
- `./test-runner.sh test system/boot/runit` passed after being expanded and
  refactored to RSpec-style examples. It probes `run`, `check`, `finish`, and
  `control.hangup`; all probes use a command found only through service `path`
  and validate an environment variable from service `environment`.
- Code audit of `os/modules/system/boot/runit/default.nix`: `run`, `finish`,
  and `control/*` already propagated service `path` and `environment`; `check`
  was the missing script type. `log/run` is a separate logger service and there
  are no repository uses of custom `service.log.run`.
- `git diff --check` passed.
- Overcommit pre-commit hooks (`Nixfmt`, `RuboCop`) passed.
- Commit-msg hooks passed after message rewrap.
- Remote branch `origin/2026-06-11-vpsadminos-ci-conntrack-failure` points to
  `5c387622316aa04058b9b333e1eafb241caa13f9`.
- Branch CI `27379904757` attempt 1 failed in unrelated
  `dist-config/systemd-rundir` cases. Artifact evidence showed the runner could
  not copy `/nix/store/...-dist-config-systemd-rundir-script.sh`; this was not
  in code touched by this initiative. `system/boot/runit` and
  `firewall/conntrack` both passed in that run.
- Branch CI `27379904757` attempt 2 passed.
- `origin/staging` was fast-forwarded from
  `11a751d028bce0a0a2e85ed2a51e06743585d1bf` to
  `5c387622316aa04058b9b333e1eafb241caa13f9`.

## Open questions

- None.

## Cleanup

- Removed worktrees:
  - `worktrees/2026-06-11-vpsadminos-ci-conntrack-failure/vpsadminos`
  - `worktrees/2026-06-11-vpsadminos-ci-conntrack-failure/vpsadminos-staging-merge`
- Removed transient local merge branches:
  - `2026-06-11-vpsadminos-ci-conntrack-failure-merge`
  - `2026-06-11-vpsadminos-ci-conntrack-failure-merge-final`
- Kept the feature branch refs as required by workspace policy.
