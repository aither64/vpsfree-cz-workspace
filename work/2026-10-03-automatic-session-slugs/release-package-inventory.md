# Final branch inventory

Generated from actual refs after commits. Remote-default-to-head series and committed final diff are the review scope; own deployed/current-master-to-head diffs distinguish this initiative. No default-branch integration authorized.

## codex-web

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-03-automatic-session-slugs/codex-web`

Remote default/base: `4c170393a96ed0a6ac2e43488d073f6fcab36132`  
Head: `ca0f3bc980ca99454d000761aeee37b4b9bbafc3`

Complete series:

```text
ca0f3bc980ca99454d000761aeee37b4b9bbafc3 codex: run bounded ephemeral utility turns
```

Final diff: [`codex-web-final.diff`](codex-web-final.diff).

```text
codex/client.go                         |   38 +-
 codex/ephemeral.go                      |  871 +++++++++++++++++++++
 codex/ephemeral_integration_test.go     | 1247 +++++++++++++++++++++++++++++++
 codex/ephemeral_policy.json             |   57 ++
 codex/ephemeral_test.go                 |  623 +++++++++++++++
 docs/reference.md                       |  113 +++
 test/codex_ephemeral_config_contract.py |   67 ++
 test/codex_protocol_contract.py         |  103 ++-
 8 files changed, 3112 insertions(+), 7 deletions(-)
```

## dev-workspace

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-03-automatic-session-slugs/dev-workspace`

Remote default/base: `924c0ec28c41dd8b56aaf17f2212b302ca614899`  
Head: `42be6ee588f5770c4ed324c676b82758b932ba1e`

Complete series:

```text
4ef298b30f9cdbdcfe02bf6526e0f69ecc9bf7b4 runtime: require maintenance-aware cluster transition policy
802b3db0757ddc1e79aacc879842c6d2787a4be7 uploads: reserve initial files for accepted session requests
e6837343b79813d201d0a784eece39a896a55f6e portal: prepare sessions before choosing their names
092ce4206d3af64ed923506a288a05bd5aeceef8 portal: name sessions through the private utility client
34d493ceddc062ae081563b4d9b1dcf706ad79cd nix: pin the ephemeral session naming client
42be6ee588f5770c4ed324c676b82758b932ba1e portal: recover requests while preparing session names
```

Final diff: [`dev-workspace-final.diff`](dev-workspace-final.diff).

```text
docs/codex-package.md                              |   28 +
 docs/session-preparations.md                       |  249 ++++
 docs/workspace-portal.md                           |   50 +-
 flake.lock                                         |    8 +-
 flake.nix                                          |    2 +-
 libexec/dev-session                                |   61 +-
 libexec/workspace-host                             |    2 +-
 nix/workspace-portal.nix                           |    4 +-
 portal/go.mod                                      |    3 +-
 portal/go.sum                                      |    6 +-
 portal/internal/session/authority.go               |   18 +-
 portal/internal/session/runtime-contract.json      |    2 +-
 portal/internal/uploads/preparation_test.go        |  216 ++++
 portal/internal/uploads/store.go                   |  311 +++--
 portal/internal/web/browser_contract_test.cjs      |    1 +
 portal/internal/web/creation.go                    |   82 +-
 portal/internal/web/creation_store.go              |    3 +
 portal/internal/web/preparation.go                 |  888 ++++++++++++++
 .../web/preparation_browser_contract_test.cjs      |  280 +++++
 .../internal/web/preparation_compatibility_test.go |  154 +++
 portal/internal/web/preparation_store.go           |  457 +++++++
 portal/internal/web/preparation_test.go            | 1273 ++++++++++++++++++++
 portal/internal/web/server.go                      |  104 +-
 portal/internal/web/server_test.go                 |    9 +-
 portal/internal/web/session_name.go                |  155 +++
 portal/internal/web/session_namer.go               |   97 ++
 portal/internal/web/session_namer_test.go          |  200 +++
 portal/internal/web/static/app.js                  |  250 ++--
 portal/internal/web/static/creation.js             |   82 +-
 portal/internal/web/static/preparation.js          |  172 +++
 portal/internal/web/templates/creation.html        |   11 +-
 portal/internal/web/templates/index.html           |   29 +-
 portal/internal/web/templates/session.html         |    2 +-
 portal/internal/web/uploads.go                     |   15 +
 test/README.md                                     |   40 +-
 test/creation_browser.cjs                          |  404 ++++---
 test/dev_session/preparation_reservation_test.rb   |  176 +++
 test/dev_session_test.rb                           |    1 +
 test/fixtures/preparation_baseline_test.go         |   66 +
 test/preparation_compatibility.sh                  |   17 +
 test/workspace_host/profile_transition_test.rb     |  144 +++
 41 files changed, 5638 insertions(+), 434 deletions(-)
```

Own incoming base: `4ef298b30f9cdbdcfe02bf6526e0f69ecc9bf7b4`

Own diff: [`dev-workspace-incoming.diff`](dev-workspace-incoming.diff).

## vpsfree-dev-workspace

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-03-automatic-session-slugs/vpsfree-dev-workspace`

Remote default/base: `8f8d8ecf5031c40d3e4a4ee2e9425721fc035800`  
Head: `2e3733ade1bac712f0b852d1960a681e5bca5076`

Complete series:

```text
5b2e9a4bb95bcf4070d62da33b219ed3c5a33f12 flake: require the maintenance-aware runtime transition policy
101d31264fb54cc39b2d0d9519a202d0705a7078 vpsadmin: preserve stopped clusters through maintenance copy
f50c92bf146c3f3d93a5293e0c005f5fdb3a26e2 vpsadmin: preserve assignments in the development storage profile
399c33023a568a8d7a21e4e4df52829628720a28 vpsadmin: test retained services through interrupted maintenance
2e3733ade1bac712f0b852d1960a681e5bca5076 flake: select automatic session naming runtime
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

Remote default/base: `1fa9c982b866a305bd1451f2c32f6d387d2dc1a3`  
Head: `f5d30e291929bdf771f0d3842b84db1f08640131`

Complete series:

```text
4123553c1ae1fc47767e9b30445ff4f7f79266e9 Record infra monitoring investigation and policy proposal
c9366959fd4a5deea5a8205b73044091951dc597 Track automatic portal session slug implementation
d863cc6447c53088e2b9458d3fbb4dc6360b55b0 tracking: record verified infra monitoring branch
fbd5f8245fb87a254533ae0e6893078b383ce728 Plan investigation of newadmin OAuth API exception
b9c2ef2b51b66c898ee073a958581d3ac36c4bc7 work: plan newadmin probe fix and warning alerts
8bd7c4e7d756a4fe2db860a72bf19c020425060b Record API specs workflow optimization investigation
ad539340b25786bf5cac11fa9c968144c417d1bd Record API specs timing evidence and parallelization proposal
f5d30e291929bdf771f0d3842b84db1f08640131 flake: select automatic portal session names
```

Final diff: [`workspace-final.diff`](workspace-final.diff).

```text
flake.lock                                         |  24 +-
 flake.nix                                          |   2 +-
 ...26-10-03-add-members-to-retained-solo-roster.md |  15 +
 .../2026-10-03-retained-member-nix-checks.md       |  26 ++
 work/2026-10-03-api-specs-optimization/design.md   | 442 +++++++++++++++++++++
 .../investigation.md                               | 165 ++++++++
 work/2026-10-03-api-specs-optimization/plan.md     |  52 +++
 work/2026-10-03-api-specs-optimization/portal.yml  |  19 +
 .../review-packet.md                               |  54 +++
 work/2026-10-03-api-specs-optimization/state.md    |  67 ++++
 .../timing-summary.json                            | 170 ++++++++
 work/2026-10-03-automatic-session-slugs/plan.md    | 119 ++++++
 work/2026-10-03-automatic-session-slugs/state.md   |  69 ++++
 .../architect-result.md                            |  57 +++
 .../branch-inventory.md                            |  52 +++
 .../central-builds-result.json                     |  39 ++
 work/2026-10-03-infra-monitoring/design.md         | 390 ++++++++++++++++++
 .../implementation-check-request.md                |  56 +++
 .../implementation-result.md                       | 181 +++++++++
 work/2026-10-03-infra-monitoring/plan.md           |  77 ++++
 work/2026-10-03-infra-monitoring/portal.yml        |  31 ++
 .../quick-checks-2-result.json                     |  40 ++
 .../quick-checks-result.json                       |  20 +
 .../r1-check-result.json                           |  16 +
 work/2026-10-03-infra-monitoring/review-packet.md  | 100 +++++
 work/2026-10-03-infra-monitoring/review.md         | 126 ++++++
 work/2026-10-03-infra-monitoring/state.md          |  97 +++++
 work/2026-10-03-infra-monitoring/verification.md   |  77 ++++
 work/2026-10-03-newadmin-exception/plan.md         |  46 +++
 work/2026-10-03-newadmin-exception/state.md        |  48 +++
 work/2026-10-03-newadmin-http-check/plan.md        |  83 ++++
 work/2026-10-03-newadmin-http-check/portal.yml     |  13 +
 work/2026-10-03-newadmin-http-check/state.md       | 120 ++++++
 33 files changed, 2880 insertions(+), 13 deletions(-)
```

Own incoming base: `ad539340b25786bf5cac11fa9c968144c417d1bd`

Own diff: [`workspace-incoming.diff`](workspace-incoming.diff).

## Final history and migration disposition

The related independent review in recovery-review.md covered all20complete
base-to-head commits and exact final/incoming diffs. The only later source
change is the reviewer-requested checked GET snapshot, directly inspected
and focused-tested under mandatory step9; its temporaryb45bb08 commit was
folded into owning backende683734 without changing tested tree6b4520e.
Adapter/dependency/frontend patches remain unchanged apart from parent IDs.
Runtime preserves exact deployed4ef298b; extension preserves all four already
consumed maintenance/storage ancestors through399c3302. Final consumers each
have one pin update, no repeated fixes or obsolete unapplied approaches.

No incoming database migrations, namespace conversions or state-root changes.
No transitional migrations. Preparation schema1, receipt1/2/3, catalog1 and
unchanged authority/journal/manifest contracts are retained. Existing deployed
policy2-to3 and storage/bootstrap lineage is preserved, not rewritten.
No new extension host-migration VM trigger; normal host/path checks required.
