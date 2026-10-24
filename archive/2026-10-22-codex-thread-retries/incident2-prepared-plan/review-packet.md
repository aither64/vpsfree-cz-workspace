# Prepared plan delivery and HTTP runtime contention review

RELEASED final A/B source review. Intended A/B changes are committed and
quickchecked. Published identities are frozen below; W/C follow as a separate
mechanical pin/history supplement. Do not run tests/builds/native operations.

User reported this session's Implement-now alert: earlier submission has no
managed admission proof; browser retains Outcome unknown / Implement the plan.
Separately ordinary message/queue reconciliation requests fail with runtime lock
contention mapped to conversation unavailable before dispatch. Ordinary messaging
after the64steer hotfix was confirmed, but that did not exercise this plan path.

Read current design.md section Incident2 in full. Source-backed cause and exact
public A signatures, B scoped HTTP proof/recovery and context-aware runtime wait
contract are there. UI redesign is paused. No native version/protocol/schema/
public-error change. Preserve exact original browser submission and accepted/
submitting/queue proof; no reset/delete-reprepare/newUUID/globalprepared bypass.

Review retained reviewer0 Sol/xhigh/read_only, no overrides or nested agents.
HIGH risk: library/API, persisted identity, concurrent HTTP/lifecycle admission.
General, architecture, scope/proportionality, risk/compatibility lanes required;
read mandatory skill and all4references. Actual production Handler + real managed
client must cover fresh plan and deployed prepared recovery, exact accepted/
acknowledged-history receipt first, altered identity/settings and other unknown
attempt rejection. Runtime EXbarrier→HTTPwait→release→one originalIDsend; expiry
zero native; fresh authority/generation/lifecycle refusal after wait; no inverted
locks. Existing failfast lifecycle APIs unchanged. Retain ed2pressure/replay tests.

Actual deployed predecessor A c1f415ad5602c23e6443cced73cb59267a796f05,
tree7e3523236dc4500b68a008398305b2290beabcc8, baseea64ef57fdd2ff5fd60715b62f2d1696bc0133e5.
B ed2a75b98a75f9b37b7a359e9091a94e9846644e,
tree63eba6140c340d28f38c39b010d0a5b2874b7680, basebf6d4b0c49600c15e17fe71248807ef43424e932.
These are real deployed state/consumer boundaries. Preserve original series,
bundles/receipts and append coherent successor behavior; no literal merged claim.
Full base-to-final series/diffs and migrations/update streams need independent
conclusions. No migrations: retry schema1/native ledger3 unchanged. B's A pin
stream must be consolidated per procedure, with supported exact deployed revision
preserved separately; do not use deployment label to excuse redundant pins.

W0a1d20e7/C7feaa9e1 deployed predecessors preserved; dependent final mechanical
pins only after final A/B publication. Their exact graphs/history follow separately.
No moving-source W/C review. Cbasec105 intentionally retains deployed unrelated
inputs; current remotecc313 drift is unrelated emergency deployment scope.

Ordinary HTTP contention evidence: own journal filtered metadata proves
LockRuntimeShared LOCK_NB EWOULDBLOCK before native VerifyThread/Send; no stuck
holder at observation. Source proves teamassign/report EXholds same runtime lock
across synchronous RPC. Do not infer which historical process or UUID sent from
that alone; no live native request used for diagnosis.

Owners provide exact quick commands/logs/tested-tree evidence and lasting docs.
Lead applies user prose pass before commit. Required postreview selection: exact
A/B package checks with drv/input reuse, targeted native contract/controller,
runtime/package/lifecycle exclusion regression, W4/C8 and scoped profile/system
builds. No unrelated VM campaign unless concrete impact requires it. Full rooted
input/output receipts. Lead owns activation under held claim201af6c8 and user
original submission retry; no integration/reboot/release/lifecycle authorization.

## Final A input (B and reviewer release still pending)

A final ac62eeeb9d8b1fa7b8ed8fb95ba8160acb7efa1c,
tree c0066833953974d27019c40754301a45a58868b0, clean and SSH published.
Full ea64-to-final series:

1. df00fa36c820fc7a62ee5b8dd6e1745940ff8e15 — exact failed-turn continuation/context.
2. 6c828759440705c632e1902fa8309ccac446b050 — optional application retry controls.
3. c1f415ad5602c23e6443cced73cb59267a796f05 — private native verification fixture, actually deployed.
4. ac62eeeb9d8b1fa7b8ed8fb95ba8160acb7efa1c — additive prepared-send proofs.

The first three commits are unchanged. The successor changes client.go,
prepared_send_test.go and docs/reference.md; schema3 and native protocol remain
unchanged. Exact deployed c1f bundle and owner inventory are in incident2-a/.
The new public methods have no native RPC or policy mutation. Lead accepted
the final reference prose/comments/error before commit.

Focused normal/race command/status/JSON evidence is under incident2-a/;
final-normal and final-race each contain 48 passing test/subtest events with
zero failures/skips. Committed tree equals tested staged tree. Source metadata:
NAR sha256-tCfdy/lh9LHbvEd6BYO0trM1pUelyv2T63KsQ1iEK90=,
lastModified1792775188, revCount112.

A owner final packet: incident2-a-final.json (SHA256
6a7882c9bf9408e0e86a8f68c66d92dd111a3a321e215ec9a992cfaeca302d02).
Owner reports exact A CI39992358832 completed success, queried without waiting.

Lead accepted B history preparation: ed2 need not remain a literal ancestor;
no runtime/state dependency requires that ancestry. Preserve deployed exact
refs/bundles/receipts, retain independent product commits, consolidate the sole
A dependency stream into its final selection, and bind old/new ranges plus
deployed-product comparison. This is preparation, not final history acceptance.

B new production-path regression files to inspect at final head:
portal/internal/web/plan_delivery{,_test}.go,
portal/internal/web/runtime_wait_test.go,
portal/internal/session/authority_wait_test.go and
portal/internal/workspacecodex/prepared_send_test.go. Runtime HTTP fixture
contains 18 route/outcome combinations, with fresh authority/generation/
lifecycle/cold checks on the plan route and wait/release/deadline cases for
root/member messages, queues and queue reconciliation. Existing ordinary
provider/creation/observation tests remain applicable; tests are owner-run,
not rerun by lead during implementation.

Actual Handler admission-save boundaries now cover refusal before save and
interruption after durable save: native0/settings1 before recovery; original
prepared UUID survives; recreated client/controller recovery yields native1/
settings1. Focused race2.052s. A fixture reentrant metadata-RPC deadlock was
diagnosed and removed without changing product behavior; preserve owner logs.

Latest B owner quick evidence (final committed tree identity still pending):
web actual plan/runtime route batch PASS4.648s normal /14.658s race;
session lock PASS0.070s normal /1.130s race;
workspacecodex options/retention race57.401s; turnretry race2.136s.
Earlier fake roster/resume and private-directory fixture failures were corrected
without product relaxations; retain failure/diagnosis evidence in owner receipt.
Independent final review must inspect the actual final committed tests.

## Final B and review assignment

B final 7b8c646974df72e0df3e576d10f09d79823ae004,
tree9a409e0eb0003d1e3cefd6874d0cae028506d368, clean. Lead directly checked
full bf6d-to-final series, deployed-ed2-to-final 17-file diff inventory and
whitespace. The complete series is:

1. 7262c24e4fbe9dbf8604e73590f9b5ef3d5dce99 — original durable retry core.
2. b3c7187c6e26e269994433716a0ee719d0a7edf7 — original package capability.
3. aafaf4195d695c4641ce4f9342d56a1786f237c3 — original managed runtime.
4. a708f4011d33e7df6b73256b9a3873c24d03bbe7 — sole final Aac62 dependency pin.
5. f856549e54e2dbe56cc91548d2ea9b588c7e6633 — retained accepted-only retention patch.
6. 9fe56d2b031928ed18a8fa7bde61dc5edadef24e — exact prepared-plan recovery.
7. 7b8c646974df72e0df3e576d10f09d79823ae004 — bounded HTTP runtime wait.

The original first three commits remain exact. The final A selection replaces
d819's pin; retention is replayed without changing its product patch. Exact
actually-deployed ed2 refs/bundle/receipts remain preserved; it is not an ancestor
of this final B and no literal merged/equivalence claim is made. The unchanged
retention boundary plus substantive incident fixes requires fresh deployment.
No migrations/eager rewrites; deployed retry1/native3 records remain supported.

Final focused owner batch implementer1-incident2-final-focused.log passes:
web8.927s/workspacecodex5.720s/session0.072s/teamruntime1.159s. Earlier race logs
and failure diagnoses are retained under implementer1-incident2-*; the owner
final receipt binds exact commands/blobs/trees and is supplemental evidence,
not a substitute for actual source inspection. Final committed tree equals the
quickchecked tree. Lead main copy pass is incorporated in the owning guide.
Source metadata implementer1-incident2-final-source-metadata.json:
NARsha256-s5/AadLEaAnjZCuDm9Ww09C4g74C1TAgFoBx9A4P5/E=,
lastModified1792776345, source/nix/store/iwpjzdbqiz1d87awy3sr8izdzfmrn5a3-source.

Assign retained reviewer0, gpt-6.1-sol/xhigh/read_only, no overrides or nested
agents, HIGH general/architecture/scope/risk lanes. Review the whole final A/B
series/history/migration/pin disposition and concrete changed delivery/locking
contracts. Use prior reviews for historical context, inspect current source and
callers directly. Read owning docs and all four skill references in full.
Return findings ordered by severity and explicit history/update-stream/no-
migrations conclusions. Do not edit session/source files, run tests/builds,
inspect live submissions, wait for CI, deploy, integrate, claim or release.
Lead saves the report as incident2-prepared-plan/review.md. W/C supplement will
be separately frozen and supplied; no stale moving-source downstream approval.

## Owner final B receipt

implementer1-incident2-final.json SHA256
9c9fa1ce491df9922891ba444aecfc22c2025a9e60e66b127f6514e8530fd26d
binds final/tested tree, clean remote head, source metadata, commands/logs,
complete history and original failure diagnoses. Its associated consolidation
range-diff shows original commits1–3 exact, the one final A pin replacement,
retention exact (=), removed interim pin and unchanged final behavior patches.
Lead directly read the range-diff and final reference wording; no product
change beyond the accepted incident2 boundary is inferred from history cleanup.

Lead independent source inventory: incident2-prepared-plan/lead-source-inventory.json
binds exact clean heads/trees/series and directly computed equal retention
patch IDs. It supplements, without replacing, the reviewer's own checks.
