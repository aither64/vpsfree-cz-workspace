**Result: failed.** The single authorized A run tested HEAD `dc95fbca818d3de38b5b65be6ff633d8529ed58c` and exited 1 after 67 seconds.

The first failure was `[chromium] e2e/specs/admin/security_advisory_nodes_mobile_actions.spec.ts:27:1`: the expected advisory node editor was not found after clicking Edit. Playwright stopped at the first failure: 11 passed, 1 failed, 1 interrupted, and 111 did not run. I did not retry or run B.

- Full log: [webui-browser-core-host-fixed.log](/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/webui-browser-core-host-fixed.log)
- Result record: [webui-browser-core-host-fixed-result.md](/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/webui-browser-core-host-fixed-result.md)
- Failure trace: [trace.zip](/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/browser-dc95fbca-nix1228/core-results/admin-security_advisory_no-a0ccc-y-directly-usable-on-mobile-chromium/trace.zip)
- Failure screenshot: [test-failed-1.png](/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/browser-dc95fbca-nix1228/core-results/admin-security_advisory_no-a0ccc-y-directly-usable-on-mobile-chromium/test-failed-1.png)

After the runner exited, no matching Playwright/Vite process remained and port 5187 had no listener. This was Vite source with synthetic API fixtures; it does not establish live API, production build, Nix package, or deployed acceptance.