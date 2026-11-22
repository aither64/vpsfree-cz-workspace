# Team UI findings on selected 25b

Read-only source diagnosis by implementer1, 2026-11-20. Basis: selected
`25b679656bbd63d8e13406f0e2bcaec45bfa1d89`, immutable source
`/nix/store/wf6yazj31l9bh9lzzlzl5qxv3ms13hf0-source` (wf6).
The supplied screenshot was inspected; it shows the static-dash rendering below.
No screenshot identities, peer records, logs, transcripts or envelopes are retained here.
No application edits, tests, builds, native sends or live probes were performed.

## Concrete roots

1. **Team statistics are disconnected for Pi in three places.**
   `portal/internal/web/pi_workflows.go:1139–1163` constructs the actual Pi
   `TeamView` without setting any row's `Stats` field. The fallback Pi projection
   in `team_view.go:20–38` does the same. Thus shared
   `templates/session.html:380–381` emits seven literal dashes instead of metric
   cells. Independently, `static/app.js:4691–4694` refuses Team polling unless
   `codexBackend`, and `team_stats.go:20–96` enumerates the Codex roster/thread
   identifiers and legacy `codex.ActivitySnapshot`. Enabling the cells alone
   cannot repair the data path. Roster `ready` is not activity or coverage.

2. **Pi already has the needed activity operation.**
   `piruntime/activity.go:53–95` reads existing-worker `activity_v1` into shared
   `conversation/backend.ActivitySnapshot`; unsupported contracts remain absent.
   `web/pi_workflows.go:1240–1379,1559–1568` exposes it through ordinary typed
   Pi resolution/admission, exact identity, scope, generation and profile checks.
   `pi_activity_test.go:33` already proves admitted HTTP activity uses one read
   binding without a transcript read and refuses stale scope. The Team omission
   does not establish that live native data are missing. No Pi extension is
   required to connect these existing observations to Team.

3. **Idle wait display uses browser-read age instead of the native state anchor.**
   `pi-runtime/src/activity.mjs:3–11,38–43,61–76` preserves `stateSinceMs` across
   reads and provides `observedAtMs`; idle `openWaitingMs` is always zero.
   Shared `static/app.js:768–769` computes open wait from `openWaitingMs` plus
   the browser clock's elapsed-since-read. `createTimingClock.received()` at
   895 resets that extension on every successful read (5117), so fresh polls,
   focus/resume and reload show zero again. Section selection itself only
   toggles panels (3454–3463); source does not prove each section click directly
   resets a clock. Codex's producer supplies an already accumulated idle
   `openWaitingMs` (`codex-web` pinned b302, `codex/activity_snapshot.go:220–226`),
   which masks the shared consumer assumption. Use a defined observed state
   duration, bounded by freshness; never infer historical idle from session age.

4. **Two Pi activity fields also disagree with the existing common consumer.**
   `activity.mjs:20–26,66–67` counts user prompts as `sentMessages` and assistant
   messages as `receivedMessages`. The common Team contract is the reverse:
   assistant replies/plans sent, user prompts received (`docs/workspace-portal.md:2039`,
   pinned b302 `codex/turn_history.go:112–116`). Also Pi `waitingMs` already
   includes its open interval (63–71), while common `activityPresentation`
   adds `openWaitingMs` again (app.js:766). Ten seconds of one open retry wait
   projects as twenty. Pin down these adapter semantics before exposing totals;
   do not hide the mismatch by renaming columns per backend.

5. **Repository empty copy is a literal backend name.**
   `portal/internal/web/templates/details.html:47` says “Codex has not added any
   repository worktrees yet.” The template is shared by both backends. A neutral
   empty-state sentence needs no runtime/interface change.

## Smallest implementation boundary for architect/lead

Reuse the existing Team row, metric cells, poller and shared activity snapshot.
Connect Pi roster members to admitted read-only activity through the existing
resolver; retain per-member unknown/unsupported results and current tuple/scope
checks. Do not Load/Create/Send to obtain metrics, fall back to Codex, or add a
parallel observer/metrics subsystem. `team_stats.go`, Pi row projection in
`pi_workflows.go`/`team_view.go`, and `static/app.js` own that gap. Exact file
allocation remains the design owner's decision. `pi-runtime/src/activity.mjs`
owns the field semantic discrepancies; the design must choose an explicitly
compatible projection/worker correction rather than assume a worker deployment.
`templates/details.html` owns only the copy change.

Keep partial timing truthful: Pi's monotonic totals cover the current worker
attachment, not full historical lifetime (`docs/pi-runtime.md:39–52`); its
`coverageComplete=false` and reason must remain visible. Counts come from the
retained branch. A never-started member stays “Awaiting first assignment” with
unknown metrics, distinct from a populated member whose observation failed.
Observed zero is a value; absent data are unavailable, not zero. Existing stale
and last-good display behavior must not turn into fresh activity claims.

## Focused acceptance proposal (UNRUN)

- Extend the existing admitted Pi activity/Team fixtures and common browser
  controls: populated lead/member plus a never-started member; exact asymmetric
  sent/received counts, distinct tools, working/waiting/idle values, partial
  label, and one unsupported/failed row. Retain stale-scope refusal and no
  transcript/load/send effect. Reuse Codex controls for the shared consumer.
- Fix an idle observation at 120 seconds with an unchanged native state anchor;
  poll, switch session sections, hide/show the browser tab, and reload. Fresh
  observations retain/advance the interval; stale observations stop extending
  and show unavailable. A real state transition resets it. Include one open
  retry wait so its elapsed time is counted once.
- Render an empty repository list under both backends with the same neutral
  copy. Use existing fixtures/browser harnesses, no new framework or live run.

Sending latency, delivery/queue state and cross-session classification/labels are
outside this package and remain with implementer0. Abstraction/SDK design remains
with architect0. Next action: accepted sufficient design and explicit source
allocation; no implementation or verification launched by these findings.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/
