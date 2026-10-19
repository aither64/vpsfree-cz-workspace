# Final branch inventory

Generated from actual refs after commits. Remote-default-to-head series and committed final diff are the review scope; own deployed/current-master-to-head diffs distinguish this initiative. No default-branch integration authorized.

## codex-web

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-03-automatic-session-slugs/codex-web`

Remote default/base: `4c170393a96ed0a6ac2e43488d073f6fcab36132`  
Head: `8db6adfd9511e95db2b8941edee69bfcba6d13ae`

Complete series:

```text
8db6adfd9511e95db2b8941edee69bfcba6d13ae codex: run bounded ephemeral utility turns
```

Final diff: [`codex-web-final.diff`](codex-web-final.diff).

```text
codex/client.go                         |   38 +-
 codex/ephemeral.go                      |  871 +++++++++++++++++
 codex/ephemeral_integration_test.go     | 1557 +++++++++++++++++++++++++++++++
 codex/ephemeral_policy.json             |   57 ++
 codex/ephemeral_test.go                 |  623 +++++++++++++
 docs/reference.md                       |  120 +++
 test/codex_ephemeral_config_contract.py |   67 ++
 test/codex_protocol_contract.py         |  103 +-
 8 files changed, 3429 insertions(+), 7 deletions(-)
```

## dev-workspace

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-03-automatic-session-slugs/dev-workspace`

Remote default/base: `924c0ec28c41dd8b56aaf17f2212b302ca614899`  
Head: `d05e75270a9bed417d07e9be8bc082c906f6846a`

Complete series:

```text
4ef298b30f9cdbdcfe02bf6526e0f69ecc9bf7b4 runtime: require maintenance-aware cluster transition policy
802b3db0757ddc1e79aacc879842c6d2787a4be7 uploads: reserve initial files for accepted session requests
e6837343b79813d201d0a784eece39a896a55f6e portal: prepare sessions before choosing their names
092ce4206d3af64ed923506a288a05bd5aeceef8 portal: name sessions through the private utility client
34d493ceddc062ae081563b4d9b1dcf706ad79cd nix: pin the ephemeral session naming client
ea3175602f819eac47ce043ca29de953dcf46cb5 portal: recover requests while preparing session names
d05e75270a9bed417d07e9be8bc082c906f6846a test: serialize member client event recording
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
 portal/internal/teamruntime/runtime_test.go        |    7 +
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
 test/creation_browser.cjs                          |  424 ++++---
 test/dev_session/preparation_reservation_test.rb   |  176 +++
 test/dev_session_test.rb                           |    1 +
 test/fixtures/preparation_baseline_test.go         |   66 +
 test/preparation_compatibility.sh                  |   17 +
 test/workspace_host/profile_transition_test.rb     |  144 +++
 42 files changed, 5665 insertions(+), 434 deletions(-)
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
Head: `f5d30e291929bdf771f0d3842b84db1f08640131`

Complete series:

```text
f5d30e291929bdf771f0d3842b84db1f08640131 flake: select automatic portal session names
```

Final diff: [`workspace-final.diff`](workspace-final.diff).

```text
flake.lock                                         |   24 +-
 flake.nix                                          |    2 +-
 .../2026-10-03-cached-nix-member-hooks.md          |   24 -
 .../2026-10-03-storage-profile-ar-reader.md        |   20 -
 .../2026-10-03-stored-diff-whitespace.md           |   11 -
 .../api-remote-restore-ci.md                       |   13 -
 work/2026-09-23-storage-redesign/design.md         | 1350 +-------------------
 .../node-rpc-recovery-review.md                    |  402 ------
 work/2026-09-23-storage-redesign/plan.md           |   21 -
 work/2026-09-23-storage-redesign/portal.yml        |    6 -
 work/2026-09-23-storage-redesign/state.md          |  552 +-------
 .../storage-profile-admission-consumer-review.md   |  126 --
 .../storage-profile-admission-review.md            |  193 ---
 .../storage-profile-rebase-review.md               |   26 -
 .../storage-profile-rollout.md                     |  149 +--
 .../api-ci-completion-result.json                  |   36 -
 work/2026-10-03-newadmin-exception/api-final.diff  |  256 ----
 .../api-review-packet.md                           |   89 --
 .../api-specs-60m-completion-result.json           |   52 -
 .../api-specs-retry-result.json                    |    1 -
 .../api-specs-timeout.md                           |   60 -
 .../configuration-build-result.json                |   14 -
 .../configuration-final-build-result.json          |   13 -
 .../configuration-final-outputs.json               |   19 -
 .../configuration-final.diff                       |   19 -
 .../configuration-result.md                        |  461 -------
 .../configuration-review-packet.md                 |   86 --
 .../configuration-updated-build-result.json        |   22 -
 .../configuration-updated-outputs.json             |   16 -
 work/2026-10-03-newadmin-exception/design.md       |  400 ------
 .../environment-result.json                        |    8 -
 .../green-regression-result.json                   |   10 -
 .../implementation-result.md                       |  224 ----
 .../integration-result.json                        |   30 -
 .../pinned-webui-trace.md                          |   28 -
 work/2026-10-03-newadmin-exception/plan.md         |  113 +-
 work/2026-10-03-newadmin-exception/portal.yml      |   53 -
 .../red-regression-result.json                     |    6 -
 .../regression-proof.txt                           |   39 -
 work/2026-10-03-newadmin-exception/review.md       |  179 ---
 work/2026-10-03-newadmin-exception/rollout.md      |   78 --
 work/2026-10-03-newadmin-exception/state.md        |  275 +---
 work/2026-10-03-newadmin-exception/verification.md |  135 --
 43 files changed, 125 insertions(+), 5516 deletions(-)
```

Own incoming base: `a51fa51e2e2503ce658003f75b77a5be1ff6c042`

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


Fixture-review checkpoint: provider8db6adfd consolidates all fixture prerequisite,
diagnostic and supported HTTP-fallback corrections into its original utility
unit; exact final tree4133363d is preserved. Runtimeea317560 folds both creation
browser fixture fixes into their owning frontend unit. d05e7527 retains the
independently reproducible inherited event-recording race fix as a separate
7-line test-only unit. Exact runtime tree d81d7af7 is preserved. Production
provider Go files/policy and runtime application files equal the tested/published
ca0f3bc9/42be6ee5 sources. No new migrations or compatibility paths. Consumer
pins remain at the already-packaged ca/42/2e/f5 composition pending native proof;
then one mechanical pin per consumer will replace the existing pin unit.
