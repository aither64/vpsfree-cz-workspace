# Network availability and IPv4-left counter: implementation design

Status: accepted implementation brief, reconciled 2026-10-06 with the user's
role-only classification and both configuration-channel updates. The architect
has changed only this brief; source implementation and verification follow under
the lead. No deployment or production database inspection is recorded here.
Architect: `architect0`; lead owns plan, state, and portal records.

## Recommendation and scope

Add `Network.enabled`, default `true`, meaning **eligible for new allocations
and assignments**. Administrators can disable an obsolete network without
deleting it or disrupting its existing allocations. Enforce the flag in the
shared API allocation and assignment paths, and use it in the existing
`Cluster.PublicStats.ipv4_left` calculation. Both index pages already consume
that field and require no independent counting logic.

Use `Network.role` alone to distinguish public and private networks, as explicitly
directed by the user. Do not introduce address-range classification or predicates
in the counter, allocation policy, diagnostic, or tests. Add network status and
administrator controls to both WebUIs.

Implementation includes `vpsadmin`, `vpsadmin-webui`, and both application channel
pins in `vpsfree-cz-configuration`. No changes are needed to vpsAdminOS, node
protocols or routing configuration. Production deployment, network disabling and
default-branch integration remain separate actions requiring authorization.

## Evidence and limits

Inspected canonical bare repositories only, without fetching or changing refs:

- **V**: original `vpsadmin` investigation at
  `b4ef8535a629ee8c9cd753afecdb05e0895d0eea`; refreshed local
  `refs/remotes/origin/master` is `c4d9b50f4e74417ed37b5fe410cca3ec1addc24e`.
  Only `webui/composer.lock` and `webui/php-packages.nix` differ; the V evidence
  below remains unchanged.
- **W**: `vpsadmin-webui`, `refs/remotes/origin/main`
  `02ac0c7de1a588dbb14a18e652fe3f7e9b45cc51`, refreshed by the lead. Network and
  public API adapters, NetworksPage and the cited public-counter components are
  unchanged from the original `aa2f60b89df65d2f987be48784ed42bab7010833` inspection.
  Its updated AGENTS.md requires new task branches named `dev/<name>` and dated
  work-log entries; preserve existing colleagues' branches.
- **C**: `vpsfree-cz-configuration`, local `refs/remotes/origin/master`
  `cde8451718d75929c931db63626b48f7de92fc4f`.

Paths and line numbers below refer to those exact revisions, not deployment
proof. Root and repository instructions, relevant architecture/IP/transaction
documentation, and verification procedures were read.

| Evidence | Confirmed behavior |
| --- | --- |
| V `api/lib/vpsadmin/api/resources/cluster.rb:31-74` | PublicStats counts allocation rows with no user, no interface, IPv4 network, and `role=public_access`. There are no other eligibility checks. |
| V `webui/pages/page_index.php:86-90`; W `src/lib/api/public.ts:81,166`, `src/pages/public/OverviewModel.ts:74`, `OverviewPage.tsx:62-94` | Legacy and new index counters read the same API field. |
| V `api/db/schema.rb:566-582,691-712,949-961`; `api/models/network.rb:12-29`; `api/lib/vpsadmin/api/resources/network.rb:14-24` | Network has role, purpose, managed/split settings and location associations, but no enabled flag. Location has maintenance state; LocationNetwork has autopick/userpick. None is consulted by PublicStats. |
| V `api/models/network.rb:111-133` | Public/private role controls quota resource identity. Role/IP-version changes are rejected when allocation rows exist. |
| V `api/models/ip_address.rb:147-240` | `free?` means no interface, not unowned or unlocked. Automatic selection allows free unowned or requesting-user-owned addresses, filters role/location/purpose and policy, excludes IP resource locks, then revalidates after reservation. |
| V `api/models/transaction_chains/ip/allocate.rb:17-37`; `vps/create.rb:216`; `vps/clone/os_to_os.rb:515` | VPS creation/clone and resource allocation share the picker. Owned detached addresses may be reused, with destination charge checks. |
| V `api/models/transaction_chains/export/create.rb:87-96,130-147`; `vps/migrate/base.rb:574-587` | Export service addresses use the same picker with private/export policy; migration replacements also use it. |
| V `api/models/network_interface.rb:65-93,124-143`; `transaction_chains/network_interface/add_route.rb:27-37,63-99` | Explicit-ID assignment validates location, purpose, ownership/free state and userpick, including a current check after IP reservations. Admin bypasses userpick but not ordinary location/purpose rules. Internal AddRoute calls can omit the actor. |
| V `api/models/ip_address.rb:66-114`; `network.rb:141-190`; `transaction_chains/ip/update.rb:10-46`; resource `ip_address.rb:241-307` | Manual registration, managed-network address creation, and assigning/transferring ownership are separate paths that must be considered alongside the picker. |
| V `api/models/transaction_chains/vps/update.rb:218-289,399` | VPS owner change reserves assigned IPs and transfers their ownership/accounting. Guard this ownership path too; it does not call IpAddress.Update. |
| V resource `user.rb:261-339`; resource `ip_address.rb:45-70,122-181` | User-owned availability counts and selectable inventory have separate query logic. Index/Show visibility is not allocation authorization. |
| V `api/models/transaction_chains/vps/migrate/base.rb:329-385`; `vps/replace/os.rb:282-296`; `vps/swap.rb:141-213,307-312` | Some operations preserve existing allocations/interfaces; others replace addresses. Restore/replacement/swap can move or regenerate an existing service's networking. |
| V `api/models/transactions/vps/populate_config.rb:19-39`; `transactions/network/register.rb`; `libnodectld/lib/nodectld/commands/network/register.rb` | VPS config generation emits assigned routes without an availability filter. Network.Register sends version/address/prefix/role; its inspected node implementation is a no-op. |
| V `api/models/transaction_chains/network/create.rb`; resource `network.rb:102-209`; `operations/location_network/{update,delete}.rb` | Admin API supports create/update/add-addresses, with no Network delete action here. Network creation registers with online nodes. Location associations and selection flags are separate; deleting one is not a safe retirement mechanism. |
| V `docs/ip-locking.md`, `docs/ip-release.md`, `docs/transactions.md`; `transaction_chains/ip/{free,disown}.rb` | Reservations last through asynchronous confirmation/rollback. Campaign cleanup keeps ownership until final success. No IP cooldown column or allocator predicate was found; release timestamps are campaign evidence. |
| V `webui/forms/cluster.forms.php:209-269`, `webui/pages/page_cluster.php:522-625`; W `src/lib/api/networks.ts:9-129`, `src/pages/app/admin/cluster/NetworksPage.tsx` | Legacy UI lists networks and manages their locations; it needs a new enable/disable action. React UI already has network create/edit forms. |
| V `api/spec/api/resources/cluster_spec.rb:183-198` | Existing counter test calculates its expectation using essentially the same query. It does not independently establish desired semantics. |
| C `flake.nix:69-78,106-112` | Channel `vpsadmin`, role `vpsadmin`, selects `vpsadminServices`; channel `vpsadmin-webui`, role `vpsadmin-webui`, selects `vpsadminWebui`. The latter's `inputs.vpsadmin` follows `vpsadminServices`. |

**Confirmed mechanism:** obsolete network rows continue contributing as long
as they contain unowned, unassigned allocations tagged public IPv4. The current
model cannot mark a whole network unavailable. Networks marked `private_access`
are already excluded, and that classification remains authoritative.
Reserved rows can also contribute while asynchronous assignment has not yet
changed their stored user/interface.

**Unverified production hypothesis:** these mechanisms explain how inflation
can happen, but source inspection cannot prove which networks contribute to the
reported number or which revision is deployed. Obtain the diagnostic below
before selecting networks to disable.

## Availability contract

`enabled=true` permits new allocations subject to all existing checks. It does
not guarantee a matching location, sufficient quota, or immediately available
addresses. `enabled=false` prevents new use in that network for administrators
as well as members. Administrators can explicitly re-enable it when needed;
there is no hidden admin bypass.

| Operation on a disabled network | Required behavior |
| --- | --- |
| Automatic allocation, including reuse of an owned but detached address | Exclude it in initial selection and reject it in the locked recheck. |
| Explicit assignment of an unassigned parent allocation, even one already owned by the requester | Reject. Ownership is retained, but it is not permission to start new service on a retired network. |
| New ownership or transfer to a different owner through IpAddress.Update | Reject. A same-owner no-op remains harmless; disowning remains allowed. |
| VPS owner change carrying disabled-network allocations | Reject before ownership/accounting mutations. Changing effective owner is new use, including where the IP row has no explicit owner. |
| IpAddress.Create or Network.AddAddresses with an owner | Reject new owned allocations while disabled. |
| Admin registers unowned inventory, including creating a disabled network with prefilled addresses | Permit inventory preparation. Those rows remain unavailable and contribute zero to the public counter. |
| Existing assigned VPS/export, routes, host addresses, quota and owner | Preserve. No detach, disown, route removal, node command, or automatic migration on disable. |
| Boot/restart/reinstall/config regeneration; host-address management within an existing assigned prefix | Preserve existing service and normal authorization. Do not filter assigned associations by enabled. |
| Migration/restore/replacement/swap retaining an already assigned allocation | Permit continuity of the existing service under existing location/ownership checks and reservations, including an internal interface/VPS replacement. |
| Clone or restore that needs additional/replacement addresses | Allocate only from enabled networks. A historical snapshot is not authority to reacquire a currently detached address. |
| Release/disown, route removal, campaign cleanup, transaction rollback | Continue to work while disabled. Released addresses stay unavailable until re-enabled. |

Existing owner-only allocations remain visible with their status and can be
released. Already assigned addresses remain visible and manageable. Do not add
a global `default_scope` to Network or IpAddress: it would hide existing service
from config generation, history, cleanup, and association expansion.

The continuity exception belongs to existing, trusted migration/replacement
operations retaining the same owner and holding the relevant reservations. It must not become a client input
that bypasses the new-assignment guard. Do not place a blanket enabled check in
the low-level route transaction or node daemon: they also execute continuity and
rollback work. Preserve current routing and reachability constraints; the flag
does not make an old network physically reachable in a new location.

## Shared backend changes and interfaces

1. Add one non-null boolean `networks.enabled`, database default `true`, plus
   boolean validation. Existing rows and older clients creating a network retain
   current behavior. No data-driven automatic disabling and no migration guards
   for stale disposable schemas.
2. Expose `enabled` through Network Create/Update and Index/Show, add an optional
   exact Index filter, and allow only administrators to write it. Omission on
   Update must not reset a disabled network. Include it in member read output
   so consumers can explain unavailable existing allocations.
3. Centralize the enabled policy in a small Network/IpAddress helper. Add enabled
   selection to `IpAddress.pick_scope` and a current locked check shared by new
   assignment/ownership entry points. Place the explicit-ID guard in the
   AddRoute chain for all callers, not only actor-dependent validation. Early
   validation must respect the lock order below. Cover owned registration,
   IpAddress ownership changes and VPS owner changes, which do not go through
   automatic selection.
4. Update `User.AvailableIps` and free-address selection queries so disabled
   rows are not offered as usable. Keep inventory/history listings able to show
   disabled networks; if a new selection filter is needed, make it explicit and
   preserve list defaults. Audit cached React selectors and release-request
   assignment hints: the API must reject a stale ID regardless of UI state.
5. Keep `ipv4_left` as the existing integer field. Compute the count once in the
   API; both frontends continue reading it unchanged.

Required count criteria are: an existing IpAddress row, no owner, no interface,
network enabled, IPv4, role public_access, and no IpAddress resource reservation.
A reusable unlocked scope can serve this query and the picker;
do not apply a current-user picker to an unauthenticated global statistic.

Retain the current **allocation-row count**, not subnet size or theoretical
network capacity. Multi-location networks count once. The flag is the explicit
operator decision to include a network's remaining inventory. Do not additionally
infer retirement from purpose, managed state, autopick/userpick, maintenance,
node uptime, or missing locations. Those can still make part of the enabled
inventory unavailable to a particular VPS; this is a cluster inventory statistic,
not a promise that any user can allocate the displayed number. A separate
per-location readiness metric is outside this minimal fix.

Expected source boundaries: V schema/migration, Network and IpAddress models,
NetworkInterface/AddRoute and ownership/registration guards, resources Network,
Cluster, User and allocation selectors; the legacy cluster list/form/action;
relevant regression specs and IP documentation. W network types/adapters,
NetworksPage, affected free-address selectors, catalogs and design/work log.
Include V `transaction_chains/vps/update.rb` for owner-transfer admission.
C changes are generated application channel pin commits only, preserving the
existing input mappings and follows edge. No new protocol, Nix module option,
generated daemon configuration, unrelated dependency bump, or routing change.

## Concurrency

Initial filtering is insufficient. Use current SQL shared reads of network rows
for admission and hold those locks until chain preparation or the synchronous
write commits. A toggle acquires the network row's exclusive update lock. The
lead accepted the following lock-order clarification on 2026-10-06:

1. Identify candidate networks without locking existing IP rows. Acquire shared
   network row locks, in ascending network ID order for a known batch, before
   current IP row locks. Check enabled. Registration already takes an exclusive
   network row lock before inspecting/creating IP rows and must retain that order.
2. Preserve existing resource-reservation ownership and IP-ID ordering, followed
   by host-address reservations. Reserve/reload the selected IPs, then perform
   authoritative enabled, ownership, purpose and location rechecks while the
   network locks are still held. Confirm each current IP belongs to a locked
   network; do not silently acquire a different network late in a batch.
3. `ensure_pickable!` currently uses a joined `FOR UPDATE` query. Do not upgrade
   already-shared network locks through that join: the selected IP row is already
   exclusively locked, so use current shared reads for the joined policy recheck.
   The same rule applies to explicit assignment's current network/location reads.
4. Automatic multi-address selection must capture and lock the whole containing
   operation's candidate network set before its first IP row lock. Retain that
   set across allocation counts, resource families and interfaces; nested chain
   calls do not release SQL locks. Later picks use only already-held networks,
   with current eligibility rechecks. Shared locks must remain shared. Keep any
   selection retry within the established transaction/reservation cleanup rules.

This avoids an IP-then-network inversion against `Network.add_ips` and
`preserve_allocation_resource`, which currently take network locks before IP
locks. Do not solve it with a chain-long exclusive resource lock on the whole
pool. Network toggling must not enumerate or lock its allocation rows. Add
coverage for concurrent registration/role validation as well as toggle admission,
and for two allocations in the same network so shared-lock upgrades are caught.

The commit order defines the result: disable first means the new-use operation
fails or picks another enabled pool; admission first means a prepared chain may
finish after disable. Disabling does not cancel previously accepted work.
Document that boundary in admin feedback. Resource reservations keep such
pending addresses out of the proposed count. Tests must force both interleavings
with separate database connections, not just stub a changed model instance.

### Migration and swap batch boundary clarification (2026-10-06)

The current draft's `Vps::Migrate::Base#setup` locks source and candidate
destination networks before source IP rows, but discards the returned network
map. Its later `pick_replacement_ip` calls `IpAddress.pick_addr!`, which computes
and locks a fresh candidate set, followed by `lock_for_new_use!`, which also
acquires a network lock. Newly enabled/configured pools could therefore enter
after source IP locks are held. `Vps::Swap` includes migration setup twice in one
outer chain, so its second setup can also introduce network locks after the
first setup's IP locks. The accepted network-before-IP ordering applies across
the whole containing operation, not separately to each helper invocation.

Use a retained, transaction-local network map for these concrete boundaries:

- In standalone migration `setup`, capture source network IDs and the candidate
  destination IDs actually needed for replacement. Acquire their sorted union
  once and retain the returned map through preparation. Candidate discovery is
  unnecessary when `handle_ips` or `replace_ips` is false, or when migration
  retains addresses instead of taking the replacement branch. Source networks
  remain in the continuity set even when disabled.
- `pick_replacement_ip` must select only within the retained destination ID set,
  intersected with the current `pick_scope` and unreserved predicate. Do not
  rerun unrestricted candidate discovery or acquire network locks there. An
  empty retained set means no replacement, never fallback to all networks.
- Give `pick_addr!` and `lock_for_new_use!` an internal retained-map path, or use
  an equivalent narrowly scoped helper: attach the already-held network object,
  reserve/reload the IP, verify its current `network_id` belongs to that map,
  then check enabled and current allocation policy. No network-lock acquisition
  is allowed on this path. Reject an identity mismatch or unavailable selection;
  do not widen the set after IP locks. Ordinary standalone callers can retain
  their initial network-locking path before any IP row locks.
- In `Vps::Swap#link_chain`, after reserving both VPSes and before either
  migration setup or other work takes IP row locks, collect both current source
  IP sets. Acquire the union of their network rows once, then reserve/reload the
  union of IP parents in ID order and their hosts afterward. Both migration
  calls have `handle_ips: false` and `replace_ips: false`: they require no
  destination free-pool discovery. Pass this same internal map to both setups;
  each setup reuses it and validates current identities without locking a new
  network. Reuse must still perform required current IP reads, even when the
  outer chain already owns their resource reservations.

The retained map is internal chain-preparation state, never API input, a public
bypass flag, or a cache reusable across SQL transactions. Do not require enabled
for the entire continuity map; apply that check only when taking a new address.
Network additions outside the captured set wait for a fresh request/preparation
after the current transaction and reservations have been released. Existing
changed-selection/no-capacity behavior is sufficient; do not retry by growing
the map while holding IP locks. Lock only this operation's source/candidate
networks, never all cluster networks. This is call-site guidance for the accepted
design, not an independent code review or runtime verification result.

### Automatic allocation batch lifetime clarification (2026-10-06)

Source inspection of the session-owned V draft confirms the containing SQL
transaction: `api/models/transaction_chain.rb` `fire2` (lines 73–114) wraps
`link_chain` in `transaction(requires_new: true)`; `use_chain` (383–405) invokes
`use_in` (132–165), which calls the child method directly without committing.
The plain `IpAddress.transaction` in `Ip::Allocate#allocate_to_netif` therefore
joins that transaction. Returning from a pick or included chain leaves prior
IP locks held. A nested `requires_new` savepoint would not fix this ordering.
This establishes the boundary from source; no runtime deadlock was reproduced.

Use explicit domain-level keyword arguments for a held network map and captured
candidate IDs; no `TransactionChain` registry or framework-wide lock mechanism:

- `Vps::Create#link_chain` (`transaction_chains/vps/create.rb`, family loop
  around 201–229): capture selections for all requested positive resource counts,
  retaining the destination's IPv6 support rule. Before the first IP lock,
  acquire the sorted union of their candidate networks once. Pass that context
  to every `Ip::Allocate#allocate_to_netif` invocation. Derive candidates from
  the same target owner, location, allocation environment, role, purpose and
  optional address location used by allocation, preferably with one shared
  selection builder.
- `Vps::Clone::OsToOs#clone_network_interfaces` and `#clone_ip_addresses`
  (`transaction_chains/vps/clone/os_to_os.rb`, around 441–532): capture positive
  family counts and destination selections across **all** source interfaces
  before the first allocation. Preload one union and pass it through both
  helpers to every allocator call. Per-interface preloading is insufficient.
  Select for the destination owner and node, preserving `strict: false` partial
  allocation. If source continuity IPs are locked earlier in clone preparation,
  prepare this destination set before those locks and union it with the source
  network IDs at that earlier boundary. Preserve source parent/host reservation
  order and allow disabled source networks for continuity; do not remove or
  postpone an existing source lock to make a later preload appear safe.
- `Ip::Allocate#allocate_to_netif` also loops when `n > 1`. With a parent context,
  every pick and `lock_for_new_use!` must use the held-map path described above,
  without network discovery or acquisition. A standalone call prepares its one
  selection's candidate map once before entering the loop, while it holds no
  IP locks. Keep the zero-count fast return. A provided empty candidate set
  means no capacity under the existing strict/non-strict behavior, never a
  signal to fall back to unrestricted selection. Retain current policy and
  identity checks after each IP reservation, constrained to the captured set.
- `Export::Create#pick_ip_address` (`transaction_chains/export/create.rb`,
  around 130–148) retries selection of **one** private IPv4 export endpoint.
  It returns after its first successful pick; ordinary resource-reservation
  contention occurs before the selected IP's `reload(lock: true)`. That loop
  alone does not establish the Create/Clone multiple-success inversion. Prepare
  its single selection context once before the retry loop and pass it to both
  picker and new-use guard for consistent bounded retries. Later `all_vps`
  grants use `ExportHost.lock_ip!` on existing assignments without acquiring
  network admission locks, so they require no additional candidate pool set.

When a map includes disabled source continuity networks, keep destination
candidate IDs distinct and check enabled only for new use. A newly available
pool outside the captured set waits for a fresh preparation after the current
transaction releases its locks. Do not broaden the map after a successful
allocation, commit between families, or change allocation atomicity/retry policy.

## Administrator UI and compatibility

Both network lists should show enabled state and retain disabled rows. Legacy
Cluster/Networks needs a CSRF-protected POST action with explicit target state;
React can extend its existing edit flow. Show network identity, existing assigned
and owned counts, and explain that existing service continues while detached
allocations cannot be assigned. Re-enable uses the same normal API update.
Neither interface changes the public-counter arithmetic.

The additive field does not require existing generated Go/Ruby clients or
Terraform consumers to update just to keep working; they cannot manage the new
flag until they learn it. The dynamic API/CLI can expose it through discovery.
Verify actual client tolerance and stale API-description caches before rollout.
New UI controls must be absent/unavailable against an API that does not advertise
support; a missing value must not be displayed as a confirmed disabled state.

Implementation includes Czech/English copy and the owning repositories'
localization/KB impact workflows; KB production publication is a separate action.
Lasting semantics should live in V IP/network documentation
and W requirements/workflow docs; individual rollout evidence stays in session
records.

## Configuration pins, rollout and recovery

Prepare one final pin update per application in the session-owned configuration
feature worktree after its source head is committed and selected by the lead.
For exact feature revisions, use the repository's Nix shell and channel tools:

```sh
confctl inputs channel set --commit vpsadmin vpsadmin <vpsadmin-revision>
confctl inputs channel set --commit vpsadmin-webui vpsadmin-webui <webui-revision>
```

For a selected published default-branch release, the corresponding normal
commands are `confctl inputs channel update --commit vpsadmin vpsadmin` and
`confctl inputs channel update --commit vpsadmin-webui vpsadmin-webui`; verify
their resolved heads are the intended release. Do not manually edit `flake.lock`
or use an unrelated production/staging channel. Preserve generated commit history
and the `vpsadminWebui.inputs.vpsadmin` follows edge to `vpsadminServices`.
Inspect exact pins and expected transitive changes; keep unrelated inputs fixed.
Both pins belong to the implementation deliverable and its review packet.

The follows edge means an API pin change also changes the WebUI's effective
vpsAdmin input even if its own application revision is unchanged. Validate the
combined final input graph and affected API/PHP and React/BFF packages, with
configuration builds after final review. A pin commit does not deploy it and is
not permission to integrate configuration master. Deployment, when authorized,
uses this order:

1. Confirm deployed revisions and inspect per-network contributions read-only.
   Identify obsolete networks explicitly; do not change role to hide inventory.
2. Apply the additive default-true migration and deploy API/writer code that
   enforces enabled. Clear/refresh normal API discovery caches as needed.
3. Replace all old API and other allocation writers before disabling anything.
   Old code ignores the flag, so mixed writers are safe only while every network
   remains enabled. Already prepared chains may finish under the admission rule.
4. Deploy both admin UIs; verify API/CLI and both unchanged public-counter clients.
   Explicitly disable the operator-selected networks and verify the count delta
   and continued operation of existing assignments. No node-wide update required.

Rolling back only the UI is safe; leave the column and enforcing API in place.
Re-enabling a network is the reversible operational recovery. Rolling API code
back to a version that ignores enabled is unsafe while any network is disabled:
it can allocate retired addresses again. Retain the enforcing version or first
stop new-allocation writers and deliberately resolve all disabled-network policy
before restoring old writers. Do not silently re-enable obsolete pools or drop
the column as routine rollback. Existing route/ownership data remains readable
by old code; loss of admission policy is the compatibility risk.

## Read-only production diagnostic, not executed

The query below reproduces current counter contribution by network at V's
schema while exposing the reserved subset and selection-policy context.
`public_access` is enum value 0 at V; verify the deployed enum/schema first.
Subqueries avoid multiplying allocation rows by location associations.

```sql
SELECT n.id, n.address, n.prefix, n.ip_version, n.role, n.purpose,
       n.managed, n.primary_location_id,
       COALESCE(i.free_rows, 0) AS unowned_unassigned_rows,
       CASE WHEN n.ip_version = 4 AND n.role = 0
            THEN COALESCE(i.free_rows, 0) ELSE 0 END AS current_ipv4_left,
       COALESCE(i.reserved_rows, 0) AS reserved_subset,
       COALESCE(l.locations, 0) AS location_count,
       COALESCE(l.autopick_locations, 0) AS autopick_locations,
       COALESCE(l.userpick_locations, 0) AS userpick_locations
FROM networks n
LEFT JOIN (
  SELECT ip.network_id, COUNT(*) AS free_rows,
         SUM(EXISTS (SELECT 1 FROM resource_locks rl
                     WHERE rl.resource = 'IpAddress' AND rl.row_id = ip.id))
             AS reserved_rows
  FROM ip_addresses ip
  WHERE ip.user_id IS NULL AND ip.network_interface_id IS NULL
  GROUP BY ip.network_id
) i ON i.network_id = n.id
LEFT JOIN (
  SELECT network_id, COUNT(*) AS locations,
         SUM(autopick = 1) AS autopick_locations,
         SUM(userpick = 1) AS userpick_locations
  FROM location_networks
  GROUP BY network_id
) l ON l.network_id = n.id
ORDER BY current_ipv4_left DESC, n.id;
```

Sum `current_ipv4_left` to compare with a contemporaneous PublicStats response;
concurrent allocation can change it between reads. After migration,
include `n.enabled` and measure the proposed complete predicate separately.
Investigate deployment/data disagreement before claiming the production cause.

## Acceptance and verification brief

Quick checks, inside the declared Nix environments, should establish:

- Migration defaults existing/new rows to true; false persists; omitted Update
  cannot re-enable. Member writes fail and disabled inventory remains readable.
- Independent fixtures prove the public count excludes disabled, private-role,
  owned, assigned, IPv6 and reserved allocations; includes an enabled public
  allocation exactly once across multiple locations. Preserve role-only
  classification and row-count semantics.
- Picker and locked recheck reject disabled networks for VPS create/clone,
  export creation, replacement allocation and owned detached reuse. Explicit-ID
  AddRoute, IP/VPS ownership changes and owned registration cannot bypass the flag.
- Existing routes/ownership and unowned inventory registration follow the table;
  release, rollback and same-allocation continuity remain possible.
- Both toggling directions, stale form/selector state, errors, authorization,
  old API feature detection and cs/en rendering work in both interfaces.
- Both configuration channel pins resolve to the selected source heads; the
  WebUI's effective API input follows vpsadminServices. No unrelated channel or
  host-policy changes appear in the generated diff.

Extend V `cluster_spec`, network read/write specs, user_available_ips specs,
Ip::Allocate/AddRoute/Ip::Update/registration specs and existing IP concurrency
coverage. Do not reproduce the implementation query as the expected result.
Run scoped RuboCop/PHP checks and relevant React type/unit checks; use the
repository's full/core topic placement rules for any new API spec files.

After completed implementation, all intended source/UI/configuration/docs
changes committed, and quick checks passed, perform mandatory independent final
review before long integration verification. Include complete branch histories,
final diffs and migration provenance; consolidate obsolete unapplied migrations.
This brief revision itself is planning and does not trigger that review.
Longer checks should exercise both disable
race orders using real MariaDB connections, then an isolated cluster: retain a
working VPS/export while disabling its pool, reject new allocations through API
and UIs, migrate/restore existing service, release an address without making the
disabled pool available, and re-enable it. Preserve and verify a known data file
through migrations/restores. Confirm routes and connectivity, not just API
responses. Validate mixed-version restrictions and migration recovery on a
disposable database. Follow the fresh verification-watcher procedure for long
or uncertain runs; no such runs have been launched here.

Remaining evidence: deployed version and database contribution breakdown;
operator-selected obsolete networks; runtime coverage of each continuity path
and third-party/site allocation writers. Implementation is authorized through
the lead; production inspection/mutation and rollout are not authorized by this
architect assignment.
