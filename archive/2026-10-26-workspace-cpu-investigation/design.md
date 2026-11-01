# Accepted implementation brief — 2026-10-26

**READY FOR IMPLEMENTATION.** This addendum supersedes proposal-only scope and
conflicting recommendations below. Historical measurements remain unchanged.
The lead relayed explicit user authorization for the three bounded optimizations,
meaningful regression tests, controlled benchmarking, aitherdev system deployment
through vpsfree-cz-configuration plus application profile deployment, verification,
then integration into dev-workspace/workspace/vpsfree-cz-configuration master and
machine release. No reboot, session cleanup or lifecycle termination is authorized.
The lead owns rollout, integration, resource claims and durable delivery records.

Session/env were reverified; shared feature worktree is
`worktrees/2026-10-26-workspace-cpu-investigation/dev-workspace`, starting at
`7e6d7c9cdb3388ab7abc720c034c15c21afbd686`, matching measured deployed source.
All four assigned implementers are retained ready workspace-write members.

## Owners, boundaries and dependencies

- **implementer0: coordinator.** Own `libexec/workspace-coordination*.rb` and
  narrowly required integration selectors, focused Ruby tests,
  `docs/coordination.md`, and the scheduling sentence in `docs/integration.md`.
  No new persistent state, scheduler framework or general Store read cache.
- **implementer1: settled retry gate.** Own `portal/internal/web/turn_retry.go`,
  dedicated retry helper/tests and existing retry-owning documentation.
  Avoid `server.go`; controller changes only if a small in-fence capture cannot
  be expressed through existing policy callbacks, with architect/lead consultation.
- **implementer2: coordination display cache.** Own `coordination.go`, dedicated
  cache/tests, minimal `server.go` wiring and actual lifecycle-success invalidation
  (including supervised success), and `docs/workspace-portal.md` cache paragraph.
- **implementer3: controlled benchmark and later delivery assembly.** Own a small
  opt-in fixture, separate benchmark-method documentation and entrypoint link
  after peers. Reuse actual stores/schedulers/status handlers and counting
  synthetic native Client/Backend; do not add a native wire daemon or profiler.
  Fixture feasibility comes before expansion. Package helpers needed by fixtures
  are coordinated with their owners. Lead serializes Git and shared-file edits.

Packages 0, 1 and 2 may begin independently now. Benchmark consumes their narrow
interfaces and can prepare its disposable fixtures in parallel. Broad healthy
recovery sharing, catalog/roster refactoring, cross-session status projection and
MCP consolidation are outside this implementation. Preserve existing intervals.

## A. Coordinator candidate selection

Reconcile uncertain attempts first as today. Then read validated ledger, claims
and integration journal inventory once per workspace pass and group candidate
work by owner. Preserve owner order and claim sequence fairness. Include:

1. Waiting claims or `notificationPending`; bootstrap owners process claims only.
2. Every nonterminal job, including waiting approval/dependency/resource states.
3. Schema-2 continuation work without jobs. Match existing dispatcher eligibility:
   runnable; waiting when observed revision differs; needs_attention when its
   event is absent. Preserve pause/supervised, generation and identity handling.
   A conservative superset is acceptable; never omit runnable work.
4. Pending/retry outbox events whose retryAt is due.
5. Due handoff reminders, including **completed continuations**: matching owner,
   identity, recipient and generation; pending/acknowledged handoff; complete or
   needs_attention phase; not paused/held; both nextReminderAt and leaseUntil due.

Skip owners with no candidate work before notification_owner/native verification.
Snapshots are scheduling hints only. Retain existing current-generation, owner,
incarnation, fence, session-admission and locked action-time rereads. No snapshot
may authorize a grant, dispatch or delivery. Completed-owner notification/reminder
paths use notification_owner, not active-only engine.owner. After any owner work,
a fresh notification eligibility read may deliver newly created events; otherwise
wake/next pass handles them. Keep wake datagrams, five-second lost-wake fallback,
collection cadence, uncertainty recovery, suspension and blocked-owner fairness.
Bound full inventory work for idle owners; active mutation reads stay authoritative.
Malformed inventory is an error, never a healthy empty snapshot.

## B. Settled retry gate

A due-deadline-only predicate is incorrect: Step also enrolls state, discovers new
failures, settles accepted counts, suppresses policy changes and handles manual
input. Use a bounded process-local settled token as an optimization hint.

Every candidate reads current exact identity/ready member, retry state, policy and
**Backend.Observe** (fresh passive ReadTurnState), not a potentially stale activity
snapshot. Token includes exact relevant identity (generation, incarnation, scope,
thread/member identity), state content, complete relevant policy/thread content,
and actual observation Turn/Status/Code. No content change can be ignored merely
because policy revision did not change. No uncertain/due work can skip admission.

- Missing policy runs existing bounded EX transactRetryPolicy bootstrap, retaining
  stable double observation and inherited opt-out; reload afterward.
- Missing retry state, unenrolled state, missing policy thread, no token, changed
  input or unproved settlement falls back to the existing full path. Malformed or
  unreadable input fails; it is never cached as idle.
- Pending submitting/reconciling state always takes existing reconciliation-only
  admission, even after opt-out/cancellation, then reloads before ordinary dispatch.
- Scheduled pending becomes due at max(now, ClockMS) >= DeadlineMS. Matching
  settled tokens never bypass due work. Fresh execution keeps both existing
  pre/post-runtime-lock checks and all mutation/admission locks.
- Capture settlement **inside the admitted Step transaction**, never from an
  unlocked post-Step Load. The implementer's minimal SessionPolicy wrapper is
  accepted: delegate Decide/Checkpoint unchanged; remember the actual nonnil
  observation and capture final state/policy after the successful final nil
  Checkpoint while admission remains held. Stage the token until Step succeeds;
  discard on error, uncertainty, due state, or ambiguous callback ordering.
  Enrollment, dispatch and paths lacking a certifiable observation stay full
  fallback. Capture actual values processed, not a later sampled observation.
  Ordinary fresh preflight equality discovers a later native change next tick.

Keep one-second discovery, two-worker fairness and duplicate-job exclusion.
Bound tokens to live candidate identities, prune retired identities, and lose all
on restart. Tokens confer no execution authority and require no persisted schema.

## C. Coordination display cache

TTL **2 seconds from successful completion**. Retain at most **128 successful
entries and 16 MiB successful payload bytes**, plus at most **128 distinct active
flights**. Overflow returns the existing generic 503, never unbounded subprocesses.
Use expired-first/LRU successful-entry eviction; never evict a flight with waiters
as permission to launch a duplicate. Keep existing per-helper output bounds.

Key by workspace root/name, selected package/profile generation token, global
versus session scope; session scope includes current root/thread and
ObservationIdentity/incarnation. On **every request**, perform existing fresh
authorization and identity checks before using cache. Compare
readHostProfileIdentity directly; do not add a new provider admission gate.
Revalidate generation/incarnation after shared completion before publishing or
serving. Authorization is never cached.

Same-key requests share one flight. Successful valid JSON only is cached. Preserve
existing JSON, HTTP headers and error contract: expired data waits for refresh;
failed refresh returns existing 503, **no stale-success fallback**. Each waiter
cancels independently. Helper uses its own five-second context bound to server
lifetime; last-waiter departure or shutdown cancels its owned process group via
processgroup.Run. Shutdown waits for owned helper completion through existing
server ownership. A canceled first waiter must not cancel surviving waiters.

Successful local lifecycle/coordination-affecting mutation invalidates relevant
entries, including supervised lifecycle success; invalidating all workspace keys
is acceptable. Epoch fencing prevents an already-running old flight from
repopulating or serving invalidated content. External CLI changes may remain
visible for at most TTL; CLI authority and mutation reads remain uncached.

## D. Checks and benchmark acceptance

Each owner adds meaningful deterministic tests in its existing test package:

- Coordinator: 1/10/100 idle owners and roughly 3 MiB valid ledger; zero native
  owner-verification helpers and full inventories bounded per pass, not per
  idle owner. Exercise every candidate category, completed reminder/no-job
  continuation, same-pass new event, lost wake, blocked owner, and state/fence/
  generation change between selection and action with fresh refusal.
- Retry: after conservative settlement, 20 roots/100 members over 60 fake seconds
  of unchanged state produce zero full retry admissions/tmux checks; passive
  observation continues. Changed failure schedules; deadline dispatches once;
  unknown result reconciles; accepted checkpoint gap repairs; missing policy/state
  bootstrap safely; manual input/disable/retirement/identity race cannot execute.
  Prove settlement cannot certify a raced state or failed/dispatch Step.
- Cache: 20 concurrent same-key reads => one helper; TTL hit => zero; expiry =>
  one. Check key separation, malformed/failure 503, invalidation during flight,
  surviving waiter, last-waiter cancellation, shutdown and both capacity bounds.
  Fresh identity must reject stale incarnation even within TTL.

Controlled fixture uses real stores, actual retry workers/status handler and real
Ruby coordinator traversal with synthetic counting native backend and disposable
records only. A small Ruby loop adapter may invoke the real candidate pass and
baseline-equivalent per-workspace traversal; disable collection **only in this
disposable fixture**. A Go parent may launch that adapter in one owned cgroup;
whole-cgroup CPU includes synchronous helper children. Ruby Process.times at a
quiescent checkpoint can report coordinator self+child CPU separately. Native
Codex daemon CPU is excluded and must be disclosed. No other live session data.

Use representative 0/1/5 same-scope consumers, small and retained-state scale,
and an active phase with one completed-turn change plus due notification every
five seconds. Record reaction latency. Compare baseline/candidate on the same
host, three alternating warmed runs (10s warm-up, 30s measurement), reporting
self and whole-cgroup CPU, command counts, latency, allocations where available,
fixture identities and variation. A ~16-minute full matrix is acceptable after
fixture feasibility and review. Proposed 80% coordinator and 50% combined CPU
improvements remain experimental targets, not promised results or substitute
for correctness. No fixed <=5/10% absolute CPU requirement. Measure deployed live
cgroup CPU separately after authorized rollout with workload caveats.

Use repository Nix tooling and required hooks. Quick checks precede final
independent committed-deliverable review; long/integration/benchmark checks follow
review through a fresh policy watcher. Lead owns validation sequencing and exact
source/input receipts. No schema/protocol/state migration or coordinated node
update is intended. Keep code/docs compatible with mixed old/new browser assets;
cache and settled tokens vanish on process restart. Forward recovery uses the
same or a newer corrected profile; no unsupported profile rollback. Prepare
build/copy work before machine ownership, deploy under the required machine
claim, verify effects, integrate approved exact lineage, and release verified
machine ownership promptly. The session stays open.

---

# Workspace CPU investigation and proposed optimization packages

Status: investigation and proposals only, 2026-10-26. No application source,
service configuration, running process, package selection or lifecycle was changed.
Architect: architect0. Live measurements: implementer0. Portal source analysis:
implementer1. The lead owns scope decisions and any later implementation approval.

Supporting reports: [live process measurements](process-findings.md) and
[portal source findings](portal-findings.md).

## Scope and evidence identity

Explain sustained `workspace-portal` and `.workspace-host` CPU on this host,
identify bounded optimization packages, and propose regression checks. This brief
does not authorize implementation, deployment, restart, profiling that changes
service configuration, or cleanup of retained processes/sessions.

`dev-session current` and both environment identity variables matched
`2026-10-26-workspace-cpu-investigation` in
`/home/aither/workspace/ai/vpsfree.cz` before investigation. All source inspection
uses immutable selected-package source, not another initiative's checkout.

| Identity | Observed value |
| --- | --- |
| Selected package | `/nix/store/vq113xqpwhz09sc7myd9zciyqvn1lsvv-dev-workspace-0.2.0` |
| Package derivation | `/nix/store/m723id7qwyfm1gq4mbbi65h11p83cxbk-dev-workspace-0.2.0.drv` |
| Derivation `env.src` | `/nix/store/xzh3s2660hw9p1klfh26ck93l9msjy3w-source` |
| Source NAR hash, independently computed | `sha256-WX2++51WBDKFFp37i1IHZC6lz1GlcVOiNM2Vgl2BDCg=` |
| Matching workspace lock input | `aither64/dev-workspace`, `7e6d7c9cdb3388ab7abc720c034c15c21afbd686` |
| Source lock's codex-web revision | `8b60554bc10c2a6bcbf9732a8b77ad959c317036` |

The source hash equals the dev-workspace input hash in the workspace `flake.lock`;
this establishes the revision association. The canonical bare repository's local
master was `52dcd471186ef874c5c93f4133744195d4815454`, so its current tree is not
the deployed-source authority. References below are relative to the immutable
source directory above unless stated otherwise.

## Measurements and limits

Percentages use **100% = one CPU core**, not a percentage of the whole host.
The refined 30-second interval reported at `2026-10-26T19:30:46.622Z` measured:

| Service/process | Main-process CPU | Service cgroup CPU, including descendants |
| --- | ---: | ---: |
| Portal serve, PID 2017250 | 82.39% | 187.58% |
| Coordinator, PID 2017256 | 62.03% | 78.44% |
| Router, PID 2016996 | 1.30% | not separately reported |

The portal and coordinator therefore consumed about **2.66 CPU cores together**
in this interval. The earlier 30.142-second interval also reproduced the issue:
portal 88.91% self and coordinator 69.14% self. Its reaped-child counters were
120.73% and 17.98%, respectively; those counters attribute cumulative child CPU
at exit and are less suitable than cgroup deltas for precise interval totals.

The refined sampler consumed about 1.589% of one core. Sampling process births
every 200 ms observed at least 115 portal child births in 30 seconds: 75 `tmux`
(70 `display-message`), 30 host `coordination status` invocations, five `gh`, two
`git`, and three `dev-session`. The coordinator produced at least 18 portal
helpers. A third 20.066-second interval starting `19:32:07.065Z` classified 16
coordinator helper PIDs as `workspace-portal coordination-notify`, including any
present at the first sample. Short-lived children and wrapper-to-process exec
transitions make birth counts lower bounds. No process arguments containing
request text or credentials were reported.

The coordinator main thread accounted for 61.90% CPU. Portal work was distributed
among 64 threads; its hottest reported thread used 5.10%. Portal main RSS was
about 137 MiB. A later portal cgroup snapshot of about 2.00 GiB consisted of
253 MiB anonymous memory and 1,772 MiB file memory. It is mostly charged file
cache, not the portal's Go heap; these categories must not be added to RSS/PSS.

The third interval found 131 stable `team-mcp` helper processes using an older
package, with 1.03 GiB summed PSS, 2,996 threads and only 2.49% combined CPU.
This is a separate memory/thread footprint, not proof of a leak or a dominant
CPU cause. PSS apportions sharing; summed RSS would double count shared pages.
Older provider-worker and tmux-worker processes used only 0.30% and 0.17% CPU in
the first interval. Their package age alone does not justify cleanup.

These are active-workspace measurements, including this investigation's team.
No controlled idle experiment, sampled CPU stack profile, or before/after
optimization comparison was performed. Source analysis identifies concrete work
amplifiers, but does not apportion the measured CPU among individual functions.

## Findings: proven behavior versus inferred CPU contribution

### Coordinator repeats global work for every retained owner

`libexec/workspace-coordination-host.rb:639` starts the scheduler loop. Each
pass creates an engine per workspace, reconciles attempts, reads the global
owner list, and calls `coordinate_owner` for every unfenced owner. Its five-second
socket wait is a fallback; transaction wakes can run another pass sooner.

`coordinate_owner` at line 676 reads/validates the claims file, reads/validates
the global ledger, and scans every integration journal for each owner. Even when
there are no active jobs or background integrations, it still performs
`notification_owner`, a reminder scan, and notification eligibility checking.

`Store#read` (`libexec/workspace-coordination.rb:157`) reads and validates the
entire ledger each time. Validation includes per-job snapshot digests.
`Store#integration_journals` (line 317) reads all journal files on every call.
`notification_owner` (line 1078) reads the ledger again, then
`verified_owner_tracking` reads tracking and invokes a native verification
helper. `notification_call` (line 975) writes a private request with atomic
publication/fsync, starts `workspace-portal coordination-notify`, and removes
the request. `dispatch_notifications`
(`libexec/workspace-coordination-execution.rb:746`) reads the ledger again even
when there is no due event. `remind_integrations`
(`libexec/workspace-integration-handoff.rb:110`) repeats the journal inventory.

The live ledger's size was **2,659,042 bytes** and claims file **83,643 bytes**
(metadata only; other sessions' contents were not inspected). Repeated whole-file
validation multiplied by retained owners is a strong explanation for coordinator
CPU. The measured `coordination-notify` helpers match this path, though the
sample does not distinguish each helper's `verify`, `prepare` or `send` action.

### Retry and healthy-runtime checks repeatedly enter expensive admission

`portal/internal/web/server.go:3570` normalizes interactivity with two native
thread verifications and one `tmux display-message` check
(`portal/internal/session/authority.go:253`). Successful automatic-retry
admission calls it before and after acquiring the runtime lock
(`server.go:3749,3782`). Those two checks protect against concurrency changes.

The retry worker enumerates ready roots and members every second. Its
`stepTurnRetry` (`portal/internal/web/turn_retry.go:193`) reconciles uncertainty,
then resolves full mutation admission **before** `Controller.Step` decides
whether work is due. A successful admission therefore performs two tmux and four
native checks even when no retry will run. Queue limits bound concurrency, not
the cumulative unchanged work. This is a concrete early optimization target:
cheap due-state selection can avoid unnecessary admission while retaining the
full pre/post-lock proof for actual execution and reconciliation of uncertainty.

Healthy automatic recovery also normalizes each eligible session every five
seconds (`portal/internal/web/recovery.go:121`): A eligible sessions offer A/5
tmux checks per second before browser reads are included. Display/recovery
observations can share a bounded snapshot; actual recovery/mutation checks stay
fresh. The source explains opportunities behind measured tmux churn, but no
profile apportions the 75 observed tmux children among these callers.

### Catalog and roster repetition are secondary candidates

Independent of browser tabs, the server starts retry, notification and activity
workers (`portal/internal/web/server.go:548`). The retry worker lists ready
active sessions and their rosters every second (`turn_retry.go:148`); notification
observation lists sessions every two seconds (`notifications.go:51`); activity
observation lists sessions and rosters every five seconds (`activity.go:221`).

There is already a one-second session-discovery cache
(`portal/internal/session/catalog.go:153`). A miss enumerates active and archived
tracking; validation checks three confined files per session
(`manifest.go:293`, `catalog.go:98`). Existing caching and passive history
connections should be extended selectively. Adding a second blanket cache or
merely slowing every timer would obscure freshness and ownership contracts.

Unchanged parsed session records are already cached; a miss does not imply
parsing every YAML document again. Roster reads remain separate full JSON
loads (`portal/internal/teamruntime/runtime.go:699`). Broader snapshot reuse and
an active-only discovery view are secondary candidates after the concrete
retry/status subprocess work is reduced. Existing repository status caching also
has no singleflight; independent remote GitHub refresh is lower priority.

### Coordination display reads spawn a full helper per HTTP request

`portal/internal/web/coordination.go:15` invokes `workspace-host coordination
status --json --portal` for a global read, or its `dev-session` counterpart for a
session read. Every GET starts a subprocess with a five-second timeout; there is
no shared in-flight request or snapshot cache at this handler. The portal guide
documents operations and reservation badges refreshing every five seconds.

Thirty observed status-helper births in thirty seconds establish repeated work.
The number of browser consumers and their exact contribution were not measured;
the process rate alone does not prove how many tabs were open. This read path is
a direct target for coalescing and cached display snapshots.

## Ranked implementation packages (proposals, not assignments)

| Rank | Package and file boundary | Proposed change and acceptance |
| --- | --- | --- |
| 1 | Coordinator work selection: `libexec/workspace-coordination-host.rb`, scheduler tests in `test/integration_test.rb` and `test/workspace_coordination_test.rb`; small selectors in coordination/integration modules only as required | Read ledger, claims and journal inventory once for scheduling; index pending jobs, claims, notifications and due handoffs by owner. Skip idle owners before native verification. Preserve the existing action-time admission and authoritative rechecks. With zero due work, one pass launches zero owner-verification helpers; adding idle owners does not multiply full ledger/journal reads. |
| 2 | Cheap retry scheduling and shared runtime observation: `portal/internal/web/turn_retry.go`, `recovery.go`, narrowly scoped `server.go` helpers and focused tests | Select due enabled retries and unresolved outcomes before full admission. Preserve uncertainty reconciliation, policy bootstrap and fresh pre/post-lock checks for execution. Twenty roots plus 100 members with no due/uncertain work produce zero full retry admissions after discovery over 60 fake seconds; one due retry executes exactly once. Share only healthy display/recovery observations, retaining recovery detection within its current five-second cadence. |
| 3 | Coordination display snapshots: `portal/internal/web/coordination.go` and its tests | Coalesce concurrent identical reads and reuse one short-lived successful snapshot keyed by workspace/package/scope/incarnation. Twenty concurrent reads for one key produce one helper; reads inside the chosen TTL produce none. Keep authorization per request, bounded freshness, stale/error presentation and mutation invalidation. Start with same-key sharing; cross-session workspace projection is optional follow-up needing explicit filtering design. |
| 4 | Continuous regression evidence in existing Go/Ruby tests and optional fixture benchmark | Add deterministic work-count/scale assertions first, then a representative process/cgroup benchmark. Keep raw timing as comparison evidence until variance is characterized; avoid an uncalibrated universal wall-clock gate. This test package is coupled to the three changes, not a new monitoring subsystem. |

Ranks 1 and 2 have independent Ruby/Go boundaries and can proceed in parallel
after approval; rank 3 is also narrow but may share Go server wiring with rank 2.
The lead should serialize edits to common server fields/tests. Catalog/roster
reuse can be a later package in `portal/internal/session/catalog.go` and
background-reader/roster code if residual CPU warrants it. Avoid a schema
rewrite, replacing Ruby with Go, broad persistent indexes, or indiscriminate
longer polling in the first optimization pass. The measured data does not yet
justify those costs. Reporting-helper consolidation is a separate investigation
if memory/process count remains a user concern.

## Compatibility and invariants

- Scheduling snapshots choose candidate work only. Before grants, dispatch,
  notification delivery or lifecycle-sensitive reads, retain exact current
  generation, owner incarnation, fence, session lock and ledger checks. A cached
  display or scheduling snapshot never grants authority.
- Work selection must include pending claim notifications, runnable background
  integrations with no jobs, retry deadlines, and handoff reminder/lease deadlines.
  Retain wake datagrams and the five-second lost-wake fallback. Preserve fairness
  when one owner is blocked, fencing/suspension, uncertain operation reconciliation,
  and completed-session notification delivery.
- A ledger can change between candidate selection and action. Revalidate under
  existing locks, invalidate local snapshots after writes, and retry later rather
  than act on stale proof. A cache must preserve read/validation errors and bounded
  state limits. Do not turn failed reads into an empty, healthy inventory.
- Background observation must still discover ready members without an open tab,
  detect input/finish notifications, preserve stale markers and timing coverage,
  and never start held/stopped threads. Batch status must preserve tmux/server
  identity and package generation semantics.
- Initial proposals require no persistent-state, database, Codex protocol, API
  removal or cluster schema migration. Optional HTTP age/stale fields must be
  additive, with older browser behavior considered explicitly.
- Deploy through the existing selected user-profile package workflow only after
  separate authorization. No coordinated vpsAdminOS/node update is needed. The
  runtime is forward-only: recovery uses the same or newer corrected package;
  do not propose selecting an older profile. Existing recovery contracts and
  deployed lineage requirements remain intact.

## Regression acceptance and verification plan

No test suite or synthetic service workload was run for this investigation.
The checks below are proposals for a future authorized implementation.

| Level | Fixture/scenario | Required observation |
| --- | --- | --- |
| Quick Ruby | Empty work with 1, 10, 100 retained owners and a valid roughly 3 MiB ledger | Zero verification/notification subprocesses; full ledger and journal scans bounded per pass rather than per idle owner; no state mutation. |
| Quick Ruby | One due claim, event or reminder among many idle owners | Only its owner receives action-time verification; wake path and fallback discover it; deadlines and fairness stay bounded. |
| Quick Ruby | Runnable background integration without pending jobs; completed owner with pending delivery | Existing behavior retained, using `test/integration_test.rb:507` and completed-session delivery coverage around line 401 as regression anchors. |
| Quick Ruby | Change fence, generation, owner identity or claim between snapshot and dispatch; lost wake | Refuse stale action, retain uncertain receipts, recover on a fresh pass. Preserve existing wake test at `test/workspace_coordination_test.rb:618`. |
| Quick Go | Twenty roots and 100 members; 60 fake scheduler seconds with no due/uncertain retry, then one due retry | Zero full retry admission/tmux checks after discovery while idle; exactly one dispatch when due. Preserve unknown-response reconciliation, manual-input supersession, member retirement and generation checks. Existing `web/turn_retry_test.go:42` supplies queue fairness coverage. |
| Quick Go | Concurrent/repeated background discovery and roster reads; unchanged archive grows 1/10/100 times | Instrument metadata reads, YAML parses, tmux/native calls and allocations. Work attributable to unchanged history is bounded by refresh policy, not multiplied by independent consumers. |
| Quick Go | Concurrent coordination GETs, expired cache, cancellation and helper failure | Single in-flight helper per scope, correct fanout, bounded stale result, no healthy empty fallback; one canceled client does not corrupt or leak shared work. |
| Browser fixture | 1/10/50 tabs; hidden, foreground, reconnect, question arrival | Hidden tabs stop polls/streams, foreground state recovers within documented intervals, and repeated badges do not multiply backend status commands. Reuse existing browser visibility tests. |
| Longer benchmark | Disposable synthetic workspace with current-scale ledger, active/idle sessions, retained teams and long/short history; no tabs versus visible tabs | Record cgroup CPU seconds, main CPU, subprocess counts by fixed command family, request counts, p50/p95 latency, Go allocations and memory breakdown after warm-up. Compare baseline and candidate on the same host and workload. |

The first performance gate should enforce deterministic counts and asymptotic
behavior. Suggested benchmark target, to confirm against the controlled baseline:
reduce coordinator CPU and its idle-owner helper launches by at least 80%, and
reduce aggregate portal/coordinator cgroup CPU by at least 50% with unchanged
visible update latency. These are **proposed targets**, not measured improvements
or proven achievable absolute limits. Report active and idle workloads separately;
do not require zero background CPU because observation and notifications operate
without browsers.

Use the selected repository Nix environment. Quick checks should be focused
Ruby tests and `go -C portal test -mod=readonly` for affected packages; syntax and
applicable package evaluation precede independent review of any implementation.
Longer fixture/native/browser checks follow review under the normal verification
watcher policy. Three comparable warmed runs are sufficient initially; stop if
variance prevents a useful conclusion and fix the fixture before expanding CI.

## Remaining uncertainty

The leading hypotheses align with measured CPU and child command rates, but
there is no stack-level attribution or causal before/after proof. Both member
reports are reconciled above. Their example absolute CPU budgets are exploratory;
this brief does not adopt them as product requirements. The immediate deliverable
is an actionable diagnosis and test plan, not a claim that performance is fixed.

Session remains open:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-26-workspace-cpu-investigation/>.
