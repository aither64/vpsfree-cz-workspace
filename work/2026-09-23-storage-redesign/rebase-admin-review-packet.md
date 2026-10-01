# Final rebased vpsAdmin review packet

HIGH risk; all four mandatory lanes. Retained independent reviewer0 uses saved
GPT-6.1 Sol/xhigh, read-only, no overrides or nested reviewers.

## Goal and scope

Rebase existing advisory storage work onto current default branches and redeploy
this session's disposable storage/bridge cluster with the separate React WebUI.
User authorized resetting this exact cluster. Keep PHP freeze UI; no React freeze
feature, default-branch merge, shared-host deployment, production strict or APPLY.
Architect contract: [design.md](design.md). Rollout record:
[rebase-devcluster-20261001.md](rebase-devcluster-20261001.md).

## Exact inputs and full history

vpsAdmin registered worktree under worktrees/2026-09-23-storage-redesign/vpsadmin.
Base master 90184b374ce0a139319b66326a29373b92d8ee93;
head e65a5a6b0f227f78cdcd40afa6a8de1f5b497b36.
OS published 8d05dc3ae1fb71c1385609990acdf093af49ceec on staging 26f28c691;
OS complete one-commit/no-migrations four-lane review cleared with no findings.
React clean published main aa2f60b89df65d2f987be48784ed42bab7010833 unchanged.
Config guide 603da36e on 029c616e; generated service pin follows after Admin publication.

Complete 19 commits:

```text
3ca86b30bb0f964a9d0f1421c70cf72fd5bae306 storage: establish integrity schema and freeze bootstrap
b867d906dc61cfcdb422d6ddd488a1f1b1e064cd storage: journal observer writes across API and NodeCtld
4eaad0ffe446febe583d1d19c2ece8c69bf95a03 storage: add advisory inventory and reconciliation
77420f06a9de019d576998374f10ec95c0f68862 storage: add authenticated freeze API and WebUI
6ca68942039e6cc1ecfa5d2dfc9af25730292a1c storage: prove strict snapshot dispatch in test mode
57a2826e70ebb539a778edb4651daa645ef5bf88 storage: document integrity evidence and observer limits
6471d0bdd1a3e99b61433d101b41469db3b8cc9d nodectld: observe bounded local storage activity
0f2e53dadc0dee884d20da08b2e9d0d8e53815ec storage: preserve exact GUIDs in signed inventory
f3f53c05c31325cbb0f9bb251fe4688094ef93cf storage: sample node and osctld activity around inventory
8177a2d0e209a31a0239b9d09414ca2125231857 storage: accept capped settled intents in activity reports
e71fd39db179650bdf084a03372a840130f78f65 Distinguish completed rollbacks in DB capture overlap
d04e073156f480bef73d176e41076a2a16fef8f5 Keep storage reconciliation replay cold and offline
320df0fdf391f3871b3939476a820c93cc24814f api: canonicalize captured storage GUID decimals
98350f78696cfcb3bd03947817f64b1fc6459513 storage: version offline coverage conservatively
b4284b8c8b7bc5b16ace035e8a336b23c66efa47 Bound storage reconciler capture to current evidence
64917fadacd5363a58c897b847ba6b83f2b6ffc1 Restore pooled DB isolation after storage capture
107c93ee5a2dfd0b1dc0dd38b3638b78cbaa7bee api: avoid fixture IP address collisions
0bdd6caaa4aadfc16b5f124f16b7b5bb102bc0ed Use the shared transient node exchange for inventory
e65a5a6b0f227f78cdcd40afa6a8de1f5b497b36 flake: vpsadminos 8e44a5124 -> 8d05dc3ae
```

All 18 retained thematic commits are patch/message equivalent to the previously
reviewed/published fa7 series. The obsolete old OS pin was dropped, replaced by one
generated current OS pin from the required tool at the final head. Full non-lock tree equals the
initial clean rebase eade (189 feature blobs equal fa7). Upstream default delta had no
source-path overlap. Do not require removing consumed v1 artifact readers:
sealed v1 captures exist; v2 old readers reject. Published runtime-isolation and
paired transient-exchange fixes remain independently reviewable follow-ups.
No transitional writer, duplicate provider pin or new feature was introduced.

## Migration provenance

Consumed in prior disposable G0/G1a cluster and published feature history; not
merged/released to production. User reset waiver does not erase consumption:

- 20260924210000_add_storage_integrity_foundation.rb, gitblob
  7d929052f314d5a821b2ce65345680c0740b1b0c.
- 20260926100000_add_bounded_storage_capture_indexes.rb, gitblob
  d60868e615024c70fb4b87b736a2466ceb8349db.
- Core schema gitblob e9aa952df7b94451c5491c965d22962265c8f545.

All blobs/versions unchanged. Fresh schema needs singleton bootstrap before
normal seed; old DB upgrades retain epoch and audit. No down-migration rollout.
Inspect full migration history/schema, not only final lock diff.

## Pins, ownership and actual consumers

Final generated pin changes only vpsadminos + its existing nixpkgsUnstable and
nixpkgs_2 lock fields. Input mappings unchanged; verify these exactly match OS 8d05's
current dependency closure. The pin affects Ruby/package/module/test graph.
Provider root UNIX pool_storage_activity/gc_trash_v1 matches signed 5291 consumer;
old/missing versions unknown. Equal samples never prove children or exclusion.
Site vpsadminServices follows separate vpsadminosStaging; internal Admin pin does
not upgrade shared host osctld. No site OS pin switch here.
Installed devcluster provider owns optional React/BFF integration; same-session
path override selects aa2. Packages may embed supported unknown/dirty/unavailable:
match actual frontend/BFF metadata and record separate Git/tree+source/output
provenance. No provenance or React behavior patch is added.

## Quick verification

Initial equivalent rebase: OS 36/0 plus normal hooks, API 62/0, Node 42/0,
PHP 5 tests/17 assertions, selector 18 runs/77 assertions; Ruby syntax passed
for 162 Admin and 12 OS files. Final-pin checks passed at exact e65: three separate migration processes
(4+2+2 examples, zero failures), focused API 74/0, Node 42/0, and all normal
Admin hooks. Logs are private under /tmp/storage-redesign-redeploy-20261001.
Final diff check clean, non-lock parity and migration blobs independently confirmed.

## Documentation and residual acceptance

Reference docs/storage/integrity-{foundation,reconciler}.md and site rollout
guide keep their owning behavior; no source feature changed by rebase. Individual
reset/redeploy decisions belong to the linked session rollout and architect brief.
Current catalog/P/U selector completeness is diagnostic; historical terminal coverage unknown,
node_quiet=false, repair_ready=false, executable=false and APPLY off remain. Existing global
retained-lock cohort throughput risk remains unmeasured; prior 40k lock-free capture at 13.33 seconds
is not a lock fan-out proof. Runtime trial after review proves fresh bootstrap,
actual packages/socket, real React login/API/logout and PHP freeze CAS/auth/admission
plus normal resumption. No production use implied by local checks or this review.

## Final diff inventory

```text
 .github/workflows/api-specs.yml                    |   1 +
 .../workflows/storage-group-snapshot-contract.yml  |  93 +++
 AGENTS.md                                          |  10 +
 api/bin/vpsadmin-storage-reconcile                 |  97 +++
 ...60924210000_add_storage_integrity_foundation.rb | 374 +++++++++
 ...26100000_add_bounded_storage_capture_indexes.rb |  10 +
 api/db/schema.rb                                   | 270 ++++++-
 api/lib/vpsadmin/api.rb                            |  16 +
 api/lib/vpsadmin/api/exceptions.rb                 |   6 +
 api/lib/vpsadmin/api/locales/cs.yml                |  80 ++
 api/lib/vpsadmin/api/locales/en.yml                |  77 ++
 api/lib/vpsadmin/api/resources/storage_freeze.rb   | 184 +++++
 api/lib/vpsadmin/api/tasks/db.rake                 |  14 +
 api/lib/vpsadmin/api/transaction_signer.rb         |   6 +-
 api/lib/vpsadmin/storage_reconciler.rb             |  10 +
 .../vpsadmin/storage_reconciler/activity_report.rb | 455 +++++++++++
 api/lib/vpsadmin/storage_reconciler/artifacts.rb   | 270 +++++++
 api/lib/vpsadmin/storage_reconciler/capture.rb     | 212 +++++
 api/lib/vpsadmin/storage_reconciler/comparator.rb  | 682 ++++++++++++++++
 api/lib/vpsadmin/storage_reconciler/db_capture.rb  | 784 ++++++++++++++++++
 api/lib/vpsadmin/storage_reconciler/format.rb      |  71 ++
 .../vpsadmin/storage_reconciler/node_transport.rb  | 341 ++++++++
 api/lib/vpsadmin/storage_reconciler/offline.rb     |  13 +
 .../vpsadmin/storage_reconciler/private_store.rb   | 172 ++++
 .../vpsadmin/storage_reconciler/proof_planner.rb   | 732 +++++++++++++++++
 api/models/snapshot_in_pool.rb                     |   8 +
 api/models/snapshot_in_pool_in_branch.rb           |   9 +
 api/models/storage_effect_registry.rb              | 154 ++++
 api/models/storage_filesystem_identity.rb          | 128 +++
 api/models/storage_freeze_control.rb               |  10 +
 api/models/storage_freeze_status.rb                | 168 ++++
 api/models/storage_freeze_transition.rb            |  35 +
 api/models/storage_integrity_scope.rb              |  39 +
 api/models/storage_mutation_admission.rb           | 128 +++
 api/models/storage_mutation_attempt.rb             |  39 +
 api/models/storage_mutation_intent.rb              |  34 +
 api/models/storage_mutation_intent_scope.rb        |  17 +
 api/models/storage_mutation_journal.rb             | 259 ++++++
 api/models/storage_mutation_target.rb              |  61 ++
 api/models/storage_mutation_target_observation.rb  |  27 +
 api/models/storage_observation_run.rb              |  31 +
 api/models/storage_observer_catch_up_audit.rb      |  52 ++
 api/models/storage_observer_settlement.rb          | 216 +++++
 api/models/storage_snapshot_identity.rb            |  31 +
 api/models/transaction.rb                          |  43 +
 api/models/transaction_chain.rb                    |  12 +
 api/models/transaction_chains/dataset/snapshot.rb  |  25 +-
 .../dataset_in_pool/detach_backup_heads.rb         |   5 +
 .../transaction_chains/storage/activity_probe.rb   |  11 +
 api/models/transaction_chains/storage/inventory.rb |  11 +
 .../transactions/network_interface/rename.rb       |   1 +
 .../storage/activate_snapshot_clone.rb             |   1 +
 api/models/transactions/storage/activity_probe.rb  |  15 +
 api/models/transactions/storage/apply_rollback.rb  |   1 +
 api/models/transactions/storage/branch_dataset.rb  |   1 +
 api/models/transactions/storage/clone_snapshot.rb  |   1 +
 .../transactions/storage/clone_snapshot_name.rb    |   1 +
 api/models/transactions/storage/create_dataset.rb  |   1 +
 api/models/transactions/storage/create_pool.rb     |   1 +
 api/models/transactions/storage/create_snapshot.rb |  11 +-
 .../transactions/storage/create_snapshots.rb       |  27 +-
 api/models/transactions/storage/create_tree.rb     |   1 +
 .../storage/deactivate_snapshot_clone.rb           |   1 +
 api/models/transactions/storage/destroy_branch.rb  |   1 +
 api/models/transactions/storage/destroy_dataset.rb |   1 +
 .../transactions/storage/destroy_snapshot.rb       |   1 +
 api/models/transactions/storage/destroy_tree.rb    |   1 +
 .../transactions/storage/ensure_ugid_offset.rb     |   1 +
 .../transactions/storage/inherit_property.rb       |   1 +
 api/models/transactions/storage/inventory.rb       |  15 +
 api/models/transactions/storage/local_send.rb      |   1 +
 .../transactions/storage/prepare_rollback.rb       |   1 +
 api/models/transactions/storage/recv.rb            |   1 +
 api/models/transactions/storage/remove_clone.rb    |   1 +
 api/models/transactions/storage/rename_dataset.rb  |   1 +
 api/models/transactions/storage/rollback.rb        |   1 +
 api/models/transactions/storage/rsync_dataset.rb   |   1 +
 api/models/transactions/storage/set_canmount.rb    |   1 +
 api/models/transactions/storage/set_dataset.rb     |   1 +
 api/models/transactions/vps/boot.rb                |   1 +
 api/models/transactions/vps/chown.rb               |   1 +
 api/models/transactions/vps/copy.rb                |   1 +
 api/models/transactions/vps/create.rb              |   1 +
 api/models/transactions/vps/destroy.rb             |   1 +
 api/models/transactions/vps/features.rb            |   1 +
 api/models/transactions/vps/map_mode.rb            |   1 +
 api/models/transactions/vps/reinstall.rb           |   1 +
 api/models/transactions/vps/restart.rb             |   1 +
 api/models/transactions/vps/send_cleanup.rb        |   1 +
 api/models/transactions/vps/send_config.rb         |   1 +
 .../transactions/vps/send_rollback_config.rb       |   1 +
 api/models/transactions/vps/send_rootfs.rb         |   1 +
 api/models/transactions/vps/send_state.rb          |   1 +
 api/models/transactions/vps/send_sync.rb           |   1 +
 api/models/transactions/vps/start.rb               |   1 +
 api/models/transactions/vps/stop.rb                |   1 +
 api/spec/api/covered_endpoints.yml                 |   4 +
 api/spec/api/resources/storage_freeze_spec.rb      | 275 +++++++
 ...210000_add_storage_integrity_foundation_spec.rb | 160 ++++
 ...000_add_bounded_storage_capture_indexes_spec.rb |  53 ++
 .../migrations/storage_freeze_bootstrap_spec.rb    |  55 ++
 api/spec/models/storage_activity_report_spec.rb    | 269 +++++++
 api/spec/models/storage_effect_registry_spec.rb    | 145 ++++
 api/spec/models/storage_freeze_api_actor_spec.rb   |  92 +++
 api/spec/models/storage_freeze_status_spec.rb      | 152 ++++
 .../models/storage_integrity_foundation_spec.rb    | 265 ++++++
 api/spec/models/storage_mutation_admission_spec.rb | 431 ++++++++++
 .../storage_mutation_attempt_provenance_spec.rb    |  66 ++
 .../models/storage_observer_catch_up_audit_spec.rb |  43 +
 .../models/storage_observer_settlement_spec.rb     | 423 ++++++++++
 .../models/storage_reconciler_artifacts_spec.rb    | 407 ++++++++++
 api/spec/models/storage_reconciler_cli_spec.rb     | 145 ++++
 .../models/storage_reconciler_db_capture_spec.rb   | 843 ++++++++++++++++++++
 .../storage_reconciler_proof_planner_spec.rb       | 887 +++++++++++++++++++++
 api/spec/models/storage_reconciler_spec.rb         | 482 +++++++++++
 .../models/storage_reconciler_transaction_spec.rb  |  47 ++
 .../models/storage_reconciler_transport_spec.rb    | 135 ++++
 api/spec/models/transaction_chain_spec.rb          |   9 +
 .../dataset/group_snapshot_spec.rb                 | 107 +++
 .../transaction_chains/dataset/migrate_spec.rb     |  30 +
 .../transaction_chains/dataset/snapshot_spec.rb    |  43 +
 .../dataset_in_pool/detach_backup_heads_spec.rb    |  26 +
 .../transaction_chains/export/create_spec.rb       |   4 +
 api/spec/models/transaction_spec.rb                |   6 +
 api/spec/spec_helper.rb                            |   1 +
 api/spec/support/db_setup.rb                       |   8 +
 .../network_export_dns_chain_spec_helpers.rb       |   8 +-
 docs/README.md                                     |   3 +
 docs/storage/README.md                             |   6 +
 docs/storage/integrity-foundation.md               |  76 ++
 docs/storage/integrity-model.md                    | 138 ++++
 docs/storage/integrity-reconciler.md               | 231 ++++++
 flake.lock                                         |  18 +-
 libnodectld/lib/nodectld/command.rb                | 404 +++++++++-
 libnodectld/lib/nodectld/commands/base.rb          |   2 +
 .../nodectld/commands/dataset/group_snapshot.rb    |  78 +-
 .../lib/nodectld/commands/dataset/snapshot.rb      | 148 +++-
 .../nodectld/commands/storage/activity_probe.rb    |  17 +
 .../lib/nodectld/commands/storage/inventory.rb     |  21 +
 libnodectld/lib/nodectld/config.rb                 |   6 +
 libnodectld/lib/nodectld/daemon.rb                 |  55 +-
 libnodectld/lib/nodectld/dataset.rb                |   4 +-
 libnodectld/lib/nodectld/dataset_expander.rb       |  16 +-
 libnodectld/lib/nodectld/db.rb                     |   3 +-
 libnodectld/lib/nodectld/node_activity.rb          | 249 ++++++
 libnodectld/lib/nodectld/queues.rb                 |  36 +-
 libnodectld/lib/nodectld/remote_commands/chain.rb  |  48 +-
 libnodectld/lib/nodectld/storage_activity_probe.rb | 376 +++++++++
 .../lib/nodectld/storage_effect_registry.rb        | 143 ++++
 .../lib/nodectld/storage_group_snapshot_receipt.rb | 486 +++++++++++
 libnodectld/lib/nodectld/storage_inventory.rb      | 444 +++++++++++
 .../lib/nodectld/storage_mutation_receipt.rb       | 481 +++++++++++
 .../lib/nodectld/storage_observer_settlement.rb    | 188 +++++
 .../lib/nodectld/storage_strict_dispatch.rb        | 558 +++++++++++++
 libnodectld/lib/nodectld/transaction_queue.rb      | 117 ++-
 libnodectld/lib/nodectld/utils/queue.rb            |   4 +-
 libnodectld/lib/nodectld/worker.rb                 |   7 +-
 libnodectld/spec/nodectld/command_spec.rb          | 260 +++++-
 .../commands/dataset/group_snapshot_spec.rb        |  78 ++
 .../nodectld/commands/dataset/snapshot_spec.rb     | 103 +++
 libnodectld/spec/nodectld/dataset_expander_spec.rb |  17 +
 libnodectld/spec/nodectld/node_activity_spec.rb    | 185 +++++
 libnodectld/spec/nodectld/queues_spec.rb           |  38 +-
 .../spec/nodectld/remote_commands/chain_spec.rb    |  94 +++
 .../spec/nodectld/storage_activity_probe_spec.rb   | 273 +++++++
 .../spec/nodectld/storage_effect_registry_spec.rb  |  81 ++
 .../storage_group_snapshot_receipt_spec.rb         | 384 +++++++++
 .../spec/nodectld/storage_inventory_spec.rb        | 212 +++++
 .../spec/nodectld/storage_mutation_receipt_spec.rb | 887 +++++++++++++++++++++
 .../nodectld/storage_observer_settlement_spec.rb   | 305 +++++++
 libnodectld/spec/spec_helper.rb                    |   1 +
 libnodectld/spec/support/remote_command_helpers.rb |   3 +-
 libnodectld/spec/support/shared_connection_db.rb   |   2 +-
 nixos/modules/vpsadmin/database-setup.nix          |   1 +
 tests/ci-selection-test.rb                         |  28 +
 tests/ci-selection.yml                             |  30 +
 .../contracts/storage_group_snapshot_v4/README.md  |  27 +
 .../storage_group_snapshot_v4/api_producer_spec.rb |  84 ++
 .../storage_group_snapshot_v4/cleanup_test.sh      |  86 ++
 .../node_consumer_spec.rb                          | 283 +++++++
 tests/contracts/storage_group_snapshot_v4/run.sh   | 121 +++
 .../playwright/webui/specs/admin-cluster.spec.cjs  |  26 +
 tests/suite/storage/backup-full-incremental.nix    |   1 -
 webui/forms/cluster.forms.php                      | 174 ++++
 .../lang/locale/cs_CZ.utf8/LC_MESSAGES/vpsAdmin.mo | Bin 149746 -> 153878 bytes
 .../lang/locale/cs_CZ.utf8/LC_MESSAGES/vpsAdmin.po | 299 ++++++-
 webui/lang/locale/vpsAdmin.pot                     | 272 ++++++-
 webui/pages/page_cluster.php                       |  90 +++
 webui/tests/Regression/StorageFreezeUiTest.php     | 198 +++++
 189 files changed, 21108 insertions(+), 162 deletions(-)
```
