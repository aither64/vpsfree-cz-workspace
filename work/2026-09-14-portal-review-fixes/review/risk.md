# Risk and compatibility review

## Findings

### R1 — Blocking: a claimed response can be written to a replacement offer

`codex-web` commit `1a0ed38060db44bc3849d7adec481519d78dfa90`:
`codex/client.go:1404`, `:1453`, `:929`.

`claim` checks the token before setting `claimed`, but `finishResponse` then calls
`writeOn`, which checks only the connection and generation. While the response
waits for `writeMu` (or an approval loads its authoritative item),
`handleResolved` can remove the claimed request and the reader can admit another
offer with the same protocol ID on the same connection. The old answer then
passes the connection check and is sent using that reused ID. Its token is
checked again only when deleting local state, after the write. This can submit
answers, including secret answers, or an approval to a question the user never
answered or approved.

Evidence: inspected the general reviewer's deterministic Go overlay test
`TestReviewReissuedOfferWhileAnswerWaitsForWrite`. It holds `writeMu`, starts
`RespondPrompt` for choice `First`, waits for its claim, delivers
`serverRequest/resolved` and a replacement offer accepting only `Second`, then
releases the writer. The general reviewer reported that the old `First` answer
was delivered successfully. The replacement is delivered over the same real
test WebSocket, and its new token is observed before releasing the writer. This
also matches the same-generation ID reuse already supported by
`TestReissuedRequestRejectsOldTokensAndAutoResolutionTimers`.

Revalidate the exact claimed offer at outbound write admission and serialize
that check/write with offer retirement and replacement. A retired claim must
return a definitely-unsent error. Retain the deterministic race as a regression
test, including the automatic-answer path.

### R2 — Important: mixed browser generations can bypass offer binding

`codex-web` commit `1a0ed38060db44bc3849d7adec481519d78dfa90`:
`conversation/handler.go:797–811`; representative consumer
`conversation/assets/conversation.js:717`, `:725`, `:731`.

The HTTP handler selects `PromptResponder` only when the body already includes
a token. A tokenless body falls back to legacy methods, whose empty-token calls
explicitly skip token matching. An already-open browser from the previous
deployment can therefore answer or snooze a request ID that has since been
reissued, without checking the offer that was displayed. The bundled
`mountConversation` UI still sends tokenless answers, decisions and snoozes, so
this is also exercised by a current in-repository consumer. Retaining public Go
methods does not require permitting this fallback for HTTP clients backed by
the new responder.

Reject missing tokens with `reload_required` when the concrete HTTP target
supports bound responses, retain the documented legacy Go API, and pass each
offer token from the bundled UI. Cover an old browser against the new server,
alongside the existing unsupported-responder test.

### R3 — Important: refreshing cannot retry a failed snooze for the same offer

`dev-workspace` commit `94e3114c6fef510ca21d29efd1741faa848a4147`:
`portal/internal/web/static/app.js:2569`, `:2634–2646`, `:2792`.

A failed snooze sets `wizardState.snoozeFailed = true`. Every later snooze exits
while that flag is set, and it is cleared only when the offer token changes.
The displayed remedy, “Refresh question,” calls `recoverPrompt`; restoration
of the same valid pending offer does not clear the flag. Reproduce by failing
one snooze before delivery, restoring normal reads, clicking Refresh question,
and continuing to type: no further snooze is sent. The provider's 120-second
automatic-answer timer can consequently resolve the question unanswered while
the user is still working on its saved answers.

The shared wizard state also allows a late snooze failure from an old token to
set the failure flag after a replacement offer has reset it. Bind snooze
completion state to the exact token and make explicit refresh/retry re-enable
a snooze for an authoritatively restored current offer. Test a transient failure
with an unchanged token and an old completion arriving after token replacement.

### R4 — Important: downloading an artifact permanently suspends page reads

`dev-workspace` commit `94e3114c6fef510ca21d29efd1741faa848a4147`:
`portal/internal/web/static/app.js:1774–1784`, `:1765–1766`, `:1618`;
consumer `portal/internal/web/templates/session.html:123` and
`portal/internal/web/server.go:1186–1191`.

The new document click handler sets `pageLeaving = true` for the artifact
Download link because its URL changes and the anchor has no `download`
attribute. The artifact endpoint responds with `Content-Disposition:
attachment`; the current document remains alive and does not receive a new
`pageshow` event. Subsequent focus and visibility events refuse to resume while
`pageLeaving` is true. Details polling, repository reads, timing and prompt
recovery thus remain suspended until a reload after an ordinary download.

Mark known download links explicitly and ensure navigation attempts that leave
the document alive can recover safely. Add an acceptance case that downloads
an artifact, then observes resumed details/activity/repository reads without
reloading.

### R5 — Advisory: the changed browser contract retains a cacheable asset URL

`dev-workspace` commit `94e3114c6fef510ca21d29efd1741faa848a4147`:
`portal/internal/web/static/app.js:776`; `codex-web` commit
`1a0ed38060db44bc3849d7adec481519d78dfa90`:
`conversation/handler.go:240`, `conversation/assets/conversation.js:270`.

The application still imports `conversation.js?v=7`, while the provider serves
that asset with `public, max-age=300`. A freshly loaded new application can use
the cached previous module for five minutes. That module discards the second
argument to `snooze` and omits `code`/`notSent` on errors. With R2 fixed, snoozes
will be rejected and the automatic answer recovery remains unavailable until
the module is replaced. Bump the asset version with this browser contract
change, or use an equivalent generation-aware asset URL; include a cached-old-
module deployment check.

## Reviewed contracts and residual verification

Reviewed the packet, plan/state, applicable repository rules, mandatory review
skill and Risk lane reference, commit series and these frozen ranges:

| Repository | Base | Head |
| --- | --- | --- |
| codex-web | `6335da93acdcc82cc26200d2fbc7f479655aa7c3` | `1a0ed38060db44bc3849d7adec481519d78dfa90` |
| dev-workspace | `83136101866eb42d9e079f47191308c0549ac9e7` | `94e3114c6fef510ca21d29efd1741faa848a4147` |
| vpsfree-dev-workspace | `a08a40eeff124bdbcc1ce6b6b06aed1839a9d9fc` | `7dc4ea2ac169064de0034983377f9f19c23a281d` |
| workspace | `8f31bab` | `997f4aa2ce7ae58b2be13348036a2d168c71a2b1` |

The Go and Nix provider pins agree, and the organization/workspace locks select
the recorded runtime and provider heads. `workspacecodex.Client` embeds the
provider client, so the optional response interface reaches the concrete HTTP
target. No protocol-version, database, manifest, journal, activity-format or
host-state migration is introduced. The planned user-profile deployment and
retained previous generation remain suitable once mixed-browser handling is
addressed. No coordinated node update is needed.

The Git reader retains immutable object validation, the canonical registered
repository boundary, disabled external diff/textconv, and existing byte, line,
time and concurrency limits. Both render projections consume checked Git
ranges. Draft serialization excludes secret answer values and binds new
records to question identity/schema; old unbound records are ignored. The
automatic answer retry is bounded to one extra send and requires a typed
definitely-unsent outcome plus restored identity; no uncertain-delivery replay
was found apart from the separate outbound-offer race in R1.

No project files were changed and no long integration or live tests were run.
The reported quick-check results were treated as the review baseline. The
general lane's R1 reproduction was reused after inspecting its source; it was
not rerun. Post-remediation acceptance still needs mixed browser/server and
cached-asset cases, same-offer snooze recovery, artifact downloads, an isolated
App Server, and deployment/rollback. Those are pending checks, not validation
already performed by this review.
