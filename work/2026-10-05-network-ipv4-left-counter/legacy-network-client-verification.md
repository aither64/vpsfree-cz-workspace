# Legacy network availability client correction (2026-10-07)

The exact `webui#admin-cluster` run at V
`cc3337d0a2699a8b28a0327bbee5ef62f3fbe166` failed before the first toggle.
The network-availability page heading rendered, but the expected confirmation
form was absent. Selector and aggregate exits were 1; the first-failure wrapper
did not start any configuration build. Migration and remote descendant restore
had already passed at that head with their data and IP-identity checks intact.

The locked HaveAPI PHP client 0.29.6 exposes resource fields through `__get` and
`attributes()` without `__isset`. The new UI checks using `isset` and `??`
therefore treated known enabled/disabled values as missing. Plain-object test
doubles concealed the difference. See the
[field-presence note](../../notes/vpsadmin/2026-10-07-haveapi-php-field-presence.md).

## Correction and quick evidence

The four-path correction adds a nullable helper using the explicit
ResourceInstance attributes contract. It preserves true, false and missing
values in the network list/editor, IP inventory/detail, detached assignment
hints and stale assignment form. The advertised input metadata checks remain
unchanged. Assigned service, removal and host/VPS links remain available.
No API policy, client/vendor, schema, migration, wording, catalogue, React or
VM/browser scenario source changes are included.

The existing PHP regression file now uses actual Client actions, responses,
resource instances/lists and XTemplate rendering; only HTTP transport is
replaced by deterministic envelopes. It covers the two boolean states, missing
older-API fields, capability absence and assigned/detached address behavior.

Quick3 stopped at four test-only arrow-function spacing offenses, exit 8. No
behavior test ran. After those four spaces were corrected, quick4 passed scoped
formatting, all four syntax checks, the full PHP suite and locale health, with
all individual/aggregate exits 0. Native JUnit records 104 tests and 515
assertions, no failures, errors or skips. NetworkAvailabilityTest contributes
seven tests and 116 assertions. PHP 8.4.24, HaveAPI 0.29.6 and PHPUnit 13.4.1
were recorded. Source/helper hashes and the exact four-path diff are frozen in
`legacy-network-client-quick4.sha256` and `.diff`.

One deprecation appeared in the suite. A short seven-test diagnostic with
`--display-deprecations` passed and identified the implicit nullable Action
argument in `webui/lib/pagination.lib.php:151`, unchanged from base c4d9b50f.
No suppression or unrelated source change was made.

## Committed review and runtime verification

Root inspected and completed the normal-hook consolidation. The correction is
folded into the legacy owning commit; the original API commit and separate
visibility patch remain intact. Final V is `5d5527a67315c18b595345aa6996d7724c1ed071`
and is published. W stays at `e4c49bcdc91b33b7f644a2f125231cb413cf4bf4`.
Canonical C pins produced `072cee195d826baf78351bfc283786eb63d6dfae`;
the exact five-record K update is committed as
`a50f8c1a11ea642edf823f04521f9eaa97132fd2`. C/K feature publication passed in a
separate utility. Aggregate and all publication/cancellation steps exited 0;
no superseded C/K run was selected. Complete histories and diffs are in the
[final inventory](legacy-network-client-final-inventory.json).

Root inspected the generated graphs: only V metadata changes from the previous
C candidate, with W, follows and unrelated identities preserved. K records the
same V revision, with fingerprints and PNGs unchanged. A fresh pinned shell
resolved `/nix/store/4jqcdmnsrhf0j1pqrx57mz70n0vpkl06-source` and passed all four
static suites (8/50, 10/22, 38/112 and 4/10 tests/assertions). Inventory remains
60 concepts and 120 variants. Reviewer0 reviewed these committed heads in all
four applicable lanes with
no new findings. Complete history and migration lineage are sound within the
recorded provenance. See [final review](legacy-network-client-review-result.md);
no runtime result for the correction is claimed.

After committed-source review, fresh utility `legacy_client_final_runtime`
ran the exact unchanged legacy selector and all 12 C consumers. Aggregate,
selector and all build exits are 0. The legacy example passed in 448.5 seconds;
its script succeeded in 804.32 seconds, and the runner reported one successful
test in 1036.31 seconds. Root verified the native receipts, completed build
logs and unchanged final clean source heads. Total batch took about 32 minutes.
No unexpected local kernel build or owned running process remains. See the
[structured runtime/build proof](legacy-network-client-runtime-result.json).

Successful migration/restore receipts still belong to cc3337d0, with unchanged
backend/scenario bytes; their data and IP assertions were retained. They were
not rerun or relabeled at the final head. The unchanged vpsadminos input remains
8e44a5124439b1f3048ffc56b1717614a5360358; K a50f8c1a is the KB revision.

The two bilingual member-IP-list captures still require a supported owned
runtime. The accepted W timeout finding and its older dependency baseline
remain recorded in the visibility review. No default integration, deployment,
production retirement, PR management outside W or lifecycle operation is
authorized. V/W/C/K remain on feature branches as directed; the initiative
remains active.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-05-network-ipv4-left-counter/)
