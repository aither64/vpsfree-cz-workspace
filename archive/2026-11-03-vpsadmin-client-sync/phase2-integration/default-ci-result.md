# Default CI observation result

Observation completed for exactly the eight manifest runs. All eight initial run records matched the expected head SHA. No run/job was retried or cancelled. Terminal JSON, complete logs and artifact metadata were captured for every run; all metadata and log commands exited 0.

## Runs

### vpsfreecz/vpsadmin / 41822368583
- Head: `4ac49f49e63545200df8afa920c6eafda8722523` (expected `4ac49f49e63545200df8afa920c6eafda8722523`); event: `push`; workflow: API Specs (topic parallel).
- Result: **completed / failure**. Jobs: API specs (core) - plugins: success, API specs (core) - auth: success, API specs (full) - foundation: success, API specs (full) - auth: success, API specs (core) - dns: success, API specs (full) - vps: success, API specs (full) - dns: success, API specs (core) - storage: success, API specs (full) - plugins: success, API specs (full) - ip-ownership: success, API specs (core) - network: success, API specs (core) - vps: success, API specs (full) - mail: success, API specs (core) - mail: success, API specs (full) - network: success, API specs (core) - ip-ownership: success, API specs (full) - users: success, API specs (core) - platform-operations: success, API specs (core) - foundation: success, API specs (full) - platform-config: success, API specs (core) - users: success, API specs (full) - platform-operations: failure, API specs (full) - storage: success, API specs (full) - platform-infrastructure: success, API specs (core) - platform-infrastructure: success, API specs (core) - platform-config: success, API specs - topic coverage: failure.
- Watch: not watched (already terminal at initial read).
- Evidence: `01-vpsadmin-41822368583-initial.json`, `01-vpsadmin-41822368583-terminal.json`, `01-vpsadmin-41822368583-logs.txt` (exit 0), `01-vpsadmin-41822368583-artifacts.json` (exit 0); artifacts: rspec-results-core-platform-config, rspec-results-full-storage, rspec-results-full-platform-infrastructure, rspec-results-core-platform-infrastructure, rspec-results-full-users, rspec-results-core-storage, rspec-files-core-network, rspec-results-core-users, rspec-results-core-vps, rspec-results-full-platform-operations, rspec-files-core-platform-infrastructure, rspec-results-core-foundation, rspec-files-core-users, rspec-results-full-platform-config, rspec-files-full-platform-infrastructure, rspec-results-core-dns, rspec-files-full-vps, rspec-files-core-platform-config, rspec-files-core-foundation, rspec-results-full-network, rspec-files-full-users, rspec-files-full-platform-config, rspec-results-full-vps, rspec-files-core-dns, rspec-results-core-network, rspec-files-core-storage, rspec-results-core-platform-operations, rspec-files-full-network, rspec-files-core-plugins, rspec-results-core-mail.
- Failed-job logs: `01-vpsadmin-41822368583-failed-job-API_specs__full__-_platform-operations.txt`, `01-vpsadmin-41822368583-failed-job-API_specs_-_topic_coverage.txt`.
### vpsfreecz/vpsadmin / 41822368910
- Head: `4ac49f49e63545200df8afa920c6eafda8722523` (expected `4ac49f49e63545200df8afa920c6eafda8722523`); event: `push`; workflow: API Migration Specs.
- Result: **completed / success**. Jobs: API migration specs: success.
- Watch: not watched (already terminal at initial read).
- Evidence: `02-vpsadmin-41822368910-initial.json`, `02-vpsadmin-41822368910-terminal.json`, `02-vpsadmin-41822368910-logs.txt` (exit 0), `02-vpsadmin-41822368910-artifacts.json` (exit 0); artifacts: none listed.
### vpsfreecz/vpsadmin / 41822368892
- Head: `4ac49f49e63545200df8afa920c6eafda8722523` (expected `4ac49f49e63545200df8afa920c6eafda8722523`); event: `push`; workflow: i18n health.
- Result: **completed / success**. Jobs: WebUI i18n health: success, API i18n health: success.
- Watch: not watched (already terminal at initial read).
- Evidence: `03-vpsadmin-41822368892-initial.json`, `03-vpsadmin-41822368892-terminal.json`, `03-vpsadmin-41822368892-logs.txt` (exit 0), `03-vpsadmin-41822368892-artifacts.json` (exit 0); artifacts: none listed.
### vpsfreecz/vpsadmin-rust-client / 41822770408
- Head: `823a4f8450fce4947310fc81bcdebdca91d9ffae` (expected `823a4f8450fce4947310fc81bcdebdca91d9ffae`); event: `push`; workflow: Rust client.
- Result: **completed / success**. Jobs: msrv: success, client (async): success, regeneration: success, client (blocking): success.
- Watch: not watched (already terminal at initial read).
- Evidence: `04-vpsadmin-rust-client-41822770408-initial.json`, `04-vpsadmin-rust-client-41822770408-terminal.json`, `04-vpsadmin-rust-client-41822770408-logs.txt` (exit 0), `04-vpsadmin-rust-client-41822770408-artifacts.json` (exit 0); artifacts: none listed.
### vpsfreecz/vpsadmin-typescript-client / 41822889192
- Head: `2da950a98fa13468b36d03b13fb5e81cca206e0e` (expected `2da950a98fa13468b36d03b13fb5e81cca206e0e`); event: `push`; workflow: Package validation and release.
- Result: **completed / success**. Jobs: build: success, publish: skipped.
- Watch: not watched (already terminal at initial read).
- Evidence: `05-vpsadmin-typescript-client-41822889192-initial.json`, `05-vpsadmin-typescript-client-41822889192-terminal.json`, `05-vpsadmin-typescript-client-41822889192-logs.txt` (exit 0), `05-vpsadmin-typescript-client-41822889192-artifacts.json` (exit 0); artifacts: npm-package-2da950a98fa13468b36d03b13fb5e81cca206e0e.
### vpsfreecz/vpsadmin-webui / 41827144373
- Head: `47b6992e28c16585aa6247bd75413637a7ca6388` (expected `47b6992e28c16585aa6247bd75413637a7ca6388`); event: `push`; workflow: Playwright smoke.
- Result: **completed / success**. Jobs: PR smoke E2E (mobile-chrome): success, PR smoke E2E (mobile-webkit): success, PR smoke E2E (chromium): success.
- Watch: exit=0, elapsed_seconds=1671.692.
- Evidence: `06-vpsadmin-webui-41827144373-initial.json`, `06-vpsadmin-webui-41827144373-terminal.json`, `06-vpsadmin-webui-41827144373-logs.txt` (exit 0), `06-vpsadmin-webui-41827144373-artifacts.json` (exit 0); artifacts: playwright-report-mobile-webkit, playwright-report-chromium, playwright-test-results-mobile-chrome, playwright-test-results-chromium, playwright-report-mobile-chrome, playwright-test-results-mobile-webkit.
### vpsfreecz/vpsadmin-webui / 41827144400
- Head: `47b6992e28c16585aa6247bd75413637a7ca6388` (expected `47b6992e28c16585aa6247bd75413637a7ca6388`); event: `push`; workflow: Playwright broad smoke.
- Result: **completed / success**. Jobs: Broad smoke E2E (chromium): success, Broad smoke E2E (mobile-chrome): success.
- Watch: exit=0, elapsed_seconds=268.105.
- Evidence: `07-vpsadmin-webui-41827144400-initial.json`, `07-vpsadmin-webui-41827144400-terminal.json`, `07-vpsadmin-webui-41827144400-logs.txt` (exit 0), `07-vpsadmin-webui-41827144400-artifacts.json` (exit 0); artifacts: playwright-test-results-chromium, playwright-report-mobile-chrome, playwright-report-chromium, playwright-test-results-mobile-chrome.
### vpsfreecz/vpsadmin-webui / 41827144462
- Head: `47b6992e28c16585aa6247bd75413637a7ca6388` (expected `47b6992e28c16585aa6247bd75413637a7ca6388`); event: `push`; workflow: CI.
- Result: **completed / success**. Jobs: Chromium script regression: success, Required nonbrowser checks: success, Production build: success.
- Watch: exit=0, elapsed_seconds=96.045.
- Evidence: `08-vpsadmin-webui-41827144462-initial.json`, `08-vpsadmin-webui-41827144462-terminal.json`, `08-vpsadmin-webui-41827144462-logs.txt` (exit 0), `08-vpsadmin-webui-41827144462-artifacts.json` (exit 0); artifacts: audit-artifacts.

## Log annotations

- Run `41822368583` failed in `API specs (full) - platform-operations` and `API specs - topic coverage`; its failed-job logs are retained. Other jobs in that workflow succeeded.
- Visible skips: TypeScript `publish` job was skipped; WebUI broad smoke Chromium log reports 1 skipped test; WebUI PR smoke mobile-WebKit reports 2 skipped tests. vpsadmin specs report pending examples as recorded in the full logs.
- No observed failed-job rerun or flaky/retry annotation was recorded in the retained run evidence. Full logs are authoritative; keyword matches may include ordinary test text or retry-policy configuration.

## Watcher

- Retained utility: `dw_af6ea530112c2a5e816254d08d217be90f4f5c713a51db96`, configured as `gpt-6-luna`, low reasoning, one operation, max_concurrent 1. Launch policy in the supplied native config: danger-full-access, approval never.
- Native thread identifier was not exposed to this watcher in its available context or command environment; it is not asserted here. The operation is complete and its single slot is released.
- No remaining observation operation. This report records evidence only; the parent owns acceptance and any follow-up.

## Owner verification and final disposition

Implementer2 independently inspected all eight terminal JSON records against the
exact manifest repository/run/head identities, terminal states and job outcomes.
Actual totals: seven successful workflows, one failed workflow; 41 successful
jobs, two failed jobs and one skipped TypeScript publication job. This is not an
all-green batch. The failed API run and both failed-job logs remain unchanged.
At the final-smoke checkpoint the lead reported owner3's baseline diagnosis
complete and explicitly accepted/recorded the scoped residual, with no rerun or
source fix. That disposition does not relabel the failed workflow as passing.

All eight metadata/log capture exits are zero; artifact metadata reports no
expired artifacts. The three active WebUI runs finished successfully on exact
47b6992e28c16585aa6247bd75413637a7ca6388, with all eight WebUI jobs successful.
Their direct full watch logs and actual watch statuses are retained. Bounded
native log-summary inspection confirms PR smoke632/574/274 passing tests, two
WebKit skips; broad smoke239 Chromium passes/one skip and96 mobileChrome passes.
No flaky/retry annotation was visible in those summaries.

The parent independently verified actual native launch settings from only this
owned utility's turn_context: fresh thread
01a1a67a-bc6a-7722-b09a-ed8afe3931cd, gpt-6-luna/low,
danger-full-access, approval never. See
[native settings](default-ci-native-settings.json). Parent session/current and
both literal environment values matched the binding; utility current check
also returned the exact slug. This supplements the watcher's unavailable
introspection without changing its original statement.

Utility process ended, all observations are terminal, and the single utility
slot is released. No owner/watcher default mutation, claim, deployment, tag,
lifecycle action or cleanup. All six documentation integrations were completed
by the lead; TypeScript main is exact2da950a and WebUI main/merged PR127 exact47b6992e.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-vpsadmin-client-sync/)
