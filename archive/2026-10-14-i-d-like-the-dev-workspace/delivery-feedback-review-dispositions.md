# Delivery feedback review dispositions

Status: all three findings fixed; direct lead verification complete.
Authorized finite verification may proceed at exact5a07708e.

Review: [delivery-feedback-review.md](delivery-feedback-review.md), retained
reviewer0, saved GPT-6.1 Sol/xhigh/read_only, all four lanes, high risk.
Reviewed affected range `867682c3..a5e41580`; complete own range `832d9f1..a5e41580`.

1. Important, failed new Test retains an older check: fix. Retire the previous
   descriptor before sending the new request; failed/lost replies remain unknown
   and cannot resume or display the retired test as their result. Cover late A
   outcomes after rejected/lost B replies.
2. Important, stale tab deletes newer pending descriptor: fix. Cancellation
   compares all four descriptor fields within the existing shared transaction.
   Cover A cancellation after B is persisted and B resumption after reopen.
3. Advisory, delayed resume overwrites a new/canceled check: fix. Snapshot and
   recheck existing invalidation generation, registration, page state and absence
   of a newer pending check after the awaited read. Cover deferred read races.

Implementer0 is assigned the exact narrow recommendations in the existing client
and owning actual-module contracts. Preserve reviewed heads/packets under session
refs, amend the unpublished fifth owning commit and replay the unchanged sixth
status deletion. Keep the first four objects and consumed6e1 intact.

The lead will inspect the exact delta and focused results under mandatory review
steps 9–10. A confirmation-only reviewer rerun is unnecessary for the requested
narrow fixes; a new design or boundary would require affected review. No server,
API, schema, dependency, cleanup, visible-copy or native-flow expansion is needed.

Remediation implementation milestone: the new explicit Test waits for bounded,
exact-matching retirement before submitting another request. A per-document
retirement flag prevents resuming an old check after a failed/timed-out deletion.
If local persistence cannot delete A, no B request is submitted. Durable deletion
across an entirely new document cannot be promised after that failed write;
this limitation does not fabricate a submitted B. Normal rejected/lost B replies
occur only after A's persisted descriptor was retired. No tombstone, new field
or schema expansion is introduced. Final tests/freeze and lead verification
remain pending.

Existing a5 wrappers/native bundle remain unrun and bound to their old revision.
Prepare new revision-specific execution evidence after the amended head is frozen.
No root cause for physical Firefox/macOS non-display is established.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-i-d-like-the-dev-workspace/

## Final narrow-remedy verification

Final head: `5a07708ea80a2649265c3ef268b8379daaec47bb`.
Amended fifth: `50fba34d44e0c36c2bddf25f16fee53553cd3033`.
The six logical commits remain; first four objects and the sixth status-deletion
patch are unchanged. Reviewed a5/43c are preserved under session evidence refs.
The exact a5-to-final remedy changes only the client and owning Node contracts,
SHA256 `0885fd0c7de75a068a5a144e712c2c4b9239779d66cd9e7ed3233defe3410bd5`.

Lead inspected full descriptor compare-delete, retirement-before-send,
post-await generation/registration/page/busy/pending checks and the per-document
retirement guard. Added contracts exercise rejected/lost replies with late old
results, stale-tab cancellation and reopen, delayed resume/new-test/cancellation,
and deferred/failed/timed-out retirement. No new persisted field, abstraction,
public contract or visible wording was introduced by the remedy.

Direct exact-head lead run under declared Node24.19.0 passed26 named tests,
fail/cancel/skip0, exit0, duration1922.799774ms. NODE_OPTIONS and NODE_TEST_CONTEXT
were absent. Evidence: delivery-feedback-amended-lead-node.log/status and
-environment.txt. Member changed syntax/diff passed. Lead independently verified
cleanHEAD/tree, six-commit series, unchanged first four/sixth patch, frozen remedy
and whole-branch patches, and changed blob hashes.

Mandatory review steps9–10 are satisfied for the exact recommended remedies;
no confirmation-only reviewer rerun is needed. Earlier unaffected review/history/
migration conclusions remain within their exact boundaries. This does not claim
browser/package verification or deployment success, and does not explain the
Firefox/macOS non-display cause. Downstream composition is still pending.
