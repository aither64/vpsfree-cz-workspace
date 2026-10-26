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
