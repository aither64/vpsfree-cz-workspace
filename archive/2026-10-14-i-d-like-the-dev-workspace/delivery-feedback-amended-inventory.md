# Delivery feedback narrow review remediation: frozen amended source

Final clean head `5a07708ea80a2649265c3ef268b8379daaec47bb`.
Amended fifth delivery `50fba34d44e0c36c2bddf25f16fee53553cd3033`;
unchanged sixth patch replayed as `5a07708ea80a2649265c3ef268b8379daaec47bb`.
First four commit objects, including UI867 and consumed6e1, are unchanged.
The branch still contains exactly six logical commits over832d9f1.
HOLD publication/pins/long/browser/provider operations for direct lead verification.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-i-d-like-the-dev-workspace/>

## Accepted findings and exact remedies

The lead accepted all three reviewer0 findings for mandatory-review9/10 narrow
direct verification. Only browser-notifications.js and its owning actual-module
CJS contracts changed (131 insertions/7 deletions). No design, public API, server
state, browser persistence, worker, copy, docs, transport or cleanup boundary
changed.

1. A new explicit Test invalidates the old check immediately. It awaits bounded
   exact saved-descriptor retirement before issuing /test. Unsuccessful or
   uncertain retirement does not issue a new request; a failed/lost new reply
   retains the already-approved unavailable/unconfirmed result. Late old worker
   messages/outcomes cannot advance that result or restart the retired check.
2. cancelTest captures the complete descriptor. Its shared transaction deletes
   testPending only if identity/id/revision/expiry all still match, preserving
   another document's newer descriptor. Enable/Disable never wait on diagnostic
   storage, so compensation/subscription cleanup remain independent.
3. resumeTest snapshots generation and registration identity before await, then
   rechecks them, registered/busy/pageClosed state, retirement state and absence
   of a newer pending descriptor before assigning. A delayed read cannot undo
   new-test/cancellation/replacement/pagehide invalidation.

One per-document retirement flag prevents later visible/pageshow refresh from
reloading the old saved descriptor when retirement is still pending or failed.
There is no new persisted tombstone. If storage permanently refuses deletion,
the current document stays unknown and no new request is sent. A full new
page may still see the old saved check because cancellation was not durable;
no durable cancellation is claimed after failed persistence. This limitation was
reported to the lead rather than hidden behind a new schema. Normal rejected or
lost new replies occur only after old-descriptor retirement succeeds, so the
retired check cannot auto-resume after a normal reload.

## Focused verification

Declared cached runtime environment, Node24.19.0. No daemon/network/browser/Go or
unchanged live check was run. New delivery-feedback-amended-node, syntax-client,
syntax-contract and diff log/status files preserve exact commands and output:

- node portal/internal/web/attention_browser_test.cjs: 26 named PASS, 0 failures
  or skips, command2.049s. Original22contracts remain plus four review contracts.
- node --check for changed client and CJS: PASS.
- git diff --check: PASS.

New contracts cover A pending -> rejected/lost B reply -> late A outcome/message,
no auto-resume of retired A, shared two-document cancellation/reopen, each of the
four descriptor fields, deferred resume versus new B/Disable/pagehide/identity
replacement, and deferred/failed/timed-out retirement with no premature B send.
Tests ran before consolidation against the identical final source tree:
`381f514f59f6b24e3552166f47360746b07c133f`. Rebase final tree equality was asserted.
No unchanged Go, browser, provider or native test was rerun. Physical Firefox/
macOS cause remains unproved.

## History, references and immutable evidence

Reviewed original objects were retained BEFORE rewrite:

- refs/session-evidence/2026-10-14-i-d-like-the-dev-workspace/delivery-feedback/reviewed-final-a5e41580 -> `a5e41580d6dbeae9cbb468c707c22106f159066c`.
- refs/session-evidence/2026-10-14-i-d-like-the-dev-workspace/delivery-feedback/reviewed-delivery-43c6461e -> `43c6461e3f5ce900f72df7b2aa9593584884b04e`.

The two-file remediation was committed with normal hooks/body-file, then folded
into the unpublished fifth owning commit through autosquash. The unchanged sixth
status-row deletion was replayed without conflict. Original fifth message and
compatibility rationale were retained. No obsolete fixup remains in the final
six-commit series; the transient tree proof is in consolidation.json. Original
source/pins/UI/deployed objects and old packets remain available.

Artifacts under NEW delivery-feedback-amended-* names:

- reviewed-refs.json, consolidation.json and freeze.json;
- recommendation.patch/stat and final-delta.patch/stat (asserted byte-identical);
- owning-delivery.patch/stat, sixth-unchanged.patch (asserted byte-identical to
  original43c..a5), final series, range-diff, whole-branch.patch/stat;
- per-check logs/status/quick-results, normal fixup message/commit/rebase logs;
- preserved.sha256 and preservation-result.json; artifacts.sha256.

The preservation baseline covered67prior tracking/native files. Exactly one
file, delivery-feedback-review-dispositions.md, changed concurrently after
capture. The lead confirmed it is mutable lead-owned reconciliation, updated
by the lead to record failed-retirement semantics, not a sealed artifact.
The implementer did not write it. Baseline and expected/current digests remain
preserved. The other66recorded files matched, including all original owned
packets and all16files of live-native-a5e41580. No old native bundle is retargeted,
overwritten or run; it remains exact-a5 UNRUN and is not acceptance evidence for
this amended head. Await lead assignment before preparing a new native bundle.

## Complete source and persistent lineage

Final series: feature96717cde, providerbb9e6291, processgroup6e1d9a19, UI867682c3,
amended delivery50fba34d, replayed status-row5a07708e. The first four object
identities are unchanged. Full series/diff/stat and range-diff are retained for
whole-history inspection. No repeated dependency/pin stream or migration was
introduced.

The narrow remedy adds no API/format/persistence field. Previously reviewed
/test additive descriptor and optional IDBv1testPending/testOutcome stay intact.
Server private notificationv1, existing receipt/helper forward-only pairing,
subscription cleanup obligations, source/vendorHash dependencies and protected
upstream capability-journal lineage remain exactly as documented in the original
inventory. There is no migration rewrite or newly consumed state. Original
provider/processgroup and physical Firefox/macOS causes remain unproved.

No source publication, merge, pin, host, queue, reservation, lifecycle, provider,
SSH/HTTPS, credential, display or browser operation occurred. Session/env and
saved ready workspace_write roster17 were reverified; applicable guidance and
mandatory-change-review9/10 were read/reused. No new visible copy or doc change
requires another writing pass. Lead owns direct narrow verification, state and
artifacts, publication, final pins and finite post-review execution.
