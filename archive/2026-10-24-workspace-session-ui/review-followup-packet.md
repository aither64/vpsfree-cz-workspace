# Focused recovery design and final-history follow-up

Original reviewed base/head and report retained in `review.md`, `final.diff`,
`final-history.txt`, `review-packet.md`. No independent review of half-completed
changes requested: all intended corrections committed, quick checks pass, clean
worktree/index at final head `07d41aac2663f6e7079618da6d81bc9474af95ad`.
Base remains `b3a6eb2fc0b41cf0cb965bf4c39991815d9df734`.

[Exact remediation diff](review-remediation.diff),
[complete refreshed diff](refreshed-final.diff),
[old/new whole-series range-diff](review-range-diff.txt).

## Findings and boundary

Lead accepts original R1/R2/R3. R1/R2 are direct requested narrow repairs,
inspected with regressions under skill step9, not a blanket repair-confirmation
rerun. In-memory retry uncertainty remains unknown on failed detach. Ordered
replacement handles original removal failure and rolls back/verifies before
retiring fresh identity. Storage unable to prove/complete rollback retains
recovery records rather than discarding intent.

R3 adds a bounded recovery design from architect `design.md` section
Final-review disposition R3: finite exact status/text responses at pinned
pre-native validation, tab-owned first-dispatch provenance in memory, no unknown/
restored ID classification and no generic 4xx. A failed-head-only replacement
uses main composer snapshot with new ID, original action/position, current ready
attachment IDs; detach only after durable replacement, and retain draft on
failure. No second uploader, server/shared-provider/API/protocol change.

This focused rerun is required because R3 changes recovery behavior beyond the
original reviewed boundary. Assess applicable general, architecture/scope and
risk concerns of that changed design and interactions with direct R1/R2 fixes.
Do not re-review unrelated settings/unread/queue code merely because hashes
changed. Explicitly conclude final whole-branch history/migration/stream gate.

## Complete final series and provenance

1. `439e33a596ab334c539271cb7ebac9e508acb564` settings unchanged.
2. `4b3817f4f39e73e6012a5b3a57f7c61769a48b03` unread unchanged.
3. `a269c6227eba1a1e06bc6d362de60a42a22c9607` composer, replaces original
   `74a55c8b`; direct review repairs/R3/test folded into initial owning commit.
4. `45b12ebd86c950a3f1521a6e2da0888b6c89a908` quiet queue, patch-equivalent to
   `dedf61d8` after rebase.
5. `07d41aac2663f6e7079618da6d81bc9474af95ad` guide, original plus lead-approved
   recovery paragraph. Replaces original `5293cf5b`.

Unpublished branch autosquashed temporary fixes only. No default/published
history rewritten; complete final tree equals pre-rebase intended tree
`e1444e278ad761b5ce9495a97a86341501c85579`. No obsolete fixups, repeated dependency/
generated streams or migrations. No branch feature ever deployed/released.

## Verification before this assignment

Post-consolidation repository Nix quick checks pass: app.js and composer live
browser script syntax; composer_handoff_contract_test.cjs,
submission_notice_contract_test.cjs, paging_browser_test.cjs; range diff-check.
Focused R1/R2 cases: recovered send/queue detach failure+reload, ordered-write/
readback/revised-record write/removal false/removal-side-effect faults; exactly
old original record after compensated failures; confirmed save retry no HTTP.
R3 table: all ten status/text pairs Send/Queue, wrong status/text/missing status,
generic400/postqueue503, restored waiting retry:false, lost-response retry,
failed-state persistence, main-composer text/file replacement+detach rollback.

Fresh managed Luna/low watcher `validation_unit_watch` ran real handler/backend
Go prerequisites (33 subtests), exit0, 25s wall, package2.966s. Logs
`validation-unit.log`/`.exit`, Go source SHA256
`5071e7331bdbc56b5d8a86ce10e15eac25c5be06a0756d8a166c58efe843cbbc`, matches final
committed source. Exact command:
`nix develop --command go -C portal test -mod=readonly ./internal/web -run '^TestSubmission(ValidationBeforeNativeDispatch|FailureAfterNativeDispatch)$' -count=1 -timeout=60s`.

Authored real-browser recovery cases remain syntax-only until review passes;
prepared longer commands in verification-plan.md / verify-local.sh. Native
multi-steer execution order remains unproven, no broadened promise. Lead directly
applied required user-facing writing to receipt guidance and guide paragraph.
No integration/deployment approval. Reviewer same retained reviewer0 Sol/xhigh,
read-only; no nested reviewer/fallback/effort override. Return concrete findings
and final conclusions by message for lead to preserve.
