# Scope and proportionality review

Reviewed with `gpt-5.6-sol` at `xhigh` reasoning effort, using the scope lane from the mandatory change review workflow. The review covered only these committed ranges:

- `dev-workspace` `820277e6cc3aa7ff9acb0396feb3314e7f84996a..cbe617df87c29bf02c64df4188c9ca0878d22601`
- `vpsfree-dev-workspace` `ee9c55b3c25fd0b0002b3ce4796167d27378cd3a..e2aa14bf41d1c2d18d59f3d66ef3caee2c41c02b`
- workspace `cc5f495c6485d76abeaf16087d1fe4b0069d6893..2d037e03c3eb28f514f0f84a4cb5f15a2c0640ef`
- `codex-web` remained unchanged at `de83e9c72dec6cb5ff8ec13d5b0b21ed60148117`

## Findings

### Important

1. **Parent navigation retains an explicit `view=diff` selection instead of clearing `view` as approved.** Commit `233ee1c` defines `parentRoute` with `view: "diff"` in `portal/internal/web/static/repository-review.js:255`; `reviewURL` then serializes every truthy route key at lines 42–48. Consequently, both the parent link and the in-page navigation URL contain `view=diff`. The approved contract says parent navigation preserves review/layout and clears file, view, version, and line (`tree-navigation-plan.md:24-28`, `tree-review-packet.md:39-42`). The default route already renders a diff when `view` is absent, so the extra key has no functional benefit and leaves the durable URL outside the requested canonical state. Existing browser coverage checks the preserved layout and commit and the absent file at `test/repository_browser.cjs:190-194`, but does not check that `view` and `version` are absent and the hash is empty. The smallest fix is to omit `view` from `parentRoute` and add those narrow URL assertions. No broader routing change is needed.

### Blocking

None.

### Advisory

None.

## Proportionality assessment

Apart from the route mismatch above, the series is proportionate to the approved outcome. The backend reuses native Git ancestry and commit inspection rather than implementing a graph walker, removes the old base-bound check, and adds no endpoint, persistence, fetch, or object-retention mechanism. The public change is the already-populated `Parents` field becoming an additive non-null JSON array.

The browser builds the tree with local `Map`, list, and native `details` elements and keeps collapse state only in the live DOM. It reuses the shared copy-button factory, keeps the existing URL schema and editor bounds, and introduces one small count-parts representation so text and colored DOM renderings share formatting. These mechanisms each have a current consumer in the requested UI and do not form a speculative repository-browser framework.

The focused backend and browser tests are commensurate with the widened immutable-ancestry boundary and the explicit tree/navigation acceptance cases. They exercise owned integration behavior without trying to reproduce Git conformance. The organization and workspace commits contain only the required input pins and generated lock updates.

## Remaining test gaps

- Add a focused browser assertion that a parent link omits `file`, `view`, and `version` and has an empty hash after the finding is fixed.
- Package, live-browser, deployment, and final CI evidence described as pending in the packet remain outside this pre-integration review lane.
