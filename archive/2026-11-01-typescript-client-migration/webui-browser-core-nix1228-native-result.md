**A failed** on source HEAD `7cad7ffb3a0a294c30349680e2eb4f80c63a3926`. The exact prepared command ran once and exited **1** after 48 seconds. Playwright reported 3 passed, 1 failed, 1 interrupted, and 119 not run.

The first failed case was `[chromium] e2e/specs/admin/host_ip_addresses_responsive_actions.spec.ts:130` — “rejected host IP deletion stays in context and supports retry.” The interrupted case was the English VPS-first assignment case. No retry or B run was performed.

- Full stdout/stderr: [/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/webui-browser-core-nix1228.log](/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/webui-browser-core-nix1228.log)
- Screenshot, video, and trace: `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/browser-7cad7ffb-nix1228/core-results/admin-ip_assignment_vps_fi-a6e3d--without-an-ownership-write-chromium/`
- HTML report: `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/browser-7cad7ffb-nix1228/core-report`

I have not yet written the requested `webui-browser-core-nix1228-result.md` artifact. The run used Vite source and synthetic API fixtures; it does not establish live API, built, Nix package, or deployed acceptance.