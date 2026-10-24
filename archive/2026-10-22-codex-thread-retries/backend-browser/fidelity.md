# Real backend fixture fidelity

The new fixture is test-only. It calls existing helpers without changing them:
`prepareNativeHTTPRetry(t, true)`, `newPlanDeliveryFixture(t)`,
`addPolicyMember`, `retryPolicyPath` and `snapshotForHTTPRetry`. The retry host
uses the existing strict `retryWire`; the manual host uses the existing strict
`planDeliveryWire`. Both supply real `workspacecodex.Client` instances and
retained root/member identities. The second host avoids relaxing either wire's
allowed input. All existing helper/native fixture files remain byte-identical
to45e except owner0's accepted creation-source setup correction.

## Display-only method overrides

The wrapper embeds `*planDeliveryClient`, which embeds `*resolverRetryClient`
and the real `*workspacecodex.Client`. Its exact public overrides are:

| Method | Caller/surface | Local data |
| --- | --- | --- |
| `ReadThread` | A conversation `thread` route | Synthetic transcript text/settings for rendering |
| `ReadThreadPage` | A conversation `page` route and B member paging forwarder | Synthetic current/older pages with fixed item identities |
| `PromptsWithItems` | A browser `pending` route | Empty display prompt list |
| `ListModels` | B session model catalog and A `models` route | One bounded display model |
| `ListCollaborationModes` | B mode catalog and A `collaboration-modes` route | Existing default/plan modes |
| `ReadAccountRateLimits` | B account allowance display | Empty allowance snapshot |
| `ReadActivity` | `Server.activityProvider()` fallback, A ordinary `activity` route | Ordinary idle duration display for the resolved thread |
| `ListThreadActivity` | B `readIndexStatuses` display batch | The caller's retained identity rows |
| `Subscribe` | A `events` route | Local buffered transcript-change hints through the real SSE handler |

The private `signal` method only wakes those display subscriptions. Ordinary
`activity` is separate from `retry/activity`. No retry DTO is returned by these
methods. The local transcript and duration displays do not grant admission.

## Unchanged authority and execution paths

- Real TLS `httptest` hosts serve `Server.Handler`, actual session template,
  CSP, versioned assets and upload readiness. Trusted origins and A handlers
  are configured using the existing question fixture pattern. Browser code
  asserts the page's actual CSP and never installs a route interceptor.
- Root `/api/sessions/example/retry/...` and member
  `/codex/conversations/example~implementer0/retry/...` reach the production
  resolver, token validation, `retryProvider`, `PolicyStore` and retry ledger.
  `retry-policy` reads/writes use the real EX transaction. No retry provider,
  sender, store or admission method is overridden by the wrapper.
- Promoted `RetryBackend()` is `workspacecodex.Client.RetryBackend`, returning
  `retryBackend{c}` with the original managed receiver. Its Observe/Boundary/
  Reconcile/Continue methods and `ObserveThreadIdentity` retain that receiver.
  Their native reads, prompts, queue, submission reconciliation and exact
  settings proofs therefore use the real managed/native client, independently
  of the wrapper's display methods. B retained root/member admission and
  ordinary mutation checks remain enabled. Existing fixture archive/materialized
  identity adapters retain their original narrow synthetic scope.
- Manual `Send`, `PrepareSend`, `SendAttempted`, receipt reconciliation and
  per-member forwarding are inherited unchanged. The browser supplies its own
  durable UUID; the fixture captures and compares it with the actual receipt
  and retained browser record. The strict wire must observe exactly one native
  acceptance and unchanged optional-policy bytes. It rejects unexpected input
  and native RPCs.
- Both hosts have a genuine retry-capable client and a policy bootstrapped by
  the real transaction. The manual case first requires HTTP200 policy/activity
  and enabled real Settings switches, then corrupts the actual private sidecar.
  It requires real503/unavailable UI before making the ordinary Send. An
  unsupported client cannot satisfy those prerequisites.
- Scenario controls are confined to the disposable server wrapper. They use
  the owning State/Store/SessionPolicy APIs to schedule, save Begin, create
  actual synthetic native uncertainty, reconcile the original receipt, fail
  an optional checkpoint and retire fixture activity. They return bounded
  internal identities/hashes/counters, never retry DTOs or tokens. Browser
  action tokens come only from real production responses.
- Lost policy response instrumentation runs the actual handler into an HTTP
  recorder first, requires its real200 result, then closes only the transport.
  The browser must read back the committed state without another preference
  POST. Same-choice replay must preserve policy revision, policy bytes and
  ledger bytes.
- `newTestServer` uses `RecoverSessions=false`; `startTurnRetries` and recovery
  workers refuse that configuration. The fixture asserts that flag and never
  calls the worker or ordinary dispatch for a due deadline. Only the explicit
  unknown-stage control makes its one synthetic continuation. No daemon, model,
  preview service or live workspace is used.

## Required execution evidence

`case-manifest.json` enumerates all32 required cases across the four exact Go
subtests. Each CJS case is appended only after its assertions complete. Go
requires each exact eight-case manifest; the prepared collector additionally
requires the parent and all four subtest PASS events and zero skip/fail/missing.

The selected test fails if Node, the pinned Playwright module or Chromium is
missing. It skips only when its opt-in test is not selected by the environment.
The collector explicitly selects `PORTAL_BROWSER_TEST=1`, retains the full Nix
tool PATH and supplies the pinned Playwright1.59.1/browser1217 paths. It is
prepared and unrun pending independent final review and lead watcher release.

The last CJS-only amendment strengthens Retry now to require a strictly shorter
deadline bounded by the real returned server time. `compile-input-proof.json`
enumerates every unchanged tracked Go blob and unchanged module/Nix inputs.
The CJS file is loaded by Node at runtime and is outside the package's only
embed patterns, `templates/*.html static/*`. Its final syntax result is separate
from the prior compile-only result. No browser or fork runtime pass is claimed.
