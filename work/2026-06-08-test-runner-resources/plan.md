# 2026-06-08-test-runner-resources

## Goal

Check whether the vpsAdminOS test runner notices host CPU, memory, and
`/dev/shm` capacity changes after startup. If it does not, prepare a change
that lets the scheduler react to added or removed resources while a suite is
already running.

## Affected repositories

- `vpsadminos`
  - Branch: `2026-06-08-test-runner-resources`
  - Worktree: `worktrees/2026-06-08-test-runner-resources/vpsadminos`
  - Relevant code:
    - `test-runner/lib/test-runner/resource_pool.rb`
    - `test-runner/lib/test-runner/executor.rb`
    - `test-runner/lib/test-runner/cli/app.rb`
    - `test-runner/man/man1/test-runner.1.md`
    - `test-runner/spec/test_runner/executor_spec.rb`
    - `osctld/lib/osctld/thread_reaper.rb`
    - `osctld/lib/osctld/generic/server.rb`
    - `osctld/lib/osctld/daemon.rb`
    - `osctld/lib/osctld/user_control/supervisor.rb`
    - `osctld/spec/osctld/thread_reaper_spec.rb`
    - `tests/suite/osctld/restart.nix`
- `vpsadmin`
  - Branch: `2026-06-08-test-runner-resources`
  - Worktree: `worktrees/2026-06-08-test-runner-resources/vpsadmin`
  - Relevant code:
    - `libnodectld/lib/nodectld/daemon.rb`
    - `libnodectld/lib/nodectld/daemon_hook.rb`
    - `libnodectld/lib/nodectld/node.rb`
    - `libnodectld/templates/daemon/hook/pre-stop`
    - `libnodectld/spec/nodectld/daemon_spec.rb`
    - `libnodectld/spec/nodectld/daemon_hook_spec.rb`
    - `libnodectld/spec/nodectld/node_spec.rb`
- `confctl`
  - Branch: `2026-06-08-test-runner-resources`
  - Worktree: `worktrees/2026-06-08-test-runner-resources/confctl`
  - Relevant code:
    - `.github/workflows/tests.yml`
    - `flake.lock`
- `terraform-provider-vpsadmin`
  - Branch: `2026-06-08-test-runner-resources`
  - Worktree:
    `worktrees/2026-06-08-test-runner-resources/terraform-provider-vpsadmin`
  - Relevant code:
    - `.github/workflows/integration-tests.yml`
    - `flake.lock`
- `vpsf-status`
  - Branch: `2026-06-08-test-runner-resources`
  - Worktree: `worktrees/2026-06-08-test-runner-resources/vpsf-status`
  - Relevant code:
    - `.github/workflows/integration-tests.yml`
    - `flake.lock`
- `vpsfree-irc-bot`
  - Branch: `2026-06-08-test-runner-resources`
  - Worktree:
    `worktrees/2026-06-08-test-runner-resources/vpsfree-irc-bot`
  - Relevant code:
    - `.github/workflows/integration-tests.yml`
    - `flake.lock`

## Approach

Current findings:

- The original runner did not detect resource changes after it had started.
  `Executor#initialize` built one `ResourcePool` and kept the sampled
  capacities for the whole run.
- The first dynamic implementation refreshed in scheduler workers, but it used
  fluctuating available memory and available `/dev/shm` as the pool total and
  added already-reserved resources back to those totals. Under load this made
  the reported pool capacity grow with reservations and then fluctuate many
  times per second.
- Stable scheduling must use assigned capacity as the pool total and keep
  pressure/availability checks separate if they are ever needed.

Implementation plan:

1. Split stable capacity detection from resource accounting.
   - Keep `ResourcePool` responsible for used resources and scheduling checks.
   - Add an injectable detector/capacity source so specs can simulate resource
     changes without reading the real host.
   - Memory capacity is the effective cgroup memory limit when present,
     capped by `MemTotal`; otherwise use `MemTotal`.
   - `/dev/shm` capacity is the filesystem total size, not available blocks.
   - CPU capacity continues to use `nproc`.

2. Track refreshed capacities with optional explicit ceilings.
   - Explicit CLI or environment caps (`--max-memory-mib`,
     `--max-shm-mib`, `--max-cpus`, and matching env vars) are ceilings on
     refreshed detection, not fixed overrides.
   - If detection succeeds and an explicit max is set, use the lower value.
   - If detection fails and an explicit max is set, fall back to the explicit
     max.
   - Apply configured overcommit factors and reserves after detection and max
     ceilings.
   - If detection fails, preserve the current unlimited behavior for that
     dimension when no explicit max is set.
   - Do not add already-reserved memory or `/dev/shm` back to capacity. The
     pool total is assigned capacity; reservations are accounted separately.

3. Refresh capacity from a side-channel monitor.
   - Start one executor-owned monitor thread that refreshes cached capacity at
     a configurable interval, defaulting to 15 seconds.
   - Scheduler workers read cached capacity only. They do not call
     `/proc/meminfo`, `df`, or `nproc` while waiting for resources.
   - When refreshed capacity changes, broadcast the scheduler condition
     variable so pending tests can be reconsidered immediately.
   - Log concise resource-limit updates only when the formatted pool status
     changes.

4. Define behavior for resource decreases.
   - Do not stop or kill already-running tests.
   - If used resources exceed the new capacity, block starting new tests until
     enough running tests finish.
   - Keep the existing deadlock escape for a single oversized test when no test
     is running, because a test may legitimately exceed the detected capacity.

5. Update docs and tests.
   - Document that auto-detected resource limits refresh during the run and
     that explicit max options/env vars are ceilings/fallbacks.
   - Add focused specs for CPU/memory increase, CPU/memory decrease,
     `/dev/shm` capacity detection, explicit max ceilings, detection fallback,
     worker refresh suppression, monitor wakeup, and log/status updates.

Follow-up CI investigation:

6. Failed GitHub Actions runs must be investigated from their artifacts before
   reruns are accepted as validation.
   - Download and inspect failed artifacts/logs.
   - Record the root-cause evidence in `state.md`.
   - If the artifact is missing key logs, improve diagnostics so the next
     failure has enough evidence.

7. Add vpsAdminOS test-runner diagnostics for unexpected script failures.
   - Use `tests/runner/extensions` and the existing `after_test_script_run`
     hook.
   - Collect per-machine service, osctld, container, process, filesystem, and
     temporary test-job logs before VM teardown.
   - Keep this as diagnostics only; it does not replace fixing the underlying
     failing behavior.

8. Fix the osctld graceful-restart/user-control race.
   - Tag management and user-control client threads in `ThreadReaper`.
   - During daemon stop, close and join the public management accept loop,
     then drain only management clients while user-control servers remain
     available for callbacks needed by already-running commands.
   - Stop user-control servers only after management clients have drained,
     then stop and join remaining tracked client threads before shutting down
     daemon dependencies.
   - Preserve bounded shutdown by stopping all remaining tracked clients after
     user-control acceptors are closed.
   - Add low-level specs for grouped drains and class-level keyword forwarding,
     because Ruby keyword forwarding is required by the new grouped API.

9. Fix nodectld/osctld shutdown coordination.
   - Add an osctld daemon lifecycle hook directory under `/run/osctl/hooks`.
   - Run daemon `pre-stop` hooks immediately after osctld enters stopping
     state and before the management socket is closed.
   - Keep hook failures non-fatal so osctld can still shut down when nodectld
     is unavailable or broken.
   - Have nodectld install `/run/osctl/hooks/daemon/pre-stop` on hypervisor
     nodes. The hook synchronously sends nodectld's existing `:pause` remote
     command with a bounded timeout.
   - Keep the hook absent on non-node roles and on old vpsAdminOS versions
     where the daemon hook directory does not exist.
   - Stop nodectld from enqueuing further commands when a full daemon pause
     arrives in the middle of a selected transaction batch.

10. Keep osctld shutdown bounded for internal waits.
    - Do not split event subscribers into internal/external classes.
    - When `event_subscribe` is asked to stop, send a synthetic
      `osctld_shutdown` event to that subscriber immediately, respecting its
      filters, then return the normal shutdown error.
    - Bound `ct start --wait infinity` after osctld is stopping so unrelated
      events cannot keep the management-client drain alive indefinitely.

11. Move integration workflows to runner-managed concurrency.
    - Add `--jobs auto` to the test-runner CLI. Auto mode lets the runner
      reserve resources dynamically while using all selected tests as the hard
      concurrent-test ceiling.
    - Add configurable overcommit factors:
      `--cpu-overcommit`, `--memory-overcommit`, and `--shm-overcommit`.
      The CPU default is `1.5`; memory and `/dev/shm` default to `1.0`.
    - Keep GitHub workflows simple. Remove the shared
      `determine-test-jobs` action and run integration tests with
      `--jobs auto` so the runner owns CPU and memory scheduling in all
      consumers.

## Compatibility and deployment

- No persisted state, database schema, API, protocol, Nix module option, or
  generated client compatibility impact.
- Deployment is local to the `test-runner` Ruby gem in vpsAdminOS.
- Ruby gem package metadata must be regenerated so packaged Nix test-runner
  builds use the new code.
- Mixed versions are acceptable: old runners keep static limits, new runners
  refresh auto-detected limits.
- Rollback is safe. State created by a new runner is the same test state/log
  structure used today.
- No coordinated update of all running machines or nodes is required.
- The diagnostic extension affects only test execution artifacts and has no
  deployment impact on vpsAdminOS machines.
- The osctld race fix changes shutdown ordering only. It does not change
  persisted state, pool/container on-disk formats, APIs, or command protocol
  payloads.
- Rolling deployment is acceptable. Old daemons may still have the restart
  race; new daemons drain management clients before closing user-control.
- Rollback is safe because no state created by the new daemon depends on the
  new shutdown ordering.
- No coordinated update of all running vpsAdminOS machines or nodes is
  required.
- The daemon hook directory is a new runtime path only. It is recreated on
  osctld startup and does not persist state.
- Mixed vpsAdminOS/vpsAdmin versions are acceptable:
  - New osctld with old nodectld has an empty daemon hook directory and falls
    back to the bounded internal shutdown behavior.
  - New nodectld with old osctld skips daemon hook installation because the
    runtime directory is absent.
  - Full immediate vpsAdmin pause during osctld stop requires both sides of
    the change.
- Rollback is safe. Removing the new nodectld hook leaves osctld with no
  pre-stop script to run; no state created by the new hook is required by old
  code.
- Removing `.github/actions/determine-test-jobs` from vpsAdminOS requires
  downstream workflow updates for repositories using the shared vpsAdminOS test
  framework. Local branches were prepared for `confctl`,
  `terraform-provider-vpsadmin`, `vpsf-status`, and `vpsfree-irc-bot`.
- The consumer workflow changes affect CI only and do not change deployed
  service behavior, persisted state, API contracts, or rollback behavior.
- Consumer flake pins are temporary feature-branch pins for CI compatibility
  while this branch is under review. They should be updated or dropped when
  the vpsAdminOS/vpsAdmin changes are merged to their target branches.

## Testing plan

- Run targeted unit tests:
  `nix develop .#test-runner --command bash -lc 'cd test-runner && bundle exec
  rspec spec/test_runner/resource_pool_spec.rb
  spec/test_runner/executor_spec.rb'`.
- Run the standalone test-runner suite:
  `nix develop .#test-runner --command bash -lc 'cd test-runner && TMPDIR=/tmp
  bundle exec rspec spec'`.
- Run `nix develop --command make gems` after Ruby source changes.
- Run `nix develop --command overcommit --run` before any commit, because this
  repository declares Overcommit hooks.
- Optional smoke check after implementation:
  `nix develop .#test-runner --command bundle exec ./test-runner/bin/test-runner
  ls '<pattern>'`.
- Run full osctld specs after the daemon lifecycle change:
  `nix develop .#vpsadminos --command bash -lc 'export
  BUNDLE_GEMFILE=$PWD/osctld/Gemfile BUNDLE_PATH=$PWD/.gems
  GEM_PATH=$PWD/.gems:$GEM_PATH; cd osctld; bundle exec rspec'`.
- Run the restart regression:
  `./test-runner.sh test osctld/restart`.
- Run focused shutdown/pause specs after the daemon-hook change:
  `nix develop .#vpsadminos --command bash -lc 'export
  BUNDLE_GEMFILE=$PWD/osctld/Gemfile; export BUNDLE_PATH=$PWD/.gems/osctld;
  export GEM_PATH=$PWD/.gems/osctld:$GEM_PATH; cd osctld; bundle exec rspec
  spec/osctld/daemon_spec.rb spec/osctld/commands/event/subscribe_spec.rb
  spec/osctld/commands/container/lifecycle_spec.rb'`.
- Run focused libnodectld specs:
  `nix develop .#libnodectld --command bash -lc 'bundle exec rspec
  spec/nodectld/daemon_hook_spec.rb spec/nodectld/node_spec.rb
  spec/nodectld/daemon_spec.rb'`.
- Rebuild packaged gems after Ruby source changes:
  - vpsAdminOS: `nix develop --command make gems`.
  - vpsAdmin: `nix develop .#vpsadmin --command rake vpsadmin:gems`.
- For consumer workflow updates:
  - Run `git diff --check`.
  - Verify no workflow still references `determine-test-jobs`.
  - Install and run declared hooks through each repository's development
    shell.
