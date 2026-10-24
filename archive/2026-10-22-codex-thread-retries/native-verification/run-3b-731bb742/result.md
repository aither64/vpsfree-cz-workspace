# Corrected native verification run 3b

Result: failed (raw)

- Script: `bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-codex-thread-retries/native-b-corrected-command.sh` (invoked once)
- Exit: 1; elapsed: 14.508928415 seconds
- Tested HEAD: `731bb742e07b4374cb8ee9a3a1379eb751cf44c4`
- Tree: `67a58609dd374702984ae871b47e08977ca9abf8`
- Actual test cwd: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries/dev-workspace/portal`
- Native version: `codex-cli 0.163.0`
- Full binary identity hashes: see `binary-identity.txt` (CLI SHA-256 `dd356114c45b6b78617be9da9c21ab6d284a8d3c7de1e5a39abf45be2cabed8b`; libexec SHA-256 `5e538cfe7c25daf382afe195c08b2ffd24415b0cdd7f5456ec0cf1d277c3d1a5`)
- Exact requested cases: `TestNativeLiveSwitchReconnect` PASS; `TestNativeTurnRetryController` FAIL. No skips reported. The controller test has no named subcases.
- Full runtime JSON: `runtime.jsonl`; stderr: `runtime.stderr`; process exit: `runtime.exit`; elapsed: `runtime.elapsed`; source/cwd/tree/version evidence: `head.txt`, `cwd.txt`, `tree.txt`, `binary-identity.txt`.
- Bounded failure evidence: controller emitted `portal requires an HTTPS base URL` at `turn_retry_native_integration_test.go:260`, then `--- FAIL: TestNativeTurnRetryController (1.30s)`. Earlier output included a terminal capacity failure (`serverOverloaded`, “Selected model is at capacity. Please try a different model.”), native barrier accepted, uncertain dispatch reconciliation, and successful native continuation completion. Live switch test passed (2.87s), reporting preserved native PID 1751027 and completed active turns, queue/report retries, approval and question.
- Script/runtime completion is recorded; no still-running operation is indicated by the completed invocation.
- Launch policy supplied: explicit `danger-full-access` / approval `never`.
