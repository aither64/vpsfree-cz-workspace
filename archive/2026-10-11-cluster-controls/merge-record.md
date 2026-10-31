# Integration record

User approval: "better, merge it", after the four-repository deployed handoff.
Targets are master in dev-workspace, vpsfree-dev-workspace, configuration and
workspace. No archive/delete or unrelated feature integration is authorized.

Final independent review: inset-review.md. Original exact-head verification and
deployment: verification.md and rollout.md. The refreshed upstreams are unchanged.
Generic/extension/configuration final series and diffs exactly match their reviewed
heads. No new migration or repeated pin update; one update per consumer stream.

Workspace rebased from reviewed local feature base 64a39659 onto shared master
ea7d06da (the owned handoff tracking commit). git range-diff reports 86d96b26 =
0ea24610. flake.nix and flake.lock are byte-identical at both heads; the only
new ancestry is coordination evidence. The installed workspace remains its deployed
86d96b26 composition; the exact source is retained/published on rollout-2.
Approval and final review retain their scope under the patch-equivalent rebase
rule. No new substantive design and no affected review lane requires rerun.

## Final pre-merge inventory

### dev-workspace

Base: a8934bdac91c64f66aa3cee26b68df3bcb8c2fc0
Head: 60c679c52c263a0fc7a4b08c5f83a291cfd89191

```text
1c83d28e767c2ea061c7f49759f5ca2485ec2ae3 portal: align credential reveal and copy icons
bc6b841be0bf83ad84f47daa2e0c064f477bdf23 portal: control retained development clusters from the toolbar
60c679c52c263a0fc7a4b08c5f83a291cfd89191 portal: inset credential reveal controls
```

```text
docs/workspace-portal.md                           |  46 +++++++
 portal/internal/cluster/control_test.go            |  85 ++++++++++++
 portal/internal/cluster/status.go                  |  82 +++++++++++-
 portal/internal/cluster/status_test.go             |   4 +-
 portal/internal/web/cluster_control_test.go        |  93 ++++++++++++++
 .../internal/web/cluster_controls_browser_test.cjs | 142 +++++++++++++++++++++
 portal/internal/web/question_browser_test.go       |  28 +++-
 portal/internal/web/server.go                      |  44 ++++++-
 portal/internal/web/server_test.go                 |   4 +-
 portal/internal/web/static/app.js                  |  69 +++++++---
 portal/internal/web/static/style.css               |  14 +-
 portal/internal/web/templates/clusters.html        |  18 ++-
 12 files changed, 589 insertions(+), 40 deletions(-)
```

### vpsfree-dev-workspace

Base: 3e5dc4681b0343ec236c3f3dfc0d6f725577c376
Head: 7157c8098dcf60127aa4df823fab82b4185ad22a

```text
7157c8098dcf60127aa4df823fab82b4185ad22a devcluster: expose retained start and portal control permissions
```

```text
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

Base: decd92fe3926a4a4304c15957b05cc095948f8cc
Head: e65ef2c4cd179dac2d96cfdfe6d6c6967f08d566

```text
e65ef2c4cd179dac2d96cfdfe6d6c6967f08d566 inputs: set devWorkspace to 60c679c5
```

```text
flake.lock | 6 +++---
 1 file changed, 3 insertions(+), 3 deletions(-)
```

### workspace

Base: ea7d06da61194338d30ac9af90022e051b96afc6
Head: 0ea2461032ef6be99d0cf88f38090d3ecc38b4dd

```text
0ea2461032ef6be99d0cf88f38090d3ecc38b4dd workspace: select cluster toolbar and inset reveal controls
```

```text
flake.lock | 16 ++++++++--------
 flake.nix  |  4 ++--
 2 files changed, 10 insertions(+), 10 deletions(-)
```

## Verification and integration

Workspace patch-equivalent rebase quick checks passed: deployment fixture 4 runs/19
assertions, agent instructions 8/144, real deployment contract at60c679c. Fresh
integration target Go rendering/browser-contract tests passed (0.096s), JavaScript
syntax passed. Extension target status cases passed 2 runs/37 assertions and
retained Start cases 2/40. Configuration target composed contract passed.

All four pre-merge comparisons captured. Three independent repositories merged
--ff-only in fresh owned detached target checkouts; shared workspace master merged
--ff-only from its required shared checkout. Independent hash comparisons show
unrelated tracked working-tree and index diffs preserved. Only the intended
flake.nix/lock changed on workspace master. Feature and rollout refs retained.

All four default pushes succeeded, followed by fresh fetch and SSH exact remote
head proof. Generic 60c679c, extension 7157c80, configuration e65ef2c4 and workspace
0ea24610 are their remote master heads. No additional deployment is required for the
workspace tracking-only rebase: effective runtime/extension/config files match the
already verified deployed composition. No archive/delete or session stop.

Configuration initial push was refused by Overcommit's ambient Bundler loader.
The exact push then succeeded through its nix develop with hooks enabled; no
bypass or source correction. Existing environment lesson updated with this result.
Master CI observed by fresh Luna/low utility: runtime38225092025 and extension
38225093076 at their exact integrated source heads; no retry or cancellation.

## Completion

Both exact post-merge master workflows completed successfully:

| Repository | Check run | Exact head | Elapsed |
| --- | --- | --- | --- |
| dev-workspace | [38225092025](https://github.com/aither64/dev-workspace/actions/runs/38225092025) | 60c679c52c263a0fc7a4b08c5f83a291cfd89191 | 12m00s |
| vpsfree-dev-workspace | [38225093076](https://github.com/vpsfreecz/dev-workspace/actions/runs/38225093076) | 7157c8098dcf60127aa4df823fab82b4185ad22a | 15m16s |

Watcher completed; parent checked matching heads and success conclusions. No job
remains running. Configuration and workspace have no Actions workflows; their
composed checks and deployment were verified before integration.

All temporary integration worktrees were removed with ordinary non-force commands.
Registered feature worktrees remain clean and feature/rollout refs are retained.
Every exact final feature head is an ancestor of fetched remote master. Review,
verification, deployment, integration and cleanup are complete with no blocker or
remaining work. The session remains open; no archive, delete or stop was requested.
