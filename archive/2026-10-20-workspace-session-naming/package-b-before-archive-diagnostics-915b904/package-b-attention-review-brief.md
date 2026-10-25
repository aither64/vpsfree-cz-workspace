# Narrow browser fixture readiness follow-up

Status: exact prepared patch applied after the watcher settled and lead released
source edits. Quick checks passed; separate commit
`915b904101eca8170652a8dd198f63e3e3aae967` published normally over SSH.
Affected general/architecture review remains lead-owned; source is frozen again.

Exact review range:
`4c6b9f177d5b205b21b45880c6ac1bc3c403eef6..915b904101eca8170652a8dd198f63e3e3aae967`.
Checked/final tree: `08b9b08afbbddb3b486e8a8103028c986de96244`.
Targeted check passed 1/1, 224.663 ms total; whole-file check passed 71/71,
7.960 seconds. Logs: `package-b-attention-targeted.log`,
`package-b-attention-whole-file.log`; exact delta:
`package-b-attention-final.diff`; identity/result: `package-b-attention-result.json`.
Normal SSH publication proof: `package-b-attention-publication.log`.
The original pair remains unchanged; one logical pin stream and no migrations.

Repository/worktree: `worktrees/2026-10-20-workspace-session-naming/dev-workspace`.
Current exact base for the standalone follow-up commit:
`4c6b9f177d5b205b21b45880c6ac1bc3c403eef6`.
A client pin remains `4300c40b6406161afc74c124c40155f28a557032`.

Only source path: `portal/internal/web/attention_browser_test.cjs`, existing
single test at line 1611, “Disable fences a delayed old Enable across tabs before
local storage or unsubscribe side effects”. Prepared patch:
`package-b-attention-readiness.patch`.

The existing callbacks resolve a stage-reached Promise only after assigning
`release`. The test races that signal with Enable completion, preserving the
existing `typeof release` assertion so an early completed action fails. The
five-second Node test timeout bounds a stalled fixture without an iteration
assumption. All original production crypto, permission/registration stages,
shared state, Disable actions, storage/subscription and fencing assertions
remain unchanged. No production code, public protocol, user prose, pin, lock,
Nix hash or persisted data changes.

Failure evidence: `package-b-current-fast-failed.log` (original full job),
`package-b-current-fast-sanitized.log`, `package-b-current-fast-excerpt.log`,
`package-b-current-fast-artifacts.json` (zero artifacts), and
`package-b-current-fast-diagnosis.{md,json}`. The diagnosis distinguishes the
proven setup-readiness failure from inferred asynchronous crypto latency.

Executed known-quick checks in repository Nix:

```
node --test --test-name-pattern='^Disable fences a delayed old Enable across tabs before local storage or unsubscribe side effects$' portal/internal/web/attention_browser_test.cjs
node --test portal/internal/web/attention_browser_test.cjs
```

The second command covered all existing notification contracts in the same file;
no package build, CI rerun or integration/model call is part of these checks.
Use ordinary declared hooks and a temporary commit message. Keep one separate
focused owning test commit after the existing dependency-first/functional pair.
Lead assigns the retained reviewer general/architecture lanes on the committed
fix plus quick evidence before authorizing long verification. C waits for that
final corrected reviewed B head. No merge/deployment/lifecycle authority implied.
