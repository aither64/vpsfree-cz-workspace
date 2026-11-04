# Browser core verification result

- Result: failed; exit status 1. The command ran once and stopped at the first failure.
- Tested HEAD: `1ab9853312a95b5448e99fd6f83f846453de17a5`.
- Command: prepared A from `tracking/webui-browser-core-command.txt`, with only the five specified inherited `E2E_*` variables unset. Pinned Chromium 1.61.0/revision 1228 was present; `PLAYWRIGHT_BROWSERS_PATH` was unset; port 5187 was free before launch.
- Elapsed: approximately 4 seconds.
- Test count: 124 selected; 1 failed, 1 interrupted, 122 not run. First failed case: `[chromium] e2e/specs/admin/host_ip_addresses_responsive_actions.spec.ts:5:1 — host IP actions stay reachable without horizontal scrolling`.
- Bounded failure excerpt: Chromium headless shell exited 127: “Could not start dynamically linked executable” / “NixOS cannot run dynamically linked executables intended for generic linux environments out of the box.” No retry or diagnosis was performed.
- Full stdout/stderr and true exit status: `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/webui-browser-core.log`.
- Report/artifacts: `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/browser-1ab98533/core-report`; traces at `core-results/admin-host_ip_addresses_re-5c477-ithout-horizontal-scrolling-chromium/trace.zip` and `core-results/admin-help_boxes_responsiv-54f6b-ns-stay-reachable-on-mobile-chromium/trace.zip`. No PNG screenshots were found.
- Cleanup: no listener on port 5187 and no remaining Vite or Playwright process was found. Chromium launch PID 3693760 exited 127.
- Evidence boundary: this run provides no synthetic UI pass evidence and does not certify a live API, production build, Nix package, or deployment.
