# 2026-07-24-ct-start-hang

## Repositories

- `vpsadminos`
  - Branch: `2026-07-24-ct-start-hang`
  - Worktree:
    `worktrees/2026-07-24-ct-start-hang/vpsadminos`
  - Base: `origin/staging`
  - Base commit: `fc6c9fe67d7d365f26a5ab286625fd55fd5f79e1`

## Status

- Root cause confirmed and the timeout-free redesign is implemented.
- Mandatory review findings were first addressed in `6384c9ae5`.
- Follow-up reviews rejected `init_pid` and pre-wrapper boundaries as
  ambiguous or fallible lifecycle signals.
- Wrapper watchdogs, TERM/KILL handling, fixed 30/10-second limits, the
  runtime-start promise, and the experimental raw-hook VM fixture have been
  removed.
- The current design is event-driven: a managed run is marked pending in
  memory, `ctptywrapper` signals exact readiness through a pipe, and
  post-stop/console cleanup fulfills the existing exit promise.
- No lifecycle watchdog, wrapper TERM/KILL path, or terminal lifecycle timeout
  remains. `wait: 'infinity'` is unbounded.
- The start command releases the manipulation lock before waiting for old
  cleanup or for RUNNING. If the queued reboot starts the replacement first,
  another start joins that launch.
- Focused specs for the redesign: 200 examples, 0 failures, seed `31589`.
- `ctptywrapper`: 9 tests, 0 failures.
- `nix build .#ctptywrapper --no-link` succeeds.
- The existing run-configuration file is retained through exact-generation
  console cleanup. On restart, a live socket is reconnected; a stopped run
  whose socket is already gone resumes the same cleanup path.
- Infinite cleanup waits block directly on their completion token. Command
  shutdown explicitly wakes the token; there is no lifecycle polling interval
  or cleanup cutoff.
- Console connections carry their exact run configuration, so late EOF from an
  old wrapper cannot select or clean up a replacement run.
- Cached monitor state and the corresponding in-memory runtime phase now change
  atomically. A stopped snapshot during the pre-LXC launch window does not
  misclassify the active wrapper as old cleanup.
- osctld now binds the listener and attaches a reserved exact-generation client
  before launching the wrapper. This removes the abrupt-restart interval in
  which a live wrapper existed without a socket identity and removes all
  fallible client allocation from the post-spawn readiness path.
- Console input remains disabled until wrapper readiness, while EOF is observed
  immediately. TTY read/write failures clear only the matching descriptor, so
  stale EOF cannot clear a replacement and write failure cannot kill the sole
  cleanup observer.
- Restart reconnection retries resource exhaustion indefinitely with bounded
  backoff and no lifecycle cutoff. Missing/refused prebound sockets are exact
  evidence that no wrapper owns the listener.
- Normal console EOF cleanup also retries temporary thread exhaustion with
  bounded backoff and no lifecycle cutoff. Shutdown deliberately leaves the
  retained runtime identity for the next daemon instead of abandoning a live
  daemon's pending start.
- Reboot intent is stored as an optional boolean in the existing transient
  runtime file and therefore survives daemon restart during retained cleanup.
- Wrapper event processing handles a polled old client before accepting its
  queued replacement, preventing a dead pre-restart client from blocking reads
  on the new connection.
- Clean amended commit:
  `078afb23788a260393190c1b582b66dca76d2016`.
- Worktree is clean and one commit ahead of `origin/staging`.
- The final repository hook run passed Nixfmt and RuboCop. Commit-message hooks
  passed with only their 72-column advisory; all commit-message lines satisfy
  the workspace's mandatory 80-column limit.
- `wait: false` continues to complete managed-wrapper launch and exact console
  handoff synchronously, then skips waiting for RUNNING. It does not wait for
  an older run's cleanup and returns that conflict immediately.
- Rollback is file-format compatible but must be done after per-node container
  lifecycle activity has settled. An old daemon cannot reconstruct the new
  in-memory barrier during the retained stopped/pre-ready window and can
  otherwise re-enter the original race. Emergency recovery should roll the
  node forward again; manual state recovery is safe only after verifying that
  no wrapper owns the retained console listener.
- Runtime-file retention is conditional on the exact run's managed
  `start_pending` marker inside the container's stopped transition. Manual LXC
  starts have no console observer and therefore keep the original
  immediate-destroy behavior for both halt and reboot.
- Mandatory fresh-context review of
  `fc6c9fe67d7d365f26a5ab286625fd55fd5f79e1..078afb23788a260393190c1b582b66dca76d2016`
  concluded with no Blocking, Important, or Advisory findings. The reviewer
  accepted the per-node rollout and documented rollback drain/recovery
  constraint.
- `./test-runner.sh test osctl/ct-console` passed all 6 examples and the test
  script in 272.58 seconds. It verified console startup, input before and after
  osctld restart, terminal resize propagation, attached-console behavior across
  clean stop/start, and clean stop.

## Current redesign review

- Mandatory review of `291dc4e70` found two blocking design issues:
  - the persisted cleanup marker could not be paired with its recreated,
    in-memory exit promise after osctld restart and could itself strand starts;
  - a no-wait start could release the lock before the marker was set and allow
    another start to overwrite the launch.
- It also found that cleanup and startup restarted the finite wait budget.
- The redesign removes the persisted marker. A live console socket reconstructs
  pending cleanup on daemon restart. The already-existing run-configuration
  file is retained until console cleanup, which lets a restarted daemon resume
  cleanup even when the wrapper socket has already disappeared.
- The wrapper readiness pipe closes the pre-LXC/no-wait window without using a
  clock. Finite cleanup and RUNNING waits share one deadline; the exact wrapper
  handoff is never abandoned while its outcome is still unknown.
- The standalone reviewer inspected the dirty follow-up and identified
  restart, exact-generation, and monitor-ordering gaps. Those findings are now
  addressed; the reviewer must provide a concluding review of the clean amended
  commit before the VM integration test.

## Superseded design history

The remaining results below describe rejected intermediate designs. They are
kept as investigation history, not as the current implementation.

## Commands run

- `bin/dev-session current`
- `git status --short --branch`
- Inspected both screenshots in `osctl-debug-threads-ls/`.
- Filtered `node21-osctld-log.log` around container `tank:26108`.
- `bin/dev-session worktree add 2026-07-24-ct-start-hang vpsadminos
  --as-is --base origin/staging`
- Read the workspace and repository `AGENTS.md` files.
- Inspected osctld start, stop, console, run-configuration, monitor, and
  manipulation-lock code and history.
- Built the `libosctl` native extension in the osctld bundle.
- Ran focused osctld specs for promise, run configuration, container, and
  lifecycle commands.
- Attempted the complete osctld spec suite.
- Ran RuboCop on all changed Ruby files.
- Ran `./test-runner.sh ls osctl/ct-console`.
- Ran `nix develop --command overcommit --run`.
- Committed with
  `nix develop --command git commit -F
  /tmp/vpsadminos-ct-start-hang-commit.txt`.
- Ran the mandatory fresh-context review against `95d715b30`.
- Ran the expanded focused spec set after addressing review findings.
- Amended the review fixes into the functional commit using the required Nix
  development environment and commit-message file.
- Ran the expanded console, monitor, receive-transfer, lifecycle, container,
  run-configuration, promise, and manipulation-lock specs with a test-only LXC
  load stub.

## Results

- At `00:23:44`, container `tank:26108` exited; lxc-monitor reported
  `STOPPING` and `STOPPED` by `00:23:45`.
- The old LXC `ct_post_stop` hook had not finished. External `ct_start` arrived
  at `00:29:37`, found the monitor state stopped, acquired the container
  manipulation lock, and attempted another start while old cgroup/runtime
  cleanup was still active.
- The overlapping start hit busy cgroups and failed to attach its wrapper.
- The old `ct_post_stop` reported `Reboot requested` at `00:29:46`. Its console
  stop handler subsequently tried to run `Commands::Container::Start` with
  `manipulation_lock: 'wait'`.
- The thread dump shows the external start still holding the manipulation lock
  in `Start#wait_for_ct`, while the reboot start is blocked in
  `ManipulationLock#acquire`. The state transition needed by the first start
  therefore cannot be produced.
- `ct recover state --no-lock 26108` generated state recovery and released the
  waiting start; the queued reboot then started the container successfully.
- LXC monitor state is not a sufficient start barrier: it reports `STOPPED`
  before the old `ct_post_stop` hook and console cleanup have finished. Starting
  in this window overwrites the old run configuration and collides with the old
  runtime's cgroups.
- `Container::Start` now checks for an unfulfilled run-exit promise while
  holding the manipulation lock. It releases the lock before waiting, then
  reacquires it and retries the normal start path. The cleanup and startup
  phases share the command's existing wait deadline.
- `Promise` now remembers fulfillment and immediately fulfills late tokens.
  This closes the race between releasing the manipulation lock and subscribing
  to the old run's exit notification.
- A fulfilled past run is intentionally ignored. The console fulfills the exit
  promise immediately before requesting the automatic reboot and only forgets
  the past run after that start returns.
- Initial focused specs: 88 examples, 0 failures, seed `31589`.
- Mandatory review found two blocking edge cases:
  - a pre-launch failure, such as a dataset mount error, could leave an
    unfulfilled active run configuration that the next start would
    misinterpret as pending cleanup;
  - a nested start called by a command that already owned the reentrant
    manipulation lock could still wait while the outer lock remained held.
- Both findings are fixed. A stopped active run configuration without an init
  PID is treated as a replaceable pre-launch attempt. `Manipulable` now exposes
  whether the current thread owns the lock, and a nested start returns a safe
  error instead of waiting for cleanup under an outer lock.
- The expanded focused set covers the real reentrant manipulation lock,
  pre-launch retry, and shared finite deadline: 95 examples, 0 failures, seed
  `31589`.
- Follow-up review found that `init_pid` can remain unset after LXC reaches
  running state because monitor state queries are allowed to fail. Inferring
  cleanup from the PID could therefore reopen the original race.
- Run configurations now persist an explicit `runtime_cleanup_required`
  marker before osctld forks the LXC wrapper. Failures before that boundary
  discard the unlaunched run configuration. The LXC pre-start callback marks
  manually launched containers, and monitor startup marks already-running
  containers loaded during an osctld upgrade or restart.
- Existing legacy run files without the marker default conservatively to
  requiring cleanup. Older versions ignore the additional key, so rolling
  updates and rollback do not require a file conversion.
- Expanded focused specs after the marker revision: 105 examples, 0 failures,
  seed `31589`.
- Final review found that setting the marker before `fork_and_switch_to` still
  covered fallible cgroup creation and `Process.fork`; those failures could
  leave a marker without any process able to fulfill cleanup.
- A later review showed that a forked child can still fail during user/cgroup
  setup or before spawning the wrapper, so a successful fork is not the
  lifecycle boundary either.
- Start now waits on a persistent in-memory runtime-start promise. The
  container's LXC pre-start callback and lxc-monitor transitions persist the
  cleanup marker and fulfill that promise only after LXC lifecycle is reached.
  An unconfirmed wrapper is terminated after 30 seconds and its unmarked run
  configuration is discarded.
- Focused coverage verifies wrapper-spawn failure, successful wrapper creation
  without an LXC lifecycle notification, and a confirmed LXC lifecycle retry.
  The final runnable focused set has 106 examples, 0 failures, seed `31589`.
- Review of `5ee07e782` found three remaining blocking races:
  - a delayed STOPPED monitor event could create and mark a spurious new run
    configuration after `ct_post_stop` had moved the real run to
    `past_run_conf`;
  - the fixed 30-second lifecycle wait ignored a shorter command deadline and
    made no-wait starts wait;
  - sending TERM without confirming wrapper exit allowed the unmarked run
    configuration to be discarded while its process group was still alive.
- Monitor events now mark only an existing active or past run. A late stopped
  event fulfills the past run's notification without recreating its already
  destroyed on-disk configuration.
- Once the wrapper PID is received, the run is a persisted cleanup barrier.
  A separate runtime-start promise records whether LXC pre-start was reached.
  Pre-wrapper failures remain immediately discardable.
- The runtime-start wait consumes the caller's remaining deadline. No-wait
  starts return without waiting on that promise and register a tracked
  background watcher instead.
- Failed wrappers receive TERM and are checked by process group. The run
  configuration is discarded and its exit promise fulfilled only when the
  group is confirmed gone and LXC lifecycle was never reported. Otherwise the
  cleanup barrier remains, and confirmation continues asynchronously when the
  command deadline has expired.
- Unexpected errors after wrapper creation also install the asynchronous
  lifecycle watcher from `ensure`, so the persisted barrier cannot be left
  without a component able to confirm runtime start or wrapper exit.
- Review of `c6dbcdc7f` found that asynchronous confirmation stopped after ten
  seconds and that a STOPPED-only event did not set the cleanup marker on an
  initially unmarked past run.
- Background termination confirmation now continues until LXC lifecycle starts
  or the wrapper process group is confirmed gone. During daemon shutdown it
  escalates the already-terminated unconfirmed wrapper to KILL and still waits
  for confirmation, so shutdown does not silently orphan the barrier.
- A delayed STOPPED/ABORTED event sets the past run's cleanup marker in memory
  before fulfilling its runtime-start promise. The managed-start parent uses a
  container-serialized marker method, so it also avoids recreating a run file
  if `ct.stopped` won the race.
- Focused specs after these revisions: 111 examples, 0 failures, seed `31589`.
- The Nixfmt and RuboCop pre-commit hooks pass for amended commit `464db8b01`.
- Mandatory follow-up review of `fc6c9fe6..a2665f394` reports no remaining
  Blocking, Important, or Advisory findings. The reviewer confirmed the
  indefinite process-group confirmation, shutdown escalation, active-to-past
  serialization, in-memory past-run barrier, and all earlier fixes.
- Residual review risks are intentionally assigned to the gated VM test: the
  real lxc-monitor path, the reboot/start overlap, and real process-group
  timing. The complete local osctld suite remains unavailable because
  `ruby-lxc` cannot load in the generic shell.
- First VM attempt:
  `./test-runner.sh test osctl/ct-console` failed only in the new overlap
  example after the first five examples passed. The runner retained artifacts
  in `/tmp/os-test-runner/os-test-osctl__ct-console-bdf3027c`.
- The failure occurred before exercising the fix. The custom Nix-store LXC
  post-stop hook exited with status 127, which prevented the internal
  `ct-post-stop` hook from running; osctld logged `Unable to properly handle
  container stop`, and the test timed out waiting for the custom sentinel.
- The regression setup now uses the supported per-container `post-stop` hook
  under `/tank/hook/ct/<ctid>/`. It delays `ct_post_stop` after `ct.stopped`
  without replacing or breaking osctld's internal LXC post-stop hook chain.
- The second VM attempt reached the delayed user hook, but the overlap example
  timed out waiting for the exact cleanup-wait progress message. The container
  had been stopped using `osctl ct restart --reboot`; its test init traps the
  signal and exits normally, so LXC did not report a reboot target and osctld
  did not log `Reboot requested`. In addition, the user `post-stop` hook runs
  after `ct.stopped` and is asynchronous, so it is not a cleanup barrier.
- The VM fixture is being corrected to invoke `/sbin/reboot -f` inside the
  container and delay LXC's post-stop hook chain before osctld's internal
  `ct-post-stop`. The hook uses an absolute Nix-store `sleep` path because LXC's
  sanitized hook environment caused the first raw hook to exit with status 127.
- The third VM attempt confirmed `/sbin/reboot -f` stopped the container, but
  LXC again returned status 127 before the Nix-store delay hook created its
  sentinel. The internal `ct-post-stop` hook therefore did not run and osctld
  reported an improper stop; the overlap example timed out before starting the
  external command. The final cleanup exposed the expected unfulfilled exit
  promise from this broken fixture.
- The delay hook is now a one-shot wrapper stored beside osctld's own hook
  under `/run/osctl/pools/tank/hooks/`. It uses only shell builtins, waits on a
  FIFO, and then executes the real `ct-post-stop` with the original arguments
  and environment. Later stops pass through immediately.
- The fourth VM attempt showed the `/run` wrapper was launched but exited with
  status 1 before creating its sentinel. Raw LXC hooks run with the container
  root as `/`, so the wrapper could not access its host `/run/osctl` marker
  directory after launch.
- The fixture now keeps its FIFO and markers in the mounted container rootfs,
  where both the namespaced hook and host-side test can address them. The delay
  hook exits successfully after release, allowing LXC to invoke osctld's real
  `ct-post-stop` as the next configured hook.
- The fifth VM attempt again returned hook status 1 before creating the rootfs
  sentinel. LXC's documented semantics and the status sequence show that
  `post-stop` is host-namespaced but runs as the container's unprivileged host
  user. The earlier `/run` fixture failed because its marker directory was mode
  0755 and writable only by root; the rootfs path also had non-traversable
  parent ownership.
- The dedicated `/run/osctl` delay directory is now mode 0777. The test hook
  still uses only shell builtins, and no shared osctld hook path or production
  configuration is made writable.
- `monitor/process_spec.rb` cannot load in the generic development shell
  because it imports the unavailable Ruby LXC native extension. Its added
  marker assertion is therefore deferred to the VM test together with the
  real lxc-monitor path.
- RuboCop found no offenses in the changed Ruby files.
- The repository Nixfmt and RuboCop pre-commit hooks pass.
- The first commit attempt from the ambient shell was correctly rejected
  because Nixfmt and RuboCop were not on `PATH`. The same commit was rerun
  inside the repository's Nix development environment; all pre-commit and
  commit-message hooks ran, and the commit succeeded without bypassing hooks.
- The test runner resolves the VM test as `osctl/ct-console`.
- The complete osctld spec load is not available in the generic development
  shell because the Ruby LXC native extension cannot be loaded. It stopped
  during spec loading with eight `cannot load such file -- lxc/lxc` errors and
  ran no examples. The affected focused specs do not require that extension and
  pass.
- Concurrent `nix develop` bundle setup briefly raced over the worktree's
  shared `.gems` directory. The corrupt transient files were moved aside,
  dependencies were installed serially, and subsequent checks pass. The
  existing durable note
  `notes/vpsadminos/2026-06-07-parallel-nix-develop-gems.md` already documents
  this issue.
- The latest focused regression set has 173 examples and 0 failures with seed
  `31589`. It includes atomic monitor transitions, staged-state preservation,
  daemon-restart reconstruction, exact console generations, retained runtime
  cleanup, and default immediate cleanup for recovery/receive callers.
- Final focused regression set: 200 examples, 0 failures, seed `31589`.
- Final `ctptywrapper` checks: `cargo fmt --check`, 9 tests with 0 failures,
  and `nix build .#ctptywrapper --no-link`.
- Final repository hooks: Nixfmt and RuboCop passed. Commit-message hooks passed
  with only their 72-column advisory; every commit-message line is within the
  workspace's mandatory 80-column limit.

## Cleanup

- Worktree is active.
- Worktree is clean at `078afb23788a260393190c1b582b66dca76d2016`.
- `ctptywrapper/target/` was moved to
  `/tmp/ctptywrapper-target.w1qKiH/target` before committing.
- Keep the feature branch after merge; remove the worktree only after the
  initiative is complete.
