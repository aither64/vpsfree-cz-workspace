# Upload display and prompt file limits

Design owner: architect0, retained GPT-6 Astra / xhigh. This implements the
accepted [plan](plan.md). The coordinating lead assigns implementation and owns
tracking, verification execution and delivery. This brief is source inspection
and planning only; no application edits or checks have been performed.

Inspected bases: codex-web `32775fa7fdd9bc9b41aef74b7f195e5c3bc0f8d5` and
dev-workspace `6a972b9ab01077611b2c60e0fc726c185e050315`, in this initiative's
isolated worktrees. Both worktrees were clean at inspection.

## Scope and implementation contract

1. **Shared selection summary.** In codex-web's
   `conversation/assets/uploads.js`, `mountUploads` renders a summary beside its
   notice/list, inside the upload root. Hide it when selection is empty. For
   nonempty selection show `N file(s) · SIZE total`, using singular for one file
   and the existing `fileSize` formatter. Append ` · K of N complete` only while
   `K < N`.

   `N` is all retained selection entries; SIZE is the sum of their full `size`
   values, never transferred bytes or offsets. `K` counts `state === "ready"`,
   which means acknowledged completion. A zero-byte upload counts as selected
   immediately and complete only after acknowledgement. Paused, failed-transfer,
   missing and deleted entries remain in the total until removed. An entry
   awaiting removal remains selected; a failed removal of a ready file does not
   undo its completed upload. Existing readiness/error/persistence checks still
   govern submission independently of this display.

   Update the summary through the existing render path, covering picker/drop,
   transfer completion, retry, removal, restoration, clear and locking. Keep
   error notices distinct. Reuse the component's muted text styling, with a
   dedicated summary class if needed in `uploads.css`. Preserve hidden-root and
   external `controlsRoot` behavior, adjacent controls and destroy cleanup.
   No new options, callback fields or serialized draft fields are needed.
   `renderAttachments` and submitted transcript cards are outside this change.

2. **Creation-only growth.** Add a specific rule in dev-workspace's
   `portal/internal/web/static/style.css` for
   `#creation-uploads.codex-upload-composer`: `max-height: none` and
   `overflow-y: visible`. Its specificity must win even though shared uploads
   CSS loads later. Keep all creation cards in normal document flow and preserve
   the existing form/action ordering. Leave codex-web's shared 12rem cap and
   conversation `#message-uploads` unchanged. Do not introduce a global layout
   option, resize observer, pagination or another scrolling container.

3. **50 prompt files.** Change dev-workspace's default in
   `portal/internal/uploads/store.go` from 10 to 50. Use one named Go default
   (for example `uploads.DefaultPromptFiles`) for `DefaultLimits().Files` and
   the persisted/input attachment count check in
   `portal/internal/web/preparation_store.go:validatePreparation`. This is the
   default supported preparation bound; per-store custom limits remain enforced
   by the store. Change `normalizeDraft` in
   `portal/internal/web/static/preparation.js` to accept up to 50 ordered IDs.
   Its schema, UUID, duplicate, scope, body and field-presence validation stay
   intact. The generic upload picker already reads `limits.files` from the
   server; it does not need a second default.

   The same default applies to creation, sending, steering and queuing. Existing
   `prepareSubmission` count/byte enforcement remains authoritative. Accepted
   preparation replay still resolves the original request before consulting
   current upload state; do not change its identity or recovery ordering.

## Interfaces, files and boundaries

| Owner | Expected touched files |
| --- | --- |
| codex-web | `conversation/assets/uploads.js`, optional summary styling in `uploads.css`, `conversation.js` import/export versions, `test/uploads_browser_contract_test.cjs`, `docs/reference.md`; CSS entrypoints only as required for cache invalidation |
| dev-workspace limits/recovery | `portal/internal/uploads/store.go`, `portal/internal/web/preparation_store.go`, `portal/internal/web/static/preparation.js`; existing upload/preparation Go tests and `preparation_browser_contract_test.cjs` |
| dev-workspace integration/layout | `portal/internal/web/static/style.css`, `static/app.js` asset import, affected `templates/*.html` asset references, `test/creation_browser.cjs`, `test/README.md` if its instructions change |
| Dependency and documentation | `portal/go.mod`, `portal/go.sum`, `flake.nix`, `flake.lock`, `nix/workspace-portal.nix` vendor hash; `README.md` prompt attachments and `docs/session-preparations.md` compatibility guidance |

Public JSON names and shapes stay unchanged, including `limits.files`,
attachment arrays and creation status. Catalog schema 1, preparation schema 1,
input digest version 1 and browser preparation schema 2 remain unchanged.
Preserve ordered attachment IDs, UUIDs, exact serialized attempted POST bodies,
scope ownership, immutable prompt references, pending retention, same-origin
checks, locks and package-generation checks.

Keep the generic codex-web Go/JS 100-ID ceiling and 100-entry generic draft
validation unchanged, including legacy browser-selection detection. Keep 1,000
stored files per scope and 10,000 records per catalog category. Byte quotas stay
1 GiB/file, 2 GiB/prompt, 10 GiB/session and 100 GiB/workspace; 4 MiB chunks,
two browser transfers, eight server chunks, free-space reservations, catalog
bounds and retention policies also stay unchanged. Existing tests deliberately
using a custom 10-file limit need not be changed to the new default.

No upload transport redesign, prompt-reference format change, naming change,
new recovery route, schema migration, lifecycle helper, NixOS/module change,
CLI/Terraform/client generation or node update is in scope. Route any need to
change these boundaries through the lead.

## Actual 50-file capacity and remaining bounds

There is no additional fixed count ceiling below 50 in the inspected submission
path after the three count checks above are aligned. Count acceptance is still
conditional on the existing byte limits. In particular, `prepareSubmission`
builds the actual initial goal/message as:

```text
TrimSpace(prompt + "\n\nAttached local files (inputs; keep these files outside version control):\n"
          + JSON.MarshalIndent([{name, size, path}, ...], "", "  "))
```

That UTF-8 wire string must fit `session.MaxMessageBytes == 20_000`. Each file
contributes its JSON-escaped name, byte count and absolute storage path. Storage
uses `<upload-root>/files/<UUID>/file<restricted-extension>`, not the full name.
Fifty short names with a short prompt and an ordinary state path can fit; fifty
255-byte names, JSON escape expansion, a long state root or substantial prompt
text can exceed the limit even when all upload byte quotas pass. The existing
"Message and attachment references exceed the prompt limit" rejection is
intentional. Verify one real 50-file creation case and an over-bound reference
case; do not promise every otherwise valid set of 50 can be submitted.

The form body also retains its existing 61,024-byte bound
(`20_000 * 3 + 1_024`). Fifty repeated `attachmentIds` fields occupy about
2.55 KiB before other fields. Normal short creation requests fit; encoded
near-limit text/settings can still hit this transport bound. Do not raise it or
the 20,000-byte wire limit in this initiative. Document the prompt/reference
bound in the attachments guidance; reduce prompt length or selected files when
it is exceeded. Do not truncate references, omit files or silently retry a
different request.

## Compatibility, rollout and recovery

New code reads existing records/drafts unchanged. Old clients with the old
preparation script retain their 10-ID recovery check; they require refreshed
assets to use the expanded creation flow. New clients talking to the older
backend must continue respecting its advertised 10-file limit. There is no new
protocol field or App Server request shape.

The immediately preceding dev-workspace reader validates full preparation
snapshots with `len(attachments) <= 10`. An unfinished 11–50-file record is
therefore unreadable to that reader; catalog schema compatibility alone does
not make a software downgrade safe. Before evaluating older-reader
compatibility, finish/recover those requests under the new reader, let normal
terminal compaction durably replace/move them into
`session-preparation-mappings/`, and clear tab drafts through the normal
identity-confirmed acceptance/cleanup flow. Merely reaching handoff or obtaining
a ready receipt is insufficient evidence of compaction. Terminal mappings have
no snapshot/attachment list and the older validator accepts their unchanged
shape. Ready compaction still requires creation proof and upload binding.

Do not hand-edit/delete an unfinished record, discard a browser draft or release
uploads to force compatibility. Failed/pre-reservation records that cannot reach
normal compaction require keeping a reader that supports 50. Completed session
records and upload catalogs retain their formats and files. An older package may
again reject a new submission of more than 10 files, including submission replay
paths subject to its store count check.

These are data compatibility prerequisites, not authorization or a new downgrade
procedure. The current workspace package switch policy is forward-only:
operational recovery retains the new package or uses a newer compatible package.
Do not bypass that policy or run an installed-package downgrade as a test.

Integrate the provider into the runtime in dependency order: commit codex-web,
then pin dev-workspace's Go module and Nix input to the same exact feature
revision and refresh its vendor hash. Package/deploy as one coherent user-profile
runtime when separately authorized; no system configuration or node fleet
deployment is required. This brief authorizes no deployment or merge.

Browser cache chain to update together:

- `uploads.js?v=3` -> a new token in both import and re-export in
  codex-web's `conversation.js`.
- dev-workspace `app.js` imports `conversation.js?v=11`; advance that token and
  its parents, `app.js?v=21` in index/session templates.
- `preparation.js?v=2` advances in index and creation templates; `style.css?v=3`
  advances at every existing template reference when the creation override is
  added.
- If shared `uploads.css` changes, advance direct `uploads.css?v=2` consumers
  and cover the other entry path, `conversation.css`'s `@import` of uploads CSS:
  version the import and refresh its host entrypoint URLs. Preserve unrelated
  asset versions. External codex-web hosts own their entrypoint cache policy.

## Acceptance and verification plan

The implementer adds focused regressions to existing fixtures. These are planned
checks, not passing evidence. Run quick checks in the repositories' declared Nix
tool environment; Go browser-contract tests must find Node and must not skip.

- **Selection behavior:** use the shipped `mountUploads` fixture, not a duplicate
  reducer. Assert empty hidden state, singular/plural and binary formatting,
  zero-byte files, full total during partial progress, acknowledged completion,
  retry/failure, failed and successful removal, restored entries, lock/unlock,
  clear after accepted submission and external controls. Update positional DOM
  fixture assumptions if the summary adds a child. Keep readiness and existing
  removal/persistence regressions passing.
- **Count and quota behavior:** a store using the real default accepts 50 small
  ready files and rejects 51; exercise preparation claim and ordinary prompt
  submission. Retain byte-quota rejection and test reference expansion beyond
  20,000 bytes. Generic ID helpers retain 100/101 behavior. Small synthetic
  uploads suffice; allocating GiB fixtures is unnecessary.
- **Durability:** accept and reload a full preparation containing 50 attachments;
  identical POST/status/retry retains request ID, receipt, ordered IDs and wire
  text. Preserve conflict for reordered/changed input. Browser attempted draft
  with 50 IDs survives response loss/reload and 404 recovery resends the exact
  body; 51, duplicate/malformed IDs and mismatched bodies remain rejected.
  Cover terminal compaction dropping the snapshot and normal draft cleanup.
- **Quick commands:** codex-web `node --test
  test/uploads_browser_contract_test.cjs`, `go test ./conversation`, and syntax
  checks for changed JS; dev-workspace, from `portal/`, focused upload tests and
  web selectors for `TestSessionPreparation`, `TestDraftUploadHTTP` and
  `TestShippedBrowserClientMatchesSessionAPI`. Include the newly added tests in
  selectors and record nonzero execution. Read source/diff for unchanged schema,
  quota and 100-ID bounds. Do not run full integration suites as quick checks.
- **Post-review checks:** after all intended changes are committed, quick checks
  pass and independent final review is resolved, a fresh utility watcher runs
  the selected packaged checks (`nix flake check --print-build-logs` per repo)
  and extended `test/creation_browser.cjs` with explicit `PLAYWRIGHT_MODULE`,
  `CHROMIUM_EXECUTABLE` and `CODEX_WEB_SOURCE` matching the pinned provider.
  The browser fixture currently does not load production CSS; extend its asset
  serving/markup to load both actual stylesheets before claiming layout evidence.
  At desktop and narrow widths, use 50 cards and long names, verify the creation
  root has no internal vertical scrollbar, and scroll the page to reach every
  action and Create session. Check computed styles/overflow, summary transitions,
  51st-file rejection and the unchanged conversation cap. This local fixture
  performs no live Codex inference.

For older-reader evidence, use an isolated fixture at the recorded dev-workspace
base to establish rejection of an unfinished >10 snapshot and acceptance of its
new-code-compacted terminal mapping. Do not use the existing preparation
compatibility runner's older `924c0ec...` baseline as proof of this specific
boundary: it predates the preparation reader. Run any cross-version harness
only in the post-review stage; no installed runtime is switched.

## Focused commit split and documentation

1. codex-web: shared summary, browser regressions, cache references and generic
   upload contract in `docs/reference.md`.
2. dev-workspace: 50-file defaults, preparation/browser validation and recovery
   regressions; update README limits/reference bounds and preparation reader
   compatibility guidance.
3. dev-workspace: creation-only layout, matching provider Go/Nix pins and vendor
   hash, host asset versions and browser/layout coverage. Include the user-visible
   display explanation in README. Keep no temporary path/module replacement.

The lead/implementer applies the user-facing writing skill to final interface
copy and public prose. No vpsAdmin WebUI or KB page is affected. Review uses the
complete final series/diffs with an explicit no-migrations conclusion; it is not
part of this design assignment. The lead records actual checks, exact revisions,
review and any later rollout in state and keeps the initiative active pending
explicit repository/target integration direction.
