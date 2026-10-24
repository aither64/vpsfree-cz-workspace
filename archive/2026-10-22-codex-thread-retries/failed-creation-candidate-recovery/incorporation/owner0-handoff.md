# Candidate failed-creation recovery: frozen source handoff

Owner: implementer0. All six paths are complete, uncommitted and frozen. Implementer1 remains sole B Git owner; incorporation and final committed review are pending. No live recovery, receipt reconciliation, profile selection, restart, deletion, creation, build, native or deployment operation was performed for this package.

## Source and patch

Current reported B base is `fda46ca1a45c1f0a0046213448c47d80b976e032` after D1 incorporation. Baseline snapshots retained under this directory; no Git/index operations by this owner. The patch contains only the six assigned paths.

Patch: `final.patch`, SHA-256 `dc63492758a82348354b6ae66c63264f95c8c0f38734e6b8763dac47efe1756c`.

| Path | SHA-256 |
| --- | --- |
| `libexec/workspace-host` | `acf46cb6ac8b2efdb85f9328d8dc43984dd53cb1f5b23c422fc5c85148c8ef63` |
| `libexec/dev-session` | `396b42fb80a55da8dc1f99fa568197082f6f48f8fecf90c395df86cf94fa39ca` |
| `test/workspace_host/failed_creation_delete_recovery_test.rb` | `9016c87b841534f74f4d090ad9e2bcb883f92084e18c023cdb5996b38cd77a9d` |
| `test/dev_session/deletion_recovery_test.rb` | `217d2a8b8487854d62d754ead7bcebf190f8246f1cb34a7683ff4a861e6f2ffa` |
| `test/workspace_host_test.rb` | `99801431d6ba6b85c33f94e4e96dffdfc0d51aed930bdd3ecd497fbc316038ba` |
| `docs/session-archive-recovery.md` | `5cf4ea352507dadf85e6510465b446823b6ef10bace4b8c06fed25a6ee6af7f0` |

The loader adds exactly one `require_relative` for the new host fixture and otherwise preserves its order. `aggregate-discovery.json` proves all eight new topnames are found by the normal `test/run_ruby_suite.rb --list workspace_host_test.rb` aggregate/shard discovery. Scoped whitespace check passed.

## Behavior and compatibility

The public candidate host entry binds the exact built source output, selected predecessor profile token and native executable/protocol. It permits only the documented absent-to-1 or equal-1 `turnRetrySessionPolicy` contract difference. It retains transition exclusion, ordinary confirmation, capability checks and predecessor generation authority. It does not select the candidate.

The public verifier and ordinary deletion share one private typed context validating the exact failed direct request, accepted team/root, explicitly false initial-goal flags, creation nonce and subordinate start. Ordinary deletion records durable `thread_retiring` before transferring the unchanged start bytes to private recovery; the ordinary deletion journal owns completion and replay. Other operation conflicts and archive/start behavior remain strict. Unknown native member-start provenance remains retained. No schema/phase/native API migration or external state mutation.

## Final quick evidence

All commands and before/after six-path hashes are in the named JSON receipts; raw stdout/stderr are adjacent.

| Receipt | Result | Command wall time |
| --- | --- | --- |
| `final-host.json` | 8 tests, 209 assertions, 0 failure/error/skip | 17.935s |
| `final-executor.json` | 5 tests, 27 assertions, 0 failure/error/skip | 1.977s |
| `final-unchanged-guards.json` | 8 tests, 45 assertions, 0 failure/error/skip | 2.530s |
| `final-syntax-2.json` | All 5 Ruby paths syntax OK | 0.720s |

The three selected suites total 21 tests and 281 assertions. They are focused disposable evidence, not a full suite or full-system pass. The host fixture invokes the real public host, ordinary CLI confirmation/generation handling and Runner admission, locks, removal phase writers, atomic moves and completion serialization. Its terminal/native/portal external adapters are synthetic. It covers pre-phase refusal, durable-phase/move/native-retirement/tracking relocation interruptions, exact operation replay, byte preservation, request/root/roster/nonce/contract/profile/native negatives and unchanged selected generation.

Earlier failures are retained in `attempt-1-findings.md` and attempt-2 artifacts: disposable cluster adapter setup; initially missing explicit migration refusal fixed in source; and a native-turnover fixture that had selected the legitimate fallback, corrected to mutate at the lock barrier. Green attempt-3 and aggregate-focused receipts remain historical, not substitutes for the final receipts above.

## Producer/consumer reconciliation

Owner1 provisional real Ruby writer/Go receipt reader evidence is `delete-guard/receipt-consumer/handoff.json` (11 PASS tests/subtests, 23.748s). It loaded producer SHA `b2d7bd0eb5e2f54065643485e76ca3245fff0859e716f52a071dc2cb9b03e014`; the final producer SHA differs. `consumer-producer-final.delta.patch` lists the exact differences. They strengthen UUID/goal/native/roster/completed-receipt admission, add explicit conflicts, load current authority, preserve persisted force on replay and route early lifecycle admission through the same typed context. Removal/completion serialization is unchanged, but executable admission changed: no automatic final-tree reuse is claimed. Owner1/lead owns a final bounded consumer rerun or explicit source-bound disposition. The final producer is frozen for that window.

## Documentation and remaining gates

Applied the main-agent writing replacement exactly once, checked both the old section and whole-doc expected hashes. `lead-copy-applied.json` binds the approved final document SHA `5cf4ea352507dadf85e6510465b446823b6ef10bace4b8c06fed25a6ee6af7f0`. All inventoried production errors/help/comments remain as accepted. The recovery section now explicitly requires stopping if ordinary portal reconciliation cannot prove deletion, before any normal switch.

Next: owner1 final consumer disposition, lead incorporation release, sole owner1 coherent recovery18 commit/publication, independent exact committed review, then only separately authorized verification or live operations. Ready replacement911b remains unchanged.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/
