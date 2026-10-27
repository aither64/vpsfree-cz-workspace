# Deferred Codex upgrade and naming

Architect0 owns this design under the verified retained roster; the lead owns
plan/state and consequential scope decisions. The lead accepted the verification
boundary below on 2026-10-26. Scope is the remaining raw 0.164 naming/upgrade work
on fresh defaults. Historical full-upgrade briefs are evidence, not an execution
checklist. Source-session state, rollout and design sections 1841/3136/5115 were
read as historical inputs; that session and its worktrees remain untouched/open.

## Temporary recovery failure after runtime becomes ready, 2026-10-27

Lead accepted this bounded correction; owner0 is released after reading this brief.
This is a new coherent fix after published f624, based on merged0e47, with no
rewrite of merged history. The prior older-session admission correction remains
valid but does not fix this separate source path. Retained diagnosis and original
evidence: `older-session-input/ci-40563820256-diagnosis.md` and its linked
failed-step log/metadata. CI40563820256 reached naming success, creation ready
and the initial reply, then timed out waiting for enabled Send. Its page showed
the exact temporary `another dev-session command is changing ...` failure.
The competing lock owner is unproven and unnecessary to this correction.

`dev-session resume` converts SessionBusyError into exit75. `restoreRuntime`
correctly marks that failure `Retry:true`, while hard identity/lifecycle refusal
remains nonretryable. The defect is in the existing `startRecovery` coordinator:
after the runtime becomes verified interactive, its sweep simply continues and
leaves the failed operation in memory. `recoveryStatus` gives that stale failure
precedence over current readiness, so the browser continues blocking input.

Keep the existing coordinator as the sole owner of automatic reconciliation.
In its verified-interactive branch, retire only the observed in-memory operation
whose state is `failed` and `Retry` is true. Use a small local helper in
`portal/internal/web/recovery.go`, callable by its focused tests. Under existing
transition SH then session Runtime SH, with a bounded context, re-read the exact
current summary and matching recovery root/socket record. Require current host
generation/provider admission, no pending lifecycle/creation operation, a valid
automatic-restoration intent, and fresh interactive verification through the
existing authority/tmux/native identity checks. Failed or unavailable proof
leaves the failure untouched. Reuse the existing verification path; do not add
another observation/discovery subsystem or require a cold idle proof to recognize
an already active runtime.

Only after those checks, acquire existing `operationMu` then `recoveryMu`, refuse
if closing or a recovery job owns this slug, and compare the current operation
with the exact failed snapshot being reconciled before deleting it. A newer
recovering entry, hard failure or replacement must survive. Do not hold these
in-process mutexes during I/O. This is removal of an obsolete access error, not
publication of execution permission. Do not call resume/Continue/Send, clear an
attempt, write RecoveryStore, add ActiveThreads, change Automatic, reset a
continuation, or touch queues/goals. Normal `recoveryStatus` then projects active
permission, held idle, saved work or unverifiable work from the existing sources.

The current 30-second backoff governs another restore command, not recognizing
that one is unnecessary. Check it only after current-runtime reconciliation,
immediately before launch eligibility. A temporary failure can therefore clear
on the next ordinary five-second sweep. Noninteractive runtime still uses the
same backoff/two slots and exit75 retry behavior. Hard failures remain explicit
Retry cases. No new timer, detached worker, state/schema field, generic error
clearing, browser readiness override or record-repair mechanism.

Owner0's complete package: `portal/internal/web/recovery.go`, existing focused
`recovery_test.go` and real-route `retained_input_test.go`/
`recovery_input_browser_test.cjs`, and the existing recovery paragraph in
`docs/workspace-portal.md`. No Ruby, client, dependency, naming, native or product
JS behavior change. A small extraction of the existing sweep step is permitted
to test it deterministically without sleeping through its timer/backoff.

Quick regressions must create the actual exit75 failure via the existing helper
fixture, then prove interactive recovery retires it without a second helper
invocation. Compare recovery/continuation/receipt state before and after; clearing
must produce no native load/start/queue calls. Cover already-active and held
states, including held queue/goal/unknown preserving their normal blockers;
hard exit1, Automatic=false, wrong identity/generation/provider/pending lifecycle,
and missing live runtime remain uncleared. A barrier case replaces the observed
failure with a new job/hard failure before retirement and proves it survives.
Assert the live branch bypasses launch backoff without admitting another command.

After quick Go route/recovery checks and a committed affected independent review,
run only the existing affected mounted real-route recovery/input fixture. Give
it a real server temporary failure and then run the coordinator's same verified
step; require the page to lose the stale error and enable an explicit original-ID
message without reload or automatic replay. Reuse its accepted/unknown receipt
checks; no mocked successful message POST or new browser suite. Use the normal
watcher for uncertain-duration checks, followed by ordinary required final
package/CI/activation verification. No extra VM/native/provider campaign or
target-session action. Preserve prior evidence at its actual scope. Pending
consumer pins consolidate later within the new unmerged stream; the stopped
profile rollout remains a lead-owned operational decision. Architect changed
this design only and ran no tests, builds or live/private diagnostics.

## Older-session input provenance and held timing, 2026-10-27

Lead accepted this bounded corrective package. It is a new commit after merged
runtime `0e47e92f`, independent of the previously accepted delivery/integrations;
do not rewrite merged history. Owner0 may implement after reading this section.
The user's quoted `release kb staging please` is diagnostic context, not an
instruction to release staging or execute anything in the reported session.

Actual evidence for the specifically reported `2026-09-13-auth-email` target:
the selected portal service logged four POSTs at 19:38:55–19:39:11 UTC, each
failing `resolve conversation: retained runtime authority changed`. Logger
source includes only method/path/error. Client583 returns the generic404 before
body decoding, SendAttempted, reconciliation or native submission. These
invocations never reached delivery; the saved original outcome remains unknown.
Narrow metadata inspection found open/work, lifecycle active, schema1 with
creation/repository/artifact keys, manifest client version `0.154.0`, ready
authority version `0.159.2`, and selected portal version `0.164.0`. Authority
slug/workspace/root-thread/socket match the manifest and selected endpoint.
Only those scalars/equality results were retained; no prompt/receipt/history or
target-team reads or mutations occurred.

This is a supported provenance difference. `reconcile_native_client!` and
`update_native_client_version!` update the actual tmux version and ready runtime
authority without rewriting manifest `codex.client_version`.
`require_current_codex_provenance!`, `session_codex_provenance_matches?` and
`normalizeInteractivity` bind root/socket and independently validate runtime
authority. By contrast, `requireRetainedInputIdentity` rejects the historical
manifest/terminal version difference; creationless ordinary web mutation
admission repeats that same equality. Neither old scalar denotes the currently
selected App Server. Do not rewrite either record or replace the equality with
a requirement that either historical version equal selected0.164.

Owner0's application boundary is `portal/internal/web/plan_delivery.go` and the
ordinary retained mutation helper in `server.go`: remove only that cross-record
version equality. Preserve valid manifest provenance, ready authority, exact
slug/workspace/root/socket, current package generation, provider/lifecycle and
creation receipts, native cwd/identity, original submission proof, mode binding,
and all existing locks. `RuntimeAuthority.VerifyTmux` continues checking the
actual terminal version against its runtime authority, including tamper refusal.
Cold new-input admission still requires the stopped managed pane and no old
queue/goal under Runtime EX. Accepted originals return their receipt; submitting
unknown originals reconcile without replay. No blanket404-to-notSent conversion,
automatic copy, new ID, implicit resume, historical scope fallback, Ruby guard
change, client/API change or new admission framework.

The reported `Loading timing…` has a separate source cause: app.js
`refreshActivity` intentionally returns while executionHeld, but
`updateCodexWork` leaves the initial loading text when no snapshot exists.
Use the existing `Timing unavailable` text for held/no-snapshot presentation;
preserve any available snapshot and current post-activation refresh behavior.
Do not fetch activity, fabricate zero durations, resume a thread or release a
hold to fill the display. The bounded log also showed one thread/page read
failure at 19:38:50; it does not establish another version-equality failure or
justify broader native/history inspection.

Owner0 also owns this small app.js rendering change, the existing
`retained_input_test.go` real HTTP fixture and
`recovery_input_browser_test.cjs`, plus the affected ordinary retained readiness
paragraph in `docs/workspace-portal.md`. Test the real
`/api/sessions/example/message` path with manifest154, authority+fake-tmux159,
and selected164: explicit original-ID retry with no prior durable attempt,
prepared, accepted and genuinely unknown states. Require exact ID/content,
at most one delivery for fresh/prepared, the same accepted receipt without new
execution, and unknown reconciliation with no resume/start/copy. Include the
creation-ready held path that failed here and representative creationless
ordinary admission; preserve actual tmux-authority version mismatch, wrong
root/socket and archive refusal with zero effects. Capture immutable fixture
manifest/authority bytes to show admission does not repair them.

Extend the existing mounted real-route fixture to reload an older held session
with the original buffered entry, show Timing unavailable without activity
requests, and explicitly Retry original using its unchanged ID. Keep its true
unknown case and verify no unsolicited delivery. A successful fresh original
may start the existing timing refresh only after receipt/permission publication.
Do not mock the message POST or add a new fixture/suite. Quick Go route/identity
and existing Node checks precede the new committed affected independent review;
the existing mounted fixture follows review under normal watcher procedure.
Then use ordinary final package/CI/activation verification for the successor,
with no extra VM/native/provider campaign. Existing successful unrelated checks
retain only their actual unchanged scope. No dependency or persisted-format
change, migration, target-record repair or machine action is part of this brief.
Architect ran source/diagnostic reads only and changed this design, not product
source. Preserve the reported original for the user's later explicit retry.

## Naming high: real client admission correction, 2026-10-27

Lead accepted this bounded correction and released implementation to owner0 once
saved. It supersedes the earlier b44 rollout-readiness assumption; the separate
progress UI remains unchanged. CI40551336662 failed creation at runtime
`b44fb1a86af8ba2706a9d722b151c096ac3ef827`: naming returned settings failure
before any provider request. The retained evidence is
`naming-high/ci-40551336662-diagnosis.md` and its linked original log/metadata.
Runtime b44 and bb238 pass `high`, but consumed client
`255f0b4f74951ebbd0a5ab15eea7a3142be0ab93` rejects every effort except `low`
in the shared preconnection guard. The runtime adapter mock never exercised
that guard. This is a confirmed contract mismatch, not a provider failure.

The supported pairs are explicit: strict `RunEphemeralTurn` keeps
`gpt-5.5/low` and `gpt-6-luna/low`; prompted `RunPromptedEphemeralTurn` accepts
only `gpt-6-luna/low` and `gpt-6-luna/high`. Preserve prompted low for existing
callers. The immutable Luna catalog declares low/medium/high/xhigh/max, but its
broader capability list does not expand this bounded naming API to every level.
Retain the existing exact `model/list` effort check: advertised high is required
before creating a thread. Do not normalize, substitute or silently downgrade
an unsupported effort. No catalog bytes, hashes, generator, protocol shape,
native package, fixed restrictions, provider selection, private transport,
deadline, sink, retry proof or teardown behavior changes. Prompt guidance still
does not establish strict native tool isolation.

Owner0 owns one serialized package across both repositories:

- Client: `codex/ephemeral.go` guard and public comment;
  `codex/prompted_ephemeral_test.go` and the strict profile cases in
  `codex/ephemeral_test.go`; matching profile wording in `docs/reference.md`
  and `skills/update-codex-web/SKILL.md`. No broader skill/docs rewrite.
- Runtime consumer: publish the reviewed client first, then update its exact
  selection in `flake.nix`, `flake.lock`, `portal/go.mod`, `portal/go.sum` and
  `nix/workspace-portal.nix`. Retain the runtime's high option and existing
  adapter assertion; native/source/catalog inputs stay fixed. Compute and
  verify the final vendorHash from the changed client contents once, retaining
  the actual fresh dependency derivation evidence; an old cached hash does not
  prove new vendored content. No redundant rebuild after that proof.

The decisive regression calls the real public client using existing
`promptedEphemeralFixture`/`ephemeralFake`, not an injected naming adapter.
Table the existing private-policy/provider test over low and high, require the
unchanged defenses and exact requested `turn/start.effort`, one thread/turn,
successful final output and unsubscribe/cleanup. High is RED on client255's
actual guard and GREEN after the correction. Keep provider mismatch behavior.
Replace the prompted test's obsolete high-rejection case with unsupported
values; keep strict high rejected for both strict models before connection.
Add high absent from `model/list` as a settings failure with zero thread/turn
starts. Existing deadline, observer, catalog, question and retry tests retain
their guarantees. No new transport harness or client API is needed.

Quick checks cover these public-client tests, existing runtime naming adapter
tests and pin/import checks. Reuse already generated exact native schema/config
inputs for any required existing validator; no schema regeneration or corpus
expansion is caused by an effort scalar already represented in the corpus.
Commit the complete units and obtain independent affected client/runtime review
before long verification. Then use normal required final package/CI and
activation verification. The original creation failure must be corrected, not
waived; no separate VM, native/provider, catalog or corpus campaign is added.
Do not claim provider quality/latency from the fake transport result.

Preserve refs and rollout evidence for client255, deployed b44/yi4 and retained
bb238 before any feature-series consolidation. Keep the client change coherent
with its prompted contract, and consolidate the runtime dependency selections
into the existing logical update stream. Do not rewrite released/default
history; retain any concrete supported consumer boundary. Record old/new ranges
and equivalence for the unchanged UI patch and reuse its mounted PASS only for
those identical UI inputs. The corrected client requires fresh affected review
and consumer dependency evidence. No persistent format or migration changes;
older clients still reject high. Deploy the corrected consumer as a new verified
successor, without relabelling b44's earlier health checks as naming success.
Merge/default integration remains unapproved. Architect changed this design
only and ran no tests, builds, live/native/provider actions or Git mutations.

## Hideable progress concern, 2026-10-27

User-requested, bounded frontend milestone; design ready for lead release to
owner0. The naming b44 rollout proceeds independently on its frozen source and
must not wait for or consume this change. Architect scope is this section only;
no application edit, test, build, live action, state or rollout change was made.

Source confirms that `progress-observer.mjs` rewrites the entire warning above
the Codex heading on every poll. The existing `.chat-heading` supports a compact
button beside its h2 and wraps below 650px; no new toolbar is needed.
`progressobserver.State.Apply` retains `concern.key` while summary, count and
lead response change. Only the existing matching resolution/evidence contract
clears the concern. The browser already receives that key and warning flag.

Owner0 owns one implementation unit:
`portal/internal/web/static/progress-observer.mjs`,
`portal/internal/web/templates/session.html`,
`portal/internal/web/static/style.css`,
`portal/internal/web/progress_observer_test.cjs`, the affected portion of
`portal/internal/web/presentation_browser_test.cjs`, and the small existing
Progress status paragraph in `docs/workspace-portal.md`. No app.js, Go handler,
observer scheduler/state, native/client, dependency, schema or workflow change.

- Group the Codex h2 with a native `type="button"` triangle using the existing
  `icon-button` appearance/focus behavior and warning color. Keep the group
  together when the heading wraps. Use ID `progress-observer-warning-toggle`,
  title and accessible name `Progress concern`, `aria-controls` pointing to
  `progress-observer-warning`, and accurate `aria-expanded`. The decorative
  triangle is aria-hidden. Show the button whenever the existing warning is
  active, including while the panel is hidden; remove both only when the
  authoritative response no longer reports a warning.
- Move the existing warning below the heading and make it a labelled panel
  containing heading `Progress concern`, visible `Hide` button
  (`progress-observer-warning-hide`), and a plain-text body
  (`progress-observer-warning-message`). The triangle toggles the panel; Hide
  collapses it and returns focus to the triangle. Preserve `textContent` for
  all concern/response text and the full Settings view. No modal, focus trap,
  automatic focus or new navigation structure.
- Cap the entire expanded panel at `min(12rem, 25dvh)` with border-box sizing.
  Keep its heading/Hide row visible and put overflow in its body using
  `min-height: 0`, `overflow-y: auto`, preserved line breaks and wrapping.
  The body is keyboard-focusable and named by the panel heading. Scope CSS to
  these controls, including explicit `[hidden]` rules so flex display cannot
  expose hidden elements. Keep the composer reachable and conversation visible
  at desktop and narrow/short viewports. A long message must not grow the panel.
- Keep only a hidden concern key in tab-local `sessionStorage`, under
  `workspace-portal.progress-concern-hidden.${slug}`. Store no concern text.
  Catch storage access/write failures and keep the same behavior in memory.
  The stored key must equal the current nonempty `concern.key` to hide it.
  Repeated polls, count/summary/response updates, focus refresh and reload of
  the same tab preserve Hide. A different key opens the bounded panel; clear
  the old preference when an authoritative response resolves/removes the
  concern. Reopen clears the matching preference. Initial loading and failed
  reads must not clear it or claim resolution. A missing key gets no durable
  hide identity. Do not synchronize tabs or invent a concern history.
- Local hide/reopen works in read-only views and while checks are paused. It
  sends no POST and changes no enabled/running/concern/recovery state. Keep
  current polling/lifecycle behavior. Avoid rewriting unchanged live text;
  use a short polite announcement for a newly observed concern key, outside
  the interactive panel, rather than announcing its full text on every poll.

Acceptance and checks: extend the existing Node mount contract to cover
Hide/reopen with zero writes, same-key text/count/response updates staying
hidden, reload and session isolation, a new key opening, authoritative removal,
read failure and unavailable storage, read-only use, literal unsafe text,
ARIA state and focus return. Run its existing `TestProgressBrowserPresentation`
entry (or the same Node script directly), syntax checks and diff checks in the
repository Nix environment. Keep the existing settings/check-now assertions.
One mounted check is warranted because the reported failure is lost viewport
space: extend the existing presentation script with a long mocked progress GET,
keyboard Hide/reopen, persistent triangle, bounded scroll body, visible composer
and no horizontal overflow at desktop and narrow/short dimensions. Exercise
only `TestQuestionBrowser/presentation_browser_test.cjs` through the established
Playwright fixture; mocking this read-only response is sufficient for this
presentation contract. No new fixture server, suite or real observer run.
Commit the unit after quick checks and obtain final independent affected review
before the mounted integration check. Use the existing watcher procedure for
that check if its runtime is uncertain. Stop after this bounded verification;
no VM/native/naming campaign is justified by these files.

Compatibility: existing GET/POST contracts and authoritative evidence semantics
are unchanged. The optional browser preference is disposable and ignored by
older assets; rollback needs no migration. Later ordinary frontend deployment
is separate from the in-flight b44 rollout. Lead owns final prose, records and
deployment/review coordination; owner0 owns implementation and its Git work.

## Approved recovery and manual input fix, 2026-10-27

### Deployed3e29 follow-up: real HTTP admission

Authorized correction; merge/release remain paused. Owner0's narrowly filtered
selected-service log records the CPU message POST twice at 16:00:47/16:01:02 UTC:
`resolve conversation: retained runtime authority changed`. Client255 emits the
reported generic404 before decoding the message or calling Send. This identifies
this request's pre-submission refusal, not the original attempt's delivery state.
Preserve the original ID and exact reconciliation; never convert generic404 into
positive unsent evidence or resend a new ID.

The confirmed source defect is reuse of `requirePlanDeliveryIdentity`
for ordinary cold input: it requires lifecycle `active`, although completed/open
sessions remain interactive under the existing ordinary contract and
`TestTerminalUnarchivedSessionRemainsInteractive`. After the HTTPS metadata read
failed trusted TLS validation, the lead separately authorized one selected local
router HTTP read. Owner0 obtained HTTP200 and only the opening body attributes:
CPU lifecycle `complete`, archived `false`. This proves the active-only predicate
blocks that open session; it does not rule out another independent authority
mismatch. No private records, transcript or delivery probes were read.

Frozen implementation boundary: owner0 extracts the existing common identity
validation into an ordinary retained-input helper, allowing supported unarchived
`active`, `complete` and `abandoned` sessions. `requirePlanDeliveryIdentity` remains
a thin active-only plan wrapper around that validation. Use the ordinary helper
at the held message resolver and member cold-send identity callsites; leave actual
plan admission/reconciliation callsites on the plan wrapper. Preserve exact
root/socket/version/tmux/native identity, provider, archive and pending-lifecycle
checks; do not change lifecycle to active, repair authority, or weaken general
observation. This fixes the incorrect ordinary-send restriction without changing
the plan-specific product policy or taking a general retry redesign.
Owner0 owns runtime/Go tests and sole Git. Owner3 owns only the necessary browser
regression; no JS permission or client protocol change is presently selected.

Acceptance must traverse the real browser root alias
`POST /api/sessions/<slug>/message` through `Server.Handler`, resolver, generic
conversation handler and cold send. A completed/open fixture with valid retained
authority and inactive/no-queue/no-goal native state must accept the exact saved
waiting ID once. Cover complete and abandoned, plus the original ID with
`retry:true`: an exact prepared/unsent original may progress, accepted returns its
receipt without replay, and submitting-without-proof remains unknown without
dispatch. Retain real authority/version/archive negative cases with zero native
dispatch and a plan-policy negative proving the wrapper remains active-only. Replace
the relevant mounted fixture's fabricated message202 with this actual route;
reload sends nothing, explicit Resume sending uses the saved ID/text/attachments,
mode precedes the first native send and permission follows its receipt. Current
wrapper-only positive tests and mocked browser202 do not establish this boundary.
No new native, vendor, schema or broad verification campaign is required.

Verification for this correction is the focused real-handler Go cases, affected
independent review, then the mounted original-ID path against that handler and
ordinary exact-final package build/feature CI. Required final CI jobs run once;
do not dispatch duplicate creation/archive workflows. The changed admission
helper and badge renderer do not alter host activation, service/boot configuration,
native invocation, queue/receipt storage or dependency generation. Reuse successful
host/boot VM evidence for those unchanged behaviors without another VM campaign.
Call a VM result exact-final only when its actual derivation/consumed input scope
is unchanged; if packaging gives the VM a different derivation, retain the old
result as scoped infrastructure evidence, not a new-head PASS. The real HTTP and
mounted tests supply the missing changed-path proof. A concrete relevant VM input
or behavior change reopens only that affected check, not the historical batch.

### Separate display-only unloaded-thread label

Implementer1 owns the bounded `static/app.js` status-badge renderer and its focused
existing Node contract cases; owner0 remains sole Git owner. Coordinate that one
file with owner3, who owns the CPU mounted regression. This separate milestone
must not hold the CPU commit, review or real-route acceptance.

Render `Idle` instead of raw `notLoaded` only when the current selected thread has
fresh successful recovery classification `state: idle`, with no error,
`inputBlockedReason` or `workKind`. Never infer idle from `notLoaded` alone,
notice dismissal or an absent banner. Scope/invalidate the display proof when
thread identity changes. Use one small badge-rendering function from both existing
transcript and recovery updates so either arrival order converges to the same
label; uncertainty retains the truthful native/unavailable presentation. Do not
change raw status, `threadActive`/`threadIdle`, readiness, `executionHeld`, automatic
dispatch, subscriptions, server responses or native calls.

Extend the existing Node contract for both update orders: verified idle plus
notLoaded gives Idle while execution stays held; notLoaded without proof and
queued/goal/interrupted/unavailable states do not get that label; thread changes
discard prior proof. Syntax and those focused contracts suffice for this label
delta. No additional mounted suite, VM, native test or long check is selected.

**Implementation approved:** the user said “okay, proceed with implementation”
and authorized autonomous aitherdev deployment. Merge/release remain paused until
corrected verification. The lead owns execution/review/deployment sequencing.
Only the CPU session's public lifecycle/open attributes and scoped sanitized
request-error metadata were inspected as described above; neither reported
session's native/queue/receipt state was read. No foreign session action is authorized.

Confirmed source mechanism: `RecoveryStore.Set` clears execution permission on
socket-epoch change. `web/recovery.go` labels every interactive held thread
`waiting`, without checking whether work was interrupted. Dismissal only saves a
notice preference. Meanwhile `static/app.js` accepts and stores a new message but
its dispatcher requires `!executionHeld`; it also hides Plan/Default. Thus the
browser can show a perpetual local “Waiting to send” without making an HTTP send.
The plan renderer and recovery banner have independent predicates, so both can
appear while the plan dispatch remains blocked. These mechanisms fit the reports;
they do not establish either session's individual delivery history.

Recommended behavior:

- Separate runtime access, implicit execution permission and actual pending work.
  A verified completed idle/unloaded thread with no queue or active goal reopens
  normally, without a restoration prompt. Use existing bounded cold reads and
  existing refresh paths; a GET must not load a thread or grant `ActiveThreads`.
  An epoch change alone is not an interrupted-task classification. Unknown or
  failed observation stays explicit; never describe it as known saved work.
- Offer opt-in continuation for positively identified interrupted execution or
  saved queued/goal work. Dismiss means handle manually: hide the notice without
  executing anything, but keep the composer and supported mode controls usable.
  Show unavailable metadata/capabilities with their reason; do not invent Default.
- A fresh Send or Implement plan is explicit intent. For a cold target, validate
  identity/generation and check prior queue/active goal before enqueueing or
  loading. Empty queue/no goal permits the ordinary supported path. Actual prior
  work gets a specific inline refusal and its existing work controls, preserving
  draft/attachments/original attempt ID; no mandatory recovery dialog or silent
  activation of older work. Native resume can release queues/goals, and client255
  has no primitive that runs only new input while arbitrary old work stays held.
  Unknown original sends remain unchanged and use exact receipt recovery only.
- Keep fresh explicit sends distinct from restored local waiting entries and
  uncertain originals. A readiness change must either progress the fresh attempt
  once or explain its blocker; opening/dismissing the page must not drain older
  entries automatically. A knowingly closed dispatch gate must not report an
  indefinite unexplained “Waiting to send”.
- Give the existing composer view one action-precedence decision. A completed
  current plan on an otherwise idle restored thread shows the ordinary plan
  choice, with no competing recovery Continue. Actual interruption/saved work
  shows its applicable choice; native blocking questions still take precedence.
  Dismissal exposes manual input without authorizing stale plan attempts.

Owner0 owns Go/runtime admission, templates/docs and sole Git operations. Owner3
owns `static/app.js` and its assigned browser/Node regressions; owner0 must not edit
those files concurrently. No client source/API change is selected. Freeze this
small additive response contract in existing page/details/recovery responses:

| Field | Meaning |
| --- | --- |
| `executionHeld` | Authoritative implicit-execution hold, independent of presentation state. True keeps subscriptions, implicit resume and automatic dispatch paused. Missing field uses the old conservative `state != active` fallback. |
| `state` | Keep existing values; add `idle` for positively inactive/no-queue/no-active-goal restored access and `unavailable` for unproven observation. `waiting` requires positive actual saved work. `idle` hides the recovery banner without granting execution permission. |
| `workKind` | Optional `queue`, `goal` or `interrupted` reason for waiting. A historical terminal failed/canceled/interrupted turn alone is not fresh interrupted work; an already-idle session stays normal. |
| `inputBlockedReason` | Specific current reason a new input cannot safely activate (prior queue/goal, unknown execution or runtime authority). Show inline, keep composer/draft; do not capture into unexplained waiting. No reason for an otherwise ready idle cold target. |

Explicit Send/Resume sending/Implement eligibility uses interactive access and
these fields, not `!executionHeld`. Automatic retries/draining and subscriptions
retain the hold. An existing local waiting `say hi` is resumed only by its user's
explicit Resume sending, with its original ID/text/attachments. No startup drain.
Use the existing `message_not_sent`, HTTP503, `notSent:true`, `retryable:false`
response for a positively unsent cold refusal; do not introduce a generic409
that the browser would misclassify as uncertain delivery. Refresh existing details
for `inputBlockedReason`; preserve true outcome-unknown responses and originals.
Mode uses the existing settings API's `collaborationMode`, projected in cold
transcript/page results. Load the existing mode catalog while held; no Default
guess, no new polling. Hide only genuinely unsupported controls, with an explicit
loading/unavailable state when support is not yet known.

The bounded writer fence is existing per-session Runtime EX, acquired initially
after transition SH (never upgrade an already-held SH), then roster/message locks
in existing order. Re-read scope/permission after acquisition. It excludes managed
HTTP, CLI/team and scheduler writes; hot operations retain SH. Under EX, extend the
existing exact tmux-authority reader to verify its retained Codex pane is stopped/
the configured shell. Canonical restoration uses `launch_codex:false`, and
`reconcile_native_client!` declines launch while held; EX excludes CLI relaunch.
Do not stop a native client to pass this check. A running managed native client,
active/in-progress/pending native work, prior queue or active goal yields a visible
refusal. Inactive loaded status alone is not a refusal when the managed writer
and actual work checks pass. Raw operator clients are outside this managed
contract; no hostile-process exclusion or new lock framework is added.

Cold explicit send ordering: reconcile the exact original first; a found receipt
returns without resubmission, and uncertainty stays uncertain. For fresh/proven
prepared input, use existing Prepare plus IsPrepared proof, then revalidate empty
queue/no-goal/native inactivity before effects. Capture the pending selected mode
and exact request ID/native epoch in the existing deferred-settings record before load; reject
a conflicting mode/request change while this activation remains unresolved. Load
with policy/model/effort, apply and confirm mode, then dispatch the same prepared
ID through a runtime-local direct validated client call, without recursively
reentering the cold wrapper. **Publish ActiveThreads only after its exact receipt**;
mode/load/definitely-unsent failure keeps the hold and binding for explicit retry.
An uncertain dispatch is reconcile-only; no requeue or synthetic continuation.
Clear the binding on the matching accepted receipt; a receipt from an older epoch
never grants permission in a new one. The existing activation API
does not apply collaboration mode, so queue-before-load-before-mode is forbidden.
This reuses native/client calls and the existing record/locks, not a new ledger.

Cross-entrypoint continuation must honor that retained binding after Runtime EX
is released. In `workspacecodex.sendWithRecovery`, reconcile the incoming exact
original first; a confirmed receipt may return without activation. Before any
new Prepare/Queue/load/permission publication for a held target, read the existing
thread-scoped `next-settings` binding and refuse if its request ID is unresolved,
including a different socket epoch. Do not treat a matching ID as authorization
to bypass its bound mode: only the existing mode-aware original recovery path
may finish it. Continue and queue Start use the same rule before enqueue/load.
Absent records or ordinary deferred settings without a request binding retain
existing explicit-assignment behavior; do not generalize this into a new policy
for all team deliveries. Share a small identity-validating private-record reader
below `web` if needed; retain its current path/format/limits and existing runtime
locks, with no new ledger, RPC or migration. Malformed or mismatched binding
records refuse rather than disappearing. One focused cross-entrypoint regression
covers failed cold mode/send -> later CLI/team assignment refused without queue,
load or permission writes and binding unchanged -> exact original recovery still
works; existing no-binding assignment coverage remains applicable.

No native, receipt, recovery-schema or roster migration is expected. An optional
deferred mode is additive to the existing private settings record; older readers
ignore it, so it does not promise old-package behavior. Preserve current forward
recovery, exact identity, lifecycle and delivery contracts. Focused
existing Go/Node/browser regressions cover idle epoch change without notice or
execution; real interruption; dismiss then one fresh send; old queue/goal refusal
before enqueue/load; unknown/restored attempts not replayed; mode applied before
first turn (including failure); and one plan/recovery choice. Reuse unaffected
client/native evidence. No new campaign; this proposal ran no checks.

## Deployment-blocking idle refusal fix, 2026-10-27

The user rejected indefinite deployment refusal from invisible delivery records.
This authorizes a bounded runtime fix; application deployment and integration are
paused pending its review and verification. Native idle and an empty browser
receipt panel do not prove server receipt settlement: browser send receipts live
in tab-local sessionStorage, independently of the durable submission database.
Do not require receipt repair or add a receipt UI. Retain client025's behavior
except the narrowly required observer queue-read permission described below.

**Acceptance:** a compatible forward package/native transition may preserve inert
prepared or submitting attempts with uncertain outcomes. It must not mark them
accepted, discard them, resend them, change their IDs/options/context, or treat a
SQLite admission claim as proof of a live sender. Unknown native execution,
identity, storage validity or compatibility still refuses. Strict archive,
retirement, stop and other existing lifecycle checks remain unchanged.

Owner0 owns one runtime implementation package:

| Files/interface | Required change |
| --- | --- |
| `libexec/workspace-host`, existing host transition tests | Add a package-transition-only quiescence mode to native-changing profile activation and Codex reconciliation. Hold existing host EX admission, drain previously running portal services through ordinary systemd stop, quiesce selected-generation managed terminals, then perform cold execution checks for roots/members. Do not alter same-native live-switch behavior, unregister/suspend/provider transitions, or generic predecessor executor selection. |
| `libexec/dev-session`, existing tmux/quiesce tests | Pass that distinct mode only through quiesce to root/team proof helpers. Retain creation/slug locks, exact workspace/socket/state root, predecessor profile token/generation, stopped-terminal behavior and selected-package compensation. Ordinary quiesce and lifecycle callers retain strict idle. |
| `portal/cmd/workspace-portal/main.go`, `portal/internal/workspacecodex`, `portal/internal/teamruntime`, adjacent tests | Add explicit execution-quiescence commands/methods for the transition path, composed from existing client APIs. Traverse the same retained ready root/member identities and reject pending retirement/automatic retry work. Validate native identity, terminal turn/activity status and empty native queue, and validate the selected submission store through its existing thread-scoped reader. Preserve all receipt records, including unknown outcomes. Do not reuse strict `RequireSubmissionAttemptsResolved` or catch-and-ignore its error. |
| `portal/cmd/workspace-portal/main.go`, `naming_runtime.go` and its existing tests | Pass host-supplied `serve --codex-version` into naming startup. Before spawning any bundled process, require it to equal the child's pinned `0.164.0`; missing/mismatched identity leaves the existing namer unavailable. Retain the child binary's own exact-version check. |
| `docs/workspace-portal.md` | Explain this execution-versus-receipt distinction, brief portal outage/compensation and supported staged bootstrap after owner2's proof. Lead applies final user-facing writing. |

The host EX lock drains supported synchronous application calls through their
receipt writes: HTTP send/ack/queue/respond retains resolver SH until handler
return, including a disconnected browser's admitted send; plan/team requests,
CLI/report/creation, coordination notification helpers and retry/progress/archive
workers likewise retain SH around dispatch and receipt completion. Native TUI
clients bypass that application lock and retain existing terminal quiescence.
Client-owned implicit-resume goroutines and auto-answer timers also bypass SH;
therefore EX alone is insufficient. Stop the selected portal process/service and
confirm its termination before final observation. Client.Close is not a join.
Do not introduce a client lease API, liveness schema or general drain framework.

Use a fresh unwatched cold proof client with ObserverOnly, no observer subscription,
no implicit resume and no automatic answers/rejections/settings writes. Its RPC
allowlist is native metadata/turn/queue reads plus initialization. An empty local
prompt map on this new connection is not evidence of no native prompts: require
an exact singleton status object `{"type":"idle"}` or `{"type":"notLoaded"}`,
matching retained identity and a terminal latest turn. Reject `active` (including
empty or waiting flags), `systemError`, missing/unknown/malformed status and
in-progress turns even if metadata says idle. `notLoaded` is positive unloaded
status, not an unknown-state fallback; do not resume a retained root/member to
inspect it. For nonarchived unloaded threads, native `thread/queue/list` reads
stored queue rows without loading the thread; an actual queue still refuses.
Cold archived threads reject that RPC, so retain their separate positive archived
identity proof rather than interpreting its error as an empty queue. Test an
unloaded retained root and ready member with terminal history and empty queue,
plus unloaded queued refusal and contradictory status/turn refusal.
Exercise the helper with incoming request and
reconnect events to prove it sends no resume/answer/start/steer/queue mutation.
Preserve the existing archived-member identity distinction without loading them.

Owner3 owns one necessary client exception discovered by the focused runtime test:
add only `thread/queue/list` to `codex/client.go`'s ObserverOnly request allowlist.
The native0.163/0.164 `request_processors/thread_queue_processor.rs:list` reads
`QueuedItemService.list_page`; `require_thread` reads stored metadata for an
unloaded thread and never resumes it. Their `thread_status.rs` maps absent/unloaded
runtime to NotLoaded and upgrades idle/notLoaded to Active for an in-progress
turn. The unchanged client native state06 fixture also reads an unloaded held
queue and verifies that it stays unloaded without inference. Reuse that evidence.
Add a focused observer queue-pagination/read test with incoming requests and
assert no answer/resume or mutation; add/update/start/delete and turn mutations
must remain refused. No new client API, state schema or general permission.
Publish the narrow successor, retain025, and consume its exact runtime module/
flake pins, checksums and vendorHash in the existing dependency update unit.

Remember which portal services were running before drainage. Before profile
selection, any drain/quiesce/proof failure restores those services and every
actually quiesced terminal through the selected generation, reporting incomplete
compensation honestly. Previously stopped services/terminals stay stopped. Native
App Server is not stopped merely to make its active work disappear. After profile
selection retain existing forward-only recovery, pending target, native roots,
claim and activation-completion rules; never restore the predecessor package.
Keep portals drained through the last proof and native cutover; a new portal must
not resume old native threads in the gap between checking idle and restarting.

Quick acceptance is one affected batch: idle prepared/submitting records survive
the transition reader/reopen unchanged and missing-history retry remains unknown;
strict archive still refuses them; active/waiting root/member, queue, invalid
identity/store or owned retry refuses. Barrier coverage proves EX waits through a
disconnected send's receipt and excludes new sends; service-stop ordering excludes
async resume/auto-answer before cold proof. Host tests cover no profile selection
before proof, previously-stopped preservation, partial-drain/refusal compensation,
selected-generation helpers and forward recovery after selection. Reuse existing
client receipt/admission tests; no native compatibility or canary campaign.

Owner2 verified the existing same-native bootstrap end to end. The override is
passed to candidate activation; native launch markers, arguments, capacity,
reporting equivalence, protocol checks, profile tokens and claim guards remain
authoritative. The first ordinary switch uses the final fixed source and
`DEV_WORKSPACES_SYSTEM_CODEX=/nix/store/jrsm1rzxm1ak23j1f2vn0lil9qgxblym-codex-package-0.163.0/bin/codex`.
It keeps the current daemon/terminal processes, restarts portal/router/coordinator,
refreshes inventory and clears pending state. A live-predicate mismatch refuses
under the predecessor's ordinary rules; never force it. No candidate helper,
bridge package or executor adapter is needed.

The lead accepted one necessary startup prerequisite: suppress bundled0.164 naming
while ordinary0.163 remains active. Both use the host-selected Codex home, and
ephemeral0.164 startup can write/prune diagnostic SQLite; state06 proved only an
offline old-reader cold read, not concurrent mixed writers. Private sockets do
not isolate this storage. During stage1 automatic naming is unavailable, with
the existing retained-request/manual-name path; no0.164 naming process may start.
Test missing/0.163 active version with an executable that records any invocation:
there must be none, including a version probe. Matching0.164 retains existing
startup/ownership behavior. Do not copy credentials or create another home.

The second ordinary switch uses the same final source with the override removed,
from the external shell once actual native work is idle. It now runs the fixed
selected helper, preserves dormant receipts, drains portal/terminal writers and
adopts packaged0.164 before starting matching private naming. Only this step can
establish full native/naming readiness. Keep the machine claim and retained roots
through both stages and final integration. The override is transient: after
stage1, the pending-only timer has nothing to reconcile, and activation enables
but does not start the unconditional reconcile service. Do not interleave a boot,
user-manager restart, system-generation change or explicit reconciliation: those
existing entry points use the packaged native without the temporary override.
Preserve ordinary pending/forward recovery if either stage fails.

Preflight isolation is a separate, independently useful owner0 commit in the same
runtime review batch. `probe_codex_registration` and `check_codex` currently put
their sockets/schema output in temporary directories but inherit the caller's
Codex home and cwd. The packaged wrapper only changes PATH. This establishes an
unisolated startup path, not evidence that the earlier attempt changed or damaged
live state. Both preflight App Servers can start before quiescence; the second
bootstrap switch must therefore isolate them before starting candidate0.164.

Within each existing temporary directory, create a private Codex home and use
child-only `CODEX_HOME`, `CODEX_SQLITE_HOME` and the existing
`CODEX_INTERNAL_APP_SERVER_REMOTE_CONTROL_DISABLED=1` marker, with child cwd in
that disposable directory. Apply the same environment/cwd to native schema
generation. Native0.163/0.164 resolve configured `sqlite_home` before the environment
and allow explicit `log_dir`; write only those two disposable absolute paths to
the new home's config so ordinary inherited system defaults cannot redirect
these files. Do not copy caller configuration or credentials, change parent ENV/
cwd, or alter the selected native executable, registration arguments, schema
validator, socket readiness, process-group TERM/wait or cleanup. This isolates
ordinary caller home/environment/project state; it is not a sandbox against
administrator-enforced native storage requirements. Preserve such policy rather
than bypassing it or adding a generic configuration isolation framework.

Extend existing Ruby subprocess coverage with a fake native that records only
its argv, cwd and relevant path variables, writes a disposable sentinel and
serves the probe socket. Assert both App Server sites and schema generation use
the private paths even when caller home/SQLite env/cwd are populated; caller
sentinels, ENV and cwd stay unchanged, registration argv/schema checks still run,
and the child is joined before temporary cleanup on success/refusal. This is a
focused launch-contract regression, not a new native/provider campaign.

After quick checks and committed affected review, use ordinary final consumer
builds and branch CI. Run the existing host job command once on frozen final source
under one fresh utility:
`nix build --no-link --print-build-logs .#checks.x86_64-linux.host-module-idempotency .#checks.x86_64-linux.session-recovery-boot`.
No new suite or workflow edit. Do not dispatch the whole workflow: it duplicates
fast/creation/archive. The ordinary final push supplies those required CI results
once. Reassess at about twenty minutes without automatically adding checks; an
actual failure or unexpected local kernel build returns to the owning procedure.
Reuse unaffected client/native evidence. The observer permission changes actual
vendored client content, so prior1a dependency proof no longer covers final inputs:
refresh the normal module/checksum/vendorHash pins and verify one fresh final
dependency computation under the runtime update skill. Owner0's reserved utility
runs normal hash generation after client review/publication as generated-source
preparation, before runtime commit/review. Retain the exact final inputs, actual
hash computation and successful build with that hash. This satisfies freshness;
do not add a separate `--rebuild` after genuinely recomputing the same final
dependency contents. Reassess only a change to consumed generator inputs, not
later statement-only changes. Host/integration/profile checks remain after the
runtime affected review.
Stop after these affected checks, bootstrap proof and coherent final outputs.

## Current forward refresh, 2026-10-27

The lead confirmed all three prerequisite initiatives merged: title notifications,
CPU improvements and archive permissions. Their merge proofs and the user's
archive-scope confirmation satisfy the wait. The user authorizes refreshed
deployment, verification, then integration of this session's four repositories
into master. This supersedes the earlier approval hold, not the no-canary or
external-shell idle constraints. No activation, claim or lifecycle action is part
of this architect assignment.

Owner0 alone rebases reviewed `7e6d7c9c..096062879a74` onto fresh runtime master.
This assessment covers incoming `7e6d7c9c..fffbd0d59fffc09667cb39878d9f7da8bdcd3806`;
check any later default movement as a delta. Retain the four reviewed feature
units and exact client025/native0.164 selection; never deploy old096 over newer
title/CPU/archive work. Owners1/2 then refresh only their consumer pins on current
defaults. Keep old ranges, builds and review evidence under their original heads.

| Boundary for owner0 and reviewer | Required combined behavior |
| --- | --- |
| `nix/tests/session-archive-lifecycle.nix` | Keep our idle, persisted retry-policy and bounded shared-flock checkpoint before worktree registration. Also keep incoming `require-idle --user-state-root` and read-only-cache archive/revival assertions. The storage-selection fix and ordering fix are complementary. |
| `nix/workspace-portal.nix`, portal guide | Retain incoming `workspace-cleanup-permissions` installation and guide additions alongside our native/client/vendor updates and prompted-naming explanations. No whole-file ours/theirs resolution. |
| CPU retry and shutdown | Preserve settled-retry tokens as process-local scheduling shortcuts: changed, due, missing or uncertain inputs take full admission/receipt recovery. Client025 must not weaken exact capacity classification or retirement cancellation. `Server.Close` must join coordination helpers and operation workers before the naming child closes. |
| Incoming UI, scheduler and archive | Preserve background attention-only title reads without hidden acknowledgment/presence or other hidden polling; bounded identity/generation-keyed coordination display caching; scheduler work selection with action-time ownership fences; temporary owner-write cleanup only within owned directories, no symlink traversal, and original recovery/mode restoration. |

No new persistent format or migration is introduced by this combination. CPU
caches/tokens are memory-only; archive recovery must retain its existing snapshot
and mode checks. The ordinary idle package transition excludes mixed writers.

Reuse client025/native stages00–06 and their stated limits. The actual1a vendor
rebuild also remains applicable to this inspected incoming delta: added Go imports
are standard library/local packages plus already-vendored `codex-web/codex`;
no build/embed directives, module/lock or vendoring hooks change. The Nix package
addition is in installation, not dependency generation. Owner0 must retain that
boundary during resolution; only a concrete new dependency-generation change
requires reconsideration. No second forced rebuild is selected speculatively.

After resolution, one focused quick batch covers existing naming/retirement/
admission tests plus `TestSettledRetry*`, `TestCoordinationCache*`, incoming title
Node contracts and affected Ruby archive/coordination tests. Do not duplicate
checks already run on the final composition. Give the reviewer the old/new ranges,
resolution diff and these shared behaviors under the existing affected-review
workflow; preserve the whole-branch/no-new-migrations conclusion. Use the final
branch's normal fast/creation/archive CI results and ordinary final consumer
builds. Earlier096 results remain historical. No CPU benchmark, optional Firefox
campaign, new native/managed VM suite or real-provider call is added. Stop when
those affected checks/review and final outputs are complete.

The selected coordination guide was read from
`/nix/store/lm7xpfxxzr2012y80wq2fnvirlyfakzz-dev-workspace-0.2.0`; owners1/2 separately
establish actual system/profile/native baselines and final output identities.
Prepare builds/copies before machine ownership. Preserve system-before-profile
ordering and existing journal/claim contracts. The profile's native change needs
all managed roots/team turns idle, with no queued/pending execution; the
caller's turn is not exempt. Use the supported stable switch from an external
ordinary shell with exact session identity and the then-held machine claim. Do
not interrupt sessions, schedule a launcher or bypass an idle refusal.
The new defect-fix section supersedes the older blanket durable-uncertainty gate.

An unresolved-message refusal counts durable nonaccepted attempts; it does not
prove active turns or stale bookkeeping. Attempts do not expire, and require-idle
does not reconcile them. The supported owner recovery starts with the original
portal tab's saved receipts. **Retry original** reconciles an uncertain submitted
attempt by its exact identity, but can dispatch a prepared, proven-unsent original;
it is not a read-only diagnostic. Waiting only helps if an actual sender or normal
transcript acknowledgment is still completing. If public observation cannot verify
identity/persistence, obtain the normal owner-facing conversation/receipt status
before choosing recovery. Do not infer state or manufacture identities from private
records. On the selected lm7 refusal path, source restores the failing terminal and
earlier quiesced terminals, then records the pending candidate before selection.
There is no public pending/restoration-history reader; distinguish that contract
from observed effects. Lead-owned rollout records retain this attempt's facts.

Following authorized activation, verify actual system/profile/native and naming
child/catalog identities, service health, conversation continuity and preservation
of the incoming features. Use packaged tests as archive/creation behavior evidence;
no live archive or real naming canary is authorized by this brief. Recover a
partial switch forward through its original attempt, retaining journals and
roots; old-reader cold-read evidence does not establish downgrade safety.
Then integrate the four approved masters with short separate repository claims
and fresh remote proofs. Release the exact machine claim promptly only after
verified effects and complete deployed lineage are integrated. Preserve source/
output identities and refreshed ranges in existing rollout/review records; leave
both sessions, worktrees and feature refs open/intact.

## Interfaces and implementation

Keep codex-web025's explicit prompted ephemeral entry point and strict0.163 API.
Reuse the unchanged exact client commit and its successful input-scoped evidence.
Runtime naming uses the prompted API, Luna/low, bounded request-only instructions,
30-second total budget, two operation slots and at most one proven safe fresh
attempt. Native willRetry remains on the original turn. Cleanup uncertainty,
invalid output and permanent failures cannot authorize a retry. No generic-name
fallback: pause before reservation and retain manual/retry recovery.

Port runtime1f8ed674 naming/upgrade and875ed0c7 retirement cancellation onto
7e6d7c9c. Retain only ca8c9e03's small private registry/environment correction in
the existing managed fixture. Its historical manifest prerequisites stay as they
are; do not build their replacement or import ca8's manifest/VM/real-canary
framework. Exclude239d8 archive diagnostics andbe5b creation diagnostics. Preserve
all current UI/capacity and observer changes.

The existing managed naming child remains portal-owned, uses a private socket,
does not fall back to the ordinary daemon and is joined after worker cancellation.
Raw0.164 tool restrictions are prompt guidance, not enforced tool isolation.
Retain startup catalogs, bounded output validation, provider selection and privacy.

## Implementation boundaries

| Owner | Files and result | Dependency |
| --- | --- | --- |
| implementer3 | codex-web exact02533a152223416f159bac2578e88bcbe653f247; evidence in client-report.md | Preserve strict0.163 and prompted0.164 APIs; no policy-only client edits |
| implementer0 | Runtime naming adapter/worker and tests, naming startup version prerequisite/tests, loaded-retirement cancellation/tests; existing creation fixtures and package/preparation docs; flake/module/vendor pins | Client025; only remaining feature deltas on current master |
| implementer1 | Configuration dev-workspace channel and generated lock | Published final runtime; retain current system llm-agents ea188 and unrelated inputs |
| implementer2 | Workspace direct nested runtime override and scoped lock update | Same published runtime; preserve extension and unrelated inputs |
| lead | Context-dependent wording, combined acceptance/review, plan/state | Architect advice; owners' coherent commits and check results |

Runtime production paths are `portal/internal/web/session_name.go`,
`session_namer.go`, `portal/cmd/workspace-portal/naming_runtime.go` and
`portal/internal/workspacecodex/client.go`. Native launch ownership changes only
in its accepted version string; process-group, shutdown and service contracts
remain unchanged. Retirement discovery preserves cancellation alongside the
original observation error; it does not change archive dispatch or receipts.

## Compatibility and recovery

No migration is added. Preserve current observer persistence/control behavior and
all upstream delivery, archive preparation, collection and creation locking.
Retirement cancellation only preserves interrupted-operation semantics when
discovery fails; it does not authorize lifecycle actions in this session.
Keep current native packaging helper and fixed raw native bytes. Consumer pins
must select the same reviewed runtime while preserving all unrelated input nodes.

Activation follows the current approval and supported idle guards, system then
application. Existing native025 evidence proves upgrade and an offline old-reader
cold read only. Recovery stays forward; never run concurrent old/new writers.

## Acceptance and verification boundary

Before review, complete coherent commits and declared hooks, pin/protocol checks
and one focused runtime batch in its Nix environment (`-mod=readonly`). Select
existing tests for these risks, without adding a runner:

- `TestNamingRuntime*`: exact version acceptance/predecessor rejection, provider
  arguments, one owned child, group cleanup, constructor/HTTP shutdown.
- `TestSessionNaming*`, `TestSessionName*`, `TestSessionPreparation*`: native retry
  versus one proven fresh attempt, total budget/two slots, invalid output and
  cleanup refusal, cancellation, no fallback/reservation, retained manual recovery.
- `TestCreationAdmissionSharesGenerationWithPayloadCollection`,
  `TestCreationAdmissionDistinguishesRuntimeUpdateFromUnavailableLock`,
  `TestCreationRechecksGenerationAfterWorkerTransitionLock` and preparation
  generation tests: collection admission and package/preparation exclusion.
- `TestRetireThread*`/`TestRetirement*` and existing `TestProgress*` regressions:
  cancellation cause/attempt retention and preservation of current observer state.

Reuse completed client/native results at their actual scope; see
[client-report.md](client-report.md). Stages00–05 executed on8e and were accepted
for unchanged025 inputs. Stage06 executed on025/tree8080: exit0/7s, batch43.031s,
upgrade/restart/fork/receipts/queue/messages and offline old-reader cold reads
passed with no skipped/failed cases and no additional old-reader inference.
The lead read the complete assessment in this session's transcript before its raw
file became unavailable. Surviving Markdown plus that first-hand record support
reuse; do not recreate missing receipt machinery or infer a new execution.
Final consumers must still select the unchanged raw0.164 executable SHA256
`d2af1cd0ea4187d413c237e80204e94ffcd5c7d8142840a662156b89750f54ae` from llm-agents
`ea188d2f072e0ec8d5b71245e228803672801a22`, matching client/catalog inputs.

Independent final review covers complete branch histories, the public API
boundary, incoming observer/UI preservation, source provenance and an explicit
no-new-migrations conclusion. After review, use existing repository checks:

| Required final-input result | Reason and existing command |
| --- | --- |
| Runtime package/focused checks and final system/application builds | New runtime composition and consumer pins need normal package verification; reuse exact successful lower-level checks and dependency evidence |
| `session-creation` once | Prompted0.164, retry and manual recovery now compose with the shipped browser, provider arguments and native initializer; unit/state06 results do not establish this combination. `nix build --no-link --print-build-logs .#checks.x86_64-linux.session-creation` |
| `session-archive-lifecycle` once | New native0.164 participates in the packaged archive tool/shutdown/recovery path, outside state06. Existing pre-deployment requirement: `nix build --no-link --print-build-logs .#checks.x86_64-linux.session-archive-lifecycle` |

Runtime `README.md:418` calls session-creation mandatory; `README.md:450` describes
session-archive-lifecycle and explicitly requires it before deployment at line457.
`.github/workflows/check.yml` triggers on push, pull_request and workflow_dispatch;
its `creation` and `archive` jobs run the commands above on ordinary feature pushes.
Consume one successful normal CI result for the final relevant source/input
composition; do not duplicate it locally. A missing result uses the existing job
or command, not a custom campaign. The separate `host` job is restricted to master
push/manual dispatch and is not added here merely to obtain creation/archive
coverage. Long checks use the lead's single fresh utility and normal CI tooling.

Vendor verification is one ordinary final `goModules --rebuild` in implementer2's
post-review profile batch. Identical client/go.mod/go.sum/vendorHash alone do not
cover its consumed inputs: `nix/workspace-portal.nix:274` supplies runtime source,
and buildGoModule inherits source/hooks and runs `go mod vendor` over the portal
source/test imports. The retained forced proof covered an older runtime, before
the current observer composition. Its missing raw JSON is not the reason to
repeat; the changed generator input is. After the normal profile build makes the
output available, rebuild only `packages.x86_64-linux.default.goModules` from that
same workspace selection, with ordinary substitution enabled for dependencies.
Record target derivation, output, command and successful hash comparison; stop
after that one result. No fake-hash discovery, file inventory, new receipt format
or native-test rerun is needed.

The actual successful rebuild on runtime1a may be reused for successor096062879a74:
its complete diff only moves an existing test assertion and adds two comments.
Imports, package/build selection, modules and generator hooks are unchanged;
`go mod vendor` does not consume test statement order. The source-dependent Nix
derivation identity changes, but the vendoring computation is unaffected. Keep
the execution labelled1a; no second forced rebuild is required for this fix.
Ordinary final consumer builds and required final CI retain their own scope.

No separate managed naming VM or native-retirement campaign is required.
The changed launcher prerequisite is covered by owner tests, while retained raw
native tests cover local-only launch, static catalog and prompted protocol.
Ordinary creation CI covers actual packaged naming/provider composition. Service
cgroup/launch changes would reopen this conclusion; none is present in this patch.
Historical managed fixture prerequisites and unexecuted cases are not passes.

## Real-provider wording and stopping rule

The user's explicit rejection supersedes mandatory real-canary wording for this
session. The lead accepted two short owning-guide corrections in
`docs/codex-package.md` and `docs/session-preparations.md`: describe a canary as
separately authorized optional validation and state that synthetic coverage does
not prove real-provider adherence or latency. Preserve exact-binary, protocol,
cleanup and all other feature requirements. Implementer0 owns those technical
paragraphs; the lead applies the direct writing pass before commit. Do not add a
skill/policy-only commit or alter exact client025. Its reference and the runtime
skill's older wording do not reinstate the rejected gate. No credential/account
prerequisite, auth search, copied credentials or synthetic-as-real claim is
permitted. Positive real inference and serving-transport behavior remain untested.

Build readiness ends when the focused commits/quicks and final review are
resolved, the two standard CI checks and relevant package checks pass on their
final inputs, consumer pins match, and final system/application outputs are built.
Retain compact revision/command/result/output evidence in existing records. Stop
there; no optional canary, extra browser campaign, new manifests or repeated passed
checks. Investigate an actual relevant failure once and repeat only its affected
checks. Reassess a normal dependency-check batch exceeding the repository's
under-20-minute target before expanding work.

Build readiness is not deployment acceptance. Current deployment/verification/
integration authorization and external-shell constraints are recorded in the
forward-refresh section above. No live creation/archive exercise or lifecycle
action is launched by this design. Both sessions stay open and old retained
roots/branches remain intact.
