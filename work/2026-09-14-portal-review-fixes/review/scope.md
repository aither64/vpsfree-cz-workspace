# Scope and proportionality review

Two Important findings; no Blocking or Advisory findings. Reviewed only the
frozen packet revisions. Later remediation is outside this review.

## Important — Unbound HTTP replies exceed the documented legacy compatibility need

At codex-web `1a0ed380`, `conversation/handler.go:797` selects token-bound
dispatch only when the browser supplies a token; lines 806–811 otherwise call
the legacy response methods. Those methods deliberately supply an empty token
(`codex/client.go:1303`, `:1338`), which bypasses the offer-token check at
`:1414`. This is exercised by a current consumer: the bundled
`mountConversation` renderer omits the token from answer, snooze and decision
requests (`conversation/assets/conversation.js:717`, `:725`, `:731`), and
`cmd/codex-web-example/main.go:33` mounts that renderer.

If an old displayed request ID is reused after connection retirement, a reply
from this renderer can claim the replacement offer, provided its action still
passes the replacement's validation. The compatibility shim therefore preserves
the exact stale-response behavior the change is meant to prevent. The packet
requires compatibility for existing Go consumers; it separately says updated
clients require tokens and unsupported generations request reload. Maintaining
unbound HTTP actions is a broader and unsafe compatibility promise.

Keep the existing Go APIs, send tokens from every bundled browser response
control, and reject tokenless HTTP replies against token-capable clients.
Retain fallback for other implementations only if its supported boundary is
explicitly justified. Add a focused HTTP/renderer regression showing that an
old tokenless browser cannot act on a reissued offer. This is also a
cross-project compatibility finding for reconciliation with the other lanes.

## Important — Artifact downloads permanently suspend page reads

At dev-workspace `94e3114`, the new document click listener in
`portal/internal/web/static/app.js:1774` calls `suspendPageReads(true)` for
same-window links whose path changes. That latches `pageLeaving`; subsequent
focus and visibility recovery return immediately at `:1766`, and only a
`pageshow` event clears it at `:1784`.

The existing artifact Download link is such a link: the template has no
`download` attribute (`portal/internal/web/templates/session.html:123`), and
`app.js:1618` assigns an `/artifacts/...` URL without adding one. The handler
serves that URL with `Content-Disposition: attachment`
(`portal/internal/web/server.go:1186`). Clicking Download keeps the current
document loaded, so no restoration `pageshow` clears the flag. Details,
repository and timing reads remain suspended; prompt recovery also returns
early while `pageReads.paused`.

Mark this known download control with the HTML `download` attribute so the
existing listener exclusion applies, and add a focused download regression
that confirms the page continues polling. This fixes the current supported
flow without expanding the navigation mechanism into a generalized browser
navigation framework. Other cancelled-navigation behavior remains a browser
acceptance case, not a demand for speculative infrastructure.

## Scope and series assessment

Reviewed the packet, linked plan/state, assigned skill/reference, local rules,
commit messages, diffs, consumers and relevant tests across:

- codex-web `6335da93..1a0ed380`;
- dev-workspace `83136101..94e3114`;
- vpsfree-dev-workspace `a08a40ee..7dc4ea2`;
- workspace `8f31bab..997f4aa`.

The remaining mechanisms have a demonstrated consumer or requested acceptance
case. Git owns changed-line classification; bounded CodeMirror character diffs
remain cosmetic. The real OAuth2 fixture, provenance and COPYING support the
reported regression and are not imported by the editor build. The retained
80 generated examples exercise projection behavior using Git's result rather
than reproduce its algorithm. Collapse/read generations and one bounded
answer retry address specified lifecycle failures. No unrelated host, schema,
protocol-version or destructive-session changes appear in these ranges.

The series is coherent: sidebar relocation and reviewer-model selection are
separate functional commits; the repository-rendering commit groups related
editor/content lifecycle changes; answer recovery carries its required
provider dependency; downstream commits only propagate these pins. Further
splitting is not necessary for this delivery.

No long integration or live tests were run. Browser navigation restoration,
download behavior, stale-response ordering, packaged assets, isolated live
App Server recovery and profile rollback remain acceptance gaps until the
coordinator completes the planned post-review checks. This scope review does
not independently certify those behaviors.
