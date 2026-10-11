# Final review packet: cluster controls

Read root AGENTS.md, its mandatory routing procedures and each affected
repository AGENTS.md in full before reviewing. Also read plan.md, design.md
and state.md here. Follow /home/aither/.codex/skills/mandatory-change-review/SKILL.md
and all four lane references: general, architecture, scope, risk.

Outcome: icons in reveal/copy order, fixed copy alignment; visible Start/Stop
and separate destructive Release in toolbar beside Ready. User chose normal
Start (current sources, retained disks/topology/network), visible controls, and
approved implementation/deployment. No merge or archive authorization.

Risk: high (secrets, destruction, long provider operations, cross-project
contracts and live deployment). Local workspace operator is trusted per both
repository AGENTS; remote browser clients are untrusted. Review validation,
lifecycle/generation admission, concurrency, maintenance and data preservation.
Do not invent resistance to a compromised trusted local operator.

Review selection: no retained roster (shell session has no valid lead Codex
thread). Installed default development team lead_reviewed, lexicographically
first review-purpose role reviewer: GPT-6 Astra, xhigh, read-only, fresh context.
Native identity dw_34bb6a768d6175719d13cda28b7adc221b586314b3fc5167;
config /home/aither/.local/state/dev-workspaces/profile/share/dev-workspace/agent-teams/lead_reviewed/reviewer-xhigh.toml.
Verify these settings/catalog and report identity. No nested agents or edits.

Quick checks passed: work/2026-10-11-cluster-controls/quick-checks-3.log
and status 0. Go internal/cluster and selected internal/web behavior/contract
tests; JS syntax; Ruby status 2 runs/37 assertions and start 2 runs/40 assertions;
bash syntax and diff checks. Composed deployment contract passed with exact
runtime 74b2dc1079610182e8dde8b8cf81dc555152484c. Config hooks passed with
generated message width warning retained. Long package/browser checks not started.

Contract owner: generic portal docs/workspace-portal.md. Actual consumers:
its configured providers and vpsFree extension helpers, extension mkPackage
consumed by workspace flake, matching generic host module consumed by config.
Status actions opt-in, missing means legacy Release-only; ordinary CLI output
unchanged. Start --existing is additive and reads retained selection under lock.
Portal POST routes select configured kind, no arbitrary commands. Provider
locks nonblocking only for portal. Archive reset remains ordinary locked path.
No database/schema/persisted-format changes or migrations in any repository:
no versions merged, released, deployed or externally consumed. New code has
not yet deployed. Older/newer combinations are intentionally supported.

Documentation: generic docs/workspace-portal.md and both provider README.md.
Design and temporary rollout records stay in initiative. No KB content changes.
Non-goals: first-time creation, force, rebuild controls, topology editing,
maintenance bypass, session cleanup, CI modifications, master integration.

Commits separate credential UI, generic controls, provider contract, composed
workspace pins and host module pin. Tests/docs bundled with owning behavior;
shared browser scenario tests both requested UI pieces because they share the
same real card fixture. No superseded functional designs or follow-up fix
commits remain. Each pin stream has one final update; no intermediate pins.
Extension selection advances from 0ff827 to its current master 3e5dc46 (review
procedure documentation only) plus feature 7157c80. No sibling input changes.

Explicitly conclude whole-branch history/consolidation, migration lineage
(no migrations), mixed-version safety, each lane and remaining verification
gaps. Save report to this initiative's review.md only; read-only application
source. Do not run long tests or approve deployment.

## Branch inventory

### dev-workspace

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-11-cluster-controls/dev-workspace
Base (origin/master merge-base): a8934bdac91c64f66aa3cee26b68df3bcb8c2fc0
Head: 74b2dc1079610182e8dde8b8cf81dc555152484c

```
1c83d28e767c2ea061c7f49759f5ca2485ec2ae3 portal: align credential reveal and copy icons
74b2dc1079610182e8dde8b8cf81dc555152484c portal: control retained development clusters from the toolbar
```

Final diff: dev-workspace.diff

```
docs/workspace-portal.md                           |  45 ++++++++
 portal/internal/cluster/control_test.go            |  85 ++++++++++++++++
 portal/internal/cluster/status.go                  |  82 ++++++++++++++-
 portal/internal/cluster/status_test.go             |   4 +-
 portal/internal/web/cluster_control_test.go        |  93 +++++++++++++++++
 .../internal/web/cluster_controls_browser_test.cjs | 113 +++++++++++++++++++++
 portal/internal/web/question_browser_test.go       |  28 ++++-
 portal/internal/web/server.go                      |  44 +++++++-
 portal/internal/web/server_test.go                 |   2 +-
 portal/internal/web/static/app.js                  |  69 +++++++++----
 portal/internal/web/static/style.css               |  12 ++-
 portal/internal/web/templates/clusters.html        |  18 +++-
 12 files changed, 556 insertions(+), 39 deletions(-)
```

### vpsfree-dev-workspace

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-11-cluster-controls/vpsfree-dev-workspace
Base (origin/master merge-base): 3e5dc4681b0343ec236c3f3dfc0d6f725577c376
Head: 7157c8098dcf60127aa4df823fab82b4185ad22a

```
7157c8098dcf60127aa4df823fab82b4185ad22a devcluster: expose retained start and portal control permissions
```

Final diff: vpsfree-dev-workspace.diff

```
dev-clusters/lib/runtime.sh            | 48 +++++++++++++++++++++++++++++++++-
 dev-clusters/vpsadmin/README.md        | 21 +++++++++++++++
 dev-clusters/vpsadmin/bin/devcluster   | 11 +++++++-
 dev-clusters/vpsadminos/README.md      | 14 ++++++++++
 dev-clusters/vpsadminos/bin/devcluster | 11 +++++++-
 test/devcluster_commands_test.rb       | 45 +++++++++++++++++++++++++++++++
 test/devcluster_status_test.rb         | 23 ++++++++++++++--
 7 files changed, 168 insertions(+), 5 deletions(-)
```

### vpsfree-cz-configuration

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-11-cluster-controls/vpsfree-cz-configuration
Base (origin/master merge-base): decd92fe3926a4a4304c15957b05cc095948f8cc
Head: 04039ba97fbbdb56911a40e3b31e0994cbebda7d

```
04039ba97fbbdb56911a40e3b31e0994cbebda7d inputs: set devWorkspace to 74b2dc10
```

Final diff: vpsfree-cz-configuration.diff

```
flake.lock | 6 +++---
 1 file changed, 3 insertions(+), 3 deletions(-)
```

### workspace

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-11-cluster-controls/workspace
Base (origin/master merge-base): 0c82757629b48cef93df2c98677c07f5a9ba5059
Head: 72a2876bdefd6e64796fddd1047920716428af06

```
1deacf09fc7b5a305563ea38bef4d897b9f993bd work: plan cluster toolbar and credential controls
72a2876bdefd6e64796fddd1047920716428af06 workspace: select cluster toolbar and retained-start controls
```

Final diff: workspace.diff

```
flake.lock                                  | 16 +++---
 flake.nix                                   |  4 +-
 work/2026-10-11-cluster-controls/plan.md    | 80 +++++++++++++++++++++++++++++
 work/2026-10-11-cluster-controls/portal.yml |  5 ++
 work/2026-10-11-cluster-controls/state.md   | 55 ++++++++++++++++++++
 5 files changed, 150 insertions(+), 10 deletions(-)
```

Workspace was rebased onto current local shared master. 1deacf09 is the required initial tracking-only plan/state/manifest commit already on shared master; it is not functional feature history.
