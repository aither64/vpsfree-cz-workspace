# Portal CPU source investigation

2026-10-26, implementer1. Investigation and proposals only; no application edits,
builds, tests, service changes, worktrees or branches. Session identity and both
environment variables matched `2026-10-26-workspace-cpu-investigation` in
`/home/aither/workspace/ai/vpsfree.cz` before reading session records.

## Source and evidence boundary

- Selected profile: `/nix/store/vq113xqpwhz09sc7myd9zciyqvn1lsvv-dev-workspace-0.2.0`.
- Its deriver: `/nix/store/m723id7qwyfm1gq4mbbi65h11p83cxbk-dev-workspace-0.2.0.drv`.
- Derivation `env.src`, inspected directly:
  `/nix/store/xzh3s2660hw9p1klfh26ck93l9msjy3w-source`.
- Architect0 independently matched that source NAR hash to locked dev-workspace
  revision `7e6d7c9cdb3388ab7abc720c034c15c21afbd686`.
- All dev-workspace references below are relative to that immutable source.
  Browser defaults come from packaged codex-web source
  `/nix/store/9izv9lhmq9qgkx1rixyxz9msr62k6idf-source`, revision
  `8b60554bc10c`, `conversation/assets/refresh.js:10-15`.

The live measurements were supplied by implementer0/lead, not produced by this
source investigation: a refined 30-second interval had portal self CPU 82.39% of
one core, portal cgroup CPU including children 187.58%, and at least 115 portal
child births, including 75 tmux (70 `display-message`), 30 host coordination
status wrappers, five gh and two git. Sampling is a lower bound and wrapper
processes can represent stages of one invocation. The simultaneous coordinator
had 62.03% self / 78.44% cgroup CPU. These observations establish sustained work
and child churn; they do not assign a measured CPU percentage to a source path.
Architect0 owns coordinator internals; this report traces portal callers only.

## Highest-priority paths

### Coordination badges spawn the host CLI per visible page

`portal/internal/web/static/coordination.js:4-9` activates on both the session
list and session coordination panel. `:229-258` issues a GET and schedules the
next read five seconds after completion. `:264-275` pauses hidden pages but keeps
session reservation badges refreshing while another section is selected.
There is one in-flight request per page, with no cross-tab sharing.

`portal/internal/web/coordination.go:15-42` unconditionally starts
`workspace-host coordination status --json --portal` (or its session-specific
dev-session form) for each GET, with a five-second timeout. It validates and
returns the resulting JSON; there is no server cache or in-flight coalescing.
Therefore V visible pages offer roughly `V / (5s + request latency)` host
invocations per second. The measured 30 host wrapper births/30s are consistent
with this source path; page count and exact invocation count were not measured
by this package. Five short-latency tabs would offer about one invocation/second.

Small first package: coalesce identical read requests in the portal and retain a
short display cache, preserving workspace, selected package, session and
observation identity boundaries. Start with a five-second display window, or a
two-second window if the accepted freshness requirement demands it. A shared
global projection for different sessions needs explicit scope/filtering design;
identical-key coalescing is the smaller initial change. Preserve failure/stale
indicators and same-slug incarnation fencing. Keep authoritative CLI reads and
mutation admission fresh. Do not add a new daemon or persistent cache for this.

### Repeated interactivity checks explain tmux opportunities

`portal/internal/web/server.go:3570-3638` normalizes interactivity with two native
thread verifications and one `RuntimeAuthority.VerifyTmux`. The latter launches
`tmux -S ... display-message -p ...` at
`portal/internal/session/authority.go:253-261`. This is an exact match for the
dominant sampled tmux subcommand, but its caller proportions remain unmeasured.

Callers include:

- Recovery: `portal/internal/web/recovery.go:121-162` scans every five seconds,
  and normalizes each eligible automatic-recovery session even when its saved
  runtime is healthy. With A eligible sessions, this alone offers A/5 tmux
  commands/second and 2A/5 native thread verifications/second.
- Automatic retries: `portal/internal/web/turn_retry.go:148-178` enumerates all
  retained-ready active roots and ready members every second and feeds two
  workers. Each admitted `stepTurnRetry`, `:193-236`, reconciles uncertainty then
  resolves an ordinary mutation before `Controller.Step` decides what to do.
  `server.go:3749` and `:3782` both normalize interactivity. A successful full
  retry admission therefore has two tmux calls and four native verifications,
  plus member checks; repeated scheduler steps have no initial due-state filter.
  Two workers and a bounded queue limit concurrency, not total idle work.
- Browser details: `server.go:1364-1388` normalizes interactivity for every
  details read. `static/app.js:3772-3780,3864` polls visible pages every 15s by the
  shipped codex-web policy. Conversation API resolution also normalizes at
  `server.go:3745-3749`, so pending/queue/activity reads can add checks.

Next small package: distinguish cheap scheduling/observation from actual retry
admission. Avoid entering full mutation admission for a conversation without a
due enabled retry or an unresolved outcome. Reconcile uncertain attempts before
fresh execution and preserve all locks, generation proofs and fresh pre/post
lock checks for actual mutations. For healthy recovery and display readers,
coalesce same-session checks and consider a bounded observation cache keyed by
runtime authority plus package/thread identity. A display cache must never grant
execution permission. Removing the second mutation-time check outright would
lose its concurrency protection and is not the proposed optimization.

## Other amplification and existing mitigation

Server startup (`portal/internal/web/server.go:548-557`) starts all relevant
background workers independently of browser presence:

| Reader | Cadence and scaling | Evidence |
| --- | --- | --- |
| Retry scheduler | 1s; active roots and ready members | `web/turn_retry.go:148-170` |
| Notifications | 2s; lists all sessions and observes attention | `web/notifications.go:51-80` |
| Activity discovery | 5s; validates ownership and reloads each active roster | `web/activity.go:221-250,276-290` |
| Activity per thread | 5s active, 30s idle, 1s while refreshing; event wakeups, four shared read slots | `web/activity.go:117-129,166-201,293-374` |
| Recovery | 5s; saved recovery state plus live verification | `web/recovery.go:121-162` |
| Provider-watch recovery | 1s; provider state and marker directory | `web/provider_watches.go:47-79` |
| Progress observer | 1 minute | `web/progress_observer.go:117-124` |

Here `web/` means `portal/internal/web/`. Lifecycle display worker wakes every
second but gates substantive work to requested/running operations and backs off
(`web/operation_state.go:54-98`); it should not be described as a full scan every
second unconditionally.

The existing session catalog helps: it coalesces discovery for one second and
caches parsed records. However, `session.List` still inventories both `work` and
`archive` on a miss (`portal/internal/session/manifest.go:293-335`), validating
three confined file stamps per cached session (`session/catalog.go:98-128`).
Hits clone every returned summary (`:90-95,153-165`). Background readers receive
archived summaries before filtering them. With N retained sessions and repeated
discovery misses this is O(N) metadata traffic, not repeated parsing of every
unchanged YAML record. A shared active-only discovery view and unchanged-file
roster cache are secondary proposals after measured subprocess work is reduced.

Roster loads are not cached: `web/server.go:2225-2233` constructs a store and
`portal/internal/teamruntime/runtime.go:699-728` opens, reads, JSON-decodes and
validates the full roster each time. Retry, notification attention and activity
discovery independently do this (`web/attention.go:165-193` also rechecks live
ownership). This can contribute portal self CPU, especially with many large
rosters; no CPU profile proves its share yet.

Repository polling explains gh work: details refresh validates repositories and
requests status even outside Repositories (`web/server.go:1375-1388`). The status
cache lasts 5s active / 1min archived, without singleflight (`:1468-1506`). On a
miss, `repository/status.go:101-124,157-202` fans out local Git plus remote status;
GitHub commands are at `repository/origin_github.go:71-80,124,158`. Consider
sharing refreshes and slowing remote metadata independently from local status,
or fetching full repository details on demand. Preserve exact-head CI matching.
This is lower priority than the observed host/tmux churn.

## Regression checks to propose, not run in this investigation

Extend existing tests rather than introducing a separate harness:

1. **Coordination command count:** inject a counting/blockable command reader;
   twenty concurrent GETs for one cache identity launch one command, and reads
   within the accepted display TTL launch none. After expiry exactly one new
   command runs. Different workspace/package/incarnation keys never share data.
   Canceling one waiter must not cancel surviving waiters; deadlines and failures
   retain bounded retries and visible stale state. Use fake time and counters.
2. **Retry idle budget:** twenty roots with five members each and no due or
   uncertain retries, advance sixty scheduler seconds: zero full mutation
   resolutions, tmux checks or retry starts after initial policy discovery. Then
   schedule one due retry: exactly one execution, with fresh mutation proofs.
   Unknown response, manual input, generation change and member retirement must
   still prevent duplicate execution. Keep the two-worker fairness check.
3. **Recovery/display budget:** unchanged healthy authority should require at
   most one shared observation per accepted window, independent of duplicate
   display callers. Replace authority/thread/package while cached: subsequent
   mutation must fail or revalidate immediately. Preserve recovery detection
   latency (initial target <=5s) and interruption cancellation.
4. **Catalog/roster counts:** unchanged entries must not be decoded again;
   active-only readers must not reparse archived entries. Atomic rename,
   same-size rewrite, deletion, duplicate root, archive/revive and roster changes
   must invalidate correctly. Track metadata/parse counts independently.
5. **Browser workload:** fake-clock 0/1/5 visible tabs, hidden tabs and repeated
   focus events. Hidden tabs send zero periodic reads; ten focus events in a
   fresh interval do not multiply reads. Retain notification observation with all
   tabs closed; disabling observation to meet a CPU goal changes behavior.

Relevant existing coverage:

- `web/coordination_browser_test.cjs:94,152,220,246,258`: hidden-page cancellation,
  badges outside the selected panel, cached rendering and incarnation fencing.
  It does not enforce a server subprocess budget across tabs.
- `web/activity_test.go:42,118,272,324,457`: state-based snapshot reuse, browserless
  observation, four-slot concurrency, duplicate-thread fairness and team watches.
- `session/catalog_test.go:74,113,144`: mutation-safe copies, concurrent deletion
  and duplicate roots; no large-inventory command/metadata budget.
- `web/turn_retry_test.go:42` prevents duplicate queued jobs and worker monopoly;
  it does not require idle conversations to skip full admission.
- `web/operation_state_test.go:785,819,1125`: fast published snapshots and skipping
  completed/failed receipts. Preserve these while changing shared refresh work.
- `web/read_cycle_browser_test.cjs:77-170` protects lane retirement/freshness and
  late responses. `web/read_diagnostics.go:76-170` adds Server-Timing and bounded
  slow/error logs; these measure wall time, not CPU. No `Benchmark*` Go functions
  or pprof endpoint/import were found in portal sources.

Suggested disposable scaling fixtures: (a) empty/no tabs; (b) 20 active roots,
100 members, 200 archived sessions, all idle/no tabs; (c) same plus five tabs;
(d) 100 active roots/500 members/1,000 archives; (e) ten active streams, long
transcript backfill, one due retry and one failed provider. Hold membership and
input size constant between comparisons. Do not read other live session content
to populate fixtures. Count children, RPCs, catalog/roster parses and allocations
first; wall-time microbenchmarks alone miss child CPU.

Provisional machine-level acceptance, to calibrate on the same host: after
warm-up, fixture (b) should use <=5% of one core across portal plus children and
should launch zero coordination-status children with zero tabs. Fixture (c)
should use <=10%, with no linear five-tab multiplier for an identical status
key; a 5s cache has a target <=12 status commands/minute/key. These are proposed
budgets, not verified performance or established product requirements. Record
portal self and cgroup CPU separately; require no >20% same-host regression in
larger fixtures while preserving activity latency <=5s active / <=30s idle and
fresh mutation safety. Tune absolute CPU targets after a disposable baseline.

## Handoff

Priority order: coordination read coalescing/cache; cheap retry due-state
scheduling and healthy-runtime observation sharing; roster/catalog reuse;
repository remote refresh isolation. Each is a separate bounded package and
needs explicit implementation scope plus the architect's accepted safety brief.
No persistent format or API migration is needed for process-local display
caches. Main compatibility risks are stale authority granting writes, cross-
session/incarnation leakage, delayed recovery or notifications, missed uncertain
retry reconciliation, and cancellation behavior. Preserve process-local cache
teardown on package restart and existing rollback/state contracts.

Investigation findings need no project documentation changes or mandatory change
review. Lead owns plan/state/design synthesis and final user recommendations.
Session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-26-workspace-cpu-investigation/
