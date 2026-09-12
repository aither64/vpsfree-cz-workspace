# Compact comparison layout: Risk and compatibility review

Review lane: Risk and compatibility
Overall risk: High because exact downstream pins, deployment order, rollback,
and mixed-version behavior are in scope
Reviewer model/effort: `gpt-5.6-sol`, `xhigh`
Review date: 2026-09-12

Reviewed the complete final committed series described by
`compact-review-packet.md` and `compact-review-final-packet.md`:

- `dev-workspace`
  `41c6d75e8f7cdea1e5cbced7d0106d072d56484d..dc8d6cf7628a6a8db240f2e11ad61e8bc31ddacd`
- `vpsfree-dev-workspace`
  `6c98b3676a46c9a9c2830198eae9042b064a71e7..b37edd0f63fb7a984ba634c2d52d08e9344304b4`
- workspace
  `c6daa04a9cbf6ce8611c7ae38dcfc7c4cc7a5636..7985e127b55b48683457fdfe12a894e983d32890`
- `codex-web` unchanged at
  `de83e9c72dec6cb5ff8ec13d5b0b21ed60148117`

The review used the repository trust boundary: the local operator is trusted to
administer the development host; browser clients and content from repositories
under review remain untrusted. I inspected the local `AGENTS.md` files, commit
sequence and final trees, browser route and rendering logic, component coverage,
the creation-order test correction, package-relevant predecessor equivalence,
and every final direct and transitive Nix pin.

## Findings

No Blocking, Important, or Advisory findings.

## Security and data-safety assessment

- The change adds no server endpoint, request parameter, authorization decision,
  Git invocation, secret access, destructive operation, or persistence write.
  Commit `2414ffa7d9efbfe47e6d517e57f59b24b34a88b8` creates folder icons from fixed
  SVG paths, while untrusted directory and file names continue to enter the DOM
  through `textContent` (`portal/internal/web/static/repository-review.js:15-29,
  487-503,527-545`). Commit messages, identities and parents likewise continue
  through text nodes and the existing validated route builder
  (`repository-review.js:422-448`). Moving those nodes into the diff scroller
  does not make repository content executable.
- The implicit first-file rule is local presentation state. It does not write a
  file ID into browser history, a review record, or another persisted format.
  It falls back to the first file only when the route has no explicit file; an
  invalid explicit ID still yields the existing unavailable-file notice rather
  than selecting different content (`repository-review.js:254-255,267-281,
  385-415`). Explicit file and line links still serialize the same keys and the
  comparison request remains bound to the same repository and frozen review.
- The existing eight-editor retention limit is preserved and now protects the
  implicit first record by object identity (`repository-review.js:256-265`).
  Navigation races re-evaluate the current selection before revealing a loaded
  editor (`repository-review.js:283-290,385-415`), so a late file load cannot
  redirect the user to an older selection.
- Runtime commit `dc8d6cf7628a6a8db240f2e11ad61e8bc31ddacd`
  changes only `portal/internal/web/creation_test.go`. The test holds model
  validation blocked, obtains the HTTP response through a buffered channel, and
  uses five seconds only as a deadlock guard
  (`creation_test.go:121-145`). Test cleanup releases the worker before closing
  the server. No creation handler, receipt, authority, manifest, or private-state
  behavior changes in this commit.

## Contracts, compatibility, and deployment assessment

- There is no API schema, URL key, protocol, database, session manifest,
  lifecycle journal, canonical/private state, Git retention, or configuration
  option change. New code accepts all existing explicit comparison/file/line
  URLs. A URL without a file is also accepted by the previous package; rollback
  restores the previous behavior of replacing that URL with the first file and
  scrolling to it, without misidentifying the review or mutating durable state.
  Old browser code and the new backend, and new browser code and the old backend,
  therefore use the same API shapes.
- Runtime commit `e35cf0b0bfc343d5a4d476340980e06ac252396b`
  is the final UI tree. The final runtime head differs from it only in the test
  file, so the CI correction does not reopen the reviewed browser, API, or
  persisted-state boundary.
- The organization input and lock both select runtime
  `dc8d6cf7628a6a8db240f2e11ad61e8bc31ddacd`
  (`vpsfree-dev-workspace/flake.nix:6`, `flake.lock:58-77`). The site input and
  lock select organization `b37edd0f63fb7a984ba634c2d52d08e9344304b4`,
  and its transitive lock selects the same runtime revision and nar hash
  (`workspace/flake.nix:6`, `flake.lock:62-81,429-450`). No unrelated input moved.
- The rebased site predecessor `c6daa04a9cbf6ce8611c7ae38dcfc7c4cc7a5636`
  and deployed predecessor `cd648e2bd31e3b5d43703320be7967a92bd1e06b`
  match on `flake.nix`, `flake.lock`, `AGENTS.md`, `bin/`, `config/`, and `test/`.
  Range-diff reports the four earlier pin commits unchanged. The new site commit
  is therefore a single exact package selection on current coordination master,
  rather than an accidental replay or loss of an earlier deployment change.
- The planned runtime to organization to site build/deployment order is
  sufficient. A user-profile generation switch is reversible to the retained
  previous generation because neither version creates state the other cannot
  read. No coordinated machine/node update, database migration, operator data
  conversion, or system-configuration change is required.

## Residual risks and verification gaps

- Final exact-head CI, full package verification, exact installed-source checks,
  and live browser acceptance are intentionally pending until review
  reconciliation. The component fixture covers the new behavior against real
  editor and copy assets but uses fixture repository HTTP responses.
- No live rollback or already-open-browser test across a user-profile switch is
  claimed. An existing page can continue running its loaded JavaScript against
  the new server because the API is unchanged; the planned fresh live check
  remains the evidence for final asset composition and geometry.
- Replacing the 500 ms creation assertion deliberately removes a wall-clock
  latency ceiling from this unit test. The revised test deterministically proves
  that the response does not wait for blocked validation, but it is not a portal
  responsiveness benchmark. The twenty focused and five race-enabled repetitions
  reported in `compact-ci-investigation.md` cover ordering and concurrency; live
  acceptance remains the appropriate check for perceived response time.
- The previously accepted extreme Git directory-depth recursion limit remains at
  `repository-review.js:527-545`. This follow-up changes row contents and folder
  decoration without changing the recursive traversal or server bounds. No
  5,000-file stress, extreme-depth, or shallow-repository run is claimed.
