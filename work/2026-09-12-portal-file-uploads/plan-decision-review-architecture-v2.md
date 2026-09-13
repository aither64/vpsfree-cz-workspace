# Architecture and repetition review rerun

Reviewed the focused turn-bound receipt correction in dev-workspace
`9ed5ff56171b0b1a127aa1bbe26b10580bef7d36..2bfb0ee6aa4d56cbcbe079ef49c79d772a2e8fcf`,
the unchanged codex-web provider at `c0fbae9d4828bb05fdf5f17f9b85a66eaf98c612`,
the final review packet, prior findings, repository instructions, and the
consolidated downstream pins in `plan-decision-revisions.json`. The preceding
upload and menu implementation was outside this rerun.

## Blocking

### 1. Refusing a legacy prepared request leaves an unresolvable provider ledger entry

Commit: dev-workspace `2bfb0ee6aa4d56cbcbe079ef49c79d772a2e8fcf`;
provider: codex-web `c0fbae9d4828bb05fdf5f17f9b85a66eaf98c612`.

The new unversioned path correctly calls non-submitting reconciliation and then
returns a reload conflict when no submitted receipt was found
(`portal/internal/web/server.go:1574-1592`). For a legacy attempt in
`prepared` state, however, `ReconcileSend` deliberately returns the same
`found=false` result as an absent attempt and leaves the record unchanged
(`codex/client.go:3732-3776`). A fresh page creates a new turn-bound attempt
under a new browser ID, so no later path addresses the old record.

That old record is durable, and codex-web counts every send whose state is not
`accepted` as unresolved (`codex/client.go:2246-2281`). Consequently, an
interruption after the old server's `PrepareSend` but before submission leaves
the conversation permanently unable to pass `RequireThreadIdle`. dev-workspace
uses that check when quiescing or stopping a session and before archive
(`portal/cmd/workspace-portal/main.go:426-430` and
`libexec/dev-session:1364,6852-6884`). Completing a fresh v2 implementation does
not clear the legacy prepared entry. Recovery therefore trades an ambiguous
submission for stranded persistent state that blocks normal session lifecycle
operations.

The provider owns send-attempt state and its lock, so the version-migration
policy needs an explicit provider operation rather than treating `false` as
both "absent" and "prepared." Add an exact, durable resolution for a matching
legacy prepared attempt, such as safely discarding it before instructing the
browser to reload, or atomically rebinding it to a freshly validated turn-bound
identity. Preserve the rule that an unversioned request cannot submit work.
Cover a real provider ledger that begins in `prepared`, exercise the new-server
legacy request followed by a fresh v2 request, restart the client, and prove
that `RequireSubmissionAttemptsResolved` succeeds after the v2 receipt is
acknowledged.

## Architecture assessment

The turn-bound v2 path itself resolves the prior architecture finding.
`planActionContext` owns browser construction of `plan:<turn>:<digest>`, and
both banner recovery and the click handler delegate complete equality to
`matchingSendAttempt` (`portal/internal/web/static/app.js:67-70,1846-1857,2717-2728`).
The server independently derives the same context before provider
reconciliation and still revalidates the current raw plan turn and digest. That
small cross-language duplication is required at the untrusted HTTP boundary;
there is no second downstream business-rule implementation.

The consolidated pins are coherent. vpsfree-dev-workspace `909fde2` selects
runtime `2bfb0ee`; workspace `f9d156a` selects organization package `909fde2`;
and vpsfree-cz-configuration `4362c8c1` directly selects runtime `2bfb0ee` for
the host module. All three lock graphs resolve codex-web `c0fbae9`. These
repositories contain pin changes only.

## Residual compatibility risk

An already loaded unversioned browser can still present an earlier submitted
legacy receipt as the result of a later identical plan because the legacy
ledger context has no turn identity. The new server prevents such a request
from starting work, which preserves at-most-once submission, but the old page
can dismiss the later decision after receiving the earlier receipt. If this
mixed-page behavior is accepted, record it explicitly and require reload before
using a newly displayed plan during the transition. Otherwise the server needs
to refuse legacy receipt recovery while another current plan decision is being
presented. This residual does not remove the Blocking lifecycle issue above.
