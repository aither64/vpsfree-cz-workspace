# IP lifecycle and secondary DNS associations

Investigation owner: implementer2. Scope: canonical source inspection and this
evidence file only; no application edits, commits, runtime tests, production
database queries, service reloads or DNS mutations. Findings are proposals, not
implemented behavior. Session and both environment identity markers matched
`2026-11-08-dns-transfer-ip-lifecycle` and the trusted workspace binding.

## Source identity and evidence limits

Canonical bare repository: `/home/aither/workspace/ai/vpsfree.cz/repos/vpsadmin.git`.
Inspected `refs/remotes/origin/master` at
`e5e39bf380ebbb469d201f92d62434cd6ebca230`; subsequent reads used that immutable
commit. No fetch or peer worktree access occurred. All source references below
are repository-relative paths and line numbers at this revision. Reproduce with
`git --git-dir=repos/vpsadmin.git show <revision>:<path> | nl -ba` from the
coordination workspace. These are source semantics, not evidence of the
production deployment revision or the user's actual transactions.

Read workspace AGENTS.md, session/documentation/project/verification procedures,
`docs/agent-teams.md`, documentation/handoff skills, and the canonical repository
AGENTS.md, documentation index, API client synchronization, testing, IP ownership
and transaction guides. Live same-session roster confirmed implementer2 and
assigned peers with saved addresses/access. No worktree was necessary.

## Ownership authority

- `api/models/ip_address.rb:3–12,327–339`: an `IpAddress` is an allocation
  (single address or prefix); `user_id` is its explicit owner. `current_owner`
  returns explicit user first, otherwise the assigned interface's VPS owner.
  Explicit ownership on an assigned allocation must match the VPS owner.
- `api/models/host_ip_address.rb:1–6,40–53`: a host belongs to that allocation;
  its owner delegates to the parent. `assigned?` means host `order` is non-null,
  which describes a locally configured host address, not ownership or parent
  routing. DNS transfers reference the host, not the interface.
- `api/models/network_interface.rb:124–155` and
  `api/models/transaction_chains/network_interface/add_route.rb:28–44,65–81`:
  attachment requires the allocation to be free and unowned or explicitly owned
  by the destination VPS owner. A routed prefix uses `route_via` through an
  assigned host on the same interface. Removing its gateway is rejected while
  dependent allocations exist. Ownership remains the prefix's `user_id`, not
  the gateway host's ownership.
- `api/models/dns_zone_transfer.rb:40–59`: external zones permit primary
  transfers; internal zones permit secondary transfers. A user zone's owner
  must equal the host's effective owner; TSIG key and zone owners must match.
  There is no assigned/routed requirement. Therefore a detached explicitly
  owned primary is already valid through the API.

Use explicit allocation ownership after detach: inherited VPS ownership vanishes
when the interface is cleared. Environment `user_ip_ownership` is admission and
accounting policy; it is not a substitute for inspecting the allocation owner.

## Current call paths

| Operation | Exact source evidence | Current DNS consequence |
| --- | --- | --- |
| Public route detach | `api/lib/vpsadmin/api/resources/ip_address.rb:445–487`; `api/models/network_interface.rb:104–110`; `api/models/transaction_chains/network_interface/del_route.rb:12–31,39–75,133–152` | Reserves and reloads allocations, checks actor/interface/owner, removes host assignments and route, then unconditionally removes every host's transfers at lines 63–68. Confirmation clears interface, route-via and order, never `user_id`. Thus temporary detach removes transfers even when explicit ownership survives. |
| Host-only unassignment | `api/models/transaction_chains/network_interface/del_host_ip.rb:15–30,33–51` | Clears host `order`; does not remove transfers. A DNS primary can be reachable within a routed prefix without being configured on the VPS interface. |
| Same-owner move / reattach | `api/models/network_interface.rb:65–92,124–143`; `api/models/transaction_chains/network_interface/add_route.rb:30–44,65–101` | Requires detach then attach, so existing detach loses transfers. Attach contains no recreation of deleted transfers. With retention, the same host ID/address can survive the move; reservations prevent conflicting assignment. |
| Explicit disown | `api/models/transaction_chains/ip/update.rb:10–37`; `api/models/transaction_chains/ip/disown.rb:7–43` | Uses shared cleanup with `delete:true`, removes transfers/PTR/user-created hosts before owner and quota release. When cleanup emits asynchronous commands, owner, charge environment and quotas remain until final success; no-cleanup disown is immediate. |
| Shared host cleanup | `api/models/transaction_chains/network_interface/cleanup_host_ip_addresses.rb:8–29` | When `delete` is true, removes transfers for every host, unsets PTR, then confirms deletion of user-created hosts. DelRoute currently calls it with `delete: !env.user_ip_ownership` in addition to its unconditional transfer-removal loop. |
| Direct A→B allocation transfer | `api/lib/vpsadmin/api/resources/ip_address.rb:288–315`; `api/models/transaction_chains/ip/update.rb:11–50,53–63` | Admin-only action. Changed owner while assigned in an ownership-enabled environment is rejected; detached transfer is allowed with a valid target environment and enabled network. Non-null target ownership currently changes quotas and owner immediately, without DNS cleanup. Model validation still prevents an assigned IP's owner differing from its VPS owner. This path must be covered when retaining detached references. |
| VPS owner transfer | `api/models/transaction_chains/vps/update.rb:218–236,272–311,399–469` | Reserves all affected IPs/hosts, stages VPS/IP/quota changes, and removes DNS transfers from VPS addresses. This effective-ownership change must continue removing old-owner associations. |
| Interface/VPS deletion | `api/models/transaction_chains/network_interface/clear.rb:17–24`; `network_interface/destroy.rb:6–15`; `vps/soft_delete.rb:15`; `vps/destroy.rb:27–29` (all under `api/models/transaction_chains/`) | Clear passes routed-via allocations before direct allocations through DelRoute, including VPS soft/hard deletion. Current unconditional removal applies. Under retention, explicitly owned allocations left detached should retain associations and report the detached condition; unowned ones require cleanup. |
| Migration removing old routes | `api/models/transaction_chains/vps/migrate/base.rb:576–594` | Calls DelRoute with captured source environment and migration options. It inherits the same owned/unowned retention boundary; same-address low-level route updates need not delete associations. Full migration behavior was not expanded beyond this call site. |
| Host deletion | `api/lib/vpsadmin/api/resources/host_ip_address.rb:317–338`; `api/models/transaction_chains/host_ip_address/destroy.rb:7–27` | Public action checks effective ownership, chain reserves parent then host, rejects default or assigned hosts, removes transfers before deletion. Detached user-created host deletion legitimately removes transfers even if parent remains owned. |
| Account/quota teardown | `api/models/transaction_chains/ip/free.rb:9–35` | Uses shared cleanup before confirming owner and charge release. Existing reservation/accounting recovery contracts remain required. |

## Removal ordering, rollback and security

`api/models/host_ip_address.rb:10–36` reserves all parents before children and
requires cleanup before clearing the parent owner. `api/models/ip_address.rb:65–97,
165–181` supplies current resource/SQL locks and effective-owner rechecks, including
a current shared read of VPS ownership for inherited ownership.

`api/models/transaction_chains/dns_zone_transfer/destroy.rb:13–51` locks the
host/parent and zone, emits RemoveServers plus DNS reload for each server zone,
then marks the association pending destruction and confirms deletion. Without
server commands deletion is immediate. Node removal has an add-back rollback in
`libnodectld/lib/nodectld/commands/dns_server_zone/remove_servers.rb:6–13`.
`docs/transactions.md` specifies that confirmations normally apply together at
chain completion, rollback restores marked associations, and fatal chains retain
reservations for recovery. Earlier command placement is not proof that an owner
database edit becomes visible before later cleanup.

The required security boundary is ownership change, not temporary attachment:
never allow an old user's zone to continue using an address now owned by another
user. Direct A→B transfer currently has no cleanup; retaining detached references
makes this an explicit acceptance case. Architect0 selected the small proposal:
reject A→B while any existing DNS references remain, requiring explicit removal
first. Check under the held IP reservation so a concurrent create cannot bypass
it. Same-owner no-op must remain allowed. Normal disown and VPS owner transfer
continue their existing cleanup.

An alternative would defer both source/target quota changes and owner transfer
behind the existing DNS destruction commands, keeping A as owner on failure.
This is possible with existing reservation/confirmation machinery, but requires
changing `Ip::Update`'s immediate accounting path. Do not compose separately
confirmed disown/chown chains or clear ownership before cleanup. This alternative
is not necessary for the selected bounded proposal.

## Primaries, configuration and visibility

`api/models/dns_server_zone.rb:45–60` includes **all user-configured primary
transfer addresses**, without checking parent attachment or host assignment, and
then adds peer vpsAdmin server-zone addresses. External zones use other vpsAdmin
secondaries as potential transfer sources. `api/models/dns_zone_transfer.rb:28–35`
returns the host address/TSIG parameters without routing checks;
`api/models/transactions/dns_server_zone/create.rb:37–45` passes them to the node.
`libnodectld/lib/nodectld/dns_config.rb:118–120,139–140` skips a zone only when the
effective primary list is empty and otherwise renders that whole list in BIND.
Thus retaining a detached owned reference retains the address in BIND; the API
does not establish whether that address is reachable or runs a DNS server.

Deleting the last **user-configured** primary is allowed by the destruction
chain. Peer sources may remain, so it does not always omit the BIND zone. Peers
can serve the same serial without proving any user-configured upstream remains.
The zero-user-primary monitoring/configuration condition must inspect existing
`DnsZoneTransfer.primary_type` associations, not `DnsServerZone#primaries.empty?`.
Existing `webui/forms/dns.forms.php:232–235` warns when an external zone has no
transfer associations. No detached-primary warning/configuration diagnostic was
found in the bounded DNS models, resources, config and forms inspected.

For a retained primary, the local detached condition is the parent allocation's
missing `network_interface_id` while its explicit owner remains the zone owner.
Do not use `HostIpAddress#assigned?`: it would incorrectly label usable hosts
inside routed prefixes. Keep diagnostics per association, and separately report
zero user primaries. Lead's later user steering requires a monitoring alert for
zero user primaries, beyond the existing form warning; implementer1 owns tracing
the existing monitoring/error-condition email interface. That alert must remain
true with peer BIND sources present. Detached status is configuration information,
not a manufactured transfer-failure log event.

Visibility constraint: `api/lib/vpsadmin/api/resources/host_ip_address.rb:47–63`
inner-joins interfaces for direct user host visibility but uses left joins for
included associations. Therefore a detached owned host can remain expandable
through a transfer while direct host Show/list excludes it. Warning rendering
should include the parent allocation through the transfer association rather
than assume a separate direct-host request succeeds. The add-transfer WebUI
currently requests `routed:true` (`webui/forms/dns.forms.php:593–603`); the API
allows detached owned hosts. Expanding that selector is a separate product choice,
not required to retain an already configured association.

## Candidate package and checks

Smallest lifecycle package: gate DelRoute's unconditional transfer-removal loop
on absence of explicit allocation ownership, and exclude retained owned
allocations from destructive shared host cleanup even when environment policy
is ownership-disabled. Preserve current PTR/user-created host semantics for
unowned allocations unless design explicitly changes them. Add the reserved
A→B reference rejection in `Ip::Update`; keep explicit disown, host deletion,
VPS owner transfer and account teardown cleanup. No schema, node protocol or new
service is needed. Existing removed associations cannot be reconstructed from
this change; do not guess an incident repair from allocation history.

Diagnostic package: expose the detached-owned configuration condition plus
zero-user-primary condition in the existing DNS configuration/monitoring and
WebUI mechanisms selected by architect0/implementer1. Reuse current association
expansion and keep missing-upstream alerts distinct from historical transfer
results. Visible behavior needs the repository localization/KB workflow; any new
API diagnostic fields need the generated-client synchronization procedure.

Focused proposed regression checks (not executed):

1. Owned IPv4 and routed-prefix detach retains host ID, transfer/TSIG and BIND
   source, leaves owner/quota unchanged, and reports detached configuration.
   Reattach/move to the same owner's second VPS clears that condition without
   re-adding each zone association. An unassigned host within an attached prefix
   must not be considered detached.
2. Unowned detach removes all references with one and multiple user primaries;
   disown, host deletion, VPS owner transfer and account release still remove
   references. Exercise rollback/failure and held reservations.
3. Detached A→B with references is rejected before owner/quota mutation;
   no-reference transfer and same-owner no-op retain existing behavior. A
   concurrent reference creator cannot pass the rejection check unnoticed.
4. Environment ownership policy does not override actual explicit ownership;
   test owned allocation in ownership-disabled environment and unowned allocation
   in ownership-enabled environment. Interface/VPS deletion inherits the rule.
5. Zero user primary raises the intended config/monitoring condition with peer
   sources present; no claim of upstream health from peer serial equality.
   Removing one of several primaries only changes the affected associations.

Existing unit/spec homes: `api/spec/models/transaction_chains/network_interface/
del_route_spec.rb`, `clear_spec.rb`, `destroy_spec.rb`; corresponding `ip/
update_spec.rb`, `disown_spec.rb`, `free_spec.rb`; `dns_zone_transfer/
create_spec.rb`, `destroy_spec.rb`; resource `ip_address_spec.rb` and
`dns_zone_transfer_spec.rb`. Existing destruction specs cover a last user-primary
removal; current DelRoute specs cover empty resource deltas and stale-interface
selection, not retention. Use the repository Nix/API-spec tooling for later
implementation. No tests were selected or run in this investigation-only package.

Compatibility: retained associations use existing persisted formats and node
messages. Deploying an old API afterward resumes deleting on future detach;
it can read the retained rows. All API writers must share the ownership-change
guard/cleanup before promising this invariant; staggered old writers can still
perform old detach/chown behavior. No data migration is proposed. Do not promise
recovery of associations already deleted before rollout.

## Incident boundary and handoff

This source trace establishes a plausible mechanism for the reported user burden
but does not prove which incident operation ran or when. No production chain or
database history was read. implementer0 reports the November 8 success source
`37.205.11.85` is ns4, with the same serial as the earlier external-primary
success; it must not be described here as proof of recovered user upstream.
Correlate only through [log-evidence.md](log-evidence.md),
[status-evidence.md](status-evidence.md) and architect-owned [design.md](design.md).

Ready for lead acceptance as an evidence-only package. Application implementation,
review, tests and deployment remain outside this assignment. Lead owns state and
manifest reconciliation; this package changes only this evidence file.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-08-dns-transfer-ip-lifecycle/
