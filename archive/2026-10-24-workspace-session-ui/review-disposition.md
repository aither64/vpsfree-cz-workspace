# Final review disposition and accepted history

User scope: four portal fixes, implementation authorized. No merge/deployment
approval, no live runtime or settings/lifecycle mutation. Session remains open.

## Reviews retained

- Original final review: base `b3a6eb2fc0b41cf0cb965bf4c39991815d9df734` to
  `5293cf5b3d6752e804223833a1bb9d484e55b759`, retained reviewer0 Sol/xhigh,
  all four lanes; `review.md`, `final.diff`, `final-history.txt`.
- Focused new R3 recovery design: same base to
  `07d41aac2663f6e7079618da6d81bc9474af95ad`, same reviewer/settings, affected
  general/architecture/scope/risk lanes; `review-followup.md`,
  `refreshed-final.diff`, `review-range-diff.txt`, remediation packet.
- Direct R4 requested narrow correction: same base to
  `45deeeacf119eb733852a5df21abd6e030262e26`. Lead inspected `r4-final.diff`
  and source/regressions under mandatory review step9; no new boundary/contract,
  no blanket repair-confirmation rerun. `r4-range-diff.txt` binds history.

## Accepted findings and fixes

R1 Blocking: recovered unknown IDs remain uncertain on draft capture/detach
failure; send/queue reload regressions show original identity cannot be
edited/discarded as unsent. R2 Important: edited snapshot replacement reconciles
ordered state and original/new record retirement, including refused writes,
readback failure and deletion side-effect; compensating failures retain recovery
records when proof of cleanup is impossible. R3 Important: exact known pre-send
response/status pairs only on in-memory first-dispatch provenance; fresh
attachment refusals become failed only after persisted proof. Failed head can
be replaced with current composer/new attachment selection/newID, original action/
position; unknown receipts retain recovery fence. Exact real handler/backend
unit tests prove all ten refusal pairs before native calls, with native/post-
acceptance errors distinct. R4 Important: every definitely-unsent retry, including
unchanged text and persisted failed reload, uses newID replacement. Repeated
refusal stays recoverable; unknown retry keeps original ID. Focused regressions
fail on old reviewed code and pass on final code.

All findings are fixed within accepted boundaries, with main-agent writing pass
for new copy/guide. Reviewed old/new bases/heads and reports retained; source
history never deployed/released or merged. No database/server/native schema
migrations, no dependency/generated streams. New tab-local schema1 dispatch key
is separate; existing attempt encoding remains unchanged. Forward-compatible
new-browser recovery required; older browser cannot manage new FIFO semantics.

## Exact accepted final inventory

Base `b3a6eb2fc0b41cf0cb965bf4c39991815d9df734`; final head
`45deeeacf119eb733852a5df21abd6e030262e26`;
final tree `593a353ad9ed32de4bdb437eb1287937851a2dd0`.

1. `439e33a596ab334c539271cb7ebac9e508acb564` settings (unchanged review).
2. `4b3817f4f39e73e6012a5b3a57f7c61769a48b03` unread (unchanged review).
3. `3b5e1cfdd3e156134a27d50d13a39f512fff1c8e` composer + folded direct fixes.
4. `4aca5811a6b025dee8c3ce23c8065b9cc68b7da9` quiet queue (patch-equivalent).
5. `45deeeacf119eb733852a5df21abd6e030262e26` final guide + approved retry text.

Lead complete history/diff/range inventory: five coherent commits, no obsolete
unapplied approaches/fixups/transitional schemas, no migration versions or
repeated dependency streams. Worktree/index clean. `accepted-final.diff` and
`accepted-history.txt` bind final source. All quick checks and real-handler
prerequisite passed; longer verification results tracked separately in state.
No readiness/deployment conclusion before those results.

## Post-verification fixture correction

At published `45deeeac`, full local evaluation and fast/package checks passed;
Chromium composer passed, paging scenario failed because new fixture returned
102 entries despite pinned shared reader's100 limit. Lead accepted direct
bounded fixture repair from implementation owner: drop two oldest synthetic
newest rows before appending hidden tool/team, assert every fixture page <=100,
and await actual changed text rendering before badge assertion. No product,
protocol, persistence or prose behavior changed; direct inspected test repair,
no new design requiring independent rerun.

Final published head `63ab97ce9bf131f76e1a058085c24ab38e3d212e`, tree
`9c9f3fb330090ca2ab9533f7cd0c5f5f8c3d458c`. Five final commits:
settings439e33a5; unreadfa4b6d17 (fixture repair folded); equivalent composer
49a1c9a3; equivalent quiet87f49266; equivalent docs63ab97ce. Complete series,
`final-published.diff`/`final-published-history.txt` and
`paging-fixture-range-diff.txt` inspected: no obsolete commits/migrations/pins or
repeated updates. Exact prior reviewed/published heads retained; no deployed
lineage claimed. Feature force push used explicit old-head lease45deeeac;
remote proved new63ab97ce. Corrected real-browser proof and native remainder
still require results; new final-head CI replaces superseded run.

## Final hidden-section fixture repair and verification binding

The100-entry correction exposed a second fixture omission: its final synthetic
snapshot mutation did not send the `/fixture/refresh` SSE hint used in all prior
cases. Internal section clicks do not supply a separate read invalidation;
no product defect was demonstrated. Lead accepted four-line fixture-only repair:
while Settings inactive-Codex assert hidden section, send normal refresh hint,
await rendered new text and unread button's absent hidden attribute, then reopen
Codex and retain original visible badge assertion. No weakened acceptance.

Complete focused paging Chromium passed42s at63ab97ce plus exact held fixture
SHA256 `5828030c62b0cf6e800164c04f50a0621d4124c9d085a500256dcc06b7fab53e`.
Final consolidated source hash is identical; final tree equals tested intended
pre-autosquash tree `0be2d72b477a6b921f6beb32bf33534d4305b77e`.
Head `064e311e6dc933bc9a0f5d7cd20eaf20eeccbbf9` has five commits:
settings439e33a5, unreadb925417c (only fixture delta), equivalent composer9e225a4f,
equivalent quiet9e86c0af, equivalent docs064e311e. `hidden-section-range-diff.txt`,
`hidden-section-final.diff`, `verified-final.diff`, `verified-history.txt` retain
full inventory and comparison to prior reviewed ranges. No product/protocol/
copy/pin/migration or obsolete history changes. Postconsolidation Node syntax/
paging contracts and full-range whitespace pass, index/worktree clean.

Local full package/composer Chromium PASS at45deeeac; later changes exclusively
paging opt-in fixture. Native pinned recovery/FIFO PASS at63ab97ce, unchanged
native/input graph. Corrected paging complete PASS bound by exact file hash and
source equivalence; no claim full package derivation identical after test-only
source change. Final exact-head CI supplies fresh packaged verification.
