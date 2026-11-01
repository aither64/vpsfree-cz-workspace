**Important — propagate startup cancellation through attachment reconciliation.** General/risk lanes; commit `496ae1b4`; [preparation.go:925](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-25-archive-unmanaged-files-investigation/dev-workspace/portal/internal/web/preparation.go:925).

`NewContext` now supplies the signal context to preparation reconciliation. If SIGTERM arrives after transition admission while `ClaimPreparation` waits for the upload catalog lock, the store returns `context.Canceled`. Reconciliation treats that as an ownership failure, persists `failed` with “Accepted attachment ownership changed,” then continues and can return success. `NewContext` can consequently start workers on its independent, uncanceled operational context.

This path follows directly from the inspected error handling; the passing tests do not reproduce it. Return cancellation/deadline errors before translating attachment errors into persisted failures, and check startup cancellation before launching background workers. Add a focused regression that cancels during the preparation attachment claim, verifies the accepted record is preserved, and requires constructor cancellation.

This finding requires a fix or explicit recorded decision before proceeding under the mandatory review workflow.

The demonstrated transition-wait correction otherwise looks sound. `serve` passes its signal context to initialization and suppresses only an error wrapping that canceled context. `New` preserves its background-context behavior. Operational workers remain independent, and `Close` retains park-before-cancel ordering. Constructor errors before worker launch cancel the unused operational context; later failure uses `Close`, while outer defers retain owned-child cleanup.

The baseline reproduction is meaningful: the actual subprocess opens the parent-owned transition inode, receives SIGTERM while EX remains held, and its failure stack identifies `New → reconcilePreparations → acquireTransitionContext`. Observing the child descriptor before signaling avoids testing an earlier startup phase. This establishes the startup wait defect, **not the exact historical VM timeout execution**.

Independent quick verification passed on committed `496ae1b4`:

- Command startup/owned-child tests: **0.310 seconds**, including real SIGTERM cancellation.
- Worker lifetime, transition cancellation, archive drain and preparation-confirmation tests: **0.255 seconds**.
- Full-range whitespace check; worktree remained clean.

Reviewed the complete range `b974f2f3f83792a494610d1ea03f3d69e97bc1a4..496ae1b4debe0d244118d010d13c0d6ce66e12f2`, retaining the prior assessments of unchanged commits:

1. `2a58cf49` — worktree reader contention.
2. `b75a6a10` — native fixture correction.
3. `78077b0e` — equivalent-refresh retry guard.
4. `496ae1b4` — startup cancellation.

**No obsolete unmerged approaches or redundant fixup history remain. No repeated dependency/input/generated-update streams exist. No migrations or transitional migrations.** Earlier merged/deployed history remains preserved.

Final-head packaged verification and replacement consumer pins remain outstanding. Artifacts for `78077b0e` establish evidence only for that revision. This report grants no approval and establishes neither final CI nor deployment completion.

Performed directly and read-only under the retained `gpt-6.1-sol` / `xhigh` assignment, without nested agents, edits, long checks, integration or deployment.