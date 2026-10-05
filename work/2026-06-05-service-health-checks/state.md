---
lifecycle: active
---
# Service health checks state

## Status

Implementation is merged to the default branches and pushed in both affected
repositories. The feature branches are preserved locally and remotely, and the
initiative worktrees have been removed.

Netboot machine builds were attempted earlier but are blocked in this local
environment by a pre-existing missing ISO image path. Targeted live health
checks were attempted earlier, but local SSH host-key/connectivity failures
prevented validation against production machines.

## Repositories and worktrees

- Repository: `confctl`
  - Bare clone: `repos/confctl.git`
  - Remote: `git@github.com:vpsfreecz/confctl.git`
  - Default branch: `origin/master`
  - Feature branch: `2026-06-05-service-health-checks`
  - Worktree: removed after merge
  - Base commit:
    `af164b442100b92b8d93c0d67b315eff982e0180`
    (`skills: add NixOS release upgrade workflow`)
  - Commit:
    `7e8b7c9b1484f1f9ade3038656168e5e85eb50c4`
    (`Preserve remote command arguments`)
  - Merged to `master`:
    `7e8b7c9b1484f1f9ade3038656168e5e85eb50c4`
  - Pushed branch: `origin/2026-06-05-service-health-checks`
- Repository: `vpsfree-cz-configuration`
- Bare clone: `repos/vpsfree-cz-configuration.git`
- Remote: `git@github.com:vpsfreecz/vpsfree-cz-configuration.git`
- Default branch: `origin/master`
- Feature branch: `2026-06-05-service-health-checks`
- Worktree:
  removed after merge
- Base commit:
  `6f2934dac1bfb77693a55e6a5e545707c57ed120`
  (`cluster: add auto-update tag to em1`)
- Rebased onto:
  `58ad6547d06716bbf27adce51dd201cd3ba2f695`
  (`inputs: update nixpkgsProduction, nixpkgsStaging to 535f3e69`)
- Latest commit:
  `b413ab0938581f77856730ad702bd45d74dda844`
  (`monitor: check public HTTP response bodies`)
- Commits:
  `8a9771445bc6d04d0e1d9e5b040dbca8a2cd57b4`
  (`health-checks: check service endpoints`)
  `8acb0899e5b587d1c6efb41ab47a481f3e51bcbc`
  (`health-checks: resolve local vhost curls`)
  `d987f3f104a2668fed4c6db28089542c3c88dcc3`
  (`inputs: set confctl to 7e8b7c9b`)
  `051a098f43068191dffef7a765b7e8b077236b3f`
  (`health-checks: use fixed confctl argv handling`)
  `b413ab0938581f77856730ad702bd45d74dda844`
  (`monitor: check public HTTP response bodies`)
- Merged to `master`:
  `b413ab0938581f77856730ad702bd45d74dda844`
- Pushed branch:
  `origin/2026-06-05-service-health-checks`

## Commands run

- `git -C repos/vpsfree-cz-configuration.git remote -v`
  - Confirmed SSH remote.
- `git -C repos/vpsfree-cz-configuration.git symbolic-ref refs/remotes/origin/HEAD`
  - Confirmed `refs/remotes/origin/master`.
- `git fetch origin --prune`
  - Completed successfully.
- `git --git-dir=repos/vpsfree-cz-configuration.git rev-parse --short origin/master`
  - Returned `6f2934da`.
- `git --git-dir=repos/vpsfree-cz-configuration.git worktree add -b 2026-06-05-service-health-checks worktrees/2026-06-05-service-health-checks/vpsfree-cz-configuration origin/master`
  - Created the branch and worktree.
  - Command exited 78 because the repository checkout hook attempted to load
    Overcommit/Ruby gems that are only available in the dev shell. The worktree
    is present and clean; see the existing note
    `notes/vpsfree-cz-configuration/2026-06-04-overcommit-dev-shell.md`.
- `git status --short --branch`
  - Worktree is clean on `2026-06-05-service-health-checks...origin/master`.
- Read repository-local `AGENTS.md`.
- Inspected:
  - `health-checks/*.nix`
  - `health-checks/vpsadmin/*.nix`
  - `modules/cluster/default.nix`
  - `modules/clusterconf/monitor/default.nix`
  - `modules/clusterconf/monitor/http.nix`
  - `modules/clusterconf/monitor/rules/*.nix` relevant to HTTP/vpsAdmin
  - service modules under `cluster/cz.vpsfree/containers`,
    `cluster/cz.vpsfree/machines`, and `cluster/cz.vpsfree/vpsadmin`.
- `nix develop -c nixfmt ...`
  - Formatted all changed Nix files.
- `git diff --check`
  - Passed.
- `confctl build -y cz.vpsfree/containers/prg/int.mon1`
  - Built generation `2026-06-05--18-42-50`.
- `confctl build -y cz.vpsfree/containers/prg/int.mon2`
  - Built generation `2026-06-05--18-43-44`.
- `confctl build -y cz.vpsfree/containers/prg/int.alerts1`
  - Built generation `2026-06-05--18-44-41`.
- `confctl build -y cz.vpsfree/containers/prg/int.alerts2`
  - Built generation `2026-06-05--18-45-34`.
- `confctl build -y cz.vpsfree/containers/int.web`
  - Built generation `2026-06-05--18-46-28`.
- `confctl build -y cz.vpsfree/containers/int.kb`
  - Built generation `2026-06-05--18-47-22`.
- `confctl build -y cz.vpsfree/containers/prg/proxy`
  - Built generation `2026-06-05--18-48-18`.
- `confctl build -y cz.vpsfree/containers/prg/int.grafana`
  - Built generation `2026-06-05--18-49-12`.
- `confctl build -y cz.vpsfree/containers/int.rubygems`
  - Built generation `2026-06-05--18-49-58`.
- `confctl build -y cz.vpsfree/containers/int.paste`
  - Built generation `2026-06-05--18-51-05`.
- `confctl build -y cz.vpsfree/containers/int.utils`
  - Built generation `2026-06-05--18-52-12`.
- `confctl build -y cz.vpsfree/machines/build`
  - Failed during evaluation because
    `/srv/iso-images/systemrescue-11.01-amd64.iso` does not exist locally.
  - Log:
    `worktrees/2026-06-05-service-health-checks/vpsfree-cz-configuration/.confctl/logs/2026-06-05--18-52-49-confctl-build.log`
- `confctl build -y cz.vpsfree/machines/prg/apu`
  - Failed with the same missing
    `/srv/iso-images/systemrescue-11.01-amd64.iso` path.
  - Log:
    `worktrees/2026-06-05-service-health-checks/vpsfree-cz-configuration/.confctl/logs/2026-06-05--18-54-54-confctl-build.log`
- `confctl build -y cz.vpsfree/machines/brq/apu`
  - Failed with the same missing
    `/srv/iso-images/systemrescue-11.01-amd64.iso` path.
  - Log:
    `worktrees/2026-06-05-service-health-checks/vpsfree-cz-configuration/.confctl/logs/2026-06-05--18-55-29-confctl-build.log`
- Removed untracked `.bin/` and `.bundle/` directories created by local
  dev-shell/hook setup so the worktree only shows intended tracked changes.
- `nix develop -c overcommit --run`
  - Passed Nixfmt and RuboCop pre-commit hooks.
- `nix develop -c git commit -F <tmpfile>`
  - Created commit `291d17c8`.
  - Amended once to wrap commit message text at the stricter hook width.
  - Final commit passed Nixfmt and all commit-msg hooks.
- `git push -u origin HEAD`
  - Failed outside the dev shell because the hook environment could not load
    Overcommit/Ruby gems.
- `nix develop -c git push -u origin HEAD`
  - Pushed branch `2026-06-05-service-health-checks` to origin and set
    upstream tracking.
- Removed untracked `.bin/`, `.bundle/`, and `.rubocop_cache/` directories
  created by local hook/dev-shell commands.
- Created `confctl` worktree:
  `worktrees/2026-06-05-service-health-checks/confctl`.
- In `confctl`, fixed `MachineControl` remote command execution to pass one
  shell-escaped remote command string to `ssh`, preserving literal argv
  boundaries for arguments containing spaces.
- In `confctl`, updated health-check selection to use runnable machines and
  skip carried/non-target machines such as `cz.vpsfree/machines/nixos-live`.
- In `confctl`, adjusted rollback-status shell redirection to use explicit
  `sh -c`.
- In `confctl`, added RSpec coverage for:
  - SSH argv preservation with spaces, quotes, empty strings, and shell
    metacharacters;
  - runnable-machine health-check filtering;
  - `confctl health-check` using only runnable machines.
- In `confctl`, extended `tests/suite/deploy/base.nix` to exercise:
  - a machine health-check command argument containing a space;
  - a `confctl ssh` command argument containing a space.
- `nix develop -c bundle exec rspec`
  - Passed: 35 examples, 0 failures.
- `nix develop -c bundle exec rubocop`
  - Passed: 120 files inspected, no offenses.
- `nix develop -c overcommit --run`
  - Passed Nixfmt and RuboCop pre-commit hooks.
- `./test-runner.sh test deploy/flakes`
  - Passed: 23 examples, test successful in 890.35 seconds.
- `nix develop -c git commit -F <tmpfile>`
  - Created `confctl` commit `7e8b7c9b`.
  - Amended commit message until commit-msg hooks passed without warnings.
- `nix develop -c git push -u origin HEAD`
  - Pushed `confctl` branch `2026-06-05-service-health-checks`.
- `nix develop -c confctl inputs set --commit --no-editor confctl 7e8b7c9b1484f1f9ade3038656168e5e85eb50c4`
  - Created generated config commit `6a787f0d`.
  - Updated `confctl` input `eb26c228 -> 7e8b7c9b`.
  - Commit-msg hook warned about a generated message line over 72 columns; the
    generated commit message was left unchanged as required.
- Restored explicit Host-header curl checks in `int.web`, `int.kb`, and
  `int.utils`, now backed by the fixed `confctl` argv handling.
- Changed `int.rubygems` content match from `Geminabox` to `Gem in a Box`.
- `nix develop -c nixfmt cluster/cz.vpsfree/containers/int.web/module.nix cluster/cz.vpsfree/containers/int.kb/module.nix cluster/cz.vpsfree/containers/int.utils/module.nix cluster/cz.vpsfree/containers/int.rubygems/module.nix`
  - Passed.
- `confctl build -y cz.vpsfree/containers/int.web`
  - Built generation `2026-06-05--18-45-57`.
- `confctl build -y cz.vpsfree/containers/int.kb`
  - Built generation `2026-06-05--18-46-59`.
- `confctl build -y cz.vpsfree/containers/int.utils`
  - Built generation `2026-06-05--18-52-12`.
- `confctl build -y cz.vpsfree/containers/int.rubygems`
  - Built generation `2026-06-05--18-49-58`.
- `confctl health-check --yes cz.vpsfree/containers/int.web`
  - Attempted with fixed `confctl`, but failed locally before service checks
    could run because SSH reported `Host key verification failed` and
    `Connection closed by 172.16.9.28 port 22`.
  - Log:
    `worktrees/2026-06-05-service-health-checks/vpsfree-cz-configuration/.confctl/logs/2026-06-05--22-05-33-confctl-health-check.log`
  - The log shows the fixed command shape, for example one shell-escaped
    remote command argument after `ssh -l root web.int.vpsfree.cz`.
- `git diff --check`
  - Passed after the final config changes.
- `nix develop -c overcommit --run`
  - Passed Nixfmt and RuboCop pre-commit hooks.
- `nix develop -c git commit -F <tmpfile>`
  - Created final config commit `dc5a3412`.
  - Amended once to wrap commit message text at the stricter hook width.
  - Final commit passed Nixfmt and all commit-msg hooks.
- `nix develop -c git push`
  - Pushed config branch `2026-06-05-service-health-checks` from
    `456e64da` to `dc5a3412`.
- Removed untracked `.bin/`, `.bundle/`, and `.rubocop_cache/` directories
  created by local hook/dev-shell commands.
- Reported runtime failure:
  - `curl --header Host:\ vpsfree.cz http://localhost/` returned HTTP 400.
  - The health-check runner logs show the Host header argument with an escaped
    space, which can be misinterpreted by the remote SSH command execution.
- Replaced explicit `--header "Host: ..."` arguments with `--resolve` and real
  vhost URLs in:
  - `cluster/cz.vpsfree/containers/int.web/module.nix`
  - `cluster/cz.vpsfree/containers/int.kb/module.nix`
  - `cluster/cz.vpsfree/containers/int.utils/module.nix`
- `rg -n -- "--header|Host:" cluster health-checks`
  - No remaining matches.
- `nix develop -c nixfmt cluster/cz.vpsfree/containers/int.web/module.nix cluster/cz.vpsfree/containers/int.kb/module.nix cluster/cz.vpsfree/containers/int.utils/module.nix`
  - Passed.
- `confctl build -y cz.vpsfree/containers/int.web`
  - Built generation `2026-06-05--18-45-57`.
- `confctl build -y cz.vpsfree/containers/int.kb`
  - Built generation `2026-06-05--18-46-59`.
- `confctl build -y cz.vpsfree/containers/int.utils`
  - Built generation `2026-06-05--18-52-12`.
- `git diff --check`
  - Passed.
- `nix develop -c overcommit --run`
  - Passed Nixfmt and RuboCop pre-commit hooks.
- `nix develop -c git commit -F <tmpfile>`
  - Created follow-up commit `456e64da`.
  - Amended once to wrap commit message text at the stricter hook width.
  - Final commit passed Nixfmt and all commit-msg hooks.
- `nix develop -c git push`
  - Pushed `291d17c8..456e64da` to
    `origin/2026-06-05-service-health-checks`.
- Removed untracked `.bin/`, `.bundle/`, and `.rubocop_cache/` directories
  created by local hook/dev-shell commands.
- Verified phase 2 public blackbox marker strings with
  `curl --fail --silent --show-error --location --max-time 15 --compressed`
  and `grep -E` for:
  - `https://vpsfree.cz/prihlaska/fyzicka-osoba/`
  - `https://vpsfree.org/registration/fyzicka-osoba/`
  - `https://api.vpsfree.cz/`
  - `https://console.vpsfree.cz/vzconsole.js`
  - `https://vpsadmin.vpsfree.cz/`
  - `https://status.vpsf.cz/`
  - `https://kb.vpsfree.cz/`
  - `https://kb.vpsfree.org/`
  - `https://rubygems.vpsfree.cz/`
  - `https://paste.vpsfree.cz/`
  - `https://discourse.vpsfree.cz/`
  - `https://munin.vpsfree.cz/`
  - `https://grafana.prg.vpsfree.cz/`
- The first marker-check command used `grep -q` in a pipe with `pipefail`,
  which stopped early after matching `vpsadmin.vpsfree.cz` and made `curl`
  report a harmless broken pipe. The remaining checks were rerun by buffering
  each response before grepping.
- Added optional `bodyMatches` to public HTTP probe definitions and rendered
  it as `fail_if_body_not_matches_regexp` in generated blackbox modules.
- Added public probes for KB CZ/EN, rubygems, paste, Discourse, Munin, and
  Grafana.
- Added warning-level public-service blackbox alerts and adjusted existing
  HTTP probe descriptions to mention unexpected HTTP responses.
- `nix develop -c nixfmt modules/clusterconf/monitor/http.nix modules/clusterconf/monitor/default.nix modules/clusterconf/monitor/rules/vpsfree-web.nix modules/clusterconf/monitor/rules/vpsadmin.nix`
  - First run failed because `rules/vpsfree-web.nix` used a bare list item
    `let`; moved the `let` to wrap the list.
  - Rerun passed.
- `nix develop -c confctl build -y cz.vpsfree/containers/prg/int.mon1`
  - Built generation `2026-06-05--22-23-40`.
  - Build included `blackbox.yml`, checked blackbox exporter config, and
    Prometheus rule checks.
- `nix develop -c confctl build -y cz.vpsfree/containers/prg/int.mon2`
  - Built generation `2026-06-05--22-24-54`.
- `nix-store --query --outputs /nix/store/12x04b90izc1wx5cmca2v3mrngdkbb5b-blackbox.yml.drv`
  - Returned `/nix/store/n3pl2rwixdiggwa2wav0kwxkzjkv6gy5-blackbox.yml`.
- `rg -n "fail_if_body_not_matches_regexp|kb_vpsfree_cz_http_2xx|grafana_prg_vpsfree_cz_http_2xx|api_vpsfree_cz_http_2xx" /nix/store/n3pl2rwixdiggwa2wav0kwxkzjkv6gy5-blackbox.yml`
  - Confirmed generated blackbox modules contain the expected body-match
    regexes.
- `git diff --check`
  - Passed for the phase 2 diff.
- `nix develop -c overcommit --run`
  - Passed Nixfmt and RuboCop pre-commit hooks for the phase 2 diff.
- `nix develop -c git commit -F <tmpfile>`
  - First attempt passed pre-commit hooks but failed because the files had not
    been staged.
  - Staged the four monitor files and reran the commit.
  - Commit-msg hooks initially warned about lines over 72 columns; amended the
    message until all commit-msg hooks passed without warnings.
  - Final commit:
    `e5d904bde1e08892fd987cb27a8abd20f374d4ce`
    (`monitor: check public HTTP response bodies`).
- `nix develop -c git push`
  - Pushed `dc5a3412..e5d904bd` to
    `origin/2026-06-05-service-health-checks`.
- Removed untracked `.bin/`, `.bundle/`, and `.rubocop_cache/` directories
  created by local hook/dev-shell commands.
- `git fetch origin --prune`
  - Refreshed both repositories before merging.
  - `confctl` was already a fast-forward from `origin/master`.
  - `vpsfree-cz-configuration` required a rebase because `origin/master`
    advanced to `58ad6547`.
- `nix develop -c git rebase origin/master`
  - Rebased `vpsfree-cz-configuration` feature branch successfully.
  - Rewrote the config feature commits to:
    `8a977144`, `8acb0899`, `d987f3f1`, `051a098f`, `b413ab09`.
- Created detached merge worktrees from current `origin/master`:
  - `worktrees/2026-06-05-service-health-checks/confctl-merge-master`
  - `worktrees/2026-06-05-service-health-checks/vpsfree-cz-configuration-merge-master`
- `git merge --ff-only 2026-06-05-service-health-checks`
  - Fast-forwarded `confctl` merge worktree to `7e8b7c9b`.
  - Fast-forwarded `vpsfree-cz-configuration` merge worktree to `b413ab09`.
- In the `confctl` merge worktree:
  - `nix develop -c bundle exec rspec` passed: 35 examples, 0 failures.
  - `nix develop -c bundle exec rubocop` passed: 120 files inspected, no
    offenses.
  - `nix develop -c overcommit --run` passed Nixfmt and RuboCop hooks.
- In the `vpsfree-cz-configuration` merge worktree:
  - `git diff --check origin/master..HEAD` passed.
  - `nix develop -c overcommit --run` passed Nixfmt and RuboCop hooks.
  - `nix develop -c confctl build -y cz.vpsfree/containers/prg/int.mon1`
    built generation `2026-06-06--18-27-47`.
  - `nix develop -c confctl build -y cz.vpsfree/containers/prg/int.mon2`
    built generation `2026-06-06--18-28-56`.
  - `nix develop -c confctl build -y cz.vpsfree/containers/prg/int.alerts1`
    built generation `2026-06-06--18-29-41`.
  - `nix develop -c confctl build -y cz.vpsfree/containers/prg/int.alerts2`
    built generation `2026-06-06--18-30-21`.
  - `nix develop -c confctl build -y cz.vpsfree/containers/int.web`
    built generation `2026-06-06--18-31-04`.
  - `nix develop -c confctl build -y cz.vpsfree/containers/int.kb`
    built generation `2026-06-06--18-31-54`.
  - `nix develop -c confctl build -y cz.vpsfree/containers/int.utils`
    built generation `2026-06-06--18-32-37`.
  - `nix develop -c confctl build -y cz.vpsfree/containers/int.rubygems`
    built generation `2026-06-06--18-33-16`.
  - `nix develop -c confctl build -y cz.vpsfree/containers/int.paste`
    built generation `2026-06-06--18-33-59`.
  - `nix develop -c confctl build -y cz.vpsfree/containers/prg/proxy`
    built generation `2026-06-06--18-34-46`.
  - `nix develop -c confctl build -y cz.vpsfree/containers/prg/int.grafana`
    built generation `2026-06-06--18-35-29`.
- `/srv/iso-images/systemrescue-11.01-amd64.iso`
  - Still missing locally; netboot machine builds remain locally blocked.
- `nix develop -c git push origin HEAD:master`
  - Pushed `confctl` master `af164b4..7e8b7c9`.
- `nix develop -c git push --force-with-lease origin 2026-06-05-service-health-checks:2026-06-05-service-health-checks`
  - Updated the rebased `vpsfree-cz-configuration` feature branch:
    `e5d904bd...b413ab09`.
- `nix develop -c git push origin HEAD:master`
  - Pushed `vpsfree-cz-configuration` master `58ad6547..b413ab09`.
- GitHub Actions after pushing `confctl` master:
  - `RSpec` passed.
  - `RuboCop` passed.
  - `Tests` failed before checkout because the runner working directory
    `/run/github-runner/runner/confctl/confctl` did not exist.
  - Rerunning `Tests` produced the same pre-checkout runner error and no
    `test.log`, so this is recorded as a CI runner issue, not a test failure.
- Removed initiative worktrees:
  - `worktrees/2026-06-05-service-health-checks/confctl`
  - `worktrees/2026-06-05-service-health-checks/confctl-merge-master`
  - `worktrees/2026-06-05-service-health-checks/vpsfree-cz-configuration`
  - `worktrees/2026-06-05-service-health-checks/vpsfree-cz-configuration-merge-master`
- Updated bare local `master` refs to match `origin/master`.

## Findings

- Existing machine health checks already support:
  - `systemd.unitProperties`;
  - `machineCommands`;
  - `builderCommands`;
  - `standardOutput.match`;
  - `standardOutput.include`.
- Local HTTP content checks already exist for vpsAdmin API, vpsAdmin web UI,
  RabbitMQ diagnostics, DNS command checks, and Munin.
- Gaps found during configuration walk-through:
  - monitoring/alerting services mostly check only unit activity;
  - `int.web`, `int.kb`, `int.utils`, and `prg/int.grafana` have no machine
    health checks;
  - `prg/proxy` checks only `nginx.service`;
  - netboot machines do not assert `nginx.service`;
  - public Prometheus blackbox probes check status code but not body content.

## Implemented changes

- Added HTTP command checks to reusable Prometheus and Alertmanager health
  checks.
- Added local HTTP content checks and relevant unit checks for `int.web`,
  `int.kb`, `int.utils`, `prg/int.grafana`, `int.rubygems`, and `int.paste`.
- Extended `prg/proxy` with HTTPS checks through local nginx for `vpsfree.cz`
  and `kb.vpsfree.cz`.
- Added `nginx.service` unit checks to the netboot hosts `build`, `prg/apu`,
  and `brq/apu`.
- Fixed `confctl` remote command argv preservation and health-check filtering
  for non-runnable carried machines.
- Pinned the config branch to fixed `confctl` revision `7e8b7c9b`.
- Replaced local Host-header curl checks with `--resolve` vhost checks and
  corrected the rubygems content match to `Gem in a Box`.
- Added Prometheus blackbox body matching for existing public HTTP probes.
- Added public blackbox probes for KB CZ/EN, rubygems, paste, Discourse, Munin,
  and Grafana.
- Added warning-level alerts for the new public blackbox jobs.

## Tests

- Passed: `nix develop -c nixfmt ...`
- Passed: `git diff --check`
- Passed: `confctl build -y` for all changed service containers listed above.
- Passed after follow-up fix: `confctl build -y` for `int.web`, `int.kb`, and
  `int.utils`.
- Passed in `confctl`: `bundle exec rspec`, `bundle exec rubocop`,
  `overcommit --run`, and `./test-runner.sh test deploy/flakes`.
- Passed after pinning fixed `confctl`: `confctl build -y` for `int.web`,
  `int.kb`, `int.utils`, and `int.rubygems`.
- Passed for phase 2: live marker checks for all public blackbox targets.
- Passed for phase 2:
  `nix develop -c confctl build -y cz.vpsfree/containers/prg/int.mon1`.
- Passed for phase 2:
  `nix develop -c confctl build -y cz.vpsfree/containers/prg/int.mon2`.
- Passed for phase 2: generated blackbox config inspection found
  `fail_if_body_not_matches_regexp` in the expected modules.
- Passed for phase 2: `git diff --check`.
- Passed for phase 2: `nix develop -c overcommit --run`.
- Passed after merge from fresh merge worktrees:
  - `confctl`: RSpec, RuboCop, and Overcommit.
  - `vpsfree-cz-configuration`: `git diff --check origin/master..HEAD`,
    Overcommit, and all focused service-container builds listed above.
- GitHub Actions after merge:
  - `confctl` RSpec and RuboCop passed.
  - `confctl` Tests failed twice before checkout due to a missing runner
    working directory, so no test command ran and no `test.log` was created.
- Blocked locally: live `confctl health-check --yes` for `int.web`, because SSH
  host-key verification/connection failed before any service command could run.
- Blocked locally: `confctl build -y` for netboot machines `build`, `prg/apu`,
  and `brq/apu`, because `/srv/iso-images/systemrescue-11.01-amd64.iso` is not
  present in this environment.

## Next step

Runtime validation remains: rerun targeted `confctl health-check --yes`
commands from an environment with accepted SSH host keys/access. To fully
validate the netboot machine edits, rerun their `confctl build -y` commands in
an environment where `/srv/iso-images/systemrescue-11.01-amd64.iso` exists.
