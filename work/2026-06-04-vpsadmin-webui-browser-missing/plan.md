# vpsadmin webui browser missing fix

## Goal

Find and fix the root cause of GitHub Actions run 26969448540 failing the
vpsadmin `webui` integration test.

## Affected components

- `vpsadmin`: `tests/playwright/webui/playwright.config.cjs` and the webui
  integration-test workflow.
- `vpsadminos`: test runner and NixOS VM image construction are relevant
  because vpsadmin imports the vpsAdminOS test framework.

## Approach

- Inspect the GitHub Actions run and downloaded `vpsadmin-test-logs` artifact.
- Correlate the first Playwright failure with VM image construction logs.
- Evaluate the failing commit's Nix expressions to compare Playwright's
  expected browser path with the packaged browser output.
- Update the Playwright Chromium executable resolver to support the x86_64
  `chrome-linux64/chrome` layout and the older/ARM `chrome-linux/chrome`
  layout.
- Verify with a config-level Node check and one representative webui browser
  script.

## Compatibility

No production compatibility impact. The change is limited to Playwright test
configuration. It remains compatible with both known Chromium package layouts
and does not change deployed API, web UI, database, protocol, or NixOS module
behavior.
