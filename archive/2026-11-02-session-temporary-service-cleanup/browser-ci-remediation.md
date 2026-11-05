# Browser read-cycle CI correction

Committed owning-UI fixup `c850a545c336b64f82d9f5d31d9fe24bb36bae33`, tree `b9f7154cabbd95624dc447d87b855f2b01b33247`,
parent `e29d4d83fc62e0dc929aca332f324336c9c8b034`. One B-owned test file,
three insertions/three deletions. Runtime index/worktree clean; Git lane returned,
no operation running. No push/rebase/pin/build/CI retry/deployment/lifecycle action.

## Complete CI diagnosis

All complete failure stacks from creation, fast and archive in CI41509697499
show the same distinct failure: read_cycle_browser_test details resumed-read test
throws `ReferenceError: applyCount is not defined` from extracted eval line134.
All other reported derivation errors are downstream dependency failures. Native
VM tests never began. No separate core/Go failure or nonzero Ruby failure/error
summary was observed. A was notified; no core files were edited.
[Full per-job stacks and inventory](browser-ci-failure-inventory.json) bind the
complete log SHA256, exact lines and dependency failures. Original CI evidence
remains under runtime-ci-e29d4d83/.

The details fixture began extraction at `let detailsTimer`, omitting the newly
preceding shipped count helpers. The full application already includes them.
The test now extracts from `countSnapshots`, injects the actual exported
`resourceCountPresentation`, and supplies the ordinary document event-listener
fixture. It retains real read-slot/finally wiring and late-settlement checks.
No duplicate count implementation, mock success bypass, product change, public
contract, persisted format, schema, ownership or prose change was introduced.
No reusable documentation change was useful because only a test harness changed.

## Exact focused verification

- Baseline existing read-cycle file reproduced17tests/1failure with the same
  applyCount exception. [Baseline log](browser-ci-baseline.log).
- Initial affected combined browser run:127tests passed, zero failures/skips.
- Exact package-declared Node selection was then run in its declared order,
  separate processes:10syntax checks and readcycle17 + attention75 +
  coordination14 + resources2 + providers19 =127tests, all passed.
- The first raw-checkout sequence reached its final syntax command and stopped
  because generated review-editor.js is absent from the checkout. All127tests
  had passed. This was package preparation, not a new product/test defect.
- `nix/workspace-portal.nix` preBuild copies reviewAssets/review-* into static.
  Nix evaluation identified the already-realized pinned asset path
  `/nix/store/hllcfkaav40y98j1v7vl3gkikgpd0w75-workspace-repository-review-assets-1.0.0`.
  A temporary isolated web export with that exact preparation ran all15declared
  commands successfully in11.709seconds. No asset/source build occurred and no
  generated asset was added to the checkout. The temporary fixture was removed
  after its commands exited; no live session state was used.
- Whole diff whitespace passed. Committed test bytes match the successful
  selection's SHA256. Normal Nix-shell/tempfile commit honored hooks; no hook
  framework is declared or active. No bypass. Runtime flake/lock unchanged.

[Exact commands/result and tested hash](browser-ci-package-js-prepared-result.json),
[complete successful output](browser-ci-package-js-prepared.log),
[raw-checkout preparation failure](browser-ci-package-js.log),
[commit receipt](browser-ci-correction-commit.json),
[committed diff](browser-ci-correction.diff).

The lead accepted the harness-only diagnosis and will inspect the exact committed
correction under narrow-fix policy. Publication/consolidation requires its next
package. Current e29 downstream pins are held and unchanged. No full package/VM
acceptance is claimed by these quick checks.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-session-temporary-service-cleanup/
