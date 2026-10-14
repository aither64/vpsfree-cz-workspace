# Final legacy client correction review packet

Initiative: 2026-10-05-network-ipv4-left-counter. Bound workspace
/home/aither/workspace/ai/vpsfree.cz, active tracking plan/state/design in this
directory. User requires V/W/C/K feature branches only; workspace instruction
policy was separately FF integrated. No deployment/retirement/lifecycle or PR
management outside W.

Overall risk remains high for the initiative (schema/admission/permissions);
this bounded correction changes UI detection inside the accepted contract.
Reviewer: retained reviewer0/read_only/gpt-6.1-sol/xhigh, without overrides.
Apply general, architecture/repetition, scope/proportionality and risk/
compatibility lanes to the correction, its callers, realistic coverage and pin
composition. Preserve earlier independent reviews for unchanged behavior.

## Exact committed snapshots and whole-branch inventory

- vpsadmin: c4d9b50f4e74417ed37b5fe410cca3ec1addc24e -> 5d5527a67315c18b595345aa6996d7724c1ed071; 3 logical commits; clean.
- vpsadmin-webui: 02ac0c7de1a588dbb14a18e652fe3f7e9b45cc51 -> e4c49bcdc91b33b7f644a2f125231cb413cf4bf4; 1 logical commits; clean.
- vpsfree-cz-configuration: 6f6aff9029cd57e1a0f9201356f7fdc9f6480671 -> 072cee195d826baf78351bfc283786eb63d6dfae; 2 logical commits; clean.
- vpsfree-kb-contracts: 873758fd6aec0c03f50a94600e0ceab97946f255 -> a50f8c1a11ea642edf823f04521f9eaa97132fd2; 1 logical commits; clean.

[Inventory](legacy-network-client-final-inventory.json) provides exact paths/
refs/complete commit series. `legacy-network-client-final-{v,w,config,kb}.diff`
and `.history.log` retain full comparisons. `legacy-network-client-source-range.diff`
and `legacy-network-client-consolidated-correction.diff` prove consolidation.
The four-path correction is folded into the legacy owning commit; original API
fc4f01a0 and the separate accepted Index patch remain unchanged. C keeps two
canonical generated streams/messages. K keeps one exact five-record commit.
Explicitly conclude whether any obsolete branch history remains and reconcile
migration lineage using this inventory and earlier reviewed unchanged blobs.

## Runtime finding and intended behavior

Exact legacy selector at cc3337d0 failed before its first toggle; correct page
heading but no confirmation form. HaveAPI PHP client 0.29.6 ResourceInstance has
__get/attributes but no __isset. New isset/?? checks falsely treated known state
as missing; plain-object fixtures concealed it.

The typed nullable network_enabled_state helper reads the explicit client
attributes contract, without fallback probing. Reused call sites: network
list/editor, IP inventory/detail state, detached assignment links and stale
assignment form. True/false/missing remain distinct; advertised input metadata
checks remain stdClass isset. Preserve oldAPI omission, admin-only capability
controls, existing assigned service/removal/host/VPS links and direct Show.
No framework/vendor/API/policy/schema/migration/approved wording/catalog/React
change. Owning feature docs already describe this behavior; helper comment
explains the client invariant, and the reusable workspace note records the
diagnostic. No unrelated pagination fix is included.

## Quick checks and scope proof

All quick4 formatter/syntax/fullPHP/locales/aggregate exits0. NativeJUnit104tests/
515assertions, errors0/failures0/skips0; NetworkAvailabilityTest7/116. Real locked
Client actions/Response/ResourceInstance/List and real XTemplate render; only
transport deterministic. PHP8.4.24/HaveAPI0.29.6/PHPUnit13.4.1. One deprecation
is unchanged Pagination\System implicitnullable Action argument at151; root
seven-test diagnostic and baseline blob inspection established this, no
suppression or fix. Logs/XML/freeze under legacy-network-client-quick4-*.
Normal source hooks passed; fixup autosquash finaltree equality and exact oldto
new4path diff inspected. Complete API/docs/testsscenarios/clientlocks/catalogs
byte-identical to cc3337d0. Quick1/2 were unused snapshots; quick3 formatter
failure preserved.

C only selected V locked rev/hash/time differs from reviewed b217e0f0; W e4,
follows and full unrelated graph preserved. K five records match finalV;
fingerprints/pages/PNG bytes unchanged. Fresh pinned shell actual source
/nix/store/4jqcdmnsrhf0j1pqrx57mz70n0vpkl06-source; bin/check passed suites
8/50,10/22,38/112,4/10 with failures/errors/skips0 and unchanged inventory.
K candidate inspected and normal committed with declared/no-active-hook proof.
V/C/K are published on their exact feature refs. Publication receipt and remote
head proofs match these committed objects; no default integration occurred.

## Migration, runtime and readiness limits

Sole migration20261006120000_add_network_enabled follows20260914190000 directly:
reversible final NOTNULL/defaulttrue bool, no stale-schema guards. Source/schema
blobs unchanged from API commit and prior review; declared consumption disposable
API/VM tests only, no merged/released/deployed/prod consumption established.
W/C/K no migrations. Schema first, every writer before first disable; old writer
rollback loses enforcement with disabled pools. No coordinated node update.

Migration-with-data and remote-descendant restore passed at cc3337d0 with exact
payload/checksum/IP/disabled-state assertions; their source/backend bytes are
unchanged. Do not relabel them as executions at the new head. After this gate,
rerun ONLY webui#admin-cluster and build all12currentC consumers; retain all
original assertions. No runtime check of this correction has run yet.

Accepted W shared-OPTIONS timeout Advisory remains unchanged, as does older
proxy-addr2.0.7/baseline requiring reconciliation before current-release/deploy
readiness. Two CS/EN memberIP-list captures remain blocked on supported owned
runtime; no rawhelper/statecopy/ownership bypass. Production writer/revision
inventory, actual count attribution and retirement list remain unverified.

[Correction evidence](legacy-network-client-verification.md),
[earlier source review](visibility-review-result.md),
[prior dispositions](visibility-review-findings.md),
[portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-05-network-ipv4-left-counter/).
