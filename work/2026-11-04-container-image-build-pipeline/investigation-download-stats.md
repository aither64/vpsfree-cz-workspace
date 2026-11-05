# I12: download statistics and Go dashboard feasibility

Investigation/proposal only, 2026-11-05, `implementer1`; capacity, session/env and
saved roster settings verified. C = org configuration
`ca96c95a1fee04793468785d8323a759615b2b4e`; V = vpsadminos
`2951a632c4254a44747a8da326e3dde897eaa0e2`. Canonical bare source only;
reuses [I2](investigation-publication.md) for V's v1 paths and client behavior.
Only this file is written; no live logs, identities, hosts, tests or mutations.

## Configured requester path and remaining trust work

All C paths below are under `cluster/org.vpsadminos/` unless stated otherwise.
`proxy/config.nix:79` enables nginx and recommended proxy settings (`:84`).
`proxy/config.nix:100` forces HTTPS/ACME for `images.vpsadminos.org` and proxies
to the internal images nginx service over HTTP (`:103`).
`int.images/config.nix:21` permits port 80 from proxy's primary address (`:24`);
`:35` serves `/srv/images` with fancyindex. Declared proxy addresses are IPv4
`37.205.14.58` and IPv6 `2a03:3b40:fe:48::1` (`proxy/module.nix:13`).
The configured chain is requester → public TLS nginx → internal nginx → files.
Origin connection address is normally the proxy, not the original requester.

These configs and C `environments/base.nix` add no explicit `real_ip_header`,
`set_real_ip_from`, requester-header override or custom access-log format.
`recommendedProxySettings` delegates header defaults to the pinned NixOS module;
their expanded values, inherited nginx settings and active log format were not
established. Do not assume current origin `$remote_addr` or a forwarded header
contains a trustworthy client IP, or that usable historical logs exist.

For Go, explicitly overwrite one canonical requester header at public nginx
with its socket requester address, discarding client-supplied copies. Trust that
header only from the exact configured proxy peer; otherwise use Go's socket
address. If inner nginx remains before Go, explicitly preserve the trusted edge
value through that hop, or restore it with narrowly scoped real-IP configuration
before forwarding. Do not blindly take the leftmost X-Forwarded-For value or
accept arbitrary Forwarded/X-Real-IP headers from other peers. Record socket peer
and interpreted requester separately. Verify actual upstream source addresses,
IPv4/IPv6 handling, bypass reachability and header overwrite at implementation;
the source metadata/firewall expression alone does not establish runtime routing.

## Small useful dashboard

Use request events to show per-day trends and totals by image distribution,
version, vendor/variant/architecture and actual tar/ZFS format; retain requested
path separately. I2 documents V's canonical `v1/.../image-{archive,stream}.tar`
paths and INDEX tag/default resolution. A Go file server can record the resolved
tuple/content generation at serving time, avoiding later misclassification of
moving tag/default URLs. With access logs alone, unresolved aliases remain
requested aliases unless matching catalog history is available.

Show artifact GET requests, response bytes written, status classes and individual
errors; a bounded recent-request table can show timestamp, tuple/path, requester
IP, client-supplied User-Agent, method, status and bytes. Keep daily aggregates
separate from bounded raw requester rows. No GeoIP or identity system is needed.

Keep HEAD requests and INDEX/directory/theme traffic separate from artifact GETs.
Split 200, 206 range responses, 304 cache validation, errors and interrupted
responses. Record Range/Content-Range and bytes, rather than equating each 206
with a complete image. Retries and overlapping ranges count as separate requests
and may repeat bytes; do not add them up as unique completed downloads. Even a
200 response or matching byte count does not prove receipt/import by a client.
These are HTTP requests and server response bytes, not container imports,
distinct people, VPS creations or authenticated identities. NAT/proxies share
IPs; clients can choose User-Agent. Internal CI downloads should be separately
classified by route/run context where known, not inferred from a human identity.

## Where measurement belongs

Routing public `/v1/` traffic through Go behind the existing TLS edge permits
direct request/byte/status events and resolved tuple attribution. Ensure nginx
does not bypass Go for artifacts; cached responses served before Go would need
edge logs too. Preserve I2's URLs and client semantics; serving compatibility is
separate from this statistics proposal. Staging-only Go sees staging traffic,
not public downloads: it needs public ingress/origin access-log ingestion with
the same trusted requester fields, method/path/status/body bytes/UA and range
details. Count one authoritative event source to avoid proxy/origin duplication.
Existing TLS proxy can stay; no public TLS replacement is required for stats.

Unverified limits: active generated nginx headers/logging, extra intermediaries,
current log availability/rotation, traffic volume, Go serving placement and any
upstream cache. No historical download count or requester identity is asserted.
