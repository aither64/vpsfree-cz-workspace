# Final consuming-pin readiness supplement

Use retained independent reviewer0 with saved settings, no overrides. Read
mandatory-change-review skill and general/risk references, applicable workspace
routes and each affected repository AGENTS.md. Read-only, no source/tracking
edits, nested agents, tests/builds, publication or lifecycle/deployment action.

This supplements completed all-four-lane SDK/runtime whole-branch reviews and
extension general/risk adoption review. Inspect the final cross-project pin
composition and complete inventories below. Do not rerun unaffected design
lanes; there is only mechanical input adoption in workspace/configuration.

## codex-web

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-02-portal-creation-performance/codex-web
Base: d210d3f7cc93981d0ab163b1fcf0718f9587f47e
Exact head: 4c170393a96ed0a6ac2e43488d073f6fcab36132
Complete series:

```text
4c170393a96ed0a6ac2e43488d073f6fcab36132 codex: support database-only thread listing
```

Final diff:

```text
codex/client.go                 |  7 +++++
 codex/client_test.go            | 61 +++++++++++++++++++++++++++++++++++++++++
 docs/reference.md               |  7 +++++
 test/codex_protocol_contract.py |  7 +++++
 4 files changed, 82 insertions(+)
```

## dev-workspace

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-02-portal-creation-performance/dev-workspace
Base: 4bec20165387d567b761e43b11fdeabb096618d7
Exact head: 7e4e62b9f7c785e9fc36b8fd3c75c0f864140c75
Complete series:

```text
dfda7b8fc501c4a6f761f6d5bc8451da3cc853b8 inputs: select database-only Codex thread listing support
bd18b321117ec144d66a06c5662a64004e413ae1 sessions: bypass discovery only for locked fresh creation
7e4e62b9f7c785e9fc36b8fd3c75c0f864140c75 portal: stream initialization stages into creation receipts
```

Final diff:

```text
docs/dev-sessions.md                               |  38 ++-
 docs/workspace-portal.md                           |  42 +++
 flake.lock                                         |   8 +-
 flake.nix                                          |   2 +-
 libexec/dev-session                                | 205 ++++++++++++++-
 nix/workspace-portal.nix                           |   2 +-
 portal/cmd/workspace-portal/main.go                |  71 +++++-
 portal/cmd/workspace-portal/main_creation_test.go  | 125 +++++++++
 portal/go.mod                                      |   2 +-
 portal/go.sum                                      |   4 +-
 portal/internal/creationprogress/progress.go       | 196 ++++++++++++++
 portal/internal/creationprogress/progress_test.go  |  90 +++++++
 portal/internal/teamruntime/runtime.go             |   8 +
 portal/internal/teamruntime/runtime_test.go        |  13 +-
 portal/internal/web/creation.go                    |  57 ++++-
 portal/internal/web/creation_progress_test.go      | 155 +++++++++++
 portal/internal/web/server.go                      |  22 ++
 portal/internal/workspacecodex/client.go           | 278 ++++++++++++++++----
 portal/internal/workspacecodex/client_test.go      |  76 ++++--
 .../workspacecodex/recovery_candidates_test.go     | 284 +++++++++++++++++++++
 test/creation_browser.cjs                          |  11 +
 test/dev_session/creation_progress_test.rb         | 110 ++++++++
 test/dev_session/fork_recovery_test.rb             |  11 +-
 test/dev_session/session_initialization_test.rb    |   5 +-
 test/dev_session/session_recovery_test.rb          |  12 +-
 test/dev_session_test.rb                           |   1 +
 26 files changed, 1708 insertions(+), 120 deletions(-)
```

## vpsfree-dev-workspace

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-02-portal-creation-performance/vpsfree-dev-workspace
Base: c56f981a950ab763b71dc91c59e8b5256d478851
Exact head: c0dad081732dcb10d5df0f276ba358e46bcf3b87
Complete series:

```text
c0dad081732dcb10d5df0f276ba358e46bcf3b87 inputs: select faster portal session creation runtime
```

Final diff:

```text
flake.lock | 16 ++++++++--------
 flake.nix  |  2 +-
 2 files changed, 9 insertions(+), 9 deletions(-)
```

## vpsfree-cz-configuration

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-02-portal-creation-performance/vpsfree-cz-configuration
Base: 028d70b233c5b100fea7f7aa0b945fb8b6d3ec4d
Exact head: dfc1d6e547a798b51b68e32b9ad078addf7faf17
Complete series:

```text
dfc1d6e547a798b51b68e32b9ad078addf7faf17 inputs: set devWorkspace to 7e4e62b9
```

Final diff:

```text
flake.lock | 14 +++++++-------
 1 file changed, 7 insertions(+), 7 deletions(-)
```

## workspace

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-02-portal-creation-performance/workspace
Base: 2557592363bd510c4691e1ac80f25b2008eca7a4
Exact head: 5b0ea6a12cbd63bc2c5e961666564055c7a498f2
Complete series:

```text
5b0ea6a12cbd63bc2c5e961666564055c7a498f2 inputs: select faster portal session creation package
```

Final diff:

```text
flake.lock | 24 ++++++++++++------------
 flake.nix  |  2 +-
 2 files changed, 13 insertions(+), 13 deletions(-)
```

Workspace was cleanly rebased onto current shared master25575923 before its
one functional pin commit. Intervening coordination-only commits are excluded
from the functional inventory and do not change application behavior. Runtime
series deliberately separates SDK pins, fresh/retry routing and progress.
No obsolete/superseded approaches, unmerged follow-up fixes, unused compatibility
paths or migrations remain in any branch. No new schema/migration version has
been merged, released, deployed or externally consumed. All feature refs retained.

Quick checks: SDK wire/schema checks passed; runtime selected Go/60 Ruby624
assertion checks passed before its review. Runtime full exact-head Check CI
37032485966 now passed; SDK full37024785401 passed. Extension exactc0dad081
Check37033746180 running separately, no result claimed. Parent parsed committed
workspace lock and proved only extension/generic/SDK nodes changed; configuration
channel dev-workspace/devWorkspace via confctl --commit changed only generic/SDK
nodes. Active configuration Overcommit checks passed, generated message preserved.
git diff --check passed in owned workspace/config trees. Exact deployment checker
passed canonical aitherdev portal identity and matching generic7e4e62b9. All
Codex0.160/llm-agents/provider/catalog/host-path inputs remain unchanged.

Risk high for runtime state/protocol adoption and deployment sequencing.
Actual owner/contract and consumers are in review-runtime.md and owning
SDK docs/reference.md; generic docs/dev-sessions.md and workspace-portal.md
describe freshness proof, conservative retry and progress. No useful new feature
prose for pure consuming pins. Site rollout is separate rollout.md; design and
prototype briefs remain session records. Advisory no-tools guard was fixed by
architect; parent directly inspected contract/guard and AST/hash (no application
change or scope expansion). Package/timing/fault/live canary checks remain pending.

Workspace application is extension mkPackage with existing concrete site and
Full catalog, deployed only through workspace-host user-profile switch. Config
independently consumes generic host support, selector cz.vpsfree/machines/aitherdev;
no application system pin. Build/check final consuming package and host before
dry-activate/switch, preserve health checks, journals/ownership/idle refusals;
recover software through a newer reverting generation. No schema change, no
Codex upgrade, no projectId, no unsafe retry bypass. No default-branch integration
approval; session remains active.

Report findings and explicit whole-branch history/no-migrations conclusions
for final workspace/configuration branches plus exact cross-project coherence.
Send full report to native lead and repeat in final public output for parent.
