# Milestone 4 browser evidence — superseded UI, not a complete matrix pass

Source: `9f68dad5436799d82e9c9e1c69e73866a279e9a6`, tree
`c3c3e04337bcf9669dbb79611d72a65c686af9e0`. HTTP invocation
`8c36c3b467a945fea166f3ba1cb6feda`, Ruby 358140/DB 358993.
All five loaded HaveAPI gems were 0.31.0; health loaded/current/clean agreed.
Preview receipt: `../preview/milestone4-final-receipt.json`.
No product source, Git, hooks, dependencies, service or authentication changes.

## Completed actual evidence

- Run1 real unrouted cache/search: 31.572s; real changed-CS-locale: 6.674s.
  Index 883,877 bytes: 152 resources, 524 actions, 6,358 parameters.
  Cold input-to-results 2,954.4ms; warm 46.7–54.5ms (browser/driver diagnostics,
  not calibrated performance gates). No page-load bulk fetch; one keyed server
  request. Same-view navigation reused disk cache (two recorded hits, each
  zero encoded network bytes), with no second keyed server request.
- Neutral page and controlled persisted-event restore each bootstrapped
  `current` with no-store. Real Accept-Language cs changed key and made one cold
  request. Actual native BFCache was NOT observed: BrowsingInstanceNotSwapped /
  BackForwardCacheDisabledForDelegate. Controlled persisted-event proof passed.
- Actual parameter result landed on TR with Token active. URL/viewport/display
  preference did not move while searching; no query/results/index storage.
- Already-running run3 completed historical 390/768/1024/1440 responsive
  assertions (13.124/11.904/12.433/11.151s), including touch/keyboard/theme,
  current resource/action tracking/submenu, local validator/code scrolling,
  long inert layout fixtures and no document overflow. This is not milestone5
  acceptance. Screens were captured but final visual acceptance was superseded.
- Run3 actual 409/no-index/native Enter/no-JS fallback passed in 20.180s.

## Failed harness cases and remaining scope

Run1 failed after 537.554s total: its 409 `Response.body()` read had no timeout
and remained pending for 498.041s. Exact owned Node inspector diagnosis and
correct visible fallback are retained in `milestone4-matrix-final-9f68dad5-run1/`
(`overrun-await.json`, `overrun.png`, `result.json`) and its sibling log.
Only that pending body promise was rejected; normal finally closed the browser.
The remaining-only harness inspects the actual no-index response by bounded
native navigation instead; original script and all artifacts are preserved.

Run2 stopped at an immediate auto-theme media assertion (6.054s actual script).
Run3 retained exact assertions with the existing 15s UI bound; its diagnostics
prove immediate/settled theme differences at 768/1024/1440 (async media events).
Only ignored harness files changed, including pre-close failure capture.

Run3 ended normally with exit1 after 89.085s, at the 15s controlled fault-case
fallback wait. That controlled phase remains unresolved and was not diagnosed
further after milestone5 superseded this UI. No overall matrix pass or product
failure is claimed. New final UI needs its required responsive/fallback/safety
coverage; do not rerun old completed phases merely to produce a green aggregate.

## Operations and disposition

Fresh watcher per operation: retained catalog `3ff7a212…`, Luna/low, full access
(danger-full-access / approval never). Run1 native child; run2 standalone native
Codex `01a182ef-08ac-7cc0-b01c-9d4cb18da5bd`; run3 standalone native Codex
`01a182f0-eb7f-7b31-8322-2f9836ef20f0`. Actual CLI headers retained in watcher logs.
Run2/run3 sibling `.log`, `result.json` and watcher-result files are preserved;
run3 contains navigation/validator/long-account PNGs for all four widths.

On milestone5 stop, SIGINT was attempted only for owned Node464950, but the
process had already exited naturally; no signal was delivered. Watcher and
parent reconciled runner/browser descendants. No active browser/watcher/check
remains; matrix SOURCE HOLD RELEASED. Preview, DB, files/refs and session remain.
No further work before formal milestone5 assignment; no local HTTPS/auth attempt.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/
