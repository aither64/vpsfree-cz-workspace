# Committed branch inventory

Generated from actual refs after commits. Remote-default-to-head series and committed final diff are the review scope; own deployed/current-master-to-head diffs distinguish this initiative. No default-branch integration authorized.

## codex-web

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-03-automatic-session-slugs/codex-web`

Remote default/base: `4c170393a96ed0a6ac2e43488d073f6fcab36132`  
Head: `de874bc39553f8955cecdfaaeb4216959b40bd3c`

Complete series:

```text
de874bc39553f8955cecdfaaeb4216959b40bd3c codex: run bounded ephemeral utility turns
```

Final diff: [`codex-web-final.diff`](codex-web-final.diff).

```text
codex/client.go                            |   38 +-
 codex/ephemeral.go                         |  940 ++++++++
 codex/ephemeral_integration_test.go        | 3473 ++++++++++++++++++++++++++++
 codex/ephemeral_policy.json                |   57 +
 codex/ephemeral_test.go                    |  847 +++++++
 codex/testdata/ephemeral-models.json       | 1613 +++++++++++++
 codex/testdata/ephemeral-models.provenance |    5 +
 docs/reference.md                          |  184 ++
 test/codex_ephemeral_config_contract.py    |   67 +
 test/codex_protocol_contract.py            |  107 +-
 10 files changed, 7324 insertions(+), 7 deletions(-)
```

## dev-workspace

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-03-automatic-session-slugs/dev-workspace`

Remote default/base: `924c0ec28c41dd8b56aaf17f2212b302ca614899`  
Head: `87eb917f50986d5206a08b3355837800a03e4529`

Complete series:

```text
4ef298b30f9cdbdcfe02bf6526e0f69ecc9bf7b4 runtime: require maintenance-aware cluster transition policy
802b3db0757ddc1e79aacc879842c6d2787a4be7 uploads: reserve initial files for accepted session requests
e6837343b79813d201d0a784eece39a896a55f6e portal: prepare sessions before choosing their names
91ef039477abd3670fa044727229ca44622d95a7 portal: name sessions through an owned utility runtime
53994ef29996fbbb146ee93c394b1dfde29a7fcd nix: pin the ephemeral session naming client
a44186788603f30ec1a59672630633dd4fc375c0 portal: recover requests while preparing session names
1219d9ace75acf72e21ca259fc84643b0531c402 test: serialize member client event recording
87eb917f50986d5206a08b3355837800a03e4529 portal: verify naming child in a managed user service
```

Final diff: [`dev-workspace-final.diff`](dev-workspace-final.diff).

```text
docs/codex-package.md                              |   47 +
 docs/session-preparations.md                       |  294 +++++
 docs/workspace-portal.md                           |   57 +-
 flake.lock                                         |    8 +-
 flake.nix                                          |    3 +-
 libexec/dev-session                                |   61 +-
 libexec/workspace-host                             |    2 +-
 nix/workspace-portal.nix                           |    9 +-
 portal/cmd/workspace-portal/main.go                |   30 +-
 portal/cmd/workspace-portal/naming_runtime.go      |  171 +++
 .../naming_runtime_integration_test.go             | 1367 ++++++++++++++++++++
 portal/cmd/workspace-portal/naming_runtime_test.go |  341 +++++
 portal/go.mod                                      |    3 +-
 portal/go.sum                                      |    6 +-
 portal/internal/session/authority.go               |   18 +-
 portal/internal/session/runtime-contract.json      |    2 +-
 portal/internal/teamruntime/runtime_test.go        |    7 +
 portal/internal/uploads/preparation_test.go        |  216 ++++
 portal/internal/uploads/store.go                   |  311 ++++-
 portal/internal/web/browser_contract_test.cjs      |    1 +
 portal/internal/web/creation.go                    |   82 +-
 portal/internal/web/creation_store.go              |    3 +
 portal/internal/web/preparation.go                 |  888 +++++++++++++
 .../web/preparation_browser_contract_test.cjs      |  280 ++++
 .../internal/web/preparation_compatibility_test.go |  154 +++
 portal/internal/web/preparation_store.go           |  457 +++++++
 portal/internal/web/preparation_test.go            | 1273 ++++++++++++++++++
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
 46 files changed, 7728 insertions(+), 464 deletions(-)
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

Remote default/base: `a51fa51e2e2503ce658003f75b77a5be1ff6c042`  
Head: `725db6717a82524776f1a687ae9ff96515168b79`

Complete series:

```text
725db6717a82524776f1a687ae9ff96515168b79 flake: select automatic portal session names
```

Final diff: [`workspace-final.diff`](workspace-final.diff).

```text
flake.lock | 24 ++++++++++++------------
 flake.nix  |  2 +-
 2 files changed, 13 insertions(+), 13 deletions(-)
```

Own incoming base: `a51fa51e2e2503ce658003f75b77a5be1ff6c042`

Own diff: [`workspace-incoming.diff`](workspace-incoming.diff).

## Disposition and readiness limits

This is a source checkpoint before native verification and final consumer repins,
not release readiness. The provider has one owning helper/test/documentation
unit; obsolete incoming Luna/V8 and empty-file designs are folded away. The
PID fixture correction is folded into that owning unmerged unit; pre-correction
head1be remains in a backup ref. Runtime's narrowly corrected managed fixture
is one verification unit following production and dependency units.

No new migrations. Protected externally consumed runtime4ef and extension399
remain exact ancestors and must not be rewritten; schema1/policy3 and their
maintenance/storage lineage are preserved. New preparation records are additive
version1 files, not modifications of those existing lifecycle/cluster formats.
Final pins, package resources, native/VM/live execution and a final complete
series review remain pending. Default-branch integration is not authorized.

The bases above identify this reviewed source checkpoint. A subsequent owned
tracking-only master commit does not change the reviewed project sources. The
workspace feature must rebase on actual current shared master and recapture its
comparison before the final readiness/integration gate.
