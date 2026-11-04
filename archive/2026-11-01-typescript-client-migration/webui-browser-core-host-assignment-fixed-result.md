# Browser verification result

- Result: failed (the exact command exited 1).
- Tested revision: `3d91b9ef3727cc2370d48c1dcab3f7e84efb8184`; checkout was clean before the run.
- Command: supplied `webui-browser-core-host-assignment-fixed-command.txt`, invoked once by the exact requested `env -u ... bash /home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/webui-browser-core-host-assignment-fixed-command.txt` command.
- Duration: approximately 3m 49s (from process start and terminal exit).
- Counts: 43 passed, 1 failed, 1 interrupted, 79 did not run (124 total).
- First failure: `e2e/specs/app/vps_network_tab_actions.spec.ts:247:3`, assigns routes and manages interface addresses and PTR. At line 353 expected request body `{}`, received `{ host_ip_address: {} }`.
- Artifacts: `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/browser-3d91b9ef-nix1228/core-results/app-vps_network_tab_action-efb70-interface-addresses-and-PTR-chromium/` (screenshot, video, error context and trace); interrupted-test artifacts are also in `browser-3d91b9ef-nix1228/core-results/`.
- Log: `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/webui-browser-core-host-assignment-fixed.log`.
- Cleanup: port 5187 had no listening socket after process exit.
