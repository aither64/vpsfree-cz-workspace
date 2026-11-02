# Verification batch 6

Source `8d4e03d53699d80f46030b0ee6eb213151b8ae30`, clean source/unchanged lock
verified before execution. Documented parent-monitoring fallback, handle96792;
complete per-command status/argv/log bindings in verification-6-status.json.

| Stage | Exit | Duration | Log |
| --- | --- | --- | --- |
| vm | 0 | 227.03s | verification-6-vm.log |
| build-mx2 | 0 | 72.91s | verification-6-build-mx2.log |
| build-brq-int-ns1 | 0 | 65.09s | verification-6-build-brq-int-ns1.log |
| build-prg-int-ns1 | 0 | 60.15s | verification-6-build-prg-int-ns1.log |
| build-prg-int-mon1 | 1 | 27.82s | verification-6-build-prg-int-mon1.log |

prg/int.mon2 did not run because batch stopped at first failure. Parent/Nix
finished, statusrunning=null. Successful VM native cleanup completed0.87s;
no owned VM/process or deployed machine/claim. No source changes while active.

## Successful isolated mail test

Full native test passed, command227.03s (script202.93s). Actual completed cases:

- isolated DNS, effective policy and enabled SMTP firewall (7.73s).
- relay denial is independent of greylisting and never queues DATA (7.12s).
- fresh Postgrey tuple, retry and policy-state restart persistence (6.68s).
- original DNSBL rejects a listed external source (1.26s).
- exact-domain delivery, envelopes/content, IPv4/IPv6 and missing-milter fail-open (25.65s).
- unavailable policy service temporarily rejects before DATA (1.77s).
- accepted outage queue survives Postfix restart and reboot, then drains (67.08s).
- primary 4xx defers accepted message until recovery (8.79s).
- primary permanent rejection returns a DSN to the controlled sender (6.71s).
- opportunistic outbound TLS permits a primary without STARTTLS (13.38s).

Realized test output `/nix/store/jgq1lk68xjj40j2h4wnw403pc3nylni4-vm-test-run-mx2`,
deriver `/nix/store/8pan3ddqairw3js87iaysvjqwzalxgls-vm-test-run-mx2.drv`,
NARsha256-pQpattmS9VmO3ZIQUFn66az8GSmB4IvYhTTCFn6SUmo=.
Realized actualmx2 `/nix/store/cpd6wpk8rmpn144hn3r49swgalrfz3f5-nixos-system-mx2-26.05.20261026.718f670`,
deriver `/nix/store/3i0j3mdsxka3aylji983m8midp1322l6-nixos-system-mx2-26.05.20261026.718f670.drv`,
NARsha256-ztI7D6vuYUDXM7/27qTkyi4DPLW+7PjRFTLHsN+lMBs=.
Both validated with nix path-info after success; no prior failed output assumed.

Native confctl current generation metadata/symlinks for completed systems agree:

- mx2:2026-11-02--18-00-32, outputcpd6wpk8... above.
- brq/int.ns1:2026-11-02--18-01-34,
  `/nix/store/m4wgivh327z0ppax2nk01c6dhqlrv0av-nixos-system-ns1-26.05.20261026.718f670`.
- prg/int.ns1:2026-11-02--18-02-39,
  `/nix/store/g0m4r81lcnr5h5lx6i4swmyprb61c44h-nixos-system-ns1-26.05.20261026.718f670`.

These are built outputs, not activated profiles or production verification.
Full source/input graph lock binding is unchanged in implementation receipt.

## Remaining monitor integration failure

prg/int.mon1 evaluation fails at modules/clusterconf/monitor/default.nix157:
metaConfig.services.node-exporter missing while rendering Prometheus target.
Owner0 assigned exact baseline/consumer/machine metadata diagnosis; do not label
unrelated or defer without evidence. Smallest supported current metadata contract
fix if newhost caused it, no genericfallback/registry/dependency campaign. New
production metadata requires affected-lane independent review after committed
quick checks before long rerun. Successful8d4e test/builds remain bound to their
actual derivations/inputs; assess exact identities before reuse on successor.

Owned native typecheck scratch dirs removed by owner after confirming no live
consumers; standalone /tmp/mx2-test-script-with-types.py retained/accounted pending
final pass. Source, .confctl generations, store outputs and session retained.

## Later artifact-availability qualification

The immediate postrun path-info/NAR validation above succeeded at that time.
Subsequent reviewer/owner/root queries find the VM check output absent/null;
no session-owned store deletion occurred and cause is unknown. The current
output is not claimed available. Full passing log/status and immutable exact
8pan derivation/input graph remain and were independently accepted for reuse
on the metadata-only successor. See monitor-review.md and the metadata receipt.
