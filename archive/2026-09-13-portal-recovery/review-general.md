# Mandatory change review: General lane

Reviewed the committed series and final trees described in `review-packet.md`:

- codex-web `ee9ab42791a84b79315d952501264a6cbafc8695..9151c2b862c04775f2562a77365103380772ee04`
- dev-workspace `8a43d3b09ddd9fa3b2c5f6c9aaba3ef7efc0ad0f..723ff4a79d2d6d705364fbfdfa7509337f4df8aa`
- vpsfree-dev-workspace `37f3bfa21079b217aef15a4c2e75ed7451b9d156..71229ca9c0ea5a3cd0af6e6bf1e2b6d283d95c92`
- workspace `5d5137959467555675529aeab7df91c719b8a0c4..569a71dae07e71f7a369451f31579f69f2ebed2f`
- vpsfree-cz-configuration `b0252827958a4cc231a2a0bb56ae3a1844db8ae8..6cb0894a958a67357c7b72f230c4675dd4590a9f`

I read the initiative plan/state, every repository-local `AGENTS.md`, commit
messages, complete changed-file lists, implementation context, tests,
documentation, and downstream dependency pins. The remote feature branches
resolve to each packet head. The commit series is focused and reviewable: the
provider's SSE and synchronization contract ships with its mounted consumer,
tests, and documentation; the runtime keeps the independent repository-summary
behavior separate from the recovery consumer and its required provider pin;
the remaining commits are isolated generated or package pin propagation. I
found no commit-split or commit-message finding.

## Findings

### Blocking: a failed refresh releases its gate without cancelling unfinished sibling work

Commit `9151c2b862c04775f2562a77365103380772ee04` clears the cycle deadline in
`conversation/assets/sync.js:104-119` after `options.read()` rejects, but it
does not abort `cycle.abort`. A `Promise.all` read can therefore reject because
one operation failed while another operation remains alive with a signal that
will never reach the controller's 35-second deadline.

Commit `723ff4a79d2d6d705364fbfdfa7509337f4df8aa` exercises exactly that shape in
`portal/internal/web/static/app.js:2883-2887`: thread, pending requests, and
queue reconciliation are sibling work. Queue reconciliation is a POST. In the
pinned provider, `conversation/assets/conversation.js:213-239` applies the
client deadline only to GET requests, so `reconcileQueue({signal})` depends
entirely on the synchronization cycle signal for cancellation.

If thread or pending fails quickly while reconciliation stalls, the controller
reports failure, clears its active gate, and retries, but the stalled
reconciliation remains alive. Each later backoff attempt can add another stuck
POST. This violates the accepted requirement that queue reconciliation remain
inside the bounded snapshot refresh and can accumulate browser requests and
server/App Server work throughout an outage.

I reproduced this against the committed provider with Node 24 by returning
`Promise.all([Promise.reject(...), new Promise(() => {})])` from `read`. After
the refresh settled, the captured cycle signal still reported
`abortedAfterFailure: false`. The existing single-read timeout contract in
`test/sync_browser_contract_test.cjs:57-71` cannot detect this sibling leak.

Abort the cycle signal whenever a refresh cycle settles, including the early
failure path, so any unfinished work receives cancellation before the gate is
released. Add a regression contract with one immediate rejection and one
stalled signal-aware sibling; for the runtime consumer, cover stalled
reconciliation alongside a failed thread or pending request.

## Residual gaps

- Long browser acceptance has not started. The planned Firefox and Chromium
  tests remain necessary for real EventSource behavior, sleep/timer suspension,
  BFCache restoration, composer and attachment preservation, request-answer
  drafts, scroll retention, and the actual portal DOM.
- The lane did not repeat the recorded full Go and Node suites. It confirmed
  the reported commit ranges and test sources and ran the focused failure probe
  above. Package/flake checks, CI for every downstream head, system build, dry
  activation, deployment, and rollback validation remain pending as recorded
  in the packet.
- Repository totals have focused unit/API coverage for page boundaries, net
  changes, renames, binary files, rebases, integrated comparisons, batching,
  and limit failure. Their final narrow-layout and browser interaction behavior
  remains part of the planned browser acceptance.
