# Final branch inventory

Generated from actual refs after commits. Remote-default-to-head series and committed final diff are the review scope; own deployed/current-master-to-head diffs distinguish this initiative. No default-branch integration authorized.

## codex-web

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-03-automatic-session-slugs/codex-web`

Remote default/base: `4c170393a96ed0a6ac2e43488d073f6fcab36132`  
Head: `32775fa7fdd9bc9b41aef74b7f195e5c3bc0f8d5`

Complete series:

```text
32775fa7fdd9bc9b41aef74b7f195e5c3bc0f8d5 codex: run bounded ephemeral utility turns
```

Final diff: [`codex-web-final.diff`](codex-web-final.diff).

```text
codex/client.go                            |   38 +-
 codex/ephemeral.go                         |  940 +++++++
 codex/ephemeral_integration_test.go        | 3811 ++++++++++++++++++++++++++++
 codex/ephemeral_policy.json                |   57 +
 codex/ephemeral_test.go                    |  847 +++++++
 codex/testdata/ephemeral-models.json       | 1613 ++++++++++++
 codex/testdata/ephemeral-models.provenance |    5 +
 docs/reference.md                          |  189 ++
 test/codex_ephemeral_config_contract.py    |   67 +
 test/codex_protocol_contract.py            |  107 +-
 10 files changed, 7667 insertions(+), 7 deletions(-)
```

## dev-workspace

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-03-automatic-session-slugs/dev-workspace`

Remote default/base: `924c0ec28c41dd8b56aaf17f2212b302ca614899`  
Head: `45d4f13ab14a2dd7d19ea564dc1d364c5ac155c6`

Complete series:

```text
4ef298b30f9cdbdcfe02bf6526e0f69ecc9bf7b4 runtime: require maintenance-aware cluster transition policy
89fb1b07fe0e787801d4e15964ea190f4ed884e7 uploads: reserve initial files for accepted session requests
ea5b2e98c91f1257c2406559f7c3a3f4ad125552 portal: prepare sessions before choosing their names
81e88cb9a7e4f6ad4d2bc5d832efaf297708304f portal: name sessions through an owned utility runtime
8cb615a8e16bd61da429ef6702b8fd09bc66fff8 nix: pin the ephemeral session naming client
376748c4f7f771a3cfdf9bfa84b3eb9dee1c6ac0 portal: recover requests while preparing session names
59caed4f2796a78ed1cc48cc513cbbcaaa59bd3b test: serialize member client event recording
45d4f13ab14a2dd7d19ea564dc1d364c5ac155c6 portal: verify naming child in a managed user service
```

Final diff: [`dev-workspace-final.diff`](dev-workspace-final.diff).

```text
docs/codex-package.md                              |   49 +
 docs/session-preparations.md                       |  300 +++++
 docs/workspace-portal.md                           |   57 +-
 flake.lock                                         |    8 +-
 flake.nix                                          |    3 +-
 libexec/dev-session                                |   61 +-
 libexec/workspace-host                             |    2 +-
 nix/workspace-portal.nix                           |    9 +-
 portal/cmd/workspace-portal/main.go                |   30 +-
 portal/cmd/workspace-portal/naming_runtime.go      |  171 +++
 .../naming_runtime_integration_test.go             | 1367 ++++++++++++++++++++
 portal/cmd/workspace-portal/naming_runtime_test.go |  360 ++++++
 portal/go.mod                                      |    5 +-
 portal/go.sum                                      |    6 +-
 portal/internal/session/authority.go               |   18 +-
 portal/internal/session/runtime-contract.json      |    2 +-
 portal/internal/teamruntime/runtime_test.go        |    7 +
 portal/internal/uploads/preparation_test.go        |  296 +++++
 portal/internal/uploads/store.go                   |  317 ++++-
 portal/internal/web/browser_contract_test.cjs      |    1 +
 portal/internal/web/creation.go                    |   82 +-
 portal/internal/web/creation_store.go              |    3 +
 portal/internal/web/preparation.go                 |  888 +++++++++++++
 .../web/preparation_browser_contract_test.cjs      |  280 ++++
 .../internal/web/preparation_compatibility_test.go |  154 +++
 portal/internal/web/preparation_store.go           |  457 +++++++
 portal/internal/web/preparation_test.go            | 1365 +++++++++++++++++++
 portal/internal/web/server.go                      |  156 ++-
 portal/internal/web/server_test.go                 |    9 +-
 portal/internal/web/session_name.go                |  155 +++
 portal/internal/web/session_namer.go               |   98 ++
 portal/internal/web/session_namer_test.go          |  254 ++++
 portal/internal/web/static/app.js                  |  250 ++--
 portal/internal/web/static/creation.js             |   82 +-
 portal/internal/web/static/preparation.js          |  172 +++
 portal/internal/web/templates/creation.html        |   11 +-
 portal/internal/web/templates/index.html           |   29 +-
 portal/internal/web/templates/session.html         |    2 +-
 portal/internal/web/uploads.go                     |   15 +
 test/README.md                                     |   40 +-
 test/creation_browser.cjs                          |  424 +++---
 test/dev_session/preparation_reservation_test.rb   |  176 +++
 test/dev_session_test.rb                           |    1 +
 test/fixtures/preparation_baseline_test.go         |   66 +
 test/preparation_compatibility.sh                  |   17 +
 test/workspace_host/profile_transition_test.rb     |  144 +++
 46 files changed, 7934 insertions(+), 465 deletions(-)
```

Own incoming base: `4ef298b30f9cdbdcfe02bf6526e0f69ecc9bf7b4`

Own diff: [`dev-workspace-incoming.diff`](dev-workspace-incoming.diff).

## vpsfree-dev-workspace

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-03-automatic-session-slugs/vpsfree-dev-workspace`

Remote default/base: `8f8d8ecf5031c40d3e4a4ee2e9425721fc035800`  
Head: `67c9a60b802537bbb7154959405b67f168f85397`

Complete series:

```text
5b2e9a4bb95bcf4070d62da33b219ed3c5a33f12 flake: require the maintenance-aware runtime transition policy
101d31264fb54cc39b2d0d9519a202d0705a7078 vpsadmin: preserve stopped clusters through maintenance copy
f50c92bf146c3f3d93a5293e0c005f5fdb3a26e2 vpsadmin: preserve assignments in the development storage profile
399c33023a568a8d7a21e4e4df52829628720a28 vpsadmin: test retained services through interrupted maintenance
67c9a60b802537bbb7154959405b67f168f85397 flake: select automatic session naming runtime
```

Final diff: [`vpsfree-dev-workspace-final.diff`](vpsfree-dev-workspace-final.diff).

```text
dev-clusters/lib/devcluster_runner.rb              |  49 +-
 dev-clusters/vpsadmin/README.md                    | 278 ++++++++
 dev-clusters/vpsadmin/bin/devcluster               | 335 +++++++++-
 dev-clusters/vpsadmin/lib/devcluster-runner.rb     |   4 +-
 dev-clusters/vpsadmin/lib/maintenance.rb           | 631 ++++++++++++++++++
 dev-clusters/vpsadmin/lib/storage_profile.rb       | 585 +++++++++++++++++
 .../vpsadmin/nix/storage-profile-provision.rb      | 156 +++++
 dev-clusters/vpsadmin/nix/storage-profile.nix      | 120 ++++
 .../vpsadmin/nix/storage-profile/config.rb         |   6 +
 .../vpsadmin/nix/storage-profile/dataset_plans.rb  |   4 +
 dev-clusters/vpsadmin/nix/storage-profile/hooks.rb |   4 +
 dev-clusters/vpsadmin/nix/test.nix                 | 239 +++++--
 .../tests/run-storage-profile-api-specs.sh         |  22 +
 .../vpsadmin/tests/storage-profile-acceptance.rb   | 593 +++++++++++++++++
 flake.lock                                         |  16 +-
 flake.nix                                          |  25 +-
 nix/tests/retained-services-maintenance.nix        | 235 +++++++
 test/devcluster_commands_test.rb                   | 198 ++++++
 test/devcluster_maintenance_test.rb                | 357 +++++++++++
 test/devcluster_nix_smoke.rb                       |  67 +-
 test/devcluster_runner_test.rb                     | 122 ++++
 test/devcluster_status_test.rb                     |  38 ++
 test/devcluster_storage_profile_test.rb            |  64 ++
 .../devcluster-runner.rb                           | 508 +++++++++++++++
 test/vpsadmin_storage_profile_spec.rb              | 707 +++++++++++++++++++++
 25 files changed, 5292 insertions(+), 71 deletions(-)
```

Own incoming base: `399c33023a568a8d7a21e4e4df52829628720a28`

Own diff: [`vpsfree-dev-workspace-incoming.diff`](vpsfree-dev-workspace-incoming.diff).

## workspace

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-03-automatic-session-slugs/workspace`

Remote default/base: `a51fa51e2e2503ce658003f75b77a5be1ff6c042`  
Head: `8876efbffbb1312c782687226deeac3e7f053749`

Complete series:

```text
5c855f52412b2cf38bc0b998c370557dff76c07e tracking: preserve automatic session slug implementation checkpoint
8876efbffbb1312c782687226deeac3e7f053749 flake: select automatic portal session names
```

Final diff: [`workspace-final.diff`](workspace-final.diff).

```text
flake.lock                                         |   24 +-
 flake.nix                                          |    2 +-
 ...background-workers-and-persistence-baselines.md |   51 +
 .../2026-10-04-code-mode-tool-selection.md         |   33 +
 .../2026-10-04-ephemeral-diagnostic-logging.md     |   31 +
 .../2026-10-04-http-probe-dial-lifetime.md         |   26 +
 .../2026-10-04-native-responses-http-fallback.md   |   26 +
 ...026-10-04-nonempty-instruction-file-contract.md |   21 +
 .../backend-report.md                              |  166 +
 .../binary-identity.json                           |   41 +
 .../branch-inventory.md                            |  206 +
 .../codex-web-final.diff                           | 7449 ++++++++++++++++
 .../control-eligibility.diff                       |  271 +
 .../control-review-packet.md                       |   59 +
 .../control-review.md                              |   34 +
 .../design-report.md                               |  450 +
 work/2026-10-03-automatic-session-slugs/design.md  | 2976 +++++++
 .../dev-workspace-final.diff                       | 9179 ++++++++++++++++++++
 .../dev-workspace-incoming.diff                    | 8956 +++++++++++++++++++
 .../fixed-file-codex-web.diff                      |  550 ++
 .../fixed-file-dev-workspace.diff                  |  195 +
 .../fixed-file-review-packet.md                    |  105 +
 .../fixed-file-review.md                           |  106 +
 .../fixture-provider.diff                          |  504 ++
 .../fixture-review-inventory.md                    |  250 +
 .../fixture-review-packet.md                       |   98 +
 .../fixture-review.md                              |   50 +
 .../fixture-runtime.diff                           |  115 +
 .../frontend-report.md                             |  191 +
 .../implementer-preflight.md                       |  124 +
 .../managed-child-fixture.diff                     | 1373 +++
 .../managed-child-report.md                        |   33 +
 .../managed-child-review-packet.md                 |  114 +
 .../managed-child-review.md                        |   66 +
 .../managed-child-smoke-brief.md                   |  296 +
 .../managed-child-smoke.nix                        |  103 +
 .../native-fixed-file-observation.md               |   74 +
 .../native-http-fallback-plan.md                   |   18 +
 .../native-observation-fixture.diff                |  753 ++
 .../native-observation-review-packet.md            |   63 +
 .../native-observation-review.md                   |   35 +
 .../native-observation.md                          |   49 +
 .../pid-boundary-report.md                         |   34 +
 .../pid-boundary-review-packet.md                  |  135 +
 .../pid-boundary-review.md                         |   60 +
 .../pid-boundary.diff                              |  821 ++
 .../pid-native-observation.md                      |   63 +
 work/2026-10-03-automatic-session-slugs/plan.md    |   91 +-
 work/2026-10-03-automatic-session-slugs/portal.yml |  115 +
 .../recovery-final.diff                            | 1607 ++++
 .../recovery-report.md                             |  126 +
 .../recovery-review-packet.md                      |  172 +
 .../recovery-review.md                             |   66 +
 .../release-package-inventory.md                   |  232 +
 .../review-packet.md                               |  214 +
 .../review-pass1/branch-inventory.md               |  205 +
 .../review-pass1/codex-web-final.diff              | 3225 +++++++
 .../review-pass1/dev-workspace-final.diff          | 5797 ++++++++++++
 .../review-pass1/dev-workspace-incoming.diff       | 5574 ++++++++++++
 .../review-pass1/vpsfree-dev-workspace-final.diff  | 5894 +++++++++++++
 .../vpsfree-dev-workspace-incoming.diff            |   61 +
 .../review-pass1/workspace-final.diff              | 2125 +++++
 .../review-pass1/workspace-incoming.diff           |   83 +
 work/2026-10-03-automatic-session-slugs/review.md  |   85 +
 work/2026-10-03-automatic-session-slugs/rollout.md |   71 +
 .../runtime-base-range-diff.txt                    |    3 +
 .../state-history.md                               | 1102 +++
 work/2026-10-03-automatic-session-slugs/state.md   |  240 +-
 .../static-profile-native-observation.md           |   54 +
 .../static-profile-review-packet.md                |  136 +
 .../static-profile-review.md                       |   50 +
 .../utility-report.md                              |  341 +
 .../verification-plan.md                           |   86 +
 .../verification.md                                |  305 +
 .../verify-live.py                                 |  147 +
 .../vpsfree-dev-workspace-final.diff               | 5894 +++++++++++++
 .../vpsfree-dev-workspace-incoming.diff            |   61 +
 .../workspace-current-master-range-diff.txt        |    1 +
 .../workspace-final.diff                           |   83 +
 .../workspace-incoming.diff                        |   83 +
 80 files changed, 70627 insertions(+), 81 deletions(-)
```

Own incoming base: `5c855f52412b2cf38bc0b998c370557dff76c07e`

Own diff: [`workspace-incoming.diff`](workspace-incoming.diff).

## History and migration disposition

Provider has one final helper/test/docs unit. Superseded incoming Luna/V8 and
empty-instruction-file designs are folded away; the final Direct profile,
nonempty constant, PID boundary and accepted diagnostic row exception enter
that owning unit directly. Runtime keeps uploads, preparation, naming child,
one dependency stream, browser recovery, event-recording fix and managed
verification as focused units. Atomic evidence and prose were folded into the
naming-child unit; exact provider/Go/flake/vendor changes were folded into the
single dependency unit. Extension and workspace each have one pin stream.
No fixup/follow-up cleanup or unused compatibility path remains incoming.
Backups retain prior heads, not extra incoming source commits.

Workspace's remote-default series also contains tracking-only5c855f5, already
on shared local master. It records this initiative's curated evidence and six
owned reusable notes; it adds no functional behavior. Functional final review
base is current shared master5c855f5. The prior workspace pin commit rebased
patch-equivalently (range-diff725=b382) before the final dependency updates32ca/8876;
its incoming diff contains only flake.nix/flake.lock. No shared branch switched,
foreign files/index staged or published master history rewritten.

NO NEW MIGRATIONS. Native SQLite migration0002 is external pinned schema being
inspected, not an incoming conversion. Preparation version1 records are additive
files, with reviewed old-reader/conflict/forward-recovery semantics. Exact
externally consumed runtime4ef298b3 and extension399c3302 remain unchanged
ancestors; inherited schema1/policy3 and maintenance/storage support are retained.
Both consumed heads are published/deployed but unmerged into current defaults,
so their history was preserved rather than rewritten.

All four final feature heads are published over SSH with exact leases, clean
and coherent. Runtime Go module v0.0.0-20261004060753-32775fa7fdd9 and flake pin
select identical provider327; vendorHash sha256-KlckfIvbzTtFvu31Fd5T/GYM/V7Es8Ks7yv/HZwEhOU=.
No committed local module replacement. Tidy removes obsolete old provider sums
and classifies existing managed-tag x/net/html dependency as direct, retaining
versionv0.42.0. Runtime lock changes only codex-web; extension only runtime/provider;
workspace only extension/runtime/provider. All unrelated native/Codex/nixpkgs/
cluster/team/site inputs remain unchanged. Final whole-branch review passed history/pins with one Important R1; its narrow
prevalidation fix is directly verified under step9. Runtime45, extension67 and
workspace8876 supersede the reviewed pins; only the R1 source/tests and generated
pins changed. Package/resource/managedVM, exact-head CI and live MODEL/custom/
replay still gate use.
