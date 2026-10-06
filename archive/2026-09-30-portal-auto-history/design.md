# Automatic upward transcript history

Design and verification brief for `2026-09-30-portal-auto-history`, prepared by
`architect0` on 2026-09-30 before application implementation. The lead owns
scope decisions, tracking and acceptance; the implementer owns application
edits. Material deviations from this brief go through the lead.

## Scope and implementation boundary

Replace the normal **Load older** button with one older-page read when a fresh
upward user input reaches within 200 CSS pixels of the transcript top. Retain
100-item pages, the visible reading position, centered transient feedback and
an explicit **Retry** action. The same browser path serves lead conversations,
team-member conversations and archived sessions.

Only `dev-workspace` application files are in scope:

| File | Responsibility |
| --- | --- |
| `portal/internal/web/static/app.js` | Upward-input gate, existing scroll/follow integration, typed history retry state, feedback rendering |
| `portal/internal/web/templates/session.html` | Remove normal load button; preserve status and accessible retry control |
| `portal/internal/web/static/style.css` | Center feedback and keep its visibility changes from moving the reading anchor |
| `portal/internal/web/paging_browser_live_test.cjs` | Real input, request-count, failure and geometry coverage |
| `portal/internal/web/paging_browser_test.cjs` and `browser_contract_test.cjs` | Update affected contracts; add small state tests only if a helper warrants them |
| `docs/workspace-portal.md` | Current history navigation, feedback and retry contract |

Keep codex-web's `createTranscriptHistory` and `readTranscriptPage`, the current
page API and history-merging/repair algorithm. Do not add a dependency, alter
server pagination, add an observer that drains all history, or change lifecycle,
cluster, package-transition or persisted-state behavior. This brief makes no
application edits. The lead should register it as a portal artifact and link it
from state; lasting behavior belongs in the owning project's portal guide.

## Existing behavior and findings

The inspected feature base is
`d20bb64c45db1d803fc3b7a8c2956049860d72dd`. Relevant existing paths are:

- Transcript input handlers mark `transcriptUserScroll` for 800 ms and pause
  following on upward movement. That flag is a follow-tail heuristic, not a
  consumable authorization to read history.
- `runHistoryRead(kind)` serializes older and continuity-repair reads, uses a
  35-second `pageReads` deadline, and rejects stale thread/repair-version
  responses. `scheduleHistoryRepair` fills a bounded continuity gap separately
  from intentional navigation into older history.
- `patchTranscriptEntries` reuses keyed rows, captures the first visible row,
  and compensates its position after prepending. CSS disables native
  `overflow-anchor`, avoiding two competing anchor adjustments.
- The normal-flow history row appears above the transcript. Toggling this row
  changes viewport geometry before/after the prepend calculation.
- `renderThread(..., "newest")` currently clears every history error. The
  existing retry handler schedules repair or a newest refresh; it does not
  reliably repeat a failed older-page operation.

The last two observations require explicit handling; replacing the button with
a top-of-scroll check alone is insufficient.

## Input and state design

Use a small, page-local, one-shot history-input state separate from
`transcriptUserScroll`. Suggested fields are an input sequence/token, source,
scroll position at input, latest observed position, optional expiry, and a
pending animation-frame handle. Exact names are implementation choices.
Keep at most one pending token; never queue input credits.

Automatic older reads are eligible only when all of these hold:

- The transcript has rendered its initial page, is visible with nonzero
  viewport height, and the document/read scope is active.
- Paging helpers and `client.threadPage` are available; paging is not marked
  unavailable.
- `hasOlder` and `olderCursor` are present, there is no continuity gap, no
  retryable history failure, and no history read is running.
- A current upward user input qualifies, and normalized `scrollTop` is at most
  200 pixels. Treat a negative overscroll position as zero.

Inputs received while ineligible, especially while a read is running or an
error is displayed, do not create deferred work. Initial load, page completion,
repair completion and ordinary newest refresh never call the older-read gate
without a new user input.

| Input | Qualification |
| --- | --- |
| Wheel | Negative vertical delta over the transcript; ignore zero/downward movement and browser zoom gestures |
| Touch | A single-touch movement whose finger Y increases, using the previous touch position; touchstart alone only establishes a baseline |
| Keyboard | ArrowUp, PageUp, Home and Shift+Space when navigating the transcript; ignore editable/form controls and unrelated shortcuts |
| Scrollbar | Pointer-originated transcript navigation followed by an actual decrease in scrollTop; pointerdown alone is not upward intent |

Preserve native scrolling and existing follow-tail behavior. Do not prevent
default wheel/touch/key actions. Upward intent pauses follow-tail before the
read; a successful older read must not pull the reader to the newest output.

For directional inputs, check eligibility immediately when already near the
top. This covers a viewport at zero or too short to scroll, where no `scroll`
event will occur. Otherwise retain only that input's one-shot token so its
native scroll can cross the threshold. A post-input animation-frame check or
the corresponding `scroll` callback may consume it after the default action.
The deferred check must establish actual upward movement from the recorded
position; being near the top after an unrelated layout change is insufficient.
Expire unused intent within a short bounded window (the existing 800 ms input
window is an acceptable upper bound), clear it on opposite movement, and do
not rely on elapsed time alone to prevent repeats.

For scrollbar navigation, pointerdown starts observation and pointer movement
can renew its one-shot token. Only observed upward native scrolling qualifies.
Clear on pointerup/cancel, lost interaction or blur. Consuming one pointer token
must not leave an active held pointer able to reauthorize another read without
fresh pointer input. Verify native scrollbar event delivery in the actual
browsers; do not accept a test that only sets scrollTop as proof of dragging.

Consume the token synchronously before calling `runHistoryRead("older")`.
Clear pending intent when any history read starts. Clear/cancel it before
application-driven scrolling or layout updates: transcript patching, filter
changes, status geometry changes, follow/new-output actions, section restore,
resize-follow, thread replacement and document suspension/navigation. Resync
the scroll baseline after those updates. Deferred callbacks must compare their
captured token with the current one before acting. Keep callbacks safe during
initial handler registration; avoid a temporal-dead-zone dependency on a later
history function declaration.

The invariant is **at most one older-page request per fresh qualifying input**,
with no queued request after completion. Multiple wheel events, touch movements
or key repeats are separate inputs, but events while a request is in flight
are discarded. Native momentum or a restoration-generated scroll event without
new input cannot fetch another page. A short or filtered page that still leaves
the view at zero waits for another input instead of recursively loading.

## Reading-anchor invariant

For a retained visible message, preserve its DOM identity when its content is
unchanged, disclosure state, and viewport Y position across a history prepend.
Capture the visible anchor immediately before applying the response, so user
scrolling while the request is pending is respected. Preserve current fallback
behavior if the anchor disappears or there are no visible messages; never jump
to the oldest/newest message merely because a page was loaded.

Retain keyed patching and native-anchor suppression. Do not rerender the whole
transcript to prepend. Do not use a height-delta adjustment as the primary
anchor when a stable message row is available. Date boundaries and filters must
not replace a retained visible message unnecessarily.

Feedback geometry is part of this invariant. Prefer a status area whose
show/hide transition does not reflow the transcript (a locally positioned
status layer, or equivalent stable geometry). It must not obscure the reading
anchor or intercept ordinary scrolling. If the implementer keeps normal-flow
feedback, compensate its geometry changes and prove the same invariant,
including loading, failure and retry transitions; prepend compensation alone
does not cover them. The normal button stays absent, and normal idle history
has no visible status row. Keep the treatment local to the transcript UI.

The browser regression tolerance remains less than 8 CSS pixels for an
unchanged anchor. Assert during a held request and after settlement, not only
before/after a fast response. At a genuinely non-scrollable view, preserve
retained content and avoid a jump to tail; geometric clamping limits must be
handled without cascading reads.

## Loading, errors and retries

Retain `#history-status` as a polite status region, with centered feedback.
Loading text is `Loading earlier messages…`. Disable/hide actionable retry
while its read is active. The normal `#load-older` control and handler disappear.

Represent retryable history failure with the failed operation kind (`older` or
`repair`) and its thread/continuity identity, rather than inferring the operation
from the displayed string. Existing error text may remain. A generic failure
or timeout retains loaded messages and exposes centered **Retry**. No further
upward input or automatic repair timer retries while that failure remains.
Unrelated successful newest-page refreshes must not clear it.

Explicit retry clears the failure as part of starting one read. For an older
failure, use the current valid older cursor; for a repair failure, use the
current repair cursor. Do not persist or blindly reuse a cursor that has become
invalid. If a newer snapshot changes continuity, re-evaluate against current
history: a gap requires repair, a changed thread discards the old failure, and
history that is now fully satisfied needs no retry. Remove failure state only
when its operation succeeds or its identity is demonstrably superseded. A
successful unrelated newest page is not by itself such evidence.

Preserve the existing special recovery paths:

- Cursor-expired/reset-required responses retain messages, invalidate the
  cursor and request a fresh newest page with `History changed. Reconnecting…`.
  A successful reconciliation clears that transient recovery notice and can
  continue the existing bounded repair. It must not continue ordinary older
  browsing automatically.
- Explicit paging-unavailable responses retain the existing legacy fallback
  and unavailable message. Do not present an older-page retry that can never
  succeed in this state. Authorization failures remain errors, not fallback.
- A stale thread/version response or aborted read from page suspension is
  ignored under the current guards. Returning to the page does not reuse an
  old upward-input token.

Continuity repair may still read successive bounded pages to connect retained
and newest data, as it already does. The one-input rule governs browsing beyond
the retained history, not this existing repair algorithm. Repair and older reads
share the existing single-flight guard. A repair error remains stopped until
explicit retry, even if newest refreshes continue successfully.

## Compatibility, deployment and recovery

No on-disk format, database, migration, seed, API, cursor, generated client,
CLI, Terraform interface, service protocol or NixOS/vpsAdminOS option changes
are needed. Input and retry state are browser-memory-only. Old browsers retain
the existing page/full-thread endpoints; new browsers retain the documented
authorized legacy fallback against a server without paging support. There is
no required node coordination or data conversion.

Browser assets and server ship in the user-profile package. Prepare deployment
from the reviewed `dev-workspace` feature revision through the existing
aitherdev workspace-package workflow; preserve selected extensions/catalogs.
The lead owns the exact candidate build and rollout record. No configuration
master integration or feature/default-branch merge is authorized by this brief.
Keep the feature branch active until separate integration direction.

The current application permits forward-only package switches and rejects
`workspace-host rollback`. Recover a bad UI change by building and switching
to a newer package that reverts the browser behavior, using the normal package
transition preflights. Do not promise activation of an older generation. A
browser reload resets input/error state without losing transcript data. There
is no data/schema rollback or cleanup requirement introduced by this feature.
This corrects the initial plan's previous-generation rollback wording; the lead
must reconcile that wording before handoff.

## Acceptance and verification

The decisive evidence is browser behavior, with cursor reads counted separately
from newest-page reads. Use controlled responses and held requests, not sleeps
as the only indication that a request happened. Include at least three pages
so an accidental second fetch is detectable.

1. Initial load remains bounded at 100 items with no cursor read. No normal
   **Load older** button exists; idle status is hidden.
2. Programmatic movement to zero, filter restoration, resize, section reopen,
   newest refresh and prepend compensation cause zero older reads, including
   immediately after a consumed input while the follow-tail flag is still set.
3. Upward wheel navigation crossing 200 pixels causes one older read. Another
   upward input at zero also works when content cannot scroll. Downward/horizontal
   input and unrelated keyboard editing do not fetch.
4. Keyboard, touch and scrollbar navigation qualify correctly. Held requests
   plus repeated input prove single-flight behavior and no queued read after
   release. A later fresh upward input can fetch the next page.
5. Both a tall page and a page with no entries visible in the current filter
   stop after one read. Exhausted history never requests another page, including
   repeated upward inputs at zero.
6. An unchanged visible message remains the same DOM node and moves less than
   8 pixels through loading and success; user scrolling during a held response
   chooses the later visible anchor. Cover a date separator and retained
   disclosure/filter behavior with focused existing coverage where possible.
7. A failed older read retains entries and Retry through a successful newest
   refresh. More upward input causes no retry. Clicking Retry repeats one valid
   older operation and can succeed. A second failure remains actionable.
8. A failed continuity repair similarly survives newest refresh and retries
   repair. Cursor invalidation, unavailable paging and page suspension retain
   their special semantics and never trigger an ordinary older-page cascade.
9. Preserve independent request/queue/metadata refresh, newest streaming and
   follow/new-output behavior. No page errors or unhandled rejections occur.

### Quick checks before independent review

Use Nix-provided interpreters from the project's package environment or a
suitable Nix shell. This flake has no declared development shell. From the
feature worktree, run JavaScript syntax checks and existing paging contracts:

```sh
node --check portal/internal/web/static/app.js
node --check portal/internal/web/paging_browser_live_test.cjs
node portal/internal/web/paging_browser_test.cjs
git diff --check
```

Run the focused live regression through the actual server harness from
`portal/`, with Nix-provided Go/Node/Playwright modules and
`PLAYWRIGHT_BROWSERS_PATH` configured:

```sh
PORTAL_BROWSER_TEST=1 go test ./internal/web -run '^TestQuestionBrowser$/^paging_browser_live_test[.]cjs$' -count=1 -v
```

The lead must resolve the exact shell/module paths before execution. These
commands are a verification plan, not executed results. Use a fresh verification
watcher if the build/test duration is uncertain; quick checks that are known to
finish within a minute may stay inline. Have the main context owner apply the
user-facing writing guidance to final feedback/doc text before committing.

### Longer checks after mandatory review

After intended edits are committed and quick checks pass, give the independent
reviewer the complete base-to-head series and diff, explicitly recording that
there are no migrations or codex-web changes. Review the input-consumption and
failure-reset races, not only the happy-path scroll handler.

Through the required fresh Luna/low watcher, run the broader Go/browser suite
and package checks (`nix flake check --print-build-logs` as the repository
declares), and monitor feature CI as directed by the lead. Distinguish actual
Playwright execution from skipped Go browser tests: ordinary package checks
do not enable `PORTAL_BROWSER_TEST` automatically. Chromium provides automated
geometry evidence; verify Firefox and native touch/scrollbar behavior where
test automation differs, recording any outstanding device/browser coverage.

After the authorized candidate deployment, refresh a long lead conversation
and a member conversation, and check archived read-only history. Confirm one
page per fresh input, stable reading position, explicit failure recovery and
unchanged follow-tail/new-output behavior. Record the exact tested package
revision. Do not mark deployment, independent review or acceptance as complete
based solely on this design.

## Handoff concerns

- Lead reconciliation: replace the plan's omitted-architecture and old-package
  rollback statements with this assigned brief and forward recovery.
- Highest behavioral risks: stale upward intent, live newest refresh clearing
  failure state, and status-row reflow moving the anchor.
- Native scrollbar/touch input needs actual browser evidence; synthetic
  scrollTop assignments only prove the programmatic no-fetch case.
- No implementation tests, package builds, deployment, merge or session
  lifecycle actions were performed while writing this brief.
