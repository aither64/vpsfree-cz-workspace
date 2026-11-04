# Second published CI diagnosis — 2026-11-02

[Run41450042371](https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41450042371), attempt **1**, pull-request event, exact head **d3d5efbef53af8eb1caec025737dc47ecbc67e96**, ended cancelled. Each check-run annotation explicitly states **“The job has exceeded the maximum execution time of 40m0s”**. This establishes the job cap; no human cancellation actor is inferred. Genuine assertions preceded cancellation. Companion CI41450042642 passed all3jobs (retained watcher receipt).

## Scope and counting

| Job | Exact job URL | Selected | Observed failing headings |
| --- | --- | ---: | ---: |
| Chromium | [125292707311](https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41450042371/job/125292707311) |632|32|
| mobileChrome | [125292707754](https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41450042371/job/125292707754) |574|30|
| mobileWebKit | [125292707684](https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41450042371/job/125292707684) |276|41|

**103 project-specific headings,70 unique test identities ignoring project,27spec paths.** No completed suite totals survived. These counts describe observed failures, not all executed cases. The source is retained combined log `webui-e2e-41450042371.log`; all line numbers below are global lines there.

Actual commands:

- Chromium427: `npm run e2e:pr:desktop` → `npm run env:check && E2E_START_SERVER=1 node scripts/playwright.mjs test --pr-smoke --project=chromium --workers=2`; selected count434.
- mobileChrome6129: `npm run e2e:pr:mobile` → same driver with `--pr-smoke-mobile --project=mobile-chrome --workers=2`; selected count6136.
- Actual mobileWebKit3573: `npm run e2e:touch:webkit` → same driver with `--project=mobile-webkit`; selected count3580. This runs configured WebKit testMatch without a PR-only tag filter.

Published `playwright.config.ts:42–45`:90s testcase timeout,15s expect timeout,two workers,two CI retries. Cancellation lines:2062/7646/5576 respectively.

Method: parse expanded `##[error] N) [project] › spec:line:column › title` headings, deduplicate retry repeats by project+ordinal+full title. Ordinals are contiguous1–32/30/41. Independently parsed GitHub inline error headings corroborate101cases; Chromium24 and WebKit14 appear only as expanded headings, inspected directly at1601/4203. Negative test titles are never counted as outcomes. Every case has its first error and log line. Complete titles/paths/first errors/locators/retry occurrence lines are in [JSON](ci-41450042371-diagnosis/test-failure-summary.json) and [TSV](ci-41450042371-diagnosis/failures.tsv).

## Comparison

All27paths and103headings are **newly observed and outside** the prior run41366168907’s30-path/109-heading inventory and local100-case mapping. Comparison strips source positions and `e2e/specs/` prefix, retains engine, and separately permits the recorded WebKit→mobileChrome substitution: still zero overlap. No prior artifacts were downloaded again. Absence from this failure stream neither certifies old cases passed nor dates these newly observed defects.

Chromium/mobileChrome share28identities. WebKit shares5with either Chrome project;36appear only in WebKit here. Different selection and timeout progress prevent calling those36engine-specific defects. Prior local substitution supplied no native WebKit proof. [Structured comparison](ci-41450042371-diagnosis/comparison.json).

| Newly observed spec (`e2e/specs/`) | Chromium | mobileChrome | WebKit |
| --- | ---: | ---: | ---: |
| `app/dataset_download_delete_confirm.spec.ts` | 3 | 3 | 0 |
| `app/dataset_downloads_keyset_pagination.spec.ts` | 2 | 2 | 0 |
| `app/dataset_snapshots_keyset_pagination.spec.ts` | 2 | 2 | 0 |
| `app/dns_record_type_capabilities.spec.ts` | 1 | 1 | 0 |
| `app/dns_relation_delete_failures.spec.ts` | 2 | 2 | 0 |
| `app/dns_tsig_keys.spec.ts` | 1 | 1 | 0 |
| `app/dns_zone_delete.spec.ts` | 1 | 1 | 0 |
| `app/dns_zone_logs_keyset_pagination.spec.ts` | 2 | 2 | 0 |
| `app/dns_zone_records_live_contract.spec.ts` | 1 | 1 | 0 |
| `app/export_delete_failures.spec.ts` | 2 | 2 | 0 |
| `app/known_devices_keyset_pagination.spec.ts` | 2 | 2 | 0 |
| `app/monitoring_event_action_feedback.spec.ts` | 1 | 1 | 0 |
| `app/profile_mail_settings_failure.spec.ts` | 1 | 1 | 0 |
| `app/profile_metrics_tokens.spec.ts` | 0 | 2 | 0 |
| `app/profile_mfa_recovery.spec.ts` | 1 | 1 | 0 |
| `app/profile_user_namespaces.spec.ts` | 2 | 2 | 0 |
| `app/security_advisories_admin.spec.ts` | 2 | 2 | 0 |
| `app/snapshot_delete_availability.spec.ts` | 3 | 1 | 4 |
| `app/snapshot_export_shortcut.spec.ts` | 2 | 1 | 2 |
| `app/storage_sections_contract.spec.ts` | 1 | 0 | 0 |
| `app/transactions_readability.spec.ts` | 0 | 0 | 2 |
| `app/transactions_table_followup.spec.ts` | 0 | 0 | 6 |
| `app/vps_admin_modifications.spec.ts` | 0 | 0 | 8 |
| `app/vps_console_controls.spec.ts` | 0 | 0 | 4 |
| `app/vps_console_page.spec.ts` | 0 | 0 | 9 |
| `app/vps_console_viewport.spec.ts` | 0 | 0 | 2 |
| `app/vps_dns_shortcut.spec.ts` | 0 | 0 | 4 |

## First shared Chrome boundary

`app/dataset_downloads_keyset_pagination.spec.ts:67`, “next/prev updates URL and rows”, fails at76: `dataset.downloads.list` invisible (Chromium438/441,mobileChrome6140/6143). The **original mobileChrome trace**, without a retry suffix, records:

- Two `GET /api/v7.0/datasets/10?_meta[includes]=vps%2Cenvironment%2Cdataset_expansion%2Cuser%2Cparent`, HTTP200 (network events425/427,zero-based).
- Body `{status:true,response:{id:10,full_name:...,name:...,vps:...}}`: fields directly under `response`, **no `response.dataset`**.
- Generated `dist/generated/resources/dataset/actions/show.js:8` declares `outputNamespace:"dataset"`; HaveAPI0.32 `dist/haveapi-client.js:3119–3121` rejects the missing namespace. The caught Error object is not exposed by this trace, but the wire key mismatch and decoder branch are concrete.
- Snapshot shows **“Failed to load dataset Please try again.”**; **zero snapshot_downloads requests**. The list locator is a downstream symptom before pagination executes.
- Fixture14–25/48 returns a bare dataset; `e2e/fixtures/haveapi.ts:266–271` wraps only the success envelope. `src/lib/api/datasets.ts:108–114` invokes generated Show before its output guard. These inspected source bytes match published d3d5 and local6c755ea2.

This establishes this case’s response-framing mismatch only. It does not classify all103failures or prove a complete repair. WebKit’s first failure is `snapshot_export_shortcut.spec.ts:7`, member NFS export:59 `pickerLoaded` remains false (3584/3587); this initial package did not inspect that trace.

## Retained artifacts and next action

[Evidence directory](ci-41450042371-diagnosis/) contains fresh run/jobs/check annotations/artifact metadata, inventories, compact boundary and hash receipt. GitHub metadata:

| ID / project | Bytes | SHA256 |
| --- | ---: | --- |
|13146254501 Chromium|220285501|`29cbde48a4bf598a288121b084ee7848aae30de59b3a459ba75ca2109fe37b05`|
|13145688796 mobileChrome|143921874|`f57ce6fb0241d75aa347812f1cc6eead72e813ff282c29ff7732e6a061afb136`|
|13145774201 mobileWebKit|238507673|`77ad2523674f838e24167d38567133de8efd04112d15270c90c10e4969b0ab18`|

Initial diagnosis downloaded only mobileChrome and verified its full digest. Local `playwright-test-results-mobile-chrome.zip` has489entries indexed in `artifact-index-mobile-chrome.json`. Selected original member: `app-dataset_downloads_keys-fa24e-t-prev-updates-URL-and-rows-mobile-chrome/trace.zip`. Only its569564-byte trace and6348-byte error context were extracted into `selected-evidence/`. Nested network `0-trace.network`; dataset body resource `07fa1a1dcf6e7a9928cb26473f537acc8817e062.json`. Compact boundary excludes headers/auth. Reuse local ZIP/index for other mobileChrome failures.

Architect subsequently requested **only** the WebKit archive centrally for seven paths lacking mobileChrome traces; its verified archive/index receipt is reported separately. No Chromium archive retrieval or whole-archive extraction. Remaining failure causes and actual browser differences require owner diagnosis; no blanket fixture conclusion.

Next: architect groups27paths and assigns read-only owner diagnosis using these traces, distinguishing response-framing/field/error mismatches from application or browser defects before repairs. No source/check/browser/CI mutation/install/API/DB operation occurred. No product documentation update is appropriate for temporary failed-run evidence; lead owns aggregate state reconciliation.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-typescript-client-migration/
