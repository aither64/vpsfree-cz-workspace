# Native verification run 4

Result: **passed**.

The released wrapper was invoked once and exited 0. Its SHA256 was
`d81583688d251d52d7d90e4df24b08b8605d1fb037a644785ce2819cfbab448a`.
No process remains running.

| Command | Exit | Elapsed | Working directory |
| --- | ---: | ---: | --- |
| A native Go package command | 0 | 34.187799386 s | `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries/codex-web` |
| B native Go package command | 0 | 7.398063191 s | `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries/dev-workspace/portal` |

Source identity recorded by the wrapper: A head
`c1f415ad5602c23e6443cced73cb59267a796f05`, tree
`7e3523236dc4500b68a008398305b2290beabcc8`; B head
`d819ad044ef7fcc7bb4a111dc7676fe251383249`, tree
`6f1f05da60b09743d3716eb1a0adf794b90cf5a3`. Both worktrees were clean at
the selected heads. Nix reported `2.34.9`; native reported `codex-cli 0.163.0`.
Wrapper SHA256:
`dd356114c45b6b78617be9da9c21ab6d284a8d3c7de1e5a39abf45be2cabed8b`.
Underlying executable SHA256:
`5e538cfe7c25daf382afe195c08b2ffd24415b0cdd7f5456ec0cf1d277c3d1a5`.

Required JSON event inventory:

| Required case | Result |
| --- | --- |
| `TestPinnedCodexRecoveryRemainsColdUntilActivation` | PASS |
| `TestPinnedCodexFailedTurnRetryContract/nonempty_continuation_default` | PASS |
| `TestPinnedCodexFailedTurnRetryContract/nonempty_continuation_plan` | PASS |
| `TestPinnedCodexFailedTurnRetryContract/exact_cyber_terminal` | PASS |
| `TestPinnedCodexFailedTurnRetryContract/automatic_queue_uses_execution_context` | PASS |
| `TestPinnedCodexFailedTurnRetryContract/lost_accepted_reply_recreated_client` | PASS |
| `TestPinnedCodexFailedTurnRetryContract/native_direct_busy_race_compatibility` | PASS |
| `TestNativeLiveSwitchReconnect` | PASS |
| `TestNativeTurnRetryController` | PASS |

No required case was skipped, failed, or missing. Full JSON, stderr and exit
artifacts are retained under `evidence/`. A's stderr contained only the Nix
warning that `system` is renamed/replaced by
`stdenv.hostPlatform.system`; B's stderr was empty.

Evidence: `evidence/library.jsonl`, `library.stderr`, `library.exit`,
`library.elapsed`, `library.cwd`; matching `runtime.*`; source heads,
trees and clean status; `binary-identity.txt`, `nix-version.txt`, and
`session.txt`.
