# Final CI diagnosis

Run [41366168907](https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41366168907),
PR126, attempt1, exact head `14cfdcb6d2a3bc337fd445932fd38916b3dcd9ab`.
Read-only diagnosis captured 2026-11-02T01:02:39.534696+00:00. This smoke run is **incomplete**, with real
assertion failures before cancellation. The accepted core CI run41366168908 and
local A124/B8, isolated API23, package and review evidence retain their own scope.

## Supported cancellation cause

All three check-run annotation APIs explicitly report:
`The job has exceeded the maximum execution time of 40m0s`.
This establishes native job timeout. The committed workflow sets
`timeout-minutes: 40`; its desktop30-minute comment is an estimate.
The run's trigger/actor fields do not identify a cancellation actor. No evidence
supports replacing the native timeout diagnosis with actor/concurrency inference.
All three E2E steps ended cancelled; their later artifact steps succeeded.
No rerun, dispatch, cancellation or timeout/selection change was performed here.

## Selection and observed progress

| Project | Job ID | Selected tests | Observed failing-case headings |
| --- | --- | ---: | ---: |
| chromium | 125026671252 | 632 | 32 |
| mobile-chrome | 125026671433 | 574 | 35 |
| mobile-webkit | 125026671379 | 276 | 42 |

Commands in the native logs match the committed workflow/package scripts:

- Chromium: `npm run e2e:pr:desktop`, expanding to the existing
  `--pr-smoke --project=chromium --workers=2` shortcut.
- Mobile Chrome: `npm run e2e:pr:mobile`, using
  `--pr-smoke-mobile --project=mobile-chrome --workers=2`.
- WebKit: `npm run e2e:touch:webkit`, using `--project=mobile-webkit` and its
  configured complete testMatch list, not the PR-tag-only selection.

The shortcuts map to the documented tag grep in `scripts/e2e-harness.mjs`.
CI configuration uses two retries and two workers. The selected matrix is broader
than local A/B. All jobs reached tests after successful setup/toolchain/browser
installation. Native logs end at cancellation without terminal pass/skip/completed
counts; uploaded artifacts contain no `.last-run.json` or complete HTML report.
Exact completed coverage therefore cannot be recovered from those receipts.
The counts above come from numbered GitHub reporter error records, not occurrences
of the word "failed" in negative-test titles. They are not final suite totals.

## First actionable boundary and next check

The first reported failure in all three projects is
`admin/admin_dashboard.spec.ts:78`, Czech news shortcut, assertion91:
`expect(card).toContainText(...)`, locator `app.dashboard.news.card`.
The card displays its news-load error. Original-attempt traces for all three
projects are extracted under `selected-evidence/<project>/`.
Their mocked `GET /api/v7.0/news_logs` returns HTTP200 with `news_logs` rows
containing `id`, `published_at`, `cs_message`, `en_message` and no `message`.
`src/lib/api/newsLogViews.ts:32` requires a localized string `message`;
`e2e/specs/admin/admin_dashboard.spec.ts:58` supplies the stale fixture.
This is a concrete fixture-boundary candidate for the existing content owner,
not evidence to relax the guard. Other failure causes have not been diagnosed.

Shortest next step: architect0 owns the bounded common-boundary triage and grouped
original-owner brief using these retained traces. After that brief and the
assigned owner's bounded correction, the existing prepared Chromium environment
can check the two news-shortcut cases with retries disabled:

```sh
E2E_START_SERVER=1 node scripts/playwright.mjs test e2e/specs/admin/admin_dashboard.spec.ts --grep 'news administration shortcut' --project=chromium --workers=2 --retries=0 --max-failures=1 --global-timeout=180000
```

This command is proposed, not executed or authorized by this diagnosis. The architect brief will route the remaining observed failures by their existing
domain owners using the inventory below and retained traces. Do not rerun the full timed-out matrix or
increase its budget before the demonstrated failures are addressed. The broader
CI gate remains pending even if a focused fixture check passes.

## Failure-path inventory

Columns count observed project-specific testcase headings, including locale or
scenario variants. `test-failure-summary.json` retains every title, original
error, locator, timestamp and exact job-log line. Multiple projects overlap.

| Spec | Chromium | Mobile Chrome | WebKit | First error at this path |
| --- | ---: | ---: | ---: | --- |
| `e2e/specs/admin/admin_dashboard.spec.ts` | 2 | 2 | 2 | Error: expect(locator).toContainText(expected) failed |
| `e2e/specs/admin/cluster_dns_resolvers_smoke.spec.ts` | 1 | 1 | - | Error: expect(locator).toHaveCount(expected) failed |
| `e2e/specs/admin/cluster_dns_tools_smoke.spec.ts` | 1 | 1 | - | Error: expect(locator).toBeHidden() failed |
| `e2e/specs/admin/cluster_resource_maintenance.spec.ts` | 1 | - | - | Error: expect(locator).toBeVisible() failed |
| `e2e/specs/admin/cluster_resource_packages_filter_contract.spec.ts` | 1 | 1 | - | Error: expect(locator).toBeVisible() failed |
| `e2e/specs/admin/cluster_summary_maintenance_smoke.spec.ts` | 1 | 1 | - | Test timeout of 90000ms exceeded. |
| `e2e/specs/admin/ip_address_detail_page.spec.ts` | 1 | 1 | - | Error: expect(locator).toBeHidden() failed |
| `e2e/specs/admin/mailer_log_smoke.spec.ts` | 1 | 1 | - | Error: expect(received).toEqual(expected) // deep equality |
| `e2e/specs/admin/node_detail_control_center.spec.ts` | 2 | 2 | - | Test timeout of 90000ms exceeded. |
| `e2e/specs/admin/node_pool_maintenance.spec.ts` | 5 | 5 | - | Error: expect(locator).toBeVisible() failed |
| `e2e/specs/admin/os_templates_responsive_actions.spec.ts` | 1 | 1 | - | Error: expect(locator).toBeHidden() failed |
| `e2e/specs/admin/requests_operations_smoke.spec.ts` | 3 | 3 | - | Test timeout of 90000ms exceeded. |
| `e2e/specs/admin/user_detail_page.spec.ts` | 1 | 1 | - | Error: expect(received).toEqual(expected) // deep equality |
| `e2e/specs/admin/user_packages_bulk_remove.spec.ts` | 5 | 5 | 5 | Error: expect(locator).toHaveCount(expected) failed |
| `e2e/specs/admin/user_payments_smoke.spec.ts` | 1 | 1 | - | Error: expect(locator).toContainText(expected) failed |
| `e2e/specs/admin/user_security_delete_failures.spec.ts` | 1 | 1 | - | Error: expect(locator).toBeHidden() failed |
| `e2e/specs/admin/user_security_status_badges.spec.ts` | 1 | 1 | - | Error: expect(locator).toBeVisible() failed |
| `e2e/specs/app/action_state_transactions_responsive.spec.ts` | 2 | 2 | 2 | Error: expect(locator).toBeVisible() failed |
| `e2e/specs/app/admin_income_forecast.spec.ts` | 1 | 1 | - | Error: expect(locator).toBeVisible() failed |
| `e2e/specs/app/admin_network_live_noc.spec.ts` | - | 1 | - | Error: expect(locator).toContainText(expected) failed |
| `e2e/specs/app/backup_center.spec.ts` | - | 1 | - | Error: expect(locator).toBeHidden() failed |
| `e2e/specs/app/blocking_action_progress_modal.spec.ts` | - | 2 | - | Error: expect(locator).toBeVisible() failed |
| `e2e/specs/app/centered_dialogs.spec.ts` | - | - | 5 | Test timeout of 90000ms exceeded. |
| `e2e/specs/app/export_hosts_responsive_actions.spec.ts` | - | - | 4 | Error: expect(locator).toBeVisible() failed |
| `e2e/specs/app/incident_create_context.spec.ts` | - | - | 1 | Test timeout of 90000ms exceeded. |
| `e2e/specs/app/mobile_lookup_popover.spec.ts` | - | - | 8 | Error: expect(locator).toBeAttached() failed |
| `e2e/specs/app/mobile_touch_interactions.spec.ts` | - | - | 1 | Test timeout of 90000ms exceeded. |
| `e2e/specs/app/mobile_workflows.spec.ts` | - | - | 4 | Error: expect(locator).toBeVisible() failed |
| `e2e/specs/app/payment_qr_images.spec.ts` | - | - | 8 | Error: expect(locator).toBeVisible() failed |
| `e2e/specs/app/profile_user_data.spec.ts` | - | - | 2 | Error: expect(locator).toBeVisible() failed |

## Retained evidence

All paths below are relative to `ci-41366168907-diagnosis/` in this session:

- `run.json`, `jobs.json`, `artifacts.json`: authoritative metadata/inventory.
- `annotations-<jobID>.json`: all annotation pages. These expose only the early
  failure titles; the complete job logs prove the larger inventory above.
- `run-logs.zip` (184,633 bytes, SHA256
  `c4fb89a83d1d5380d9fefcea04b368114836caa76239cf7b2fe3a6dad44fc1a0`)
  and `job-logs/`: full logs for all three jobs/steps.
- `artifact-index-<project>.json`: original member paths, sizes and metadata.
- `selected-evidence/<project>/`: unchanged first-failure trace/error-context.

Only the three artifacts belonging to this exact run/head were downloaded:

- `13108697730` / `playwright-test-results-mobile-webkit`: 146,750,877 bytes, 104 trace ZIPs; `playwright-test-results-mobile-webkit.zip`. Digest verified: `sha256:575e59b767d75dbe71ecf1920b721f2aed4720f6e4c567a7d7698d6ff0169fc2`.
- `13108298957` / `playwright-test-results-chromium`: 663,207,492 bytes, 98 trace ZIPs; `playwright-test-results-chromium.zip`. Digest verified: `sha256:99cf21bec6e04add5795ce950b3886c6c228d267890c99b59e7456c229980152`.
- `13108212673` / `playwright-test-results-mobile-chrome`: 315,165,864 bytes, 107 trace ZIPs; `playwright-test-results-mobile-chrome.zip`. Digest verified: `sha256:9cd14630f9cd348aae14ab42d2c16c3f740174db06579a64e3d4a4747feb2574`.

The upload-report steps explicitly say `No files were found with the provided
path: playwright-report`. Trace/results artifacts are available and unexpired
until2026-11-09. Their SHA256 digests match the API inventory. No production
credentials, environment values or full HTTP headers were printed. No repository
source/Git/install/test/application-API/DB/Nix changes or checks were made. Original archive
bytes are retained; the diagnosis does not certify the other29 failure paths as
fixture-only or claim full execution coverage.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-typescript-client-migration/)


## CW centered-dialog repair diagnosis and source milestone

After the lead released source work, the only edited CW leaf is
`e2e/specs/app/centered_dialogs.spec.ts` (source SHA256
`4634be986c821aa1c1c4c86fdcce61e26b5bd329a58e6f8b6518f836afe0ef76`).
It remains uncommitted pending the serialized Git turn. Existing strict coverage
already adopts this complete spec; no metadata/hash refresh is needed for it.

The original five WebKit traces all record HTML language `en` and timeout while
waiting for the English Advanced button. Each actual primary GET returns
`status/response` with `response:[]`, rather than a namespaced collection.
Environment/location/network/system-config pages return their error state before
rendering existing advanced controls. Canonical explicit reads now cover only
the observed route requirements:

- Environments: `environments:[]`.
- Locations: `environments:[]` and `locations:[]`.
- Networks: `locations:[]` and `networks:[]`.
- System config: `system_configs:[]`.
- User data: `vps_user_data:[]`.

User-data source independently proves the Advanced control no longer exists.
The replacement case keeps that route covered: visible inline format filter,
select/clear behavior and URL scope, absent obsolete search/Advanced controls,
then creation-editor centering, bounded geometry, overflow and touch/click close.
The other26 advanced-route cases retain their geometry/open/close checks. Total
route coverage stays27. No test is skipped, no obsolete control reintroduced,
and no fallback/helper, product, locale, SDK or dependency behavior changed.

Original trace-member paths, response shapes, final selector and actual DOM
languages are retained in
`ci-41366168907-diagnosis/centered-dialogs-original-trace-boundaries.json`.
Source readers were checked only for these five observed routes. No valid payload
rejected by the product was found in this bounded inspection.

Pinned scoped ESLint and changed-spec strict E2E typing both exit0 with no
diagnostics. Strict typing uses existing project options, the support declaration
and the spec's import closure; it is not the whole-program gate. Pinned formatting
and scoped diffcheck pass. No browser/server, global compiler, install or Git
mutation ran. `w-ci-centered-dialogs-source-manifest.json` records the stable scope.
The parent-owned representative browser case is the environment Advanced dialog;
the distinct second cause is the supported user-data editor. Then run all five
observed routes with retries0 under the existing Chromium watcher, preserving
WebKit acceptance for the original CI project.
