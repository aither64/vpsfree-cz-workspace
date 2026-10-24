# Emergency retry provenance retention review

RELEASED for independent final review. All intended B changes are committed,
quickchecked and SSH published. Source is frozen for this review.

Session: `2026-10-22-codex-thread-retries`, workspace
`/home/aither/workspace/ai/vpsfree.cz`. Worktree group:
`worktrees/2026-10-22-codex-thread-retries/`.

## Outcome and scope

Restore ordinary portal messages for a valid deployed schema1 record containing
64 accepted steers bound to one current turn. Both reported sessions hit that
shape; capture rejected entry65 before native submission. The fix remains
B-only. A stays c1f415ad5602c23e6443cced73cb59267a796f05. UI redesign is deferred.

Read the HOTFIX supplement near the top of ../design.md, ../plan.md and
../state.md. Preserve original delivery identity, generic ledger/history replay,
unknown-outcome holds and shared admission fences. Retire only positively
accepted bound provenance; preserve protected queue/pending/uncertain tuples.
Persist exact-turn Handled suppression and invalidate cached proof before
dispatch. All-protected fresh admission refuses; no cap increase, schema change,
state reset or fresh-admission omission. Already accepted result settlement may
remain blocked/settings_unproven with exact Pending/ResultTurn and keyed quota,
without derived proof; this must converge without replay after restart.

## Review selection

HIGH risk: persisted state, concurrent admission, replay and deployed recovery.
Retain reviewer0, saved gpt-6.1-sol/xhigh/read_only, no overrides or nested agents.
Applicable lanes: general, architecture, scope/proportionality, risk/compatibility.
Read the mandatory-change-review skill and all four lane references in full.
Verify live same-session identity, saved role/access and source identities.

## History and compatibility

B base bf6d4b0c49600c15e17fe71248807ef43424e932.
Actual deployed predecessor d819ad044ef7fcc7bb4a111dc7676fe251383249,
tree6f1f05da60b09743d3716eb1a0adf794b90cf5a3. Its original four commits are
7262c24e4fbe9dbf8604e73590f9b5ef3d5dce99,
b3c7187c6e26e269994433716a0ee719d0a7edf7,
aafaf4195d695c4641ce4f9342d56a1786f237c3,
d819ad044ef7fcc7bb4a111dc7676fe251383249.
The narrow hotfix is one successor behavior commit after that deployed boundary.
Preserve the deployed bundle and receipts; assess the complete base-to-final
series/final diff as well as d819-to-final delta. State explicit whole-history,
update-stream and migration conclusions. No migrations: schema1 retry state,
schema3 native ledger and A API remain unchanged. Deployed state is a real
supported predecessor, not a disposable iteration.

The B managed wrappers consume unchanged A send/reconciliation APIs. W/C own
mechanical final B selection and preserve all unrelated input edges. Their final
generated streams require graph/history inspection after publication; content
review exemption does not exempt history consolidation. No merge permission.

## Acceptance inspection

Inspect actual root/member wrappers and core/controller/proof callers. Require
regressions for deployed64/successive sends, exact UUID replay after retirement
and acknowledgement, changed identities/settings, cached proof suppression,
restart/crash/save boundaries, protected FIFO/unknown holds, all-protected refusal,
aggregate/accepted-result slots and encoded-byte limits. Confirm prospective
persistence failure precedes native calls and accepted recovery does not resend
or reset quota. The public generic503 stays conservative.

Assess owning project documentation against final behavior, including lasting
manual-only semantics and replay guarantees. Main lead supplied the exact prose
for docs/turn-retry-recovery.md after the required writing pass; owner applies it
with the source package. No visible UI changes or API expansion are intended.

## Verification after review

After findings are reconciled: fresh Luna/low utility, exact B package checks and
Ruby aggregate with full derivation/input-based reuse; targeted B native
recovery/controller against pinned0.163; exact W4/C8 checks and scoped
system/profile builds. Unchanged A native evidence retained. No automatic
hourlong host/lifecycle/archive/creation VM repeat: source unaffected; escalate
any concrete affected contract that requires a change in this selection.
Outputs and derivations must be rooted promptly and full input/output receipts
saved. Review does not itself establish native/build/deployment success.

## Final identity and receipts

B final head570d900a4b7bbfe5c716cfd234f9dc89bbedc746,
treef877578a730f0d61a5d6aa2dcc18332cb9712c07, clean. Fifth commit:
portal: retire accepted retry provenance before bounded admission.
All original four commits remain exact. A pin/Go/Nix metadata unchanged.
Exactly eight changed files: turnretry state/controller/store/retention_test;
workspacecodex turn_retry/turn_retry_proof/turn_retry_retention_test; and
docs/turn-retry-recovery.md. Final delta1042insertions/37deletions, primarily
772lines of focused regressions supporting the persisted-state/replay boundary.

Owner inventories/evidence in parent tracking directory:
implementer1-hotfix-final-history.txt, implementer1-hotfix-deployed-history.txt,
implementer1-hotfix-deployed.patch, implementer1-hotfix-successor.patch,
implementer1-deployed-d819-hotfix-predecessor.bundle and bundle-verify receipt.
Quick logs: implementer1-hotfix-focused-4.log (core0.241s, wrapper43.774s),
implementer1-hotfix-race-core.log (7.637s),
implementer1-hotfix-race-controller-corrected.log (workspacecodex88.445s/web7.346s),
implementer1-hotfix-race-admission.log (individual protected/FIFO/crash passes,
plus diagnosed fixture context expiry),
implementer1-hotfix-race-replay-corrected.log (37.185s),
implementer1-hotfix-race-byte-budget.log (1.503s).
Earlier fixture failures are retained and diagnosed, not erased. Replay context
now starts after setup and changed-tuple assertions require identity-reuse error.
No native/packaged/build/hotfix deployment evidence is claimed yet.

Supplement: owner final command/hash/provenance receipt is
../implementer1-hotfix-final.json. Reviewer interim confirmed Important finding
at Controller.preflightAccepted clearing Pending on known-never-submitted
capacity refusal. Lead requires retaining that exact Pending in the existing
blocked representation; owner holds source570 frozen until review concludes.
The narrow correction will be inspected and focused-tested under workflow step9,
then only the new successor commit is amended. Final deployment/pinning waits
for the corrected exact head. No source edit occurred during review.

W/C owner is released for mechanical final B pinning concurrently in separate
worktrees; B source remains frozen. Their exact published graphs/history follow
as a supplement; do not read moving W/C source as a final packet.
Save final report under hotfix-64-steers/review.md and report findings to lead.
