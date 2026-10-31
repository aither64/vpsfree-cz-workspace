# Portal restart recovery design

Main agent owns design and application edits; this shell-only initiative has no
retained team. The user approved the preceding plan and explicit held-work
semantics. Substantive design uses xhigh reasoning.

## Scope and interfaces

The durable generic runtime owns recovery intent under private user state,
scoped by registered workspace, slug and exact retained root. The session helper
owns terminal reconstruction and authority publication under existing creation,
lifecycle and package-generation locks. The portal owns bounded startup
reconciliation and separate asynchronous Resume and Continue receipts.

Resume recreates runtime only. Continue explicitly activates retained work.
Send accepts a stable message receipt and queues the message before loading the
thread. Cold metadata/history and native queue/goal reads are permitted; native
thread/resume, event subscriptions and fallback settings reads are prohibited
until explicit action. Recovery status is stopped, recovering, waiting, active
or failed. Browser state refresh preserves the current draft.

## Invariants

- Reuse exact saved root and retained members; never create replacement threads.
- Session/runtime readiness does not imply permission to execute native work.
- Automatic restoration never loads native threads, replays requests, drains
  queues or resumes goals. Members remain held until explicitly addressed.
- A portal-only restart retains loaded execution without interrupt or replay.
- Cold Send records a stable queue item before activation, preserving existing
  order. Continue adds a visible prompt only when no queue or active goal exists.
- Exact authority and retained-state proofs remain mandatory. Ambiguous identity,
  wrong workspace, lifecycle reservations and package supersession fail closed.
- Independent failures do not prevent other sessions from recovering. Transient
  transport errors retry; identity and lifecycle failures require operator action.

## Compatibility and recovery

Keep ordinary manifest, authority and destructive lifecycle journal schemas.
Use an atomic, private, separately versioned sidecar. New start enables automatic
restoration, explicit stop disables it, archive/delete retire it. Upgrade seeds
only sessions with exact live terminal and authority proof. Stopped sessions
remain stopped. Avoid interpreting mere tracking presence as restoration intent.

Publish the recovery-state capability in the runtime package contract. Existing
holds must survive transition quiescing and terminal reconstruction; refuse a
target lacking the capability while recovery state requires it. Preserve
forward recovery and normal generation locks. No native Codex patch is planned:
the selected app-server invocation is not a managed-daemon and cold reads are
already available, while native resume can execute both queues and goals.

## Deployment

Publish exact feature commits and compose codex-web into dev-workspace. Select
one exact runtime commit through the workspace's existing nested runtime input
and configuration's confctl channel. Preserve the extension and unrelated locks.
Check both effective graphs before host build/dry activation/switch and user
profile switch. Do not reboot aitherdev, erase its runtime directory or mutate
other sessions during validation. Exact rollout evidence belongs in rollout.md.

## Acceptance and checks

Quick checks exercise exact durable identity, automatic versus manual intent,
held root/member gates, async receipts and lost-response retries, cold queue
ordering, Continue queue/goal/prompt selection, status transitions and browser
draft retention. Commit all intended changes and inventory complete series and
any state migrations before independent final review.

After review, the utility watcher owns long complete tests and builds. Native
fixtures use the selected app-server with a local mock provider: destroy only
their disposable runtime state, restart services, read history and poll status,
and prove zero inference with saved queue and goal. Explicit Send/Continue must
activate the same root once and preserve receipts/order/history. Cover retained
members, restart of only portal, stopped/archive/delete exclusions, lifecycle
reservations, transient transport retry and identity failures. Disposable VM
boot tests check lingering and service ordering without rebooting aitherdev.

The main agent accepts results, diagnoses failures, owns deployment and verifies
service health plus an owned smoke fixture. Keep branches unmerged until the
user explicitly directs integration into named repositories and targets.

## Review remediation contracts

The reusable client gates implicit subscription resume through a caller callback
on every connection generation, covering retained browser and observer watches.
The workspace supplies filesystem-only exact root/socket/permission proof. Native
activation remains explicit. Generation-pinned RPC prevents a watch from moving
to a different connection after its permission check.

The reusable ledger owner distinguishes known exact native queue receipts from
resolved execution. Observation uses the known proof; retirement keeps the strict
started-history proof plus existing idle/empty queue checks. A prepared send
delegated to the same queue identity retains its options and context in schema 3.
No new ledger state or migration is introduced. Queue deletion retires both
correlated records, and discard refuses a prepared send with a queue attempt.

Typed connection/deadline errors become transport_unavailable observations or
helper exit status 75. Canonical identity/lifecycle refusals remain permanent
until explicit Retry. Continue decisions survive failed activation retries and
are cleared by successful root activation, stop or a new socket cycle. Held
wrappers retain attachment-aware deletion completion. UI recovery controls
require retained-ready creation/receipt proof independently of live authority.

Cold Send first reconciles its exact prior send receipt, including a hot send
whose browser response was lost before native restart. An accepted or submitting
attempt must never become a new queue entry. The provider checks that boundary
in the same ledger transaction that reserves the queue attempt; an exact
nonsteered prepared send may still delegate to the queue. Existing application
mutation locks remain authoritative for operation serialization. Retry returns
the original receipt without releasing held work; unknown outcomes fail closed.
Focused tests cover accepted, submitting and delegated prepared attempts plus
portal and team cold-boundary retries.

Transport classification must survive the entire retained-set proof, including
loaded-thread discovery and repeated root/member materialization reads. Read
errors retain their type before separate identity comparison. Native identity
refusals still fail permanently; failed observation remains unknown and never
grants runtime readiness.

## Duplicate artifact follow-up design and verification brief

Owner: main agent; shell-only initiative has no native roster. Scope is the
generic runtime manifest validators and artifact catalog plus consumer pins.
Artifact paths identify files, so repeated normalized paths are valid. Every
raw declaration is validated; only presentation/access catalogs deduplicate,
keeping the first label and original path/order. Parsed manifest arrays and raw
files remain intact, protecting journal projections and digest comparisons.
Ruby's load/write validation follows the same acceptance rule without mutating
the supplied mapping. Existing atomic saves still validate before writing.

Interfaces retain existing manifest schemas and API shapes. No migration. Older
readers reject duplicates as before; updated selected-package dispatch handles
all supported clients. Existing recovery/live-switch contracts and native
0.160.0 remain unchanged. Rollout requires matching runtime pins, normal guarded
configuration switch and stable user-profile live switch. Recover forward under
the existing policy; preserve original source/rollout evidence.

Acceptance: the unchanged affected manifest validates and its portal page loads;
future duplicates added while open preserve access to the exact conversation and
show one artifact. No user warning or cleanup. Negative checks still reject
unsafe or malformed entries even following an otherwise valid duplicate.
Quick checks: Go session/web duplicate regression, Ruby shared fixtures/load
readiness/atomic-save validation, syntax/format/diff checks. Longer checks: full
packaged Go/Ruby and composed package, affected browser fixture, exact final CI,
aitherdev configuration build. Independent all-lane review precedes long checks.
Post-deployment: boot ID and native/tmux PIDs unchanged, services/health/owned and
affected pages return success, affected manifest bytes remain unchanged.
