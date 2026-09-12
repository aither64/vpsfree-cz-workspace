# Mandatory change review: general lane

Reviewer: `gpt-5.6-sol`, reasoning effort `xhigh`
Risk classification from packet: High

## Reviewed ranges

- `dev-workspace`: `820277e6cc3aa7ff9acb0396feb3314e7f84996a..cbe617df87c29bf02c64df4188c9ca0878d22601`
- `vpsfree-dev-workspace`: `ee9c55b3c25fd0b0002b3ce4796167d27378cd3a..e2aa14bf41d1c2d18d59f3d66ef3caee2c41c02b`
- `workspace`: `cc5f495c6485d76abeaf16087d1fe4b0069d6893..2d037e03c3eb28f514f0f84a4cb5f15a2c0640ef`
- `codex-web`: unchanged at `de83e9c72dec6cb5ff8ec13d5b0b21ed60148117`

## Findings

No Blocking, Important, or Advisory findings.

The three runtime commits have distinct, reviewable purposes. `4e714b7` widens
commit-detail membership to ancestors of the saved head and adds native and HTTP
coverage; `233ee1c` adds the parent-page presentation and browser coverage; and
`cbe617d` adds the cohesive tree and file-heading controls. Documentation stays
with the behavior it describes. The two downstream commits contain only the
matching source pins and generated lock updates. There are no fixup commits,
superseded protocols, repeated dependency updates, or unrelated changes in the
reviewed ranges.

The implementation matches the requested behavior. `ComparisonCommit` validates
a complete object ID and checks ancestry against the immutable saved head before
reading metadata (`portal/internal/repository/review.go:358-384`). `CommitPair`
uses the first parent and constructs an object-format-correct empty tree only for
a root commit (`portal/internal/repository/review.go:391-407`). Parent routes retain
the frozen review and layout while clearing file, version, and line state and
selecting the diff view
(`portal/internal/web/static/repository-review.js:255-264,404-423`). The tree uses
native disclosures, sorts directories before files, handles path components with
`Map`, copies destination paths, and keeps navigator collapse separate from diff
sections (`portal/internal/web/static/repository-review.js:462-526`). Layout and
version changes reuse the active tree, while direct file and history navigation
open the selected file's ancestors (`portal/internal/web/static/repository-review.js:368-398,558-574`).

Coverage exercises ancestor traversal beyond the comparison base, merge and root
commits, first-parent diffs, unrelated/newer/non-commit/missing objects, frozen
state after ref movement and service restart, exact clipboard text, collapse and
history behavior, keyboard disclosure, Unicode/deep paths, file-directory name
collisions, status/count presentation, URL cleanup, CSP, responsive layout, and
the existing eight-editor bound. The packet also records passing full Go, race,
JavaScript parse, whitespace, workspace-contract, and 21-check Chromium runs.

## Residual risks and test gaps

- The long package/live deployment acceptance and a real rollback have not run;
  these are the planned post-review checks. The API addition is non-null and
  additive, so the remaining rollback behavior is availability of newly exposed
  ancestor links under the old package rather than persisted-state corruption.
- Browser coverage follows parent links normally and validates their frozen URL,
  reload, and Back behavior. It does not automate a modifier-click or middle-click
  into a new tab. The links have ordinary `href` values and the click handler
  declines modified and non-left clicks, so this is a small residual browser gap,
  not a correctness finding.
