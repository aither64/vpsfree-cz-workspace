# Final isolated-testDB compatibility assessment

Reviewer0 report2026-10-30, preserved by lead under read-only reviewer contract.
Retained Sol/xhigh, no overrides/delegation. Bound tracking-current identity
verified with trusted binding and absent environment markers. Mandatory skill
and applicable lanes read/reused; current scope restricted to isolated helper,
diagnostic integrity/docs, narrow generic fallback diff and final history.
Unaffected application/UI/template reviews retained.

**No Blocking or Important findings. Source cleared for requested test-helper
correction and final consolidated range.** Not a hosted11.8 CI pass, guest
integration pass, production DB qualification, deployment or merge approval.

## Exact source/history

`ac10a62f1cb0fc890378ae83cdf18dd0e29f049a..4d72e3e754fd47b598de1e54e05b3c5d26c62200`:

-8beecad4492840be353a14a1f861e2d535847323 backend.
-52b794ef8fdd92474e558ec000cafebbe2be3934 unchanged legacy patch.
-4d72e3e754fd47b598de1e54e05b3c5d26c62200 isolated testenv/docs.

Final tree588e65a8a13e3da69483cbf4c44cdfac84694a9e equals retained tested
preconsolidation tree; tracked/index clean, disposable PHPUnit cache only.
Merge-base correct; exact-range diff checks pass. Three coherent commits,
patch-equivalent legacy '=' in range-diff, no obsolete fixups/abandoned behavior
or repeated dependency/input/generated-pin streams. No dependency/pin updates
in this correction. Exactly one feature migration20261030180000; migration/core
schema byte-identical to cleared5a59ead4, no new/transitional migration or guards.
Owner provenance remains no merge/release/deployment/external persistence;
disposable local DBs only. Reactb67c7917/templates e8c2c3d unchanged, no migrations.

## Test-only setting and consumers

Parent52b794ef..4d72e3e7 changes only tools/test_db.rb and tests/README.md.
Sole behavior choice is --innodb-snapshot-isolation=OFF when the existing helper
spawns isolated mariadbd with --no-defaults. Transaction isolation, locks,
application SQL, retry behavior, assertions and production settings unchanged.
Existing query logs actual version/tx_isolation/snapshot and raises on failure.
Configured DATABASE_URL/database.yml bypasses auto_start as before. API and
libnodectld share SpecDbSetup; both hosted plugin modes use automatic helper.
Conventional scope explicitly preserves prior local server semantics rather
than adding retries or weakening data-integrity checks.

## Diagnostic evidence independently inspected

Both old hosted foundation groups:1459examples/30failures, all in six enumerated
files. Those files byte-unchanged across base..final, expectations unweakened.
Representative cluster-resource test establishes an old RR snapshot and needs
locking reads of concurrent current usage/budget to prevent lost updates.
Local11.4.12/RR/OFF passes1/0; same example11.4.12/RR/ON fails1/1 with exact
record-changed error. This is meaningful negative control, not blind rerun.
Corrected native core/full each64/0 across the six affected files, fresh helper
output11.4.12/OFF/REPEATABLE-READ. Final source retains accounting, ownership and
MFA invalidation checks.

Reviewer independently read official MariaDB tags:11.4.12 ha_innodb.cc854-856
snapshot defaultFALSE;11.8.6 lines865-867 defaultTRUE. Hosted package logs show
11.8.6-5ubuntu0.1 both modes. Correction restores documented11.4 semantics in
disposable servers. This does not prove every old hosted failure disappears
on11.8: native corrected checks used11.4, so exact final hosted settings/results
remain required. Production module source has its own READ-COMMITTED default,
further separating it from RR spec semantics; no production server inspected
or live/default-upgrade support claimed. Future snapshot qualification explicit.

## Generic fallback boundary

dbfd2bbf..8beecad4 changes only two generic English bodies: replace site
membership paragraph with generic memory advice, remove external vpsFree
incident-KB paragraphs. Worker/memory/shared-node advice, counts, internal link,
conditional consequences and past autostart effect retained. Restores existing
generic-content contract; actual site templates e8c2c3d/user links unchanged.
Native29/0 content/render/New/Send evidence retained, assertion unchanged.
No full prose/application re-review required for narrow correction.

## Limits/next action

Reviewer performed read-only source/history/log checks only, no tests/builds/
CI/browser actions or edits. Corrected source may publish and proceed to
selected exact-head hosted/guest verification. Old failed hosted results remain
failed evidence;64/0focused runs are not a full-suite proof. Old-head image
outputs remain cache preparation only. KB197 assessment stays exact to oldpin;
refresh consistent mechanical pins after final publication. Guest/capture
capacity, fourPNGs, merge and deployment remain separate. Session stays open.
