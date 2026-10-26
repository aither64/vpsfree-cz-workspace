# Portal and host CPU optimization

Delivered: the authorized implementation, deployment and integration milestone
is complete. The original investigation scope below is historical; the later
implementation authorization supersedes it. Final evidence and current CI status
are in state.md, performance-results.md and rollout.md.

## Goal and scope

Investigate sustained workspace-portal and .workspace-host CPU on this host;
recommend optimizations and meaningful performance regression tests. Findings
and proposals only: no application edits, restarts, deployments or integration.

## Affected repositories

- dev-workspace: portal, workspace-host helpers, refresh/polling and tests.
- codex-web only as a read-only dependency reference if evidence points there.
- Coordination workspace: this session's investigation records only.

## Approach and backlog

| Owner | Result | Acceptance | Dependencies/checks |
| --- | --- | --- | --- |
| implementer0 | Live process findings | Interval CPU, process identity, child churn, overhead/limitations | Read-only bounded /proc sampling |
| implementer1 | Portal source findings | Exact source references, refresh/call costs, existing test gaps | Match selected runtime, coordinate architect |
| architect0 | Investigation synthesis/design.md | Ranked causes and optimizations, concrete regression workloads/budgets, measured/inferred distinction | Process and portal reports |
| lead | Acceptance and user report | Reconcile claims, preserve records and stable portal URL | Member evidence |

## Compatibility and deployment

No runtime or persisted state changes. Future optimizations must preserve freshness,
ownership checks, mixed-version behavior and error visibility. Any proposed cache
must identify invalidation and stale-read rules. Deployment and implementation are
outside this investigation milestone.

## Documentation and testing

Readers: operator and future implementer. Findings remain under this session;
no reusable behavior documentation is changed. Sample live usage in short batches;
inspect source and existing test coverage. Propose isolated deterministic work/count
assertions plus representative scaling benchmarks, avoiding timing-only unit tests.
Do not run production fixtures, builds or long integration checks for this analysis.

## Authorized implementation milestone

User accepted the implementation plan and said “Implement the plan.” Earlier
authorization: “aitherdev can [be] deployed using vpsfree-cz-configuration. when
verified, you can merge it and release aitherdev.” The accepted plan identifies
dev-workspace, workspace and vpsfree-cz-configuration master as merge targets.
No reboot or session lifecycle action is authorized. Selected display TTL:2s.

| Owner | Implementation | Acceptance/dependencies |
| --- | --- | --- |
| architect0 | Final durable design and technical decisions | Complete candidate semantics and file boundaries before edits |
| implementer0 | Coordinator due-work index and Ruby tests/docs | O(1)global inventories,zero idle verify helpers,preserve fresh actions |
| implementer1 | Settled retry token and Go tests/docs | Fresh passive observations,zero unchanged idle full admissions,preserve all retry transitions |
| implementer2 | Coordination display cache and Go tests/docs |2sTTL,128entries,16MiB,same-key sharing,fresh identity,cancellation,no stale success |
| implementer3 | Controlled benchmark fixture/methodology, later consumer pins | Baseline vs candidate whole-serviceCPU,synthetic input,3warmed runs; no new subsystem |
| reviewer0 | Mandatory final independent review | Committed changes+quickchecks,complete branch/migration assessment |
| lead | Acceptance,records,publication,rollout/integration coordination | No repository claims until fresh approved merge; separate machine claim |

Shared dev-workspace worktree starts origin/master7e6d7c9c. Independent files
may be edited concurrently; overlapping docs/server edits and Git mutations
serialize. No broad catalog/recovery/MCP changes. No public API/state migrations.

Commit and quickcheck all intended work, then independent review, then longer
packaged/benchmark checks via fresh utilities. Target50%combined idleCPU and
80%coordinator improvement, no repeatable>20%active regression; measure whole
service descendants,callcounts,latency,allocations with3comparable warmed runs.
Preserve current update latencies and reject stale/duplicate mutations.

Consumer pins select exact published runtime. Use confctl channel dev-workspace
role devWorkspace and workspace nested override; preserve extension and unrelated
inputs,check deployment contract. Prepare exact committed system/application
builds and copies before aitherdev claim. Claim physical vpsfree:aitherdev,
dry-activate/no-reboot system switch,then claimed application profile switch.
Verify health/continuity/behavior/CPU and exact paths. Merge each approved master
with short individual claims,fresh targets/hooks/push+remoteproof,release before
CI/records. Prove all deployed lineage integrated,then inspect exact machine
claim/reconcile effects/release+verify. Retain hold on failed/uncertain effects.
Application recovery is forward-compatible same-or-newer generation.
