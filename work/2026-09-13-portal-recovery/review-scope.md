# Scope and proportionality review

Reviewed the committed series recorded in `review-packet.md`:

- codex-web `ee9ab42791a84b79315d952501264a6cbafc8695..9151c2b862c04775f2562a77365103380772ee04`
- dev-workspace `8a43d3b09ddd9fa3b2c5f6c9aaba3ef7efc0ad0f..723ff4a79d2d6d705364fbfdfa7509337f4df8aa`
- vpsfree-dev-workspace `37f3bfa21079b217aef15a4c2e75ed7451b9d156..71229ca9c0ea5a3cd0af6e6bf1e2b6d283d95c92`
- workspace `5d5137959467555675529aeab7df91c719b8a0c4..569a71dae07e71f7a369451f31579f69f2ebed2f`
- vpsfree-cz-configuration `b0252827958a4cc231a2a0bb56ae3a1844db8ae8..6cb0894a958a67357c7b72f230c4675dd4590a9f`

The review used the immutable commit objects because remediation of other
review findings made the codex-web and dev-workspace worktrees dirty while this
lane was running.

## Finding

### Advisory: transient EventSource reconnection is reimplemented by the application

Commit: codex-web `9151c2b862c04775f2562a77365103380772ee04`.

`conversation/assets/sync.js:155-163` handles every EventSource `error` by
closing the source, discarding it and scheduling a newly constructed source
through the controller's own exponential backoff. This treats a normal
transient disconnect and a permanently closed source identically. The browser
platform already owns transient EventSource reconnection and exposes
`readyState` to distinguish `CONNECTING` from `CLOSED`; its processing model
also permits browser-managed backoff and waiting for operating-system network
recovery. See the [WHATWG EventSource processing model](https://html.spec.whatwg.org/multipage/server-sent-events.html#processing-model).

The application still has concrete reasons to recreate a source after a
heartbeat deadline, wake/BFCache recovery, or a permanent `CLOSED` state, and
it must retain its independent bounded snapshot retry. Replacing transient
browser reconnection as well adds another reconnect policy, timer interaction
and failure path without extending the supported recovery contract. It can
also discard any future server-supplied EventSource retry or last-event state.

The test at `test/sync_browser_contract_test.cjs:95-103` encodes the broader
behavior by firing a generic `error` on a fake source with no `readyState`, then
requiring a second source. The smaller contract is to leave a `CONNECTING`
source to the browser and explicitly recreate only `CLOSED` or watchdog-expired
sources. Model both states in the fake. This is Advisory because the extra
surface is localized and does not prevent the requested snapshot recovery.

## Proportionality observations

- The synchronization controller's wake signals, refresh deadline, stale
  response guard, periodic snapshot, heartbeat watchdog and snapshot backoff
  each map to the recorded sleep/network-loss failure modes and acceptance
  criteria. Its `live`, `eventStream`, refresh, retry and destroy modes have
  current consumers; injected clock/browser primitives support deterministic
  tests rather than a speculative runtime framework.
- The 227-line synchronization contract suite is proportionate to the state
  machine it owns. Repository summary tests match the explicitly requested page
  boundaries, net-tree semantics, preserved comparisons, batch parity and
  summary-limit behavior.
- Repository totals add only the missing whole-range commit count and reuse
  existing comparison-file calculation, stats reduction, immutable snapshot
  identity and cache. The browser pagination rule is the direct two-condition
  acceptance rule.
- The two dev-workspace functional commits separate repository presentation
  from conversation recovery. The provider pin is necessarily bundled with
  its importing recovery consumer; the three downstream commits contain only
  generated or direct package propagation required for the authorized
  aitherdev deployment.

No Blocking or Important scope findings were found.

## Residual gaps

- This lane did not assess the in-progress remediations after the packet heads.
  If a remediation expands the public synchronization or history-response
  contracts, the scope lane must be rerun on the new committed head. Narrow
  deletion, parameter unification, cancellation and typed-response fixes do not
  require a scope rerun.
- External codex-web consumers outside the checked-out workspace cannot be
  enumerated here. The reviewed public options are documented and the two known
  browser consumers exercise their distinct live and mounted modes.
- Long Firefox/Chromium outage, BFCache, draft/attachment/scroll, narrow-layout,
  package and deployment acceptance remains pending as recorded in the review
  packet. This lane did not repeat quick checks and made no implementation
  changes.
