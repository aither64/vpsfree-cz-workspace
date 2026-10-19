# Proactive swap removal: staging handoff

vpsAdminOS **staging** is merged at `ca3ff61a3931f0eb524543151d5d78a70f87bfc7`, selecting Linux6.12.113 source `1dfea587406b7dd79973831d1677fb2418e5e9aa`. Only .113 changed; other kernel/ZFS pins and frozen outputs remain unchanged. Experiment controls and QEMU/test tooling are retired; native DAMON remains.

## Evidence and limits

- Required hooks/formatting, source/history/native patch checks, exact source archive byte hash/root, and final four-case no-build Nix evaluation passed. No new tests were authored.
- reviewer0 independently reviewed complete original Linux/OS deliverables, histories, migrations and linkage; four Important ordinary-view regressions were fixed narrowly and directly reconciled. Original report/refs are retained. No migrations, obsolete task history or repeated pin stream remains; inherited prefix history debt is explicitly unchanged.
- Coordinated FF merge8db9c04d-a44e-488d-9448-bf9d481bbf30/job162fcc38-0fa4-48f5-b343-4b3b7d9a2b84 succeeded and verified remote staging exactca3ff61a; lead independently confirmed over SSH. No machine reservation/deployment/reboot or Linux release/default rewrite.
- Compilation, matching modules/ZFS build, boot and runtime tests were NOT performed. Full CI was not awaited. User owns subsequent staging validation; identify new build/storepath, not uname6.12.113 alone.
- Known unchanged baseline advisory: virtual /proc/swaps Size/Used fields use bytes where ordinary tests expect KiB. Removal does not introduce it; source/runtime limitations are explicit in review-report.md.

## Durable references

[Design](design.md), [source/history inventory](linux-source-inventory.md), [original independent review](review-report.md), [direct I1–I4 reconciliation](review-reconciliation.md), [final Nix evaluation](os-evaluation-revised-final.log), [archive proof](linux-archive-revised-proof.json), [integration result](integration/8db9c04d-a44e-488d-9448-bf9d481bbf30/result.json).

Evidence housekeeping: final evaluation watcher accidentally executed its command twice, both identical passes, recorded in its result. Revised archive watcher reported success but did not persist requested raw log/result; parent preserved actual completed-script proof and wrote transparent recovery records at linux-archive-revised-hash.log/result.json, without rerunning. Original source/ref/evidence remain retained.

Session remains open/active; source-only Linux feature is intentionally published rather than merged into existing release/default refs. User staging validation remains pending. No archive/delete/stop or background cleanup is authorized.

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-16-proactive-swap-patch-removal/
