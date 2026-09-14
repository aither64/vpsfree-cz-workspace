# Architecture and repetition review

Reviewed the committed series at:

- `dev-workspace` `e9ed544bf66ba8be07b4fca27aede6e6fd1bfe0a..df21f2ea8fe27efdb2cb8c0330fa31acd0f3a933`
- `vpsfree-dev-workspace` `916223fce1c5b7b78578ca8a16aaaa472c68b08c..89a03581b13056fa83114e592f2e2993e6a87887`
- `workspace` `f523eddf3e1d1cdebf445992318247030e11c7f3..1e01e557cac5527666d5b1e35fa52fadcdbb81af`

## Findings

No Blocking, Important, or Advisory findings.

## Assessment

The implementation puts composer, completed-plan, question, Interrupt, and focus
presentation under one private controller in
`portal/internal/web/static/app.js:80-137`. This removes the former independent
plan-only visibility mutation and gives the requested priority ordering one
owner. `renderApproval` remains the authority that decides whether a pending
entry is an answerable wizard (`app.js:2332-2390`); the controller observes the
rendered `.question-approval` cards, so it does not repeat protocol-kind, error,
interactivity, or authority-availability rules that could drift from rendering.

Moving the existing `#interrupt` node between its recorded composer home and the
first question heading preserves a single event handler and a single enabled
state (`app.js:97-103`, `2048-2055`, and `2702-2806`). It does not introduce a
second action or a parallel interrupt path. Pending replacement and plan
rendering both call the same controller (`app.js:1959-1986` and `2598-2612`),
including the transition from a question to an eligible completed plan.

The focus restoration logic is local to that same view boundary. Request ID plus
control name/value identifies the corresponding control after a pending snapshot
rebuild, while the existing wizard draft store remains responsible for values and
page state. This avoids duplicating answer encoding or draft persistence.

The cross-project ownership is also appropriate. The generic `dev-workspace`
portal owns the behavior and browser regression. `vpsfree-dev-workspace/flake.nix:6`
only pins that runtime and continues to compose it through `dev-workspace.lib.mkPackage`;
the site `workspace/flake.nix:6` only pins the organization extension and keeps
its existing `siteConfig` composition. The lock changes follow that dependency
chain and do not create another implementation or public interface.

## Residual risks and test gaps

The DOM behavior is covered by a broad real-Chromium regression, but
`TestQuestionBrowser` is opt-in through `PORTAL_BROWSER_TEST=1`; the ordinary Go
suite will skip it. Future changes to question markup, focus identity, or layout
therefore need the explicit browser invocation used in the review packet. The
committed browser scenario exercises multiple simultaneous question requests,
snapshot replacement, and draft/focus restoration, but it does not separately
exercise snapshot replacement while positioned on a later page of one
multi-question request. Existing page state and name-based matching make that a
limited residual gap rather than a finding.

Packaged checks, assembled-package validation, and deployed asset/browser checks
remain pending by design until review reconciliation. They are validation steps,
not unresolved architecture concerns.
