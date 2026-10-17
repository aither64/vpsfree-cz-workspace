# Independent final review packet

Read workspace AGENTS.md and applicable procedures, repository AGENTS.md and
~/.codex/skills/mandatory-change-review/SKILL.md with all four lane references.
Read-only review; do not delegate or edit code. Report General, Architecture,
Scope and Risk conclusions distinctly. Trusted operator boundary is defined by
repository AGENTS.md; remote input remains untrusted.

Request: fix proven supervised archive authorization failure and add a real
packaged browser/worker archive/revive release gate. User explicitly chose this
bounded approach over redesign. Plan/state/design in this directory are context.

Repository worktree: worktrees/2026-10-17-archive-worker-authorization/dev-workspace
Base: 27ffc68 (remote master at initiative start).
Head: 174281a. Complete series:
- a54100f archive: authorize receipt-bound background workers
- 174281a test: gate releases on packaged browser archive recovery

Inventory: no migrations or persistent format changes, no obsolete intermediate
approaches or repeated dependency streams. Existing schema/readers unchanged.
Two logical commits separate production dispatch+regressions from VM/CI gate.
The new workflow uses upstream verified checkout v7.0.1 and install-nix-action
v31.11.2; existing unrelated jobs remain pinned as before.

Quick evidence: positive CLI regression failed against original dispatch; fixed
focused Ruby 4 tests/66 assertions passed; focused existing Go worker/command
tests passed; Ruby/Node/Nix syntax and git whitespace passed; VM drv evaluates.
Long integration/package checks have not started and follow this review.

Compatibility: provider is generic dev-workspace; consumers discovered in
workspace flake.nix nested vpsfree-dev-workspace/dev-workspace override and
configuration devWorkspace channel. Those later pin changes are mechanical and
must select final published runtime consistently. No API/CLI/schema changes.
No fleet update. Preserve failed portal receipt for normal Retry after deployed
disposable smoke acceptance. Do not merge defaults without separate approval.

Project docs updated: README verification entry and session-archive-recovery
authorization contract/retry guidance. Runtime recovery mechanisms deliberately
remain unchanged. New VM uses real package/native services without model turns;
systemd pre-exec barrier and archive-root permission failure inject real faults.
Check those fixtures, selection and eventual completion assertions carefully.

High risk classification: authorization and destructive lifecycle execution.
No roster exists (threadless initiative); use installed catalog fallback,
review-purpose role reviewer, GPT-6 Astra/xhigh, catalog digest
437585347ac8b2cdbf498a169d8871e684f3f61ccf1dd48e8589d79ef9629abd.

Return findings with severity/file-line, explicit complete-history and migration
conclusion, repeated-stream conclusion, and residual test/rollout limits. Future
consumer pins do not change runtime code and remain separately inventoried.
