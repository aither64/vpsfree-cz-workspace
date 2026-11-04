# Measurement investigation — package B

Advice only, 2026-10-31. Inspected canonical `repos/dev-workspace.git` at
`6f54d0c7fdb974705c120b3c1ef5372f5897d544`, the corrected workspace pin,
using `git show`/`git grep`. Bare `master` was not the selected source.
`dev-session current` and both environment identity values matched this session
and workspace; the same-session roster confirmed implementer1 and architect0.
No peer roster, files, conversations, worktrees or detail endpoints were read.
No code/configuration edits, fetch, push, tests or lifecycle actions were made.
The installed portal's source revision and live API behavior were not verified;
the source conclusions below must not be presented as installed-runtime proof.

## Immediate aggregate visibility result

The pinned portal provides **`GET /api/index-status`**, a workspace-wide
read-only overview. Its `sessions` rows contain `slug`, `sensitive`,
`observationIdentity`, `updatedAt`, `archived`, repository count, running-cluster
count/known flag, optional cluster notice and pending lifecycle. The envelope
includes `generatedAt`, `authoritative`, `loading`, `warning` and lifecycle
operation summaries. `?progress=1` avoids explicitly requesting a display refresh.

This route can establish overview membership and count nonarchived sessions;
nonarchived does not mean currently working. Check freshness, authoritativeness,
loading and warnings before treating counts as complete. `updatedAt` is a recent
activity/record timestamp, not working duration or a delivery milestone.
There are **no working/waiting/idle/coverage totals or current activity states**
in this response, and no `GET /api/sessions` collection route at this revision.
No workspace aggregate-clock route was found in the pinned route table.

`GET /api/sessions/<slug>/team-stats` returns per-member snapshots and loads that
session's roster. It is a same-session diagnostic, not an allowed workaround for
peer aggregate data. `/progress` exposes observer status/concerns, not aggregate
clocks; do not call peer detail endpoints to synthesize missing totals.

Sources: `portal/internal/web/server.go:113`, `:804`, `:1008`, `:1042`,
`:1156`; `portal/internal/web/team_stats.go:20`;
`portal/internal/web/progress_observer.go:595`.

## What the clocks establish

- Lead and retained-member clocks describe **their individual conversation
  histories**, with working, waiting and idle durations. Waiting includes blocking
  questions, approvals, sleep and team waits; overlapping waits count once.
  Nonblocking questions do not pause work. Idle means no current turn.
- Timing is observed by the portal service without requiring an open browser.
  Observed timing checkpoints survive restart; historical or disconnected
  intervals that cannot be reconstructed stay unclassified. Partial coverage is
  not evidence of low effort. Fresh observation after reconnect does not repair
  earlier unknown intervals. Stopped/removed members use saved final snapshots.
- Counts describe prompts, assistant/plan messages and tool items, not useful
  work or completed packages. Forks exclude inherited turns. Utility verification
  watchers are outside the persistent roster, so team totals are not a complete
  resource-accounting view.
- The observer receives individual working minutes plus `CoverageComplete`,
  `TimingApproximate`, `UnclassifiedMS` and coverage reason. Its prompt explicitly
  says member clocks overlap and incomplete coverage is a lower bound, not
  session age. Context includes the lead and ready, nonretiring non-observer
  members; it is not identical to Team's retained-member population.

The observer's scheduling predicate is separate from accumulated working time:
it permits current `working` **or** `waiting` activity except approval/user-input
waits, after checking freshness/current turn. When the activity monitor is absent,
an active transcript is the fallback. Thus a check can be eligible while
a lead waits for a tool/member. A check interval is wall-clock scheduling, not
an accumulated-work budget, throughput measure or delivery deadline.

Sources: `README.md:348`, **Working and waiting time**;
`docs/workspace-portal.md:1671`; `docs/dev-sessions.md:466`;
`portal/internal/web/activity.go:17`, `:58`, `:116`, `:169`, `:244`;
`portal/internal/web/team_stats.go:34`;
`portal/internal/web/progress_evidence.go:16`, `:44`;
`portal/internal/web/progress_observer.go:93`, `:266`, `:280`.
Exact classification is imported from `github.com/aither64/codex-web/codex`;
the pin selects `d3a29bee90ef00a08816920408c596152339a637` in `flake.lock:44`
and `portal/go.mod:7`. That dependency's implementation was not inspected, as
agreed with the lead; these are documented and consumer-level semantics.

## Why lead working duration cannot identify the bottleneck

A long lead clock does not say whether time went to necessary scoping,
coordination, duplicated investigation, tooling or rework. A short lead clock
can coexist with a slow prerequisite, blocked implementers or a long verification
job. Neither clock records package readiness, dependency release, accepted
outputs or whether the lead was on the path determining delivery time.

Summing overlapping member clocks measures observed participant time, not
elapsed delivery time. For a common fully covered window of length T, working
totals Wi only bound the union U: `max(Wi) <= U <= min(T, sum(Wi))`. They cannot
recover overlap or the dependency critical path. Incomplete or unequal coverage
makes utilization/speedup comparisons less reliable. Message/tool counts and
diff size also cannot establish productive parallelism or design necessity.

## Prioritized measurement advice

1. **Package/milestone timeline first.** Record scope, owner, dependencies,
   contract-ready time, assignment, first activity, reviewable output and lead
   acceptance. Include concise evidence of resolved design constraints and the
   next observable result. This distinguishes necessary prerequisite design,
   dispatch delay, execution and acceptance delay without pressuring premature
   parallel implementation.
2. **Explain blockers on the delivery path.** Track intervals with reason and
   the dependency that releases them: design/contract, member result, approval,
   merge/resource ownership, build/test or rework. For verification include
   queue/start/finish/result and watcher ownership. Separate avoidable lead
   serialization from genuine prerequisites. Report wall time from accepted
   scope to accepted milestone alongside these intervals.
3. **Add concurrency only with coverage.** For the same observation window,
   aggregate interval unions and number of concurrently working development
   participants; distinguish lead, execution, review/observer and watcher work.
   Preserve unclassified time and snapshot freshness. With a dependency timeline,
   identify the chain determining delivery; do not label summed clocks a
   critical-path measure or infer a solo speedup baseline.
4. **If global timing is later required**, propose a dedicated read-only summary
   containing only aggregate counts/durations, observation window, coverage and
   freshness. Define cohort, overlap semantics and unavailable behavior first.
   This is a possible follow-up, not a current implementation recommendation or
   authorization to inspect peer detail records.

Existing clocks support a progress conversation; they do not prove that lead
work is the bottleneck or justify changing team size. The smallest useful next
measurement is a dependency-aware milestone/package timeline for an authorized
session, then comparison of actual delay segments.

Session portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-31-team-workload-parallelization/
