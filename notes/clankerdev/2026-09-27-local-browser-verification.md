# Browser prerequisites in clankerdev verification

Observed at `fd290b5ec1b22900e704e8cb990c5ba050af2394` during
[the new interface review](../../work/2026-09-27-newadmin-integration/verification.md).

`npm run ci:pr` reaches a browser-dependent Node script test before its BFF and
Vitest phases. `scripts/live-vps-certification-browser-proxy.test.mjs` starts
Chromium against loopback stubs; it does not perform live VPS certification.
A plain Node environment allowed 130/131 script tests to pass, then stopped the
aggregate command because Chromium was absent.

The repository has no Nix shell at this revision. Provisioning
`nix shell nixpkgs#nodejs_22 nixpkgs#chromium -c bash` and setting
`E2E_CHROMIUM_EXECUTABLE_PATH` to `command -v chromium` let the failed script
test pass. Run the aggregate's skipped phases explicitly when diagnosing this
failure. Node was 22.23.2, npm 10.9.8 and Chromium 153.0.8010.52; upstream CI
pins a different npm version, so this does not reproduce its full runner image.

`npm run e2e:pr` selected 32 workers on this host: the desktop stage had
349 passes and 29 failures, preventing the chained mobile stage from running.
Five representative failures all passed with one worker after their original
logs and page trees were inspected. This supports load/timing sensitivity but
does not establish the cause of the remaining failures or a passing full suite.
Set a deliberate worker limit for reproducible diagnosis, preserve initial
failure evidence, and do not treat a focused rerun as release certification.
