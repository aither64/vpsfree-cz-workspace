# Complete final branch inventory

All intended source and pin changes are committed and clean, 2026-10-06.
Original whole-branch review remains in review-original-*; review-result.md
records narrow direct corrections and checks under workflow step 9.

## vpsadmin

- Branch: 2026-10-05-network-ipv4-left-counter
- Base: c4d9b50f4e74417ed37b5fe410cca3ec1addc24e
- Head: be136b6c00f03b85b7a12cc57550b4a1394a94a7
- Default: master
- Final diff: [final-vpsadmin.diff](final-vpsadmin.diff)

```text
fc4f01a025e373ba5c85a7e78ea8b61ac1e1dc1f api: add network availability admission controls
be136b6c00f03b85b7a12cc57550b4a1394a94a7 webui: expose network availability and enabled address selectors
```

```text
 .../migrate/20261006120000_add_network_enabled.rb  |   5 +
 api/db/schema.rb                                   |   3 +-
 api/lib/vpsadmin/api/locales/cs.yml                |  10 +
 api/lib/vpsadmin/api/locales/en.yml                |  10 +
 api/lib/vpsadmin/api/resources/cluster.rb          |   3 +-
 api/lib/vpsadmin/api/resources/ip_address.rb       |   4 +-
 api/lib/vpsadmin/api/resources/network.rb          |   8 +-
 api/lib/vpsadmin/api/resources/user.rb             |   4 +-
 api/models/ip_address.rb                           |  69 ++++++-
 api/models/ip_release_request_address.rb           |   2 +-
 api/models/network.rb                              |  18 +-
 api/models/network_interface.rb                    |   1 +
 api/models/transaction_chains/export/create.rb     |   6 +-
 api/models/transaction_chains/ip/allocate.rb       |  39 ++--
 api/models/transaction_chains/ip/update.rb         |   3 +
 .../network_interface/add_route.rb                 |   2 +
 .../transaction_chains/vps/clone/os_to_os.rb       |  27 ++-
 api/models/transaction_chains/vps/create.rb        |  11 +-
 api/models/transaction_chains/vps/migrate/base.rb  |  49 ++++-
 api/models/transaction_chains/vps/swap.rb          |   9 +
 api/models/transaction_chains/vps/update.rb        |  44 +++--
 api/spec/api/resources/cluster_spec.rb             |  30 ++-
 api/spec/api/resources/network_write_spec.rb       |  28 +++
 api/spec/api/resources/user_available_ips_spec.rb  |  11 ++
 .../20261006120000_add_network_enabled_spec.rb     |  29 +++
 api/spec/models/ip_ownership_concurrency_spec.rb   | 218 ++++++++++++++++++++-
 api/spec/models/network_registration_spec.rb       |  19 ++
 .../transaction_chains/export/create_spec.rb       |   2 +-
 .../models/transaction_chains/ip/allocate_spec.rb  |  77 +++++++-
 .../models/transaction_chains/ip/update_spec.rb    |  15 ++
 .../network_interface/add_route_spec.rb            |  14 ++
 .../transaction_chains/vps/clone/os_to_os_spec.rb  |  24 ++-
 .../models/transaction_chains/vps/create_spec.rb   |  22 +++
 .../models/transaction_chains/vps/migrate_spec.rb  |   1 +
 .../transaction_chains/vps/replace/os_spec.rb      |   3 +-
 .../models/transaction_chains/vps/swap_spec.rb     |   2 +
 .../models/transaction_chains/vps/update_spec.rb   | 116 +++++++++++
 docs/README.md                                     |   1 +
 docs/ip-locking.md                                 |  58 ++++++
 docs/upgrade-network-availability.md               |  32 +++
 .../playwright/webui/specs/admin-cluster.spec.cjs  |  37 ++++
 tests/suite/network/export-lifecycle.nix           |   9 +
 .../network-interface-routes-and-host-ips.nix      |  35 ++++
 ...ore-after-reinstall-with-descendants-remote.nix |  14 ++
 tests/suite/vps/migrate-with-data-check.nix        |  18 ++
 webui/forms/cluster.forms.php                      |  44 +++++
 webui/forms/networking.forms.php                   |  17 +-
 .../lang/locale/cs_CZ.utf8/LC_MESSAGES/vpsAdmin.mo | Bin 149746 -> 150374 bytes
 .../lang/locale/cs_CZ.utf8/LC_MESSAGES/vpsAdmin.po |  79 +++++---
 webui/lang/locale/vpsAdmin.pot                     |  61 ++++--
 webui/lib/functions.lib.php                        |   4 +
 webui/pages/page_cluster.php                       |  23 +++
 webui/tests/Regression/CsrfStateFormsTest.php      |  15 ++
 webui/tests/Regression/NetworkAvailabilityTest.php |  86 ++++++++
 54 files changed, 1331 insertions(+), 140 deletions(-)
```

## vpsadmin-webui

- Branch: dev/network-enabled
- Base: 02ac0c7de1a588dbb14a18e652fe3f7e9b45cc51
- Head: e4c49bcdc91b33b7f644a2f125231cb413cf4bf4
- Default: main
- Final diff: [final-vpsadmin-webui.diff](final-vpsadmin-webui.diff)

```text
e4c49bcdc91b33b7f644a2f125231cb413cf4bf4 networking: manage network availability
```

```text
 docs/design/API_CONTRACTS.md                       |  33 ++++-
 docs/design/EVIDENCE_MATRIX.md                     |   5 +-
 docs/design/REQUIREMENTS.md                        |   8 +-
 docs/design/WORKFLOWS.md                           |  17 +++
 docs/work-log/2026-10-06-network-availability.md   |  80 +++++++++++
 e2e/specs/admin/network_availability.spec.ts       | 135 +++++++++++++++++
 scripts/fixtures/e2e-type-coverage.json            |   1 +
 scripts/fixtures/structural-debt-ledger.json       |   8 +-
 src/i18n/locales/cs/adminCluster/networks.ts       |   3 +
 src/i18n/locales/en/adminCluster/networks.ts       |   3 +
 src/lib/api/ipAddresses.ts                         |   9 ++
 src/lib/api/networks.test.ts                       |  21 ++-
 src/lib/api/networks.ts                            |  22 +++
 src/pages/app/admin/cluster/NetworksPage.test.tsx  | 159 +++++++++++++++++++++
 src/pages/app/admin/cluster/NetworksPage.tsx       |  49 +++++++
 .../useProgressiveSuggestedIpQueries.test.tsx      |  92 ++++++++++++
 .../useProgressiveSuggestedIpQueries.ts            |  17 ++-
 .../networking/UserNetworkAddressActions.test.tsx  |  49 +++++++
 .../app/networking/UserNetworkAddressActions.tsx   |  34 +++++
 src/pages/app/networking/UserNetworkPage.tsx       |  24 ++--
 .../networking/fetchAssignableIpAddresses.test.ts  |  23 ++-
 .../app/networking/fetchAssignableIpAddresses.ts   |   9 +-
 tsconfig.e2e.json                                  |   1 +
 23 files changed, 763 insertions(+), 39 deletions(-)
```

## vpsfree-cz-configuration

- Branch: 2026-10-05-network-ipv4-left-counter
- Base: cde8451718d75929c931db63626b48f7de92fc4f
- Head: dd10d88073da3aed6c4512e938abe4374422aab1
- Default: master
- Final diff: [final-vpsfree-cz-configuration.diff](final-vpsfree-cz-configuration.diff)

```text
8e84787b9d362cf7482ceeb590446163ce042edc inputs: set vpsadminServices to be136b6c
dd10d88073da3aed6c4512e938abe4374422aab1 inputs: set vpsadminWebui to e4c49bcd
```

```text
 flake.lock | 12 ++++++------
 1 file changed, 6 insertions(+), 6 deletions(-)
```

## vpsfree-kb-contracts

- Branch: 2026-10-05-network-ipv4-left-counter
- Base: 873758fd6aec0c03f50a94600e0ceab97946f255
- Head: 291566b2c0bd43389802f607852fd9a4f8241752
- Default: master
- Final diff: [final-vpsfree-kb-contracts.diff](final-vpsfree-kb-contracts.diff)

```text
291566b2c0bd43389802f607852fd9a4f8241752 inputs: pin network availability vpsAdmin revision
```

```text
 captures.json           | 2 +-
 contract/navigation.yml | 2 +-
 contract/pages.yml      | 2 +-
 flake.lock              | 8 ++++----
 flake.nix               | 2 +-
 5 files changed, 8 insertions(+), 8 deletions(-)
```
## History, migrations and pin disposition

V retains two logical commits and W one; normal-hook fixups were autosquashed with exact final-tree equality and unchanged schema/migration blobs. Original author/message splits remain. No superseded approaches or fixups remain. C regenerated two canonical confctl commits from its original base; K one exact-pin commit. All pins match final V/W source heads. Complete transitive diffs were inspected; unrelated inputs/follows are unchanged. Only the two C lock nodes and one K lock node changed, with follows edges and unrelated inputs unchanged.

The sole migration is 20261006120000_add_network_enabled, following 20260914190000_add_node_kernel_evidence_checkpoints, Schema[8.1]. It adds NOT NULL/default-true enabled directly, without stale-schema guards. Unmerged, unreleased, undeployed and unconsumed outside disposable test databases; production provenance is unverified. W/C/K have no migrations.

Original whole-branch review concluded coherent history and sound migration lineage. Direct remediation inspection and focused checks passed; mechanical pin refreshes passed and their complete transitive diffs were inspected. Long runtime/build verification is now cleared. No merge or deployment is authorized. Two existing KB images remain pending a supported capture runtime.

## Separate dependency prerequisite

The registered vpsadmin-webui-proxy-addr branch is independent of the network
source/pin series. Its one four-file commit a7361bb2912485b61a5a0b1472d51158ac08ec96
starts at W main base 02ac0c7de1a588dbb14a18e652fe3f7e9b45cc51, with no
migration, runtime/API/trust-policy change or obsolete fixup. Its complete scope,
mechanical review exemption and exact package proof are recorded in
[maintenance review](proxy-addr-maintenance-review.md).

Runtime/build results and remaining prerequisites at these exact heads are in
[final verification](fixture-final-verification.md); the network deliverable
still has outstanding migration/restore/legacy and KB visual evidence.
