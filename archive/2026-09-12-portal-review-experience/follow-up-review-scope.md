# Follow-up scope and proportionality review

Lane: scope and proportionality
Risk: High
Reviewer: `gpt-5.6-sol`, `xhigh`
Review date: 2026-09-12

Reviewed the complete frozen commit series and final trees at:

- `codex-web` `83770217d63f2c206689d2c569e1c81950544504..de83e9c72dec6cb5ff8ec13d5b0b21ed60148117`
- `dev-workspace` `d3bfd0f5a7c419c9df0ed53aa5f1acb77f8e10c2..ebc0e4a71b01e81d0d90a29b0ca7385a61b1bdd1`
- `vpsfree-dev-workspace` `a30de6c62d2bcd1ff41ee48018c595140c6d4042..534d0f2c5530bbbbf36d8254d282a9945cef9bfc`
- workspace `5dbe312b1edf6a4454c4e86ec06f68baa3b5f4b4..77ca31a5e3e5e4f44c907b34b0f30bd99aec6980`

I compared the changes with `plan.md`, `follow-up-plan.md`, the review packet,
the local repository rules, focused tests, and current consumers. I inspected
the commit sequence as well as the final trees. The already accepted commit
bundling and dependency-order problem is not repeated here; the coordinator is
reconstructing that series separately.

## Findings

### Important — opening the repository overview eagerly loads and initializes the complete syntax stack

- Files: `portal/internal/web/static/repository-review.js:74-78`;
  `portal/review-ui/highlight-client.js:22-24,37-44,76-77`;
  `portal/review-ui/highlight.js:33-41`
- Commit: `5eeed4e3759c37050d9bab3719c1af4e9a67906c`

`mount` runs when the Repositories tab becomes active. It immediately imports
`review-editor.js` and calls `preloadReviewEditor`, even if the user only wants
to read commit histories, copy a hash, or inspect branch status. The warm-up
request constructs the worker and initializes all bundled Shiki grammars. The
reviewed Nix output measures 270,600 bytes for `review-editor.js` and 2,442,923
bytes for `review-highlight-worker.js`, so an overview-only visit fetches and
parses about 2.7 MiB and leaves a grammar worker resident before any source is
shown.

This is outside the smallest supported path. The approved plan explicitly says
to lazy-load the CodeMirror assets (`plan.md:52-54`), and the follow-up retains
CodeMirror while making plain source available before asynchronous syntax. The
existing `renderFile` path already imports the editor when it has actual file
content, and `highlightSource` can start the worker for the first source that
has a recognized language. There is no acceptance criterion or measured need
for warming all grammars while the user remains on the history overview.

Remove the unconditional import/warm-up from `mount` and let the first file
render start the editor and worker. If prefetching is deliberately preferred
for a measured first-comparison latency goal, record that as an explicit change
to the lazy-loading decision and defer only after the browser is idle. Add a
focused browser request-boundary check that the editor and worker are not
requested while only the overview is used.

### Advisory — the new copy-button API exposes two equivalent callback forms

- Files: `conversation/assets/conversation.js:146,178-183,195-198`;
  `README.md:191-193`
- Commit: `de83e9c72dec6cb5ff8ec13d5b0b21ed60148117`

`createCopyButton` accepts either a callback in `text` or a callback in
`getText`, then documents and tests a precedence rule when both are present.
The runtime uses `text: () => location.href`, while the transcript wrapper uses
`getText: () => transcriptEntryCopyText(entry)`. Both cases need the same
on-click evaluation behavior, and this export is new, so no earlier public
consumer requires two names.

Keep one input shape: for example, let `text` remain a string-or-callback and
change the transcript wrapper to pass its callback through `text`. Removing
`getText` and its precedence rule before release leaves a smaller public
contract and avoids two equivalent conventions spreading to future consumers.

No Blocking findings were found.

## Proportionality and consumer assessment

- Native Git remains the appropriate owner for history, object access, rename
  detection and raw/numstat output. The custom parser is required to preserve
  modes, object IDs, unusual paths, renames and nullable binary counts in the
  requested single command; introducing a second Git implementation would be
  broader.
- The ephemeral snapshots, persisted review descriptors, old saved-pair
  records and immutable response cache serve different current contracts:
  issued commit/file membership, restart-safe exact links, rollback and old
  client compatibility, and repeated-read latency. Their separation is
  justified by the requested frozen-link and compatibility boundaries.
- Single endpoints remain for compatibility; the bounded history, state and
  file batches have current browser consumers. The shared Git-process budget,
  request admission, coalescing and cancellation address authenticated but
  untrusted remote request concurrency rather than hypothetical hostile local
  operator behavior.
- The custom unified projection is justified by the accepted requirement for
  independent old/new syntax context and line anchors. It delegates diff
  construction to public CodeMirror `Chunk.build` output and does not reproduce
  a general diff engine.
- The selected grammar set maps to the languages used across the workspace's
  declared project portfolio. Unknown inputs fall back to plaintext; the
  implementation does not add dynamic grammar loading, CDN, WASM, evaluation,
  an icon library, or another Git dependency.
- The provider-to-runtime-to-organization-to-workspace dependency direction is
  unchanged. The downstream commits contain only exact pin propagation, and no
  unrelated configuration or deployment integration is present.

## Residual risks and verification gaps

- Findings and line numbers refer to the frozen packet heads. The reconstructed
  runtime series was still in progress during this lane; final tree equality,
  clean committed ranges, functional intermediate commits, and exact downstream
  pin propagation remain coordinator checks. This review does not repeat the
  accepted series finding.
- Other review lanes identified direct fixes that are being folded into their
  owning reconstructed commits. They were outside the frozen trees and were not
  credited here. A scope rerun is needed only if reconciliation broadens a
  product contract or introduces a new mechanism.
- Long Nix package/VM tests, full-handler live browser checks, deployment and
  old/new profile validation remain intentionally deferred until findings are
  reconciled.
- Existing Chromium acceptance opens a comparison and therefore does not prove
  the overview-only asset boundary described above. Its API is mocked while the
  Go tests exercise Git, persistence, authorization, cache and cancellation
  separately; post-review integration still needs to compose those layers.
- Durable review links intentionally depend on locally retained Git objects.
  Supporting automatic fetch or object retention would broaden the approved
  contract and is not recommended to close that accepted availability limit.
