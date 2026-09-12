# Architecture and repetition review

Review result against the exact packet revisions: **0 Blocking, 0 Important,
0 Advisory**.

Reviewed ranges:

- `dev-workspace`
  `820277e6cc3aa7ff9acb0396feb3314e7f84996a..cbe617df87c29bf02c64df4188c9ca0878d22601`
- `vpsfree-dev-workspace`
  `ee9c55b3c25fd0b0002b3ce4796167d27378cd3a..e2aa14bf41d1c2d18d59f3d66ef3caee2c41c02b`
- `workspace`
  `cc5f495c6485d76abeaf16087d1fe4b0069d6893..2d037e03c3eb28f514f0f84a4cb5f15a2c0640ef`
- `codex-web` unchanged at
  `de83e9c72dec6cb5ff8ec13d5b0b21ed60148117`

## Findings

No Blocking, Important or Advisory architecture/repetition findings were
identified.

## Architecture and consumer assessment

The backend change stays with the existing native Git owner. Commit parents are
parsed once by `parseReviewCommits` and carried by `ReviewCommit`; both history
responses and selected-commit details therefore use the same declaration
(`portal/internal/repository/review.go:49-63,316-338`, commit `4e714b7`).
`ComparisonCommit` widens only its saved-head ancestry rule, and `CommitPair`
uses the first parent from that same parsed value or derives the repository's
empty-tree object for a root commit
(`portal/internal/repository/review.go:358-407`). There is no parallel parent
registry, alternate revision parser or second diff implementation.

The HTTP service continues to own session/repository scope and durable review
restoration. A requested commit is validated against the immutable saved pair
before the service creates a comparison snapshot, then the existing files,
content, cache and preview paths are reused
(`portal/internal/web/repository_review.go:432-477`). This keeps feature-history
range selection separate from full ancestor navigation without adding another
endpoint or allowing a moving branch ref to redefine the accepted graph. The
new repository and handler tests cover both merge parents, the base and earlier
ancestors, root comparison, newer and unrelated commits, non-commit object IDs,
missing objects, branch/default-ref movement and cold service restoration.

The browser tree is derived directly from the one `payload.files` collection
with nested `Map` objects, and each leaf retains the existing section record
used for navigation and lazy content loading
(`portal/internal/web/static/repository-review.js:465-526`, commit `cbe617d`).
Directory and file namespaces remain distinct, which handles a file-to-directory
replacement without inventing synthetic file identities. The selected leaf's
actual disclosure ancestors are recorded during rendering and reopened from
that record during direct or history navigation (`repository-review.js:368-397`).
Layout and version changes reuse the active comparison and preserve the native
`details` state.

Changed-file status interpretation remains centralized in `fileStatus`, while
text and colored DOM counts now share `countParts`
(`repository-review.js:51-73`). File, full-file and parent routes reuse the
existing URL serializer; `parentRoute` deliberately drops file, view-version
and line state while keeping the frozen review and layout
(`repository-review.js:250-263,404-423`). Path and hash copy controls reuse the
unchanged provider-owned `createCopyButton` interface rather than adding a
runtime-specific clipboard implementation. The exact `codex-web` pin documents
and tests its string/callback contract.

The commit series is ordered by dependency: `4e714b7` supplies the native/API
parent contract and focused tests, `233ee1c` consumes it in the parent-page UI,
and `cbe617d` adds the related navigator and file-heading presentation. The
organization and site commits contain only matching flake URL/lock updates. The
actual lock graph confirms the intended one-way chain: `dev-workspace` retains
`codex-web` `de83e9c`; `vpsfree-dev-workspace` pins `dev-workspace` `cbe617d`;
and `workspace` pins `vpsfree-dev-workspace` `e2aa14b`, whose nested lock selects
the same runtime and provider. No equivalent downstream implementation or
additional consumer change is needed for this additive runtime-owned behavior.

## Residual validation gaps

- The actual Chromium component test composes the final runtime assets with the
  real pinned `codex-web` copy control, but uses fixture HTTP responses. The Go
  tests exercise the native Git and HTTP boundaries separately. Packaged and
  live composition therefore remain for the planned post-review checks.
- The tree is intentionally rendered eagerly from the already bounded changed
  file list while file content and editors remain lazy and capped. The browser
  acceptance covers 30 files, deep and Unicode paths, a file/directory
  replacement, navigation and the eight-editor bound; it is not a stress test
  at the existing 5,000-file server limit.
- Long package, deployment and live rollback checks were not run in this review,
  as required by the packet. Findings and line references apply to the frozen
  packet heads above.
