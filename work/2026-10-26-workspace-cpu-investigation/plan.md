# Portal and host CPU investigation

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
