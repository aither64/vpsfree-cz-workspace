# Architecture and repetition review, final recovery rerun

Reviewed the bounded recovery correction described in
`plan-decision-review-packet-v3.md`, the applicable repository instructions,
the provider and runtime commit series, the new provider interface and focused
tests, and the actual Go and Nix consumers at their final pinned revisions:

- codex-web `c0fbae9d4828bb05fdf5f17f9b85a66eaf98c612..ee9ab42791a84b79315d952501264a6cbafc8695`
- dev-workspace `2bfb0ee6aa4d56cbcbe079ef49c79d772a2e8fcf..7f0d1abd0c382088cc05e7f82d2e65af5b5dd4c8`
- vpsfree-dev-workspace `a4b837f1c976c7611493e2f4f87ad49a008a4853`
- workspace `ab7a866482b3dcd0d1cc2d675a58e8ce00d2527b`
- vpsfree-cz-configuration `c7d639ec9d63e5d1f69d3508cf06b49d72b76a36`

The preceding upload, menu, and plan-presentation implementation was outside
this rerun.

## Findings

No Blocking, Important, or Advisory architecture/repetition findings.

## Architecture assessment

codex-web is the correct owner of the new `DiscardPreparedSend` operation. The
method treats the action context as opaque provider identity, reloads and
updates the ledger under the existing per-thread mutation lock and durable
ledger transaction, compares the exact client ID, message digest, and context,
and persists deletion before returning success
(`codex/client.go:3732-3762`). It does not encode portal plan policy. Returning
false for `submitting` and `accepted` keeps uncertain or completed delivery in
the established reconciliation path. The provider test covers exact-identity
rejection, idempotent absence, lifecycle unblocking after durable retirement,
and retention plus reconciliation of submitted states
(`codex/reconcile_send_test.go:86-126`). This resolves the prior stranded-ledger
finding at the component that can make the transition atomically.

dev-workspace remains the policy owner. Unversioned `action=same` requests are
rejected before receipt reconciliation (`portal/internal/web/server.go:1563-1576`),
so an old page cannot interpret a legacy receipt as approval of a later
identical plan. The separate `action=recover` path reconciles submitted states
first, proves a v2 proposal is no longer current before requesting retirement,
and returns before the mode-change and send path
(`portal/internal/web/server.go:1586-1627`). Legacy retirement is deliberately
limited to recovery because its stored context cannot prove a turn. The browser
derives recovery only from its durable exact context, keeps current and
unproven v2 attempts available for an explicit retry, and removes local state
only after the server reports retirement
(`portal/internal/web/static/app.js:67-78,2137-2151,2596-2616`). Receipt
acceptance continues through the normal transcript acknowledgement mechanism.

The equality rule for the visible current-plan decision and implementation
click remains owned by `matchingSendAttempt`; recovery parses the persisted
versioned context because it must reconstruct the HTTP request after a reload.
The corresponding Go construction and validation are appropriate independent
checks at an untrusted transport boundary. There is no parallel downstream
ledger implementation or catalog to keep synchronized. The shared
conversation client interface remains unchanged; only the portal's internal
provider-facing interface gains the additive operation implemented by the
concrete codex-web client.

The final consumer graph is coherent. dev-workspace selects codex-web
`ee9ab427` in `portal/go.mod`, `portal/go.sum`, `flake.nix`, and `flake.lock`.
vpsfree-dev-workspace selects dev-workspace `7f0d1ab` and resolves codex-web
`ee9ab427`; workspace selects vpsfree-dev-workspace `a4b837f` and its lock graph
resolves the same runtime/provider pair; vpsfree-cz-configuration directly
selects runtime `7f0d1ab` and provider `ee9ab427`. The three downstream commits
contain mechanical pins only, with no duplicate recovery policy.

## Residual risks and test gaps

The provider test does not inject a ledger-write failure specifically into
`DiscardPreparedSend` or race this new method from two OS processes. The method
uses the already tested cross-process ledger transaction and atomic write path,
and its local rollback restores the exact removed record, so this is a bounded
test gap rather than a design finding. The prepared browser fixture and package
or deployment checks in the packet remain the appropriate integration coverage.

Recovery also depends on the browser retaining the exact retry identity. If
that browser storage is deliberately erased, the provider continues to fail
closed on an unresolved prepared attempt; this correction does not add a
general ledger migration or unauthenticated discovery mechanism. The ledger
schema and App Server protocol are unchanged, and a rollback server rejects the
new version/action rather than reinterpreting the identity, so mixed-version
failure is recoverable by reloading the deployed portal.
