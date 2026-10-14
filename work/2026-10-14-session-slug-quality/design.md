# Session slug quality and recovery

The parent owns this bounded design and application implementation. The public
change is an additive `canSetName` preparation status and POST
`/api/session-creations/<request-id>/name` with receiptId, attempt and name.
The mutation uses the existing origin/profile/transition guards and upload plus
operation locks. It accepts failed/paused automatic-name requests with no slug
or handoff and no selected base except a previously chosen manual base. It
validates custom syntax, advances the attempt, durably saves Base with outcome
custom, and dispatches continuation. It never changes the frozen input/digest.
Stale offers conflict, active/terminal/reserved requests refuse, and retries
retain selected results. A custom collision stops and permits another selection.

Naming failures retain their existing outcome codes in failed/stopped records
with empty Base/Slug/Handoff. Failure does not create session state or release
accepted uploads. Cancellation/shutdown leaves normal startup pause behavior.
Naming remains isolated from ordinary session sockets and team/model policy.

The creation UI exposes retry naming and manual selection only from confirmed
status, keeps controls disabled during mutations, refreshes after conflicts,
and preserves an uncertain manual selection payload for identical recovery.
Redirect remains conditional on the original request/receipt and ready slug.

Schemas stay at version 1. Prior readers can load new records; prior writers
retain their old naming policy. Frozen legacy fallback names remain unchanged.
Automatic collisions keep suffixing; custom selections use exact-name collision
behavior. No database migrations, host state conversions or coordinated node
upgrade is involved. System pin and application composition match the same
reviewed runtime revision. Activation is system then user profile through the
existing coordinator; interrupted selection recovers forward.

Acceptance covers valid two-word/model names, invalid/error/timeout preservation,
manual-name recovery including collision and lost response, request replay,
stale/concurrent mutations, restart and existing records. Quick Go/browser
checks and syntax precede committed final review. Package and pinned native
runtime checks follow review using fresh watcher policy. Live naming on the
supplied notifications request plus varied requests must be descriptive and
respect bounds. Deployment acceptance precedes the approved master merges.
