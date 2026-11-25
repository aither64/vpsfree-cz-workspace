# Legacy UI: common incident escalation rework

2026-10-30. Released common contract implemented; final legacy quick checks pass.
Package awaits owner0's coordinated commit/consolidation and independent review. Scope is `webui/` only. Implementer0 owns
all vpsAdmin Git operations, browser scenario/registry coordination and coherent
backend/legacy history consolidation. Heavy images, guests, browsers and builds
remain held. No dependency restoration was launched during preparation.

## Preserved original source and evidence

Read-only inventory before rework:

- Base: `ac10a62f1cb0fc890378ae83cdf18dd0e29f049a`.
- Final original head: `4d72e3e754fd47b598de1e54e05b3c5d26c62200`.
- Both `refs/heads/2026-10-30-oomd-abuse-policy` and its origin-tracking ref
  currently name that exact head; neither was changed by implementer1.
- Full original series: backend
  `8beecad4492840be353a14a1f861e2d535847323`, legacy UI
  `52b794ef8fdd92474e558ec000cafebbe2be3934`, shared MariaDB test fix
  `4d72e3e754fd47b598de1e54e05b3c5d26c62200`.
- Existing older original review ref:
  `refs/review/2026-10-30-oomd-abuse-policy/vpsadmin-original` points to
  `51297de1a05fee60aaba8a31e443abf95675396c`; it is not the final original head.
  Implementer0 preserved the exact current final head under
  `refs/review/2026-10-30-oomd-abuse-policy/vpsadmin-before-shared-incident-rework`
  before history changes; implementer1 independently verified that ref.
- Current source is committed; only untracked `webui/.phpunit.cache/` is present.
- Preserve [original delivery evidence](legacy-ui-delivery.md),
  [original copy inventory](legacy-ui-strings.md),
  [original review packet](review-packet.md),
  [review follow-up](review-followup.md) and
  [integration/verification receipts](integration-verification.md) unchanged.

## Required contract dependencies

- Selected registered type parameter, default and display-label availability.
- Exact common summary fields and per-type override settings, distinguished from
  VPS-scoped stop permission/cooldown/outstanding-action state.
- Index filter names, selected-type propagation and explicit-null reset envelope.
- Missing-field capability fallback for older APIs.
- Incident history codename/registered-type link contract.

Adapt the existing list/detail/settings without an extra rule editor or menu.
Preserve threshold/cooldown semantics, owner reads/admin writes, validation,
CSRF, nullable reset and pending/failed/uncertain vs confirmed-stop behavior.
Existing process-level OOM-report/rule pages remain independent and untouched.
Final English/Czech copy remains lead-owned after technical facts settle.

## Delivered common UI package and final checks

The released contract is implemented; this package now waits for owner0's
coordinated commit. Original range/ref/evidence above remain preserved.

- Renamed helper/form to `webui/forms/incident_policy.forms.php` and regression
  to `webui/tests/Regression/IncidentPolicyTest.php`, deleting their old feature
  names. No runtime aliases for unreleased OOM feature fields.
- Uses numeric `incident_count_7d` plus returned `incident_policy` for capability,
  escaped localized `incident_policy_label`, selected count/effective limits and
  history codename. Old APIs omit new query parameters and hide the feature.
- Explicit selector is carried through list filters, detail links, forms/error
  refresh, save/reset and selected readback after synchronous update. Reset
  preserves the shared exemption; unrelated POST fields stay outside the update.
- Shared VPS-wide exemption/cooldown/outstanding-state help and memory-only
  protection help use lead's exact accepted EN/CS. Final copy inventory:
  [legacy-incident-ui-strings.md](legacy-incident-ui-strings.md).
- Semantic IDs `vps.oom-summary`, `vps.oom-details`, `vps.oom-settings` retain
  existing intent. Existing process OOM pages/rules and incident-report flows
  remain untouched. Owner0's permanent docs distinguish per-type counts/limits/
  warnings from shared permission/cooldown/outstanding stop.

Final quick checks on original committed `4d72e3e754fd47b598de1e54e05b3c5d26c62200`
plus uncommitted common rework, in repository `nix develop .#webui` (PHP8.4.24,
PHPUnit13.4.5):

- First focused batch via fresh retained-catalog Luna/low watcher: exit0,
  13tests/92assertions, ~12s with shell. Actual client validation/JSON encoding,
  null/false, explicit selected readback, numeric+type capability, synthetic
  second-type label/count/limit/history, escaping and memory-help isolation.
- Final complete suite after final source/locale/formatter: exit0,
  120tests/832assertions,19.4s. Same existing pagination.lib.php:151 implicit
  nullable parameter deprecation as previously diagnosed; no new failures.
- Gettext regeneration/--check, all5PHP lint checks, scoped PHP-CS-Fixer3.95.1
  dryrun and git diff --check -- webui passed. Existing embedded-URL gettext
  warnings in oom_reports/page_index unchanged.

Logs: /tmp/incident-legacy-pinned-focused.log,
/tmp/incident-legacy-final-quick.log,/tmp/incident-legacy-format-check.log.
A preliminary root-CWD PHPUnit invocation printed usage only; corrected pinned
shell evidence above is authoritative. Composer reported no updates/installations;
no dependency or heavy allocation was needed. No runtime/service/browser/image,
Git mutation, publication or deployment by implementer1.

Exact owner0 commit handoff (10paths,2renamepairs):

```text
DELETE webui/forms/oom_policy.forms.php
ADD    webui/forms/incident_policy.forms.php
MODIFY webui/forms/vps.forms.php
MODIFY webui/pages/page_adminvps.php
MODIFY webui/public/index.php
DELETE webui/tests/Regression/OomPolicyTest.php
ADD    webui/tests/Regression/IncidentPolicyTest.php
MODIFY webui/lang/locale/vpsAdmin.pot
MODIFY webui/lang/locale/cs_CZ.utf8/LC_MESSAGES/vpsAdmin.po
MODIFY webui/lang/locale/cs_CZ.utf8/LC_MESSAGES/vpsAdmin.mo
```

Exclude webui/.phpunit.cache. No UI migrations. Owner0 owns browser source,
registry/CI, hooks and coherent backend+legacy history consolidation. Complete new
final head/series awaits owner0; independent affected review remains required
before long verification/publication.

KB impact stays getting-started/vps-list and restore-backups/playground-vps-list,
cs/en4PNGs; column now shows localized registered-type label. Detail appends after
unchanged base table, outside existing first-table crop. Owner3's bounded new
pin/capture package waits final combined source and capacity release. No broader
capture scope or React certification.
