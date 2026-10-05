---
lifecycle: active
---
# 2026-06-08-test-runner-resources

## Repositories

- `vpsadminos`
  - Branch: `2026-06-08-test-runner-resources`
  - Worktree: `worktrees/2026-06-08-test-runner-resources/vpsadminos`
  - Base: `origin/staging` at `a791e6b37`
  - Remote: `git@github.com:vpsfreecz/vpsadminos.git`

## Status

- Worktree prepared for `vpsadminos`.
- Repository-local `AGENTS.md` read.
- Code inspection completed for current runtime resource behavior.
- Current conclusion before implementation: the runner sampled detected
  resources once at startup and did not notice CPU, memory, or `/dev/shm`
  capacity changes after startup.
- Implementation completed in the worktree.
- Dynamic scheduling now refreshes detected capacity before scheduler
  decisions.
- Explicit `--max-*` and `TEST_RUNNER_MAX_*` values are implemented as
  ceilings/fallbacks for refreshed detection.
- Packaged Ruby gem metadata was regenerated with build id
  `26.05.0.build20260608123012`.
- Validation passed: targeted specs, full test-runner specs with `TMPDIR=/tmp`,
  smoke `test-runner ls`, `git diff --check`, and Overcommit hooks.
- Functional changes committed as `ad4904231` and generated gem metadata
  committed as `afd058b71`.
- Branch pushed to `origin/2026-06-08-test-runner-resources`.
- GitHub RuboCop and RSpec workflows passed. The first CI integration run
  failed in `osctld/restart`; failed jobs were rerun and CI passed.
- Follow-up investigation downloaded the failed CI artifact to
  `/tmp/vpsadminos-failed-ci-27134382216` and inspected the failed
  `osctld/restart` logs.
- Added a vpsAdminOS test-runner extension that collects service, osctld,
  container, process, filesystem, and temporary test-job logs from machines
  when a test script has an unexpected result.
- The diagnostic extension collects complete known vpsAdminOS log files rather
  than tails, and avoids probing non-existent `/var/log/osctld/*`,
  `/var/log/messages/*`, or `/var/log/syslog` paths.
- Diagnostic extension committed as `6ab1cfd93`.
- Updated top-level `AGENTS.md` to require failed CI artifact/log
  investigation before accepting a rerun as validation.
- Implemented the osctld graceful-restart race fix in the same vpsAdminOS
  worktree.
- `ThreadReaper` now supports grouped drains, management and user-control
  clients are tagged separately, and `Daemon.stop` drains management clients
  before closing user-control servers.
- During verification, the first packaged VM run exposed a Ruby keyword
  forwarding bug in the new `ThreadReaper` class helpers:
  `ThreadReaper.add(..., group: :management)` was forwarded as a third
  positional argument, causing management client connections to crash the
  server thread under `Thread.abort_on_exception`.
- Fixed the class helper forwarding and added a regression spec for keyword
  forwarding.
- Packaged Ruby gem metadata was regenerated again with build id
  `26.05.0.build20260608180929`.
- Validation passed for the osctld fix: full osctld specs, `osctld/restart`
  integration test, `git diff --check`, and Overcommit hooks.
- Follow-up vpsAdminOS CI run `27165394635` failed in the test job after the
  GitHub runner received a shutdown signal. The run had no downloadable
  artifacts because the runner shutdown skipped the artifact upload steps.
- The failed job log showed resource totals growing with reservations and then
  fluctuating many times per second, e.g. memory capacity rose from the
  initial 95.6 GiB to more than 130 GiB while tests were reserved.
- Root cause identified in `ResourcePool::CapacitySource`: memory and
  `/dev/shm` capacity used fluctuating available values and added current
  reservations back into the detected total.
- Implemented a second test-runner resource scheduler correction:
  stable memory capacity now uses cgroup memory limits capped by `MemTotal` or
  falls back to `MemTotal`, `/dev/shm` capacity uses filesystem total blocks,
  and reservations no longer inflate capacity.
- Scheduler workers now read cached resource capacity only. A single executor
  monitor thread refreshes capacity every 15 seconds by default and broadcasts
  the scheduler when capacity changes.
- Added `--resource-refresh-interval` to tune the monitor interval.
- Validation passed for the scheduler correction so far: focused
  resource/executor/CLI specs, full test-runner specs with `TMPDIR=/tmp`, Ruby
  syntax checks, and `git diff --check`.
- Final scheduler correction commits were created:
  - `d7246fc4e` `test-runner: use stable resource capacity`
  - `efdbb7835` `os: update gems to 26.05.0.build20260609094620`
- The local vpsAdminOS branch is clean and intentionally diverges from the
  remote branch by replacing the previous generated-gem tip commit. Publishing
  requires `git push --force-with-lease`.

## 2026-06-09 follow-up status

- vpsAdminOS restart test uses `tests/suite/machines/vpsadminos/tank.nix` with
  named shells; no machine configuration overlay is needed.
- vpsAdminOS branch head is `1d37a2ea6` and all branch workflows completed
  successfully: RuboCop, RSpec, changed container images, and CI.
- vpsAdmin branch head is `82f4d5a9f`. The branch includes the nodectl gem
  rebuild against vpsAdminOS `1d37a2ea6`.
- vpsAdmin API specs, web UI PHPUnit, client specs, and libnodectld specs
  passed. vpsAdmin CI run `27211171072` is still being watched.
- Downstream branches were pushed for `confctl`, `vpsf-status`,
  `vpsfree-irc-bot`, and `terraform-provider-vpsadmin`.
- `terraform-provider-vpsadmin` integration run `27211415840` failed at
  `d5bf79f19`. The failed artifact was downloaded to
  `/tmp/terraform-provider-vpsadmin-failed-ci-27211415840`.
- The provider CI root cause was an API compatibility issue: current HaveAPI
  rejects pagination limits above 1000, while provider lookup helpers requested
  10000 rows for public keys, OS templates, DNS resolvers, and VPS lookup in
  mount discovery.
- Implemented provider commit `cd5399de4`
  `provider: keep API lookup page limits valid`, using a shared 1000-item API
  page limit and adding request-shape regression tests for the affected helper
  lookups.
- Provider validation passed:
  - `gofmt` and `git diff --check`
  - `nix develop --command make test`
  - `nix develop --command make test-get-token`
- Provider branch was pushed from `d5bf79f19` to `cd5399de4`.
- Pending workflow runs being watched:
  - vpsAdmin CI `27211171072`
  - confctl Tests `27211423410`
  - terraform-provider-vpsadmin Go Tests `27216757982`
  - terraform-provider-vpsadmin Integration Tests `27216757990`
  - vpsfree-irc-bot Integration Tests `27211422303`

## 2026-06-09 default-branch merge

- Stopped the feature-branch workflow watcher after the user accepted the
  queued/running CI state.
- Rebasing and final pins:
  - `vpsadminos` was rebased onto current `origin/staging`
    `b5f77df40`; final tip is `715b58e95`.
  - `vpsadmin` was rebased onto current `origin/master` `f68d64c13`.
    The old vpsAdminOS flake/gem tail was rebuilt to point at
    `vpsadminos` `715b58e95`; final tip is `c8fbfe38f`.
  - `confctl` flake tail was rebuilt to point at `vpsadminos`
    `715b58e95`; final tip is `617b222`.
  - `vpsf-status` flake tail was rebuilt to point at `vpsadmin`
    `c8fbfe38f`; final tip is `457b111`.
  - `vpsfree-irc-bot` flake tail was rebuilt to point at `vpsadmin`
    `c8fbfe38f`; final tip is `65b19c9`.
  - `terraform-provider-vpsadmin` flake tail was rebuilt to point at
    `vpsadmin` `c8fbfe38f`, then the provider page-limit fix was
    cherry-picked; final tip is `b9b0acb`.
- Generated vpsAdmin nodectl gems were rebuilt after the final vpsAdminOS pin:
  - OS build id: `26.05.0.build20260609152612`
  - vpsAdmin build id: `20260609193301`
- Validation after rebasing/rebuilding:
  - vpsAdminOS: focused test-runner specs, focused osctld specs,
    `git diff --check`, and Overcommit hooks passed.
  - vpsAdmin: vpsAdminOS lock verified at `715b58e95`, `git diff --check`,
    and Overcommit hooks passed. The hook run created unrelated PHP fixer
    edits, which were reversed from the worktree before pushing.
  - Downstream repos: lock revisions verified at final default tips and
    `git diff --check` passed.
  - `terraform-provider-vpsadmin`: `nix develop --command make test` and
    `nix develop --command make test-get-token` passed.
- Feature branches were force-updated while still unmerged, then default
  branches were fast-forwarded from fresh detached merge worktrees:
  - `vpsadminos/staging`: `715b58e95`
  - `vpsadmin/master`: `c8fbfe38f`
  - `confctl/master`: `617b222`
  - `vpsf-status/master`: `457b111`
  - `vpsfree-irc-bot/master`: `65b19c9`
  - `terraform-provider-vpsadmin/master`: `b9b0acb`
- Temporary merge worktrees under
  `worktrees/2026-06-08-test-runner-resources/_merge/` were removed.
- Recorded a durable note for the confctl temporary-worktree stale Ruby bundle
  hook failure at
  `notes/confctl/2026-06-09-temp-worktree-bundle-ruby.md`.
- Latest default-branch workflow status snapshot after pushes:
  - vpsAdminOS `715b58e95`: RuboCop and RSpec passed; CI and changed image
    workflow queued.
  - vpsAdmin `c8fbfe38f`: RuboCop, libnodectld specs, Webui PHPUnit,
    Client Specs, and API Specs passed; CI queued.
  - confctl `617b222`: RuboCop and RSpec passed; Tests queued.
  - vpsf-status `457b111`: Integration Tests queued.
  - vpsfree-irc-bot `65b19c9`: RSpec passed; Integration Tests queued.
  - terraform-provider-vpsadmin `b9b0acb`: Go Tests passed; Integration Tests
    queued.

## 2026-06-09 cleanup

- Confirmed all initiative repository worktrees were clean after default-branch
  pushes.
- Removed the initiative worktrees for `vpsadminos`, `vpsadmin`, `confctl`,
  `vpsf-status`, `vpsfree-irc-bot`, and `terraform-provider-vpsadmin`.
- Removed the empty initiative worktree group directory.
- Removed the transient `/tmp/vpsadmin-hook-format.patch` file.
- Preserved `work/2026-06-08-test-runner-resources/` and durable notes.

## Commands run

- `bin/dev-session current`
  - Result: active slug is `2026-06-08-test-runner-resources`.
- `ls -la work/2026-06-08-test-runner-resources`
  - Result: found placeholder `plan.md` and `state.md`.
- `find worktrees/2026-06-08-test-runner-resources -maxdepth 2 -type d -print`
  - Result: no repository worktree existed before setup.
- `git --git-dir=repos/vpsadminos.git branch --all --list
  '*2026-06-08-test-runner-resources*'`
  - Result: no existing branch for this slug.
- `git --git-dir=repos/vpsadminos.git remote -v`
  - Result: origin uses SSH for fetch and push.
- `git --git-dir=repos/vpsadminos.git symbolic-ref refs/remotes/origin/HEAD`
  - Result: default branch is `origin/staging`.
- `git --git-dir=repos/vpsadminos.git worktree list`
  - Result: no worktree for this slug before setup.
- `bin/dev-session worktree add 2026-06-08-test-runner-resources vpsadminos
  --as-is`
  - Result: fetched `origin/staging` and created branch/worktree, but exited
    non-zero because the checkout hook requires the `overcommit` gem in the
    ambient shell.
- `git -C worktrees/2026-06-08-test-runner-resources/vpsadminos status --short
  --branch`
  - Result: clean branch `2026-06-08-test-runner-resources...origin/staging`.
- `sed -n '1,240p'
  worktrees/2026-06-08-test-runner-resources/vpsadminos/AGENTS.md`
  - Result: read repository instructions, including Nix dev shell and
    Overcommit requirements.
- `rg -n
  "cpu|cpus|memory|mem|resource|Resources|parallel|jobs|schedule|scheduler|total"
  test-runner`
  - Result: identified `resource_pool.rb`, `executor.rb`, CLI flags, and
    resource scheduling specs.
- `sed -n '1,260p' test-runner/lib/test-runner/resource_pool.rb`
  - Result: confirmed resource detection is done in `from_options` and stored
    in instance variables.
- `sed -n '1,280p' test-runner/lib/test-runner/executor.rb`
  - Result: confirmed scheduler wakes while waiting but never refreshes
    resource capacity.
- `sed -n '1,360p' test-runner/spec/test_runner/executor_spec.rb`
  - Result: existing specs cover static scheduling and resource release.
- `sed -n '1,180p' test-runner/lib/test-runner/cli/app.rb`
  - Result: current CLI exposes fixed max and reserve options, with no refresh
    option.
- `nix develop .#test-runner --command bundle exec rspec
  test-runner/spec/test_runner/resource_pool_spec.rb
  test-runner/spec/test_runner/executor_spec.rb`
  - Result: failed before examples loaded because running from the repository
    root did not put `test-runner/spec` on Ruby's load path.
- `nix develop .#test-runner --command bash -lc 'cd test-runner && bundle exec
  rspec spec/test_runner/resource_pool_spec.rb
  spec/test_runner/executor_spec.rb'`
  - Result: initially failed because `libosctl/native.so` was not built in the
    fresh worktree.
- `nix develop .#test-runner --command bash -lc 'cd libosctl/ext/libosctl &&
  ruby extconf.rb && make && cp native.so ../../lib/libosctl/native.so'`
  - Result: built local `libosctl/native.so` test prerequisite.
- `nix develop .#test-runner --command bash -lc 'cd test-runner && bundle exec
  rspec spec/test_runner/resource_pool_spec.rb
  spec/test_runner/executor_spec.rb'`
  - Result: passed, 23 examples, 0 failures.
- `nix develop .#test-runner --command bash -lc 'cd test-runner && bundle exec
  rspec spec'`
  - Result: failed 3 CLI specs because `nix develop` set `TMPDIR` to a
    nix-shell temporary directory while the specs expect `/tmp`.
- `nix develop .#test-runner --command bash -lc 'cd test-runner && TMPDIR=/tmp
  bundle exec rspec spec'`
  - Result: passed, 134 examples, 0 failures.
- `nix develop --command overcommit --run`
  - Result: passed before gem regeneration.
- `nix develop --command make gems`
  - Result: passed; published regenerated internal gems and updated
    `.build_id` plus `os/packages/*/{Gemfile,Gemfile.lock,gemset.nix}`.
- `nix develop .#test-runner --command bash -lc 'cd test-runner && TMPDIR=/tmp
  bundle exec rspec spec'`
  - Result: passed after gem regeneration, 134 examples, 0 failures.
- `nix develop --command overcommit --run`
  - Result: passed after gem regeneration.
- `git diff --check`
  - Result: passed.
- `nix develop .#test-runner --command bundle exec
  ./test-runner/bin/test-runner ls 'suite/*'`
  - Result: exited 0; no entries printed for the selected pattern.
- `nix develop --command git commit -F <tmpfile>`
  - Result: created functional commit `ad4904231`
    (`test-runner: refresh resource limits while scheduling`); hooks passed.
- `nix develop --command git commit -F <tmpfile>`
  - Result: created generated gem metadata commit `afd058b71`
    (`os: update gems to 26.05.0.build20260608123012`); hooks passed.
- `git push`
  - Result: failed because the ambient shell did not have the `overcommit` gem
    required by the repository pre-push hook.
- `nix develop --command git push -u origin
  2026-06-08-test-runner-resources`
  - Result: pushed the branch and set upstream tracking.
- `nix shell nixpkgs#gh -c gh run list --repo vpsfreecz/vpsadminos --branch
  2026-06-08-test-runner-resources --limit 10`
  - Result: RuboCop and RSpec were successful; CI was initially in progress.
- `nix shell nixpkgs#gh -c gh run view 27134382216 --repo
  vpsfreecz/vpsadminos --json status,conclusion,jobs,updatedAt`
  - Result: watched the CI run status.
- `nix shell nixpkgs#gh -c gh run download 27134382216 --repo
  vpsfreecz/vpsadminos --name os-test-logs-27134382216 --dir <tmpdir>`
  - Result: downloaded logs for the initial failed CI run.
- `nix shell nixpkgs#gh -c gh run rerun 27134382216 --repo
  vpsfreecz/vpsadminos --failed`
  - Result: restarted the failed CI job.
- `nix shell nixpkgs#gh -c gh run watch 27134382216 --repo
  vpsfreecz/vpsadminos --interval 30 --exit-status`
  - Result: rerun completed successfully.
- `nix shell nixpkgs#gh -c gh run list --repo vpsfreecz/vpsadminos --workflow
  CI --limit 10`
  - Result: checked recent CI durations while the rerun was still active;
    recent runs ranged from about 48 minutes to 1 hour 23 minutes.
- `nix shell nixpkgs#gh -c gh run list --repo vpsfreecz/vpsadminos --branch
  2026-06-08-test-runner-resources --limit 5`
  - Result: final branch workflow status is green for RuboCop, RSpec, and CI.
- `git -C worktrees/2026-06-08-test-runner-resources/vpsadminos status
  --short --branch`
  - Result: branch is clean and up to date with
    `origin/2026-06-08-test-runner-resources`.
- `nix shell nixpkgs#gh -c gh run download 27134382216 --repo
  vpsfreecz/vpsadminos --name os-test-logs-27134382216 --dir
  /tmp/vpsadminos-failed-ci-27134382216`
  - Result: downloaded the full failed CI artifact.
- `find /tmp/vpsadminos-failed-ci-27134382216 -name test-result.txt ...`
  - Result: confirmed the only unexpected failure was
    `os-test-osctld__restart-b891f158`.
- `sed -n '700,900p'
  /tmp/vpsadminos-failed-ci-27134382216/os-test-osctld__restart-b891f158/machine-shell.log`
  - Result: inspected the failure timing and `ct-start` job output.
- `sed -n '1,80p'
  /tmp/vpsadminos-failed-ci-27134382216/os-test-osctld__restart-b891f158/test-runner.log`
  - Result: inspected the failed example summary.
- `nix develop .#test-runner --command ruby -c
  tests/runner/extensions/vpsadminos_logs.rb`
  - Result: syntax check passed.
- `nix develop .#test-runner --command bundle exec
  ./test-runner/bin/test-runner ls 'osctld/restart'`
  - Result: extension loaded and the test was listed.
- `nix develop .#test-runner --command bundle exec
  ./test-runner/bin/test-runner test --stop-on-failure 'osctld/restart'`
  - Result: started a targeted local integration run, then terminated it before
    completion because the diagnostic extension needed correction.
- `kill <test-runner-pids>`
  - Result: stopped the targeted local integration run.
- `nix develop .#test-runner --command ruby -c
  tests/runner/extensions/vpsadminos_logs.rb`
  - Result: syntax check passed after correcting the diagnostic extension.
- `nix develop .#test-runner --command bundle exec
  ./test-runner/bin/test-runner ls 'osctld/restart'`
  - Result: corrected extension loaded and the test was listed.
- `nix develop --command overcommit --run`
  - Result: passed for the staged diagnostic extension.
- `nix develop --command git commit -F <tmpfile>`
  - Result: created commit `6ab1cfd93`
    (`tests: collect vpsAdminOS failure diagnostics`); hooks passed.
- `git show -s --format=%B HEAD | awk '{ print length, $0 }'`
  - Result: commit message lines are within the workspace 80-column limit.
- `git status --short --branch`
  - Result: vpsAdminOS branch is clean and ahead of origin by one commit.
- `nix develop .#vpsadminos --command bash -lc 'export
  BUNDLE_GEMFILE=$PWD/osctld/Gemfile BUNDLE_PATH=$PWD/.gems
  GEM_PATH=$PWD/.gems:$GEM_PATH; cd osctld; bundle exec rspec
  spec/osctld/thread_reaper_spec.rb spec/osctld/generic/server_spec.rb
  spec/osctld/daemon_spec.rb spec/osctld/user_control/supervisor_spec.rb'`
  - Result: passed, 23 examples, 0 failures, before the keyword-forwarding
    regression spec was added.
- `nix develop --command make gems`
  - Result: regenerated packaged gems with build id
    `26.05.0.build20260608175028`.
- `./test-runner.sh test osctld/restart`
  - Result: aborted after more than 600 seconds because osctld was
    crash-looping during initial readiness.
  - Root cause: the `ThreadReaper` class-level forwarding methods did not
    forward Ruby keyword arguments. `Generic::Server` called
    `ThreadReaper.add(thread, handler, group: :management)`, but the class
    helper passed the keyword hash as a third positional argument to
    `ThreadReaper#add`, raising `ArgumentError`. With
    `Thread.abort_on_exception = true`, this killed osctld whenever a
    management client connected.
- `nix develop .#vpsadminos --command ruby -Ilibosctl/lib -Iosctld/lib -e
  '<real Generic::Server/ThreadReaper socket exercise>'`
  - Result: reproduced the `ThreadReaper.add` keyword forwarding crash before
    the fix; after the fix, that crash was gone and only the artificial local
    logger setup failed.
- `nix develop .#vpsadminos --command bash -lc 'export
  BUNDLE_GEMFILE=$PWD/osctld/Gemfile BUNDLE_PATH=$PWD/.gems
  GEM_PATH=$PWD/.gems:$GEM_PATH; cd osctld; bundle exec rspec
  spec/osctld/thread_reaper_spec.rb spec/osctld/generic/server_spec.rb
  spec/osctld/daemon_spec.rb spec/osctld/user_control/supervisor_spec.rb'`
  - Result: passed after the keyword-forwarding fix, 24 examples, 0 failures.
- `nix develop --command make gems`
  - Result: regenerated packaged gems with final build id
    `26.05.0.build20260608180929`.
- `./test-runner.sh test osctld/restart`
  - Result: passed; 6/6 examples succeeded, including
    `active container start continues through a concurrent osctld restart`;
    total runtime 316.65 seconds.
- `nix develop .#vpsadminos --command bash -lc 'export
  BUNDLE_GEMFILE=$PWD/osctld/Gemfile BUNDLE_PATH=$PWD/.gems
  GEM_PATH=$PWD/.gems:$GEM_PATH; cd osctld; bundle exec rspec'`
  - Result: passed, 992 examples, 0 failures.
- `git diff --check`
  - Result: passed.
- `nix develop --command overcommit --run`
  - Result: passed; Nixfmt and RuboCop hooks passed.
- `gh run list --repo vpsfreecz/vpsadminos --branch
  2026-06-08-test-runner-resources --limit 20`
  - Result: latest vpsAdminOS CI run `27165394635` failed; RuboCop, RSpec, and
    image workflows passed.
- `gh run view 27165394635 --repo vpsfreecz/vpsadminos --json
  status,conclusion,jobs,headSha`
  - Result: test job `80206655018` failed on the `Run tests` step at head
    `398342ea945dcb7b01499c46e1d88efcdf9589de`.
- `gh api repos/vpsfreecz/vpsadminos/actions/runs/27165394635/artifacts`
  - Result: `total_count` was 0.
- `gh run download 27165394635 --repo vpsfreecz/vpsadminos`
  - Result: no artifacts were available to download.
- `gh run view 27165394635 --repo vpsfreecz/vpsadminos --log > /tmp/...`
  - Result: saved the job log locally for inspection.
- `nix develop .#test-runner --command bash -lc 'cd test-runner &&
  TMPDIR=/tmp bundle exec rspec spec/test_runner/resource_pool_spec.rb
  spec/test_runner/executor_spec.rb spec/test_runner/cli/command_spec.rb'`
  - Result: passed after fixing the monitor stop race and test setup, 42
    examples, 0 failures.
- `nix develop .#test-runner --command bash -lc 'cd test-runner &&
  TMPDIR=/tmp bundle exec rspec spec'`
  - Result: passed, 144 examples, 0 failures.
- `ruby -c test-runner/lib/test-runner/resource_pool.rb`
  - Result: syntax OK.
- `ruby -c test-runner/lib/test-runner/executor.rb`
  - Result: syntax OK.
- `git diff --check`
  - Result: passed for the scheduler correction.
- `nix develop --command overcommit --run`
  - Result: initially failed on RuboCop `Style/MultipleComparison` in the
    cgroup memory-limit parser.
- `nix develop .#test-runner --command bash -lc 'cd test-runner &&
  TMPDIR=/tmp bundle exec rspec spec/test_runner/resource_pool_spec.rb'`
  - Result: passed after the RuboCop fix, 13 examples, 0 failures.
- `nix develop --command overcommit --run`
  - Result: passed after the RuboCop fix.
- `nix develop --command make gems`
  - Result: regenerated packaged gems with build id
    `26.05.0.build20260609094620`.
- `nix develop .#test-runner --command bash -lc 'cd test-runner &&
  TMPDIR=/tmp bundle exec rspec spec'`
  - Result: passed after gem regeneration, 144 examples, 0 failures.
- `git diff --check`
  - Result: passed after gem regeneration.
- `nix develop --command overcommit --run`
  - Result: passed on the final functional plus generated diff.
- `git reset --mixed HEAD^`
  - Result: removed the previous generated-gem tip from local history while
    preserving the working tree, so the new gem update can replace it.
- `nix develop --command git commit -F <tmpfile>`
  - Result: created functional scheduler commit `d7246fc4e`; hooks passed.
- `nix develop --command git commit -F <tmpfile>`
  - Result: created generated gem metadata commit `efdbb7835`; hooks passed.

## Results

- Initial static behavior source:
  - `ResourcePool.from_options` reads `TEST_RUNNER_MAX_*` or CLI max values, or
    falls back to one-time detection using `/proc/meminfo`, `df -Pk /dev/shm`,
    and `nproc`.
  - `ResourcePool#can_reserve?` compares pending test resources against stored
    capacity and current usage.
  - `Executor#reserve_next_test` waits with `scheduler_cv.wait(..., 5)`, but
    no method updates `resource_pool` capacity during the run.
- Therefore, if an administrator adds/removes CPUs or memory after the runner
  starts, the current runner will not adjust scheduling to the new values.
- Implemented behavior:
  - `ResourcePool` now has refreshable capacity sources and an injectable host
    detector.
  - `Executor#reserve_next_test` refreshes capacity before each scheduler
    decision under the scheduler mutex.
  - CPU capacity refreshes from detected CPU availability.
  - Memory and `/dev/shm` refreshes add back this runner's already-reserved
    memory/shm before scheduling, avoiding double-counting running jobs.
  - Explicit max values are ceilings when detection succeeds and fallbacks when
    detection fails.
  - Running tests are not interrupted when capacity decreases; new reservations
    wait until they fit.
  - Resource limit updates are logged only when the formatted pool status
    changes after a refresh.
- Generated gem metadata now points packaged tools at
  `26.05.0.build20260608123012`.
- Osctld graceful-restart behavior:
  - The old daemon shutdown used one global `ThreadReaper.stop` phase.
    New user-control clients accepted while that stop phase was active were
    immediately asked to stop, even when they were callbacks required by
    already-running management commands.
  - The fix adds `ThreadReaper.drain(group:)` and assigns management clients to
    `:management` and user-control clients to `:user_control`.
  - `Daemon.stop` closes and joins the public management accept loop, drains
    management clients while user-control remains available, then closes
    user-control servers and stops all remaining tracked clients.
  - Existing running commands are allowed to finish; new public management
    clients are rejected once the management socket is closed.
  - The restart regression `osctld/restart` now passes the previously failing
    active `ct start` example.
- Generated gem metadata now points packaged tools at
  `26.05.0.build20260608180929`.
- Commits:
  - `ad4904231` `test-runner: refresh resource limits while scheduling`
  - `11c9d5f1b` `tests: collect vpsAdminOS failure diagnostics`
  - `d8f03efee` `osctld: drain management clients before user-control`
  - `d38fbd2ce` `os: update gems to 26.05.0.build20260608180929`
- Scheduler correction after failed vpsAdminOS CI run `27165394635`:
  - `d7246fc4e` `test-runner: use stable resource capacity`
  - `efdbb7835` `os: update gems to 26.05.0.build20260609094620`
- Push:
  - `origin/2026-06-08-test-runner-resources` was force-updated with
    `--force-with-lease` to remove the old generated-gem commit and now points
    at `d38fbd2ce`.
  - PR creation URL:
    `https://github.com/vpsfreecz/vpsadminos/pull/new/2026-06-08-test-runner-resources`
- GitHub workflows:
  - Force-push cleanup runs:
    - RuboCop run `27152513699`: success.
    - RSpec run `27152513712`: success.
    - CI run `27152513860`: in progress.
  - RuboCop run `27134382277`: success.
  - RSpec run `27134382223`: success.
  - CI run `27134382216`: initial run failed in `osctld/restart`.
  - Initial CI failure summary: `72 tests successful`, `1 tests should have
    succeeded, but failed`; failed script was `osctld/restart`.
  - Failed example:
    `active container start continues through a concurrent osctld restart`.
  - The failure was in container startup during an osctld restart and did not
    point at the scheduler/resource-pool changes.
  - Artifact evidence:
    - `ct-start` started at 13:46:20, its blocking `pre-start` hook was
      reached at 13:46:22, `sv restart osctld` removed
      `/run/osctl/osctld.sock` by 13:46:23, the hook was released at
      13:46:23, and `ct-start` exited 1 by 13:46:25.
    - The captured `ct-start` output was only
      `error: container failed to start`, followed by progress messages
      `Starting container`, `Connecting console`, and
      `Waiting for the container to start`.
    - The failed artifact did not contain `/var/log/osctld` or the container
      LXC log under `/tank/log/ct`, so the exact lower-level error from
      `osctld-ct-start`/LXC cannot be proven from that artifact alone.
  - Source-level root-cause analysis:
    - `osctl ct start` runs as an active management client in old osctld.
    - During `Daemon.stop`, `ThreadReaper.stop` enters stop mode while old
      active management clients are still being drained.
    - `ct start` then spawns `osctld-ct-start`, which opens a new user-control
      client to `/run/osctl/user-control/<ugid>.sock`.
    - `ThreadReaper` immediately requests stop for new client threads added
      after stop mode begins. If that races ahead of the user-control callback,
      the wrapper callback can fail and `ct start` reports the generic
      container-start failure.
    - This race is independent of the test-runner resource scheduler changes.
  - Diagnostic improvement:
    - `tests/runner/extensions/vpsadminos_logs.rb` now collects per-machine
      `*-failure-diagnostics.log` files on unexpected script results.
    - It collects complete `/var/log/osctld`, `/var/log/messages`,
      `/tank/log/ct/*`, runit status, process state, `dmesg`, and relevant
      temporary test files.
    - It intentionally does not probe non-existent `/var/log/osctld/*`,
      `/var/log/messages/*`, or `/var/log/syslog` paths.
  - Failed CI jobs were rerun; the rerun passed.
  - Final CI job duration after rerun: `Run test suite` passed in 1h19m40s;
    `Build OS and populate binary cache` passed in 1m36s.

## Open questions

- None for the implemented changes.

## Cleanup

- Worktree should remain until the implementation is either merged or abandoned.
- Local test/build artifacts were created in ignored paths by Bundler, native
  extension compilation, RSpec, and gem packaging.
- Functional changes and generated gem metadata were committed separately per
  repository guidance.
- vpsAdminOS worktree is clean on branch
  `2026-06-08-test-runner-resources`; it matches origin after the force-push
  cleanup.
- Top-level `AGENTS.md` has an uncommitted CI-failure-investigation rule.

## Current follow-up: nodectld pause during osctld stop

- Added vpsAdmin worktree
  `worktrees/2026-06-08-test-runner-resources/vpsadmin` on branch
  `2026-06-08-test-runner-resources` from `origin/master`.
- vpsAdmin worktree creation completed but the ambient checkout hook exited
  non-zero because Overcommit was not available outside the Nix shell.
- Repository-local `vpsadmin/AGENTS.md` was read.
- Implemented uncommitted vpsAdminOS changes:
  - `RunState` creates `/run/osctl/hooks` and `/run/osctl/hooks/daemon`.
  - `Daemon.stop` runs blocking daemon `pre_stop` hooks before management
    socket shutdown/drain and logs hook failures without aborting shutdown.
  - `event_subscribe` emits a synthetic `osctld_shutdown` event immediately
    when stopped, respecting subscriber filters.
  - `ct start` wait is bounded after osctld is stopping so unrelated events
    cannot keep shutdown draining forever.
  - `osctld/restart` now checks that an idle monitor client sees
    `osctld_shutdown` on graceful restart.
- Implemented uncommitted vpsAdmin changes:
  - Added `NodeCtld::DaemonHook.pre_stop`, which synchronously sends
    nodectld's existing `:pause` remote command with a default 5-second
    timeout and treats missing/unavailable nodectld as non-fatal.
  - Added daemon hook template `libnodectld/templates/daemon/hook/pre-stop`.
  - `Node#init` and `Node#refresh_pools` install the daemon hook on hypervisor
    nodes when `/run/osctl/hooks/daemon` exists.
  - `Daemon#do_commands` now checks `run?` before command selection and before
    each selected command, so a daemon pause in the middle of a selected batch
    stops further enqueues.
- Wrote durable note
  `notes/vpsadmin/2026-06-08-libnodectld-ruby-cache-abi.md`.
- Validation passed:
  - vpsAdminOS focused specs:
    `nix develop .#vpsadminos --command bash -lc 'export
    BUNDLE_GEMFILE=$PWD/osctld/Gemfile; export
    BUNDLE_PATH=$PWD/.gems/osctld; export
    GEM_PATH=$PWD/.gems/osctld:$GEM_PATH; cd osctld; bundle exec rspec
    spec/osctld/daemon_spec.rb
    spec/osctld/commands/event/subscribe_spec.rb
    spec/osctld/commands/container/lifecycle_spec.rb'`
    passed with 49 examples and 0 failures.
  - vpsAdmin libnodectld focused specs:
    `nix develop .#libnodectld --command bash -lc 'bundle exec rspec
    spec/nodectld/daemon_hook_spec.rb spec/nodectld/node_spec.rb
    spec/nodectld/daemon_spec.rb'`
    passed with 20 examples and 0 failures.
- Environment note:
  - The first `.#libnodectld` run failed before examples because
    `/tmp/dev-ruby-gems` contained native gems linked against Ruby 3.4.8 while
    the current libnodectld shell used Ruby 3.4.9.
  - The stale cache was moved to
    `/tmp/dev-ruby-gems.ruby-3.4.8-bak-20260608194748`; a fresh shell rebuilt
    `/tmp/dev-ruby-gems` and the focused specs passed.
- Remaining before commit:
  - Commit functional changes and generated gem changes separately when asked.

## Current follow-up validation

- Rebuilt vpsAdminOS packaged gems with build id
  `26.05.0.build20260608195550`:
  `nix develop --command make gems`.
- Rebuilt vpsAdmin packaged gems with final build id
  `4.1.0.build20260608200416`:
  `nix develop .#vpsadmin --command rake vpsadmin:gems`.
- vpsAdmin new libnodectld files were staged before gem generation because
  `libnodectld.gemspec` uses `git ls-files`.
- vpsAdmin focused specs after the final runtime guard change:
  `nix develop .#libnodectld --command bash -lc 'bundle exec rspec
  spec/nodectld/daemon_hook_spec.rb spec/nodectld/node_spec.rb
  spec/nodectld/daemon_spec.rb'`
  passed with 20 examples and 0 failures.
- vpsAdminOS focused specs after the event-subscribe loop cleanup:
  `nix develop .#vpsadminos --command bash -lc 'export
  BUNDLE_GEMFILE=$PWD/osctld/Gemfile; export
  BUNDLE_PATH=$PWD/.gems/osctld; export
  GEM_PATH=$PWD/.gems/osctld:$GEM_PATH; cd osctld; bundle exec rspec
  spec/osctld/daemon_spec.rb
  spec/osctld/commands/event/subscribe_spec.rb
  spec/osctld/commands/container/lifecycle_spec.rb'`
  passed with 49 examples and 0 failures.
- vpsAdminOS checks:
  - `git diff --check` passed.
  - `nix develop --command overcommit --run` passed; Nixfmt and RuboCop OK.
- vpsAdmin checks:
  - `git diff --check && git diff --cached --check` passed.
  - A full `nix develop .#vpsadmin --command overcommit --run` passed after
    fixing RuboCop offenses, but PHP CS Fixer reformatted unrelated clean
    `webui` files. Those hook-induced unrelated edits were reverted from the
    worktree.
  - Final targeted checks were run serially after clearing the ignored root
    `.gems` cache:
    `nix develop .#vpsadmin --command bash -lc 'bundle exec rubocop
    libnodectld/lib/nodectld/daemon.rb
    libnodectld/lib/nodectld/daemon_hook.rb
    libnodectld/lib/nodectld/node.rb
    libnodectld/spec/nodectld/daemon_hook_spec.rb
    libnodectld/spec/nodectld/daemon_spec.rb
    libnodectld/spec/nodectld/node_spec.rb && nixfmt --check
    packages/libnodectld/gemset.nix packages/nodectl/gemset.nix
    packages/nodectld/gemset.nix'`
    passed; RuboCop inspected 6 files with no offenses.
- Notes:
  - Running multiple `nix develop .#vpsadmin` commands in parallel can corrupt
    the ignored root `.gems` Bundler install. The cache was removed and rebuilt
    before final targeted checks.

## Current follow-up: auto jobs and consumer workflows

- vpsAdminOS branch was rewritten and pushed with final head
  `398342ea945dcb7b01499c46e1d88efcdf9589de`.
- Current vpsAdminOS commit stack:
  - `398342ea9` `os: update gems to 26.05.0.build20260608221438`
  - `0bf079cc2` `test-runner: add auto jobs and resource overcommit`
  - `6fafa7d43` `osctld: expose daemon pre-stop shutdown hooks`
  - `d8f03efee` `osctld: drain management clients before user-control`
  - `11c9d5f1b` `tests: collect vpsAdminOS failure diagnostics`
  - `ad4904231` `test-runner: refresh resource limits while scheduling`
- The previous vpsAdminOS RSpec workflow failure was investigated from the
  full job log because the run had no artifacts.
  - Run: `27164485050`, job: `80188018711`.
  - Root cause: `RunState.create` now creates `HOOK_DIR` and
    `DAEMON_HOOK_DIR`, but `spec/osctld/run_state_spec.rb` did not stub those
    constants into the temporary tree. CI tried to create `/run/osctl` as the
    runner user and failed with `Errno::EACCES`.
  - Fix: stub and assert `hook_dir` and `daemon_hook_dir` in
    `run_state_spec`; squashed into `osctld: expose daemon pre-stop shutdown
    hooks`.
- vpsAdminOS validation after the RSpec root-cause fix:
  - `nix develop ..#vpsadminos --command bundle exec rspec
    spec/osctld/run_state_spec.rb --seed 60093` passed with 8 examples.
  - `nix develop ..#vpsadminos --command bundle exec rspec spec/osctld
    --seed 60093` passed with 997 examples.
  - `git diff --check` passed.
  - Push used `nix develop --command git push --force-with-lease origin
    2026-06-08-test-runner-resources`.
- vpsAdmin branch was rewritten and pushed with final head
  `2b3527055ace17be0b5134e651d338c057d88080`.
- Current vpsAdmin commit stack:
  - `2b3527055` `packages: update nodectl gems`
  - `4188a208c` `flake: vpsadminos 0ac745ae3 -> 398342ea9`
  - `f96ef94d5` `ci: let test-runner choose integration concurrency`
  - `5db985185` `nodectld: pause before osctld stops`
  - `594a856df` `nodectld: stop admitting commands after pause`
- The earlier bundled vpsAdmin commit was split so the already-selected
  transaction admission fix is separate from daemon pre-stop hook integration.
- vpsAdmin validation after the final flake-lock rewrite:
  - `git diff --check origin/master..HEAD` passed.
  - Focused libnodectld specs had passed before the package rebuild, and the
    final flake-lock rewrite changed only the vpsAdminOS input.
- Updated and committed local, unpushed consumer branches:
  - `confctl`: `b67dead` `flake: vpsadminos a169291a5 -> 398342ea9`,
    `9f22d59` `ci: let test-runner choose integration concurrency`.
  - `terraform-provider-vpsadmin`: `bdf5a44`
    `flake: vpsadmin b46d38616 -> 2b3527055`, `9e2d6a6`
    `ci: let test-runner choose integration concurrency`.
  - `vpsf-status`: `573db8a` `flake: vpsadmin 597848686 -> 2b3527055`,
    `fa74c4a` `ci: let test-runner choose integration concurrency`.
  - `vpsfree-irc-bot`: `8b07b4f`
    `flake: vpsadmin c0aef236e -> 2b3527055`, `cb2c8d5`
    `ci: let test-runner choose integration concurrency`.
- Consumer workflow changes remove
  `vpsfreecz/vpsadminos/.github/actions/determine-test-jobs@staging` and run
  integration tests with `./test-runner.sh test -f --jobs auto`.
- Consumer branches are intentionally not pushed yet.
- Hook and validation notes for consumers:
  - `confctl` and `vpsfree-irc-bot` Overcommit hooks were installed with the
    project Nix/Bundler environments.
  - `vpsf-status` Lefthook hooks were installed with `nix develop --command
    make hooks`.
  - `terraform-provider-vpsadmin` has no declared hook framework.
  - `git diff --check` passed in all four consumer worktrees.
  - Commit hooks passed for all consumer commits.
  - After the `confctl` flake update changed Ruby from 3.4.8 to 3.4.9, the
    existing `.gems` cache had a stale native `json` extension. Rebuilt it
    with `nix develop --command bundle pristine json`; Overcommit then loaded
    and the flake commit passed hooks.
- GitHub workflow status at this point:
  - vpsAdminOS corrected `RSpec` run `27165394724` passed.
  - vpsAdminOS `RuboCop` run `27165394638` passed.
  - vpsAdminOS `CI` run `27165394635` and image run `27165394655` were queued.
  - vpsAdmin rerun has `Webui PHPUnit`, `Client Specs`, and
    `libnodectld Specs` green; `API Specs (topic parallel)` and `CI` were
    still in progress.
- Final workflow snapshot before stopping local watchers:
  - vpsAdminOS `CI` run `27165394635` remained queued after `1h14m46s`.
  - vpsAdminOS `Build and test changed container images` run `27165394655`
    remained queued after `1h14m46s`.
  - vpsAdmin latest `CI` run `27165562591` remained queued after `1h11m30s`.
  - vpsAdmin latest `Webui PHPUnit`, `Client Specs`, `libnodectld Specs`, and
    `API Specs (topic parallel)` were green.
  - `gh api repos/*/actions/runners` returned HTTP 403 with the available
    token, so runner availability could not be inspected directly.
  - The queued jobs had no job steps, logs, or artifacts to inspect yet.
- Local `gh run watch` processes were stopped after confirming the remaining
  jobs were queued, not failed or running.
- Final worktree status:
  - vpsAdminOS and vpsAdmin are clean and match their pushed feature branches.
  - `confctl`, `terraform-provider-vpsadmin`, `vpsf-status`, and
    `vpsfree-irc-bot` are clean local branches, each ahead of `origin/master`
    by two commits and intentionally not pushed.

## vpsAdminOS stable resource-capacity follow-up

- vpsAdminOS branch was later rewritten and pushed with final head
  `efdbb78351a2837e8843e5a716dc70de799c9c63`.
- Added `test-runner: use stable resource capacity`:
  - resource capacity now uses stable totals (`MemTotal` capped by effective
    cgroup limit, `/dev/shm` total size, and `nproc`) instead of adding current
    reservations to fluctuating available memory;
  - resource refresh is handled by one monitor thread at a configurable
    interval, defaulting to 15 seconds;
  - workers no longer refresh capacity in a tight scheduling loop.
- Validation before that push:
  - `ruby -c test-runner/lib/test-runner/resource_pool.rb` passed.
  - `ruby -c test-runner/lib/test-runner/executor.rb` passed.
  - `nix develop .#test-runner --command bash -lc 'cd test-runner &&
    TMPDIR=/tmp bundle exec rspec spec/test_runner/resource_pool_spec.rb
    spec/test_runner/executor_spec.rb spec/test_runner/cli/command_spec.rb'`
    passed with 42 examples.
  - `nix develop .#test-runner --command bash -lc 'cd test-runner &&
    TMPDIR=/tmp bundle exec rspec spec'` passed with 144 examples.
  - `git diff --check` passed.
  - `nix develop --command overcommit --run` passed after fixing one RuboCop
    offense.
  - `nix develop --command make gems` rebuilt packaged gems with build id
    `20260609094620`.
- GitHub results for the `efdbb7835` push:
  - RuboCop run `27192412049` passed.
  - RSpec run `27192412029` passed.
  - CI run `27192412061` failed in job `80275924835`.
- Downloaded failed CI evidence:
  - job log: `/tmp/vpsadminos-ci-27192412061/job.log`;
  - artifact: `/tmp/vpsadminos-ci-27192412061/artifacts`;
  - artifact name `os-test-logs-27192412061`, id `7503219417`.
- Resource messages in the failed CI run showed the resource fix working:
  - initial limit line was stable at about `memory=0 MiB/92.0 GiB`,
    `shm=0 MiB/120.7 GiB`, `cpus=0/63`;
  - reservation lines kept stable totals and changed only the used side;
  - the earlier high-frequency `Resource limits updated` spam and growing
    totals were gone.
- The CI failure root cause was an osctld restart test race, not OOM and not
  the runner resource scheduler:
  - only unexpected failure was
    `os-test-osctld__restart-b891f158/test-result.txt`;
  - failing example was `idle clients notifies monitor clients during graceful
    restart`;
  - the monitor job log contained
    `No such file or directory - connect(2) for /run/osctl/osctld.sock`;
  - `/var/log/osctld` in the artifact had no `event_subscribe` before the
    graceful restart at `2026-06-09 10:15:59 +0200`;
  - `wait_host_job_running` only proved the background shell still existed,
    so the restart could remove the socket before `osctl -j monitor` had
    connected and subscribed.
- Fixed locally with commit `fb4377d6c`
  `tests: wait for event monitor subscription before restart`:
  - the test now starts a small Ruby protocol monitor using only `json` and
    `socket`;
  - it writes a ready marker only after osctld replies to `event_subscribe`
    with `subscribed`;
  - the graceful restart assertion still checks the monitor output for
    `osctld_shutdown`;
  - the fixed one-second sleep was removed from `wait_host_job_running`.
- Local validation of the test fix:
  - `./test-runner.sh ls osctld/restart` returned `osctld/restart`.
  - `git diff --check` passed.
  - `./test-runner.sh test osctld/restart` passed in 326.26 seconds with all
    7 examples successful.
  - Local log confirmed the ready marker was checked before restart and the
    monitor output contained `{"type":"osctld_shutdown","opts":{}}`.
  - `nix develop --command overcommit --run` passed.
- The branch was rewritten again so the generated gem update remains the final
  commit:
  - `633e7cf2a` `os: update gems to 26.05.0.build20260609094620`;
  - `fb4377d6c` `tests: wait for event monitor subscription before restart`;
  - `d7246fc4e` `test-runner: use stable resource capacity`;
  - earlier functional commits unchanged.
- Push notes:
  - plain `git push --force-with-lease` failed because the installed
    Overcommit hook could not load the `overcommit` gem outside the Nix
    environment;
  - `nix develop --command git push --force-with-lease origin
    2026-06-08-test-runner-resources` succeeded and force-updated the remote
    from `efdbb7835` to `633e7cf2a`.
- GitHub Actions after the `633e7cf2a` push:
  - only a new `CI` run was created for this head, run `27196871433`;
  - build job `80290649383` passed in about 2 minutes;
  - test job `80291032483` passed in about 61 minutes.
- Completed vpsAdminOS CI log was saved at
  `/tmp/vpsadminos-ci-27196871433/test-job.log`.
- CI log checks:
  - resource totals stayed stable at `memory=92.0 GiB`,
    `shm=120.7 GiB`, and `cpus=63`;
  - there were no `Resource limits updated` spam lines;
  - `osctld/restart` ran as `[26/73]` and passed in 213.41 seconds;
  - the suite ended with `Run 263 test scripts of 73 tests` and
    `73 tests successful`;
  - the full-log upload step was skipped because there were no failed tests.

## vpsAdmin pin refresh after validated vpsAdminOS head

- vpsAdmin was rewritten so its vpsAdminOS flake pin points at the validated
  vpsAdminOS head `633e7cf2a45609eca6d68f51f78442d8e0143de8`.
- Rewrite steps:
  - reset the old vpsAdmin flake-pin and generated gem commits;
  - temporarily stashed generated nodectl package files;
  - ran `nix develop .#vpsadmin --command
    tools/update_vpsadminos_flake.sh
    github:vpsfreecz/vpsadminos/633e7cf2a45609eca6d68f51f78442d8e0143de8`;
  - reapplied the generated package files and recommitted them as the final
    subject-only gem update.
- Current vpsAdmin stack:
  - `dbc6b58f7` `packages: update nodectl gems`;
  - `0efe4968f` `flake: vpsadminos 0ac745ae3 -> 633e7cf2a`;
  - `f96ef94d5` `ci: let test-runner choose integration concurrency`;
  - earlier nodectld shutdown-admission commits unchanged.
- vpsAdmin validation before push:
  - repository helper committed the flake input update and hooks passed;
  - generated package commit hooks passed;
  - `git diff --check origin/master..HEAD` passed.
- Pushed with `nix develop .#vpsadmin --command git push --force-with-lease
  origin 2026-06-08-test-runner-resources`, updating the remote from
  `2b3527055` to `dbc6b58f7`.
- GitHub Actions for the `dbc6b58f7` push started:
  - `Webui PHPUnit` run `27200494318`;
  - `Client Specs` run `27200494341`;
  - `libnodectld Specs` run `27200494481`;
  - `API Specs (topic parallel)` run `27200494485`;
  - `CI` run `27200494563`.
- Early vpsAdmin workflow results:
  - `Webui PHPUnit` passed;
  - `Client Specs` passed;
  - `libnodectld Specs` passed;
  - `API Specs (topic parallel)` passed;
  - `CI` job `80302985313` was still in progress in the `Run tests` step
    after selecting and previewing integration tests successfully.
  - GitHub still returned `BlobNotFound`/HTTP 404 for the CI job log while
    the job was in progress, so no partial integration-test log could be
    inspected.

## Consumer pin refresh after validated vpsAdminOS head

- `confctl` was rewritten locally so its direct vpsAdminOS flake pin points at
  the validated head `633e7cf2a45609eca6d68f51f78442d8e0143de8`.
- Current `confctl` stack:
  - `665188b` `flake: vpsadminos a169291a5 -> 633e7cf2a`;
  - `9f22d59` `ci: let test-runner choose integration concurrency`.
- `confctl` validation:
  - `git diff --check` passed;
  - flake metadata reports vpsAdminOS rev
    `633e7cf2a45609eca6d68f51f78442d8e0143de8`;
  - commit hooks passed.
- The other unpushed consumer branches were rewritten locally to pin the
  pushed vpsAdmin head `dbc6b58f7baff240dc08b583f10cd3ca458cbfea`, which in
  turn carries vpsAdminOS `633e7cf2a45609eca6d68f51f78442d8e0143de8`:
  - `terraform-provider-vpsadmin`: `ee7abed`
    `flake: vpsadmin b46d38616 -> dbc6b58f7`;
  - `vpsf-status`: `6bc8ac1`
    `flake: vpsadmin 597848686 -> dbc6b58f7`;
  - `vpsfree-irc-bot`: `f325278`
    `flake: vpsadmin c0aef236e -> dbc6b58f7`.
- Consumer validation after pin refresh:
  - `git diff --check origin/master..HEAD` passed in all four repositories;
  - flake metadata confirmed the expected vpsAdmin/vpsAdminOS revisions;
  - `vpsf-status` Lefthook passed on commit;
  - `vpsfree-irc-bot` Overcommit passed on commit;
  - `terraform-provider-vpsadmin` has no declared hook framework;
  - `confctl` hook validation is noted above.
- Current worktree status snapshot:
  - `vpsadminos` is clean and matches pushed
    `origin/2026-06-08-test-runner-resources` at `633e7cf2a`;
  - `vpsadmin` is clean and matches pushed
    `origin/2026-06-08-test-runner-resources` at `dbc6b58f7`;
  - `confctl`, `terraform-provider-vpsadmin`, `vpsf-status`, and
    `vpsfree-irc-bot` are clean local branches ahead of `origin/master` by two
    commits and remain unpushed.
- Current workflow snapshot:
  - vpsAdminOS `CI` run `27196871433` passed.
  - Direct check-runs for vpsAdminOS head
    `633e7cf2a45609eca6d68f51f78442d8e0143de8` were rechecked after the
    user reported a failure; both current-head checks were successful and
    there were no non-success check-runs. The visible failed vpsAdminOS CI run
    is stale run `27192412061` on old head `efdbb7835`, whose artifact root
    cause was already fixed by commit `fb4377d6c`.
  - vpsAdmin `Webui PHPUnit`, `Client Specs`, `libnodectld Specs`, and
    `API Specs (topic parallel)` passed for `dbc6b58f7`.
  - vpsAdmin `CI` run `27200494563` remained in progress in job
    `80302985313`, step `Run tests`.

## Follow-up: daemon hook docs and restart test named shells

- The daemon pre-stop hook added by `osctld: expose daemon pre-stop shutdown
  hooks` was undocumented. The commit was rewritten to add the hook to
  `osctl/man/man8/osctl.8.md`:
  - daemon hooks live under `/run/osctl/hooks/daemon`;
  - `pre-stop` runs after `osctld` enters the stopping state and before it
    stops accepting management clients;
  - hook failures are logged and do not abort shutdown;
  - documented environment variables are `OSCTL_HOOK_NAME`,
    `OSCTL_DAEMON_STATE`, and `OSCTL_DAEMON_PID`.
- Commit `fb4377d6c` had a malformed commit-message paragraph break. The branch
  was rewritten and the commit is now `5b4f0c413` with normal paragraph
  wrapping and hooks passing.
- The `osctld/restart` test was refactored to use named machine shells instead
  of guest-side detached `nohup` jobs:
  - commit `c9af52729` `tests: use named shells in osctld restart test`;
  - the test still uses `machines/vpsadminos/tank.nix`, merged with top-level
    machine shells `client` and `restart`;
  - long-lived commands run in Ruby threads through named shells;
  - protocol and hook ready markers remain the synchronization points;
  - job status and output now come directly from the test runner.
- Because `osctl.8.md` is packaged in the `osctl` gem, vpsAdminOS gems were
  rebuilt again:
  - new generated commit `1d37a2ea6`
    `os: update gems to 26.05.0.build20260609152612`;
  - previous generated commit `633e7cf2a` was replaced.
- Validation:
  - embedded Ruby syntax check for `tests/suite/osctld/restart.nix` passed;
  - `./test-runner.sh ls osctld/restart` resolved the test;
  - `./test-runner.sh test osctld/restart` passed all 7 examples in
    335.83 seconds;
  - commit hooks passed for both the named-shell test commit and generated gem
    commit.
- Current vpsAdminOS local head:
  `1d37a2ea63c57aa64b1ed2f1dcec69b2b705a050`.
- vpsAdmin and consumer pins still point at the superseded vpsAdminOS/vpsAdmin
  heads and need to be refreshed after this vpsAdminOS head is pushed.

## Follow-up: refreshed vpsAdmin and consumer pins after hook docs

- vpsAdminOS branch was force-pushed to
  `origin/2026-06-08-test-runner-resources` at
  `1d37a2ea63c57aa64b1ed2f1dcec69b2b705a050`.
- vpsAdmin was rewritten to replace the superseded vpsAdminOS pin and nodectl
  gem build:
  - `82f4d5a9f` `packages: update nodectl gems`;
  - `172ca93a0` `flake: vpsadminos 0ac745ae3 -> 1d37a2ea6`;
  - earlier workflow and nodectld shutdown-admission commits unchanged.
- Rebuilt nodectl packages with `rake vpsadmin:gems`:
  - vpsAdmin package build id `4.1.0.build20260609155151`;
  - osctl package build id `26.05.0.build20260609152612`.
- vpsAdmin validation before push:
  - `tools/update_vpsadminos_flake.sh` committed the flake input update and
    hooks passed;
  - generated package commit hooks passed;
  - generated package files no longer reference superseded osctl build
    `26.05.0.build20260609094620` or nodectl build
    `4.1.0.build20260609151543`.
- vpsAdmin branch was force-pushed to
  `origin/2026-06-08-test-runner-resources` at
  `82f4d5a9f8336cfb9f0467bd4b4f193468142a7f`.
- Consumer branches were rewritten and pushed:
  - `confctl`: `45232f0`
    `flake: vpsadminos a169291a5 -> 1d37a2ea6`;
  - `terraform-provider-vpsadmin`: `d5bf79f`
    `flake: vpsadmin b46d38616 -> 82f4d5a9f`;
  - `vpsf-status`: `51e8664`
    `flake: vpsadmin 597848686 -> 82f4d5a9f`;
  - `vpsfree-irc-bot`: `763029c`
    `flake: vpsadmin c0aef236e -> 82f4d5a9f`.
- Consumer flake locks now point at vpsAdmin
  `82f4d5a9f8336cfb9f0467bd4b4f193468142a7f` and vpsAdminOS
  `1d37a2ea63c57aa64b1ed2f1dcec69b2b705a050`.
- Hook validation while amending/pushing consumer commits:
  - `confctl` Overcommit/Nixfmt hooks passed;
  - `vpsf-status` Lefthook pre-commit ran and passed;
  - `vpsfree-irc-bot` Overcommit hooks passed;
  - `terraform-provider-vpsadmin` has no declared hook framework in this
    branch.
- GitHub Actions snapshot after pushes:
  - vpsAdminOS `RuboCop`, `RSpec`, and changed image workflow passed at
    `1d37a2ea6`; vpsAdminOS `CI` run `27210837128` is still in progress.
  - vpsAdmin `Webui PHPUnit`, `Client Specs`, `libnodectld Specs`, and
    `API Specs (topic parallel)` passed at `82f4d5a9f`; vpsAdmin `CI` run
    `27211171072` is still queued.
  - `confctl` `RuboCop` and `RSpec` passed at `45232f0`; `Tests` run
    `27211423410` is still queued.
  - `vpsfree-irc-bot` `RSpec` passed at `763029c`; its integration run
    `27211422303` is still queued.
  - `terraform-provider-vpsadmin` integration run `27211415840` and
    `vpsf-status` integration run `27211416076` are still queued.
