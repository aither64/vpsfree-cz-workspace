# 2026-07-04-test-runner-status

## Goal

Add periodic suite-level progress/status output to the vpsAdminOS
test-runner so long multi-hour runs show:

- tests that succeeded as expected;
- tests that failed as expected;
- tests that unexpectedly failed;
- tests that unexpectedly succeeded;
- tests currently running;
- tests still queued to run.

## Affected repositories

- `vpsadminos`
  - Worktree: `worktrees/2026-07-04-test-runner-status/vpsadminos`
  - Branch: `2026-07-04-test-runner-status`
  - Base: `origin/staging` at `495957f5ce89b1504a8959bb4dcb3ab85e951bbf`

## Approach

Proposed implementation:

1. Add a suite status interval option to the `test` command, for example
   `--status-interval <seconds>`, defaulting to a modest periodic value such
   as `300` seconds. Treat `0` as disabled so noisy environments can opt out.
2. Add a `-v`, `--verbose` switch to the `test` command. By default, hide the
   current per-test heartbeat:

   ```text
   Test 'webui' still running after ... seconds, log: ..., last output: ...
   ```

   Keep that diagnostic heartbeat available only in verbose mode. The
   heartbeat is useful for stuck-test investigation, but it should not be the
   default long-suite progress signal.
3. In `TestRunner::Executor`, add a lightweight status monitor thread, modelled
   after the existing resource monitor thread. It should wait on a condition
   variable so shutdown is immediate and does not wait for the full interval.
4. Track in-flight tests explicitly in the executor, rather than deriving that
   solely from resource-pool usage. Suggested structure: a hash keyed by test
   path containing the scheduler index, `Test` object, and start time. Update it
   when a test is reserved, and remove it when the worker finishes the test or
   aborts.
5. Build status snapshots from executor state:
   - completed results from `@results`;
   - running count from the in-flight hash;
   - remaining count from `@pending`;
   - total count from `@test_count`.
6. Reuse the existing final-summary semantics for result categories:
   - `expected_to_succeed? && successful?` => succeeded as expected;
   - `expected_to_fail? && failed?` => failed as expected;
   - `expected_to_succeed? && failed?` => unexpectedly failed;
   - `expected_to_fail? && successful?` => unexpectedly succeeded.
7. Emit one concise line, for example:

   ```text
   [2026-07-04 22:30:00 +0200] Status: 12 succeeded as expected, 1 failed as expected, 0 unexpectedly failed, 0 unexpectedly succeeded; 4 running, 83 remaining
   ```

8. Keep script/example/test result logs unchanged. The new status line answers
   the suite-level progress question, while verbose mode remains available when
   the operator wants per-test log-tail diagnostics.
9. Document the new flags in `test-runner/man/man1/test-runner.1.md`.

Locking note:

The current scheduler logs while holding `@scheduler_mutex`, and `log` takes
`@mutex`. Avoid introducing the inverse lock order. A safe pattern is to copy
`@pending.length` while holding `@scheduler_mutex`, then copy completed/running
state under `@mutex`, release both locks, and only then call `log`.

## Compatibility and deployment

The change is local to the `test-runner` CLI and Ruby gem in `vpsadminos`.
It should not change test definitions, NixOS/vpsAdminOS generated
configuration, VM state formats, API contracts, or deployed node behavior.

The default behavior will add periodic stdout lines during `test-runner test`.
This is intentionally user-visible. Existing log parsers should tolerate extra
human-readable output because the runner already prints timestamped progress
and heartbeat lines. If strict consumers exist, they can use
`--status-interval 0` under the proposed CLI.

The current 300-second per-test heartbeat will become less visible: it will be
hidden by default and restored with `-v`/`--verbose`. This changes human-facing
stdout only. Test result files, state directories, and exit behavior should not
change.

No coordinated deployment or mixed-version handling is needed. Rollback simply
removes the extra status output and CLI option.

## Testing plan

- Add focused executor specs for:
  - status summary category counts;
  - running and remaining counts while work is in progress;
  - monitor thread shutdown without waiting for the full interval;
  - disabled status interval.
- Add executor coverage that the per-test `still running` heartbeat is hidden
  by default and emitted when verbose mode is enabled.
- Add CLI command spec coverage that `--status-interval` is passed to
  `TestRunner::Executor`, and that `-v`/`--verbose` enables verbose mode.
- Update the man page for the new flags.
- Run, after implementation:
  - `nix develop .#test-runner --command bundle exec rspec test-runner/spec/test_runner/executor_spec.rb test-runner/spec/test_runner/cli/command_spec.rb`
  - `nix develop --command overcommit --run` before any commit.

The mandatory change review skill should be run after the intended code changes
are committed and the quick local verification above passes, before any long
integration test run.
