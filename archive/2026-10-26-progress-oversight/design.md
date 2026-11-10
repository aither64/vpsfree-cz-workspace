# Progress observer design and verification brief

## Responsibilities and interfaces

The generic runtime recognizes a ready read-only general-purpose member whose
role is observer. Adding that member opts a retained/Solo session in; new site
multi-member presets include it. Removal stops scheduling. Retained models,
efforts and instructions remain authoritative. No new catalog schema is needed.

A portal background worker visits eligible sessions once per minute. It admits
at most one check per session every 15 minutes, only during current active non-observer root/team
work; observer turns and observer-triggered idle lead acknowledgments do not
count as work. Active development, including long tests, remains observable.
Lifecycle/recovery/creation exclusions use existing runtime admission. Missing
observer, fully idle work and human-input waits do not start inference. Recent
activity in a now-idle session never permits a model call.

Each check has a stable submission ID, exact retained member/thread identity,
bounded prompt and three-minute deadline. Save its pending submission before
sending; reuse normal client-correlated submission recovery after restart. Scheduled
checks use a dedicated runtime send boundary without automatic-retry admission;
owned manual retry work defers a check and preserves its original identity/deadline;
manual member assignments retain normal retry behavior.
Read only the latest transcript pages, the beginning of plan/state and compact
previous concern/disposition. Do not persist the complete transcript. Save
progress state in a separate private per-root record; do not change roster,
lifecycle or submission schemas. An uncertain send never permits a fresh ID.

The observer returns JSON with status on_track or concern; concerns contain a
stable key, summary and recommendation, at most 150 words combined. No tools,
application edits, approval, reassignment, test cancellation or required-check
waiver. The role remains distinct from independent final review. Pending settlement and its exact-turn deadline run before unrelated development
evidence reads. A retained removed/archived observer record retires old pending
ownership; replacement members never inherit it. The worker
accepts only completed output belonging to the scheduled turn. It may interrupt
only its own exact scheduled observer turn when the deadline expires.

A first concern sends one normal same-session challenge to lead. Identical
continuations do not repeatedly wake lead; two consecutive completed concerning
checks show a portal warning. A completed on_track check resolves it. Failed or
missing observations preserve concerns and display unavailable status. Lead
records a concise decision in its normal update using
`Progress response <key>: <decision and reason>`; the next observation captures
it for the portal. Acknowledgment does not resolve a concern by itself.

GET/POST /api/sessions/<slug>/progress exposes status and pause/resume through a
Team-tab switch. Existing Team add/remove controls opt members in/out. Reuse the
portal's origin protection and ordinary session mutation admission. The visible
warning is also shown on the Codex tab, so it does not require opening Team.

## Invariants, compatibility and recovery

Observer failures never block development or lifecycle operations. Bounded
admission holds existing shared session locks only during individual steps;
there is no 15-minute wait under a lock. No machine/repository claim is needed.
Pending delivery and notice IDs survive portal restart. Missing optional state
is normal; older packages ignore the private progress record. No database,
Codex-native or catalog migration and no system update is needed. Site profile
selection must use the new runtime before defaults activate; previous rosters
and unrelated sessions are not modified. No live activation is authorized.

## Verification and documentation

Quick checks: fake-clock state/scheduling and result validation; bounded packet
and transcript filtering; concern recurrence/response/quiet-success; pending
restart and exact timeout ownership; API pause/resume and session isolation;
portal rendering/interaction; Nix catalog/capacity policy and existing relevant
Go/Ruby/browser checks. Tests use disposable roots and stub model delivery.
Complete quick checks and committed deliverables before independent whole-branch
review. Then run the broader affected packaged suite and a disposable scheduler
pilot through a fresh site-policy watcher. Do not invoke real model inference or
modify the live selected package as a test. Record concise evidence only.

Runtime session/portal guides own behavior, limits and recovery. Workspace
instructions own batch stopping criteria and the normal-index-metadata rule.


## Follow-up: cold observers and session settings

Live investigation found all four user-selected observers ready/enabled but
absent from recovery active_threads. The scheduler returns before recording
cadence because it requires recoveryHeld(observer)==false. The existing
SendProgressCheck/sendWithRecovery boundary already durably queues then activates
cold recipients, preserving submission identity and recovery permission. Remove
that premature observer-only gate; retain root/session admission and activity
checks. Test with actual RecoverSessions=true and cold member permission, plus
native cold progress dispatch. Do not hand-edit recovery records or send manual
work to the four sessions as a workaround.

User additionally requests moving Progress checks from Team to Settings,
per-session cadence and a Check now button. Keep the member in Team. Store
optional intervalMinutes in progress state (absent/zero means 15); accept whole
minutes 1..1440, bounded by the worker's one-minute visit cadence. GET exposes
the effective value; POST can update enabled and/or intervalMinutes, or request
checkNow alone (the user explicitly requested a Check now button). Reject invalid/ambiguous requests. No lifecycle/roster schema or
Codex version change. Old packages ignore the new optional field; rollback uses
the old 15-minute behavior and may drop the custom interval when rewriting
progress state. No irreversible state conversion is involved.

Check now explicitly requests one observation and may run while idle or paused;
it never unpauses automatic scheduling. Reuse normal admission, ownership,
manual-work deferral, stable pending IDs and deadlines. Automatic scheduling
still requires active development. Check now refuses another pending check or
an active manual observer turn. Quiet/concern settlement remains shared; results
may update the portal while idle, but never wake an idle lead. Unknown dispatch
is observed without automatically repeating the manual request.

Use existing settings panel, number input and button styles. Keep the recurring
concern banner above Codex. Runtime guides own the controls and scheduling
semantics; site team docs link there and state Settings for pause/configuration.
No KB publication is involved.

Acceptance: each of the four ready observers can be scheduled without an earlier
manual assignment; auto idle/human-wait gates hold; old state defaults15;
per-session intervals persist and isolate; Check now submits once and remains
paused/idle afterward; duplicate/pending/manual work is protected; controls appear
only under Settings. Quick regression batch should take under one minute; one
composed build after independent review is sufficient. No system VM rerun is
needed for unchanged host/lifecycle behavior. Deployment uses normal owned
profile switch with matching consumer pins and unchanged native executable.
