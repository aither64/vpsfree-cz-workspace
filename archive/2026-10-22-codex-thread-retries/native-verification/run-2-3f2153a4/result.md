# Native verification run 2

- Result: failed/incomplete; both selected commands ran once and exited 1.
- Session: 2026-10-22-codex-thread-retries; workspace `/home/aither/workspace/ai/vpsfree.cz`.
- A `codex-web`: `b6d3a92ff85edbcd661b193c2319951eb4a71725`, clean before execution.
- B `dev-workspace`: `3f2153a44e87bcd60c40ac5dcc660f214ccf04fa`, clean before execution.
- Native: `codex-cli 0.163.0`; wrapper SHA256 `dd356114c45b6b78617be9da9c21ab6d284a8d3c7de1e5a39abf45be2cabed8b`; underlying binary SHA256 `5e538cfe7c25daf382afe1956ec0cf1d277c3d1a5`.

## A library command

- Exit 1; elapsed 28 seconds. Full JSON: `library.jsonl`; stderr: `library.stderr`.
- Passed: `TestPinnedCodexRecoveryRemainsColdUntilActivation` (13.86s).
- Failed: `TestPinnedCodexFailedTurnRetryContract/nonempty_continuation_default`; parent failed. Failure excerpt: `continuation_integration_test.go:284: Codex RPC -32600: no rollout found for thread id 01a16495-e845-73f1-8218-7fc3ed5086e9`.
- It emitted `test executed panic(nil) or runtime.Goexit: subtest may have called FailNow on a parent test`; native private log warned it could not create PATH aliases under `/tmp`.
- Required remaining A subcases absent: nonempty_continuation_plan, exact_cyber_terminal, automatic_queue_uses_execution_context, lost_accepted_reply_recreated_client, native_direct_busy_race_compatibility.

## B runtime command

- Exit 1; elapsed 95 seconds. Full JSON: `runtime.jsonl`; stderr: `runtime.stderr`.
- Passed: `TestNativeLiveSwitchReconnect` (2.95s).
- Failed: `TestNativeTurnRetryController` (90.21s). Failure excerpt: `turn_retry_native_integration_test.go:165: loaded idle retry source: context deadline exceeded`; native private log warned it could not create PATH aliases under `/tmp`.
- No required retry controller scenario passed or was reported. It exceeded its own 90s scenario context; package command completed normally with exit 1.

No owned processes remain. Both prescribed commands were run once; no retries or cleanup were performed. The result directory is mode 0700.
