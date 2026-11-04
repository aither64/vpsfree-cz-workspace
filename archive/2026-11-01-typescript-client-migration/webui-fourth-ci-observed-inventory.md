# Fourth CI observed inventory — 2026-11-02

Exact published head **20aa0e9ea7568747f048242077f0cf15a325d990**, attempt1. [Core41508552632](https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41508552632) passed all3jobs. [Smoke41508552554](https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41508552554) ended cancelled; WebKit succeeded and both Chrome jobs were cancelled. Watcher exit0 means monitoring completed, not CI acceptance.

| Native job | Raw UTC start → finish | Duration | Observed scope |
| --- | --- | --- | --- |
| Chromium125494067761 |19:17:31→19:58:18|40m47s|632selected;10failing headings;partial|
| mobileChrome125494068046 |19:17:41→19:58:12|40m31s|574selected;10failing headings;partial|
| WebKit125494068271 |19:17:31→19:40:43|23m12s|276selected;274passed,2skipped terminal|

## Failures and overlap

**20 observed project-specific failing headings,16 distinct titles ignoring engine,6files.** The [machine-readable inventory/member map](webui-fourth-ci-observed-selection.json) records exact run/job/project/executed title/source position/log line, first inline and expanded failure text, retry observations and original member identities. All20cases show explicit retry1/2 output. Repeated error echoes/retry labels do not add cases.19inline records corroborate20expanded headings; the expanded-only case is listed separately. Historical Chrome testIds remain null where original metadata did not supply them.

| Spec (`e2e/specs/`) | Chromium | mobileChrome |
| --- | ---: | ---: |
| `app/vps_lifecycle_tab_actions.spec.ts` | 4 | 4 |
| `app/vps_list_action_failure_feedback.spec.ts` | 2 | 2 |
| `app/vps_maintenance_mobile.spec.ts` | 1 | 1 |
| `app/vps_power_stop_confirm.spec.ts` | 3 | 0 |
| `app/vps_private_ip_availability.spec.ts` | 0 | 2 |
| `app/vps_resource_workspace.spec.ts` | 0 | 1 |

All6paths and20case identities are disjoint from prior30/27/third11repair inventories and local220/local118cases. The earlier two old/new admin-layout title mappings remain preserved as historical mappings; none applies to these new paths. Four failing titles appear in both Chrome projects; six appear only in each. This is observed scope, not proof of an engine-specific cause or new regression.

All lines refer to517270-byte `webui-third-ci-final-ci/smoke-run.log`. First emitted Chromium failure442: `vps_lifecycle_tab_actions.spec.ts:125`, allocation override scenario; assertion134 cannot find `vps.config.admin_override`. First mobileChrome failure1550: `vps_list_action_failure_feedback.spec.ts:39`; assertion70 expects `vps.list.power_confirm` hidden, receives visible. These are failure boundaries, without source/root-cause diagnosis.

Chrome cancellation messages are999/2055. **No Chrome terminal failed/passed/skipped/unrun totals exist here**, so none are inferred from absent headings or incomplete progress. Both actual check-run annotation responses explicitly state **“The job has exceeded the maximum execution time of 40m0s”**; no actor is inferred. MobileChrome uses retained `mobile-chrome-annotations.json`. Chromium's raw response was missing from the initial allowed inputs; that original observation and watcher/404/empty capture remain preserved. Parent subsequently supplied `chromium-check-run-annotations-final.json`, now cited separately and hashed. No inventory-owner status/log polling occurred. Parent source/six-job proof is `webui-third-ci-final-ci-lead-result.json`, SHA256 `d0a68d3549ed7821c5bfcd9d09c165a961823b7d92cbdb5f24ef39cb59d9a9fe`.

## Released original evidence

The minimum failed-identity cover uses10mobileChrome originals plus6additional Chromium originals. Both same20aa archives were authorized, fetched once through existing `gh api`, and verified against retained run/head metadata. Old9d archives remain historical, not substitutes for these originals. The separately authorized small WebKit report settles only its eight touched per-case outcomes.

| Acquired artifact | Bytes | SHA256 |
| --- | ---: | --- |
|13174362819 playwright-test-results-mobile-chrome|94461738|`fd32c2d12167fe7d68f137bf102dc9183a84fe72bdfe760ea27c9383bcf7f58f`|
|13175251820 playwright-test-results-chromium|132233790|`d4e1874908335f1b28a9d5ef6197fb810563e03a1e3db1afac1d4e320d114224`|
|13173361437 playwright-report-mobile-webkit|2529089|`4920588c39ba78d9467c41b4d63c42c4210f36e3a5cca71455953f61fb09c7c5`|

Archives are under [webui-fourth-ci-evidence/](webui-fourth-ci-evidence/). Transfers exited0 in11.768s/11.150s/2.343s respectively; all handles are terminal. MobileChrome/Chromium/report indices contain292/295/14members. No extract-all, selected trace copying, retries or overwrite occurred. Duplicate WebKit test-results artifact13173029184(17423857bytes) was not acquired.

`minimum_evidence_selection.mapping` in JSON supplies every selected exact case, archive path, **original retry0** trace/error-context member, size and SHA256. Original context Name and source location match the executed heading; truncated ZIP directory names were not guessed. Owners can read `ZipFile(archive).read(member)` and nested trace ZIPs in memory. The four shared-engine observations remain recorded even though their minimum selected evidence uses one engine. No cross-engine equivalence or common cause is claimed. Exact mapping/locations were sent to architect0; no source/causal audit was performed here.

## WebKit: dots-only limit resolved by actual report

The native log3564–3567 genuinely totals274passed/2skipped, but names **none** of the8touched cases and cannot prove their individual retries. The same-head report was decoded once in memory: its actual8testIds/project/files/describes/current titles match the historical touched preflight identities, and **each has exactly one expected/passed result, retry0, no errors**. JSON retains those8actual observations and their detail-member hashes. This is direct20aaWebKit evidence, not Chrome projection; the earlier2ad8local page-setup failure remains unchanged in its original receipt.

The report's two skipped cases are separately preserved, not counted as passes:

- `e2e/specs/admin/ip_addresses_filters_pagination.spec.ts`: admin IP addresses traverse ascending API pages and paginate loaded rows locally.
- `e2e/specs/app/mobile_touch_interactions.spec.ts`: compact mouse controls retain their desktop height.

Report stats:276total/274expected/2skipped/0unexpected/0flaky; report errors empty. Parent owns acceptance of this narrower WebKit evidence and the still-incomplete Chrome workflows. No browser/check/build/Nix/install/Git/index/source/docs-worklog/API/DB/server/CI-control/PR/publication/default/deployment/lifecycle action occurred. Original reports, traces and receipts remain unchanged; user release transition stays pending and the session stays open.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-typescript-client-migration/
