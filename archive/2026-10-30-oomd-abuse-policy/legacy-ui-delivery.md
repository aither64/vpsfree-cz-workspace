# Legacy OOM UI delivery

Package owner: implementer1. Source prepared in the shared vpsAdmin feature
worktree on `2026-10-30-oomd-abuse-policy`, initial base
`ac10a62f1cb0fc890378ae83cdf18dd0e29f049a`. Implementer0 retains all Git
ownership and the shared browser registry/CI wiring. No migration belongs to
this UI package. No commit, push, merge, deployment or long browser run was
performed by implementer1.

## Delivered behavior

- VPS list uses the server batch summary for 7-day/warning and 30-day/shutdown
  count-to-effective-limit ratios, threshold status and stop exemption.
- Existing admin list filters status and stop permission. Empty filtered lists
  retain controls through advertised summary capability; unavailable old API
  fields never render zero counts.
- Detail shows modes, permission and active enforcement separately, incident
  history, queued warning time, last confirmed stop, outstanding pending/failed/
  uncertain action with transaction link, ownership accounting boundary and
  cooldown. Wording says a new incident at or after cooldown expiry is required;
  expiry does not schedule a stop.
- Admin-only CSRF-protected POST saves overrides and stop permission. Empty
  overrides explicitly send null; reset sends only the two null override values
  and preserves exemption. Server-side final-pair validation errors remain visible.
- Older API views hide the feature. Owners see summary/history but no controls;
  crafted owner writes are rejected before API calls.
- Czech/English prose accepted by lead. Exact final entries are recorded in
  [legacy-ui-strings.md](legacy-ui-strings.md).

## Exact commit paths

```text
webui/forms/oom_policy.forms.php
webui/forms/vps.forms.php
webui/pages/page_adminvps.php
webui/public/index.php
webui/tests/Regression/OomPolicyTest.php
webui/lang/locale/vpsAdmin.pot
webui/lang/locale/cs_CZ.utf8/LC_MESSAGES/vpsAdmin.po
webui/lang/locale/cs_CZ.utf8/LC_MESSAGES/vpsAdmin.mo
tests/playwright/webui/specs/oom-policy.spec.cjs
```

Exclude `webui/.phpunit.cache/` and dependency/vendor artifacts. Shared API,
technical documentation and registry files belong to implementer0.

## Quick-check evidence

Pinned repository `nix develop .#webui` shell: PHP 8.4.24, PHPUnit 13.4.5.

- Full existing PHP suite (`composer test`): exit 0, 116 tests/803 assertions,
  18.9s. One existing PHP deprecation in untouched
  `webui/lib/pagination.lib.php:151` (implicitly nullable `$action`) is triggered
  by nine NetworkAvailabilityTest examples. Targeted diagnostic run confirms it;
  no OOM regression emits a deprecation.
- Final OOM tests after strengthening the fixture to exercise actual client
  validation and JSON transport: exit 0, 9 tests/65 assertions, 1.7s. Explicit
  null and false survive serialization to the PUT request envelope. Only this
  test fixture changed after the full run; application source stayed unchanged.
- `lang/scripts/locales-update` followed by `--check`: passed. Existing embedded
  URL gettext warnings in oom_reports/page_index are unchanged.
- PHP lint on all five touched/new PHP files: passed.
- PHP-CS-Fixer 3.95.1 using the repository `.php-cs-fixer.dist.php`, explicit
  owned paths and no cache: passed; dry run reports no files to fix. Multiple
  explicit paths require `--config=.php-cs-fixer.dist.php`.
- Browser scenario Node syntax and `git diff --check`: passed.

Logs: `/tmp/oom-webui-all-quick.log`, `/tmp/oom-webui-focused.log`,
`/tmp/oom-webui-final-lint.log`, `/tmp/oom-webui-formatter-check.log`.
Required commit hooks remain implementer0's responsibility at commit time.

Follow-up read-only source crosscheck against implementer0's actual backend
confirms identical flat summary/settings names, nullable override metadata,
Index filters and owner output whitelist. `tests/suite/webui.nix` registers
`oom-policy`; shared CI tag/selection wiring is present. No source mismatch was
found. No live service or schema export was launched; schema export requires
committed source and is unnecessary for this source-level contract check.

## Deferred checks and KB scope

Browser source covers ordinary fixture VPS creation, count/override ratios,
exemption, empty results, owner read/write boundaries, Czech heading and explicit
reset preserving exemption. It has not run: intended commits and quick checks
must precede mandatory independent final review, then long checks.

Exactly two existing screenshot concepts change, each in cs/en (four PNGs):
`getting-started/vps-list` and `restore-backups/playground-vps-list`. Existing
zero-event fixtures display 0/5 and 0/10; no new capture scenario is needed.
The OOM detail section is appended after the unchanged first/base table, outside
`getting-started/vps-details`'s h1+first-table crop. Existing semantic IDs retain
their intent. Implementer3 owns the bounded canonical contract follow-up,
waiting for the complete published backend+legacy revision.

Session remains active and open:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/>.
