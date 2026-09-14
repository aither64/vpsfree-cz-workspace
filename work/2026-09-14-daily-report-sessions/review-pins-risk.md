# Final configuration pin risk and compatibility review

Reviewed with the mandatory-change-review risk and compatibility lane at
`xhigh` effort:

- vpsfree-cz-configuration
  `249bed1ee28e69a907edd09ea97a1144dbcdefeb..5036135728832d5c375705e3b69949c33460ff7e`
- pinned vpsAdmin head `9456fae6f181cef2e8982eed462e873095fd49da`
- pinned notification-template head
  `08402ffd8010384f950b1ec4a1b95de8e5410ba3`

The lane remains high risk because the selected vpsAdmin revision contains
additive live-table indexes and therefore carries migration, rollout, and
rollback considerations. The configuration edits themselves are generated,
bounded, and reversible.

## Findings

No Blocking, Important, or Advisory findings.

## Pin and consumer evidence

The reviewed range is a linear two-commit series. Each generated `confctl`
commit changes only `flake.lock`: first `vpsadminServices`, then
`vpsfreeNotificationTemplates`. The combined diff changes only each node's
`lastModified`, `narHash`, and `rev`. A normalized comparison after removing
those six expected fields found all other lock data identical. In particular,
the staging and production vpsAdmin inputs, every vpsAdminOS and nixpkgs input,
the root input mapping, and unrelated nodes are unchanged.

`nix flake metadata --json --no-write-lock-file .` resolved the committed
configuration head and confirmed:

- `vpsadminServices.rev` is
  `9456fae6f181cef2e8982eed462e873095fd49da`;
- `vpsfreeNotificationTemplates.rev` is
  `08402ffd8010384f950b1ec4a1b95de8e5410ba3`;
- the template input's `vpsadmin` edge still follows
  `vpsadminServices`;
- `vpsadminServices` still follows `nixpkgsStable` and
  `vpsadminosStaging`.

Direct `git ls-remote` checks against the SSH origins returned both exact
source heads on `2026-09-14-daily-report-sessions`. Each source head is a
single descendant of its recorded base, so the pins select the final reviewed
source commits without extra branch commits.

The configuration topology preserves the intended mixed-consumer contract.
`int.api1` consumes both channels and owns the scheduler plus replacement
notification templates; `int.api2` consumes `vpsadminServices` without the
template channel. The same `vpsadmin` channel is listed by other service
machines, but the selected source range changes only API/database content and
tests. Building both API configurations covers the changed API package, its
database/migration package, the API1 managed template, and the API2
generator-only path. No changed Nix module or vpsAdminOS behavior creates an
update-order dependency for the other machines.

## Compatibility and rollout assessment

Mixed old/new API operation remains compatible. The report payload is
additive, an old template ignores it, and the new external template guards all
new sections when an old generator omits them. The database migration adds
indexes only; new code produces correct results before migration and old code
can use the indexed schema. Rollback may leave the indexes installed. There is
no public API, persisted-record, inter-service protocol, node, or vpsAdminOS
contract change in this pin phase.

Production keeps `vpsadmin.databaseSetup.autoSetup = false`. A later authorized
rollout must explicitly run `vpsadmin-api-migrate-db.service` once from the new
package and monitor metadata-lock waits and I/O. Deploying the generator before
that step is schema-compatible but may leave the daily queries performing full
table scans. No activation or migration is part of this phase.

## Residual risks and required validation

- The two configuration builds have not run yet. They must use unchanged head
  `5036135728832d5c375705e3b69949c33460ff7e` and cover
  `cz.vpsfree/vpsadmin/int.api*` as planned. A head change invalidates this
  review.
- The configuration feature branch was committed locally but was not present
  on the remote at review time, matching the planned review-before-push order.
  The exact reviewed head must be pushed for the validated-branch handoff.
- Synthetic query plans do not measure production table cardinality, report
  latency, or live index-build locking and I/O. Those remain deployment-time
  operational risks rather than pin correctness defects.
- The shared `vpsadmin` channel may cause revision-only rebuilds when unrelated
  service machines are next evaluated, even though their functional source
  paths did not change. No deployment of those consumers is authorized here.
