# Archive preparation design and verification brief

## Accepted behavior

The portal accepts one explicit Archive intent, checks readiness before agent
shutdown, asks the retained lead to repair local blockers, rechecks, and only
then invokes the existing journaled archiver. The browser need not remain open.
Three completed repair rounds without measurable progress stop automation.
Preflight cannot guarantee later I/O success; destructive-phase failures retain
their original recovery command and identity. Automatic archival is unchanged.

## Boundaries and interfaces

Add `dev-session archive-check SLUG --as-is --json`, with structured readiness,
stable blocker codes/paths and stage progress. Share non-mutating checks with
explicit archive; run before quiescing. Keep active owned turns permissible.
Never publish journals, pause goals, capture queues, stop agents, fetch refs or
change tracking from this command. Final archive validates again under locks.

Private preparation records bind workspace, slug, original confirmation target,
retained root, operation ID and native delivery receipts. The portal background
worker persists its transition before external calls and reconciles exact
submission IDs after interruption. Use existing saved lead model/effort and
policy. An uncertain send cannot become a fresh send. Completion comes from
observing the accepted turn, not parsing a textual claim of success.

No lifecycle/transition lock remains held while the lead works. Preparation must
not enter the host's unfinished-lifecycle inventory. Cancellation revokes future
sends/archive continuation, and stale target/generation fails closed. Ordinary
user queues remain unchanged until the actual archive command owns shutdown.

Repair instructions authorize only session-owned local cleanup. They cannot
authorize shared infrastructure deployment, Git history rewrites, ownership
invention or edits to archive journals/receipts. Missing/unavailable lead or an
operator-only blocker leaves an actionable failure with no global reservation.

## Persistence and compatibility

Do not change accepted archive/revival journal schemas. New preparation data
lives separately from strict legacy lifecycle receipt schemas. Reconcile original
receipt and target before resuming; unrelated/stale records cannot launch work.
Package shutdown parks preparation into an old-readable retryable receipt before
it exits. Older packages can ignore private preparation; a later capable package
must prove the original receipt is still current before continuing.

## Acceptance and verification

First complete the existing HaveAPI archive without changing retained branches.
Cover loose/read-only gem caches, multiple blockers, wrong repository/symlinks,
active agents not stopped by failure, progress/no-progress, missing lead, lost
delivery response, portal restart, cancellation, stale identity, and unrelated
operations during repair. Existing journal retries bypass preparation. Quick
Ruby/Go/browser checks precede committed final independent review. Packaged
archive-lifecycle integration and disposable live acceptance follow review.

## Documentation

The runtime's session and archive guides own supported behavior and recovery.
This initiative owns one-time recovery and verification evidence. Keep hook
dependencies inside ignored checkout-local paths such as `.gems`.
