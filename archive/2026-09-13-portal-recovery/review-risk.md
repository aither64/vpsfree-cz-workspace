# Risk and compatibility review

Reviewed with the `mandatory-change-review` risk and compatibility lane using
`gpt-5.6-sol` at `xhigh` effort. The review covered the committed series and
repository guidance at these packet heads:

- codex-web `ee9ab42791a84b79315d952501264a6cbafc8695..9151c2b862c04775f2562a77365103380772ee04`
- dev-workspace `8a43d3b09ddd9fa3b2c5f6c9aaba3ef7efc0ad0f..723ff4a79d2d6d705364fbfdfa7509337f4df8aa`
- vpsfree-dev-workspace `37f3bfa21079b217aef15a4c2e75ed7451b9d156..71229ca9c0ea5a3cd0af6e6bf1e2b6d283d95c92`
- workspace `5d5137959467555675529aeab7df91c719b8a0c4..569a71dae07e71f7a369451f31579f69f2ebed2f`
- vpsfree-cz-configuration `b0252827958a4cc231a2a0bb56ae3a1844db8ae8..6cb0894a958a67357c7b72f230c4675dd4590a9f`

## Findings

### Important: a failed grouped read does not cancel its still-running siblings

At codex-web commit `9151c2b862c04775f2562a77365103380772ee04`,
`conversation/assets/sync.js:88-119` records a read or apply failure and then
clears the cycle's 35-second deadline, but it does not abort the cycle's
`AbortController`. A grouped `read` commonly rejects as soon as one member
fails while leaving the other promises running. Releasing `active` also lets
the retry schedule start another cycle while those operations still use the
old live signal.

The concrete consumer at dev-workspace commit
`723ff4a79d2d6d705364fbfdfa7509337f4df8aa`,
`portal/internal/web/static/app.js:2881-2887`, starts thread and pending GETs
concurrently with `reconcileQueue`. If either GET rejects quickly while queue
reconciliation stalls, the snapshot reports failure and retries but never
cancels the old reconciliation request. `reconcileQueue` is a POST and
therefore has no independent browser deadline in
`conversation/assets/conversation.js:210-239`. Repeated backoff attempts can
overlap reconciliation mutations and occupy the server mutation lock. The
current handler's 30-second operation timeout limits the bundled server, but
that does not satisfy the public controller's cancellation contract and does
not protect custom clients or servers.

Abort the cycle signal on any read or apply failure before clearing its timer,
while retaining the original error for the freshness notice. Add a contract
test in which one grouped child rejects and another child observes that its
signal was aborted. This is a partial-failure and resource-safety issue in the
explicit bounded-refresh contract; it should be fixed or explicitly accepted
before integration tests.

### Important: a send during an existing refresh can leave acknowledged text available for duplicate submission

At codex-web commit `9151c2b862c04775f2562a77365103380772ee04`,
`conversation/assets/sync.js:72-75` makes `refresh()` return the currently
active refresh promise and merely marks a later refresh dirty. The follow-up is
scheduled asynchronously after that active cycle succeeds at
`conversation/assets/sync.js:112-119`. In the mounted UI,
`conversation/assets/conversation.js:800-810` sends the message, awaits
`refresh()`, and clears the textarea only when the durable sender is no longer
pending.

If a periodic or event-triggered snapshot started before the send, that
snapshot cannot contain and acknowledge the newly accepted message. The submit
handler consequently returns with the submitted text still in the composer.
The dirty follow-up can later acknowledge the message and remove its durable
attempt, but no later path clears the matching textarea. Pressing Send again
then creates a new client message ID and submits the same text a second time.
The race is especially plausible because the event emitted by the accepted
send or the 60-second poll can overlap the POST response.

Clear only the exact, still-unchanged composer value when the authoritative
transcript acknowledgement retires that same durable attempt. Do not erase
edits made while acknowledgement is pending. Add a mounted-browser regression
test with a pre-send refresh, a stale first snapshot, a dirty follow-up that
contains the message, and an edit-during-ack case. This affects the required
submission and receipt semantics and should be fixed or explicitly accepted
before integration tests.

## Compatibility and security assessment

No authorization or tenant-boundary regression was found. Repository summaries
continue to resolve registered repositories and server-owned immutable
base/head object IDs; the new count command does not accept a browser-supplied
path or revision. Summary errors are mapped to existing generic review errors
rather than exposing Git diagnostics. The SSE payloads are constants and the
existing exact-origin, conversation resolution, thread verification, and
capability checks remain in front of the event endpoint.

The repository `summary` and `summaryError` fields are additive. Both single
and batch handlers call the same history implementation, and totals share the
same frozen pair as history and comparison files. The cache keys include the
canonical repository directory and immutable base/head. Old browsers ignore
the fields; new browsers render an unavailable state when an old server omits
them. Pagination retains Previous on later pages and is absent only when page
zero has no next page.

The named SSE `ready` and `heartbeat` events preserve the existing unnamed
`data: update` hints. Old EventSource consumers ignore unfamiliar named events,
while the new controller enforces heartbeat freshness only after the server
advertises the exact supported interval. With an old server, periodic snapshots
remain the recovery path. No App Server protocol, persisted state, receipt
format, schema, host option, ownership rule, or lifecycle journal changes were
introduced, so rollback needs no data conversion and does not require a
coordinated node rollout.

The dependency chain is internally consistent at the reviewed commits:
dev-workspace pins codex-web `9151c2b`; vpsfree-dev-workspace pins dev-workspace
`723ff4a`; workspace pins vpsfree-dev-workspace `71229ca`; and the generated
configuration update pins its host-module input to dev-workspace `723ff4a`.
The application remains selected through the workspace user-profile package,
so the recorded user-profile-first, host-configuration-second order is the
appropriate deployment order. Reversing both to the recorded generations does
not require state rollback.

## Residual gaps

- The packet records focused Go and Node checks and provider CI, but downstream
  flake/package checks, current-head CI, system build, dry activation, and the
  authorized aitherdev switch were still pending at this review point.
- Actual Firefox and Chromium validation against served modules, proxy-carried
  heartbeats, offline/silent-stall injection, BFCache/wake behavior, composer
  and pending-answer preservation, and rollback remained pending. These tests
  are needed after the Important findings are resolved.
- The tests cover controller races in isolation and the shipped module capture,
  but did not cover either concrete failure above at the mounted consumer
  boundary.
