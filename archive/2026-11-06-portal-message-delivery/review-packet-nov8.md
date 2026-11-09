# Final review after baseline refresh and queue recovery

User scope: implement portal delivery fix, deploy aitherdev through configuration,
verify then merge. Latest direction explicitly asks to resolve the stale queue
and improve the process behind the arbitrary packed-ref limit. Also warned that
workspace has moved; refreshed all three branches. Threadless session
2026-11-06-portal-message-delivery has no valid retained roster. Prior reviewer
/root/final_review is no longer available in native agent listing; fresh standalone
gpt-6.1-sol/xhigh uses installed default delegated reviewer policy.

Read root/repository AGENTS and mandatory-change-review with all four references.
Risk high: original SQLite persisted-state migration and delivery admission;
new packed-ref scanner protects exact machine source checks under ledger lock.
Local operator trusted per repo AGENTS; do not design against hostile operator.

## Revisions and complete series

Runtime worktree: worktrees/2026-11-06-portal-message-delivery/dev-workspace.
Base 32a5e31bc32362b436ccc0cfc45b5d1b74f64cb6; final head
849bfdda6e1598b1e169e22bd741079941bb2d60. Complete series:
- c96503ea15eb571b3aa8cfbeee08ebbc7ed40a6b delivery/storage
- 387448e442b5fc37ec3d02b636dbe660cc086a77 interruption
- 849bfdda6e1598b1e169e22bd741079941bb2d60 packed refs

Workspace worktree: same group /workspace. Base
8aae9bd4af090260a92ec0296472fadce13c6cd7; one final runtime pin commit HEAD.
Configuration worktree: same group /vpsfree-cz-configuration. Base
1072f89f932ad570fb6d14007387d230549ccd14; one confctl runtime pin commit HEAD.
Resolve exact companion HEADs with Git and include them in your report.
Both select runtime 849bfdda; extension/native Codex and sibling inputs preserved.
Pins mechanically regenerated on current baselines, with superseded initial pins
dropped, not retained as repeated updates. No new pin migrations.

Review whole base-to-head branch/history plus final diff. Prior review.md covers
original two logical commits; R1/R2 remediations and full successful evidence
are in state.md. rebase-nov8.diff compares old final 59d2fe18 with new range.
Focus changed assessment on upstream integration and packed refs, while retaining
explicit whole-branch history and migration conclusion.

Upstream runtime already installed at c8edcb90 is tree-equivalent to new master
32a5e31b except a creation-browser test diagnostic change. New changes preserve
upstream maintenance suppression before Interrupt, managed delivery timing, and
resumable descending native history discovery. Removed stale ErrSnapshotCapacity
diagnostic and adapted mature-history fixtures to retained async evidence.
Explicit context cancellation after durable manual-retry cancellation prevents
new capture for canceled requests. Optional receipt failures remain non-fatal.

## Migration/provenance and constraints

Original direct JSON schemas 1/2 -> schema-3 marker + SQLite only. Neither old
nor current feature migration has been merged, deployed, released or externally
consumed. No intermediate schema. Keep supported interrupted recovery, completed
missing DB refusal and compatible forward recovery. Native ledger/policy unchanged.
Packed-ref fix has no persisted schema or logical resource identity change.
Queue was canceled normally (owned waiting request only); no resources held.
No live session test messages, state rewrites, reservation bypasses or retained
ref deletion. Recreating current own config branch gives predecessor a loose
ref it can resolve; deployment uses ordinary acquired machine ownership.

Packed refs: 933490 bytes, 4346 refs including 3422 archive refs, exceeded actual
MAX_REQUEST=262144. Scan bounded chunks sized to wanted line; exact match only,
long unrelated line chunks ignored, loose ref precedence retained. Tests cover
queued grant with 5000 refs, long lines, suffix lookalike, unchanged read-only
verify, source-ref change refusal. Guide documents checking scheduler logs when
waiting has no holder; no new diagnostic persistence or UI state machine.

## Evidence and docs

Quick checks passed before review: machine_identity_test.rb (25 tests, 257
assertions, 25.9 s; packed-refs-quick.log), focused Go delivery/maintenance/
resumable-history/interrupt/storage tests (18.136 s + 7.290 s;
rebased-delivery-final.log), diff whitespace and deployment contract.
Earlier compilation failed on stale upstream ErrSnapshotCapacity diagnostic;
removed. Later old fixture assertions were corrected as above; exact failures
retained in rebased-delivery-retry.log. New broad checks await this review.
Configuration hooks passed. Runtime/workspace declare no hook framework.
Docs: docs/turn-retry-recovery.md, docs/workspace-portal.md and
docs/coordination-operations.md. Lead applied writing guidance.
Plan/design/state/rollout remain shared tracking; no deployment receipts in repos.

Write findings and explicit whole-history/migration/repeated-stream conclusion
to work/2026-11-06-portal-message-delivery/review-nov8.md. Read-only source review;
no tests, edits, deployment, source commits or nested agents.
