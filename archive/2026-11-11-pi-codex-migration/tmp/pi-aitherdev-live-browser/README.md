# Disposable live Pi browser preparation

Only syntax and offline `about:blank` checks have run. No portal, authentication,
provider or session request has run. The lead owns later execution after W/H
acceptance and strict authenticated landing-page verification.

The final scenario uses cached Firefox, its dedicated `firefox-profile` (0700),
and native NSS `cert9.db`. Cached certutil imported only the public
`/var/lib/dev-workspaces/public/ca.pem` as nickname `pi-trial-local-ca`, trust
`C,,`. The nickname/trust remained after Firefox opened and closed. This proves
local tooling/profile compatibility, not live hostname/chain acceptance.

The separate `chromium-profile` is retained as failed preparation evidence.
Chromium's Custom → Installed by you → Trusted Certificates UI was available,
but its Import attempt produced no Playwright file chooser. No CA was imported
there. No HOME/XDG, shared browser, user or system trust changed.

## Prepared commands; do not execute without lead release

Run from this directory. The lead supplies an inherited private password FD 3
for fixed Basic Auth username `aither`; no credential value enters arguments,
environment, receipts or logs. A regular private file or finite FIFO is accepted;
the script reads at most 4097 bytes, removes one final newline, then closes it.
The existing private JSON context-file alternative requires `httpCredentials`;
cookies alone do not authenticate nginx. No credential source was read in prep.

```sh
export PLAYWRIGHT_MODULE=/nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1/lib/node_modules/playwright
export FIREFOX_EXECUTABLE=/nix/store/f0rap655j6wmqbfvqdw445kwcxkxwf7n-playwright-browsers/firefox-1511/firefox/firefox
export PI_BROWSER_PROFILE_PATH=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-11-pi-codex-migration/tmp/pi-aitherdev-live-browser/firefox-profile

# Local-only compatibility check; needs no password FD:
/nix/store/gf597zf0ysgbngwb92baxgxjd02px6jh-nodejs-22.23.2/bin/node scenario.cjs blank

# Later, with lead-supplied FD 3 and a fresh explicit name/output path:
PI_BROWSER_PASSWORD_FD=3 /nix/store/gf597zf0ysgbngwb92baxgxjd02px6jh-nodejs-22.23.2/bin/node scenario.cjs create /absolute/private/original-projection.json unique-trial-name

# Original page/receipt only; never creates or sends:
PI_BROWSER_PASSWORD_FD=3 /nix/store/gf597zf0ysgbngwb92baxgxjd02px6jh-nodejs-22.23.2/bin/node scenario.cjs reconnect /absolute/private/original-projection.json

# Separate later invocation only after lead accepts original/reconnect/native proof:
PI_BROWSER_PASSWORD_FD=3 /nix/store/gf597zf0ysgbngwb92baxgxjd02px6jh-nodejs-22.23.2/bin/node scenario.cjs followup /absolute/private/original-projection.json
```

The create mode opens the shipped form, selects Pi/Solo and Sol/high, and clicks
submit once. It captures the original clientRequestId at request emission, then
202/receipt/backend/canonical path. It uses one shared 180-second bound through
ready, transcript observation and read-only reopen. A new output file is required;
failure preserves original identity and never retries, cancels or resends.
The optional followup is one distinct no-tool message with a shared 45-second
bound and a durable attempted flag. It is never invoked automatically.

Thread GETs use the exact original X-Workspace-Conversation-Scope. Projections
retain only original request/receipt/native/turn/item/scope identities and bounded
counts/status. The script checks blank Codex fields, Sol/high, the original user
once, one exact `PI_SOLO_TOOL_OK` result on that turn, terminal `PI_SOLO_DONE`,
idle, and matching identity/history on reopen. It does not change installed
Default policy, route, account, fallback configuration or product source.

Public Rdc643 `piruntime/adapter.go` omits native toolName/toolCallId/isError/exit
metadata. Therefore `public-observation-complete` is expressly incomplete: the
assigned native observer must join the retained IDs to exact builtin bash
call/result and successful exit. A 202 is preparation admission, not native
Accepted or inference proof. No private history reader is added here.

Strict TLS remains enabled. No interception, fixture password, CA bypass, provider
override, VM piExchange, restart, cold recovery or lifecycle action is included.
Browser closure joins local owned processes and says nothing about remote
operation settlement. Keep original recovery records and session open.

Source basis: R `dc64356b852ab497a0250d07e3296a69152a1963`,
`test/creation_acceptance_browser.cjs:320–379`; accepted design.md installed/UI
Solo clause near12655 and trial-preparation.md:175–198. The script is disposable
operational preparation, with no project edits or commit.

## Prepared recovery of the existing original request

`retry-original.cjs` is a task-specific copy of the frozen `scenario.cjs`
(`a49ecc7b…`). Its only mode is `retry-original`; preparation ran Node
`--check` only. The original failed create and its projection stay unchanged.

After a separate lead execution release, reuse the exports above and the
inherited private Basic Auth FD 3, with a new output path:

```sh
PI_BROWSER_PASSWORD_FD=3 /nix/store/gf597zf0ysgbngwb92baxgxjd02px6jh-nodejs-22.23.2/bin/node retry-original.cjs retry-original /home/aither/workspace/ai/vpsfree.cz/work/2026-11-11-pi-codex-migration/tmp/pi-aitherdev-live-browser/original-retry-projection.json
```

The script binds the frozen local original projection to request
`5e54c320-443d-4bc0-bb2c-42d51284e88b`, receipt `8e46292b…e36363`, custom
name `pi-solo-route-20261116-1950`, and canonical slug
`2026-11-16-pi-solo-route-20261116-1950`. It opens that request's existing
creation page, reads its fresh current attempt, verifies the unchanged goal,
then installs request/response listeners before one ordinary **Retry creation**
click. The only mutation is the shipped control's receipt/attempt POST. The
new projection retains the click flag and exact sent attempt even if its
response is lost; it never clicks again. A refusal stops observation.

The same 180-second deadline covers recovery, original transcript observation
and read-only canonical reconnect. Existing scope/native/item/turn checks are
reused. No new session, goal edit, follow-up or private trace read is included.
Public completion still requires the assigned native observer's exact bash
call/result join; `numericExitCodeObserved` remains false. Later execution
needs lead acceptance of the corrected installed packages, exclusive use of
the dedicated Firefox profile, FD 3 and a fresh evidence filename. It reads
the attempt itself; no manual attempt or new ID is supplied.

Source fit: R `8ff582caf5b4c7b6ac867d0f180212b1b4b0ce80`,
`portal/internal/web/static/creation.js` retry listener and response rendering,
`templates/creation.html`, `preparation.go` handed-off retry routing, and
`creation.go` receipt/attempt guard. No browser, auth or network ran in this prep.

## Original retry diagnosis, 2026-11-17

The original `retry-original.cjs` run stopped before its click, with
`retryClickAttempted=false` and `retryPostCount=0`. Its catch retained only the
phase, so the exact browser exception is unavailable. One bounded GET through
the supported local portal socket returned 200: every original status/goal/ID
check passed, at attempt 1 and state `failed`, phase `initializing`. This does
not establish the browser's TLS, navigation or status-response outcome.

`retry-original-diagnostic.cjs` adds only diagnostic check labels, page/status
HTTP codes and an allowlisted exception category. It preserves all assertions,
strict TLS, the same IDs/goal, listeners and single click. No raw exception,
body, header or auth value is saved. Node `--check` passed; this copy has not run.
Original script, failed projection and failure artifacts remain unchanged.

Only the lead may release execution, using the existing exports and inherited
FD 3, with a new projection filename:

```sh
PI_BROWSER_PASSWORD_FD=3 /nix/store/gf597zf0ysgbngwb92baxgxjd02px6jh-nodejs-22.23.2/bin/node retry-original-diagnostic.cjs retry-original /home/aither/workspace/ai/vpsfree.cz/work/2026-11-11-pi-codex-migration/tmp/pi-aitherdev-live-browser/original-retry-a43-diagnostic-projection.json
```

The browser boundary remains unresolved until its actual diagnostic is retained;
the status read supplies no authority to change an assertion or resend input.

## Confirmed Basic Auth challenge handling

One subsequently authorized read-only navigation observed GET `401 → 200` for
both the original creation page and its status API. Final authenticated status,
original IDs/attempt/goal, pre-click DOM and enabled Retry control all passed.
The browser closed with zero non-GET requests and no click. The proof is
`original-auth-readonly-proof.json`; the earlier failures remain unchanged.

`retry-original-authenticated.cjs` changes only the original status response
waiter from the diagnostic copy. It follows the response after an intermediate
401 challenge, retains the existing 200 assertion and every identity/CAS guard,
and records at most eight status codes. Other non-200 responses still refuse.
Node `--check` passed; its Retry path has not run.

Only the lead may release the actual Retry. With the existing Firefox exports,
strict CA and approved FD 3 redirection, use a fresh projection filename:

```sh
PI_BROWSER_PASSWORD_FD=3 NODE_EXTRA_CA_CERTS=/var/lib/dev-workspaces/public/ca.pem bash -c 'exec /nix/store/gf597zf0ysgbngwb92baxgxjd02px6jh-nodejs-22.23.2/bin/node /home/aither/workspace/ai/vpsfree.cz/work/2026-11-11-pi-codex-migration/tmp/pi-aitherdev-live-browser/retry-original-authenticated.cjs retry-original /home/aither/workspace/ai/vpsfree.cz/work/2026-11-11-pi-codex-migration/tmp/pi-aitherdev-live-browser/original-retry-a43-authenticated-projection.json 3< /var/lib/dev-workspaces/password/password'
```


## Original read-only acceptance completed, 2026-11-17

The lead executed the original Retry once before this package. Do not run a
Retry or Send to repeat this proof. The historical preparation and failure
sections above describe their original scope; their scripts/projections remain.

`original-readonly-acceptance-fitted.cjs` passed as original tool 78935 at
00:46:00.808Z–00:46:14.805Z, exit 0, browser closed. One canonical observation
and one canonical reconnect share the 180-second deadline and strict Firefox
CA/approved private FD transport. Both exact original status/thread reads were
200/JSON. Actual DOM scope, native ID, model/effort, original user/turn,
tool-result and terminal IDs were identical across reconnect and joined to the
independent native proof. One user, one result and one terminal marker remained
idle. No Retry, Send or click was invoked.

Source-fitted corrections are confined to the disposable readers:

- R a43 `pi_workflows.go:781` defines browser scope separately from native
  `piruntime/identity.go:14` HistoryRef. Each hash is validated independently.
- Ready preparation status compacts the initial request and reports preparation
  attempt 1; the original goal is verified in the transcript/native chain.
- Pinned codex-web c05 `conversation/backend/types.go:32` omits empty Text.
  Actual assistant call entry has only toolCall; optional text is handled.
- Lead accepted the actual final text: first nonempty line PI_SOLO_DONE once,
  followed by the inherited phase checklist. The old whole-text check FAILED;
  `terminalWholeTextEqualsMarker=false` remains in the successful proof.

The exact native reader is
`../pi-aitherdev-host-prep/native-tool-proof-canonical-accepted.py`. It validates
the supplied full original handle, mapping/Generation/CreationID, history header
and unique complete linear chain before emitting only bounded evidence. Actual
user/turn `da62e8f0`, assistant call `36be928c`, result `ffebbb79`, terminal
`8e800504`; exactly one approved `printf PI_SOLO_TOOL_OK`, matching toolCallId,
toolName bash, explicit isError=false, exact output and terminal stop. Numeric
exit code is absent/unobserved. The successful browser joins those anchors;
the native proof's earlier `publicAnchorJoin: pending` honestly records its
chronological scope before that join.

Startup diagnostics record six request events, all POST to the exact original
`/codex/conversations/<original-slug>/queue/reconcile`, with response events
401 then three 404s; two response statuses were not observed before closure.
R `static/app.js:6378,7432,7439` invokes ordinary startup queue reconciliation;
`pi_workflows.go:1123` refuses it before session admission/lease. Unknown
non-GET requests would be blocked; none occurred. These are classified refused
page requests, so this result does not claim zero total POSTs. Retry count is
zero. Historical tool 71849's two non-GET paths were not retained and remain
unknown; its scope/settings pass and optional-text failure are preserved.

Native read accounting: one original strict canonical proof failed at terminal
whole-text equality; one diagnostic attempt failed on the unrelated system
entry's string content shape; subsequent bounded shape, marker-position and
lead-requested visible-terminal projections succeeded; the disposition-fitted
canonical proof passed. These six narrow reads used only the exact mapping and
its canonical HistoryFile; no history inventory, SDK open/init or native action
was used. Failed original outputs are not rewritten. All shell/tool handles are
terminal. No additional worker process/environment read was needed or claimed.

Evidence (SHA256):

- Fitted browser script: `085ba2f2d2a85230ac53629b8e0f82a1e87dc454b17b096bef3d2841724b2332`
- `original-a43-readonly-acceptance-fitted.json`: `11ebbe4e329a4198f97b8d55c347c101f4b9dd54367de6a36bbd35382c27bcb6`
- Fitted native reader: `87129873e5b53a730e270528b86e3b7627e7510452e8bae1d22be9699efcb476`
- `../pi-aitherdev-host-prep/original-native-canonical-accepted-proof.json`: `f1366323516964a4b691cd7c3e8d745bf468bb18a4388b0780262faf8f8d506a`

Both new scripts passed declared syntax checks. No product source, settings,
input, build, CI, service, helper, claim, provider or lifecycle action occurred.
The lead owns acceptance and any separate later follow-up. Session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/


## Separately released single follow-up completed

`followup-original-fitted.cjs` passed as tool 68555, 00:53:16.657Z–00:53:34.202Z
(17.545s), browser closed. One canonical navigation, one ordinary Send at
00:53:24.555Z, one message POST/202; client ID
`56c52c12-a355-4643-a7bd-83c115752e37` matched native turn/user `9569cea6`.
Response `962cbd40` starts with PI_SOLO_FOLLOWUP_DONE once and adds the permitted
phase checklist: trial; done followup; remaining none; blockers/risks none; next
none. Whole-text equality is false; idle and original/native/scope anchors hold.
Fresh evidence: `original-a43-followup-projection.json`.

ONE subsequent exact canonical history read, `native-followup-proof.py`, passed
exit 0/stderr empty. `../pi-aitherdev-host-prep/original-native-followup-proof.json`
proves the matched public/native follow-up, native stop, total users 2, total
original tool calls/results 1/1 and follow-up calls/results 0/0. Original explicit
isError=false and numeric-exit-unobserved limits remain. No raw thinking/history
was retained. Total non-GET requests were 6: one authorized message202 and five
ordinary exact queue/reconcile404; unknown blocked 0. No repeated Send, Retry,
independent reconnect, or other action occurred. Original scripts/evidence stay
unchanged. All handles are terminal; lead owns acceptance/Codex continuity.
