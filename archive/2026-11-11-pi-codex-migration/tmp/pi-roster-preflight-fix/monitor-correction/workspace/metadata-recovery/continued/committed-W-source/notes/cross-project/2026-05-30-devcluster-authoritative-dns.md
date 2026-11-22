# Devcluster authoritative DNS

Initiative: `work/2026-05-30-dev-vpsadmin-clusters`

Symptom:

Dev vpsAdmin clusters needed realistic authoritative DNS so reverse zones and
PTR changes on host IP addresses could be tested before production deployment.

Implementation:

- Reuse vpsAdmin's existing NixOS DNS test module, which runs BIND plus
  nodectld as a `dns_server` node.
- Seed one hidden primary and one public secondary by default. The hidden
  server has `hidden = true` and `user_dns_zone_type = primary_type`; the
  public server has `hidden = false` and `user_dns_zone_type = secondary_type`.
- Create confirmed internal reverse zones for seed networks before registering
  IP addresses where possible, then refresh existing `IpAddress` reverse-zone
  links for already-seeded clusters.
- Fire normal `TransactionChains::DnsServerZone::Create` chains for new
  server-zone links so nodectld receives the same zone-create transactions as
  production DNS servers.

Validation:

- BIND and nodectld were active on both DNS VMs.
- Reverse zones were served by the hidden primary and transferred to the
  secondary.
- A PTR set via `TransactionChains::DnsZone::SetReverseRecord.fire` for
  `198.51.100.10` resolved from both authoritative DNS servers.

Operational note:

Secondary transfers may lag primary reloads briefly. For manual debugging,
`rndc retransfer <zone>` on the secondary forces an immediate transfer.
