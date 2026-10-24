# Combined pending retry and browser fixture handoff

Final clean, SSH-published B: `8675c87ffaba337614c902dbaaaca4f665dee192` on
`2026-10-20-dev-workspace-portal-improvements`. Default master is unchanged at
`968646471b1190c16a8cf60ff50736cd0525fa3f`. [Publication](publication-proof.json),
[remote receipt](post-push-remote.txt), [complete source proof](source-proof.json).

The original six-path product package was published at `548bce43850d4f27657f71cb8996c10dab1ad8bf`
just before the two-fixture amendment arrived. Lead explicitly accepted preserving
that checkpoint and using its exact lease for the combined publication. Both
publication receipts remain: [product](../push.log), [combined](push.log).
No rollback or stale-lease retry occurred.

## Final eight-path scope

The first six paths restore the accepted pending-read retry contract. A CURRENT
pending failure resets only `pendingSuccessAt` to its existing initial sentinel
immediately after the current-cycle guard. Existing notice history, questions,
read identity, authority, single flight and forced rerun remain intact. The old
success freshness floor no longer defers the2s retry; existing2s/4s progression
and30s cap remain. A successful read restores ordinary15s freshness.

The six paths are app.js, the actual-function read-cycle regression, three app
script references and the existing cache assertion. App53 becomes54 consistently;
store4/browser6 remain. [Original product delta](../six-path-delta.patch) and
[product source proof](../source-proof.json) are retained unchanged.

The two other paths are the EXACT parent-inspected imp0 candidate, patch SHA256
`2262c6876b3b1e752b65f9c6317e675ada823154820160daf62e09011514e8b0`.
Before apply, both base hashes matched965,1a25 and548. Final hashes equal its
immutable candidates:

- page_lifecycle_browser_test.cjs: `5f64cb304126f7826985e42af1a87cb7489a9d18c93e75578a9d0f8887f0edb7`.
- team_settings_browser_test.cjs: `771b8b8e9f605e41cbe94da82cb1b6bddea6879b84ffb15292cefbbc86817684`.

Team is selected within the exact Session sections tablist. Stale recovery reply
classification is captured before awaits; construction, fulfillment and actual
numeric marker consumption after applyRecoveryStatus are required within the
existing5s poll. Existing hidden/draft/no-send/>baseline assertions remain.
[Immutable two-file patch copy](two-fixture-delta.patch),
[final two-file delta](final-two-delta.patch), [whole eight-path delta](whole-eight-delta.patch).
No candidate generalization, production hook or fixture budget change occurred.

## Verification

All authorized checks ran in B's Nix environment:

- App/test syntax and whole read-cycle suite:17/17 PASS,329.222ms. Cases cover
  recent-success→forced503→real2s retry, retained questions, ordinary hints respecting
  backoff,4s/8s/16s/30s/30s progression, success reset, successful15s freshness,
  forced/coalesced rerun, retired failure, current403, existing deadline/history
  and legacy behavior. [Node log](../quick-node.log).
- Exact965 app blob `bb0b7501421e584ac414fb838541bc8b5dcf4db2`, disposable tracking-only
  copy with identical current regression bytes: expected exit1 observed at
  **the2s retry must dispatch inside the previous success window**, actual2 versus
  expected3 transport reads. [Negative log](../negative-965.log),
  [identity](../negative-identity.json). The feature worktree was never swapped.
- Focused Go template/cache, pending revision legacy/revision/paged forwarding,
  native fixture journal and readiness tests: PASS0.458s. [Go log](../quick-go.log).
- Both added CJS syntax checks: PASS; no actual browser execution.
  [Two-file syntax log](quick-two-syntax.log).
- Cache references, staged/full-range whitespace: PASS. No declared hook framework
  or installed pre-commit hook; ordinary Nix commits used no bypass.

The first new current-failure run exposed a missing pendingStatus DOM stub in the
partial lane harness. It was added within the approved test file; initial failed
logs remain under ../initial-*.log and are not accepted negative proof. The final
negative fails specifically at missing2s dispatch. Product bytes after the two-file
integration equal tested548 exactly, so these successful quick receipts retain
exact-source proof. No unrelated checks were repeated.

## History and reconstruction

Final tree `1b7bf9e0ae859bb6c8f976e04f61f0a079556ec4` EXACTLY equals the combined passing pre-fold tree and
reconstruction of1a25 + saved six-path product delta + immutable two-file patch.
Applying the inverse two-file patch returns product tree
`45a5447bda63f9f0a3af68521fcbb8418b5fbc6a` exactly. All521 Git blob/mode entries outside
the eight paths are identical to1a25, including every native Firefox fixture,
imp3 correction, dependency, API/schema, documentation and host/native policy file.

Eighteen logical groups remain with no fixup. Team selection is folded into
`e1c08d3b817ca9660dddd5cc9a35507cf396c000`. Pending freshness is folded into `69476991609ebd928675cc7e76e5fcc1ac536205`.
Stale-reply readiness has one focused final commit `8675c87ffaba337614c902dbaaaca4f665dee192`:
the relevant logic predates the series at92b2576d, an ancestor of base9686464;
the only earlier in-range edit to that fixture concerned download links.
[Segment provenance](lifecycle-history.txt).

Compared with original1a25's17 groups,14 patch IDs are identical; changes are
Team fixture, pending product group and notification cache context. Notification
actual added/removed lines are IDENTICAL. Compared with tested548's17 groups,
16 patch IDs match; only Team changes, plus the focused eighteenth commit.
The sole A dependency group4a2fadd and all dependency files are unchanged.
[Original range diff](range-diff-original.txt), [548 range diff](range-diff-product548.txt),
[complete final range](complete-final-range.patch),
[notification line proof](notification-added-removed.json).

All1a25/965/d617/reviewed133/deployedf8 refs and original receipts remain;548 has
an additional explicit safety ref. No migrations or persisted formats changed.
Existing deployed nonancestor lineage remains its original supported proof;
this is no claim of literal integration, redeployment or user acceptance.

## Parent next action

This report returns B source/index/Git ownership clean to the lead. No further
imp0 Git handoff is required. Parent owns the committed affected HIGH-risk review
(all four applicable lanes with full series/deployed lineage), then prioritized
long native50/browser/package/CI verification and final composition pins.
Prior unaffected review conclusions remain bound to their recorded heads.

Actual native50 acceptance is still pending, including the previously unreached
lost-response original retry, exactly one dispatch/journal entry and two attempts.
Native visibility/discard/restoration/35s foreground/hidden-zero and10s pending
retry budgets are unchanged. This distinct proven freshness defect is not an
incident-wide cure claim. No browser/full suite/package, CI wait/query/cancellation
POST retry, C/config/pin/guard, host/TLS/native, claim, deployment or lifecycle
action ran here. No new product documentation/prose was needed to restore the
existing documented contract; lead owns session state/portal cadence.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-dev-workspace-portal-improvements/
