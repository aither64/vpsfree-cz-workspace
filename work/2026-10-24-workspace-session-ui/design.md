# Portal session controls and message delivery proposal

Status: proposal only, 2026-10-24. Architect investigation for the lead; no
application changes, tests, commits, deployment or lifecycle actions authorized
or performed. The lead owns plan/state and any subsequent assignments.

## Scope and evidence

Recommend three focused changes in `dev-workspace`: reuse the existing switches
for session settings, make New output depend on changes to displayed content,
and accept another message while delivery of the preceding message is pending.
Reuse `codex-web` delivery and native queue contracts. A new server queue or
Codex protocol change is not justified by the evidence.

Session identity was verified with `dev-session current` and both matching
`DEV_SESSION_SLUG`/`DEV_SESSION_WORKSPACE` variables. Only canonical bare
repositories were read. No other session's worktrees were accessed.

The proposal uses these locally cached `origin/master` revisions, without a
fetch or a claim that they are current deployed revisions:

| Repository | Inspected proposal baseline |
| --- | --- |
| dev-workspace | `b3a6eb2fc0b41cf0cb965bf4c39991815d9df734` |
| codex-web | `11ec57d2203fc735696fe75a837d47da55a5c6af` |

The former's `portal/go.mod` pins the latter. Initial inspection also read the
older bare local master heads `52dcd471186ef874c5c93f4133744195d4815454` and
`57972192e30fe52ab33b867c8fe4d171f59a7fd5`. Newer cached references were found
before finalizing the proposal. Source locations below use the proposal baseline.
This is source analysis, not a browser reproduction of the user's incident.

## 1. Consistent settings switches

Confirmed: `portal/internal/web/templates/session.html:85` and `:86` already
use native checkbox inputs with `role="switch"` for automatic retry settings.
Per-session notifications (`:93`), Keep open (`:102`), and Play sound in
`templates/notifications.html:33` still use ordinary checkboxes. The established
switch appearance is `.retry-policy-switch` in `static/style.css:280–288`.

Reuse that appearance and interaction for these persistent on/off preferences.
Give the reusable style a generic name or alias and update the existing retry
rows with it. Keep native `input[type=checkbox]` state/change behavior, add
`role="switch"`, retain stable IDs, and associate each label, help and status
with its control. Preserve keyboard Space, label clicking, visible focus,
checked/disabled appearance and a usable touch target. Avoid a second ARIA
checked state that can disagree with the native input. Support reduced motion
and ensure on/off remains distinguishable without color alone.

These are immediate-save controls. Preserve each existing endpoint and ownership
scope: session notification preference, browser sound preference, session hold,
and session-wide retry policy are different settings. Show saving/uncertain
feedback and the last confirmed value; disable the relevant control while its
write is pending. Preserve rereads, revision/identity checks and error recovery;
do not add automatic compensating writes. Retry policy already follows this
pattern in `static/app.js:2761–2827`. Changing appearance does not change when
Keep open is saved or grant permission to change the actual session hold now.

Leave action buttons such as permission/subscription setup and test notification
as actions. Leave acknowledgements, destructive confirmations and creation-form
options outside this settings-only change. The existing Save behavior of the
model/reasoning dialog is also unchanged.

## 2. New output follows displayed content

Confirmed: `static/app.js:4705–4707` shows New output whenever the newest-page
update has any changed entry and the reader is not following. Rendering filters
entries separately at `:4516` and `:4555`. Filtering delegates through
`:324–336` to `codex-web/conversation/assets/conversation.js:76–99`.
Messages hides team traffic and other activity; errors remain visible in every
view. Hidden entries can therefore trigger the button. This explains the
reported behavior structurally, without proving which event triggered it live.

Filtering only the changed keys is insufficient. The current comparison also
includes fields a reader cannot see: `transcriptContent` at `app.js:4446` removes
only timestamps before stringifying the remaining object. Collapsed details,
receipt fields, internal metadata, or raw text superseded by `displayText` can
change without changing the displayed message.

Use the rendered-content projection for the active filter and disclosure state
as the notification criterion. Compare stable entry keys and the fields that
actually determine the visible body, summary/status, questions, attachments and
labels. Exclude transport/receipt metadata, timestamp enrichment, hidden entries
and the body of closed disclosures. A closed disclosure's changed visible
summary still counts. Reuse the rendering decisions so the notification rule
does not drift into a separate approximation of filtering.

Maintain a small unread flag with each existing per-filter view state, rather
than deriving the button from only the last update. A visible content change
while paused sets it. A hidden-only or identical update neither sets nor clears
it. Streaming additions to an already rendered visible message count; repeated
snapshots and timestamp-only changes do not. Following the tail or selecting
New output clears the selected view after showing its latest content. Preserve
the current scroll anchoring and disclosure behavior.

On filter changes, show that view's state and clear it only if that view is
actually brought to its tail. Do not unconditionally clear unread merely for
switching filters (`app.js:4644` currently does). First load, thread replacement,
older-page insertion and historical gap repair establish history, not new-output
notifications. A repair that refreshes an already known streaming item needs a
case distinguishing a new visible final update from newly loaded old history.
Hidden tabs/sections must not acknowledge content solely because a poll ran;
returning to a following view can clear after restoring its tail.

This remains a local follow-tail indicator. It does not change session attention,
Web Push, acknowledgements, persisted transcript entries or server filtering.
It does not introduce a per-message read-receipt system.

## 3. Responsive submission with existing delivery semantics

Confirmed blocker at `static/app.js:4315–4316`: both Send/Steer and Queue next
are disabled by the global `messageDispatchInFlight` flag. `submitMessage` also
returns for that flag at `:5488`. Ordinary Send already saves and detaches the
draft before HTTP (`:5538–5557`), allowing typing and new uploads. Queue next
still locks all form controls (`:5499–5501`) until its request settles. The
existing behavior is documented in `docs/workspace-portal.md:437–454`.

Recommendation: separate capturing a submission from delivering it. On each
explicit submit, validate and save an immutable message/attachment snapshot with
its existing durable attempt ID, detach that draft, show its delivery state and
immediately allow the next draft and submission. Retain generation checks so a
late response never clears, replaces or focuses a newer draft. Extend the same
ownership transfer to Queue next.

Use a small ordered browser dispatch buffer, with one active HTTP mutation per
conversation. It feeds the existing endpoints:

| User action | Existing delivery contract |
| --- | --- |
| Send / Steer now | `/message`; server starts an idle turn or steers the active turn |
| Queue next | `/queue`; native `thread/queue/add` preserves queued work for later execution |

Preserve the chosen action; do not silently turn Steer now into Queue next.
Label locally waiting submissions distinctly from server-accepted queued work.
Once the preceding operation is accepted, dispatch the next without waiting for
model completion. Preserve FIFO dispatch for this browser's accepted submission
sequence. Native queued work retains its existing FIFO and head-only Start
rules. This does not promise one execution order across steers, queued turns,
other tabs, terminal input, team assignments and automatic retries.

The server already serializes conversation mutations
(`codex-web/conversation/handler.go:326`, `conversation/mutation_lock.go`) and
Send/Queue share a per-thread lock (`codex/client.go:4528`, `:5104`). Send reads
the active turn and supplies `expectedTurnId` for `turn/steer`. Distinct accepted
sends may steer the same turn; simultaneous native steer RPCs are not issued by
this client. These locks do not establish browser click-order FIFO for multiple
concurrent HTTP requests. Keep ordered dispatch instead of merely removing the
button guard.

Multiple browser submissions may wait safely in the proposed buffer; native
behavior for several steers pending consumption has not been established here.
Existing native FIFO recovery coverage is present in
`codex/recovery_integration_test.go` and queue/receipt contracts in
`codex/client_test.go`. Native steering order and the turn-ending race remain
implementation verification cases. Preserve today's server decision at dispatch:
`/message` can start a new turn if the former active turn has ended. A requirement
to steer only the originally displayed turn would be a separate API change.

Keep retry identities and original text/attachments through response loss.
Pause automatic draining on an uncertain outcome and reconcile that exact ID;
never retry it as a fresh message or let later submissions silently overtake it.
Definite validation failures retain an editable failed entry; later dispatch
needs an explicit retry or discard of the definitely unsent entry. Dismissing
an uncertain receipt is not proof it was unsent. Existing accepted/observed
evidence must win over a late HTTP failure. Intentional identical messages after
acceptance remain distinct; double-submit and retries of unresolved snapshots
must not duplicate them.

Reuse the existing multi-attempt storage, receipt and upload machinery. Retain
ordered pending intent across reload without automatically resubmitting unknown
attempts. The exact small storage representation and explicit resume behavior
need implementation design/testing: older browser recovery must not mistake a
locally waiting, never-dispatched entry for native acceptance. Storage failure
must leave the draft intact. Bound the local buffer and give an inline error if
it cannot accept another entry. Preserve conversation/member identity and current
authorization, lifecycle holds and retry-policy arbitration at actual dispatch.

## Implementation packages and dependencies

No assignments are made by this proposal. If accepted, the lead can split work:

| Package | File boundary and acceptance |
| --- | --- |
| Settings switches | `dev-workspace/portal/internal/web/templates/{session,notifications}.html`, `static/style.css`, relevant settings presentation/browser tests. Existing switch appearance, semantics, accessible interaction and save/error behavior preserved. |
| Visible unread | `static/app.js` transcript helpers/render/view sections, `paging_browser_test.cjs`, `presentation_browser_test.cjs`, `browser_contract_test.cjs`. Visible changes set per-view unread; hidden changes do not; scroll/filter/streaming cases pass. |
| Composer dispatch | `static/app.js` submission, receipt and action-state sections; delivery browser tests and relevant HTTP/native tests. Repeated submissions accepted without draft loss; existing send/queue/retry semantics preserved. |

The latter two packages overlap `app.js`; serialize their edits/integration or
have one implementer own that file. Settings can proceed independently with
agreed CSS/markup boundaries. Add concise behavior notes to the owning portal
guide once implemented. A shared `codex-web` helper or protocol modification is
not required by the proposal; any need discovered during implementation goes
back through the lead before expanding repository scope.

## Compatibility, deployment and recovery

Switches and unread tracking are browser presentation changes. Preserve HTTP
payloads, session manifests, retry ledgers, native queue format, lifecycle
journals, role policy and authorization. No database migration, generated client,
CLI, Terraform or NixOS/vpsAdminOS configuration change is proposed.

The browser dispatch metadata is the one new persistence concern: version it
separately or extend only a proven compatible record, preserving existing
attempt IDs and recovery meanings. Test old browser/new server and reload with
pending submissions. No coordinated fleet update is expected. A later rollout
would use the normal user-profile workspace application package and matching
assets, not system pin deployment. Package selection is forward-only here;
recover with a compatible forward fix while retaining all pending receipts.
Do not discard an uncertain submission or local pending buffer during recovery.
No deployment is prepared or authorized in this investigation.

## Acceptance and verification plan

No checks were run: this turn is a proposal based on source inspection. For later
implementation, use the repository Nix environment and these focused cases:

- All persistent boolean settings in the Session Settings view use the same
  switch. Tab/Space, label click, screen-reader name/state, disabled/loading,
  save failure, stale identity/revision and refresh preserve existing behavior.
- Messages-only plus hidden tool/team changes: no badge. Existing visible unread
  plus another hidden change: badge stays. Visible streaming text: badge appears
  when paused, never pulls the reader away. Timestamp/receipt-only and closed
  details changes do not signal new content; visible summary changes do.
- Switching filters preserves each paused view; following/clicking the button
  clears after reaching the tail. Initial/older/repair pages, reconnect, section
  hiding and lead/member replacement do not manufacture or erase unread output.
- Delay the first POST; submit two more distinct messages and Queue next. Every
  draft detaches once, buttons accept new intent, dispatch is ordered, and each
  action uses its original endpoint/ID/attachments. Late success/failure cannot
  modify a newer draft. Test repeated identical intentional text separately from
  double-click and retry deduplication.
- Lose the first reply, reload while entries wait, exhaust browser storage and
  reject an upload. Preserve records and stop uncertain dispatch. Reconciliation
  neither duplicates nor reorders; explicit recovery uses the original IDs.
- Verify sequential steers before model consumption, active-to-idle transition,
  existing native queue FIFO, two browser tabs and automatic retry arbitration
  against the selected native package. Do not infer these from mocked success.

Quick checks after implementation: Node syntax and focused existing browser
contracts; relevant Go web/handler/receipt tests using `-mod=readonly` as required
by dev-workspace. Longer checks after normal independent final review: packaged
flake checks and disposable native/browser delivery tests with delayed and lost
replies. Delegate long or uncertain verification through the monitoring skill.
Review and implementation are future work, not requested by this proposal.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-workspace-session-ui/>
