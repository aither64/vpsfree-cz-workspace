# Risk and compatibility review

Lane: risk and compatibility
Risk: High
Reviewer: `gpt-5.6-sol`, `xhigh`
Review date: 2026-09-12

Reviewed the complete committed series and final trees from the frozen packet:

- `dev-workspace` `820277e6cc3aa7ff9acb0396feb3314e7f84996a..cbe617df87c29bf02c64df4188c9ca0878d22601`
- `vpsfree-dev-workspace` `ee9c55b3c25fd0b0002b3ce4796167d27378cd3a..e2aa14bf41d1c2d18d59f3d66ef3caee2c41c02b`
- workspace `cc5f495c6485d76abeaf16087d1fe4b0069d6893..2d037e03c3eb28f514f0f84a4cb5f15a2c0640ef`
- `codex-web` unchanged at `de83e9c72dec6cb5ff8ec13d5b0b21ed60148117`

The review used the documented boundary: the local operator is trusted to
administer the development host, while remote requests and content from the
projects under development remain untrusted. I inspected the local `AGENTS.md`
files, commit sequence, exact diffs, native Git invocation, durable review and
comparison records, session/repository scope binding, immutable caches, browser
navigation and rendering, tests, and downstream Nix pins.

## Findings

### Advisory — An unusually deep Git path can overflow the recursive tree renderer

- File: `portal/internal/web/static/repository-review.js:509-525`
- Commit: `cbe617df87c29bf02c64df4188c9ca0878d22601`

The API bounds a comparison to 5,000 files and 4 MiB of Git output, but it does
not bound path length or directory depth. The browser first creates one nested
`Map` per slash-separated component and then calls `renderTree` recursively once
per directory. A single repository path with several thousand short components
fits comfortably within the existing output limit but exhausts the JavaScript
call stack before rendering the comparison. An equivalent recursion run with
the package's Nix-provided Node/V8 failed with `RangeError: Maximum call stack
size exceeded` after 3,842 calls at a requested depth of 20,000.

This is a comparison-local availability failure rather than an authorization or
data-integrity break, and normal checked-out paths are constrained by the host
filesystem. Git objects and historical ancestors can still contain deeper trees,
including objects created with plumbing or received from a project contributor;
the trusted-host assumption explicitly does not extend to projects under
development. Render the nested list iteratively, or reject directory depth with
a documented bound before constructing the browser tree. Add a focused boundary
test for the chosen behavior.

No Blocking or Important findings were found.

## Security and data-safety assessment

- A durable review ID is content-addressed over the session slug, repository ID,
  scope and frozen pair. The scope incorporates tracking-directory identity,
  thread identity and repository registration. A changed registration, replaced
  tracking directory, different session or different repository therefore fails
  closed before any Git read.
- Restoring a link resolves the registered canonical repository and verifies the
  saved base and head commit objects. Commit detail accepts only complete 40- or
  64-character lowercase hexadecimal object IDs and checks that the requested
  commit is an ancestor of the saved immutable head. Newer, unrelated, missing,
  non-commit and revision-syntax inputs are rejected. Moving the branch or
  default ref does not widen an existing review.
- Git runs with replacement objects, lazy fetch, global/system configuration,
  external diffs and text conversion disabled. No browser-supplied path or ref is
  passed to Git. Existing process concurrency, timeout, output, file-count, blob,
  line and cache-size limits remain active.
- Parent navigation creates transient commit snapshots and does not overwrite the
  durable branch comparison. Every file-content request is resolved from the
  exact file IDs and object IDs produced by that immutable commit pair.
- Commit messages, paths, statuses and hashes enter the DOM through `textContent`
  or text nodes. Parent URLs use `URLSearchParams`, and the server independently
  revalidates their commit IDs and ancestry. The tree uses `Map`, including for
  components such as `__proto__` and `constructor`, so path components cannot
  mutate an object prototype.

## Compatibility and deployment assessment

- `parents` is an additive, non-null JSON array derived from the same native Git
  parse used for commit history and detail. The only in-tree consumer is the
  browser. Old browser code ignores the field, while new browser code checks
  `Array.isArray` and degrades to the previous heading when served by an old
  backend.
- The feature-history range remains `base..head`; only commit-detail admission is
  widened to the saved head's ancestry. Commit diffs continue to use the first
  parent, and root commits use the repository's object-format-correct empty tree.
- No schema, session manifest, lifecycle journal, URL key, Git retention policy,
  fetch behavior, package dependency or system configuration changes. Old
  packages retain readability of all canonical and private state. After rollback,
  URLs for commits outside the old feature range return unavailable until
  roll-forward, as recorded in the plan; they do not select a different commit.
- The downstream changes are mechanical pins. The organization flake selected the
  exact reviewed runtime, and the workspace lock selected that organization head
  and matching transitive runtime. All reviewed heads were present on their SSH
  remotes when checked. The planned runtime-to-organization-to-user-profile order
  is sufficient and does not require coordinated node updates or a migration.

## Direct remediation context

After the frozen packet, the scope lane requested that parent URLs omit the
redundant explicit `view=diff` key and assert that file, view, version and line
state are cleared. I inspected the narrow rewrite at runtime commits `9490e1e`
and `41c6d75`; it changes only browser route serialization and assertions,
reduces retained URL state, and does not alter the ancestry, authorization,
storage or deployment conclusions above. The root agent reported all 21 Chromium
checks passing after that rewrite.

## Residual risks and verification gaps

- Long package, live browser, deployment and manual rollback checks remain
  intentionally deferred until review reconciliation.
- The parent tests cover frozen-head restoration after both feature/default ref
  movement, both sides of a merge, root commits, missing objects, and newer and
  unrelated commits. They do not exercise a shallow or partially cloned canonical
  repository; under the no-fetch policy, a shallow-boundary parent can appear as
  unavailable or as a traversal endpoint.
- Root or historical first-parent diffs that exceed the existing file/output
  limits remain unavailable by design. The UI reports the bounded failure rather
  than fetching, retaining or partially presenting the object graph.
- The Chromium test uses mocked HTTP data while the Go tests exercise actual Git
  and request scoping separately. The planned live acceptance remains the
  end-to-end check of those layers and the exact deployed pins.
