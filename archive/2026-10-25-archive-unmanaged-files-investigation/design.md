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

## Creation contention follow-up (authorized by the user)

The user explicitly requested root-cause investigation and fixes for the two
creation CI failures after the archive implementation. Keep the work in this
initiative and generic runtime branch. Do not merge or deploy without the existing
explicit direction.

The naming reservation currently takes a candidate's creation/runtime EX locks
before checking whether its tracking/receipt already makes the candidate occupied.
A normal portal conversation operation retains SH runtime access, so collision
handling can fail on its lock rather than choose the next automatic name. Add an
early occupancy rejection/skip using the existing reader; retain the authoritative
occupied/ownership checks under both locks before accepting an unused name.
Custom names remain exact and fail on collisions. Busy unproved names must never
be skipped or treated as owned solely because a lock file exists.

Plan initialization calls its exclusive source verifier without waiting and from
inside destination creation/provider admission. Normal source portal operations
hold SH runtime access. Keep the exclusive source proof, but wait before acquiring
destination/provider creation admission, as accepted forks already do. Revalidate
the exact source after acquiring EX; source replacement must still fail before
native creation/provider binding. Existing journal-bound recovery keeps its
ability to finish without consulting an obsolete source.

Acceptance: deterministic reproductions use a known portal conversation SH holder
and the same lock device/inode as the Go/Ruby contender. Exercise collision
selection, exact custom-name refusal, free destination locks while plan source
verification waits, exact receipt/attempt preservation, source replacement,
cancellation and existing journal recovery. Use the existing cross-process
creation fixture; native/provider/tmux effects may be counted stand-ins, but
actual Go admission, Ruby CLI, locks, journal and completion paths stay real.
Quick regressions and committed independent affected-lane review precede the
packaged creation/archive VM checks. No persisted format, migration or public API
change is intended. Document lock ordering and supported accepted-plan behavior
in the existing session/concurrency guidance.

## Authorized aitherdev rollout (2026-10-25)

User direction: "deploy aitherdev using vpsfree-cz-configuration". Deploy the
reviewed/published runtime b974f2f3f83792a494610d1ea03f3d69e97bc1a4 without
integrating any feature into master. Extend scope to initiative-owned configuration
and workspace-composition worktrees. Preserve shared master checkouts and all
unrelated files. Exact runtime selection uses configuration channel dev-workspace /
role devWorkspace and the workspace direct nested override; retain extension and
other inputs. Build final committed artifacts before ownership, then acquire
vpsfree:aitherdev and dry-activate/switch system before the ordinary workspace-host
profile switch with the held claim and exact session identity. Use the installed claims workflow and the current configuration site guide
docs/operations/codex-providers-aitherdev.md for ordinary confctl deployment.

Verify exact system/profile identities, contract, portal/router health,
conversation continuity and a disposable creation/archive acceptance. Use normal
forward profile recovery for interruptions, retain original journals, never
reboot or force release. Keep the machine claim while deployed feature lineage
remains unintegrated. No new database/state migrations are introduced by pinning.
Individual rollout evidence lives in rollout.md; source behavior remains in
runtime docs. Readers: operator continuing deployment/recovery and merge reviewer.

## Post-merge archive CI follow-up: worktree registration

Master CI 40229910427 failed only archive (job 121279205759); creation, fast and
host passed. Exact b974f2f3. Failure is worktree add immediately after native
session start: "another dev-session command is changing ...". Earlier archive
run at the exact same head passed. Do not rerun unexplained failures. Historical
holder PIDs are not present in the retained VM log; diagnostics also show a
portal shutdown timeout, recorded separately without assuming it caused this lock.

The worktree command intentionally rejects competing exclusive session writers;
Ruby test_worktree_mutations_use_the_slug_lock asserts this. A blind wait:true
would change that contract. Reproduce with an identified actual portal
queue/reconcile SH admission on the same device/inode, then scope the fix to
worktree-add: on EX/NB contention, a successful SH/NB probe identifies compatible
readers and permits waiting for EX. A failed SH probe keeps writer refusal.
Use the existing host-lock helper with one optional internal flag, passed only
from worktree-add via with_slug_lock. Keep all actual validation after EX, retain
existing provider/lifecycle/generation locks and refusal behavior, and introduce
no new lock file, state format, restart, global lease or generic retry loop.
Other commands retain their current behavior.

Quick acceptance: deterministic Go/Ruby boundary regression with real Git
worktree creation and identified Go SH holder; prove no mutation before release,
unrelated slug worktree registration remains usable, and writer EX still refuses.
Run focused Ruby worktree/lock tests and related Go tests. Record pre-fix failure.
Commit one forward-only fix (b974f2f3 is already merged), run applicable independent
review before the archive VM/CI. Reconcile exact tested source, downstream pins,
deployment need and approved integration scope after the fix is concrete.
No machine or repository claim is held for this work. Earlier three merges and
machine release remain complete. Initiative stays active until follow-up settled.

## Archive retry/status race follow-up

The failed packaged retry issued its fresh operation GET and journal/details GET,
but no POST. refreshArchiveCompletion rejects any replacement of the cached
operation object, including a background poll decoding the same receipt again.
Reproduce by holding the background operation response, beginning Retry's details
preflight, then releasing that same receipt before releasing details. Keep
cancellation on changed receipt, target, journal, operation state/options, and
page suspension. Allow an equivalent refreshed receipt to complete preflight;
diagnostic timestamps/text alone do not change retry authority. Use the existing
browser acceptance fixture, including a changed-receipt negative control. No
API, state format, deployment contract, or migration changes are intended.


## Portal startup cancellation during package transitions

Investigation found New synchronously acquires transition SH in preparation
reconciliation using an independent background operation context. SIGTERM only
cancels serve's stopContext; the HTTP shutdown path is installed after New returns.
Thus a portal blocked in startup cannot stop while a package switch retains EX.
Prove with actual serve subprocess, owned EX transition inode observed through
/proc child descriptors, SIGTERM while retaining EX, and failure Go stacks.

Add NewContext(ctx, config) for cancellable initialization, preserving New as a
background-context wrapper. Pass the startup context only to synchronous upload
retention and preparation reconciliation. Keep operational worker context
independent, so post-start shutdown still parks preparation before canceling
workers. Main passes its signal context, and treats cancellation from its own
stop signal as a clean exit. Existing operation semantics/formats stay unchanged.
Acceptance: real SIGTERM exits before lock release, no HTTP publication or
ownership change during the wait; cancellation after successful initialization
does not cancel workers; existing shutdown and package-transition tests pass.
One forward fix after merged history; pin streams must again contain one final
update. The current780 CI/build artifacts remain evidence for that exact source
only and will not be selected as the final release if this defect is confirmed.


## Recovery contention classification

Exact780 CI passed archive and fast but creation later showed a retained source
with a completed plan and recovery failure "another dev-session command is
changing". restoreRuntime invokes resume and treats only exit75/native transport
as transient. Ruby with_host_lock raises typed SessionBusyError, currently exits1,
so ordinary lock contention freezes recovery and disables plan controls.

Keep lock admission unchanged. Only resume translates SessionBusyError into its
existing TemporaryRecoveryError/exit75 contract. The portal's existing bounded
recovery/backoff can retry after either a reader or writer releases ownership.
Other commands retain existing busy semantics; identity/lifecycle refusal remains
permanent. No polling/retry framework, waiting lock or state/API format changes.
Regression uses real flock SH/EX holders and real resume readiness/authority
writers through the existing native/tmux fixture; verify no mutation/native call
while busy, then exact retained root recovery after release. Existing Go
recovery test verifies exit75 remains automatically eligible and exit1 does not.
