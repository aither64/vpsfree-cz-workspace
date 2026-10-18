# Exact profile forward recovery

Ordinary reconcile cannot finish a preselection failure after profile_intent.
The original worker failed its creation guard before selection, with exact old
profile/token still present; the guard is now clear. The unknown receipt moves
the same reservation to blocked_recovery, which also rejects activate-prepared.

The source-only helper binds this owner, original attempt/approval/snapshot and
candidate, worker request/phase/error, already deployed system and predecessor
profile token. It retains every receipt, history entry, owner and execution
claim. Under the native store transaction it changes only this reservation's
recovery flag to held, then re-enters the installed activate-prepared command
under the exact original attempt. Normal lifecycle, source, generation, cluster,
registration and profile-token guards still apply. A worker lock excludes native
reconciliation throughout activation. The helper restores blocked_recovery on
activation failure, including after selection; retry recovers only the same
forward candidate. A durable owned recovery record precedes the state change.

After exact candidate selection and full activation, ordinary reconciliation
converts the original unknown history to applied and records deployed_review.
No ownership transfer/release, new job, changed candidate, phase rewind, receipt
forgery, foreign mutation, integration or reboot is authorized. Existing user
deployment/proceed directions cover the same exact candidate and attempt; this
helper needs independent final review before execution. Run --check first; it
performs no mutation. Review must assess whole branch/history and all four lanes
for this bounded high-risk operational recovery, including interruption/retry.

Code: workspace/docs/maintenance/recover-archive-profile-2026-10-16.rb. This is
one dated source-only recovery, not a new generic runtime capability. Runtime,
configuration and application builds remain the accepted exact sources. The
workspace branch gains only this operational source; deployed candidate remains
the original reviewed abdeefc4 composition. No migrations or format changes.

R6 correction: the activation child explicitly inherits the open worker-lock
descriptor across both command wrappers. TERM/INT cancellation is deferred
until the activation child ends; SIGKILL of the helper leaves the lock retained
by the active child. Disposable stubs verify that competing recovery and
reconciliation cannot acquire the lock after TERM or KILL, until activation
ends. Clean final capture is profile-forward-interruption-final.log; the earlier
fixture setup used a wrong relative path and two launches overlapped one log.
Both handles were collected; the overlapping capture is preserved separately.
No live mutation occurred during these checks.
