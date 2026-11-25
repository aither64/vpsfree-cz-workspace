# Legacy incident escalation CI diagnosis, 2026-11-13

Complete bounded read-only diagnosis for lead/owner0. No application/Git mutation,
check or workflow rerun, guest, dependency install or runtime action. Owner0 owns
the proposed test correction. Ordinary incident-report localization remains
architect0's separate design package.

## Conclusion

The first failure in `webui#incident-escalation` is a stale test assertion at
`tests/playwright/webui/specs/incident-escalation.spec.cjs:58`. It expects the
localized registered incident-type label inside a heading landmark. The generic
heading is correctly localized, and the exact expected type label is present in
the adjacent details-table row. This failure establishes a test selector/scope
mismatch; it does not establish a missing production translation or fixture defect.

## Exact source and preserved evidence

- Hosted run: `41185457135`, job `124491363934`, old immutable source
  `f60d41a453b1703e42de4341285bdc6ba339aff0`.
- Owner0 supplied rebased immutable source
  `c02f56e1c45d6dfeb4f5fbfbee486ee584ef1460`, onto
  `2d0946c4e699aa61092228d8a7cb275477ee46d0`.
- Read-only `git diff` between those two exact feature heads for the failing
  browser spec, `webui/forms/incident_policy.forms.php` and
  `webui/template/template.html` is empty. The same correction applies to the
  rebased architecture; no working checkout was relied on during the rebase.
- Preserved log, relative to this session tracking directory:
  `shared-f60-ci-completion-artifacts/vpsadmin-test-logs-41185457135/os-test-webui-fd1a3b33/test-runner.log`.
  SHA256 `e809f20ffa6887db2aab4d2f989eb2e108834b56a00f9e6c6444fc2a6223583a`.
- Run/job/SHA receipt: `shared-f60-ci-completion-status.json`; preserved original
  outcome: `shared-f60-ci-completion-result.md`.

Log lines 26727–26730 identify script entry and failure:
script started 2026-10-31 11:27:22 +0100; the single browser example started
11:29:17 and failed at 11:34:04 after 286.92s.

Lines 26771–26792 identify the first failing assertion:

```text
Locator: locator('[data-vpsadmin-doc-id="vps.oom-details"]')
Expected substring: "Incidenty přetížení paměti VPS"
Received string: "Opatření při opakovaných incidentech"
Timeout: 20000ms
23 × locator resolved to <h2 data-vpsadmin-doc-id="vps.oom-details">…</h2>
specs/incident-escalation.spec.cjs:58:74
```

The captured page snapshot at lines 26973–26979 already proves both translations:

```text
heading "Opatření při opakovaných incidentech" [level=2]
row "Typ incidentu: Incidenty přetížení paměti VPS"
  cell "Typ incidentu:"
  cell "Incidenty přetížení paměti VPS"
```

No new artifact download or broader log sweep was needed. Only this script's
preserved failure window/snapshot and its immutable production/test source were
inspected. Raw snapshot URLs/tokens were not copied into this report.

## Source explanation and smallest correction

`webui/forms/incident_policy.forms.php:113` renders the generic `Incident
escalation` heading through `table_title(..., 'vps.oom-details')`; line114 renders
`Incident type` and the API's localized `incident_policy_label` as a separate row.
`webui/template/template.html:181` places that documentation attribute on the
`h2`, not the table. The observed DOM matches this contract.

Owner0 can correct only the browser spec, importing the already-exported
`detailRow` helper and replacing the wrong assertion with these two assertions:

```js
await expect(page.locator('[data-vpsadmin-doc-id="vps.oom-details"]'))
  .toHaveText('Opatření při opakovaných incidentech');
await expect(detailRow(page, 'Typ incidentu').locator('td').nth(1))
  .toHaveText('Incidenty přetížení paměti VPS');
```

`detailRow` already exists at `tests/playwright/webui/lib/pages/webui.cjs:73`
and is exported at line538 in rebased c02f56e1. No new helper, fixture, markup,
semantic ID, locale, product behavior or timing adjustment is needed. Keep the
existing landmark and assert the type value where production renders it.

## Verification limits and handoff

The old execution reached line58: preceding summary/settings/filter/member-read/
write-rejection assertions completed before this failure. Assertions after the
Czech check (English restoration and final administrator reset/readback) did not
execute, so this diagnosis does not claim that the entire browser test passes.

Owner0's follow-up should use the smallest relevant static/syntax check and then
an authorized single `webui#incident-escalation` browser result when the lead
releases that verification phase/capacity, under ordinary committed-source and
independent-review gates. No rerun is authorized or performed by this package.
This is a finite diagnosis; generated-client synchronization is a separate next
package dependent on owner0's final committed API schema export and lead brief.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/>.
