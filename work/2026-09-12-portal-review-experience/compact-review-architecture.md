# Architecture and repetition review

Review result against the frozen packet revisions: **0 Blocking, 0 Important,
0 Advisory**.

Reviewed ranges:

- `dev-workspace`
  `41c6d75e8f7cdea1e5cbced7d0106d072d56484d..e35cf0b0bfc343d5a4d476340980e06ac252396b`
- `vpsfree-dev-workspace`
  `6c98b3676a46c9a9c2830198eae9042b064a71e7..2a3f442263ea614173c7eb540c55542a9373b71a`
- `workspace`
  `c6daa04a9cbf6ce8611c7ae38dcfc7c4cc7a5636..6f10c36642ecb290ee0699ecff965779f37b9702`
- `codex-web` unchanged at
  `de83e9c72dec6cb5ff8ec13d5b0b21ed60148117`

## Findings

No Blocking, Important or Advisory architecture/repetition findings were
identified.

## Architecture and consumer assessment

The generic runtime remains the sole owner of repository comparison rendering.
Commit `2414ffa` derives the compact directory tree directly from the existing
`payload.files` collection and reuses each file's existing section/navigation
record. Folder presentation is a local decorative SVG helper attached to native
`details` disclosures; it adds no icon registry, alternate tree model or hidden
extension interface. File status interpretation remains centralized in
`fileStatus`, and counts remain centralized in `countParts` while the tree simply
stops rendering those existing values
(`portal/internal/web/static/repository-review.js:15-29,65-87,487-545`). Header
path copying still uses the unchanged provider-owned `createCopyButton` callback
at the existing file-section boundary (`repository-review.js:505-512`).

Commit `e35cf0b` keeps comparison identity and controls in the runtime toolbar and
moves the already-owned commit/pair metadata into the diff pane. `comparisonTitle`
and `commitDetails` separate the compact label from the full details without
duplicating commit, parent or pair interpretation
(`repository-review.js:422-484`). The single `selectedFile` helper owns the new
rule that an absent file route implicitly selects the first file. Editor
retention, navigation highlighting, rendering, reveal and view application all
consume that helper (`repository-review.js:254-261,273-299,325-330,385-415`).
Thus ordinary comparison entry can keep the file out of the URL and stay at the
details, while explicit file/line routes continue through the existing
serializer and navigation path. There is no second selection state or parallel
history implementation that could drift.

The two runtime commits are independently coherent and ordered. `2414ffa`
contains the tree presentation change with its fixture assertions and
documentation. `e35cf0b` then changes scrolling and implicit entry with matching
fixture assertions and documentation. Neither commit depends on a downstream
implementation, and no unrelated framework or generalized abstraction was
introduced.

The actual dependency graph preserves existing ownership. `dev-workspace`
continues to import the unchanged `codex-web` revision and consumes only its
existing copy-control interface. `vpsfree-dev-workspace` calls
`dev-workspace.lib.mkPackage` and changes only its exact runtime URL and lock
entry to `e35cf0b`. The site continues to call the organization-owned `mkPackage`
with `siteConfig`; its URL and lock entries select `2a3f442`, whose nested lock
selects the same runtime. The organization and site ranges contain no duplicate
UI logic, wrapper behavior or new public contract. This keeps the established
one-way provider -> runtime -> organization -> site dependency direction and
does not require another consumer implementation.

## Residual validation gaps

- The component acceptance composes final runtime assets with real pinned
  CodeMirror, Shiki and `codex-web` copy controls, but its repository HTTP
  responses are fixtures. Exact packaged composition, installed-source checks
  and live-browser geometry remain for the planned post-review validation.
- The final browser fixture covers 30 files and the existing eight-editor
  retention bound, but it is not a 5,000-file stress test. The previously
  accepted extreme-directory-depth recursion limitation is unchanged by this
  range.
- Shallow-repository and live rollback exercises remain unclaimed. The URL and
  package contracts are unchanged, so these are validation gaps rather than
  architecture findings.
- Findings and line references apply to the frozen packet heads above. Any
  later test-only remediation commit and resulting downstream repins are outside
  this report and need focused coordinator verification; an architecture rerun
  is necessary only if those changes alter the reviewed UI, ownership or public
  contracts.
