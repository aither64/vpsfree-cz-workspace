# Verification after preceding baseline integration

All seven operations passed at exact final heads in reservation-refresh-heads.json. Independent general/history and risk/compatibility review passed with no findings: reservation-refresh-review-report.md. Previous all-lane review retained for unchanged feature architecture/scope; runtime patch range-diff equals. No own candidate has been deployed yet.

Runtime 9b50f357 on 1f3cf7ae, codex-web 5daae414. Workspace 399202fa, configuration ae3f3052. Extension 767dfd58, unrelated lock nodes/follows preserved. Final pin proof reservation-refresh-pin-proof.json. One feature commit, workspace policy separate from one pin, one generated confctl update, no obsolete pins or DB migrations.

- Runtime package and host contract passed (329.52s), artifact /nix/store/yjfz0nb9vsj1jhrrz2yh32jgd1fw9gv4-dev-workspace-0.2.0, rooted by reservation-refresh-runtime-result.
- Composed application and deployment/instruction checks passed (349.63s), /nix/store/wbilhmczhkn2h7kwvqmzkmnylrvv83xg-dev-workspace-0.2.0, rooted by reservation-refresh-workspace-result.
- Exact confctl build from configuration ae3f3052 passed (178.67s), generation 2026-10-17--10-55-55. No local kernel build.
- Systemd continuation/restart acceptance passed (4.76s).
- Isolated native fixture passed (11.05s): two idle threads, zero idle provider requests, one wakeup each, retained fixture model/effort and deduplication after native restart. Synthetic localhost provider only, no real API calls.
- Native notification protocol Go test passed (6.96s).
- Exact CI 39018599934 at runtime 9b50f357 passed.

All logs/results use reservation-refresh- prefix, aggregate reservation-refresh-verification-results.json. Changed Nix input identities caused packaged suites to rebuild; 35 integration tests/202 assertions passed. Known fixture suite skips reported normally. Quick checks 4 Ruby/49 assertions, Go metadata, composition and config hooks passed. Fresh reviewer CLI actual Astra/xhigh/read-only verified. Fresh Luna/low watcher could not read brief due sandbox mount initialization, so no check ran there; visible parent-monitoring fallback ran controller once. Original failed utility events and prior successful-head evidence retained unchanged.

New snapshot preparation must preserve original system job 879a35ce, profile job 2833768e, reservation c5fdac90 and system-before-profile dependency. Selected predecessor changed during waiting; snapshots must bind current live identities and generation, then receive separate exact approvals under existing user direction. No direct activation, forced ownership, foreign journal edits or default-branch integration before live acceptance. A notification grants no approval.
