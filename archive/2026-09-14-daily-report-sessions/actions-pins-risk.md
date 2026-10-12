# Final generated configuration pins: risk and compatibility review

Reviewed directly with the mandatory-change-review risk and compatibility lane
at `xhigh` effort:

- vpsfree-cz-configuration
  `249bed1ee28e69a907edd09ea97a1144dbcdefeb..3f213d5ebf922ab5522690ab28b3fdfa9b3bed1d`;
- pinned vpsAdmin source
  `5ac49802f892da6fd37a88c8349b9cc7ea826538..014fbc78422f3660b295add7a50f35cc7acdf0c8`,
  including the current-master dependency commits between the original base
  `791ab3aa89e2f613979da6090b89785c78245db5` and `5ac49802f892da6fd37a88c8349b9cc7ea826538`;
- pinned vpsfree-notification-templates source
  `f944ba03eba5d0d6b58b7eb856f251d1c96f2c11..6ebfb6f11c1ba00ae9dc7868ac0b3c42d30e5333`;
- the actual API1/API2 channel topology, package and template wiring, migration
  mechanism, and repository guidance.

The lane remains high risk because the pinned source contains additive indexes
for live authentication-history tables and crosses API, template, and
configuration repositories.

## Findings

No Blocking, Important, or Advisory findings.

## Pin integrity and source provenance

The configuration series is exactly two direct commits on the recorded base.
Commit `6e0021ac74b3bfcb69b09a23a7a0df7c3c869f47` changes only the
`vpsadminServices.locked` revision, timestamp, and NAR hash, from
`791ab3aa89e2f613979da6090b89785c78245db5` to
`014fbc78422f3660b295add7a50f35cc7acdf0c8`. Commit
`3f213d5ebf922ab5522690ab28b3fdfa9b3bed1d` then changes only the corresponding
three `vpsfreeNotificationTemplates.locked` fields, from
`f944ba03eba5d0d6b58b7eb856f251d1c96f2c11` to
`6ebfb6f11c1ba00ae9dc7868ac0b3c42d30e5333`. A normalized comparison after
removing those two `locked` objects is identical, and the full diff contains no
other lock node, root input, follows edge, or tracked file change.

Both exact source heads exist on the expected remote feature branches. The API
head descends from current remote master
`5ac49802f892da6fd37a88c8349b9cc7ea826538`; the template head descends from
current remote master `f944ba03eba5d0d6b58b7eb856f251d1c96f2c11`.
The generated commit messages accurately enumerate the included source series.

The API pin necessarily includes two scheduled upstream dependency updates that
landed before the feature was rebased: `io-console` 0.9.2 to 0.9.3 across the
packaged Ruby components and `nikic/php-parser` 5.8.0 to 5.9.0 in the WebUI
package. Neither changes a persisted format, protocol, deployment contract, or
host topology. The WebUI package is not enabled by these API host definitions;
the Ruby package update remains subject to the planned exact-head host builds
and the source branch CI gates.

## Consumer topology and mixed-version behavior

The lock and declared flake graph preserve
`vpsfreeNotificationTemplates.inputs.vpsadmin.follows = "vpsadminServices"` at
`flake.nix:31-34`. The template package is therefore evaluated against the same
vpsAdmin revision deployed to the service hosts instead of carrying an
independent API/checker revision.

The `vpsadmin` channel maps to `vpsadminServices` at `flake.nix:100-102`. API1
selects both that channel and `vpsfree-notification-templates` at
`cluster/cz.vpsfree/vpsadmin/int.api1/module.nix:5-10`; it enables the scheduler
and replaces managed notification templates from the external package at
`cluster/cz.vpsfree/vpsadmin/int.api1/config.nix:21-27`. API2 selects the API
channel without the template channel at
`cluster/cz.vpsfree/vpsadmin/int.api2/module.nix:5-9`. Both hosts import the
same pinned vpsAdmin NixOS modules and overlay through
`cluster/cz.vpsfree/vpsadmin/common/all.nix`.

This topology matches the intended ownership: API1 schedules and renders the
daily report and reconciles organization templates, while API2 consumes the API
package. The source contract is additive. Old templates ignore the extra
payload, and the new external template guards absent top-level hashes and absent
or empty event arrays. API hosts can therefore be updated independently without
a public API, client, daemon, node, or vpsAdminOS coordination requirement.

## Migration, rollout, and rollback

The pinned API source adds four ordinary indexes and no schema-existence guards
in `api/db/migrate/20260914120000_add_daily_report_authentication_indexes.rb:1-8`.
The report queries are correct without the indexes, so application activation
does not depend on migration completion for correctness. Older application
versions tolerate the indexes, and rollback can leave them installed.

Both API configurations explicitly keep
`vpsadmin.databaseSetup.autoSetup = false` at
`cluster/cz.vpsfree/vpsadmin/common/api.nix:39-47`, preventing concurrent or
implicit migration during host activation. A later authorized production
rollout must run `vpsadmin-api-migrate-db.service` once from the new package and
monitor metadata-lock waits and I/O while the live indexes are built. No
production migration, activation, deployment, or coordinated node update is
part of this pin series.

## Outstanding gates and residual limits

- The local configuration branch is intentionally rewritten relative to its
  published old pin head `5036135728832d5c375705e3b69949c33460ff7e`. After
  review it must be pushed with the recorded lease, and the remote feature ref
  must be verified at exact reviewed head
  `3f213d5ebf922ab5522690ab28b3fdfa9b3bed1d`.
- Build both `cz.vpsfree/vpsadmin/int.api*` configurations at that exact head.
  This is the remaining check that the combined API, updated packaged Ruby
  dependency, and followed template package evaluate and build for both actual
  consumers.
- The follow-up delivered-mail integration and remaining exact-source API CI
  jobs were still running at the packet checkpoint. Their successful
  completion remains a delivery gate rather than a pin-review finding.
- Production index-build cost has synthetic query-plan evidence but no
  production-volume latency, lock, or I/O benchmark. Retain the recorded
  monitored manual-migration procedure for any later approved rollout.
