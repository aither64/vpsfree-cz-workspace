# 2026-07-29-dns-resolver-misuse

## Goal

Determine how the recursive DNS resolvers
`ns{1,2}.{prg,brq}.vpsfree.cz` can be abused, distinguish reflected traffic
from abusive recursion initiated by a VPS, define an attribution procedure,
and recommend compatible mitigations.

## Affected repositories

- `vpsfree-cz-configuration`: resolver ACLs, listeners, firewall rules,
  metrics, resolver addresses, and monitoring.
- `vpsadminos`: possible follow-up enforcement of per-VPS source-address
  validation on host interfaces. No worktree or change is planned during this
  investigation.
- `vpsadmin`: operational source-address-to-VPS/user attribution through its
  API. No source change is planned.

## Approach

1. Inspect the declared resolver ACL, firewall, listener, network, and
   monitoring configuration.
2. Verify the behavior and limitations of the pinned Knot Resolver release,
   especially native request rate limiting, views, metrics, and dnstap.
3. Inspect vpsAdminOS source-validation behavior and identify gaps between
   IPv4 and IPv6.
4. Define a live incident procedure that first classifies the traffic by
   direction and port tuple, then attributes it through the resolver, node,
   and vpsAdmin.
5. Rank containment options by effectiveness, operational risk, and
   compatibility.

## Compatibility and deployment

- Knot Resolver rate limiting is local to each resolver and changes no
  persisted format, API, or protocol. Introduce it in dry-run mode, establish
  normal per-source query rates, then enforce one resolver at a time. Rollback
  is a configuration reload.
- Per-location ACLs can reduce the blast radius, but must retain every valid
  customer, management, and infrastructure prefix for that location.
- Explicit per-veth source validation affects routed and delegated addresses.
  A vpsAdminOS implementation must cover IPv4 and IPv6, all supported
  interface types, live address changes, and route-via/delegated prefixes.
  Nodes can roll independently if enforcement is local, but mixed-version
  behavior must be tested.
- Moving recursion to private or per-node addresses requires a dual-address
  migration: deploy new listeners, update vpsAdmin resolver data and generated
  VPS configuration, allow old and new versions to coexist, then retire the
  public addresses. Rollback must keep the old addresses available until all
  VPSes have migrated.

## Testing plan

- Test every resolver IPv4 and IPv6 address from a genuinely external network
  and from representative allowed customer and management networks.
- Run downstream query collection long enough to cover normal weekday,
  weekend, maintenance, deployment, and restart bursts. Retain raw query data
  only for a short rolling incident window and retain privacy-reduced
  aggregates for threshold analysis.
- Compute per-address and per-prefix rates using the same IPv4 and IPv6 prefix
  levels and multipliers as the Knot Resolver limiter.
- In rate-limit dry-run mode, compare sampled offenders with short packet
  captures and Prometheus request, cache, and iterator rates.
- Test legitimate burst workloads and failover before enforcement, then deploy
  one resolver at a time and watch latency, SERVFAIL, TCP fallback, and
  truncation.
- Verify spoofed and legitimate source traffic on representative vpsAdminOS
  routed interfaces for IPv4 and IPv6 before changing fleet-wide filtering.

## Decisions

- Do not assume that reported resolver-originated traffic is an amplification
  reflection. First distinguish answers sourced from port 53 from the
  resolver's iterative queries sourced from ephemeral ports.
- Do not select a rate threshold without production traffic baselines.
- Prefer DNS-aware Knot Resolver request rate limiting as the first application
  control, backed by network source validation and edge flow telemetry.
- Use downstream dnstap queries as the authoritative attribution source.
  Rate-limit logs and built-in metrics are supporting signals, not complete
  per-client accounting.
