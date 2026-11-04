# Browser core advisory fixed-command verification

- Result: failed (exit 1); exact supplied command executed once.
- Tested revision: `b611632f47d0eec4ad87bbb1566c7cb2a80dbefa` (checkout clean before run).
- Elapsed: 1m25s wall time for the owned command; Playwright reported 1.4m test runtime.
- Counts: 17 passed, 1 failed, 1 interrupted, 105 did not run (124 total; stopped at first failure).
- First failure: `e2e/specs/app/authenticated_home_smoke.spec.ts:48` — expected `getByTestId('app.dashboard.page')` to be visible; element was not found within 15s.
- Failure artifacts: screenshot, video, trace and error context under `browser-b611632f-nix1228/core-results/app-authenticated_home_smo-305a7-ootstrap-in-standalone-mode-chromium/`. The interrupted test artifacts are under `browser-b611632f-nix1228/core-results/admin-ip_assignment_vps_fi-5fea8-blocks-replay-across-reload-chromium/`.
- Complete output: `webui-browser-core-advisory-fixed-run.log`.
- Native cleanup: Playwright command exited; its managed Vite server is expected to be cleaned by Playwright. Port 127.0.0.1:5187 was free after exit.
