# Architecture and repetition review

Reviewed the committed series recorded in `review-packet.md`:

- codex-web `ee9ab42791a84b79315d952501264a6cbafc8695..9151c2b862c04775f2562a77365103380772ee04`
- dev-workspace `8a43d3b09ddd9fa3b2c5f6c9aaba3ef7efc0ad0f..723ff4a79d2d6d705364fbfdfa7509337f4df8aa`
- vpsfree-dev-workspace `37f3bfa21079b217aef15a4c2e75ed7451b9d156..71229ca9c0ea5a3cd0af6e6bf1e2b6d283d95c92`
- workspace `5d5137959467555675529aeab7df91c719b8a0c4..569a71dae07e71f7a369451f31579f69f2ebed2f`
- vpsfree-cz-configuration `b0252827958a4cc231a2a0bb56ae3a1844db8ae8..6cb0894a958a67357c7b72f230c4675dd4590a9f`

The synchronization owner is codex-web's `conversation/assets/sync.js`, exported
through `conversation.js`. The two browser consumers found from imports and
mounting code are codex-web's `mountConversation` reference interface and
dev-workspace's `portal/internal/web/static/app.js`. dev-workspace pins the same
codex-web revision in its Go module and flake; vpsfree-dev-workspace, workspace,
and vpsfree-cz-configuration propagate the runtime through their flake inputs.
Repository review history, summaries, comparisons, and their single/batch HTTP
contracts are owned by dev-workspace.

## Findings

### Blocking: the heartbeat interval has several independent owners, and the tests do not detect their drift

Commit: codex-web `9151c2b862c04775f2562a77365103380772ee04`.

`conversation/handler.go:826` creates the real ticker with a literal 20-second
period, while `conversation/handler.go:834` separately advertises a literal
`heartbeatIntervalMs: 20000`. The browser does not use the advertised interval;
`conversation/assets/sync.js:144-147` merely enables enforcement when it equals
another literal `20_000`, then `conversation/assets/sync.js:183-186` applies an
independent fixed 45-second watchdog.

The tests mirror these declarations rather than bind them together.
`conversation/events_test.go:29-55` injects a manually ticked channel into
`streamEvents`, so it never verifies that the production ticker matches the
advertisement. `test/sync_browser_contract_test.cjs:48-50` always supplies the
expected 20,000-ms advertisement. A later server change to a 30-second ticker
and advertisement can therefore pass its Go test and the unchanged browser
suite independently, while real clients silently classify the new server as a
legacy server and stop detecting dead streams. Changing only the ticker to a
period beyond the fixed browser watchdog instead produces repeated healthy
connection teardown. This is newly introduced duplication in an event protocol
that can silently diverge, which is Blocking under the architecture lane rules.

Make the wire advertisement authoritative. At minimum, one Go duration should
drive both the production ticker and encoded advertisement, and the browser
should validate and use the advertised positive interval to derive its stale
deadline with a documented tolerance. Add a contract case with a non-default
valid interval so the browser behavior cannot remain accidentally coupled to
20 seconds.

### Blocking: batched history manually republishes the single-response contract field by field

Commit: dev-workspace `1045034439cb3ec276296cacdd71711bcb8d1794`.

`portal/internal/web/repository_review.go:176-188` already defines the typed
`reviewHistoryResponse`, including its `Repository` field and the new `Summary`
and `SummaryError` fields. In contrast,
`portal/internal/web/repository_review_batch.go:63-85` constructs an untyped map
and copies `repository`, `review`, `snapshot`, `pair`, and `history`, then copies
`summary` and `summaryError` in two more conditionals. This commit demonstrates
the coordinated edits the abstraction requires: adding the two fields to the
single response also required remembering the separate batch serializer.

The tests establish the present summary values, but do not provide complete
bidirectional coverage. `portal/internal/web/repository_summary_test.go:29-34`
compares only `Summary`, and the existing batch test at
`portal/internal/web/repository_review_followup_test.go:119-128` checks selected
fields. JSON decoding into `reviewHistoryResponse` also cannot reveal a field
that the batch map omitted. A future additive field can therefore work for the
single endpoint and silently disappear from the batch endpoint, violating the
explicit single/batch parity contract. This is newly expanded duplication in a
public API contract and is Blocking under the architecture lane rules.

Use the same typed success payload for both endpoints, setting its
`Repository` field for the batch item, with a typed envelope only for the
per-item error variant. If field-wise translation must remain, add exhaustive
JSON-level parity coverage that fails for either missing or extra success
fields.

### Advisory: the shared connection renderer contains portal-specific policy text

Commit: codex-web `9151c2b862c04775f2562a77365103380772ee04`.

`conversation/assets/sync.js:230-237` is a shared provider and is documented for
custom interfaces in `README.md:208-229`, but its 401/403 message says `Portal
access denied. Sign in again, then retry.` The provider's own representative
consumer at `cmd/codex-web-example/main.go:22-37` is a loopback standalone Codex
conversation with no portal or sign-in flow. A capability or authorization
failure there therefore gives users an action that does not exist. Use neutral
provider text, or let the embedding application supply authorization/error
labels while retaining the shared state and renderer behavior.

## Positive architecture observations

- The recovery state machine is centralized in codex-web and both current
  browser interfaces adapt their own snapshot/rendering behavior to it; the
  portal does not carry a second retry/backoff/EventSource implementation.
- Repository net statistics reuse `comparisonFiles` and the existing immutable
  base/head cache, while `repository.FileStats` remains the sole stats reducer
  for the history summary and comparison response.
- Pagination visibility is a single browser rule (`historyHasPages`) and the
  downstream flake revisions consistently select the reviewed provider and
  runtime heads.

## Residual gaps

- Consumer discovery covered the checked-out workspace repositories, imports,
  reference application, Go/Nix pins, wrappers, and documentation. Other
  external users of the public codex-web assets cannot be enumerated from this
  workspace.
- Long browser acceptance and package/deployment checks were deliberately not
  run in this lane. The planned Firefox/Chromium outage tests remain necessary,
  particularly for EventSource behavior, BFCache restoration, and preservation
  of portal drafts and scroll state under real DOM timing.
- This review did not modify implementation.
