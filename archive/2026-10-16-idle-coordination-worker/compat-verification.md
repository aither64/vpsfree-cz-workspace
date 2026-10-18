# Final verification and deployment candidates

All checks passed at exact committed heads in compat-final-heads.json. Independent review accepted these heads: compat-review-report.md; narrow replay recovery fix and regressions: compat-review-remediation.md. Original evidence from earlier heads remains unchanged.

- Runtime package and host contract: passed, 331s. Artifact /nix/store/3d3g0njmwcwrxfrqdn4vi0i7cn4y6ls7-dev-workspace-0.2.0, retained by compat-runtime-result.
- Composed application, deployment contract and agent instructions: passed, 347s. Application /nix/store/h4hgs5yjq5bd30lnzhksfiqvkxq4lcnn-dev-workspace-0.2.0, retained by compat-workspace-result.
- Exact confctl build from configuration f60ebcdd: passed, 133s; generation 2026-10-17--09-49-21, system /nix/store/z2i0lpgkhy9a0vb8iwwspan5qbla1054-nixos-system-aitherdev-26.05.20261015.26f4107. Only five configuration metadata/activation/system derivations built; no kernel build.
- Systemd continuation survives submitter exit and worker restart: passed, 10s.
- Native fixture at exact built runtime: passed, 7.73s. Two disposable idle native threads, no idle provider requests, one wakeup each, retained fixture model/effort, duplicate sends reconciled after native restart. Synthetic localhost backend only; no real provider requests.
- Native notification protocol Go test: passed, 7.31s.
- Exact CI 39014845298 at runtime 543136a0: success, 162s observed wait. Previous superseded run cancellation was refused HTTP 403 token scope; current run unaffected.

Package checks include 35 integration tests / 202 assertions, all passing. Declared session/host suite skips remain reported by their aggregates. Complete logs, command/revision/status/duration receipts and aggregate results use compat- prefix. Quick predecessor probe, Go metadata, Ruby syntax, pinned Nixfmt and semantic lock proof passed; see compat-quick-verification.md, compatibility-predecessor-probe.json and compat-final-pin-proof.json. Parent monitoring fallback used because fresh utility delegation became unavailable; no substitute model or duplicate test retry.

This is build/test evidence, not live acceptance. System then profile activation must use exact own approved snapshots and the original c5fdac90 reservation. Existing job 879a35ce is refreshed, not replaced. Keep foreign journals/ownership untouched. Pending manual journals are supported by unchanged legacy metadata and the separate dual-reader contract. Live identities, services, portal, native continuity and actual background continuation will be checked before authorized integration.
