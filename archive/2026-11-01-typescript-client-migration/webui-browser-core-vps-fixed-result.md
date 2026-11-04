# WebUI browser core VPS fixed verification result

- Tested HEAD: `dbe60e2fd335efc4261f6af3a7878643221b66a7`
- Command: exact assigned `env -u ... bash .../webui-browser-core-vps-fixed-command.txt` invocation; run once.
- Exit status: 1
- Duration: approximately 164 seconds (2.8m Playwright-reported test duration).
- Counts: 124 planned; 42 passed, 1 failed, 2 interrupted, 79 did not run; one error outside any test.
- First failure: `e2e/specs/app/vps_network_tab_actions.spec.ts:247:3` (“assigns routes and manages interface addresses and PTR”); at line 336 `toHaveValue("1")` on `getByTestId("vps.network.host_addresses.assign.interface")` failed because locator was not an input element.
- Artifacts: screenshot, video, trace, and error context listed in the full log. Failure artifact directory: `work/2026-11-01-typescript-client-migration/browser-dbe60e2f-nix1228/core-results/app-vps_network_tab_action-efb70-interface-addresses-and-PTR-chromium/`.
- Full stdout/stderr: `work/2026-11-01-typescript-client-migration/webui-browser-core-vps-fixed.log`.
- Cleanup evidence: post-exit `ss -ltn ( sport = :5187 )` showed only the header and no listener.
