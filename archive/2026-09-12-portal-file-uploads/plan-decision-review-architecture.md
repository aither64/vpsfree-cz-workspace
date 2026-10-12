# Architecture and repetition review

Reviewed the committed follow-up ranges from
`plan-decision-review-packet.md`, the initiative plan/state, repository
instructions, commit series, public interfaces, browser state helpers, and the
actual Nix and Go consumers:

- codex-web `4a4c77b4acc2bbaef44e2327c37d9c984e091867..c0fbae9d4828bb05fdf5f17f9b85a66eaf98c612`
- dev-workspace `14871f50bb6f57542d3452de32924357ff629037..d2cdeabd6c43423491eead1b4cca7f8d2e866946`
- vpsfree-dev-workspace `6063618bcf1fc3eefe57187a22ccc3b1bf0b22b6..58c2dde52958a8e11fcb6decc2287b5e0a4dec11`
- workspace `96ec50e609a48372fc4ab5300e34dc12f6ba9733..545bf2df04e2844ecfa9ffa33a7e611f1d0ff6f4`
- vpsfree-cz-configuration `c79a68ea6ef80dcaaef95cf17950fa87afbe976d..15abf6b9ce8431537b8a16b538dd765357d00db9`

## Important

### 1. Default-mode plan recovery classifies attempts by display text instead of their plan identity

Commit: dev-workspace `d2cdeabd6c43423491eead1b4cca7f8d2e866946`.

`renderPlanActions` treats any retained browser send attempt whose message is
`Implement the plan.` as a pending implementation
(`portal/internal/web/static/app.js:1832-1837`). That result enables the plan
decision while the conversation is already in default mode and supplies the
`Check request` label. The durable attempt already has the explicit action
identity needed here: plan sends store `context: plan:<plan digest>`, and
`matchingSendAttempt` compares both message and context
(`portal/internal/web/static/app.js:470-509,2712-2724`). The renderer therefore
implements a second, weaker classifier for the same recovery rule.

This can replace the normal composer for the wrong plan. For example, an
unacknowledged attempt for plan A can remain in session storage after its turn;
after a later plan B and a switch to default mode, the plan A record makes plan
B appear recoverable. An ordinary message with the same literal text has the
same effect because its context is empty. The server will reject a newly
created plan B attempt in default mode, so this does not submit stale content,
but the browser still hides the composer and presents an action that cannot
succeed. Retained attempts are an intentional response-loss path, so the
renderer must use their durable identity rather than infer their kind from
human-readable text.

Hash the current plan first and use the existing matching rule (or one shared
predicate) to recognize only an attempt whose message and `plan:<digest>`
context match that plan. Use that exact match for default-mode eligibility and
the `Check request` label. Add a focused regression with an older plan attempt
and a current plan of a different digest, plus an ordinary same-text attempt,
and prove that neither replaces the composer in default mode.

## Other architecture observations

No other Blocking, Important, or Advisory architecture/repetition findings
were identified. codex-web is the appropriate owner of the additive raw
`Transcript.latestTurnId` metadata and the non-submitting ledger recovery
operation. dev-workspace owns current-plan selection, creation snapshot policy,
server revalidation, and composer presentation. Repeating current-plan
eligibility in Go and JavaScript is justified by the separate authoritative
server and responsive browser boundaries; both use the same turn, status, kind,
and nonempty-text criteria and have focused tests.

The consumer graph is aligned at the reviewed heads. dev-workspace pins
codex-web `c0fbae9` in both `portal/go.mod` and its flake source, with the Nix
package checking that those revisions agree. vpsfree-dev-workspace pins runtime
`d2cdeab`; workspace pins organization package `58c2dde`; and the aitherdev
configuration directly pins runtime `d2cdeab` for the host module. Their lock
graphs all resolve codex-web `c0fbae9`, so the application package and host
module select the same provider/runtime series. The downstream changes contain
only these pins and introduce no parallel plan implementation.

## Residual risks and test gaps

The committed provider test proves that empty and unfinished newest turns still
set `latestTurnId`, while the portal Go and Node tests cover freshness in both
server destinations and browser selection. The HTTP serialization itself is
left to the transcript struct's normal JSON path, and the committed browser
contract does not exercise real focus, hidden-form layout, upload preservation,
or dialog cancellation. The packet's prepared desktop/narrow browser fixture
is still needed after the finding above is fixed.
