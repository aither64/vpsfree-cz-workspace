# Browser core verification result

- Result: failed (test failure; runner exited 1).
- Tested HEAD: `dc95fbca818d3de38b5b65be6ff633d8529ed58c`.
- Command: exact A command from `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/webui-browser-core-host-fixed-command.txt`, run once from the specified WebUI worktree. Only the five specified inherited E2E variables were cleared; the command set `PLAYWRIGHT_BROWSERS_PATH` to the exact approved Nix bundle.
- Elapsed: 67 seconds.
- Tests: 11 passed, 1 failed, 1 interrupted, 111 did not run. Initial selection was 124 tests.
- First failed case: `[chromium] e2e/specs/admin/security_advisory_nodes_mobile_actions.spec.ts:27:1 › security advisory node actions stay directly usable on mobile`. Assertion at line 123 expected `getByTestId('admin.security_advisories.nodes.editor')` visible after clicking Edit; locator was not found before timeout.
- B/captures were not run. No retry or diagnosis was performed.
- Remaining owned process/port: no matching Playwright/Vite process and no listener on `127.0.0.1:5187` after runner exit.
- Evidence: complete stdout/stderr and exit markers in `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/webui-browser-core-host-fixed.log`; trace `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/browser-dc95fbca-nix1228/core-results/admin-security_advisory_no-a0ccc-y-directly-usable-on-mobile-chromium/trace.zip`; screenshot `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/browser-dc95fbca-nix1228/core-results/admin-security_advisory_no-a0ccc-y-directly-usable-on-mobile-chromium/test-failed-1.png`; context `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/browser-dc95fbca-nix1228/core-results/admin-security_advisory_no-a0ccc-y-directly-usable-on-mobile-chromium/error-context.md`.
- This run exercised Vite source with synthetic API fixtures. It does not establish live API, production build, Nix package, or deployed acceptance.
