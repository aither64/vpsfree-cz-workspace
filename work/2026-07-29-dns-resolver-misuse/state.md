---
lifecycle: active
---
# 2026-07-29-dns-resolver-misuse

## Repositories

- `vpsfree-cz-configuration`
  - Branch: `2026-07-29-dns-resolver-misuse`
  - Worktree:
    `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-07-29-dns-resolver-misuse/vpsfree-cz-configuration`
  - Base/head: `40b5adbf5d3ec739e6f93efd7d32a79d7981528a`
  - Source changes: none
- `vpsadminos`: inspected from the canonical repository; no branch or
  worktree created.
- `vpsadmin`: public API action metadata inspected; no branch or worktree
  created.

## Status

Investigation complete. No production or repository configuration was changed.
The recommended next implementation is a separately reviewed change that adds
Knot Resolver rate limiting in dry-run mode and abuse-volume monitoring.

## Commands run

- Verified the active development session with `bin/dev-session current` and
  `VPSFREE_DEV_SESSION_SLUG`.
- Created the dedicated configuration worktree with
  `bin/dev-session worktree add`.
- Inspected repository instructions, resolver configuration, network data,
  resolver machine definitions, monitoring rules, and relevant git history
  using `rg`, `sed`, and `git`.
- Entered the repository Nix development environment to inspect the pinned
  Knot Resolver package and source.
- Queried the four configured IPv4 resolver addresses from this workstation.
- Attempted read-only production access through direct SSH and `confctl ssh`.
- Inspected unauthenticated vpsAdmin API action/resource metadata with
  `vpsfreectl`.
- Inspected vpsAdminOS routed-interface reverse-path-filter setup.
- Consulted official Knot Resolver, Linux kernel, and IETF documentation for
  rate limiting, views, dnstap, metrics, reverse-path filtering, and BCP 38.
- Inspected the pinned Knot Resolver 6.4.1 rate-limiter, dnstap, statistics,
  and Prometheus implementation and the matching Nixpkgs packages.
- Inspected the `ns3` and `ns4` machine definitions and common authoritative
  BIND profile, then probed both public IPv4 endpoints over UDP and TCP.

## Results

- The supplied report from an authoritative BIND server classifies the
  incident as upstream recursive traffic, not reflected resolver answers. It
  records `37.205.11.222` (`ns2.brq`) with ephemeral source ports such as
  `44406` and `54833`, asking port 53 for distinct PTR names below
  `28.68.185.in-addr.arpa`.
- The reporter's `rate limit slip/drop NXDOMAIN response` text describes its
  own BIND Response Rate Limiting while answering the resolver. The
  `37.205.11.0/24` value is BIND's response-rate aggregation bucket; it does
  not mean that the resolver sent traffic to that whole prefix.
- Equivalent reports for resolver IPv6 addresses have the same
  interpretation when the resolver uses an ephemeral source port. Upstream
  IPv4 versus IPv6 does not identify the downstream client's address family;
  a client using either family can cause the resolver to select either
  transport toward an authoritative server.
- The burst of distinct leaf labels under one reverse zone is consistent with
  reverse-DNS enumeration or scanning. It may be malicious or a
  misconfigured/overactive legitimate scanner and is not, by itself, proof
  that the source VPS is compromised.
- `ns3.vpsfree.cz` and `ns4.vpsfree.cz` both import
  `cluster/cz.vpsfree/vpsadmin/common/dns.nix`. That profile explicitly sets
  `recursion no;`, forcibly clears forwarders, and opens TCP/UDP port 53 for
  authoritative service.
- Live IPv4 tests on 2026-07-29 matched the declaration. Both servers answered
  the `vpsfree.cz` SOA over UDP and TCP with `NOERROR` and the authoritative
  `AA` flag. Both returned `REFUSED` to a non-authoritative recursive query
  over UDP and TCP, did not advertise `RA`, and returned EDE 20 with
  `recursion disabled`.
- The live tests came from an internal `172.16.0.0/12` workstation. Their
  refusal therefore also rules out an internal-only recursion exception on
  the tested IPv4 endpoints.
- Direct IPv6 runtime probing was not possible from this workstation because
  it has no IPv6 route. The global BIND `recursion no;` option applies to both
  address families, but a direct external IPv6 probe would provide independent
  deployment verification.
- `configs/dns-resolver.nix` deliberately permits recursion from all declared
  customer container IPv4 and IPv6 networks, the management IPv4 networks,
  and `172.16.0.0/12`. All other sources are refused by the Knot view and
  blocked from port 53 by the host firewall.
- All customer VPSes are therefore trusted recursive clients. A compromised
  VPS can generate abusive recursive traffic, including random-subdomain cache
  misses, without violating the ACL.
- The ACL normally prevents a VPS from reflecting an answer to an arbitrary
  external victim: the forged victim source address would not belong to an
  allowed prefix. External reflection would indicate source-validation or
  deployment failure, an unexpectedly allowed victim prefix, external
  exposure, or compromise of the resolver itself.
- The four IPv4 addresses answered recursive queries from this workstation.
  This is expected because the workstation has an address in
  `172.16.0.0/12`; it is not an external open-resolver test. The workstation
  had no usable IPv6 route.
- The pinned Knot Resolver is 6.4.1. No native `rate-limiting` section is
  configured, so its UDP request rate limiter is disabled.
- In this release, the native limiter is applied before recursion for pure UDP
  requests. It aggregates IPv4 and IPv6 hosts and prefixes, supports dry-run
  sampling and per-view price factors, and can stop random cache-miss recursion
  as well as reduce response amplification.
- Metrics are already enabled, but the existing DNS alert checks availability
  rather than request, iterator, cache-miss, or traffic anomalies.
- vpsAdminOS enables strict IPv4 `rp_filter` on routed VPS interfaces after
  installing their routes. This should reject most spoofed IPv4 sources when
  runtime routes and sysctls match the declaration. No equivalent explicit
  IPv6 source filter was found in the inspected path.
- Resolver-only capture cannot reliably attribute spoofed packets. Router flow
  telemetry or node ingress-interface/per-veth observation is needed to map a
  spoofed stream to its physical ingress and VPS.
- The internal DNS zone still contains older Prague resolver AAAA records,
  while resolver modules declare newer addresses. This is a separate
  configuration inconsistency to verify; there is no evidence that it caused
  the reported incident.

## Recommended incident procedure

1. Classify the reported flow:
   - resolver source port 53 to a victim high port is a downstream DNS answer;
   - resolver ephemeral source port to authoritative destination port 53 is an
     iterative query generated while serving a client;
   - traffic arriving at resolver destination port 53 identifies client
     requests.
2. During an active event, take a short, access-controlled capture of incoming
   UDP/TCP destination port 53 on the resolver, or temporarily enable dnstap.
   Aggregate source address, QNAME, QTYPE, protocol, response size, and rate.
3. Enable the native rate limiter in dry-run mode with a short log sampling
   period. Correlate sampled source prefixes with resolver and Prometheus data.
4. Map a trustworthy source address through vpsAdmin's `ip_address` and
   `network_interface` resources to the VPS and user. For delegated IPv6
   prefixes, use longest-prefix containment rather than exact-address lookup.
5. If the source can be spoofed, correlate the timestamp and tuple with
   NetFlow/sFlow/IPFIX ingress-interface data, or capture/counters on candidate
   node veths, before attributing the VPS.

## Logging and rate-limit baseline

- Enable dnstap downstream query logging on every resolver. Query-only logging
  is sufficient for source attribution and rate measurement; responses can
  remain disabled unless response codes or latency are required.
- The pinned `knot-resolver_6` package is built with `fstrm` and `protobufc`,
  so dnstap support is present. Current Nixpkgs also provides `dnstap` 0.4.0
  and `go-dnscollector` 2.2.3 as possible local consumers.
- The dnstap Unix socket reader has to exist before Knot Resolver starts.
  A deployment therefore needs a dedicated runtime directory, restrictive
  ownership, and explicit systemd ordering between the collector and resolver.
- Keep raw client-address plus QNAME data only in a short rotating window,
  proposed as 24-72 hours depending on typical abuse-report delay. Restrict
  access and preserve only an incident-matching window when investigation is
  required.
- Produce longer-lived per-client and limiter-prefix aggregates without
  QNAMEs. Avoid exporting every client address as a permanent Prometheus label;
  use histograms, normalized-rate maxima, and bounded top-talker/event output.
- Current built-in metrics are aggregate. The configured Prometheus endpoint
  exports request protocol/family, answer/cache/RCODE, truncation, and latency
  counters, but no per-client series and no explicit rate-limited counter.
  The manager's JSON metrics endpoint may expose additional raw statistics;
  verify its live output before relying on iterator metrics.
- The current Prometheus scrape interval is 60 seconds, which can hide short
  bursts like the supplied report. A follow-up should evaluate a 10-15 second
  resolver scrape interval and alert on request rate, NXDOMAIN share, cache
  misses/upstream work, truncation, SERVFAIL, and latency.
- `stats.frequent()` can provide probabilistically sampled common iterative
  query names, but it contains no downstream client identity and is not a
  substitute for dnstap.
- Configure a candidate Knot rate limit in dry-run mode with a nonzero
  `log-period`. The log identifies a sampled limited address and prefix, with
  heavy offenders more likely to appear, but it intentionally does not report
  every offender or an exact rate.
- Knot Resolver 6.4.1 stores limiter counters in shared mmap data used by all
  eight workers. The configured limit is therefore per resolver, not per
  worker.
- The native limiter covers pure UDP queries. A real, non-spoofing client may
  retry a slipped/truncated response over TCP, so it is not a complete
  per-client quota across transports. Persistent offenders still need
  operational blocking or a front end capable of transport-independent
  client quotas.

For each time window, calculate a normalized candidate load as the maximum of:

```text
IPv4: address/1, /24/32, /20/256, /18/768
IPv6: address/1, /64/2, /56/3, /48/4, /32/64
```

Here `/24/32` means the observed query rate for that `/24` divided by Knot's
multiplier 32. A safe base `rate-limit` must exceed the high percentile and
known maximum of legitimate normalized load with operational headroom, while
remaining a small enough share of sustainable resolver capacity that one
client cannot dominate it. Inspect IPv6 allocation topology carefully because
the `/64`, `/56`, and `/48` multipliers are deliberately restrictive.

As non-enforcing experiments, compare candidate base rates such as 50, 100,
250, and 500 queries per second against captured traffic. These are measurement
points, not recommended production values. Use the actual dry-run limiter to
validate the chosen candidate because its exponential decay and
`instant-limit` burst behavior are more precise than fixed one-second buckets.

## Open questions

- What was the authoritative server's destination address, total query rate,
  duration, and complete set of affected reverse zones?
- Which downstream client addresses asked each resolver for the reported PTR
  names at the matching timestamps?
- Are every resolver's live Knot view and firewall rules identical to the
  current declaration?
- Is strict IPv4 reverse-path filtering active on every relevant VPS
  interface, and what explicit IPv6 anti-spoofing exists at nodes and edges?
- Which edge or node devices currently export ingress-interface flow
  telemetry?
- Can the authoritative-only behavior of `ns3` and `ns4` be independently
  probed from an IPv6-capable external network?

## Cleanup

- Keep the dedicated clean worktree for a possible follow-up mitigation
  implementation.
- Removed development-shell artifacts and temporary Knot Resolver source files
  created while inspecting the package.
- No production state, branches, commits, resolver configuration, or vpsAdmin
  data was changed.
