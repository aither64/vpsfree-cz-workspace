# Partial IP handling during VPS migration

Investigated on 2026-09-13 against fetched vpsAdmin `origin/master`, commit
`6923c7bfcb628f6acacb4e6fc62806084afc8213`. This is source analysis; the running
production revision and live network records were not inspected. Network
availability is taken from the user's deployment description.

## Finding

The existing migration options do not support preserving and transferring a
shared private IPv4 address while replacing a Playground-only IPv6 allocation.
Both options apply to the complete set of attached IP allocations. Transfer
takes precedence over replacement; the flags do not combine into a per-address
fallback.

For a move between locations in different environments:

| Replace | Transfer | Behavior |
| --- | --- | --- |
| false | false | Remove all attached IP allocations from the VPS. |
| true | false | Replace every allocation, matching IP version, network role, and purpose. |
| false | true | Keep and recharge every allocation, provided every network is available in the destination environment. Otherwise raise a migration error. |
| true | true | Same transfer path as above; replacement is not reached. |

Consequences for the requested cases:

1. **Public IPv4 + IPv6:** replacement enabled and transfer disabled implements
   the requested behavior, subject to eligible free destination addresses and
   resource limits.
2. **Shared private IPv4 + Playground IPv6:** no flag combination implements
   the requested behavior. Replacement changes the private IPv4 too; transfer
   fails on the IPv6 network that is unavailable in Production, including when
   both flags are enabled.

Sharing the private network does not preserve its existing address on the
replacement path. The allocator requires `network_interface_id IS NULL`, so
the currently attached private IPv4 cannot be selected as its own replacement.
The replacement remains private (the network role is preserved), and could
come from the same shared network, but it is a different address.

## Source evidence

All paths below refer to the exact revision above in `repos/vpsadmin.git`.
Read them with `git show <revision>:<path>`; links point to that immutable
upstream revision.

- [API inputs](https://github.com/vpsfreecz/vpsadmin/blob/6923c7bfcb628f6acacb4e6fc62806084afc8213/api/lib/vpsadmin/api/resources/vps.rb#L818-L826):
  `replace_ip_addresses` and `transfer_ip_addresses` are booleans. The migrate
  action exposes no address IDs, family selectors, or network-role selectors.
- [Operation mapping](https://github.com/vpsfreecz/vpsadmin/blob/6923c7bfcb628f6acacb4e6fc62806084afc8213/api/lib/vpsadmin/api/operations/vps/migrate.rb#L8-L24):
  the API booleans map directly to `replace_ips` and `transfer_ips`.
- [Branch selection](https://github.com/vpsfreecz/vpsadmin/blob/6923c7bfcb628f6acacb4e6fc62806084afc8213/api/models/transaction_chains/vps/migrate/base.rb#L357-L380):
  `if opts[:transfer_ips]` calls `recharge_ip_addresses` with the full interface
  address list. Only its `elsif` reaches `migrate_ip_addresses`.
- [Replacement selection](https://github.com/vpsfreecz/vpsadmin/blob/6923c7bfcb628f6acacb4e6fc62806084afc8213/api/models/transaction_chains/vps/migrate/base.rb#L387-L441):
  loops over every IP, calling `IpAddress.pick_addr!` with destination location
  and the source allocation's IP version, network role, and purpose. Missing
  replacements raise an error. Cross-environment resource accounting is handled
  by `transfer_ip_addresses`, an internal method distinct from the API flag.
- [Allocator](https://github.com/vpsfreecz/vpsadmin/blob/6923c7bfcb628f6acacb4e6fc62806084afc8213/api/models/ip_address.rb#L98-L159):
  requires unattached, unlocked addresses; selects from the destination
  location's autopick networks. It does not reuse the source allocation.
- [Neither flag](https://github.com/vpsfreecz/vpsadmin/blob/6923c7bfcb628f6acacb4e6fc62806084afc8213/api/models/transaction_chains/vps/migrate/base.rb#L555-L574):
  invokes `NetworkInterface::DelRoute` for every attached IP.
- [Transfer validation and accounting](https://github.com/vpsfreecz/vpsadmin/blob/6923c7bfcb628f6acacb4e6fc62806084afc8213/api/models/transaction_chains/vps/migrate/base.rb#L620-L682):
  validates every IP before recharging. An unavailable IP raises
  `IP <address/prefix> is not available in the target environment (<label>)`.
  Successful transfer updates source/destination resource usage,
  `charged_environment_id`, and ownership according to the environments'
  `user_ip_ownership` settings.
- [Environment availability](https://github.com/vpsfreecz/vpsadmin/blob/6923c7bfcb628f6acacb4e6fc62806084afc8213/api/models/ip_address.rb#L232-L237):
  `is_in_environment?` checks whether the network is associated with any
  location in the destination environment. Despite the transfer method's
  comment, this is not an exact destination-location check.
- [WebUI controls](https://github.com/vpsfreecz/vpsadmin/blob/6923c7bfcb628f6acacb4e6fc62806084afc8213/webui/forms/vps.forms.php#L1202-L1215):
  displays transfer on environment changes and replacement on location changes;
  both are independent booleans with no partial-selection mechanism. The final
  request passes both booleans in `webui/pages/page_adminvps.php:619-620`.
- `api/models/transaction_chains/vps/migrate/os_to_os.rb:138-139` calls the shared
  network migration method; no alternative partial-IP path was found.

The table applies to a location change. Within one location the replacement
path is not invoked, so both flags off normally preserves IPs. Explicit transfer
is rejected within the same location or environment. Migration also currently
rejects VPSes with more than one network interface; moving addresses between
interfaces would not provide a workaround.

## Validation and limits

- Fetched upstream over SSH and traced the exact source revision through the
  API, operation mapping, common migration chain, allocator, accounting, and
  WebUI request path.
- Inspected `api/spec/models/operations/vps/migrate_spec.rb`: covers option
  mapping, not mixed preservation/replacement.
- Inspected `api/spec/models/transaction_chains/vps/migrate_spec.rb`: its
  fixture places the destination in the same location; it does not cover
  cross-environment IP replacement/transfer.
- The baseline `tests/suite/vps/migrate.nix` requests zero IP allocations;
  searching migration integration scenarios found no use of either flag.
- No tests or production migrations were executed. No project code was changed.
  Source branching is sufficient to establish the unsupported combination.

## Potential implementation direction

Introduce an explicit opt-in mixed policy: preserve allocations whose networks
are usable at the destination and replace the others. Select by network
availability rather than hard-coding private IPv4 versus IPv6. Existing boolean
behavior should remain compatible unless changing it is an intentional API
decision; in particular, redefining both-true currently changes transfer-only
semantics.

Partition allocations before emitting transactions. Recharge retained IPs and
account for replaced IPs without overwriting one group's resource changes with
the other's. Preserve retained host addresses and ordering, routes, ownership,
assignment history, and export access; apply route/host/export changes only to
replacements. Validate exact destination-location usability as well as
environment eligibility. Cover both requested cases, multiple allocations,
quota failures, unavailable replacement pools, and rollback.

This is a design direction only. Implementation, deployment compatibility,
client/UI exposure, and integration validation have not been performed.
