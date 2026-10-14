# Final legacy client correction review (2026-10-07)

Lead record of reviewer0's independent final report received in the bound
conversation. Result: **no new Blocking, Important or Advisory findings** in the
bounded PHP correction or downstream pin composition. The previously accepted
W shared-OPTIONS timeout Advisory remains unchanged. The committed-source gate
is clear for the affected runtime/build checks; this is not deployment,
integration or final visual-artifact certification.

## Reviewer and scope

Reviewer0 independently verified the exact session, absent shell identity
markers and trusted binding, plus its live review-purpose/read-only roster
entry. Saved model/effort: gpt-6.1-sol/xhigh; thread
01a10c52-55c7-7490-8cd9-75efda7f00d9. No override, fallback, nested reviewer,
source/tracking edit, test/build, fetch/publication/CI or lifecycle operation.
Mandatory review and all four lane references plus applicable project guidance,
packet/inventory and committed source were read.

Exact independently clean merge-base-to-head snapshots:

- V: c4d9b50f4e74417ed37b5fe410cca3ec1addc24e -> 5d5527a67315c18b595345aa6996d7724c1ed071.
- W: 02ac0c7de1a588dbb14a18e652fe3f7e9b45cc51 -> e4c49bcdc91b33b7f644a2f125231cb413cf4bf4.
- C: 6f6aff9029cd57e1a0f9201356f7fdc9f6480671 -> 072cee195d826baf78351bfc283786eb63d6dfae.
- K: 873758fd6aec0c03f50a94600e0ceab97946f255 -> a50f8c1a11ea642edf823f04521f9eaa97132fd2.

The four complete binary diff artifacts equal fresh Git comparisons. See
[packet](legacy-network-client-review-packet.md) and
[inventory](legacy-network-client-final-inventory.json).

## Lane conclusions

General: the nullable typed helper at functions.lib.php:36-43 reads actual
ResourceInstance attributes and preserves true/false/omitted state. Locked
HaveAPI 0.29.6 has no __isset. Association __get resolves Network.Show before
returning ResourceInstance, so IP network callers obtain resolved state.
ResourceInstanceList constructs the same class; bootstrap loads Composer first.
Action metadata remains stdClass, so its existing isset checks are valid.
Network list/editor and IP list/detail/stale-form callers preserve old-API
omission, capability suppression, assigned removal/VPS/host links and Show.
Admin routing, POST-only update, confirmation/target validation and CSRF are
unchanged. Server admission and authorization are not weakened.

Architecture: one narrow helper owns extraction for affected callers, without
vendor patch, fallback probes or duplicated presence assumptions. Deterministic
transport retains real Client/Action/Response/ResourceInstance/List and XTemplate
behavior. No shared client/API contract change needs unrelated adoption.

Scope: comparison with cc3337d0 changes only the four assigned PHP paths.
API/docs/all VM/browser scenarios/Composer manifests and locks/catalogs are
byte-identical. API commit remains fc4f01a0; separate Index patch and unrelated
legacy content remain identical. Seven real-client tests cover the demonstrated
failure and retained old-API/service boundaries. No generalized client framework
or Pagination fix. Existing owning docs plus the helper comment suffice.

Risk/composition: C changes only rev/narHash/lastModified on selected V/W lock
nodes from its current base; all unrelated nodes, top-level fields and follows
remain unchanged. W stays e4c49bcd and follows vpsadminServices. Versus b217e0f0
only V's three locked fields differ. K's five revisions consistently pin V;
one lock node changes, with unrelated graph/follows, pages, fingerprints and PNGs
preserved. Effective /nix/store/4jqcdmnsrhf0j1pqrx57mz70n0vpkl06-source matches
final V helper/caller/test/migration blobs. Earlier unchanged API/W/debt-ledger
conclusions remain at those same blobs; no cap growth or new exception.

## Complete history and migration conclusion

Three/one/two/one logical commits, no merges:

- V fc4f01a025e373ba5c85a7e78ea8b61ac1e1dc1f (API/schema/admission),
  70314e816099855b31b56ee42d3b887e2195566a (legacy UI and correction/tests),
  5d5527a67315c18b595345aa6996d7724c1ed071 (separate Index policy).
- W e4c49bcdc91b33b7f644a2f125231cb413cf4bf4 (React behavior).
- C e047d285231395a250b2cc606306e7673574cb9c then
  072cee195d826baf78351bfc283786eb63d6dfae (canonical V/W streams).
- K a50f8c1a11ea642edf823f04521f9eaa97132fd2 (exact pin).

Splits/messages are coherent. No obsolete approach, abandoned compatibility
path, transitional migration, repeated pin iteration or leftover fixup remains.
Sole V migration 20261006120000_add_network_enabled immediately follows
20260914190000_add_node_kernel_evidence_checkpoints, directly adding reversible
NOT NULL/default-true bool, without stale-schema guards. Schema changes only
version/column. Bytes remain unchanged from API commit and prior review.
57 retained default/tag refs contain no migration; contains-commit refs are
feature/local remote feature only. Declared external consumption is disposable
API/VM tests; production merge/release/deployment/consumption is unverified.
Lineage is sound within that evidence. W/C/K: no migrations.

## Evidence and remaining gates

Reviewer independently verified quick4 freeze against current files, all five
exits 0, native JUnit 104 tests/515 assertions and real-client 7/116 with zero
errors/failures/skips. These checked draft bytes equal final committed bytes;
reviewer did not rerun tests. PHP 8.4.24, HaveAPI 0.29.6, PHPUnit 13.4.1.
The reported Pagination deprecation is unchanged baseline; no suppression/fix.
KB static suites 8/50, 10/22, 38/112, 4/10 passed, without proving bitmap freshness.

Rerun only webui#admin-cluster with original assertions, then build 12 actual
consumers at final C. Migration-with-data and remote-descendant restore passed
at cc3337d0; unchanged backend/scenario bytes support retaining those receipts
without relabeling execution. Synthetic template tests do not certify live
browser/HTTP behavior. W retains the accepted timeout and older proxy-addr 2.0.7
baseline/default divergence, requiring reconciliation before release/deployment.
Two CS/EN member-IP-list images require a supported owned capture runtime,
regeneration, visual inspection and appropriate artifact review. No lifecycle
or ownership bypass.

Rollout: schema first; every allocation writer before first disable, then
compatible interfaces/capabilities. Old-writer rollback loses enforcement with
disabled pools; UI rollback preserves it. No coordinated node update. Production
revisions/writers, counter attribution and retirement list remain unverified.

Lead disposition: no new findings need remediation. Earlier W Advisory remains
accepted/deferred as recorded in visibility-review-findings.md. Proceed only
with the affected runtime/build checks, keeping all feature/default/production
and KB runtime boundaries.

[Portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-05-network-ipv4-left-counter/)
