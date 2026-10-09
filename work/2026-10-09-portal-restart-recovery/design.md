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
