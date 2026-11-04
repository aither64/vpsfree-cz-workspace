# Browser core update fixed-command result

- Result: failed (command exit status 1).
- Tested revision: `ad5327eba64919d58cede22186958ff0e0ad0b77` (clean at launch).
- Command: the exact assigned `env -u ... bash .../webui-browser-core-update-fixed-command.txt` invocation; launched once.
- Elapsed time: approximately 2 minutes 9 seconds, from launch to observed command exit.
- Playwright reported 124 tests, 2 workers; it stopped after the first maximum allowed failure.
- Counts: 38 passed, 1 failed, 1 interrupted, 84 did not run. Playwright reported 2.8m suite elapsed.
- First failure: `[chromium] e2e/specs/app/vps_network_tab_actions.spec.ts:82:3` (`edits interface and sends PUT`); `getByTestId('vps.network.page')` was not found within 15 seconds at line 105.
- Failure artifacts: `work/2026-11-01-typescript-client-migration/browser-ad5327eb-nix1228/core-results/app-vps_network_tab_action-e861a-its-interface-and-sends-PUT-chromium/test-failed-1.png`, `video.webm`, `error-context.md`, and `trace.zip`.
- Interrupted test artifacts: `work/2026-11-01-typescript-client-migration/browser-ad5327eb-nix1228/core-results/app-user_requests_smoke--p-192f6--URL-context-or-owner-scope-chromium/test-failed-1.png`, `video.webm`, and `trace.zip`.
- Other command output: one error was not part of a test (as reported by Playwright). The full stdout/stderr log is retained at `work/2026-11-01-typescript-client-migration/webui-browser-core-update-fixed-run.log`.
- Cleanup: after process exit, `ss -ltn 'sport = :5187'` showed no listener. No retry or additional verification was run.
