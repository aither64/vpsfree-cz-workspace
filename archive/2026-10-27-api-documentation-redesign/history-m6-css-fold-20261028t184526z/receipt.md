# Narrow CSS history fold

Base `f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`; final HEAD `cefe8c5d43277dbaba35632b5239d95a1959cf1e`;
final tree `7af42033e378e354a035e9eb99b6c78d85a11d84`. Exactly five commits remain:

- A: `4363d1114f31cbb5d61411a95f6501bda17b50c0`
- B: `260e3ea8a469c8840164bd8a0f5044238f5472e1`
- C: `2eb413e0ce437bb0e1e9488bf8e7f26fc52cedbc`
- D: `1ec6807d1579e691e94808d3b9b90b4ab098641d`
- E: `cefe8c5d43277dbaba35632b5239d95a1959cf1e`

A/B are literal preserved commits. C was amended through normal hooks using its
exact accepted message. Old/new C differs ONLY by owner3's accepted CSS line:
`.docs-main li { overflow-wrap: anywhere; }`. Actual sidecar
`205f2bab4fb0b4aaed9dd5688892d876e5e2b08e` has parent `a06b0cfa2abd7560f10cb58ebe99d8eb3f10b8f9`, exactly one CSS
insertion, no additional test/source path. Accepted CSS SHA256 is
`ed81059d84817e80b27b64910d23544f981e461c35fa760aaebf6d73de8622cb`.
Main accepted strict doc390/resource390/doc900 browser and all3 asset checks
and before/fixed images; those are owner3/main evidence, not rerun here.

D/E were replayed via exact original binary full-index patches with
`git apply --index --check`, then `git apply --index`, and normal `git commit -F`.
Both actual staged and committed D/E full-index patches are byte-identical to
their originals. All five messages remain exact. All C/D/E pre-commit and
commit-message hooks PASS. Known unsigned fresh-worktree hook setup was
reconciled by checking identical configuration/custom-hook bytes, reusing the
existing root .gems and local locks, bundle check and ordinary overcommit --sign.
Nix commands used --offline/--no-write-lock-file; no bypass/install/resolution.

At each corresponding actual C/D/E commit, the complete old-to-new diff is
byte-identical to accepted-css.patch. Thus ALL other runtime, helper, module,
guide, spec, template, fixture and input declaration blobs remain identical.
Prior M6 C/D smoke and all4-lane final review scope is retained for those exact
bytes. No whole-owner projection reconstruction or smoke rerun was performed or
claimed. This is the lead-accepted narrow CSS remediation and review reuse.

BEFORE the expected-old atomic feature move from205f2bab, proof asserted full
final-tree identity/empty diff against accepted sidecar, complete five-commit
series/A/B identity, exact messages/patches and matching baseline aggregate
binary full-index patch SHA256 `2e42ada45b69dd06abaca914b568bba3b6e5b3a0c4337ab9060274913814bb06`.
Both worktrees/indexes were clean and all2148 protected hashes matched before
move. Original logical index entries/flags remain unchanged after the move.

Fresh final make doc + extracted-gem packaging/profile batch passes
10 examples,0 failures, seed50232, 10.94s wall. Exact command/log
is in final-packaging-profile.execution.json/.log. No other test batch or long
gate was started. After checks, all2148 protected hashes still match, both
worktrees/indexes are clean, and no owned command or uncertain effect remains.

Unique recovery refs `refs/heads/recovery/2026-10-27-api-documentation-redesign-css-pre-20261028t184526z` and
`refs/heads/recovery/2026-10-27-api-documentation-redesign-published-a06b-20261028t184526z` retain205f2bab and publisheda06b.
Existing35c/a06b publication/recovery contracts, all old refs/scratches/messages/
receipts are preserved. Scratch `2026-10-27-api-documentation-redesign-m6-css-fold-20261028t184526z` at `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-27-api-documentation-redesign/haveapi-m6-css-fold-20261028t184526z` remains retained.
No migrations; no feature dependency/channel/input update streams. All previous
source/history/migration evidence is preserved, not rewritten. No nonancestor
published/preview SHA is claimed literally merged.

No fetch/push/network/CI/preview/service/provider/TLS/private-fixture/peer or
lifecycle operation occurred. No product repair or source change beyond folding
the exact accepted CSS delta occurred. Exclusive Git/hooks slot RELEASED with
report; later preview/publication/matrix packages belong to lead.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/
