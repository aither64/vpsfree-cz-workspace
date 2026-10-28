# Final review packet

User requested implementation, deployment and recovery of archive failure caused
by managed retry admission rejecting an active native watcher. Accepted design:
private shutdown callback uses managed interruption for retained roots/members,
native interruption only for verified descendants. No generic retries or UI
redesign. Source and tests committed; focused Go archive/settings checks pass.

Read shared AGENTS.md, applicable procedures and each project AGENTS.md; read
~/.codex/skills/mandatory-change-review/SKILL.md and all four lane references.
Review general, architecture/repetition, scope/proportionality, risk/compatibility.
Overall risk high: destructive lifecycle shutdown and live deployment, despite
bounded implementation. Local operator trusted; wrong identity, concurrent
operations, uncertain admissions and recovery remain in scope. No speculative
hostile local filesystem hardening. Independent reviewer fallback: no retained
roster in threadless session; installed default delegated reviewer is
 gpt-6.1-sol/xhigh, read_only role, full_access execution policy. Do not edit code,
deploy, test long checks, spawn reviewers or message external services.

## Design and checks

plan.md and design.md here define acceptance and deployment. Documentation change
is in runtime docs/session-archive-recovery.md. No migration, public API or protocol
change; schema/journal compatibility retained. Runtime owns behavior, workspace
and configuration consume exact published source. codex-web and extension unchanged.
Queued prompts, goals, parent-first shutdown/resampling, child-first retirement,
managed retry cancellation/uncertainty and foreign threads must remain correct.

Red test: /tmp/archive-native-watchers-before.log (exact admission error for root/
member active child; invalid test-only pending ID separately corrected). Green:
nix develop --command bash -c 'cd portal && go test -mod=readonly
./cmd/workspace-portal ./internal/workspacecodex -run
"Test(ExplicitArchive|ArchiveSQLite|RetryManagedSettings)" -count=1'. Both pass.
Gofmt and diff checks pass; configuration normal Overcommit hooks pass; deployment
contract checker passes absolute roots; semantic input comparisons preserve all
other nodes. No long integration tests or deployment started. Proposed longer
checks: runtime package/archive VM, composed default+deployment-contract and
exact aitherdev build, exact-head CI. Fresh utilities execute/monitor checks.

## Whole-branch history

Runtime one functional commit includes directly supporting docs/tests. Workspace
one pin update atop five inherited shared tracking-only commits, no feature edits
inside that prefix. Configuration one generated channel commit, preserve its
message. Two distinct consumers each have one pin stream; no repeated updates,
obsolete branch approaches, migrations, released/deployed new schema or external
state introduced by this feature. Review complete ranges below and give explicit
history/migration/consolidation conclusion. Default-branch integration not approved.

### dev-workspace

Path: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-28-archive-native-watchers/dev-workspace`
Base: `4a002f52c3b55099540aa99708d5fcf29f7b2456`
Head: `db9578e2e195d2a86873e49bcdcfb1cf28bf62d8`

```
db9578e2 archive: interrupt owned native watchers outside managed admission
```

docs/session-archive-recovery.md                   |   4 +
 .../cmd/workspace-portal/archive_explicit_test.go  | 231 +++++++++++++++++++++
 portal/internal/workspacecodex/archive_explicit.go |  89 +++++---
 .../workspacecodex/archive_explicit_test.go        |  25 ++-
 4 files changed, 312 insertions(+), 37 deletions(-)

### workspace

Path: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-28-archive-native-watchers/workspace`
Base: `6e131813ed455b2335a9287be760877d3242fd9d`
Head: `afc2c144c7cea241b71ff425b5a455a1db060c15`

```
afc2c144c Select runtime with native watcher archive shutdown fix
5c66c3519 Plan native watcher archive shutdown correction
8b44cacea Record active native watcher archive failure investigation
7ddb53b90 Record workspace update investigation scope
82ae1f3d6 workspace: archive 2026-10-28-release-versioning-audit
abdc82d25 Track HaveAPI release versioning correction
```

.../2026-10-28-release-versioning-audit/design.md  | 228 +++++++++++++++++
 .../implementation-evidence.md                     | 282 +++++++++++++++++++++
 .../integration.md                                 |  76 ++++++
 .../2026-10-28-release-versioning-audit/plan.md    |  83 ++++++
 .../2026-10-28-release-versioning-audit/portal.yml |  22 ++
 .../review-packet.md                               | 105 ++++++++
 .../2026-10-28-release-versioning-audit/review.md  |  62 +++++
 .../2026-10-28-release-versioning-audit/state.md   | 133 ++++++++++
 flake.lock                                         |   8 +-
 flake.nix                                          |   2 +-
 .../2026-10-28-archive-active-native-watcher.md    |  22 ++
 work/2026-10-28-archive-native-watchers/design.md  |  45 ++++
 work/2026-10-28-archive-native-watchers/plan.md    |  44 ++++
 work/2026-10-28-archive-native-watchers/portal.yml |   5 +
 work/2026-10-28-archive-native-watchers/state.md   |  39 +++
 .../findings.md                                    | 114 +++++++++
 .../plan.md                                        |  47 ++++
 .../portal.yml                                     |   5 +
 .../state.md                                       |  66 +++++
 work/2026-10-28-workspace-deploy-speed/plan.md     |  28 ++
 work/2026-10-28-workspace-deploy-speed/portal.yml  |  13 +
 work/2026-10-28-workspace-deploy-speed/state.md    |  31 +++
 22 files changed, 1455 insertions(+), 5 deletions(-)

### vpsfree-cz-configuration

Path: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-28-archive-native-watchers/vpsfree-cz-configuration`
Base: `2d6837f0b9582bbd812ecccf6cd59b5685029e0a`
Head: `2c738ac851f43545272579a96cf836f99876eefb`

```
2c738ac8 inputs: set devWorkspace to db9578e2
```

flake.lock | 6 +++---
 1 file changed, 3 insertions(+), 3 deletions(-)

## Report

Write findings and explicit lane, whole-branch history, migration and consolidation
conclusions to review.md in this tracking directory. You may write only that report
or return it. Identify Blocking/Important/Advisory issues and residual verification
limits. Do not interpret unexecuted rollout as verified or grant merge approval.
