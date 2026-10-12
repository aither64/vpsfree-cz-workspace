# Inset Reveal: final review packet

Initiative: 2026-10-11-cluster-controls. Tracking is under work/2026-10-11-cluster-controls;
plan.md, design.md and state.md describe the accepted design. All feature worktrees
are under worktrees/2026-10-11-cluster-controls. Branch: 2026-10-11-cluster-controls.

## Requested result and bounds

User approved a toolbar beside cluster state/readiness with normal retained Start,
Stop and confirmed Release; existing copy icon and Reveal/Hide icons; Copy aligned
across credentials. The follow-up explicitly embeds Reveal within secret inputs
and removes external blank placeholders from plain credentials and commands.
Input and Copy are the two outer columns. The eye remains keyboard accessible,
secret text has right padding, and hidden-password Copy is unchanged. Desktop,
mobile and long values are accepted requirements. No initialization/rebuild UI,
new visual framework, API/state/schema changes or default-branch integration.
The user approved implementation and aitherdev deployment.

## Risk, review policy and ownership

High overall risk because the complete deliverable includes secrets, destructive
Release, cross-project controls, deployment and retained disks. Apply General,
Architecture/repetition, Scope/proportionality and Risk/compatibility lanes.
Read mandatory-change-review/SKILL.md and all four references. Remote clients
are untrusted; local operator is trusted under generic repository AGENTS.
The parent authored the change. No native lead/retained roster exists (team list
refuses). Previous standalone /root/final_review is absent from the live tree,
so its identity/settings cannot be validated or assigned a new turn. Replace it
with a fresh installed-catalog reviewer, GPT-6 Astra/xhigh, fork_turns none.
Installed policy catalog digest 437585347ac8b2cdbf498a169d8871e684f3f61ccf1dd48e8589d79ef9629abd,
published catalog file SHA-256 abc80df4cd14ba74a26f9de1f807b6f2a49f2b9651aea7acbbb70d9a2e5fe7bc,
lead_reviewed/reviewer role, purpose review, access read_only. Native role identity
dw_34bb6a768d6175719d13cda28b7adc221b586314b3fc5167. Tool API exposes
model/effort but no native role-file or sandbox selector: follow read-only policy;
do not claim native TOML loading or enforced read-only access.

## History and migrations

Inventory below gives the complete remote-default merge-base series and final
diff statistics; workspace also has a narrower feature comparison against shared
local master. Inspect actual final diffs with git diff BASE HEAD in each worktree.
The workspace historical registration base is 0c827576..., but its final feature
branch was rebased onto current shared master 64a39659...; tracking ancestors are
coordination records, not feature changes. No migrations in any affected project:
none merged, released, deployed or externally consumed. Persisted formats remain
unchanged. Previous deployed runtime bc6b841 is ancestor of 60c679c; extension
7157c80 is unchanged. Inset Reveal is a later user-approved presentation refinement
of the already deployed credential controls. Independently assess whether the
functional split is justified or obsolete branch history should be consolidated.

Repeated pin streams: configuration dev-workspace/devWorkspace and workspace
nested vpsfree-dev-workspace/dev-workspace each now have one final update selecting
60c679c. Workspace extension source has one final update selecting 7157c80 in the
same composed-selection commit. Superseded primary pin commits 4d0ff7c and 7c226d3
were removed by regeneration from their bases. Exact deployed sources are retained
and published as 2026-10-11-cluster-controls-rollout-1 in configuration/workspace;
rollout.md holds execution provenance. Publication/deployment is not claimed as
an exemption to pin consolidation. Generic prior functional commits remain ancestors
needed by the deployed-source reference. No intermediate pin commit remains in
these final feature series. Require explicit whole-branch history, pin-stream and
migration conclusions, independently checking these dispositions.

## Interfaces and consumers

Generic runtime owns template/CSS/browser event delegates, HTTP cluster controls,
and opt-in package provider controls contract. The site extension supplies vpsadmin
and vpsadminos status, retained start and controls catalog. Consumers discovered
from the workspace direct nested source and configuration devWorkspace host-module
input. Both final locks select the same generic runtime; extension source, sibling
nodes and follows paths preserved. Config does not install the user application.
Current inset follow-up changes only generic template/CSS/browser fixture and its
portal guide; no extension or backend code changes.

## Documentation, compatibility and deployment

Generic docs/workspace-portal.md owns inset credentials, toolbar and provider
contract. Extension dev-clusters/{vpsadmin,vpsadminos}/README.md owns retained Start.
Operational evidence remains in session rollout.md and verification.md; reusable
lessons under notes/. Inspect final documentation placement and wording.
No state/schema/catalog/protocol/migration change in inset follow-up. Existing
selectors/events survive nested input markup. Initial backend mixed-provider and
retained-disk compatibility was independently reviewed and verified. Package
switches remain forward-only with ordinary generation/ownership checks, not
rollback to older workspace software. Build matching aitherdev configuration,
dry activate and switch with health checks, then update application user profile
from exact composed workspace feature source. Check authenticated assets and
user services. No archive/delete/merge authorized.

## Verification

Quick committed generic checks passed: node --check browser fixture; git diff
--check; focused Go TestSessionPageGroupsClusterServicesAndRepositoryRevisionState
and TestBrowserClientShipsMessageAndLifecycleInteractions (-mod=readonly).
Config Overcommit Nixfmt and commit-message hooks passed (generated width warning
retained). Semantic lock check: only dev-workspace and vpsfree-dev-workspace in
workspace and devWorkspace in configuration changed from their bases. Final
bin/check-dev-workspace-deployment passed at 60c679c (both final worktrees).
Original rollout: both browsers, all flake checks, provider smoke, CI, host/profile
switch and real Stop/Start known-file retention + Release passed; historical
review.md/review-packet.md describe that evidence. The new browser fixture/package
checks and new deployment have not started; review gates them. Updated browser
scenario adds 1280/375 widths, long secret, uniform gaps, inset bounds/padding and
keyboard Space reveal + Copy, retaining existing behavior/error checks.

## Final branch inventory

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

Feature comparison base (shared local master): 64a39659a64b472ca3328620fd2dc8cd11fb9e98
Head: 86d96b2656c89f37cd4d521fb150ebb123efa89c

```text
86d96b2656c89f37cd4d521fb150ebb123efa89c workspace: select cluster toolbar and inset reveal controls
```

```text
flake.lock | 16 ++++++++--------
 flake.nix  |  4 ++--
 2 files changed, 10 insertions(+), 10 deletions(-)
```

Remote origin/master merge-base: 0c82757629b48cef93df2c98677c07f5a9ba5059

This complete series also includes pre-existing shared master coordination commits.
They are not inset feature commits; 712141b8 is foreign tracking inherited from
shared master. The mandated workspace rebase retained that shared ancestry.

```text
1deacf09fc7b5a305563ea38bef4d897b9f993bd work: plan cluster toolbar and credential controls
712141b811e26b63281d713248842207d16963cc work: diagnose missing HaveAPI documentation in API alert
64a39659a64b472ca3328620fd2dc8cd11fb9e98 work: hand off deployed cluster controls
86d96b2656c89f37cd4d521fb150ebb123efa89c workspace: select cluster toolbar and inset reveal controls
```

```text
flake.lock                                         |  16 +-
 flake.nix                                          |   4 +-
 .../2026-10-11-cluster-control-test-environment.md |  20 +++
 .../2026-10-11-user-service-owner-group.md         |  16 ++
 .../2026-10-11-noninteractive-host-build.md        |   9 ++
 .../2026-10-12-live-devcluster-readiness.md        |  24 +++
 work/2026-10-11-cluster-controls/design.md         |  76 ++++++++++
 work/2026-10-11-cluster-controls/final-heads.md    |  47 ++++++
 work/2026-10-11-cluster-controls/plan.md           |  80 ++++++++++
 work/2026-10-11-cluster-controls/portal.yml        |  39 +++++
 work/2026-10-11-cluster-controls/review-packet.md  | 155 +++++++++++++++++++
 work/2026-10-11-cluster-controls/review.md         | 151 +++++++++++++++++++
 work/2026-10-11-cluster-controls/rollout.md        | 108 ++++++++++++++
 work/2026-10-11-cluster-controls/state.md          | 164 +++++++++++++++++++++
 work/2026-10-11-cluster-controls/verification.md   |  65 ++++++++
 .../findings.md                                    | 101 +++++++++++++
 .../plan.md                                        |  58 ++++++++
 .../portal.yml                                     |  15 ++
 .../state.md                                       |  89 +++++++++++
 19 files changed, 1227 insertions(+), 10 deletions(-)
```
