# Third CI observed inventory — 2026-11-02

Frozen head **9d9617c048dded592b6362e3370d92cfca2793cb**, both runs attempt1. [Core CI41480946099](https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41480946099) succeeded in all3jobs. [Playwright41480945591](https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41480945591) failed.

| Job / ID | Raw UTC start → finish | Job duration | Native observed result |
| --- | --- | --- | --- |
| WebKit125398757644 |16:23:16→16:58:37|35m21s|7failed,2skipped,267passed;276selected|
| Chromium125398757689 |16:23:16→17:04:40|41m24s|23failing headings;632selected;cancelled, incomplete totals|
| mobileChrome125398757909 |16:23:26→17:04:07|40m41s|22failing headings;574selected;cancelled, incomplete totals|

Raw job span: **41m24s**,16:23:16–17:04:40UTC. Original `webui-second-ci-final-ci/report.md` remains unchanged, including its inconsistent1h42/18:05 claim; that claim is not used as execution duration.

## Observed cases and limits

**52 project-specific failing cases;36 identities ignoring engine;11files.** [Structured inventory/selection](webui-third-ci-observed-selection.json) contains exact project/file/full title, source position, first log line, first original inline failure/error, expanded retry error/line and duplicate occurrences for every case. Repeated retries/terminal echoes do not add cases.51inline GitHub records corroborate52expanded headings; Chromium ordinal2 appears only expanded at3166 and was inspected directly. Titles containing negative words are not outcomes.

All lines refer to the populated900121-byte `webui-second-ci-final-ci/run-41480945591.log`:

- WebKit command1392: `... node scripts/playwright.mjs test --project=mobile-webkit`;276selected at1399. Genuine terminal totals1744–1753 (repeated2565–2574):7failed/2skipped/267passed(33.8m). The acquired report independently agrees:276total/267expected/7unexpected/0flaky/2skipped.
- Chromium command3106 adds `--pr-smoke --project=chromium --workers=2`;632selected at3113.23failing headings precede `The operation was canceled.`4431; no suite terminal totals.
- mobileChrome command4990 adds `--pr-smoke-mobile --project=mobile-chrome --workers=2`;574selected at4997.22failing headings precede the same cancellation message6095; no suite terminal totals.

Commands use `npm run env:check && E2E_START_SERVER=1` and the ordinary runner. Testcase timeout failures are recorded per case. The permitted local inputs contain **no explicit job-cap annotation** for the cancelled jobs; cause/actor remains unknown. Duration alone cannot establish either. Empty per-job logs and404annotation captures are not job evidence. No absent heading is treated as a pass.

First observed headings: WebKit1404 lifetime(cs), `expect(locator).toBeHidden()`; Chromium3119/mobileChrome5004 chain detail, `expect(locator).toBeVisible()`. These are symptoms, without causal interpretation; architect owns lifetime diagnosis.

## Path partition and earlier coverage

| Spec (`e2e/specs/`) | Chromium | mobileChrome | WebKit |
| --- | ---: | ---: | ---: |
| `app/tasks_drawer_focus_trap.spec.ts` | 2 | 0 | 0 |
| `app/transaction_chain_detail_page.spec.ts` | 6 | 2 | 0 |
| `app/transaction_detail_page.spec.ts` | 7 | 6 | 0 |
| `app/user_data_editor_accessibility.spec.ts` | 1 | 1 | 0 |
| `app/vps_access_page.spec.ts` | 3 | 2 | 0 |
| `app/vps_create_admin_flow.spec.ts` | 2 | 5 | 0 |
| `app/vps_create_failures.spec.ts` | 2 | 2 | 0 |
| `app/vps_detail_tabs_matrix.spec.ts` | 0 | 1 | 0 |
| `app/vps_expiration_reactivation.spec.ts` | 0 | 2 | 2 |
| `app/vps_initialization_templates.spec.ts` | 0 | 1 | 4 |
| `app/vps_network_editor_feedback.spec.ts` | 0 | 0 | 1 |

All11paths/52headings are outside both earlier30-path/109-heading and27-path/103-heading repair inventories. None match the local220 exact project/file/describe/title identities. This broader observed scope does not invalidate or enlarge prior checks’ input scope. No engine-specific defect or shared cause is inferred.

## Released acquisition, complete

Only WebKit report **13162417238** was fetched via existing `gh api`, with no status/log query. [Local archive](webui-third-ci-evidence/playwright-report-mobile-webkit.zip):57041743bytes, SHA256 `943d2d08c85dc52e778ffb606c32e79283cd7039b63b6efcfec6a033b14ec5ce`, matching retained exact-run/head metadata; exit0/5.545s. ZIP index92members is in JSON. The report provides all7failed WebKit cases’ original retry0 trace/error-context paths and hashes, mapped in JSON. No extract-all.

Only four lifetime originals were extracted and handed to architect0:

- [Czech trace](webui-third-ci-evidence/lifetime-cs-trace.zip), original member `data/346bd899a5fdccbc23888fa61f01add6ee6a9779.zip`, SHA256 `8524529acba99f788af15407b929613b4af97d8ced981e525939f1a58631ca18`; [error context](webui-third-ci-evidence/lifetime-cs-error-context.md).
- [English trace](webui-third-ci-evidence/lifetime-en-trace.zip), original member `data/e022fd396e485e42cb34d1040c102869eb9746bb.zip`, SHA256 `1f7f08cfcb7a4de489bfca3ed3d49aed092ea35d34132ffd576c97566ea1be8b`; [error context](webui-third-ci-evidence/lifetime-en-error-context.md).

Other owners may read their mapped original nested ZIPs in memory from this same archive. No new-case source audit or causal diagnosis occurred in this package.

## Further evidence proposal — held

| Artifact | Bytes | SHA256 |
| --- | ---: | --- |
|13163190622 playwright-test-results-mobile-chrome|196441411|`4c934f4da547c1ecc1dc36061b4d297cd9aef2bba8119edf87c7a8e9cadfb31c`|
|13162417238 playwright-report-mobile-webkit|57041743|`943d2d08c85dc52e778ffb606c32e79283cd7039b63b6efcfec6a033b14ec5ce`|
|13162172353 playwright-test-results-mobile-webkit|74051919|`9db2573fd2c03d6f11ad50939a89cd6c4bcefd7e1a2d43ed486857bc3a74a45a`|
|13161334021 playwright-test-results-chromium|313152166|`90f0004267ba2ae30f60188e497f05afb906fad946c244316df7b92c7ad7c6d0`|

No further archive is needed for the architect’s lifetime boundary. If parent releases collection for every observed distinct identity, minimum candidate cover is the acquired57MBreport plus mobileChrome196MB and Chromium313MB:566635320bytes total, avoiding all4archives. The JSON36-identity selection prefers7WebKit originals,19additional mobileChrome originals and10additional Chromium originals. This deduplicates evidence by title, without asserting equivalent engines; all52observations remain recorded. Exact Chrome member names await an authorized index.

Held commands: existing `gh api repos/vpsfreecz/vpsadmin-webui/actions/artifacts/13163190622/zip` for mobileChrome and `/13161334021/zip` for Chromium. Full executable/argument arrays, unique targets, sizes and digests are in JSON. On explicit release: no overwrite/automatic retry; verify size/digest; index only; read selected original retry0 nested traces in memory, adding error context only where needed. The duplicate74MBWebKit results archive stays held because the smaller report already contains all7original traces. No retrieval framework or watcher was added; the released bounded read-only transfer retained its native handle to exit.

Raw evidence only: no acceptance, source/check/browser/Git/Nix/API/DB/CI mutation or release transition. Original receipts/reports/artifacts preserved. Lead owns aggregate state; architect owns causal triage and further source boundaries.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-typescript-client-migration/
