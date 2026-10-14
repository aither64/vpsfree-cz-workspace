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

## Accepted non-admin list visibility refinement (2026-10-06)

The user selected “Keep owned IPs visible” and authorized implementation. This
supersedes the earlier unrestricted non-admin inventory-list wording only.
Evidence baseline: V `be136b6c00f03b85b7a12cc57550b4a1394a94a7`, W
`e4c49bcdc91b33b7f644a2f125231cb413cf4bf4`, C
`dd10d88073da3aed6c4512e938abe4374422aab1`, K
`291566b2c0bd43389802f607852fd9a4f8241752`.

The minimum implementation is two resource-level query restrictions in V:

- `api/lib/vpsadmin/api/resources/network.rb`, `Index#query`: non-admins
  always intersect the query with `enabled=true`. An explicit `enabled=false`
  filter consequently returns no rows; it cannot widen access. Administrators
  retain existing inventory and exact filter behavior.
- `api/lib/vpsadmin/api/resources/ip_address.rb`, `Index#query`: retain all
  existing filters and `user_visible_scope`, then intersect non-admin results
  with `(network enabled OR owned by caller OR currently assigned)`. The
  assignment arm is safe only inside that existing permission intersection:
  it must not independently admit another user's assigned IP. Keep detached
  owned IPs and nonowned IPs assigned to an accessible VPS on disabled networks;
  remove disabled unowned/unassigned inventory. Explicit `network_enabled`,
  network, address, interface and VPS filters only narrow that result.

Apply both predicates in SQL before `count`, ordering and pagination. Do not
filter serialized pages, add joins that duplicate rows, introduce a model
`default_scope`, or change the shared `user_visible_scope`. `IpAddress.Show`
uses that scope, while `user_visible_as_association_scope` additionally permits
the caller's export endpoints. Preserve both paths and their existing field and
ownership restrictions: disabled known-ID records previously readable stay
readable, previously forbidden records stay forbidden, and host-IP, export and
history associations keep their current access. Association-only access to an
unowned export endpoint does not become direct Index access.

Consumer evidence: legacy `webui/forms/networking.forms.php#ip_address_list`
requests included network details without an enabled-only IP-list filter. W
`src/pages/app/networking/UserNetworkPage.tsx` combines active assignment history
with owned detached IPs and retains disabled badges. Its
`fetchAssignableIpAddresses.ts` and legacy `webui/lib/functions.lib.php` apply
enabled-only filtering to new-assignment choices; keep those restrictions.
Included details must continue to resolve through existing Show permissions,
even though the non-admin network filter menu now enumerates enabled pools.
No concrete frontend edit is required by these inspected consumers; do not add
blanket enabled filtering in either UI. Root owns final product/documentation prose.

Extend existing Network/IP API specs with member and support fixtures covering
enabled/free, disabled/free, disabled owned/detached, assigned nonowned, and
another user's owned/assigned addresses. Assert explicit false/network/address
filters cannot reveal hidden inventory; visible counts and multi-page cursors
exclude it while retaining eligible owned/assigned rows. Cover unchanged admin
inventory, disabled Network/IP Show, forbidden Show, included disabled network
details, assigned host IPs, own/foreign export associations and assignment
history. Preserve existing role, purpose, userpick and location permissions.
Update V `docs/ip-locking.md` inventory semantics. Run focused existing API specs
and relevant hooks, commit, and obtain independent final review before any
longer verification. This design clarification runs no checks.

No field, migration, allocator, locking, counter or role-classification changes
are needed. Existing disabled admission and continuity rules remain binding;
list visibility never grants assignment. After publishing the final V feature
head, regenerate only C's `vpsadmin` channel/`vpsadmin` role and K's exact V pins;
retain the W channel pin unless a concrete W change is required. The schema and
API shape remain compatible; older APIs may enumerate more inventory, and
rolling readers may temporarily differ. Reverting this refinement restores that
enumeration without changing allocations or admission. Keep all changes on
feature branches; no PR management outside W, integration, deployment, capture,
package transition or lifecycle action is authorized by this refinement.

## Accepted portable KB runtime implementation (2026-10-07)

The user authorized implementation of the standalone KB runtime and optional
workspace adapter. This extends verification tooling only; the accepted network
feature, role-only classification, source heads and downstream pins remain
unchanged. Architect0 owns this brief, implementer0 owns source, and lead owns
coordination, source publication and any later activation decision. No command
in this brief has been executed as verification or lifecycle work.

### Scope, evidence and repository ownership

Use the two worktrees registered by the lead under this session:

- `worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-kb-contracts-runtime`,
  branch `2026-10-05-network-ipv4-left-counter-kb-runtime`, starting at
  `a50f8c1a11ea642edf823f04521f9eaa97132fd2`. Leave the original K worktree and
  network pin branch unchanged. Its exact vpsAdmin input remains
  `5d5527a67315c18b595345aa6996d7724c1ed071`.
- `worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-dev-workspace`,
  branch `2026-10-05-network-ipv4-left-counter`, starting at freshly fetched
  `0ff827df13e82dfab4b536ff29979280f264e8f5`. The canonical bare local
  `master` was older `f2fdbcebc115b7fd07ab6e0c91ebea189a57f341`; do not develop
  from it or discard the newer maintenance/provider behavior.

K owns the single portable launcher, runner, state schema, connection/lease
protocol, source attestation and capture integration. Its README and
`docs/webui-change-workflow.md` already require operation without another
workspace at runtime. The extension owns the optional `kb` provider's session
binding, package-generation integration and provider protocol translation.
Document the portable contract once in K's `cluster/README.md` or a linked
runtime contract document; extension documentation links to it and owns only
the managed integration. No generic runtime, V, W, C, production KB or workspace
package-selection edit is presently necessary.

Confirmed K mechanisms at the stated baseline:
`bin/devcluster:7,54,230,242,754,876,1189` combines checkout-local state with
slug-only global sockets, PID-existence checks and broad process/path cleanup.
`cluster/lib/runner.rb:8` uses a fixed runner hash base;
`cluster/nix/test.nix:1276-1301` uses a slug-based inter-VM network and fixed
services forwarding ports. `lib/dev-cluster.cjs` reads implicit local state and
shared credentials; `lib/browser.cjs:36,51` hardcodes a site suffix and port.
`runner/capture.cjs:14-20,40-47` compares inventory and lock-file revisions,
without proving the running cluster's source. These are the implementation
boundaries, not evidence of a particular foreign process having been affected.

The extension's `flake.nix`, `nix/organization-tools.nix`,
`nix/site-config.nix`, `dev-clusters/lib/runtime.sh` and provider tests define
packaging and integration. Its selected generic runtime
`6a972b9ab01077611b2c60e0fc726c185e050315` discovers arbitrary catalog providers:
`libexec/workspace-host#dispatch_cluster` holds the current generation lock;
`development_cluster_state` enumerates provider-specific state;
`require_compatible_development_cluster_helpers!` calls candidate
`transition-adopt`; `libexec/dev-session` consumes `cleanup-paths` and `reset`.
`portal/internal/cluster/status.go` supports provider-owned status. This permits
an adapter without a generic runtime change. Preserve the current workspace
state-schema/transition-policy contract, including maintenance holds of other
providers. A need to change that contract is a material deviation for the lead.

### One engine, explicit inputs and portable state

Keep `bin/devcluster` as the familiar entrypoint and package the same K-owned
engine as a named flake executable. Both must call the same lifecycle code;
do not maintain shell and workspace implementations of VM startup/cleanup.
The engine can reuse K's Ruby runner and existing Node capture stack; this is
not a new general orchestration framework. Separate immutable software source
from mutable state. Standalone defaults to `<checkout>/.devcluster/v2`, accepts
an explicit `--state-root`, and never examines `DEV_SESSION_*`, a workspace
registry, sibling worktrees or installed provider files. A packaged invocation
uses an explicit state root or the documented invocation-directory default,
never a writable path beneath its store source.

State schema 2 has `clusters/<slug>/identity.json`, generated config, per-instance
credentials, disks, logs, result roots and run receipts. Locks live outside the
removable cluster directory. Validate slug components, ordinary path ownership,
private permissions and symlinks before access. Initialize identity and the
chosen resource namespace atomically under a persistent cluster lock before any
resource creation. Required identity fields are `schema`, `instance_id` (random
UUID), `owner_uid`, canonical `state_root`, `slug`, and `created_at`. Reusing a
copied identity from a different root fails; no ownership inferred from CWD,
missing environment, a PID or an absent socket. Reads do not create/repair state.

Each start gets a new `run_id`. Persist an immutable launch receipt containing
`instance_id`, `run_id`, `boot_id`, `owner_uid`, config digest, exact runner and
source provenance, recorded socket directory, resource claims and process
identities. Each process identity includes PID, Linux start ticks, executable,
and exact config/state/socket argument tuple; the launcher handoff and runner
readiness also carry the run ID. Store phase changes atomically so interruption
between reservation, build, spawn and ready is recoverable without guessing.
Readiness must identify this run, not merely leave a file from an earlier run.

Give each instance its own SSH keys, known-hosts trust, CA/leaf material and
config result roots. Use a short, private K-specific runtime directory selected
from the user runtime directory (with a validated private per-UID temporary
fallback); namespace by root/instance/run and record its exact path. Never use
the old `vpsfree-devcluster-<slug hash>` namespace. Feed the instance/run identity
into OSVM hash/network identifiers where host resources derive from them.

### Locks, reservations and cleanup

Use a per-instance lifecycle/capture gate followed by a short operation lock.
An exclusive capture lease holds the gate for the complete fixture/browser/SSH
operation, so two captures cannot change locale or fixtures concurrently and
stop, reset, update and credential replacement cannot invalidate a capture.
Status may read an atomic receipt or return a documented busy result; it must
not wait unboundedly. A runner-liveness lease is separate from the operation
lock so ordinary stop does not deadlock against a lock held for VM lifetime.

Reserve only the explicitly requested host resources. A small per-user K
reservation directory records actual TCP bind addresses/ports, inter-VM network
identity and bridge/address claims. Under one short reservation lock, compare
and claim the complete sorted resource set, or fail without a partial launch.
Do not automatically select another port, allocate a host subnet, edit host
networking, kill a listener or offer a force bypass. Durable claim records refer
to the instance/run receipt; loss of a locking process does not prove that its
VMs exited. Release claims only after proving that owned processes/resources
are gone. This registry coordinates K instances, not arbitrary host software;
kernel bind failures and observed foreign conflicts remain hard failures.

Bridge stays the default. Require explicitly dedicated, disjoint addresses for
concurrent bridge clusters. An unresponsive address is not proof of ownership;
the operator supplies the dedicated network configuration. Local mode needs
explicit forwarding ports and an isolated inter-VM network identity. Record the
resolved configuration and detect duplicate claims before spawning. Preserve
the existing VM resource sizes; insufficient RAM/shared memory remains a
verification prerequisite, not a reason to overstate capacity or rebuild kernels.

Runner-owned shutdown is the normal path. Request it through a validated runner
control channel, then wait for tracked VM children to exit and be reaped. A
forced signal requires a stable process handle (for example a Linux pidfd)
after matching UID, boot ID, start ticks and the runner tuple; never signal a
numeric PID based only on `kill -0`. Track child identities before allowing
recovery to act on them. Remove only paths recorded for the proven instance/run,
after the corresponding processes are gone. No `pgrep -f`, substring process
selection, broad process-group cleanup, recursive deletion of unknown sockets,
or GC-root removal while a live VM still depends on the closure. Keep ambiguous
orphan state and claims intact and report the exact missing proof. Start/stop
retries must converge on their own receipt without claiming unrelated state.

### Shared connection and capture-lease contract

`bin/capture --cluster SLUG` and optional `--connection FILE` are mutually
exclusive selectors for the same validated connection schema and capture path.
`--cluster` obtains a descriptor from the local engine; it does not continue to
read legacy config/network files itself. The explicit external descriptor is
for a dedicated capture environment, not an arbitrary URL or production target.
Keep its files private and outside Git; export credential references, not secret
values in status, provenance or logs.

Define connection schema 1 with these fields:

- `schema`, `kind` (`vpsfree-kb-connection`), `owner_id`, `instance_id`,
  `run_id`, `topology`, and `capabilities` including `capture-lease-v1`, `ssh`
  and the fixture capabilities needed by the requested checkpoint.
- `services`: named logical URLs and their explicit connect host/port mappings;
  `machines`: named SSH endpoints, user and private key/known-hosts references;
  `tls.ca_file`; and `accounts_file` referring to dedicated fixture accounts.
  File references are resolved against the descriptor directory, with absolute
  paths allowed for explicit runtime locations. No site path is compiled in.
- `provenance`: the immutable launch/source receipt described below.
- `control.argv`: an explicit executable/argument vector for the owning
  controller's `capture-lease` operation. No shell command string, automatic
  workspace discovery, inherited arbitrary source override or fallback to a
  different controller. This is trusted local operator configuration, not a
  remotely supplied executable instruction.

The capture process starts that controller with the expected instance/run and
descriptor SHA-256. Lease protocol 1 emits exactly one bounded JSON readiness
record containing `schema`, `instance_id`, `run_id` and `descriptor_sha256`,
only after acquiring the gate and verifying live identity/provenance. The
controller holds the lease until its supervised capture peer closes the pipe.
Use a full-duplex lifetime channel so peer/controller loss interrupts capture;
do not continue fixture calls with a dead lease. Check lease liveness before
each fixture/SSH mutation and cancel browser activity on loss. Shutdown cleanup
must complete before releasing a normally terminated capture lease. Other
lifecycle operations still prove process exit before reclaiming its resources.

The returned descriptor is an access description, not lifecycle ownership.
External stop/reset/update remains exclusively with that environment's owner.
All capture SSH/browser consumers use the leased connection, including fixtures,
console and CLI scenarios. Use exact configured host routing in
`lib/browser.cjs`, preserving logical Host/SNI, rather than the hardcoded suffix
and port. Do not route arbitrary destinations to the cluster. Remove implicit
endpoint construction from `lib/dev-cluster.cjs`; derive WebUI/API/console and
SSH access consistently from the descriptor, including nondefault local ports.

### Source provenance and fixture boundary

Build the cluster and runner from one committed, immutable K flake snapshot.
The receipt records K revision and source store identity, lock-file digest,
each relevant locked input revision and narHash (especially V and vpsAdminOS),
generated config SHA-256/store path, runner executable/store path and expected
machine toplevels. It also records the fixture contract digest. Do not follow
the extension's ordinary V/OS inputs or infer source from a nearby checkout.
Uncommitted runtime code is not accepted for final screenshot evidence.

Generate a guest-readable capture identity from that exact build: instance ID,
source/fixture digests and pinned input identities. Over the connection's
verified SSH trust, compare it and each running system closure with the launch
receipt, then compare the live V identity with both `captures.json` and the
capture checkout's lock. A host descriptor alone is not live-source proof.
Validate the current run lease as well. Perform these checks before login or
fixture mutation, and invalidate readiness on a partial update or mismatch.
External providers must supply the same proof/capabilities or fail clearly;
there is no weak external-connection bypass. Record verified instance/run and
source evidence in generated capture provenance without recording secrets.
No vpsAdmin application API change is required; K owns guest identity metadata.

### Optional workspace adapter and packaging

Add the optional `kb` provider in `vpsfree-dev-workspace`, with public command
`kb-devcluster`. An optional `siteConfig.clusterDefaults.kb` enables it; when
absent, existing package/provider behavior stays unchanged. Validate it with
the existing site-config mechanism. Concrete bridge addresses, endpoints and
credential locations stay in the consuming workspace, never extension source.
Add an exact published K input to the extension and consume K's packaged engine
and locked source. Do not use a mutable branch or an unexplained environment
source override. Preserve K's own V/OS lock graph; do not add `follows` to the
extension's different devcluster inputs. Publish the K engine commit before
generating the extension input lock. Ordinary pinned-input updates then select
a new engine explicitly and are covered by provider compatibility checks.

Managed state belongs under `.dev-clusters/kb/clusters/<session slug>` so the
existing runtime inventories it. Pass `.dev-clusters/kb` as the engine's explicit
state root; add an extension-owned binding record for workspace, session slug,
provider ID, engine revision and portable schema. The engine has no knowledge
of workspace/session meaning. Keep that binding distinct from portable schema 2
and the unchanged generic workspace state-schema contract.

Implement `status SLUG --json`, `reset SLUG`, `cleanup-paths SLUG` and
`transition-adopt SLUG`, plus the explicit start/connection/capture-lease access
needed by operators. Translate engine status to the existing provider schema;
use busy exit 75 and bounded status/cleanup budgets. `cleanup-paths` returns the
existing `{schema: 1, paths: [...]}` shape, containing only verified managed
state/socket paths. `transition-adopt` validates the binding, recorded socket,
portable schema, runner/source compatibility and retained leases without
rewriting provenance or inventing ownership. A candidate lacking `kb`, or an
incompatible K engine, must refuse while this provider owns state. Do not change
global transition policy numbers to force acceptance or weaken other providers'
maintenance-hold rules.

All public managed mutations and `capture-lease` run through the existing stable
workspace-host dispatch, retaining its generation guard for the whole operation.
The adapter checks the explicit selected workspace/session and normal lifecycle
journal exclusions. Reuse extension lock/session validation primitives where
appropriate; do not blindly reuse its legacy socket calculation or cleanup
helpers, which describe a different engine. Lock order is outer workspace
generation/session guards, adapter cluster lock, K gate/operation lock, then the
short K resource-reservation lock. The long-lived VM runner must not inherit
workspace generation/session or command-operation locks. The capture controller
does retain the generation guard and K capture gate for its lease lifetime.
Managed descriptors point to this public routed controller, not directly to a
store-private provider/engine that skips generation validation.

The extension trusts the local host operator. Test ordinary configuration
mistakes, foreign/stale state, races, retry and credential integrity; do not add
defenses solely for a compromised operator fabricating mounts or lock files.
The guest/remote connection and source-verification boundaries still apply.

### Compatibility, legacy state and activation limits

Do not adopt legacy `.devcluster/clusters` state or slug-only global sockets.
Report it without touching it; use fresh v2 instances with explicit disjoint
resources. Old binaries do not understand v2 and must not be used to manage it.
Preserving legacy disks or live clusters is outside this accepted disposable
recreate path. Any legacy cleanup needs its own explicit authorization and
complete ownership proof; this brief does not authorize it.

Unknown state/descriptor/protocol versions fail before mutations. Future
state-format upgrades require an explicit compatibility path; do not silently
migrate on read. A failed package/source update retains original run receipts
and rooted closures. Recovery uses a compatible reviewed engine; rollback must
not feed new state to an older launcher. Recreating an owned disposable cluster
is an operator decision, never an automatic rollback. App/database schema,
daemon protocol, existing allocated IPs and production deployment are unaffected.

Source adapter development and feature publication are authorized. Installing or
activating a workspace package/provider, selecting configuration inputs in this
workspace, launching a managed cluster, default-branch integration and production
publication remain separate operations. A built adapter does not itself make
the installed catalog support K. Do not invoke private/new store helpers against
real managed state to bypass activation. A standalone host may use the reviewed
K tool without a workspace package, under explicit ownership and launch scope.

### Implementation and verification brief

K changes are limited to its launcher/runner and small runtime support files,
`cluster/nix/test.nix`, default configuration/flake packaging, connection/capture
arguments and consumers, meaningful tests, and owning docs. The extension adds
the thin provider, optional site configuration, exact K input/package wiring,
provider/compatibility tests and owning documentation. Do not copy K's VM
definition, fixture code or cleanup implementation into the extension. Report a
required third repository or changed network/application pin before proceeding.

Before edits, implementer reads each owned worktree's instructions and verifies
the registered heads. Use each repository's declared Nix environment; inspect
and enable any declared hooks before commits. No new hooks or package activation
are prerequisites just because the repository lacks a hook framework.

Quick verification should extend K `bin/check` with focused runtime and
connection tests using fake runners/transports and temporary state, alongside
existing syntax, shell, Nix parse, browser and contract checks. In the extension,
run the focused new adapter Ruby tests and affected existing
`test/devcluster_{commands,status,runner}_test.rb` in its declared environment.
Cover these behavior boundaries rather than mirroring helper implementations:

- Standalone invocation outside any workspace with session variables absent;
  two roots using the same slug, explicit disjoint endpoint configuration, and
  independently owned identities, sockets, credentials and cleanup.
- Concurrent start/stop/update/reset/capture, ordered multi-resource claims,
  capture/controller interruption, partial launch and retry; no released claim
  while tracked VM children remain. Busy status is bounded and read-only.
- Stale PID/start-time/boot identity, foreign processes and socket paths,
  missing/unsupported ownership, path escape/symlink mistakes and legacy state
  all refuse without signaling/deleting unrelated resources.
- Port/bridge conflicts fail without automatic fallback or foreign cleanup;
  exact arbitrary configured host/port routing, API/console/SSH consistency and
  no hardcoded site suffix. Same-slug concurrency must exercise actual resolved
  network resource identities, not only different state paths.
- Wrong live V/K/config/fixture identity, stale run or dead lease fails before
  the first fixture call; local and external descriptors enforce identical
  capabilities and source proof. Credential references do not leak into logs.
- Adapter absent/enabled packaging, source-pin provenance, correct registered
  state inventory, wrong workspace/session, lifecycle journal refusal, busy
  capture, stale generation after lock wait, incompatible candidate/provider
  removal and supported compatible adoption. Existing provider contracts and
  maintenance holds remain unchanged. Use isolated contract fixtures, not live
  package transitions or session records.

After quick checks and commits, inventory both complete branch histories and
final diffs, including original inherited K network-pin work and v2 legacy
handling. Obtain mandatory independent final review of the completed runtime
and adapter before long checks. Delegate uncertain/long runs to a fresh watcher.
Then run extension `nix flake check --print-build-logs` and the applicable
`nix run .#devcluster-check` package/runner smoke coverage, extending the latter
only for the optional provider. A migration VM is needed only if implementation
actually changes its owning migration/host-state contract; do not broaden this
task into namespace migration.

On an explicitly authorized isolated host/environment, long acceptance uses
owned new resources to prove real two-instance isolation, safe interruption and
capture/lifecycle exclusion. Do not activate a workspace package merely to make
that test run. If managed runtime proof requires activation, record that exact
prerequisite and prepare the separate reviewed operation for the lead. Preserve
the stop-on-unexpected-kernel-build rule and genuine resource-capacity limits.

Provide a concrete standalone test route in K: a new external-test-framework
suite such as `runtime/standalone`, using K's existing pinned
`vpsadminos.lib.testFramework` outputs and a disposable NixOS test machine.
Install only K's packaged engine/capture tools and their declared dependencies
in that machine, with fresh user state and no dev-workspace package, registry,
session variables or workspace filesystem mounts. Run from a temporary ordinary
directory. Fast host-side tests can use fake OSVM processes; this isolated test
machine proves the installed standalone path. The post-review real-cluster case
requires working nested KVM and enough genuine guest/host RAM and shared memory
for the selected clusters plus the outer machine. Use the existing pinned kernel
closure from cache; neither nested KVM nor capacity may be assumed or overridden.
If those prerequisites cannot be met, report them and use a separately assigned
standalone KVM host for that case. Do not substitute execution through the
current managed host's private helpers. Define isolated mock adapter/generation
tests separately; they do not claim that the current host's provider is activated.

The screenshot acceptance remains only `networking/ip-address-list` in Czech
and English at exact V `5d5527a67315c18b595345aa6996d7724c1ed071`, selected through
the existing scenario/checkpoint interface with its real fixture prerequisites.
After approved runtime launch, use `bin/capture`, inspect both PNGs, then
`bin/validate --update` and `bin/check`; preserve semantic media IDs. Generated
PNG/manifest changes receive their owning checks and review before publication
readiness. Carry only the approved generated evidence back to the original K
feature branch through a lead-controlled step; its V pin must not move. Never
hand-edit PNGs, weaken source/fixture assertions, upload production media or
clean another instance. Source completion and a handoff leave this session open.

### Portable capture source and artifact roots (2026-10-07 clarification)

The standalone package includes a named capture executable as well as the engine;
installing capture tools in the store must work from an ordinary writable
directory. Keep one capture implementation. `sourceRoot` is the immutable source
selected by that executable, containing its lock, original inventory, scenarios,
fixtures and supporting code. `outputRoot` is independent writable storage.
Add `--output-root DIR` to capture and validation. The checkout entrypoints retain
their existing default of the owning checkout root, including when invoked from
another directory. The packaged entrypoints default to the invocation's CWD.
The wrapper selects this default explicitly; do not detect a workspace, infer
source from CWD, or silently choose another directory when a write is refused.
Resolve an explicit relative output directory against invocation CWD and report
the resolved source/output roots before work. Refuse an unwritable/store output
before connecting or preparing fixtures.

Package `capture` supplies `vpsfree-kb-capture` and its matching
`vpsfree-kb-validate`; checkout `bin/capture` and `bin/validate` call the same
respective implementations. The packaged source is fixed by the K package, not
by any descriptor or output-root option. Source modules, the lock, scenario
selection, fixture definitions and `lib/rest-client-proxy.rb` are always read
from `sourceRoot`. There is no capture `--source-root` override. An external
connection must still prove the expected exact source and V pin before fixtures.

Write PNGs only to `outputRoot/<canonical asset.output>`. Require normalized
relative manifest paths below the expected screenshots tree and reject path
escapes or unsafe output symlinks. Resolve review/overwrite policy against the
source inventory and any validated candidate, so an empty alternate output
directory cannot bypass protection of reviewed/uploaded source assets. Keep the
existing semantic IDs, CS/EN paths, selectors, masking and crop behavior.

All other mutable capture consumers receive explicit artifact or temporary
paths: `CaptureSession`, `fixtures/prepare.cjs` (`fixtures.json`),
`lib/terminal.cjs` (CLI home and traffic transcript), scenario callers, and any
browser downloads/traces added by the implementation. Use a private invocation
directory beneath `outputRoot/tmp/` for credentials, CLI state and transient
files; do not reuse another run's CLI authentication. Read code from source
while writing transient data to that invocation directory. Contact-sheet output,
if used with an artifact root, also belongs there. No helper may reinterpret an
artifact directory as a source checkout or write beneath `__dirname` merely
because the entrypoint is installed there.

Serialize captures/validation updating the same output root with a separate
artifact lock. Acquire it before the cluster capture lease, with no reverse
acquisition path. Keep `outputRoot/tmp/capture-results.json` as the existing
result-array interface, but atomically merge successful runs by `(language,id)`
instead of replacing the entire array. CS followed by EN therefore retains both
results and permits the documented single `validate --update` afterward. Replace
only successfully recaptured matching keys; preserve other successful results
with the same bound source contract. Retained entries must still match their
files' hashes. Reject duplicates, unsupported old transient data and mixed source
receipts instead of silently importing or deleting them. Publish result metadata
only after all selected checkpoints and their files validate; failed capture
must not certify partial output. Stage replacement PNGs in the invocation
directory, and fail subsequent validation if interruption leaves a mismatched
file/result pair.

Record a small source receipt alongside results: schema, source K revision/store
identity, input-lock digest, original inventory digest, normalized capture
contract digest and exact V revision. The contract digest covers immutable asset
IDs, language/output paths, scenario/checkpoint/driver, fixture requirements,
viewport/masking and page/media bindings; observed dimensions, PNG hashes and
generated capture provenance are excluded. Each result retains its verified
cluster instance/run provenance. Sequential languages may use different proven
cluster runs but must have the same source/contract identity. Validation's own
generated metadata update must not invalidate a still-matching source contract;
retain the original receipt and compare the candidate's immutable fields rather
than silently rebasing source identity onto the candidate manifest.

With a separate output root, `validate --update` starts from the source inventory
or an already validated candidate and writes only `outputRoot/captures.json`.
Validate candidate immutable fields against the source contract, every supplied
result's identity/provenance/hash, and existing review restrictions before an
atomic candidate write. For unchanged inventory entries, read the original PNG
from `sourceRoot` when no artifact override exists; changed entries require their
artifact and matching result. Strict validation still checks the full inventory,
not merely the two selected files. In checkout mode source/output roots coincide
and existing `bin/validate --update` behavior remains. `bin/check` may forward an
explicit `--output-root` to this final validation while its source-contract
checks continue reading the selected source; its default behavior is unchanged.
Do not add `--allow-missing`, weaken provenance, or silently replace source
inventory to make a partial artifact bundle pass.

Focused tests cover read-only store-like source with writable CWD/explicit output,
checkout defaults from another CWD, all identified mutable consumers, CS then EN
plus one validation update, safe recapture, interrupted publication, mixed/stale
source results, protected assets, candidate contract drift and path confinement.
The isolated standalone test installs the named capture package, exercises this
layout with no workspace checkout, and proves no source/store write occurred.
After visual review, the lead carries back only the two exact generated PNGs and
their validated inventory/provenance changes, preserving all other entries and
the exact V pin. Run the owning checkout's ordinary strict validation and check
after carryback. CLI homes, credentials, raw transcripts and result scratch files
are not committed or included in the carryback.

### Immutable-source update by owned restart (2026-10-07 clarification)

`update` replaces the complete running K cluster and runner through a controlled
restart. It does not hot-switch guest closures beneath the previous runner or
relabel that runner with new provenance. Preserve the instance ID, retained
disks, credential material and every original launch receipt/result root. The
replacement has a fresh run ID and one new immutable source/config/runner
receipt. Existing capture descriptors become stale and must be obtained again.
This is a disposable development-cluster outage, not a rolling service update.
Reject old per-machine update targets; supporting mixed-source partial updates
is outside this contract.

Before changing readiness, claims, active config, credentials, phase or disks,
validate the replacement's committed immutable source/lock identities and the
complete requested config. Include topology, machine/spin/disk compatibility,
endpoint/resource syntax and credential/certificate compatibility. Evaluate the
replacement configuration sufficiently to reject an invalid Nix/config shape
before stopping; private candidate staging is separate from live instance state.
Do not merge replacement defaults into the active config as a validation step.
Revalidate the selected instance/run after taking the gate. Invalid replacement
config/source leaves the running instance and its descriptor unchanged. A later
closure build, download or boot failure is a distinct operational failure and
may leave the instance stopped; do not promise that preflight proves build or
boot success.

In the current draft, `State#transaction` takes the gate then operation lock and
both `Engine#start` and `Engine#stop` call it. Implement `Engine#update` with one
outer transaction and private `start_locked`/`stop_locked` operations requiring
that already-held context. Public start/stop take the transaction and delegate
to the same internals. Do not invoke the public methods, spawn another CLI or
open/flock the same lock again from update. Preserve the existing outer adapter
generation/session order. Keep the gate across invalidation, stop, build, start
and verification; VM children inherit neither gate nor operation/generation
locks. The old runner's separate liveness lock must be released before spawning
the replacement. No new global lock registry is needed.

After successful preflight, atomically record an update operation binding its
operation ID, instance, old run, planned new run and candidate source/config
digest. Mark the instance non-ready before requesting graceful shutdown through
the proven old runner's control channel. Use its original receipt to prove
ownership; the replacement source must not redefine the old process tuple.
Wait for the old runner and all recorded children to be gone before touching
their sockets or allowing a replacement process. If stop fails or ownership is
ambiguous, retain processes, claims, sockets and roots, report non-ready and
do not build/start a competing run.

Once old-process exit is proven, normal owned stop cleanup may release that
run's resource claims and remove its known socket files. Preserve its disks,
credentials, source/config/launch evidence and all original result roots.
Claim replacement resources using the normal all-or-nothing reservation path;
a competing instance can claim released resources during the outage, in which
case update fails stopped without stealing them. Do not introduce a resource
handoff allocator to hide this possibility. Build the replacement config and
runner from the same new immutable K source, using run-specific staging/config
paths and roots so older receipts still resolve to their original inputs.

Persist stages for stopped, reserved/building, built, starting and verifying
before their corresponding effects. Record the spawn handoff so interruption
cannot turn an unrecorded live replacement into a presumed absent run. A failed
build retains its candidate evidence and any owned claims; no stale build result
may be launched as fallback. A failed spawn/readiness/attestation remains
non-ready with the exact new-run identity; retain claims until absence/exit of
its processes is proven. Publish the new active descriptor and ready phase only
after runner, all required guest closures, source/fixture identities and normal
cluster readiness/refresh satisfy the new receipt. Historical ready records do
not make an updating/failed instance ready.

Retry resumes the same recorded candidate and distinguishes pre-spawn from live
or incompletely stopped replacement state; it must not create a second runner.
A different candidate requires explicit resolution of the retained update.
Never automatically reboot the old source, reset disks, rotate credentials or
adopt legacy state. The new guest may already have changed application data, so
keeping old closures is recovery evidence, not proof that software downgrade is
safe. Supported updates are between compatible portable-v2 state/runner/disk
contracts, with the same machine and retained-disk layout and compatible
credentials. Reject unsupported format, machine/disk layout or TLS identity
changes before stopping; a separately designed path is needed to support them.
The boot path must actually use the new expected toplevel while preserving disk
data. Retaining an old root disk does not itself prove a new source booted, and
replacing that root disk to make verification pass violates this update contract.

Add focused fake-runner tests for one gate acquisition, capture/update exclusion,
unchanged live state on invalid candidate, stop timeout/foreign ownership,
reservation/build/spawn/readiness failures, interrupted retry without double
spawn, and stale descriptor refusal. Assert every old receipt/root and credential
survives and no reset or legacy adoption occurs. After committed final review,
the isolated real-runtime test writes a sentinel on each retained data/root disk,
updates to a compatible distinct immutable K source, and proves the same instance,
disk data and credentials with a fresh runner/run and genuinely new source/guest
closure evidence. This clarification authorizes no test or runtime action now.

### Local multicast resource identity (2026-10-07 clarification)

Correct the earlier assumption that a unique run-derived socket-network label
alone isolates local inter-VM traffic. In both vpsAdminOS
`6bdf458fd9105379860234ff33d352e55844f08f` and
`8e44a5124439b1f3048ffc56b1717614a5360358`,
`osvm/lib/osvm/machine_config.rb#SocketNetwork` passes string multicast labels
through `PortReservation.get_port`; integers are used directly.
`osvm/lib/osvm/port_reservation.rb` allocates from 10000 through 30000 in a
process-local singleton, taking the first available entry. Separate runner
processes with different labels can therefore choose the same actual UDP port.

The effective K source is presently **6bdf458**, not 8e44a512: committed
`a50f8c1a` and the inspected runtime worktree lock resolve root `vpsadminos`
through `[vpsadmin,vpsadminos]` to `nodes.vpsadminos.locked.rev=6bdf458...`.
`flake.nix` explicitly overrides V's OS input to that revision. The 8e44a512
reference describes V's own test source. Both have the relevant behavior; this
fix changes neither pin and does not require an OSVM source change.

For local mode require `local.multicastPort` to be a JSON integer in 1..65535,
with an explicit documented value in the default config. Pass that integer
unchanged into every selected machine's `SocketNetwork.mcast.port`; never
stringify it or let OSVM allocate from a label. Record the effective multicast
address (currently OSVM's `230.0.0.1`) and numeric port in the launch receipt.
Keep instance/run network labels as provenance and namespace identifiers, not
as the resource reservation key.

Add the actual UDP bind/port to the same atomic resource-claim set as local TCP
forwards. Conservatively exclude another local K cluster from that UDP port on
the host, even if its instance, root, slug or multicast group differs. Distinguish
TCP from UDP in reservation keys. Probe the UDP bind without reuse flags before
launch; a busy or unverifiable port fails without killing its owner or choosing
another port. Kernel probing is a preflight, not ownership proof or a permanent
reservation against nonparticipating software. Retain the durable K claim across
probe-to-VM handoff and while any owned VM may still use the network; release only
under the existing proven-stop rules. Do not keep an exclusive probe socket open
while QEMU needs to bind it. QEMU launch failure follows normal retained-failure
handling. Operators must configure disjoint ports; no automatic retry port,
subnet allocation or fallback is introduced. Bridge configuration and behavior
remain unchanged and do not require this local-only field.

Tests must inspect the generated machine JSON and actual SocketNetwork/QEMU
arguments to prove a numeric configured UDP port reaches the runner, including
separate OSVM processes where distinct string labels would both allocate the
first port. Cover two roots/same slug with distinct ports, distinct names with
the same UDP port refusing, an occupied foreign UDP port, invalid/string/missing
local values, TCP/UDP protocol distinction, interruption/claim retention and no
bridge change. Post-review isolated runtime verification should prove traffic
stays within each local cluster, not just that socket directories differ.

### Guarded streaming provider dispatch (accepted 2026-10-07)

This supersedes the earlier two-repository/no-generic-change assumption for the
optional adapter. The third source owner is `aither64/dev-workspace`, canonical
SSH remote `git@github.com:aither64/dev-workspace.git`. The lead registered
`worktrees/2026-10-05-network-ipv4-left-counter/dev-workspace`, branch
`2026-10-05-network-ipv4-left-counter`, from freshly fetched
`e3315a483f3d3536d492ecbe40f2655449cf630f`. At that revision, as at E's prior
`6a972b9ab01077611b2c60e0fc726c185e050315` selection,
`libexec/workspace-host#dispatch_cluster` invokes `system_env!` under the current
generation guard; that helper uses `Open3.capture3`, closing input and buffering
output until exit. Catalog extensibility does not supply the full-duplex lease
transport. The help-only exec bypass and `system_env_interactive!` are not usable
lease routes.

The accepted correction is confined to normal provider dispatch: after existing
workspace-option extraction/selection, only `argv.first == 'capture-lease'`
selects a supervised streaming helper. Other commands retain `system_env!` and
their current behavior. Retain catalog resolution inside the same generation
guard, selected-workspace environment, removal of inherited transition/session
authority variables, stale-generation rejection and ordinary success/error exit
mapping. Add injectable input (default `$stdin`) beside existing output/error
sinks. No catalog, persisted schema, transition-policy or exit-status change is
needed; no provider-specific private dispatch bypass is permitted.

Use `Open3.popen3` or equivalent mediated pipes for all three directions. Only
the guarded dispatcher owns the original caller channels. The provider receives
new pipe ends, with other descriptors closed; neither it nor any VM inherits the
generation lock or original capture channels. Forward bounded chunks promptly,
flush supported output sinks and keep stdout/stderr separate. Readiness must
reach the caller while the provider waits for input. Do not buffer a complete
lease, use inherited stdio/exec, or release the generation guard after readiness.

The dispatcher holds its guard until the exact provider child is reaped on an
ordinary return. Caller EOF, broken pipes, relay errors and interruption close
provider input and end the relay; provider early exit must cancel an input pump
blocked on the caller rather than hanging the guarded dispatch. Reap only the
spawned child, with bounded cancellation escalation if required; no process-name
search or unrelated runner cleanup. Provider and capture endpoints must treat
peer loss as lease loss, cancel capture and stop admitting new fixture work.
An abrupt dispatcher death must also work without Ruby ensure handlers: kernel
closure of mediated pipe ends yields caller output EOF and provider input EOF.
No descendant may retain the dispatcher's original channels and continue a usable
lease after its generation guard vanishes. Keep K's capture/lifecycle gate until
its own lease cleanup completes; normal ownership proof still governs lifecycle
actions. Cancellation cannot undo a remote request already accepted before loss.

Protocol stdout EOF is lease loss even when the provider process remains alive;
it is not equivalent to diagnostic stderr EOF. The mediated stdout pump must
notify the supervisor, propagate protocol closure promptly to the caller, close
provider input and use the same bounded owned-child cleanup under the guard.
Do not wait for process exit to recognize or communicate that half-closed lease.
Keep stderr available for diagnostics; stderr EOF alone does not cancel a lease.
The K capture client and optional adapter must preserve this distinction too:
stdout EOF/error fails a pending handshake or aborts an acquired lease, without
waiting for a child-process close event. Intentional normal shutdown remains
distinct. Make the protocol-output closure behavior explicit for injected test
sinks as well as real pipes; this is confined to capture-lease dispatch.

Generic ownership is limited to `libexec/workspace-host`, focused tests under
`test/workspace_host/commands_and_locks_test.rb` and necessary test support, and
the provider/extension contract in `docs/workspace-portal.md`. Real-process tests
must cover readiness before child exit, input forwarding/EOF, separated stderr,
injectable sinks, early child failure/exit, broken pipes, normal interruption and
abrupt dispatcher loss. Prove no usable lease survives parent/peer loss, no lock
or original peer FD reaches the child, the generation guard spans the lease and
ordinary reaping, and a waiting command still rejects a changed generation.
Retain coverage for stripped authority variables and unchanged non-streaming
dispatch. These are focused transport/lifetime tests, not a general runner
framework or tests against a compromised host operator.

Include a provider that sends readiness, closes stdout and then blocks on stdin
while caller input remains open: protocol loss must reach the caller, provider
input must close, and the guard must cover ordinary child reaping. Cover stdout
EOF before readiness and readiness immediately followed by EOF, including the
K client's abort/assertLive behavior. A companion provider that closes only
stderr must remain leased and exchange input/output until normal peer closure.

E must pin the exact published generic feature commit containing this contract
through its normal `dev-workspace` flake input/lock, and test its public
`kb-devcluster capture-lease` composition against that exact selection. Document
this as the minimum runtime compatibility for the optional KB provider; the old
buffered runtime is unsupported for this provider, with no fallback or override
to a private executable. K remains standalone and imports no workspace runtime.
K, E and generic source quick checks precede committed final review; packaged
composition and long integration checks follow review under a fresh watcher.
Publication is feature-only. Source/pin development does not activate an
installed package, change this workspace's selected runtime, integrate a default
branch, create a PR, deploy, or mutate a cluster/session lifecycle.

### K-owned retained NixOS root driver (accepted 2026-10-07)

Use a narrow K-owned subclass of `OsVm::NixosMachine` in the K runner. At pinned
OS `6bdf458fd9105379860234ff33d352e55844f08f`, the upstream
`NixosMachine#prepare_disks` always removes and recopies the root image, while
`Machine#prepare_disks` creates only missing declared file disks. The subclass
must invoke the latter preparation for declared disks, then create a root from
the candidate image only for the proven first creation of that instance/machine.
Subsequent launches preserve the existing owned root. An expected retained root
that is missing or invalid fails; it is not silently recreated. Persist the
first-creation handoff so interruption cannot authorize replacement of a
partially created or already populated root. This changes K's lifecycle driver,
not upstream OSVM behavior or source.

Boot the candidate's direct kernel/initrd and exact `toplevel/init`, preserving
the existing disk path/layout. `Machine#qemu_boot_options` already supplies this
direct-boot mechanism. Do not fall back to the old image, bootloader or toplevel.
After boot, the existing live SSH metadata and `/run/current-system` comparison
remain mandatory before readiness. Cover initial creation, repeated preparation,
missing/foreign retained root, interrupted creation, other declared disks and
exact QEMU boot arguments in focused tests; the reviewed long test must preserve
root and data sentinels while proving the new closure actually runs.

Retaining the root alone is insufficient: `tests/configs/nixos/test-vm.nix`
disables mounting the host Nix store. The new exact init closure must first be
present in that guest's retained store. Closure population and stopped-state
compatibility are a required refinement of the update stage order, not authority
to weaken attestation, overwrite roots or start an unprepared candidate.

### Prepared boot artifact, closure transfer and cold start (accepted 2026-10-07)

This is the final draft contract for the unconsumed portable-v2 state and
connection-1 formats. It supersedes the earlier compile-time fresh-run guest
marker and the update ordering that built closures after stopping. Keep one
clean format; do not add migration, adoption or compatibility parsing for earlier
unpublished drafts. K owns the artifact/guest/connection contract; E binds its
managed lease to that same contract. No OS source change is required.

**Artifact and run identities.** A prepared `artifact_id` is an immutable UUID
for one instance's exact source/configuration and boot artifacts. It is distinct
from `run_id`, which changes for each runner start. Guest metadata at
`/etc/vpsfree-kb-capture.json` contains `schema: 1`, `instance_id`, `artifact_id`,
the existing exact source/lock/input/fixture metadata, and `config_input_sha256`.
It contains no live runner `run_id`. The input digest covers the canonical
validated requested configuration, topology/network and relevant explicit build
inputs; do not put the resulting machine-config/toplevel digest into its own
guest build input and create a derivation cycle.

An immutable artifact receipt records that guest metadata, exact input digest,
source, topology/network/machine/disk layout, compatible credential identities,
built machine-config path/hash, exact runner executable, per-machine kernel,
initrd/toplevel (and OS squashfs), and host result roots. A separate preparation
journal binds each retained root to its initial image-creation proof or imported
candidate closure/root proof. Keep the receipt and preparation evidence rather
than changing an old artifact to describe a newer source. Root candidate host
closures and runner outputs before relying on them; preserve every earlier root
and receipt under the existing reset-only removal contract.

Each reservation/launch/process/readiness record binds fresh `run_id` to
`artifact_id` and the immutable artifact-receipt digest, in addition to its
existing instance, process, socket and resource identities. No per-start UUID
may affect Nix guest/toplevel derivation when resuming an unchanged artifact.
Actual local multicast is the configured integer; run-derived namespace labels
and socket paths remain runtime receipt fields. Preserve the instance's disks
and credentials. Connection-1 and lease-readiness records include `artifact_id`
and `artifact_sha256` alongside instance/run IDs and descriptor digest, and carry
or bind the exact artifact provenance. Capture results retain both identities.

Live attestation proves both (a) the current owned runner/process/readiness and
held lease for this run and artifact, and (b) trusted SSH guest metadata plus
actual `/run/current-system` matching that exact prepared artifact. Guest
metadata alone cannot prove the current runner, and a new runner cannot make an
old guest artifact appear newly built. Update `Software#build`/build environment,
runner receipts, `Engine#verify_live`, descriptor/lease validation and
`lib/connection.cjs` together; remove the draft assertion equating guest run ID
with descriptor run ID. Missing artifact fields refuse rather than falling back
to the earlier draft shape.

**Commands.** The final v2 command contract is `start` for fresh creation, `stop`
for owned shutdown, `resume SLUG` for cold continuation, and `update` for changed
source/config or its recorded retry. This intentionally replaces the old helper's
implicit stop/start reuse: after stopping, use `resume`, not a silently new start.
A fresh `start` prepares an artifact and creates each root once; it does not
recreate or resume retained stopped state. After a proven stop, `resume` uses the
latest accepted
prepared artifact with a fresh run ID and new resource/socket reservations. It
uses the recorded runner/config/closures, without rebuilding a run-specific
guest. The selected committed K source must match that artifact. Resume reads
its exact recorded config/topology/network and accepts no replacement config or
source; do not merge current defaults into retained config or silently
choose another artifact. Require compatible state/disk/credential identities,
complete preparation evidence and no unresolved update. Missing roots or
artifacts refuse, and postboot proof is mandatory even on an ordinary restart.

Changed source/config requires `update`: prepare through the reachable attested
old guest, or resume the same update's already complete prepared candidate.
An offline, unprepared candidate refuses. While an update journal exists,
`resume` refuses and `start` cannot choose the previous artifact as rollback;
retry the same `update` operation. Update retry may reuse completed preparation and, after
proving any prior attempt gone, create a fresh runner attempt bound to the same
candidate artifact. Persist that attempt before spawn and reconcile any ambiguous
handoff before another attempt. Once candidate boot/readiness succeeds, accept
the candidate artifact for later stop/resume. No automatic old-source
boot, image replacement or old-closure substitution is a recovery path.

**Exact closure preparation.** Source evidence supports a bounded SSH copy:
K `a50f8c1a:bin/devcluster:1121` already calls `NIX_SSHOPTS` plus
`nix copy --to ssh://root@HOST TOPLEVEL`; retain this recursive-copy primitive,
not the following hot activation. K's effective locked nixpkgs is
`5dfba6236110080a54247d6460bc2ff5dda939cc`.
Its `nixos/modules/services/system/nix-daemon.nix` enables Nix by default and
installs its package; `nixos/lib/make-disk-image.nix` copies/registers the initial
system closure. K's SSH module supplies its dedicated root key. These are source
contracts, not evidence that a particular live guest has been checked.

Within the single held gate/operation context, validate replacement source,
config, compatible disks and credentials before changing live readiness. Verify
the old run and its SSH source proof, then journal a candidate operation and mark
non-ready. Build and root the candidate config, runner and exact guest closures
before stopping anything. Candidate build failure leaves the old processes,
claims and source identity in place, with a resumable non-ready operation.

For every retained NixOS machine, use the OLD run's explicit endpoint/port, key
and pinned known-hosts file. Require working guest Nix store tools and root store
access; missing tooling is a compatibility failure, not permission to install a
different toolchain or use an unverified SSH route. Clear inherited SSH/Nix
destination/source overrides and construct options as argv or safely quoted
`NIX_SSHOPTS`; never infer a destination from the new candidate's changed network
configuration. Check available guest store bytes/inodes against the missing
recursive candidate closure and a documented conservative filesystem reserve.
Treat the estimate as preflight only: ENOSPC or another import failure still
fails safely. No automatic guest GC, disk growth, host-store mount or offline
privileged root manipulation is permitted.

Copy only the exact built candidate toplevel and its recursive references,
without guest builds/substitution fallback, profile changes, activation or
`switch-to-configuration`. Query the complete host reference/path/content
identity set, compare it with registered remote references and verify their
contents. A toplevel pathname or successful SSH exit alone is insufficient.
Install an exact per-instance/artifact guest GC root, such as
`/nix/var/nix/gcroots/vpsfree-kb/INSTANCE/ARTIFACT/MACHINE`, and verify it and the
complete closure again. Retain per-machine completion proof tied to the old run,
artifact and root identity. Confirm the running guest still reports the OLD
metadata/current-system; adding store paths never relabels or activates it.
Only after all retained NixOS guests pass may the controller request the proven
old runner's graceful stop. vpsAdminOS nodes use the candidate read-only squashfs
boot media and retained declared data disks, without this NixOS-root import.

Partial import, dropped SSH, content mismatch, GC-root failure or disk exhaustion
leaves the old runner/disks/claims intact and the update non-ready with exact
progress. Retry the same candidate idempotently, rechecking remote completeness;
do not delete valid imported paths or reset another machine to hide partial work.
After complete preparation, proven shutdown and resource reservation, direct
boot the candidate through the K-owned root-preserving driver. Existing spawn,
ownership, readiness and live-source failure handling remains in force. Retain
original receipts/roots and credentials on every failure. A complete import
receipt permits retry after stopping; it does not waive postboot live attestation
or certify an application-data downgrade.

**Verification.** Focused tests cover unchanged stop/resume with a fresh run and
the same artifact/toplevel; no rebuild or root copy on resume; mismatched offline
source/config; missing/corrupt roots or preparation evidence; pending-update
resume refusal and start-on-retained-state refusal; old-run versus artifact
confusion in descriptors and guests;
stale lease IDs; candidate-build failure; wrong SSH/source before import; missing
guest Nix/store access; incomplete closure/content mismatch; insufficient space
and mid-copy ENOSPC; second-machine failure; missing GC root; interruption before
and after stop; and same-candidate retry without double spawn or fallback.
After final committed review, the isolated real-runtime test must perform
ordinary stop/resume and a compatible changed-source update, retain root/data
sentinel contents and credentials, prove fresh live run IDs with truthful stable
or changed artifacts respectively, and verify actual new guest closures. Keep
the accepted two-language screenshot source pin and capture assertions intact.

### Managed descriptor digest and cleanup inventory (2026-10-07 clarification)

Keep K's canonical descriptor and lease protocol unchanged. In the inspected
draft, `Engine#connection` returns stored `connection.json` bytes;
`Engine#capture_lease` checks their exact SHA-256, verifies the live source and
emits that digest in readiness. Replacing its private `control.argv` with E's
public route changes those bytes. Passing the managed digest straight to K fails;
passing the canonical digest through to capture fails the caller's expected
readiness. E therefore owns one narrow supervised descriptor-digest translation.
A new portable K controller-export option is unnecessary for this integration
and would expand K's persisted/export API. Do not change K to accept arbitrary
alternate digests, trust an `owned` flag or bypass canonical validation.

Under its existing managed binding and ordered guards, E obtains the exact K
canonical descriptor bytes and validates their instance/run/artifact, receipt,
source and explicit endpoints against the managed instance and selected engine.
It derives a separate mode-0600 managed descriptor using deterministic encoding,
changing only `control.argv` to the stable public `kb-devcluster capture-lease`
route with explicit workspace/session selection. All provenance, credential
references, endpoint mappings and capabilities remain identical. Never overwrite
K's `connection.json`. Let C be the digest of exact canonical bytes and M the
digest of exact managed bytes. E may derive this mapping on demand; a second
mutable ownership database is unnecessary.

On managed lease acquisition, revalidate the binding and current canonical
descriptor, deterministically derive the expected managed bytes, and require
the caller's descriptor digest to equal M. Stale or altered managed descriptors
refuse before readiness. Spawn only the selected pinned K engine's lease command
for that verified root/slug with the exact instance/run/artifact/digest and C;
do not execute a caller-supplied private controller or substitute metadata. K's
locked canonical check closes the race if its descriptor changes before gate
acquisition. E does not emit readiness until it has received and validated the
complete, bounded single K readiness record: schema, instance, run, artifact,
artifact digest and C must all equal the expected values. Source/endpoint truth
remains bound by C, the validated full canonical descriptor and K's live proof.
Emit one otherwise identical readiness record with only `descriptor_sha256`
translated from C to M, then flush. No other field is translated.

The E process supervises that exact K child through mediated stdin/stdout/stderr
for the whole lease, inside the existing public dispatch generation/session
guards and adapter lock. It keeps K stdin open while the capture peer lives,
forwards diagnostics separately, and never hands original caller or authority
descriptors to K/VM children. Peer EOF/error, K protocol stdout EOF/error,
unexpected extra protocol output or child failure closes the lease path and
performs bounded owned-child cleanup. Stderr EOF alone is harmless. K loss
before readiness emits no managed readiness. Record protocol loss independently
of parsing so readiness and EOF observed in the same scheduling window cannot
leave a live managed lease: known loss prevents readiness publication; loss just
after publication immediately closes protocol output and aborts the caller.
Do not buffer until child exit, introduce a grace period that treats a lost
protocol as live, or claim to prevent requests already accepted before loss.
Adapter/dispatcher death relies on kernel pipe closure as well as normal cleanup;
the runner never inherits the outer guards. This is a translation in E's existing
provider, not a second launcher or private route around public dispatch.

The generic cleanup-paths protocol has a different meaning from K's command.
At D `9b5bb4d61413e1de7702f45b50ef3229d2b93244`,
`dev-session#prepare_removal!` calls `validate_removal_recovery_location!`, then
`development_cluster_cleanup_paths`, before `release_development_clusters!`
later calls provider `reset`. The paths exclude overlap with deletion recovery
storage; listing is not a deletion operation. K's draft `cleanup-paths` requires
stopped state and proven process exit, so E must not blindly pass it through.

E `cleanup-paths SLUG` is a read-only positive inventory of the verified managed
instance: validate canonical workspace/provider/session binding, K schema and
owner/instance/root identity, then return `{schema: 1, paths: [...]}` containing
its managed instance tree, any separately owned adapter record tree and exact
recorded socket namespaces for relevant retained/current/pending run receipts.
Use the selected engine's identity/receipt validation and recorded namespace
contract; do not guess slug-only sockets or include a shared state/lock/resource
registry parent. Running state is permitted for this inventory. It neither
requires nor claims that processes have exited. Malformed, foreign or ambiguous
state refuses; a genuinely absent instance with no residual binding/state can
return an empty list. Listing must not create records/locks, repair ownership,
stop processes or remove anything.

The generic deletion caller already holds its session slug lock and passes no
inherited lifecycle-lock descriptor to this early inventory call. Do not attempt
to reacquire that session mutation lock. Use bounded, noncreating adapter/K
record-read locking; return the existing busy/refusal result when a consistent
snapshot is unavailable. Actual provider reset is a separate lifecycle-authorized
operation with the existing inherited-lock validation and normal K gates and
positive stop/exit/reset proofs. An inventory response never authorizes reset of
a live or foreign instance, direct path deletion, or bypass of capture exclusion.
No generic lifecycle/schema change is needed for this translation.

Focused E tests cover exact C-to-M mapping through the stable public route,
rejection of arbitrary/stale M and changed C/binding/source/artifact, malformed or
extra canonical readiness, byte-digest fidelity, before-ready and same-window
stdout loss, stderr-only closure, peer/adapter/dispatcher loss and guarded child
reaping. Assert no unvalidated readiness or fixture access and no raw canonical
digest leaks into managed readiness. Cleanup tests cover running/stopped/pending
positive inventory, absent/foreign/partial state, exact recorded sockets,
noncreating busy reads, the generic inventory-before-reset order without slug
lock recursion, and unchanged K reset proof/capture gates. K's standalone
descriptor semantics remain unchanged. Source quick checks and final committed
review still precede long composition/runtime tests; no activation or lifecycle
operation is authorized by this design clarification.

### Standalone verification inputs and capacity (2026-10-07 refinement)

This is an accepted verification correction, not a claim that the real runtime
has passed. It changes K's existing standalone fixture, source receipt plumbing
and evidence export only. Preserve passing launcher/application behavior. The
exact K commit is assigned after these changes and quick checks; use that same
reviewed immutable revision for its engine, capture, validator and test profile.
The required vpsAdmin input remains
`5d5527a67315c18b595345aa6996d7724c1ed071`; K's effective OS input remains
`6bdf458fd9105379860234ff33d352e55844f08f`, with its existing input graph intact.
No installed workspace/provider or package activation is a prerequisite.

**Carry the original source receipt through test evaluation.** In the inspected
K draft, `flake.nix` creates `sourceMetadata` with `self.rev or ""` and gives the
OS runner `TEST_RUNNER_REPO_ROOT = self.outPath`. At OS `6bdf458`,
`test-runner/lib/test-runner/repository_source.rb` and
`test-runner/nix/resolve-repository-source.nix` preserve/root the source path,
not its Git flake metadata. `test-runner/nix/evaluate-tests.nix` then calls
`builtins.getFlake` on that path. The resulting package evaluation cannot depend
on `self.rev` surviving. `KbRuntime::Software` correctly requires a 40-hex
revision; keep that requirement. This is a source-derived defect mechanism,
without an evaluation or runtime reproduction by the architect.

Use the existing public `--test-config` route and K's existing
`lib.testFramework.mkTests`/`mkTestsMeta` boundary. Add one K-owned generated
`standalone-test-config` package output, constructed during the original exact
Git-flake evaluation. Its immutable Nix value carries one `kbStandalone` record:
schema 1, original `self.rev`, original `self.outPath`, lock SHA-256,
`sourceMetadata`, `runtimePackage`, and `capturePackage`. These are captured
store references from that same evaluation, not packages reconstructed from an
unversioned path. Creating this profile requires a genuine clean Git-flake
revision; absent/dirty/invalid revision must fail instead of producing an empty
or guessed receipt. Do not add a checked-in revision constant, ambient revision
environment variable, alternate input graph, or synthetic Git history.

K's test-framework wrapper consumes that record before supplying the standalone
suite arguments. Require its source to equal the re-evaluated immutable test
source, its revision to be 40 hex, and its lock/metadata identities to agree with
that source. Preserve the existing full locked-input and fixture validation in
`Software`. Pass the captured packages and original source into the suite;
never select source code from the writable artifact root or the invocation CWD.
The explicit profile is the supported packaged standalone test route. An
unversioned invocation without it must refuse with a useful prerequisite error,
not relax source validation; unrelated KB suites retain their existing route.
No OS test-runner, generic runtime or E change is needed for this correction.
Check receipt mismatch, missing revision, wrong source/lock and normal path
re-evaluation before VM startup. In real cases compare initial live descriptor
source to this exact expected receipt, then retain the existing guest/closure
proof. The update fixture intentionally creates and records its separate genuine
committed candidate with the same locked inputs.

**Give the isolated machine real writable capacity.** The draft
`tests/suite/runtime/standalone.nix` declares a 32 GiB, eight-vCPU outer NixOS VM
and 24 GiB guest `/dev/shm`, but no writable disk headroom. OS `6bdf458`
`tests/make-test.nix` defaults its NixOS image to `diskSize = "auto"` and
`additionalSpace = "512M"`; that cannot support nested image builds and disks.
Set this test-owned outer root to 128 GiB (`machine.diskSize = 131072`, MiB in
the pinned `nixos/lib/make-disk-image.nix` contract). Require at least 96 GiB
free there at fresh test setup before nested builds. `/nix/store`, inner state,
data images, candidate source and artifact output remain on that disposable
root, with no writable host-store/workspace mount. Refuse insufficient space;
do not resize a running/foreign disk, run GC to force a pass or reduce fixture
assertions. Sparse 320 GiB node tank files are logical capacity, not promised
physical headroom: these cases write only their bounded fixtures/sentinels.

For one outer run, reserve a conservative host disk budget of two 128 GiB images
(built source image plus writable copy), at least 16 GiB remaining headroom,
and the separately measured uncached closure/build working space. Thus 272 GiB
free is a lower planning floor before adding those uncached costs, not a proven
sufficient total or a statement about current host capacity. Count available
space on each actual filesystem; sparse/reflink savings may reduce use but are
not a prerequisite assumption. Preserve ownership of all test state/evidence.

OSVM's shared filesystem backend allocates outer guest memory from host
`/dev/shm`; the suite requests 32768 MiB of both host RAM and shared memory.
OS `test-runner/lib/test-runner/resource_pool.rb` defaults to an additional
8192 MiB reserve for each. Plan for at least 40 GiB genuinely available host RAM
and 40 GiB free host `/dev/shm` for admission, plus CPU/build headroom. Do not
override capacity detection, reserve or overcommit to bypass this requirement.
Inside the outer VM, the unchanged cases require:

| Case | Inner guest RAM | Existing preflight: available RAM / free shm |
| --- | --- | --- |
| `two-instances` | 16 GiB (two services + two nodes) | 20 / 18 GiB |
| `resume-update` | 8 GiB (services + node) | 12 / 10 GiB |
| `bilingual-capture` | 14 GiB (services + two nodes + backuper) | 22 / 20 GiB |

Inner allocations consume the outer 32 GiB; do not add them again as separate
host VMs. Host KVM and nested virtualization must be supported and exposed to
the outer guest. Opening `/dev/kvm` and `KVM_GET_API_VERSION` are prerequisites;
only the successful inner boots prove this execution path. No CPU-emulation
fallback or host virtualization reconfiguration is authorized by this brief.

The isolated VM has no dedicated host bridge, so its explicit local networking
is justified independently of normal bridge defaults. Keep disjoint declared
TCP/UDP ports. Set fixture resolver mode `cluster` with upstream
`10.0.2.3`, and replace every `domains` and `tmpDomains` value with distinct
`example.test` names. K `cluster/nix/test.nix:1256` defines that QEMU user-network
DNS address; its cluster dnsmasq uses `resolver.upstreamNameservers` while
preserving internal host records. Disabling optional DNS-server guests alone
does not remove the draft's private upstream resolvers or host-specific domains.

Configure the isolated outer builder to use the pinned OS cache in addition to
the normal NixOS cache. OS `6bdf458` `README.md:123` supplies the exact pair:
`https://cache.vpsadminos.org` and
`cache.vpsadminos.org:wpIJlNZQIhS+0gFf1U3MC9sLZdLW3sh5qakOWGDoDrE=`.
The K lock selects Nixpkgs `5dfba6236110080a54247d6460bc2ff5dda939cc`;
preserve it and the pinned kernels. This source evidence identifies the cache
contract, not current cache availability. Host and nested builds both need
reachable substitutes. Do not turn the README's optional fallback into approval
for an unexpected local kernel build: the watcher must stop only its owned run
and escalate the miss under the workspace verification policy.

**Run and retain exact evidence.** Quick checks, immutable-source/profile
evaluation checks, completed commits and independent final review precede all
long runs. A fresh policy watcher runs each selector in a distinct invocation
with a new owned runner state directory, `--jobs 1`, the same immutable profile
and unmodified resource accounting:

```sh
nix build --no-link --print-out-paths "$K_REF#standalone-test-config"
nix run "$K_REF#test-runner" -- test --jobs 1 --state-dir "$TEST_STATE" \
  --test-config "$PROFILE" 'runtime/standalone#installed-layout'
```

These are command templates: `K_REF` is a reviewed exact Git-flake reference
with the full K commit, `PROFILE` is the first command's immutable output, and
`TEST_STATE` is fresh test-owned state. Repeat the second form separately for
`runtime/standalone#two-instances`, `runtime/standalone#resume-update` and
`runtime/standalone#bilingual-capture`, each with a distinct state path. Never
replace the exact revision with a branch or use the mutable checkout as proof.
The separate invocations also avoid sharing the draft's unconditional
`/tmp/kb-ordinary` setup between scripts: OS `TestEvaluator#run_script` clones
the Ruby context while retaining the same machine objects within one run.

Tighten the existing scenarios within their accepted scope. The bilingual case
must successfully capture CS then EN into one explicit writable output root
different from CWD, validate there with the same packaged validator (`--update`
then strict), and retain exactly the two `networking/ip-address-list` results.
Keep `installed-layout`'s CWD default/error-path observations labelled as such.
In resume/update compare all six dedicated credential identities already named
by `Software.credentials_identity`: SSH private/public keys, CA certificate/key,
and server certificate/key. Compare hashes internally without exposing contents;
retain root/tank sentinels, disk inode/size, fresh run IDs, same-artifact resume,
changed committed candidate artifact and actual live closure assertions. These
checks are targeted proof of the existing contract, not an activation test.

Export evidence before the destructive outer-VM cleanup. Reuse OSVM
`Machine#pull_file` and the existing `after_test_script_run` extension hook to
copy an allowlisted successful bundle into the runner's durable
`state_dir/artifacts`, outside the machine's removable shared directory:
the CS/EN `screenshots/*/networking/ip-address-list.png`, candidate
`captures.json`, merged `tmp/capture-results.json`, and `tmp/capture-source.json`.
Preserve relative names and verify their hashes. No connection descriptor,
credential, CLI home, cluster journal or raw transcript belongs in that bundle.
Do not add a new transfer protocol or retain an entire VM merely for screenshots.
Root then runs the owning immutable packaged validator on the bundle, the
canonical K `bin/validate`/`bin/check` at the matching source/output boundary,
and visual review of both full PNGs, labels, crop, fonts and fixture data.
Carry back only the two approved PNGs and required inventory/provenance;
original feature pins and semantic screenshot names remain unchanged.

### Pinned E snapshot validation boundary (2026-10-07 clarification)

E may reuse the exact selected K source's Ruby validators as narrow integration
glue, as proposed in `dev-clusters/kb/lib/portable.rb`. This avoids copying K's
receipt rules or adding a second lifecycle interface. The adapter's executable
and imported modules must come from the same pinned K package input and source
receipt, preserving K's own input graph. No lookup through a mutable checkout,
ambient `RUBYLIB`, workspace discovery inside K or independently selected SDK is
allowed. Pin changes require the existing compatibility tests and review.

The allowed read path is construction of `State`, `Software`, `Engine` and their
nonmutating dependencies; `identity`, bounded file/JSON reads,
`phase`/`launch`/`validate_launch`, `artifact`/`validate_prepared`, recorded
namespace calculation, process identity reads (`live?`/`gone?`) and pure descriptor
construction. These draft methods validate/hash records, credentials, disks and
source without invoking lifecycle or SSH/build operations. Hold existing
noncreating `State#transaction(create: false, wait: false)` locks in the accepted
order; a busy snapshot returns busy, and absent/invalid state is not initialized.
Release that read transaction before starting the canonical child lease so it
can acquire its own gate. Outer binding/generation/adapter guards and K's final
locked descriptor validation still close the acquisition race.

Do not call `Software.checkout`/`prepare`/`build`, `Engine#verify_live`, SSH,
credential initialization, resource claim/release, state writes or lifecycle
methods through this import. All live lease acquisition and mutations use the
fixed pinned executable through the accepted public supervised provider route.
Snapshot validity is neither live readiness nor permission to clean paths.
The existing managed digest translation and inventory-before-reset contract
remain unchanged. Focused E tests must prove noncreating reads/busy behavior,
exact pin/receipt agreement, no mutating/SSH/build calls from the snapshot path,
and unchanged full lease/loss/cleanup ordering. Source/package composition tests
can exercise this boundary without activating the host workspace package;
installed generation/catalog activation and real managed capture remain separate
reviewed operations, with no success claim inferred from standalone K tests.

The managed binding's `engine_revision` is immutable creation provenance. Keep
that original value across a compatible selected-engine transition; the selected
package supplies the current exact, mutually matching validator and executable.
`transition-adopt` proves that engine can understand the existing owned state
and original artifact/source receipts without rewriting their history. It does
not certify capture readiness. Capture continues to require selected
`Software.metadata` to equal the prepared artifact source, followed by the
ordinary descriptor, lease and live-guest proof. An explicit K-owned update may
advance the prepared source while retaining original receipts and binding
provenance. The existing update/resume prerequisites still apply: unchanged
prepared source may resume; advancing source requires a live predecessor for
preparation or an already complete recorded candidate. No historical scan,
binding rewrite, alternate-source capture or new K API is required.

### Generic package CI baseline blocker (2026-10-07 investigation)

Completed CI run `37597668723` at D
`9fe491218e35a3250f2a72c203c2cecc3cb7ae16` failed the unchanged
`TestArchiveJournalRetryRefusesASameKindReplacementWhileWaitingForTheLock`
(`portal/internal/web/server_test.go:3602`, assertion at 3665). Retained evidence
is `kb-runtime-generic-final-ci-failure.log:1200` in this tracking directory.
The base `e3315a483f3d3536d492ecbe40f2655449cf630f` and final D revision have
the identical `portal/internal/web` Git tree
`dc0b96dec11c8acef332a4ba3cb95fcb0eb93fb0`; D's complete diff changes only the
Ruby host dispatcher/tests and portal documentation. The implicated Go logic
and test therefore predate the lease feature. No separate baseline run or
runtime reproduction was performed for this investigation.

The source supports a concrete lost-reconciliation interleaving.
`startLifecycleOperation` persists running/starting receipt A and requests the
background display refresh before its executor waits on the test-held mutation
lock. `refreshDisplaySnapshots` can read old journal A and propose a
running/prepared A with the journal timestamp. The test atomically replaces the
journal with abandoned B. A concurrent `lifecycleOperationForSlug` captures A,
reads B and proposes paused B. If the display worker commits its A progress
update first, `acceptLifecycleReconciliation` detects `current != original` and
returns nil without applying B; the synchronous caller then returns the current
A as successful fresh proof. The logged running/prepared A, complete mode, A
journal ID and nil error fit that path. This is source-supported causal analysis,
not an observed scheduler trace or a claim of an unsynchronized Go memory race.
The executor still checks journal identity after acquiring the mutation lock
(`server.go:2869`); this failure does not demonstrate execution against B.

Record this as an external baseline package-verification blocker while K/E work
continues. Do not disable checks or infer full package proof from the passing
Ruby checks or a later probabilistic green rerun. A repair needs separately
accepted generic lifecycle source scope: distinguish applied versus lost CAS,
and have the synchronous fresh-owner path re-read receipt and journal/repropose
within its existing deadline after a loss, returning coherent accepted proof
or an explicit bounded conflict/error. Background display may continue dropping
stale proposals. Preserve retry, attempt and dismissal protection; never force
a stale proposal over newer authority. The owning portal documentation requires
fresh checks for mutations, so polling away the test assertion or suppressing
the worker is not the proposed fix. Deterministic coverage should schedule the
same-A progress update between B proof and acceptance and retain the existing
archive/delete replacement and no-helper-invocation assertions.

For a later authorized diagnosis, the narrow existing-test selection from the
verified D checkout, using its declared package environment, is:

```sh
nix develop .#dev-workspace --command go -C portal test -mod=readonly \
  ./internal/web \
  -run '^TestArchiveJournalRetryRefusesASameKindReplacementWhileWaitingForTheLock$' \
  -count=100 -timeout=5m
```

This template was not executed. A fresh policy watcher owns uncertain-duration
verification. Related checks are the corresponding delete replacement test,
`TestLifecycleRetryCompareAndSwapRejectsAReplacementReceipt` and
`TestLifecycleReconciliationCannotOverwriteRetryOrResurrectDismissedReceipt`.
Any accepted repair follows normal quick checks, committed final review and
package verification; no CI rerun, package activation or lifecycle action is
authorized by this investigation.

### Accepted narrow generic reconciliation repair (2026-10-07)

Root accepted repairing the preceding baseline defect as necessary for usable
D/E package proof. This supersedes the earlier decision to retain it solely as
an external blocker. Keep D's current feature branch and preserve the published
lease commit `9fe491218e35a3250f2a72c203c2cecc3cb7ae16`; the Go repair is a
separate logical commit. K/E implementation continues independently. This is
source scope only, with no CI rerun, activation, integration or lifecycle action.

The implementation boundary is `portal/internal/web/operation_state.go` and
focused coverage in `portal/internal/web/operation_state_test.go`. Existing
archive/delete tests in `server_test.go` and attempt tests in
`lifecycle_target_test.go` remain regression tests with their assertions intact.
The existing browser lifecycle documentation already requires fresh ownership
proof; a short clarification beside that paragraph is optional if useful, not
a new state policy. No API, receipt/journal schema, persistent format, generation
policy, HTTP status contract or public testing interface changes are needed.

Change the internal `acceptLifecycleReconciliation` result to distinguish a
matched comparison from a lost comparison, for example `(applied bool, err
error)`. `false, nil` means current authority changed and no proposal was
accepted; `true, nil` means the comparison matched and the proposed receipt or
absence was accepted, including an already-equal/no-op result. A persistence
failure remains an error rather than a contention retry. Preserve the existing
whole-record, existence and absent-record revision comparisons, rollback on
persistence failure, and snapshot publication rules. Update the background
refresh caller to ignore the applied flag intentionally: stale display work
may be discarded without changing current authority.

`lifecycleOperationForSlug` keeps its existing 15-second context, shared
transition guard and current-profile validation. While that guard remains held,
the synchronous reconciliation path must retry a lost comparison by capturing
the new receipt/existence/revision, reading the journal again, and recomputing
the proposal and response-only view. Check the same context before each attempt
and after potentially slow proof, before accepting it. Never restart the timeout
on retry, cache old journal proof across attempts, or hold `operationMu` during
filesystem/target proof. Return the actual accepted proposal (or accepted
absence), not an arbitrary recapture performed after acceptance. Later receipt
changes remain protected by the existing mutation caller's own CAS. On timeout,
cancellation, invalid proof or persistence failure return the bounded explicit
error through existing handling; do not report stale A with a nil error.

Do not change admission retry/dismissal CAS, receipt/attempt checks on late
executor completion, display cache-only GETs, or the executor's post-mutation-lock
journal/evidence check. In particular, no force-write of B over another newer
receipt and no special exemption for a same-journal progress update is required.
This repair addresses reconciliation freshness; it grants no authority to run
the replacement operation.

**Deterministic coverage without a hook framework.** Existing
`operation_state_test.go` directly exercises receipt capture/acceptance and
`newLifecycleOperationStore` with temporary workspaces. Reuse those patterns.
Extract only a small unexported guarded retry-loop helper if necessary, taking
the initial `original`, `existed` and `revision` already captured by
`lifecycleOperationForSlug`. The normal caller supplies those values after its
unchanged guard/profile setup; after any loss the helper itself captures fresh
values. No configurable server callback, production test flag, filesystem
blocking trick or new transport is needed.

A direct store fixture, without launching a background worker, can deterministically
represent the worker's accepted progress write: persist running/starting A;
capture its original value/revision; retain its journal A progress proposal;
atomically publish abandoned journal B; commit the same-A running/prepared
progress update through the normal acceptance/store path; then invoke the real
retry helper with the captured starting-A values. Its first comparison must
lose even though its fresh journal proof is B. Require the call to retry and
return the persisted paused B, with B's mode/journal identity and a distinct
receipt, rather than current A or a nil-error stale result. This is a deterministic
unit of the production retry path; the existing full-server archive/delete
tests continue to exercise actual worker concurrency and forbid helper execution.
Do not suppress their worker, add eventual polling to their fresh-read assertion,
or use sleeps/large repeat counts as the regression's ordering mechanism.

Extend `TestLifecycleReconciliationCannotOverwriteRetryOrResurrectDismissedReceipt`
to assert the new lost-comparison flag for retry, dismissal and replacement
cases. Add a canceled/expired-context case proving that the retry helper returns
an explicit error without accepting a proposal or altering the stored outcome.
Verify the matched/no-op result is accepted so an unchanged journal does not
loop until deadline. These tests need only normal temporary files and existing
receipt/journal formats. Proposed new names are
`TestLifecycleFreshOwnerReconciliationRetriesProgressConflict` and
`TestLifecycleFreshOwnerReconciliationHonorsDeadline`.

Implementer-owned setup and quick checks use D's declared environment. Format
only changed Go files, then run this focused selection from the D worktree:

```sh
nix develop .#dev-workspace --command gofmt -w \
  portal/internal/web/operation_state.go portal/internal/web/operation_state_test.go
nix develop .#dev-workspace --command go -C portal test -mod=readonly \
  ./internal/web -count=1 -timeout=5m \
  -run '^(TestLifecycleFreshOwnerReconciliation.*|Test(Archive|Delete)JournalRetryRefusesASameKindReplacementWhileWaitingForTheLock|TestLifecycleRetryCompareAndSwapRejectsAReplacementReceipt|TestLifecycleReconciliationCannotOverwriteRetryOrResurrectDismissedReceipt|TestLifecycleTargetAttemptRejectsLateResultWithTheSameReceipt|TestLifecycleSnapshotGETDoesNotWaitForGenerationOrReceiptMutex|TestDisplayGenerationContentionKeepsReceiptUnchanged)$'
nix develop .#dev-workspace --command go -C portal test -mod=readonly \
  ./internal/web -count=1 -timeout=5m
```

These commands are a verification brief, not executed evidence. The existing
package environment supplies Go and the explicit readonly module mode avoids
its vendor default against a checkout without `portal/vendor`. Assign uncertain
duration to a fresh policy watcher; do not substitute ambient tools or disable
package checks. The focused and full affected-package checks precede the repair
commit and final review. All intended K/E/D source commits and quick checks,
then the planned independent four-lane final review, still precede long package
and VM verification. A final package result must cover the exact reviewed repair
head and downstream pin; the earlier Ruby results do not certify this Go change.

### Reconcile D with the upstream lifecycle fix (2026-10-07)

The root's normal commit wrapper stopped at its ancestry guard before staging:
fresh SSH default was `a2bbf2f1c588de7eec0d7d52580a89a9d4bef984`, containing
`8f0f40a04f5dcf1b590eb4cb8562bfecebe2962d` (`portal: retry lifecycle proof after
receipt contention`). This is an upstream advancement, not a source/check
failure. Read-only inspection confirms HEAD is still `9fe491...`, the index is
empty and only the two assigned Go files are modified. Root reports quick1
passed; those receipts remain evidence for their original source snapshot.

Use upstream's functional fix. It already supplies acceptance status, repeated
fresh proof within the original deadline, direct return of the accepted result,
the stale-CAS assertion and the explanatory portal paragraph. Do not publish a
second copy of that bugfix. Fresh default also includes shared workspace file
links, stable archived-fixture timestamps, lead-owned team support and concrete
new-session defaults; retain all of them. The original lease commit changes only
`libexec/workspace-host`, its Ruby tests and a different portal-documentation
section. These have no source-hunk overlap in the inspected upstream diff;
that observation does not certify a future rebase result.

**Preservation and ownership.** Root owns Git/history operations; implementer
owns restoring and reconciling application edits. Freeze the two Go files during
handoff. Before any restoration, root records branch/HEAD, exact target base,
index/status and the quick1 source-file hashes, then saves both full-index binary
patches in a new session-owned evidence directory outside the D worktree:

```sh
git diff --binary --full-index HEAD -- \
  portal/internal/web/operation_state.go \
  portal/internal/web/operation_state_test.go > "$D_SAVE/local-quick1.patch"
git diff --binary --full-index a2bbf2f1c588de7eec0d7d52580a89a9d4bef984 -- \
  portal/internal/web/operation_state.go \
  portal/internal/web/operation_state_test.go > "$D_SAVE/residual-on-a2bb.patch"
sha256sum "$D_SAVE/local-quick1.patch" "$D_SAVE/residual-on-a2bb.patch"
git apply --reverse --check "$D_SAVE/local-quick1.patch"
```

These are owner-executed templates, not architect actions. `D_SAVE` denotes the
new retained evidence directory, not a shared scratch path. Verify successful
complete writes, the saved hashes and unchanged source/index before proceeding.
The first patch preserves the exact old local work; the second expresses its
remaining difference from the new Go base. Do not reuse the full old patch as
the new feature diff.

With that proof and the empty index, root may restore only those two working
files from exact `9fe491218e35a3250f2a72c203c2cecc3cb7ae16`, leaving the index
untouched, then rebase the sole original lease commit from base
`e3315a483f3d3536d492ecbe40f2655449cf630f` onto exact `a2bbf2...` on the same
owned feature branch. No repository-wide reset, clean, stash, temporary duplicate
bugfix commit or change to another worktree is involved. Preserve unexpected
files/index changes and stop if the verified scope changes. If rebase conflicts,
root records them and gives application resolutions to the implementer; it must
not choose an entire old file that removes upstream changes. If that rebase
attempt is abandoned, an ordinary rebase abort restores its starting ref, and
the saved full patch can restore the two old files with a checked application
and hash comparison. Keep the preservation evidence through acceptance.

After a successful rebase, verify the two Go files still equal the exact target
base: the lease commit never changes them. Implementer can check/apply the saved
residual patch against that proven base, then minimize it, or restore the same
residual manually from the saved source evidence. Keep upstream's `accepted`
variable, contention comment and existing stale-CAS test wording; omit local
cosmetic rewrites and the redundant background comment. Do not replay or force
the already-upstream acceptance API/loop change. Root compares the old
`e3315a...9fe491` lease range with the new `a2bbf2...REBASED_LEASE` range before
accepting patch equivalence. A later default advance requires refreshed evidence
and reconciliation, not bypass of the normal ancestry guard.

**Smallest supplementary change.** Retain only the unexported
`reconcileLifecycleOperation` extraction used by deterministic coverage, the
context check after journal/proposal/view proof and before acceptance, and the
three focused test cases plus their temporary-store helper/import in
`operation_state_test.go`. Preserve upstream loop behavior and all existing
guards. The context check adds the accepted cancellation boundary after slow
proof; the tests cover progress-A versus journal-B contention, canceled/expired
entry, and accepted no-op/absence. The deadline tests do not claim to reproduce
cancellation during a slow filesystem read. No general test hook or stronger
state policy is needed. No documentation rewrite is necessary because upstream
already describes fresh reconciliation.

Commit the residual separately with a supplementary subject such as
`portal: check reconciliation deadline after proof`; explain the post-proof
cancellation boundary and deterministic coverage in its body. Do not reuse the
earlier duplicate bugfix subject. Final feature history should show the rebased
lease commit followed by this small supplement, with `8f0f40a` inherited from
the base and no schema/migration or transitional path. Root inventories the
whole new base-to-head series and final diff for independent review.

Run formatting, the preceding exact focused Go selection (its prefix includes
all three new tests), and full affected `./internal/web` quick checks on the
reconciled source. Reconfirm the rebased lease's focused public-dispatch behavior
in the declared environment, for example:

```sh
nix develop .#dev-workspace --command ruby test/workspace_host_test.rb \
  --name '/capture_lease|non_streaming_provider_dispatch/'
```

Old quick1 results alone do not validate the new base. Preserve the normal hook
and source-commit procedure. E's final D pin stays held until the final exact D
feature head is published; no intermediate rebased head becomes its contract
pin. K's published `93a16...` source and E's independent K tests are unaffected.
All intended K/E/D commits and quick checks, then the independent four-lane
final review, still precede long package/VM verification. No CI rerun,
activation, default-branch integration or lifecycle action follows from this
history reconciliation brief.

### Artifact lock lifetime during synchronous publication

This bounded clarification makes the accepted output-root serialization
requirement explicit. Evidence is original committed K
`93a16d6cecb6bc847ec9335a3f170eb8b301ab56`, not the implementer's mutable
correction: `runner/capture.cjs:30` acquires a helper-only artifact lease;
`lib/artifacts.cjs:84` snapshots retained results; and `:124` publishes through
synchronous validation, renames and JSON writes. Helper death after a final
live check can release its flock while Node is still in that synchronous
section, before Node can receive the death/EOF event. Cancellation checks alone
therefore cannot establish full serialization. This is a source-supported
interleaving, not a reproduced runtime failure or independent review finding.

**Minimal capture boundary.** Retain the existing helper and capture path, but
make the writing Node process keep the same open file description on which
the fixed `cluster/artifact-lock.rb` acquires its exclusive flock. Node opens
the persistent `outputRoot/tmp/capture.lock` without truncation or symlink
following and passes that descriptor explicitly as child FD 3. An internal
helper option selects the inherited descriptor; it must not reopen the path
and lock a different open file description. The helper verifies that FD's
regular-file, owner, mode and device/inode identity against the validated lock
path before flock and readiness. This needs only Node's existing descriptor
passing and Ruby's existing flock support, with no native dependency, generic
locking framework, workspace dependency or public capture bypass.

Keep safe creation/opening bounded to the artifact root: reject store roots,
symlink ancestors and unsafe root/tmp ownership or permissions before creating
anything; create a missing private tmp directory and mode-0600 lock with
exclusive creation, and reject unsafe existing objects rather than repairing
them. Reuse the existing path checks where applicable. Node needs the checks
that make its own open/create safe; Ruby retains its existing authoritative
path/descriptor validation before granting readiness. Do not add a second
metadata or ownership protocol. Do not unlink, replace or truncate the
persistent lock file on release. No artifact FD goes to the cluster controller,
browser, SSH transport or VM runner; only the fixed artifact helper receives it.

Both processes release their copies by **close only**. An explicit `LOCK_UN`
through either duplicate releases the shared flock even while the writer's FD
remains open and is prohibited. Helper loss or automatic helper reaping must
not close Node's copy. Hold it until publication has stopped, all browser/SSH
work has completed cleanup, and the cluster/helper shutdown paths have been
handled; close it last, including exceptional exits. If initial artifact
readiness fails, supervise/reap that owned child and close the unopened-for-work
writer handle without entering capture. Acquire readiness before constructing
`Artifacts` or reading its retained snapshot, and before acquiring the cluster
lease. Existing validation's `artifact-lock.rb --exec` already explicitly
inherits the locked description into its writing child; preserve that physical
protection and its close-only behavior.

Keep the implementer's combined artifact/cluster cancellation and live checks,
including cancellation while cluster readiness is pending and guards before
fixture work and publication. The retained descriptor supplies exclusion while
Node cannot dispatch loss events; it does not make a dead controller healthy.
Once loss is observed, further work refuses and the invocation reports failure.
Neither cancellation nor the flock can undo an already-issued remote request
or a synchronous write already in progress. Existing interruption/hash checks
and staged publication remain; no new recovery or rollback mechanism is added.

**Focused verification.** Extend K's existing `tools/test-artifacts.cjs` and
`tools/test-connection.cjs` coverage, with real Ruby helper/flock competitors:

- After helper readiness, pause the writer's event processing at a controlled
  synchronous publication boundary, kill/reap only its owned helper from a
  separate test process, and prove an independent writer still cannot acquire
  the same output lock. Resume the writer and prove exclusion lasts through
  cleanup, then acquisition succeeds after its final close. Do not substitute
  an already-delivered abort event for this interleaving.
- Prove normal helper exit/close and abnormal helper death cannot unlock a
  still-open writer descriptor; prove writer death plus helper EOF/reaping
  releases the last reference. Check that unrelated child processes cannot
  retain the descriptor. Preserve validator-child exclusion after its wrapper
  dies. Use only test-owned processes and temporary output roots.
- Cover artifact loss before readiness, in the readiness window, while waiting
  for cluster readiness, during capture, and at publication; no later fixture
  starts after observed loss, and owned children/FDs are cleaned on failure.
  Existing stderr-only behavior remains unchanged.
- Competing successful CS/EN writers must acquire before reading retained
  results and keep both entries; capture and `validate --update` exclude each
  other. Different output roots remain independent. Preserve private-path and
  inherited-FD/path mismatch refusal, source/contract/hash checks and interrupted
  publication assertions without adversarial operator-filesystem test scope.

Owning implementation/docs stay in K's artifact helper, capture/lease plumbing,
artifact tests and `cluster/runtime-contract.md`; no K state/connection schema,
D/E protocol, UI or operator approval change is required. Quick checks and
committed independent review still precede long verification. This architect
clarification runs no checks and certifies no in-progress implementation.

### Accepted network inventory and counter refinement (2026-10-08)

The user accepted implementation of this bounded V/W follow-up. It preserves
the preceding availability, role-only classification, ownership visibility and
admission contracts. Source baselines inspected are V
`5d5527a67315c18b595345aa6996d7724c1ed071` and W
`e4c49bcdc91b33b7f644a2f125231cb413cf4bf4` in their existing network feature
worktrees. D, E and the separate K runtime branch remain untouched. Architect
owns this brief; implementer owns application changes; lead owns final English
and Czech wording, publication, pins, evidence and tracking.

**Additive API contract.** Add two integer model readers in
`api/models/network.rb` and output parameters in
`api/lib/vpsadmin/api/resources/network.rb`'s existing `params(:ro)`:

| Field | Exact count |
| --- | --- |
| `available_to_users` | Zero when this network is disabled; otherwise its registered `ip_addresses` with `user_id IS NULL AND network_interface_id IS NULL`, using the existing shared `.unreserved` scope. |
| `owned_unassigned` | Its registered `ip_addresses` with `user_id IS NOT NULL AND network_interface_id IS NULL`, including reserved rows and disabled networks. |

Use SQL counts over allocation rows, not summed host-address size. One IPv6
prefix row contributes one. `IpAddress.unreserved` already uses a correlated
`NOT EXISTS` on `resource_locks` with resource `IpAddress`
(`api/models/ip_address.rb:20`); reuse it without another reservation definition.
The counters describe global stock in one network, not a particular user's
quota or a target VPS's eligibility. Do not add role, CIDR, primary-location,
purpose, node-health, quota, cooldown or other availability heuristics here.
Location/purpose/quota and current reservation checks remain admission's job.
These are observations, not reservations or a promise that a later request
succeeds; no new writer locks or snapshot protocol are required for display.

Keep all existing field computations, input contracts, list/Show/association
permission scopes, allocators, migrations and `Cluster.PublicStats.ipv4_left`
unchanged. Only administrators receive the new statistics: preserve the exact
non-admin output whitelists on `Network.Index` and `Network.Show`, including
included-network serialization. The new names are output-only and must not
enter create/update inputs. Existing admin responses using `:all` may include
them consistently. Extend optional consumer types without requiring the fields
on an older API or non-admin response.

**Counter meaning and labels.** V's `Network#size` at `:94` computes capacity
from network and split prefixes; `used` at `:105` counts registered rows;
`assigned` at `:110` counts any non-null interface; `owned` at `:115` counts all
explicit owners; `taken` at `:120` counts the union of owned/assigned rows.
The lead accepted the source-grounded correction from “Assigned to VPS” to
**“Assigned” in both UIs**: export interfaces also satisfy that unchanged query.
Use the following facts for every statistic's bilingual tooltip; lead supplies
the final natural UI text:

| Display | Tooltip contract |
| --- | --- |
| Available to users | Registered unowned, unassigned, unreserved allocations; zero on disabled networks. Global network stock, subject to location, purpose and quota when used. |
| Owned not assigned | Explicitly user-owned allocations attached to no interface; includes reservations and disabled networks and does not promise assignability. |
| Assigned | Allocations attached to a network interface, including VPS and export interfaces, whether explicitly owned or not. |
| Registered in vpsAdmin / Registered | All allocation rows registered in this network, including owned, assigned and reserved rows. |
| Total capacity | Theoretical number of allocation units derived from network/split prefixes, including units not registered in vpsAdmin; not a usable-host or available-stock count. |
| Owned total (editor) | All explicitly owned allocations, including those already assigned; distinct from Owned not assigned. |

Counts use allocation units, including prefixes, throughout. Do not subtract
owners from assignments or present their overlapping totals as disjoint.
Missing new fields display a dash; never fall back to `used - taken`,
`size - taken`, total `owned`, or a client-computed eligibility value. Numeric
zero is a known value and must render as zero.

**PHP boundary.** Reorganize only `networks_list()` in
`webui/forms/cluster.forms.php:208` into four columns:

1. Network: address/prefix, label and primary location stacked together.
2. Properties: Type, Managed, Enabled and the existing capability-gated edit link.
3. IP usage: Available to users, Owned not assigned, Assigned, Registered in
   vpsAdmin, Total capacity, with the count tooltips above.
4. Actions: preserve the existing IP-list and location-list targets.

Remove the ambiguous Free pair and total Owned from this main table. Preserve
network identity, escaping, role/type information, action capability checks and
the existing availability editor. Read optional values from
`ResourceInstance::attributes()`, as `network_enabled_state()` already does
(`webui/lib/functions.lib.php:36`); this client exposes `__get` without
`__isset`, so `isset($network->available_to_users)` is not a reliable check.
No fallback queries or per-row client discovery calls are needed.

In `webui/forms/networking.forms.php:21`'s routed-IP list, remove the Enabled
column. Only `network_enabled_state($ip->network) === false` receives the
existing `table_tr('#A6A6A6')` row treatment. Its network address carries the
translated, escaped tooltip explaining that new allocation/assignment is
blocked while existing service continues. True or missing state keeps ordinary
styling. Keep owned/assigned disabled rows visible, pagination/filter requests,
links and existing action guards; leave IP details unchanged. Preserve semantic
documentation IDs. Use the existing template path, not a new styling framework.

**React boundary.** In `src/pages/app/admin/cluster/NetworksPage.tsx:658`,
preserve the table/layout and map Used to Registered (`used`), keep Assigned
(`assigned`), replace Owned with Owned not assigned (`owned_unassigned`), and
replace Free with Available to users (`available_to_users`). Remove that
table's derived `size - taken`. Give both languages the count tooltips and
accessible descriptions. The editor at `:796` keeps `owned` but uses its own
explicit Owned total label, so a changed list translation key cannot relabel
that total as unassigned. `src/lib/api/networks.ts` gains optional new fields;
other consumed Network shapes need them only if they expose these statistics.

In `IpAddressesListTable.tsx` and `IpAddressesListMobile.tsx` under
`src/pages/app/admin/ipAddresses/`, add a warning Network disabled badge to
their existing Flags groups only for `ip.network?.enabled === false`.
Keep the current assigned/private/routed flags and row links/actions. The
existing `IpAddress` network type already has optional enabled state and the
page already requests the network association; do not add per-row fetches or
filter disabled rows out of either renderer. Missing/true state creates no
warning. Check keyboard/focus access to descriptions, accessible names,
contrast and mobile wrapping without introducing a general tooltip subsystem.

Owning documentation is V `docs/ip-locking.md` for count semantics and W's
REQ-050/REQ-071, `docs/design/API_CONTRACTS.md`, `WORKFLOWS.md` and existing
network-availability work-log entry for presentation and compatibility. Update
the relevant API/PHP and TS locale catalogs under their normal ownership.
W's locked terminology input is V
`a65a4dfeb92a59df4a80a737a20bcbf8558793ff`; its exact guide and localization
procedure were read through Git objects without a Nix evaluation. The effective
feature API revision remains a separate deployment/fixture identity.

**Hosted verification only.** The user's explicit override prohibits local CI,
test suites and builds. Source-only syntax/whitespace inspection is permitted,
but is not test evidence. Implement and commit the intended source/tests/docs,
obtain hosted evidence for each exact final head, then run committed independent
review under that override. Do not substitute historical green runs, API mocks
or this design investigation for new evidence. Any long hosted monitoring stays
lead/watcher-owned; no VM, capture or package action follows from this brief.

- Backend: extend `api/spec/api/resources/network_read_spec.rb`, with focused
  model coverage only if useful. Cover free unreserved/reserved, owned detached
  unreserved/reserved, unowned assigned and owned assigned rows; disabled zero
  versus retained owned-unassigned; a registered IPv6 prefix counted once;
  per-network isolation and unchanged old statistics. Exercise admin Index/Show,
  non-admin user/support absence of both fields, and included-network absence
  through the existing `ip_address_spec.rb` cases. Keep exact existing filters,
  counts and pagination assertions. Use the existing `network` API topic in
  full/core; `ip-ownership` covers changed IP includes specs and `foundation`
  covers any new model spec. Require the normal topic-coverage aggregate.
- PHP: extend `webui/tests/Regression/NetworkAvailabilityTest.php` using its
  real HaveAPI `ResourceInstance` fixture and XTemplate/DOM rendering. Check
  all four grouped columns, each known counter (including zero), omitted new
  fields despite plausible old Free values, escaped tooltips, retained links
  and edit capability. Replace old column-index assertions with the new DOM
  contract. Check false-only gray rows, absence of the removed column, retained
  assigned service/actions, unavailable detached assignment and unchanged
  details. Hosted `.github/workflows/webui-phpunit.yml` runs these through
  `composer test`. Preserve relevant hosted `webui#networking-dns` selection;
  adjust only directly affected browser assertions if necessary.
- React: extend `NetworksPage.test.tsx` and the existing IP-list rendering
  coverage (`IpAddressesPage.correctness.test.tsx` or focused component tests).
  Render EN/CS, divergent total-owned/unassigned values, zero and missing
  new fields, and true/false/missing enabled flags in both desktop/mobile
  renderers. Assert tooltip meaning, accessible labels, existing links/actions,
  and the separately named editor total. Extend
  `e2e/specs/admin/network_availability.spec.ts`, whose existing `@pr-smoke`
  and `@pr-smoke-mobile` tags reach both hosted Chromium projects, to retain
  implemented UI screenshots and cover grouped facts/flags and responsive
  behavior. W's existing CI runs `ci:quick`, `ci:tests` and production build;
  its Playwright smoke workflow supplies desktop/mobile evidence. Ensure added
  assertions are selected, not merely present in an unrun fixture file.
- Lead manually reviews the hosted desktop/mobile EN/CS captures: PHP four
  readable groups, counter descriptions and gray routed row without lost
  actions; React unchanged network layout, correct new counters, distinct
  editor total and wrapping warning flags. Record synthetic versus real-API
  evidence explicitly. A hover-only screenshot does not establish keyboard
  accessibility; use the rendered assertions too.

**Compatibility and remaining KB work.** These are additive read-only fields;
there is no new migration, input, node protocol or coordination requirement.
Deploying the additive API before the UIs provides complete statistics; a new
UI with an older API shows dashes, and old UIs can ignore the new fields.
UI/statistic rollback does not undo network admission. The existing prohibition
on rolling back to non-enforcing API writers while networks are disabled still
applies. C feature pins and the original K network-pin branch are updated only
after exact V/W publication through lead-owned procedures, retaining both
accepted channel mappings. No default integration or deployment is implied.

The canonical K `docs/webui-change-workflow.md` still applies. The pending
scope remains only CS/EN `networking/ip-address-list` PNGs at the final exact V
pin, now showing the gray disabled row instead of the removed Enabled column.
This supersedes that visual detail in earlier screenshot requirements, not the
portable runtime safety or provenance contracts. Keep the same semantic IDs,
review relevant contract drift, and add no new KB media. Screenshot generation,
local suite execution, staging and production publication remain unperformed
and unauthorized by this architect brief. No outstanding product decision
blocks implementation; deviations return to the lead.

### Inventory description clipping clarification (2026-10-08)

This closes the accepted tooltip/accessibility requirement for the two new W
inventory descriptions. At committed W
`a9d0b5e9402faafef937894f50463da3c27e8935`,
`NetworksPage.tsx:120` places its count tooltip inside the table, and
`IpAddressesListTable.tsx:182` does the same for Network disabled. The
`TableCard.tsx` table wrapper uses `overflow-x-auto`; a descendant's z-index
cannot escape that clipping boundary. Root's
`network-counter-visual1-result.md` records clipped count text in hosted run
`37752175398`; review identified the same concrete boundary for the disabled
badge, whose desktop capture does not show its full description. Earlier
`toBeVisible`/accessible-description assertions do not prove unclipped visual
text. These remain failed-appearance evidence, not approved final screenshots.

**Single bounded owner.** Extract one small component in the admin networking
area, for example `src/pages/app/admin/networking/InventoryDescription.tsx`,
and use it for the network count/editor labels and the new disabled badge in
both IP-list renderers. Accept an explicit unique description ID, localized
description and label content (`ReactNode`, permitting the existing Badge).
The component owns the focusable trigger, hover/focus state, description node,
positioning and listener cleanup. Remove the duplicated inline descriptions
and use the same owner rather than maintaining separate count/badge geometry.
The mutable count-only `NetworkCountLabel.tsx` portal draft was inspected for
this boundary; it is not certified by this brief.

Render the one description node through `createPortal(..., document.body)`,
following the existing Modal/Drawer destination, with fixed coordinates from
the trigger's viewport rectangle. Keep its ID/`role="tooltip"` and the
trigger's `aria-describedby`, accessible label and focus/hover behavior.
Preserve `data-row-no-nav` on the disabled-badge trigger so click, Enter and
Space cannot activate TableRowLink. Desktop-row and mobile-card IDs stay
distinct because both renderers can remain mounted. Keep the existing Badge,
copy, counter values, warning condition, table/card layout and all actions.

Bound width to the viewport, wrap the full current EN/CS descriptions, place
below when space permits, flip above otherwise, and clamp within a modest
viewport margin. Position before the popup is painted and update on resize and
captured scroll events, including horizontal table scroll. Suppress a floating
description whose trigger is no longer rendered/visible; remove listeners and
the portal on unmount. Use the existing layer conventions so editor hints are
not beneath their modal. Retain combined focus-or-hover visibility: pointer
departure alone must not hide a focused description, and blur alone must not
hide a hovered one. No global portal registry, Badge rewrite, dependency,
TableCard overflow change, page-budget increase or debt-ledger change is needed.

**Decisive hosted regression.** Extend the existing EN/CS
`@pr-smoke @pr-smoke-mobile` cases in
`e2e/specs/admin/network_availability.spec.ts`; share only a small description
geometry assertion inside that spec. Resolve the tooltip globally by the
trigger's `aria-describedby`, not as a descendant of its old table/card.
Check focus and hover separately, their combined lifetime and eventual hiding.
For each visible description assert one correct ID/role/text, body portal,
fixed position, nonempty text ranges fully inside its rectangle and viewport,
no ancestor clipping intersection and no internal scroll-size clipping for the
current strings. Assert the full description, not only an icon or short title.

Exercise count headings at the horizontally scrolled table edge and an editor
count within its modal. Put the explicit-disabled fixture in the **last**
visible desktop row and mobile card, verify that placement, focus its warning
and check the same full-text geometry. Include a near-bottom placement where
below would overflow, so above-placement/clamping is tested rather than merely
the unconstrained top row. Recheck after table/window scrolling or a viewport
resize while open. Preserve true/missing-state absence and assignment/action
assertions, including no row navigation from the warning trigger. Retain
screenshots with the complete focused count and final-row/card warning text
visible in each language/project; root manually inspects the corrected images.

This is W-only remediation of the accepted descriptions. Update the existing
work-log/evidence explanation and focused rendered tests as needed; preserve
all API, PHP, KB and runtime boundaries. No local CI/tests/builds are authorized.
Hosted evidence must name the corrected exact committed head, and the lead owns
the affected review rerun. This clarification performs no implementation or
verification and does not complete the review of original Wa9.

### PHP network inventory label/value alignment (2026-10-08)

The user accepted a bounded layout refinement after inspecting the uploaded
PHP network-list screenshot and chose right-aligned IP counts. Keep the four
outer Network/Properties/IP usage/Actions cells and one striped row per network.
Use the existing `dl.inline` key/value grid within Properties and IP usage,
with narrowly scoped network styling: zero list margins, consistent vertical
spacing, top-aligned grouped cells, plain labels, left-aligned property values
and right-aligned bold counts. The shared table does not need colspan/rowspan;
extra physical rows would change its alternating backgrounds and hover model.

Implementer0 owns only `webui/forms/cluster.forms.php`, scoped rules in
`webui/public/template/css/main.css`, the existing real-client/template
`webui/tests/Regression/NetworkAvailabilityTest.php`, and the existing hosted
`tests/playwright/webui/specs/admin-cluster.spec.cjs`. Preserve labels,
translations, descriptions/ARIA, icons, Enabled capability/Edit behavior,
links/actions, escaping, zero versus missing counters and trusted numeric
capacity markup. Keep old-API handling and all counter semantics unchanged.
No shared table helper, API, React, allocation, schema or migration change.

Extend meaningful existing assertions for separate label/value pairs and
retained actions/edge cases. Hosted admin-cluster browser coverage must check
EN/CS property value alignment, IP-count right edges, top alignment, spacing and
no content overflow, with exact-head readable images. Source-only inspection
and necessary ordinary hooks/source generators remain allowed; the user's
NO LOCAL CI/tests/builds direction remains in force. Do not execute suites,
syntax/formatter commands, Nix evaluation/builds or capture runtime locally.
Root owns final copy, normal hook commits, publication, hosted verification and
independent committed affected-lane review.

Fold the change into the owning legacy PHP feature commit, preserving the
complete four logical V subjects and unaffected API/Index/counter patches.
After exact V publication, root regenerates/consolidates canonical C V/W streams
with Wce unchanged and the original K five-record source pin. Preserve all
unrelated graphs, follows, fingerprints, pages, PNGs and source contracts.
This CSS/markup edit is compatible with existing API versions and needs no
migration, node update, deployment ordering or special rollback. The running
preview already uses the live PHP worktree; no service rebuild/reset or cluster
lifecycle action is selected. Uploaded evidence stays outside version control.
No new KB capture scope, media publication, production deployment or default
integration is authorized. The existing two CS/EN networking/ip-address-list
KB PNGs remain separate pending work; accepted denial/OPTIONS Advisories stand.

A small scoped CSS comment may explain grouped alignment if needed; no new
member-facing documentation is useful because behavior/copy is unchanged.
Record exact source/hosted/review evidence and current phase in session state.

## Accepted finish-session design — superseding refinement (2026-10-08)

The user accepted implementation of the revised finish-session plan. This
section supersedes the earlier nested `runtime/standalone` suite/profile,
outer-VM capacity requirements, artificial changed-source fixture and separate
legacy/runtime K capture streams. It also resolves the previously provisional
HTTP 400 suggestion. Existing network admission, role-only classification,
counter/visibility semantics, portable state/connection/artifact schemas,
physical artifact locking and prepared-closure recovery remain unchanged.
This is an implementation brief, not evidence of completed checks or operations.
The lead owns Git, pin regeneration, hosted verification, independent review,
visual acceptance and the separate OPTIONS issue. Implementer0 owns application
changes. Architect0 owns only this design append; plan/state/portal remain with
the lead. The preview cluster must remain running.

### Expected disabled-network errors: first implementation unit

In V, add the established narrow `IpAddressInvalid` rescue followed by
`error!(e.message)` in four public actions: `IpAddress::Create`,
`IpAddress::Update`, `Network::AddAddresses`, and `VPS::Update` (ownership
transfer). Extend Update's existing domain-error rescue rather than inventing
a second handler. The owning files are `api/lib/vpsadmin/api/resources/`
`ip_address.rb`, `network.rb`, and `vps.rb`. Keep `Network#ensure_enabled!`,
transaction rollback and the exception hierarchy unchanged. Do not add a global
`IpAddressInvalid` mapper, a new disabled-network exception type or a broad
`StandardError`/`Exception` rescue.

Return the existing action-error contract: **HTTP 200**, `status: false`,
`response: null`, the localized existing `errors.network_disabled` message,
and `errors: {}`. This matches the existing Assign/AssignWithHostAddress
`error!(e.message)` handling. HaveAPI 0.29.8 `Action#error!` leaves HTTP status
unset; its server action route defaults to 200, and the PHP client interprets
the envelope's `status` and `message`. A new HTTP 400 convention is unnecessary.
Keep unexpected exceptions non-disclosing HTTP 500 failures. No locale text,
schema, response field, allocator, node protocol or client change is needed.

Extend existing real Rack specs in `api/spec/api/resources/ip_address_spec.rb`,
`network_write_spec.rb`, and `vps_write_spec.rb`: all four routes in EN/CS with
exact status/envelope/message; unchanged IP/network/owner/interface data,
resource charges, persistent locks and transaction-chain counts after denial;
existing assignment denial remains consistent. Inject an unrelated
`RuntimeError` to retain the generic 500/non-disclosure boundary. Use realistic
inputs which reach the disabled guard rather than fail another validation first.
These are hosted tests only, under the existing full/core `ip-ownership`,
`network` and `vps` topics; preserve exact-once topic coverage and its aggregate.
The separate OPTIONS timeout warrants only the lead-owned W issue, not a
WebUI/product fix in this unit.

### One ordinary-host verifier and supported source transition

K owns one new public `runtime-verify` flake package/app exposing
`vpsfree-kb-verify`. It drives the existing packaged `vpsfree-kb-devcluster`,
`vpsfree-kb-capture` and `vpsfree-kb-validate`; it is not a second launcher.
Replace the nested standalone test, its standalone-only profile plumbing and
obsolete check references. Keep other KB page suites and their external
test-framework interface unchanged. Reuse the existing assertion/export code
where useful, without retaining an alternate nested acceptance route.

Bound implementation to K's package wiring in `flake.nix`, one portable
verification command beside the existing `tools/` commands and its focused
tests, and the fixture/capture files listed below. Remove standalone-only
`tests/suite/runtime/standalone.nix`, `nix/standalone-profile.nix` and dependent
profile/script-check plumbing when superseded; adapt the current export helper
and tests instead of retaining a dead VM hook. Update `tests/all-tests.nix` and
`bin/check` coherently. Existing launcher/state/process/resource/closure/disk
implementations and physical artifact-lock ownership need no redesign;
`kb_runtime.rb` changes here are confined to the additive fixture capability.
Route a concrete need beyond this boundary through the lead before expanding it.

The verifier takes an explicit private ordinary `--root`, `--config-a`,
`--config-b`, immutable `--predecessor-ref`, and sequential `--phase` selectors
`installed-layout`, `isolation-continuity-update`, `bilingual-capture`.
Phase receipts record exact inputs, package/source identities and completed
assertions. Later phases require their actual predecessor receipts; they cannot
infer ownership from a directory or silently start a replacement campaign.
Keep all generated state beneath that campaign's proven roots and all lifecycle
work through the public engine. Failure retains truthful incomplete evidence.

Run the installed tools directly on Linux/Nix/KVM outside workspace/checkouts,
with package-selected PATH, Ruby/Node/Playwright/Nix/SSH and cleared development,
browser and source overrides. Preserve only required ordinary user/Nix-daemon
access and the validated per-user runtime directory, so resource claims still
coordinate across roots. No required workspace package, registry, session,
provider activation or ambient source override. This proves path independence
on the actual host; it does not claim a pristine host without installed
workspace software. Immutable source and writable output/state roots stay
separate. The verifier's final source receipt and package paths come from its
exact committed Git-flake evaluation, never an invented revision on a path
flake. Keep forty-hex revisions, lock/input/fixture digests and package source
checks intact.

Use published K `68aa33b451a14eb7bf4b2f1a090a8e5a2f80b52e` as the genuine
predecessor. Resolve its `kb-runtime` and `runtime-source` outputs together
from that exact ref and invoke its packaged executable with its embedded
metadata. Do not inject replacement `--software-metadata`, manufacture a
marker-only Git commit or change the normal K/E input graph to obtain the old
engine. The final K package contains the final V HTTP fix/current PHP source;
K68 pins V5d and is never used to generate accepted screenshots.

Both A and B use `single`: services 4096 MiB plus node1 4096 MiB, DNS disabled,
services root 12288 MiB and node1 tank 16 GiB. Use the same slug in different roots.
Keep B's resolved configuration, disk layout, TLS names and SSH endpoints
unchanged from its first start through its final update. Explicit local test
networking is selected for this acceptance, without changing the engine's bridge
default: loopback forwards, disjoint integer multicast ports, `example.test`
domains and QEMU upstream DNS `10.0.2.3`. Proposed fixed A resources are SSH
24000/24001, HTTPS 24010, UDP 24020; B uses 24100/24101, 24110, 24120. These numbers
are requests, not availability claims. Existing resource claims/bind checks
must refuse conflicts, with no automatic port/subnet fallback or foreign cleanup.

Execute the real proof in this order, with recorded assertions:

1. Exercise installed-layout source/default-path behavior without an outer VM;
   start A using final K and B using K68. Prove distinct instances, roots,
   sockets and effective TCP/UDP resources. Attest each source and every actual
   guest system closure through the supported descriptor/SSH path.
2. In B create root/data sentinels and privately retain the complete six-file
   credential identity: SSH private/public key, CA certificate/private key,
   service certificate/private key. Retain root/tank device-inode-size records.
   Stop/resume B with K68: fresh live run, identical prepared artifact/closures,
   disk identities, credentials and sentinel checksums.
3. While A remains healthy, invoke final K's public `update` on live B. Require
   exact candidate closure import/content/GC-root proof before stopping old B,
   then preserved-disk direct boot and live final K/V/system-closure attestation.
   Prove genuinely changed source/closures, same B instance and disks, fresh
   artifact/run, unchanged six credentials and sentinels. No old-image fallback.
4. With A and B now both on final K, recheck same-slug/two-root isolation and
   live endpoints. Stop/reset only A through its public engine, then prove B
   remains healthy. Stop/resume B using final K to prove final-code cold
   continuity: fresh run, unchanged accepted artifact/source/toplevels/data.
5. Exercise the public live capture lease: lifecycle stop/update/reset must be
   busy while held, with unchanged state. Close the owned peer and interrupt
   only the exact controller spawned by the verifier, establish release, and
   reacquire a healthy lease. Retain wrong-source-before-fixture and explicit
   endpoint-routing assertions. Hosted process/fake tests retain the deeper
   crash-stage/EOF/artifact-flock matrix; do not claim they prove live guests.
6. Capture/validate both languages from B's attested final source as below.
   The preview cluster and unrelated state are never selected. Any final B
   stop/reset must be an explicit test-owned operation in the lead's accepted
   command packet, not implied session completion or deferred cleanup.

K68's `cluster/lib/kb_runtime.rb` update checks layout, credential identities,
domain sets, services root size and SSH endpoints. Preserve those checks; the
new fixture capability does not change state 2, artifact 1 or connection 1.
Resume still requires exactly the selected prepared source and refuses a
pending update. Existing recorded-candidate retry is the only update recovery.

### Direct capacity and cache admission

Peak guest RAM and `/dev/shm` are 16 GiB for A+B, then 8 GiB for B alone. Proposed
direct admission requires 24 GiB available RAM and 18 GiB free shm, including
host/process and shm headroom; remeasure before the operation and account for
build/browser activity. No nested KVM, outer 32 GiB VM, outer 128 GiB image or
272 GiB disk floor remains. KVM acceleration is required; no emulation fallback.

At effective OS `6bdf458fd9105379860234ff33d352e55844f08f`,
`osvm/lib/osvm/machine.rb#prepare_disks` creates tanks with `truncate`, and
virtiofs uses `/dev/shm` memory backing. K's `cluster/lib/kb_machine.rb` copies
the initial services image with `IO.copy_stream`: budget its full extent, not
assumed sparse/reflink savings. Resume/update preserve the writable root.
Three retained 12 GiB service images, two 12 GiB writable roots and two full 16 GiB
tanks total 92 GiB. Adding 16 GiB host reserve gives a **108 GiB worst eventual
owned-output envelope**, before missing package closures/build temporary peak.
It is **not a mandatory free-disk floor** or a measured allocation estimate.

Admission must account per actual filesystem for current allocated owned bytes,
remaining image/copy extents, exact missing closure requirements, sequential
build temporary peak, bounded guest/template writes and untouched host reserve.
Avoid double counting existing store outputs. Record apparent lengths and
allocated blocks, without guessing compression/reflinks/deduplication. Place
the ordinary root on the measured disk-backed filesystem; do not assume `/tmp`
is disk-backed or use shm to hide image demand. No generic host allocator,
foreign GC, capacity assertion override or automatic disk resize is needed.
The 16 GiB tank is for one explicitly 4 GiB VPS plus its selected template and
metadata; confirm real ZFS space/headroom and retain normal quota checks.

Guest import admission remains unchanged: exact missing recursive closure NAR
bytes plus 256 MiB and 10,000 inode reserve, content/reference verification and
per-artifact guest GC roots. If the 12 GiB root cannot admit the candidate, refuse
before shutdown and report the measured prerequisite. Do not weaken the guard,
resize, replace the root, mount the host store or silently recreate the instance.
Host observations supplied during planning (244.3 GiB disk, 34.25 GiB shm,
59.6 GiB RAM) are not launch-time capacity receipts.

Preserve the selected OS/nixpkgs graph and cache provenance. Current K68 uses
OS 6bdf458 and nixpkgs `5dfba6236110080a54247d6460bc2ff5dda939cc`;
the test cache is `https://cache.vpsadminos.org` with key
`cache.vpsadminos.org:wpIJlNZQIhS+0gFf1U3MC9sLZdLW3sh5qakOWGDoDrE=`.
Before construction, establish the actual selected kernel/cache prerequisites.
Cache configuration is not availability proof. Stop and investigate unexpected
local kernel compilation under the existing verification procedure.

### Minimal IP inventory fixture and bilingual capture

Add one `ip-inventory` fixture/capability, requiring services+node1. Change only
`networking/ip-address-list` from `base-vps`/`traffic-samples` to that token.
Keep old `base-vps` semantics for other captures. Update together
`fixtures/prepare.cjs`, `scenarios/networking.cjs`, `captures.json`,
`cluster/lib/kb_runtime.rb#capabilities`, `runner/validate.rb`'s allowed fixture
list and focused existing checks. Keep fixture digest coverage complete if
code is extracted. Do not put the new manifest into legacy original-K code
which cannot provide/validate this fixture.

The minimal path creates/reuses one real VPS via supported fixture/action
paths, explicitly choosing 1 CPU, 1024 MiB RAM, 4096 MiB disk, and validates its real
enabled assigned address. `cluster/seed-production-shape.rb` reapplies 4 GiB RAM
and 120 GiB production-shaped defaults; changing only seed.defaultVpsResources
would not constrain this fixture. Request the small values at the public
resource step. Keep other fixture defaults and production-shape claims intact.
Skip NAS, child dataset/mount, traffic, reverse-record and unrelated page work
for this checkpoint. Gate networking navigation by wanted checkpoints or use a
bounded IP-list-only path; retain full behavior for other selections.

Provision a uniquely identified dedicated `203.0.113.0/24` public-access pool
and `203.0.113.10/32` owned/unassigned IP while enabled, with ordinary location,
ownership and charging, then disable only that pool. Source inspection found no
configured collision; runtime must still reject unexpected existing identity,
ownership or interface state. Reruns validate the existing disabled fixture,
without re-enabling the pool, allocating again or charging again. Keep primary
198.51.100/24 and IPv6 pools enabled; preserve quota/accounting failures rather
than bypassing them. Use only dedicated synthetic users and documentation
identifiers. Existing per-user IPv4 headroom is not a license to alter quotas.

Assert the enabled assigned row's real VPS link and the disabled owned detached
row's background `#A6A6A6`, retained permitted details/actions, missing assignment
action and absence of an Enabled column. Check the localized native title and
focusable `tabindex` on the disabled network address. V's
`webui/forms/networking.forms.php` renders a native title: a DOM PNG cannot
certify that a browser-native tooltip popup was visible. Do not fabricate a
different tooltip for the screenshot. Review the contrasting rows in both PNGs
and the title/focus assertions separately.

Use final package commands and one explicit writable output root O, different
from invocation CWD, for sequential CS and EN. One invocation uses
`--cluster`/`--state-root`; the other uses the private exported `--connection`.
Both select `--checkpoint networking/ip-address-list --output-root O`.
An additional EN invocation from CWD=O without `--output-root` may replace the
same EN result to prove successful packaged writable-CWD defaults; it creates
no additional media concept. Retained results must contain exactly the two
language/ID rows from the same immutable generator source. Source files remain
unchanged. Run `vpsfree-kb-validate --update --output-root O`, then strict
`vpsfree-kb-validate --output-root O`, without `--allow-missing` for acceptance.
The existing validator may use unchanged PNGs from immutable source.

Export under the physical output lock and verify checksums for only:

- `screenshots/cs/networking/ip-address-list.png`
- `screenshots/en/networking/ip-address-list.png`
- `captures.json`
- `tmp/capture-results.json`
- `tmp/capture-source.json`

Reuse the existing export allowlist/validation contract with a direct local
copy; no VM pull transport is needed. Never export connection/account files,
credentials, CLI homes or raw browser/SSH transcripts. Retain original generating
K revision/receipt after a later media commit; do not relabel it as the media
commit. Root validates the bundle, reviews both images/crops/fonts/identifiers
and accepts the bounded carryback. No extra KB media or publication is included.

### Source lineage, ownership and recovery

Root first consolidates ONE authoritative K feature source: portable engine,
direct verifier, minimal fixture/scenario/validator and final V pin. Reconcile
original K's pin branch and runtime branch into that reviewed source before
capture, preserving historical refs and records. Do not maintain two competing
final streams or transfer new-fixture metadata into old code. K68 remains a
published immutable predecessor outside the consolidated final logical series;
no repeated canonical pin or synthetic source change is needed for update proof.

Publish final V first, then update K's five owning pin records coherently:
`flake.nix`, `flake.lock`, `captures.json:vpsadmin_commit`,
`contract/navigation.yml:vpsadmin_revision`, and
`contract/pages.yml:revisions.vpsadmin`. Preserve unrelated input graphs,
follows, semantic IDs, page budgets and unaffected fingerprints. Generator
source must already include final HTTP/PHP bytes before review and capture.
After approved media carryback, root selects the final combined K head in E's
own flake/lock, preserving K's independent input graph and D
`51aba080b264c28f5584867b6cf006bf423ae2f3`. No E adapter functional change is
indicated by the additive fixture capability. Update C's backend channel later
through its owning confctl procedure; W code and its existing pin stay unchanged.

K's `cluster/runtime-contract.md` owns portable command, capacity, provenance,
recovery and proof-limit documentation; update its README and relevant
`docs/webui-change-workflow.md` examples to the supported minimal capture path.
E's `dev-clusters/kb/README.md` links that contract and distinguishes source/
package composition from installed managed activation. V's
`docs/ip-locking.md#network-availability` should record the ordinary policy-error
envelope where useful, preserving `docs/upgrade-network-availability.md`'s
deployment constraints and member-facing locale copy. This session section
owns the actual predecessor/campaign ordering and pending evidence, not generic
project operational history.

There is no new API/database/portable-state schema or node-coordination change.
Old API versions remain callable; mixed API versions can still return generic
errors until upgraded. Reverting the HTTP-only source change reintroduces that
bug, not a schema rollback. For K, legacy state is never adopted. Incomplete
updates retry only their recorded source/config/candidate; no automatic
old-source rollback or old-image copy. Preserve all six credentials, launch/
artifact/import receipts, disks and resource claims on ambiguous failure.
Recovery uses existing public commands and positive process proof; listing paths
does not grant cleanup authority. No force cleanup, unrelated-cluster action,
default integration, production deployment/KB write, workspace activation or
session lifecycle change follows from this implementation brief.

### Hosted checks, review and real acceptance order

**NO LOCAL CI/tests/suites.** All source quick/required checks run on hosted
exact committed heads. Source reads/writes here do not claim a test result.
The following selectors are grounded in the inspected workflows, not executed:

| Owner | Hosted selection and evidence |
| --- | --- |
| V | `.github/workflows/api-specs.yml` (`API Specs (topic parallel)`): `API specs (full) - ip-ownership/network/vps` and corresponding core jobs cover the three existing spec files; the actual workflow retains all13 topics and requires `API specs - topic coverage`. Keep native per-topic JSON, environment and file manifests for the exact run/head; do not reduce the aggregate to six jobs. The job runs `bundle exec rspec "${files[@]}" --format documentation --format json --out "$result"` in its prepared API environment. |
| K source | `.github/workflows/check.yml`, `Check`/`check`: current command `nix develop --command bin/check --allow-missing`. Adapt `bin/check` to the replacement verifier, remove nested-profile-only checks and preserve existing runtime/closure/machine/connection/artifact/browser/contract checks plus meaningful new CLI/fixture/phase/export tests. Keep `--allow-missing` only for this existing source-CI convention, not real artifact acceptance. |
| K final media | Hosted canonical `nix develop --command bin/check` at the resulting media head, plus exact-source strict exported-bundle validation and root's CS/EN visual review. No local full `bin/check`. |
| E | `.github/workflows/check.yml`, `Check`: `nix flake check --print-build-logs` and `nix run .#devcluster-check`; selected `kb-provider-package`/`kb-provider-contract` and existing `test/kb_{devcluster,guards,connection,lease,cli,portable,public_dispatch,cleanup}_test.rb` cover the fixed selected engine/read-validator/public-dispatch boundary. This is source/package composition proof, not installed activation. No new host-migration VM is selected. |

K's separate `Managed page runtime` workflow currently runs all external-test
suites after a source check. Remove standalone's obsolete registration when
replacing it, retain the other page suites and their truthful scope; neither
that workflow nor a generic `test-runner.sh test` is the new direct-verifier
entrypoint. Do not silently launch broad page/VM verification to satisfy the
targeted finish-session requirement. Root owns exact workflow selection and
gating under the accepted hosted-only policy.

Complete source changes, hosted quick/required evidence and all intended source
commits before independent final review of the whole relevant branch series,
including obsolete-history and migration conclusions. Only after that gate may
the fresh verification watcher construct the exact selected packages/configs,
check launch-time capacity/cache prerequisites and run the direct phases above.
No unchecked local package build/evaluation or activation is an unblock path.
Artifact carryback follows real proof; hosted final canonical checks and any
required affected review follow its committed diff. Re-pin/check E against the
final combined K source without silently treating that as an installed package
transition. Exact source identities, commands, native exit results, stage
receipts, capacity facts and evidence limitations belong in lead-owned records.

Acceptance requires: the four bilingual policy denials and unrelated 500
boundary; installed source/path independence; real final-code two-root isolation;
old and final cold resume; genuinely changed-source update with six credentials,
disks/sentinels and live closure integrity; public lease exclusion/loss behavior;
both final-source gray-row PNGs with exact merged provenance/strict validation;
and hosted final K/E composition evidence. Missing package/guest capacity or
runtime evidence remains a named prerequisite, never a waived assertion.
Preserve the preview and leave the development session open.

### Public lifecycle contention clarification (2026-10-08)

Source inspection of K68 confirms a discrepancy with the accepted direct lease
phase: `State#lock` and `State#transaction` default to `wait: true`, and public
`Engine#start`, `#resume`, `#update`, `#stop`, `#reset` omit that option.
Only `status` and the launcher's existing cleanup/adoption queries explicitly
use nonblocking transactions. A capture lease holds the exclusive gate for its
entire lifetime. Thus a lifecycle request currently queues and may mutate the
cluster after lease release; the verifier must not launch that queued request
and race to cancel it.

Make this policy explicit at exactly the five public lifecycle entry points:
`start` uses `state.transaction(create: true, wait: false)`; `resume`, `update`,
`stop` and `reset` use `state.transaction(wait: false)`. The existing transaction
passes the same policy to gate and operation locks in their current order.
The existing `Busy` exception and launcher mapping produce exit75; a caller
must deliberately retry after contention. Leave `State` defaults unchanged.
Do not widen this change to connection, SSH, refresh, capture-lease or runner
locking. Keep all ownership/schema/path checks, existing status/query behavior,
long-operation timeouts and private `start_locked`/`stop_locked` reuse intact;
those helpers remain inside their caller's already-held transaction and do not
reacquire locks. This is a bounded necessary extension to the earlier
capability-only `kb_runtime.rb` implementation boundary.

For an existing instance, rejection must precede any phase/candidate/identity,
credential, disk, claim or process mutation. If operation-lock acquisition loses
after the gate was acquired, unwind/close the gate immediately. Fresh start may
create only the ordinary persistent empty lock infrastructure needed for
serialization before acquisition; it must not initialize a competing instance
or begin preparation before both locks are held. No new state schema, waiting
flag, timeout policy or retry daemon is needed. Old K68 remains a truthful
blocking predecessor; only final K participates in the real busy-exit phase.

Preserve truthful lifecycle success as well. The current launcher calls
`engine.status` after start/update/resume returns and releases its gate. A new
lease can acquire the gate in that window, causing exit75 after successful
mutation. These three methods already return the verified completion descriptor
from `await_ready`, including the existing-update recovery return path. Keep
that return contract and render the existing status-shaped success response
from this returned descriptor (`schema: 2`, `found: true`, `state: ready`,
instance/run IDs, `ready: true`), describing the just-completed operation.
Do not perform a second status lock acquisition to decide that command's exit.
A small launcher-local formatter is sufficient; no extra receipt, global
registry or new response field. The separate `status` command continues to
report a fresh guarded snapshot. Stop/reset success output remains unchanged.

Add hosted focused real-process flock cases using existing runtime-test support
and pipe/readiness barriers: a separate process holds the gate while each of
the five valid lifecycle requests exits75 before the holder releases it;
operation-only contention also returns75 and releases the acquired gate.
Compare retained instance bytes/claims and fake runner/build activity to prove
no mutation or queued work, including after holder release. Use finite test
deadlines only to diagnose failure, not to make cancellation the intended
behavior. Prove a fresh explicit retry works after release and that a normal
noncontended operation can run longer than lock admission without losing its
ownership. Cover start/resume/update success formatting deterministically when
another holder appears after the completed engine call: success must remain
exit0 with its completed-run receipt rather than a post-success Busy error.
Keep the existing CLI Busy-to75 test and lease/EOF tests; do not replace actual
cross-process lock contention with a mocked Busy exception alone.

Update K's runtime contract/CLI guidance to name all five nonblocking lifecycle
operations, explicit retry on75 and success-at-completion semantics. The direct
verifier uses final public commands and waits for their actual exit75 while
keeping the lease open; it never relies on killing a queued destructive command.
This clarification authorizes only the bounded source implementation above
through the lead. Tests remain hosted under the existing NO LOCAL CI policy;
no check, runtime operation or behavior verification was performed here.

### Direct verifier capacity evidence clarification (2026-10-08)

This supersedes any reading of “sequential build temporary peak” above as an
exact value derivable before construction. The mutable verifier's proposed
`build_headroom = 8 * GIB` has no supporting evidence and must be removed.
Neither cached download sizes nor missing-path NAR sizes bound a Nix builder's
temporary workspace, decompression, image construction or internal parallelism.
Unknown scratch stays explicitly unknown; it is not zero or a made-up allowance.

Keep two distinct operational boundaries. The parent prepares the exact reviewed
verifier/capture/runtime packages under a recorded capacity assessment and fresh
watcher before invoking the resulting verifier. This ordinary targeted package
construction launches no VMs and cannot be guarded by its own not-yet-built
verifier. Its realized paths and actual filesystem consumption then become facts
for runtime admission. The verifier must also validate admission before its
`installed-layout` predecessor `nix build`, not first inside the later isolation
phase. Recheck before each A/B start, resume and B update, accounting for the
already-running instances and preserving the unrelated preview.

Use one required explicit `--capacity-receipt FILE` for this campaign, supplied
by the parent/operator in a private ordinary file. This is bounded verification
input, not a new engine state schema, workspace service or general reservation
protocol. Bind it to the exact selected final source/package metadata, K68
predecessor reference, both configuration digests, canonical campaign root and
the actual filesystems containing state/images, store and builder scratch.
Record observation time, current allocated/apparent owned output, already
realized paths, known missing substitutions/closures, remaining image/copy/tank
growth, preserved reserves and the resulting available build headroom. Record
which derivations still need construction, the effective build concurrency,
kernel substitution evidence and explicitly unbounded scratch. Nix daemon
scratch location must be established; the client's `TMPDIR` alone does not prove
where builders write. A human-readable assessment may accompany these facts;
do not require an invented exact future-peak number to make the receipt valid.

The verifier checks receipt identity and filesystem bindings, takes fresh free
space/RAM/shm measurements, and records the consumed receipt digest with each
admission. Missing/mismatched evidence or inadequate measured capacity refuses
before the corresponding build/lifecycle command. A receipt cannot waive these
checks. Update the assessment when paths, configurations, filesystems or the
construction plan change; preserve previously consumed receipts. It is not a
signed certificate or a reservation against unrelated host activity. The parent
must establish the fresh watcher's reserve monitoring and owned cancellation
plan before execution; a Boolean in the receipt is not evidence of a running
monitor. Keep these host-specific facts private, outside the media carryback.

Budget per filesystem, grouping shared filesystems rather than charging the
same space twice. The 108 GiB figure remains a worst eventual owned-output
envelope with its stated reserve, not a fresh mandatory disk floor. Existing
allocated output already reduces measured free space. Remaining sparse tank
growth must still be budgeted: subtracting its full apparent `File.size` when
`truncate` has allocated few blocks would incorrectly erase that requirement.
Likewise distinguish realized immutable image allocation, future initial root
copies and retained update images. Count known missing store paths once, avoid
double counting images already included in that set, and retain uncertainty
about filesystem allocation versus NAR/download sizes. Guest/template writes
inside a budgeted tank are not an additional second full tank. Do not assume
reflinks, compression or sparse savings for initial root copies.

Ordinary needed builds may proceed with substantial measured headroom and an
explicit parent assessment of the known build set, plus live reserve monitoring;
there is no mathematically exact build-peak guarantee. Serialize campaign
commands; if the assessment assumes one local builder, enforce that through
normal Nix configuration rather than assuming nested builds are serial. Observe
all affected filesystems, RAM and shm through construction and runtime. Escalate
unexpected builders/kernel compilation, pressure or reserve consumption before
continuing later steps, and cancel only the proven owned operation under its
documented cancellation policy. Do not kill unrelated Nix jobs, reclaim foreign
store/state, stop the preview, or replay an incomplete campaign automatically.
Monitoring has detection/cancellation latency and cannot promise recovery of
space already consumed. Record minima and any interrupted stage honestly.

The source boundary matters: `Software#build` invokes `cluster-config` and
`runner` builds, and `Engine#start` proceeds from `build_artifact` directly to
`start_locked`. There is no public post-build/pre-launch pause in K68. Admission
here is therefore the measured decision before the public build-and-launch
operation, maintained by monitoring throughout it; do not claim a separate
post-build launch barrier. Preserve this public route and immutable predecessor.
No private preparation calls, new boot adapter or engine capacity framework are
required. If the concrete host cannot support that monitored operation with
credible headroom, report the missing prerequisite instead of launching it.
Guest import's existing missing-closure/inode reserve, complete closure proof,
ZFS/quota checks and interrupted-update recovery remain unchanged.

Implementation stays in the verifier and its owning runtime documentation and
focused hosted tests: reject absent/wrong-source/config/filesystem receipts
before the first build; reject fresh insufficient capacity despite an older
receipt; retain unallocated sparse growth; deduplicate shared filesystem/path
accounting; and exercise explicit unknown-scratch evidence without inventing a
bound. Hosted tests use their existing command/measurement fixtures and do not
certify host capacity. The parent supplies real preparation/admission/minimum
measurements during the separately authorized post-review run. No source edit,
check, evaluation, build, runtime action or capacity probe was performed for this
design clarification.

### E composition evidence before direct verification (2026-10-08)

Choose the mechanical interim selection, option (a). The earlier instruction to
select final K after approved media does not defer E's new-engine composition
proof until after real work. E `06eefd98` and its reported hosted Check
`37679475899` select K68/D51 and establish that pair only. E's
`flake.nix#mkOrganizationTools` takes both `kb-runtime` and `runtime-source`
from the same `inputs.kb-runtime`; its `tests` check likewise supplies that
input's metadata to the actual selected-validator tests. Old-pair results cannot
establish compatibility with the new lifecycle, verifier and fixture source.

Let G be the exact published authoritative combined K generator commit,
including final V, direct verifier, fixture and all intended runtime corrections.
Before targeted local package/guest preparation or direct real phases, root
mechanically selects G in E's existing `kb-runtime.url` and generated lock.
Retain the provider implementation commit byte-for-byte, K's own input graph,
and D `51aba080b264c28f5584867b6cf006bf423ae2f3`; inspect expected transitive
lock changes without adding follows or unrelated updates. There is no second
input, override, ambient validator or substituted executable. Root owns the
normal fetch/pin/commit/publication procedures; this clarification launches none.

Require hosted `Check` on that exact E candidate: the existing
`nix flake check --print-build-logs` includes `kb-provider-package`,
`kb-provider-contract` and `tests` with the selected K metadata; retain the
workflow's `nix run .#devcluster-check` too. Record E/G/D exact revisions and
the run/head evidence. Together with hosted G checks and the other required
source checks, all intended substantive source commits and the whole-branch
independent final review must precede targeted preparation and real verification.
Review the actual composed input graph and selected read-validator/lease boundary,
not just unchanged E source text. A failure against G is a real compatibility
finding to resolve before proceeding, not permission to return to K68 as proof.

This gate proves source/package composition and the existing synthetic snapshot,
process and pipe tests. It neither activates a workspace package nor proves an
installed managed cluster. The direct campaign still invokes G's standalone
tools outside the workspace, with immutable K68 as its genuine predecessor;
E is not a runtime dependency of that campaign.

After approved captures, let M be the final combined K media head. Keep G's
original generating provenance in the artifacts. Root then replaces the
interim G selection with M in the same canonical E input commit, consolidating
the interim selection rather than retaining a second pin commit/stream. Preserve
the unchanged provider commit, D51 and one authoritative K lineage. Record the
interim E/G evidence before rewriting unmerged feature history. Require hosted
K final-media checks and E `Check` again on the exact final E/M/D pair; old E/G
success does not certify that new pair. Final history/evidence reconciliation
must show that G-to-M contains only accepted media/generated inventory changes
and preserves the reviewed runtime, fixture and contract semantics. Any source
correction instead returns to the affected source checks/review and real-proof
selection; do not relabel G's live run as M or silently skip that distinction.

No E functional change, installed activation, default integration or additional
runtime phase follows from this clarification. The root owns exact pin and
history actions and records; the implementer can continue K independently.

### Explicit hosted strict media check (2026-10-08)

K's current `.github/workflows/check.yml` exposes `workflow_dispatch` without
inputs and always executes `nix develop --command bin/check --allow-missing`.
That successful source job cannot satisfy the accepted hosted strict final-media
gate. `bin/check` already supports both modes and forwards the optional switch
to its final `bin/validate`; no checker/API/fixture change is required here.

The implementer owns this bounded workflow source edit before generator G is
frozen: add optional `workflow_dispatch.inputs.strict`, `type: boolean`,
`required: false`, `default: false`. Keep the existing job, runner, timeout,
permissions, action references and setup unchanged. Use two mutually exclusive,
clearly named check steps with literal commands:

- If `github.event_name == 'workflow_dispatch' && inputs.strict == true`, run
  `nix develop --command bin/check`.
- Otherwise run `nix develop --command bin/check --allow-missing`, preserving
  pushes, pull requests, omitted input and explicit `strict: false` behavior.

Use GitHub's typed `inputs.strict` expression, not the truthiness of the string
in `github.event.inputs.strict`. Do not interpolate inputs into a shell command,
add another workflow, duplicate the checker or alter the separate runtime suite.
Root owns the required official upstream action-ref verification; this edit
does not select new action versions. Add a short owning explanation to
`docs/webui-change-workflow.md`: source checks tolerate not-yet-generated media;
explicit strict dispatch checks the full canonical committed inventory.

After approved carryback is committed as M, root dispatches this existing Check
workflow with `strict=true` against the published feature ref whose tip is M.
Confirm the run's actual checkout/head SHA is M and its event/input selected the
strict step; a mutable ref name alone is insufficient evidence. Record run ID,
head, selected mode and successful canonical command. The inspected retained
default workflow already exposes dispatch; root still verifies its current
hosted availability before the operation. No default-branch integration or
temporary action override is authorized to make dispatch work.

Source validation is bounded to the typed input/schema, unchanged setup and
mutually exclusive event/input cases: push, PR, dispatch omitted/false all select
the existing command; dispatch true selects exactly the strict command. Review
those cases with the workflow diff and retain hosted G push/source evidence.
The decisive strict execution evidence comes from M's explicit hosted run and
its full `bin/check`/validator result. Do not add a local CI run, new workflow
testing framework, or a test that merely restates these two conditions. A strict
failure remains a real final-media blocker; rerunning with `--allow-missing`
does not satisfy the gate. Existing strict exported-bundle validation and root's
visual acceptance remain separate required evidence.

Include this workflow edit in committed source checks and independent review
before direct real phases, alongside the preceding E/G selection. After media,
the required final pair remains strict hosted K/M plus hosted E/M/D Check, with
E's interim and final pins consolidated into one canonical input commit. No
check, dispatch, source edit outside this design, ref change or runtime operation
was performed for this clarification.

### Explicit inventory provisioning account (2026-10-08)

Source confirms the pre-capture authorization blocker. `Connection#account()`
and `browser.login` select `test-user1`, whose configured level1 is an ordinary
member. The new `inventoryApi` inherits that default even for administrator-only
network/location-link/address writes. `prepareFixtures` also unconditionally
uses the administrator member-list page to discover the member ID. This is a
source finding, not a reproduced guest failure; fix both boundaries before G.

Reuse the existing synthetic `test-admin` explicitly through supported seed
configuration. V's `api/db/seeds/test.nix` already creates this login at level99
and assigns namespace blocks1..8. K68 and current K's
`cluster/nix/test.nix#upsert_dev_user` accept `seed.users[].level`, password,
identity fields and namespace; they preserve the supplied level through the
production-shape resource setup. Both engines write exactly `config.seed.users`
to private `accounts.json`. No engine, descriptor, state or account schema
extension is necessary, and no new user/role promotion operation is needed.

Before the initial A or K68 B start, include one complete explicit `test-admin`
entry in BOTH private campaign configurations: level99, synthetic name and
`test-admin@example.test`, explicit disposable password, and namespace
`blockStart: 1, blockCount: 8`, matching the already seeded administrator.
Retain both existing ordinary members and their disjoint namespaces; keep
`test-user1` at level1. Do not silently look up the seed's built-in password or
fall back to an ambient account. This requirement belongs to the inventory
capture configuration and direct verifier's admission, not to promotion of all
capture users or a new privileged default for every capture. Check duplicate or
missing required login entries before lifecycle/fixture mutation.

Use the same B configuration/account values throughout old resume and G update;
do not inject the administrator only at update time. Configuration digests and
the capacity receipt must bind the augmented inputs from the outset. Existing
six-file SSH/TLS credential continuity, disk layout, endpoint/domain checks and
prepared-artifact semantics remain intact. Also retain/compare the private
accounts-file digest across B resume/update without printing its contents.
Existing K68 supports this configured account path; its immutable source stays
unchanged. A retained campaign created without these inputs cannot be relabeled
as this proof or repaired by unrecorded database writes.

In `fixtures/prepare.cjs`, make the inventory HTTP helper take an explicit login
and use two narrowly scoped clients: `test-user1` for member identity, and
`test-admin` only for the dedicated inventory provisioning/verification actions.
Both obtain credentials through `cluster.account(login)` and retain the same
descriptor endpoints, CA, lease checks and cancellation signal. Before creating
the VPS or inventory, call public `GET /v1/users/current` with each client;
require the expected distinct logins/IDs and levels1/99. This route and its
normal/admin behavior are covered by V's existing `user_read_spec.rb`. Use the
returned member ID, not a hardcoded ID or administrator browser lookup.

For `ip-inventory`, bypass the unconditional `findUserId`/`adminm` navigation.
Keep member browser login, member-owned VPS discovery, the existing member VPS
wizard and its explicit 1CPU/1GiB/4GiB resources. Then pass only the admin client
to `ensureIpInventory` for required network/location/IP reads and writes,
explicitly assigning the new address to the proved member. Preserve existing
collision, ownership, quota/charge, rerun and primary-network checks. The admin
view must see an already-disabled dedicated pool on rerun. No admin browser
login, impersonation, session switch or admin-created VPS is needed. Other
fixture paths keep their existing behavior; this is not a general fixture-auth
rewrite. Capture the final IP list through the original ordinary-member browser
so gray owned inventory visibility remains real member behavior.

Implementer scope is the inventory helper/branch, direct-config prerequisite
checks and their focused hosted tests, plus owning runtime/WebUI-workflow setup
documentation. `Connection.account(login)`, browser defaults, seed machinery,
V/E and public runtime schemas need no change. Hosted cases must prove explicit
credential selection; absent/duplicate/wrong-role accounts fail before any VPS
or inventory mutation; inventory uses no `adminm` lookup; member VPS creation and
capture never receive admin credentials; and a disabled-pool rerun uses admin
visibility without reallocation or charging. Keep API-denial/lease-loss failures
fail-closed with no credential fallback or response/secret dumps. Existing pure
fixture mocks do not certify real API authorization; the planned dedicated
bilingual run must establish that boundary, member ownership/gray row and
unchanged account identities. No checks or guest operations were run here.

Positive browser identity is part of this boundary. `launchBrowser` creates a
fresh context; keep that context member-only throughout provisioning and capture.
`login` merely finding logout controls is not an account-switch primitive and
must never be used as one. Before the member VPS wizard and again after loading
the selected IP-list page, assert the rendered session identity: exactly one
`[data-vpsadmin-doc-id="member.edit-profile"]` link with its `id` equal to the
proved member ID, `#logbox-submit` naming the exact member login, and no
`action=regain_admin` context-switch control. These derive from V's
`template/template.html`, `lib/xtemplate.lib.php#logbox` and the actual session
passed by `public/index.php`. Carry only member ID/login in fixture metadata;
credentials stay private. The selected networking scenario must refuse before
publishing an image if that positive check fails, even when logout is present.
A tiny shared assertion used only by this new inventory path is sufficient;
no global login refactor or administrator browser context is required. Add a
hosted wrong-session case (including admin and impersonation) proving that
logout presence alone never admits capture. Admin API calls remain outside
browser cookies/storage and never change the authenticated member context.

### Hosted E3 deletion-force fixture diagnosis (2026-10-08, proposed repair)

Evidence is the retained E Check `37833313842`, exact E
`7b5acc05d3b005ebfb4f05c2cc58d636faaabd1e`, selecting unchanged D
`51aba080b264c28f5584867b6cf006bf423ae2f3`. Native log ZIP is recorded with
SHA256 `546d74ba200290711ca05970346a993dbf28d51225fc0163b75ac9f2a5d76d3d`;
`finish-e-generator-source-log3.txt:810` reports
`TestDeleteOperationRetryUsesTheJournaledForceSetting` timing out at 2.02s.
Its receipt is `paused/validated`, attempt1, force true, expected same `a*64`
journal, empty error, with UpdatedAt restored to the original journal time.
The next E `devcluster-check` step was skipped. An earlier package test in the
same log passed the web package; neither it nor E2's reported success certifies
this failed package instance. These are retained logs, not a local reproduction
or freshly recomputed ZIP hash.

Exact D51 source establishes a fixture inconsistency:

- `portal/internal/web/server_test.go:3961` creates the validated deletion
  journal. Its helper only prints argv and exits0; it never removes that journal.
  `command_fixture_test.go:11` merely execs the helper and supplies no lifecycle
  behavior. The adjacent `TestDeleteOperationRetryCanUpgradeTheJournaledForceSetting`
  at4018 has the same omission with a prepared journal.
- `server.go:2786` requests a full display refresh, then launches the executor.
  On successful return the same receipt/attempt becomes complete. The worker
  in `operation_state.go:42-189` may run that full refresh after completion.
  `proposeLifecycleOperation` at414 explicitly converts complete to paused when
  the matching valid journal remains, restores its phase/time/options, and the
  ordinary CAS accepts that proposal only if its captured receipt is current.
- `waitLifecycleOperation` at4290 samples the raw operation map every10ms and
  accepts only complete/failed within2s. It can observe the brief complete state
  before the full refresh, or miss it and time out on the durable paused state.
  In this test, attempt1 and retained identical journal evidence distinguish
  that reconciliation from fresh journal discovery, which creates attempt0.
- The real `libexec/dev-session#delete` calls `finalize_removal!` before success;
  at6088 that function writes removed recovery metadata, unlinks the journal
  and fsyncs its directory. The neighboring tracking-moved retry fixture already
  removes its own journal before exit0. The force fixtures do not model this
  required successful-command side effect.

The supported causal explanation is executor completion followed by matching
retained-journal reconciliation before the polling helper observes completion.
The exact goroutine schedule is inferred from source and the final receipt;
there is no scheduler trace or independent runtime reproduction. The evidence
does not establish failed force propagation, executor timeout, lost-CAS proof,
or a production lifecycle defect. The2s test timeout is the reporting mechanism,
not a reason to enlarge deadlines or suppress the worker. A retained read of
origin/master `c51ba3c0ca0d41d237ef71c56accd564beb70a33` shows the same original
helper; this is not a fresh upstream fetch or a claim about later upstream.

Proposed minimal repair, pending lead source acceptance: change only the two
force-retry fixtures in `server_test.go` to capture argv and remove their exact
test-created journal before successful exit, failing if either step fails.
Pass the owned test path explicitly; no shared wrapper behavior, production
deletion call, real-session cleanup, recursive removal or new fixture framework.
Preserve all force, operation-ID, same-receipt and original-start-time assertions.
After ordinary command completion, assert journal absence and invoke the
existing synchronous `lifecycleOperationForSlug` reconciliation; completion
must survive that fresh proof with its same receipt/attempt and force options.
This deliberately exercises the post-completion order instead of hoping the
poller beats the background worker. Keep its worker and current deadlines.

Retain an explicit counter-case: an already-complete receipt with its matching
valid journal must reconcile to paused while retaining receipt/journal identity.
The existing matching-journal case in `operation_state_test.go:319` can be
extended narrowly for this state if useful; no production change or new test
hook is required. This proves the repair does not redefine journal ownership.
No broad lifecycle test cleanup belongs in this unit.

Verification remains hosted only. The focused source-environment selector is:

```sh
nix develop --command go -C portal test -mod=readonly ./internal/web -run \
  '^(TestDeleteOperationRetry(Uses|CanUpgrade)TheJournaledForceSetting|TestDeleteSessionRetryReachesTheRemovalJournalAfterTrackingMoved|TestMatchingDeleteJournalPreservesTheAcceptedBrowserIdentity|TestLifecycleOperationDoesNotInferDeletionFromAMissingManifest)$'
```

Then run the full affected Go web package and normal hosted D `Check` fast job,
whose package path runs the full Go suite in `nix/workspace-portal.nix:245`.
Do not manually dispatch the separate host VM job for this test-only correction.
Existing fresh-owner/CAS/attempt guards remain covered by the full package.
Run relevant formatting through the owning environment; no local test/CI suite
is authorized. A green rerun of unchanged E3 is not the proposed resolution.

If accepted, this requires a separate logical D test correction and root-owned
exact E reselection of that corrected D before new-pair hosted evidence. That
is a narrow proposed exception to the prior D51 pin hold, not an installed
package transition or authorization to change D lifecycle behavior. Root must
accept this scope before implementer edits. K's separate mock-selector failure
is outside this diagnosis. Only this design record was edited; no checks,
reproduction, CI retry/wait, refs, builds or lifecycle actions were performed.

Upstream comparison after the root's fetch confirms the diagnosis is unchanged.
From base `a2bbf2f1c588de7eec0d7d52580a89a9d4bef984` to exact default
`c51ba3c0ca0d41d237ef71c56accd564beb70a33`, `server_test.go` and
`operation_state.go` have no delta. `server.go` only adds `HostProfile` to
`teamruntime.Service` construction; retry, executor and display logic is untouched.
The D51 feature series is `c582ee7` (mediated capture leases) plus `51aba08`
(post-proof deadline and deterministic reconciliation tests). Preserve both
logical patches and add any accepted fixture correction separately.

The bounded rebase concern is shared-file/context preservation, not an upstream
fix for this test. Upstream changes `libexec/workspace-host` package-switch/
registration logic and publishes `livePackageSwitchPolicy`; the feature changes
its capture-lease dispatch/streaming path. Their shown code hunks are separate,
but preserve the full generation guard, supervised peer-loss handling and no
inherited runner guard when reconciling that file. Keep upstream live-switch
behavior intact. Both histories also edit `docs/workspace-portal.md`; retain the
upstream switch/report-helper explanation and the feature's lease/reconciliation
contracts. Root should establish patch equivalence and inspect any conflicts
after its normal owned rebase. New exact D/E heads need hosted checks and final
review records even if the feature patches are equivalent; old D51/E results
cannot certify the new upstream package composition. This is source readiness
work only and supplies no package-switch or installed-activation permission.

### First direct-start failure: atomic receipt reads and recovery (2026-10-09)

This is a source-supported repair brief for lead acceptance, not a reproduced
race or a recovery result. The exact generator was
`ab09bd437b310f57e4ff2453ec0432555d85eaca`, retained as
`/nix/store/k1yylxn5nbs5adcnhy36zpdz5sbgxgnl-source`. The sanitized evidence is
`finish-direct-isolation1-failure1.json` and
`finish-direct-failed-a-status1.json`. Installed-layout had passed; the first
isolation attempt exited 1 during A startup with `file changed while opening`
for its `processes-<run>.json`. Capacity monitoring recorded no reserve
cancellation. The later public snapshot reported `starting`, `ready: false`;
it did not prove that the runner was live or gone. `Engine#status` only calls
`live?` for phase `ready`. No B instance or screenshots were produced. The
phase's final failed checkpoint is consistent with the command failure; the
earlier watcher sample does not establish a separate checkpoint defect.

The confirmed source mechanism is in `cluster/lib/kb_state.rb:58–70`: `file`
checks an `lstat`, opens with `O_NOFOLLOW`, then refuses different device/inode
values. `State#write` publishes through a temporary file and atomic rename.
`cluster/lib/devcluster_runner.rb:95–103,169–179` republishes the process record
every 50 ms under its own mutex, while `Engine#await_ready` calls `live?` through
`process_record` (`cluster/lib/kb_runtime.rb:313–356`) outside that mutex. The
runner's own post-start `state.read(process_path)` can also overlap its tracking
thread. Thus a legitimate rename between reader `lstat` and `open` produces
the observed exception. The exact scheduling in the failed run remains an
inference: retained diagnostics show the mismatch, not the two syscall timings.

Prefer one bounded correction in `State#file`, the common inverse of atomic
`State#write`, rather than catching exceptions in `await_ready` or duplicating
a process-only reader. Permit at most three complete read attempts. Each attempt
rechecks ancestors, validates the named file as an ordinary non-symlink owned
0600 file within the existing size limit, opens with `O_NOFOLLOW`, and validates
the opened descriptor's type/UID/mode/size as well. Only when both snapshots are
safe but their device/inode pairs differ may it close that descriptor and restart
from fresh path checks. Never read or return bytes from the mismatched attempt.
The successful attempt must retain device/inode equality and the bounded
`limit + 1` read. Exhausted replacement churn raises the existing error family;
close every descriptor on success, retry and failure. No sleep, deadline
extension, configurable retry policy or background retry is needed.

Unsafe ancestors, symlinks, wrong ownership/mode/type, excessive size, open/read
errors, missing files and invalid JSON remain failures, not retry conditions.
Do not rescue `StandardError`, match exception text, return empty/stale cached
bytes, or replay any lifecycle/build/control request. Existing JSON identity,
source/digest/run/artifact checks still apply after the consistent read.
`State#lock` and resource/artifact lock acquisition retain their separate strict
open-file identity/flock checks; this repair does not authorize lock replacement
or change locking, publication, schemas or public command semantics. Atomic
record replacement may yield a complete old or new snapshot; it is not a promise
of a globally current multi-record snapshot. Existing owner locks and consumer
identity validation remain responsible for that consistency.

Implementation is bounded to `cluster/lib/kb_state.rb`, focused additions to
`tools/test-runtime.rb`, and a short owning explanation in
`cluster/runtime-contract.md`. No Engine or runner action retry is required.
Use the existing Minitest stubbing/barrier support to deterministically arrange
an actual safe atomic rename after the old `lstat` and before the real open;
do not merely invent mismatching stat objects or rely on probabilistic sleeps.
Assert the complete replacement bytes/JSON, finite attempt count and closed
descriptors. Cover repeated safe replacement followed by success, replacement
on every attempt reaching the bound, and unsafe replacement/path/mode/size
refusal. Retain missing-file, invalid-JSON and zero-limit lock-file behavior.
Use actual files/rename for the race; a narrow existing stat stub may test an
unavailable UID case without privileged ownership changes.

Add one integration regression through existing `LocalTransportEngine` and
the real fake-runner/control support: force the process-receipt interleaving
through the State reader during readiness, then establish that one preparation,
one spawn/run and the normal readiness/stop sequence suffice. This proves the
read repair without retrying lifecycle effects; it does not prove VM boot or
guest service health. Keep the existing same-slug isolation, busy admission,
lease EOF, complete-child exit and stop/resume tests. All tests are HOSTED ONLY:
the current `.github/workflows/check.yml` source path already runs
`nix develop --command bin/check --allow-missing`, including
`ruby tools/test-runtime.rb`, closure/machine/verifier tests and capture/lease
tests. Do not add a local test/evaluation campaign or another workflow. After
the repair and root-owned account documentation are committed, obtain exact
K/E composition checks and the required affected committed-source review before
new package preparation or a corrected real campaign.

Recovery of retained A is separate from accepting a new campaign. Parent first
binds the private root, instance/run/artifact, immutable launch/reservation and
process records, and reads only the recorded PIDs' current UID, boot ID, start
ticks, executable and argv. Copied PID/count values confer no authority. The
public stop path supports phase `starting`: it verifies the current runner tuple,
checks the recorded UNIX control peer via `SO_PEERCRED`, sends the exact
instance/run stop request and requires `complete: true` plus positive exit proof
for the recorded runner and all children before releasing claims/socket state.
Use only the exact packaged public `vpsfree-kb-devcluster --state-root <old-A-root>
stop same-slug --timeout <accepted-timeout>` under the parent's fresh watcher.
No process scan, group kill, manual signal, private helper, reset or force cleanup
is part of this recommendation. Preserve disks, credentials, source/launch
receipts and failed diagnostics; preserve the unrelated preview and foreign state.

G4's stop reader contains the same race. A failed stop is not permission to loop
blindly or infer completion: retain its native result and re-establish current
proof. If the read defect prevents ordinary stop, the reviewed corrected
packaged public stop can read compatible schema-2 G4 state without selecting a
new guest source: the CLI loads Software only for start/resume/update, and stop
validates the runner against its retained launch. Test that bounded compatibility
through the existing fake-runner support. Missing/ambiguous tuple or control
authority, incomplete descendants or unknown socket contents remains a refusal;
do not expand this reader repair into orphan recovery.

Do not replay the failed verifier phase or rewrite its campaign identity,
attempt/checkpoint or receipts. Current `runtime-verify.rb:195–238` binds exact
inputs and refuses an existing incomplete attempt. A failed initial startup
also lacks a proven accepted/prepared artifact for ordinary resume; ready-only
update is not its recovery path. Prefer a new private campaign root under the
corrected exact source/package selection, after owned old-A stop is proved.
Run its public installed-layout and later phases in order with fresh receipts;
old installed-layout success remains genuine G4 evidence, not new-source proof.
K68 stays the exact genuine predecessor. Reuse private configuration bytes only
with their unchanged digests and normal positive resource admission; never copy
old cluster identity into the new root. Refresh capacity for all retained old
artifacts/disks and the new campaign, and rebind actual kernel evidence to the
new projection without guessing equality. Retain old allocated state rather
than assuming reset/GC savings. A new exact E pin proves that new K composition;
no installed activation, default integration or source-metadata override follows.

Only this design record was appended. Source inspection and sanitized evidence
support the brief; no tests, reproduction, evaluation, build, process/guest
probe, control request, Git action or cleanup was performed by the architect.

### Retain incomplete G4 while verifying a disjoint campaign (2026-10-09)

The later `finish-direct-old-a-incomplete1.json` (09:44 UTC) supersedes the
old-A-stop prerequisite above. It records absence/zombie observations for the
exact retained runner and all 14 recorded children, with matching boot/UID
identities, but `processes.complete` remains false. This is not a complete
descendant inventory or shutdown proof. Keep G4's phase, claims, socket
directory, disks, credentials, roots and all campaign/launch/process receipts
untouched. Do not call it stopped, repaired, ready or cleaned. No public stop
was attempted, and the reader repair cannot supply missing completion evidence.

G4 `Engine#gone?` requires both `complete: true` and recorded process exit.
`stop_locked` cannot release claims when the first condition is false; `reset`
also requires proved stopped state. Preserve those conditions without a manual
complete flag, orphan command, signal/PID search, force cleanup or adoption.
The live-run public stop recommendation remains conditional guidance for a
different positively proved state; it is not the next operation for this snapshot.

A new corrected campaign is supported while G4 is retained. In exact G4
`cluster/lib/kb_resources.rb:61–100`, admission examines retained claims for
actual resource overlap, then performs ordinary bind probes; it does not demand
release of every unrelated reservation. The new campaign must have a new private
ordinary root and fresh instance/run identities. Use the same supported registry
selection and UID; changing `XDG_RUNTIME_DIR` to evade retained claims is not an
alternative. Runtime socket names include the canonical root, instance and run.
Both new A and B configurations must name explicit TCP forwarding ports and
integer multicast UDP ports disjoint from each other and from G4's retained
claims (and pass normal admission against all other claims and host bindings).
The same multicast group is isolated by its explicitly different UDP port;
neither the slug nor a new run label supplies that isolation. Keep local networking,
the accepted single topology, disk/RAM sizes, QEMU resolver and synthetic domains.
Do not silently allocate fallback ports or attach to an old socket/root.

The parent prepares new private A/B configuration files once, before either
instance is created, and records their actual digests and new endpoint choices
in the new campaign/capacity inputs. Existing synthetic account values may be
retained privately, but no old instance credentials or state are copied/adopted.
Keep the new B configuration byte-for-byte fixed from K68 creation through
resume and corrected-source update. Never edit G4's original config files,
campaign identity or failed attempt to turn them into a retry. Start the new
campaign at installed-layout under the exact corrected immutable package; its
success receipts are newly earned. Preserve the earlier exact K68/package/kernel
evidence with its original scope, rebinding only after actual source/config
projection and normal admission. Hosted K/E checks, affected committed review,
package preparation and the fresh watcher remain prerequisites.

Capacity must include retained G4 without assuming its unrecorded descendants
cannot write. Current free space already reflects its allocated disk/store bytes;
do not charge those bytes twice or predict cleanup/GC savings. Separately reserve
any still-unallocated growth of its 12 GiB services root and 16 GiB tank from
measured allocated extents, in addition to the new campaign's existing growth
budget and the 16 GiB base host reserve. Use the existing per-filesystem
`reserve_bytes` assessment to protect this additional retained-run allowance,
with the underlying observations recorded privately; no receipt schema or
allocator change is needed. Retained immutable images/closures stay rooted and
occupy observed store space. Preserve unknown builder scratch, assessed build
headroom and live reserve monitoring. Fresh available RAM/shm measurements must
support the new profile without assigning zero cost to unknown old descendants.
Insufficient capacity or any ordinary resource/ownership refusal blocks launch;
retention itself does not. Preserve the preview and foreign state throughout.

The incomplete receipt's cause is unresolved. A bounded private read of the
runner log found only the four source-defined Starting/Waiting messages for
services and node1: 72 bytes, SHA256
`3fb42cc5202efd66d0ba0f06fd9ec30655cf3ac527d3705c2ce1dd7cf4fab99d`.
No exception, atomic-read error or stopping/finalization line was present in
that file. `devcluster_runner.rb:175–210` normally enters its shutdown ensure,
stops machines, finishes tracking and then publishes the completion decision;
the controller's `State#file` exception does not itself prove this happened or
explain runner exit. The known atomic reader failure is independently supported
and remains the assigned repair; do not claim it explains this missing final
publication. The corrected campaign can test that narrow repair while retaining
this unresolved historical observation, and must stop for diagnosis if a new
runner/receipt failure occurs. It does not certify G4's cleanup or eliminate a
future separately scoped ownership-recovery requirement.

This clarification changes only the verification preparation prerequisite.
No runtime/cleanup feature is added, and the ongoing atomic reader repair is
unchanged. Only design.md was appended; no process/network probes, lifecycle
actions, source changes, checks, builds, refs or cleanup were performed here.

### G6 SSH discovery failure: diagnosis and bounded proposal (2026-10-09)

This brief is for lead acceptance before implementation. Exact G6 is
`7dc4d70830e535f4559bccfa668cf65cdce1de2d`, with realized source
`/nix/store/ni8i0lwsynrg273sk7najbwjn57pcqaw-source`. The source/package/hosted
and installed-layout results remain genuine, but isolation2 failed on its first
public A start. `finish-direct-isolation2-failure1.json` records the native
`command failed: ssh-keyscan` failure at phase `verifying`, after a matching
runner-ready receipt. No B/capture work occurred. The 35-byte native error
does not identify the failing machine, keyscan status or transport cause.
There was no reserve cancellation. Expected installed-layout refusal cases
are unrelated to this unexpected start failure.

Source and retained generated-network projections agree: services forwards
127.0.0.1:24200 to guest port 22 (and 24210 to 443), node1 forwards 24201 to 22,
and their socket network uses integer UDP 24220. K
`cluster/nix/test.nix:1256–1330` and pinned OS
`osvm/lib/osvm/machine_config.rb:117–127` render that mapping consistently.
The actual runner references OS source
`/nix/store/m7lppk7djkzqvrddvj0f2aa05sywl5d3-source` (locked OS `6bdf458…`).
No mapping defect is established. Do not change guest addresses, ports,
firewalls or pin inputs merely to make a retry different.

The confirmed readiness gap is narrower. OS `Machine#wait_for_boot` waits for
`current_shell.wait`, and `Shell#wait` accepts `test-shell-ready` over virtio.
NixOS `tests/configs/nixos/base.nix` orders that shell after its hvc device,
not sshd; OS `os/modules/osctl/test-shell.nix` also has no sshd dependency.
OS `os/modules/services/networking/sshd.nix` generates host keys before starting
sshd. K's runner publishes ready after these shell waits. Then
`Engine#await_ready` calls `establish_ssh_trust`, which makes one keyscan per
endpoint using `-T 5`. `Software.command` discards stderr and reduces a nonzero
status to the command name. A short SSH-readiness delay is possible; neither
this source gap nor the existing message proves that it caused this attempt's
failure. A persistent guest/service/transport problem remains possible.

The smallest SSH source correction belongs in `cluster/lib/kb_runtime.rb` and
`tools/test-runtime.rb`, with an owning runtime-contract explanation. Make
host-key discovery an explicit per-machine bounded readiness phase under the
existing operation lock and absolute monotonic readiness deadline. Pass the
deadline from `await_ready`; do not reset it per machine or retry. Keep exact
recorded endpoints, clear inappropriate inherited SSH overrides as the existing
SSH path does, and verify the same live runner/launch before attempts and before
accepting discovery. Bound each scan's `-T` by its remaining allowance (no more
than the existing five seconds), check the deadline after it returns, and sleep
only within the remaining allowance. Never accept a late success. Empty output
or failure to obtain host keys may be retried within this phase; this is a
readiness wait, not a claim that every transport failure is transient. Tool
invocation errors, identity/ownership failure, malformed or wrong-endpoint key
data and retained-key mismatch are immediate failures. A persistent transport
failure ends with its actual machine/endpoint/status and elapsed attempt facts.

Use a small SSH-specific capture of stdout/stderr/status rather than expanding
`Software.command` into a global retry framework. Retain bounded native
diagnostics privately under the owned run, excluded from capture exports; the
public error names the machine, recorded endpoint and diagnostic location/status
without copying raw banners, key material, credentials or configuration. Require
at least one valid key for every endpoint and retain their machine association.
Assemble the complete candidate known-hosts content before its first write;
no successful partial scan may publish partial trust. Existing nonempty trust
must never be replaced or enlarged to accommodate a mismatch. Preserve the
existing endpoint/key comparison, strict SSH checking, dedicated identity file,
disabled global known-hosts/config use and final guest metadata/toplevel proof.
Successful discovery is not authentication, correct-source or readiness proof
by itself. Do not retry authentication, `verify_live`, refresh/fixture mutations,
build/start/update or other lifecycle effects. Failure remains non-ready with
the original run, claims and evidence retained.

Focused hosted cases use existing isolated State/Engine and Minitest support:
valid late key arrival before the shared deadline; permanent empty/nonzero
transport result; exhausted deadline without another scan or trust write;
runner loss; malformed/wrong endpoint keys; retained key mismatch with no retry
or rewrite; one endpoint succeeds while another fails; exact per-endpoint native
diagnostics; and all-success flow reaching existing guest-identity verification
only once. Keep the existing retained-trust test and adapt its command seam
without weakening its assertions. A tiny real local delayed SSH/banner fixture
may supplement these only in hosted CI if needed; it is not a VM proof. The
current hosted `bin/check --allow-missing` already owns the relevant runtime,
process, closure and capture suites. No local tests are authorized.

Treat runner disappearance independently. The last process-receipt publication
was at 11:21:53.317 UTC, after the public command and its wrapper exited; later
observations found the recorded runner and 16 children absent. `complete` is
false, and the runner log has only Starting/Waiting messages. This establishes
neither a complete descendant list nor who ended those processes. The public
command's failure does not immediately stop its detached runner in source;
`Process.detach` reaps, but creates no separate process group or session.
The verifier and operation wrapper also inherit their execution group.
Execution-tool group/cgroup teardown is an unproved hypothesis, not a diagnosis.

For the portable retained-run contract, propose a separate, explicit small
lifetime correction for lead acceptance: establish a dedicated POSIX session
in K's runner process at entry before machine/descendant creation and before
publishing its live tuple. Use the same PID/executable/argv, no daemonizing fork,
alternate launcher, service installation or workspace API. If already its own
session leader, do not detach again; otherwise a failed `setsid` must refuse
before VM creation. Keep the Engine spawn's null stdin, owned log and closed
inherited descriptors, existing spawn/launch receipts and runner lock. A separate
session prevents inherited terminal/group signals from defining runner lifetime;
it does not escape a containing cgroup, kill-on-exit supervisor or host failure.
Do not infer that this fixes the historical disappearance. No process-group
cleanup or automatic orphan recovery accompanies it. The only new owner is
`cluster/lib/devcluster_runner.rb` plus focused hosted process tests/docs; E/D,
OSVM, state/protocol schemas and cleanup authority remain unchanged.

Test that exact runner-session establishment with controlled real subprocesses,
not merely a mocked setsid call: a short-lived controller exits or receives a
test-owned terminal/group signal; the recorded runner retains a distinct session
and stays observable until its existing owned shutdown path completes. Verify
unchanged PID/start/boot/executable/argv authority and no inherited operation/
generation/lease descriptors. Include refusal before child creation when session
establishment fails. These tests prove only their controlled POSIX lifetime
boundary. Genuine K68 remains unchanged, so the operation host must support its
retained runner too; final-code session isolation is not permission to alter the
predecessor or call its lifetime proved.

Before another real attempt, the parent should first read the existing private
`disks/{services,node1}-console.log` and `*-log.log` with bounded classification:
host-key generation/listening or sshd/service failures, NIC/address configuration,
QEMU exit status/signal and their timestamps. `OsVm::MachineLog` owns the
ACTION/qemu_exit/STATUS/TERMSIG records. Preserve hashes and avoid publishing
serial/config/seed transcripts. Missing diagnostics remain missing evidence.
If a later exact owned tuple is live, parent-authorized observations may compare
its actual QEMU `-netdev` arguments to the prepared mapping and perform bounded
read-only keyscan of only its proved endpoint, retaining per-machine native
outcome. Present-day access to 24200/24201 cannot be attributed to an absent old
runner and is not authorized by its historical receipt. No guest shell commands,
manual trust changes or control actions follow from this diagnostic proposal.

The next operation packet must also establish a durable ordinary-host execution
context whose documented lifetime retains guest runners when a CLI phase exits,
and retain relevant controller/runner PID/start/session/group/cgroup facts while
they actually exist. Do not assume an exec-tool handle or an invented background
daemon supplies that guarantee. A normal operator-owned durable context outside
workspace machinery is compatible; an executor that intentionally kills the
whole descendant cgroup on command completion is not a suitable host boundary.
This is a concrete operation prerequisite, not a new K activation framework.
Keep monitoring/cancellation scoped to recorded owned commands, and retain
uncertainty about daemons after an interrupted wrapper.

Both incomplete old campaigns remain untouched under the preceding retention
rule. Neither can be resumed, certified stopped or recycled by this correction.
Any new corrected campaign requires exact committed K/E composition, hosted
checks, affected review, immutable packages, fresh capacity including both old
retained allocations/growth, and new explicit disjoint resources. Preserve K68,
preview, all old receipts and existing first-contact/source guards. Do not use
another real replay to decide whether an unexplained failure was harmless.
Only this design was appended; no source edits, checks, evaluations, builds,
network/process probes, guest/control actions, refs or cleanup were performed.

Additional parent-provided retained evidence is now read:
`finish-direct-ssh-console-summary1.json` shows services host-key generation
finished and SSH Daemon starting, plus eth0/address/network configuration
completion; its filtered output has no SSH Daemon started line. Node1 shows
host-key generation and completed networking. These observations are compatible
with a service-readiness delay, but do not identify the failing endpoint or
establish that SSH had not started when keyscan ran. The services message about
an AF_UNIX OpenSSH server socket is not proof of the forwarded TCP listener.
The generic node mount-error excerpts do not establish an SSH-related failure
without their omitted context. Do not silently broaden this repair to mounts.
`finish-direct-ssh-lifecycle-summary1.json` contains only start actions for both
machines, no recorded qemu_exit/stop/kill result; that absence does not identify
an exit actor. The 514 watcher samples stayed above the accepted reserves
(minimum disk 223258656768, RAM 57368367104 and shm 30757490688 bytes).
The proposed source boundaries and unresolved-cause statements above are
unchanged. Captures and another campaign remain held pending the lead's source
acceptance and operation-lifetime prerequisites.

### Ordinary user-service context for the next direct campaign (2026-10-09)

Operation recommendation, not an executed experiment or certification of the
mutable correction. The implementer retains the accepted source work in
`finish-k-ssh-session-source-acceptance1.json`. Use one named transient **user
service per phase**, with the existing finite measurement/command wrapper as its
main process and `ExitType=cgroup`. This also accommodates genuine unmodified
K68, without a permanent holder, status remapping, engine interface or schema
change. The lead accepted this direction after the source finding.

Official [systemd-run v260](https://raw.githubusercontent.com/systemd/systemd/v260/man/systemd-run.xml)
documents service-manager parentage and detached execution. Use `Type=exec`,
ordinary start-job waiting and private file output. Omit scope, pipe, PTY,
wait-for-termination and collect options. Launcher success proves admission,
not the campaign result. Keep the default non-collecting failure policy.
The [v260 service contract](https://raw.githubusercontent.com/systemd/systemd/v260/man/systemd.service.xml)
defines `ExitType=cgroup` around remaining processes. `RemainAfterExit=yes`
retains a successfully emptied unit; it does not alone protect failure.
`OOMPolicy=continue` avoids a manager-initiated group stop after an OOM event;
it cannot prevent kernel or ancestor-policy kills. Resource guards remain.

The [v260 implementation](https://raw.githubusercontent.com/systemd/systemd/v260/src/core/service.c)
records the main exit result in `service_sigchld_event` (3868–3999), but skips
stopping a RUNNING cgroup-exit service while processes remain. Once empty,
`service_notify_cgroup_empty_event` and `service_enter_running` resolve its
outcome. Early main failure before RUNNING can instead enter start-post with
that failure and stop children. Close this startup corner in the finite wrapper:
before spawning the verifier, observe the exact unit as `active/running`,
`MainPID` equal to the current wrapper PID/start identity, and matching
invocation/cgroup. Bound this read-only startup wait. Failure before admission
launches no verifier, predecessor build or guest. No work belongs in service
pre/post-start, stop or failure hooks.

Invocation shape for the fresh watcher's later approved operation only:

```sh
"$SYSTEMD_RUN" --user --unit="$UNIT" --service-type=exec \
  --expand-environment=no \
  --property=ExitType=cgroup --property=RemainAfterExit=yes \
  --property=Restart=no --property=CollectMode=inactive \
  --property=KillMode=control-group --property=OOMPolicy=continue \
  --property=TimeoutStartSec=90s --property=RuntimeMaxSec=infinity \
  --property=WatchdogSec=0 --property=StopWhenUnneeded=no \
  --property=UMask=0077 --property=StandardInput=null \
  --property="StandardOutput=append:$CONTEXT/stdout.log" \
  --property="StandardError=append:$CONTEXT/stderr.log" \
  --working-directory="$ORDINARY_CWD" \
  "$ENV_BIN" -i HOME="$PRIVATE_HOME" USER="$OWNER_NAME" LOGNAME="$OWNER_NAME" \
  XDG_RUNTIME_DIR="$USER_RUNTIME_DIR" PATH="$SELECTED_PATH" \
  "$PYTHON_BIN" "$FINITE_OPERATION_WRAPPER" "$PRIVATE_OPERATION_PACKET"
```

The parent binds all executable paths and values explicitly. The private hashed
wrapper/packet identify one approved public verifier argv, exact package, phase,
campaign/config/capacity receipts and expected unique unit. Preserve the clean
verifier environment and native-result handling. The wrapper may use the user
bus for its context check; do not pass workspace authority, notification
variables or inherited control descriptors into K. The startup allowance bounds
exec/context admission, not the VM operation. The wrapper's context wait is
finite and no greater than that allowance. It exits after recording/reaping its
verification child; it does not remain alive merely to retain runners.

Before launch, bind the private ordinary CWD/context and confirm the unique unit
name is absent. Inspect existing user-manager lifetime and applicable defaults/
drop-ins. `finish-direct-host-context-facts1.json` establishes manager 260.4,
client tools 260.2 and the user-1000 manager cgroup, not logout persistence.
The manager must remain available through verification and retained B use under
existing host/session policy. If that cannot be established, hold launch; do not
enable lingering, install units/slices or change logout policy. Manager loss,
host failure, ancestor OOM policy and external administrative stops are outside
this guarantee and never authorize orphan cleanup.

Before its first child, the wrapper records effective properties and absence of
unexpected lifecycle hooks/stop dependencies, unit name, InvocationID,
ControlGroup, boot ID, UID, controller PID/start ticks, PPID, PGID/SID,
executable/argv identity and wrapper hash. Its cgroup must be under the recorded
user manager and outside the exec-tool command cgroup. Then record the verifier
child tuple and, while live, each exact K-recorded runner/machine tuple with its
actual PGID/SID/cgroup and instance/run/artifact identity. Read only named PIDs
and the exact owned unit, without a host scan. K68 may share the service group;
the corrected runner may have its own session. Neither replaces K ownership
proof. Readiness endpoint observations require positive current tuple proof.

Retain separate start-job admission, wrapper/native-child receipt and actual
verifier phase result/checkpoint. The watcher observes these files and exact
unit properties, not unit deactivation. Both successful and native-failed
controller exit leave surviving runners in the admitted cgroup. Native failure
stays failed even when ActiveState is active. Wrapper exception/signal without
a final receipt means incomplete: retain ExecMainCode/Status, Result and last
measurements without inventing a child exit. Once empty, successful units remain
active/exited and failed units retain failure state. Standard signal success
classification never supplies campaign acceptance.

The fresh watcher remains sole launcher and routine monitor. Reserve cancellation
targets only the positively proved verification child PID under its existing
brief; retain the exact action and aftermath. Never stop/kill/restart the unit
or signal its group to cancel. The ordinary
[control-group stop policy](https://raw.githubusercontent.com/systemd/systemd/v260/man/systemd.kill.xml)
would terminate remaining processes and is not a cluster recovery mechanism.
Wrapper/watcher loss requires handoff of exact unit/run facts, with no automatic
teardown, replay or inferred stopped state.

The isolation unit retains B through subsequent capture; capture receives a new
named service and accesses that B normally. Do not move its processes or rewrite
receipts. Root retains unit/context facts before and after each phase. Retirement
is a later separately authorized step only after preserving outcomes, proving
the exact unit empty with no jobs, and resolving all associated K descendant
ownership (or proving no guest/runner was ever launched). Empty cgroup or missing
PID alone does not certify an incomplete K receipt. No retirement is scheduled.

Future effective-unit/live-tuple evidence and native campaign results establish
acceptance; no local primitive trial or CI suite is added here. Exact committed
K/E hosted checks, affected review, package/kernel provenance and refreshed
measured capacity still precede launch. Retain allocations **and remaining
possible growth for both incomplete G4 and G6 campaigns**, without cleanup
credit. Their states, claims, resources, K68 provenance, preview and foreign
state stay untouched. Only this design was appended; no service creation,
process/endpoint probe, source/check/build/Git action or lifecycle control ran.

### PROPOSAL: runner control-thread shutdown ordering (2026-10-09)

Ready for lead source acceptance; not authorization for architect source edits.
Inspected exact K `a1897006c445d5622d21ca5e15a2bf3c5dc54521`, selected by E
`12749cbea88f65ee667436c558e46662e57895c9`. The four retained completed logs in
`finish-ssh-session-hosted2/{k,k-runtime,k-managed,k-runtime-managed}/full.log`
agree: runtime tests pass 63/663; machine/session tests report 8/104 with three
errors at `Engine#cleanup_socket`, through `tools/test-machine.rb:209`.
No E workflow was polled and no check was rerun.

Confirmed source facts and their limits:

- `cluster/lib/devcluster_runner.rb:154–173` calls `server.accept` outside the
  per-request rescue. Finalization publishes `complete` at 212–213, then closes
  the listener at 215, kills/joins the control thread at 216–217, and unlinks
  `control.sock` at 218. An exception from join skips that unlink.
- [Ruby 3.4 Thread documentation](https://docs.ruby-lang.org/en/3.4/Thread.html)
  establishes that joining a thread re-raises its unhandled exception.
  [Ruby 3.4.9 thread source](https://raw.githubusercontent.com/ruby/ruby/v3_4_9/thread.c)
  also defines the cross-thread closed-stream IOError. Closing the listener
  while its thread is blocked in accept can therefore terminate that thread
  before kill, with join then aborting the runner's remaining finalization.
  This is a concrete source-supported failure path, not a reproduced native
  scheduling trace or a proven explanation of the historical campaigns.
- `kb_runtime.rb:362–364,394–424` reaches the reported nonempty-directory refusal
  only after complete descendant/runner exit proof on the spawned path. Resource
  claims are released before socket cleanup. This particular exception therefore
  does not imply that claims were retained or that exit proof was incomplete.
  It does prevent the subsequent stopped-phase write. Preserve this existing
  behavior; do not expand the repair into resource-release ordering.
- The synthetic machine creates a child and ordinary markers, no machine sockets
  (`tools/test-machine.rb:317–343`), making the runner's control socket the leading
  leftover candidate. The logs do not include its actual directory inventory or
  private runner stderr, so the precise leftover and native exception are unknown.
- The body calls public stop through `shutdown` at 295. The enclosing ensure
  repeats it at 209 when phase is not stopped. A cleanup error can replace the
  initial stop exception or an earlier assertion. The displayed ensure stack
  cannot certify that the entire test body passed.

The minimal production owner is `cluster/lib/devcluster_runner.rb`: terminate
and join its existing control thread **before** closing its UNIX listener, then
unlink only the same control pathname that this runner created. Keep accepted
peer checks, request bounds, locks, owned machine stop/reap/finalize/cleanup,
process proof, signal handling and public Engine stop intact. This prevents
intentional listener closure from racing a blocked accept; it does not need an
IOError/StandardError catch around the accept loop or join. Unexpected thread
failures remain failures with diagnostics, not success. Do not manually remove
other socket entries, recursively delete the directory, change completion
authority, extend deadlines or add process/group signals. `kb_runtime.rb` needs
no production change for this proposal: its nonempty namespace refusal stays.

The test owner is existing `tools/test-machine.rb`. Preserve the first body/stop
exception and its backtrace, including Minitest assertions. Mark an explicit
shutdown attempt before invoking it; do not automatically repeat a failed stop
from ensure. If an earlier body failure requires the existing public cleanup,
report a secondary cleanup failure alongside that primary failure rather than
replacing it or treating the test as successful. Before the temporary fixture
directory disappears, capture runner/controller native diagnostics and a bounded
inventory of socket entry names/types plus the process-completion/phase facts.
Retain full diagnostics only in test-owned private evidence; expose a bounded
exception/backtrace excerpt and its evidence location/hash. Do not dump arbitrary
state/config/credential contents or claim deleted log paths remain evidence.
If these facts show a different cause, report it before widening source changes.

Hosted verification must retain the three real session cases and setsid-refusal
case, all through actual public `Engine.stop`. Add deterministic coverage in the
same fixture using its real UNIXServer and test-local synchronization: place the
control thread in the next accept after its stop response and force any
close-before-quiescence interleaving to be observed before the main thread
continues. A small fixture-local listener wrapper/barrier is sufficient; no
production injection option or generalized hook framework. Require successful
public stop, complete/gone proof, finalized/cleaned markers, stopped phase,
released claims and absent owned socket directory/control path. A test must
fail against the former ordering without depending on a lucky sleep.

Also cover primary-error plus cleanup-error reporting, and an unrelated
synthetic leftover that remains untouched while public stop refuses its nonempty
namespace. Do not weaken that negative assertion to permit arbitrary deletion,
or infer unchanged claims where current stop already released them. Keep the
ordinary session/PID/start/boot/argv/no-inherited-guard assertions and driver
tests. The focused hosted selector is
`nix develop --command ruby tools/test-machine.rb`; canonical hosted
`nix develop --command bin/check --allow-missing` already invokes runtime,
closure and machine suites at `bin/check:45–47`. Root selects exact published
K/E heads and existing required jobs; NO local tests/syntax/eval/build or VM
reproduction is part of this brief.

Compatibility is unchanged: state2, connection1, process receipts, public stop
and cleanup permissions remain the same. Root owns any concise runtime-contract
wording. This fixes future successful runner finalization; it is not recovery
authority for an already retained socket or incomplete run. G4/G6 causes remain
unknown and both campaigns, budgets, claims, disks, credentials and preview stay
untouched. Source acceptance, committed hosted evidence and affected review are
required before new package/real-campaign work. Only design.md was appended.

### K68 predecessor shutdown: unresolved compatibility boundary (2026-10-09)

This clarification holds the next real campaign, not the independently accepted
two-file runner/test repair. It inspects genuine immutable K68
`68aa33b451a14eb7bf4b2f1a090a8e5a2f80b52e` and committed K
`a1897006c445d5622d21ca5e15a2bf3c5dc54521`; no mutable correction was inspected.
There is no existing supported route established that removes this risk while
retaining the exact predecessor and all existing cleanup restrictions.

K68 `cluster/lib/devcluster_runner.rb:145–168,190–217` contains the same control
accept and close-before-kill/join-before-unlink ordering. Its actual machines do
not make the socket problem test-only. `cluster/lib/kb_machine.rb` changes disk
preparation, not stop/finalize/cleanup, and is byte-identical between these two K
revisions. K68's lock follows `vpsadmin` to OS
`6bdf458fd9105379860234ff33d352e55844f08f`. At that OS revision,
`osvm/lib/osvm/machine.rb:80,164,241` finalizes logs/shells, waits for ordinary
poweroff/reaping and removes machine shell/virtiofs sockets.
`osvm/lib/osvm/shell.rb:81` unlinks only that shell's own named socket. Those
paths neither unlink the runner's `control.sock` nor change its control thread.
Consequently the previously described failure path is reachable after real
ordinary machine stop too. Its occurrence on a future K68 run is not certain,
and no K68 guest shutdown reproduction or G4/G6 causal conclusion exists.

The current direct verifier at `tools/runtime-verify.rb:510–516` explicitly
uses old stop, old resume and then final live update. K68
`kb_runtime.rb:366–423` and committed final stop send the same stop request to
the running old process and require its complete exit proof plus empty socket
directory. Final update at 237 invokes that stop path after candidate import;
replacing the caller does not replace code inside the old runner. K68 resume
at 175–183 requires stopped state, gone proof and its exact prepared source.
Final resume cannot truthfully stand in for it. `transition-adopt` only validates
compatibility; refresh and guest SSH do not replace the host runner. A durable
systemd context addresses lifetime, not this shutdown ordering.

Keep genuine old resume, actual changed-source live update, six credentials,
disk/sentinel continuity, source identity and strict unknown-socket refusal as
acceptance requirements. Do not launch hoping the race will not occur, patch
K68 in memory/on disk, create an artificial predecessor, substitute metadata,
extend timeouts or turn a failed old stop into a passing receipt. Retrying the
same public stop after a leftover is retained cannot remove it under the current
contract. No private lifecycle call, signal, manual unlink or new orphan cleanup
is authorized by this diagnosis.

One minimal *new contract proposal*, for separate lead acceptance if exact K68
must remain the predecessor, is a final-controller **live shutdown handoff**.
Before requesting stop, authenticate the old runner through its existing exact
launch/process/SO_PEERCRED checks and record the identity of that specific live
control socket. Only after the existing complete/all-recorded-processes-gone
proof may that controller retire the same proven socket and otherwise require
an empty namespace. Unknown entries, changed socket identity, missing prior live
proof and incomplete descendants must continue to refuse. This is additional
cleanup authority and is not part of the accepted runner ordering repair.

Such a proposal needs a precise durable per-run proof and interruption/retry
contract before implementation: proof must precede the stop request, bind the
same run/launch and socket identity, and never be synthesized retrospectively
from a dead process, pathname, log or incomplete receipt. Normal lock and path
checks remain mandatory; no recursive deletion or generic orphan recovery is
implied. A stopped socket already absent follows ordinary cleanup. Existing
G4/G6 evidence cannot supply this new live proof. Do not add this mechanism merely
as a verifier exception or assume an in-memory observation survives interruption.

If accepted separately, the verifier would use that final public stop before
the genuine K68 resume, then the same supported handoff inside final live update.
This would prove K68's real resume and old-runner/new-controller compatibility;
it would **not** prove unmodified K68's own stop implementation. Record that
explicit change in command attribution rather than weakening any result. Hosted
coverage would first need the exact K68 runner with controlled machine stand-ins,
normal and leftover shutdown, interruption/retry and refusal of unproved or
changed entries; guest continuity/live closure proof still belongs to the later
real campaign. No test or operation is launched by this proposal.

Until the lead accepts a concrete supported compatibility route, predecessor
feasibility remains a prelaunch blocker. If the additional authority is outside
scope, retain the blocker and exact acceptance requirements instead of silently
substituting an old revision. Existing source repair, its hosted checks and
review can proceed independently. All pins, histories, configurations, retained
old states/resources and preview remain unchanged; only this design was appended.

### PROPOSAL: authenticated live shutdown handoff for genuine K68 (2026-10-09)

Direction accepted for this brief; application source acceptance remains with
the lead. This supersedes the preceding proposal's suggested *durable* handoff
receipt: use one operation-local proof, retained only while the existing gate
and operation locks remain held. No state/protocol schema, persistent recovery
record, verifier-only cleanup permission or new public command is needed. The
intentional limitation is that an interrupted controller cannot later recover a
dead runner's residual socket from recorded pathname/inode facts alone.

The source basis remains genuine K68
`68aa33b451a14eb7bf4b2f1a090a8e5a2f80b52e` and committed final K
`a1897006c445d5622d21ca5e15a2bf3c5dc54521`. K68's actual OSVM shutdown reaches the
same listener/thread/unlink ordering described above; future failure scheduling
is unproved. This proposal does not inspect or certify the independently frozen
two-file runner quiescence/diagnostics repair, and does not explain G4/G6.

**Single production owner and new authority.** Final
`cluster/lib/kb_runtime.rb` owns this through `stop_locked`, already shared by
public stop and update (`update:237`, `stop:379`, `stop_locked:394` at a189).
Extend its existing authenticated control path (`control:367`) once; do not
duplicate protocol authentication in the verifier. After an authenticated live
stop request and complete exit proof, the same invocation may unlink only that
runner's unchanged residual `control.sock`. This is explicitly additional
cleanup authority. Keep `cleanup_socket:417` strict and usable without a handoff
only for an empty namespace. Reset, read paths, source adoption and generic
resource release gain no socket-retirement authority.

**Proof before effects.** Under the existing nonblocking gate/operation locks,
validate the current state identity and immutable launch/reservation, including
instance, canonical state root, owner UID, run, artifact/digest and the exact
derived resource socket directory. Validate the private directory and ancestors
with existing path rules. Pin an opened ordinary owned 0700 parent directory;
check its opened and named device/inode/type/UID/mode agree. Pin the named
`control.sock` filesystem inode without following links; require a UNIX socket
owned by this UID with mode 0600 and stable opened/named device/inode/type. A
regular file, symlink, missing socket, unsafe directory, mode or owner refuses
before sending a request. Do not create, chmod, replace or repair these paths.

Keep those filesystem descriptors open through final retirement. A connected
UNIXSocket descriptor is not the filesystem socket inode. A small private
Linux-specific open helper in Engine may use `O_PATH | O_NOFOLLOW` with
close-on-exec for the socket and an ordinary no-follow directory descriptor;
Ruby accepts integer open flags. Explicitly reject a symlink by `fstat`, since
O_PATH with NOFOLLOW can open the link itself. This uses the repository's
existing x86_64-linux/proc/SO_PEERCRED platform contract, with no native dependency
or shared filesystem framework. The open inode reference prevents device/inode
reuse from turning a later socket into the original proof. See the Linux
[open contract](https://man7.org/linux/man-pages/man2/open.2.html) and
[O_PATH ABI definition](https://github.com/torvalds/linux/blob/v6.12/include/uapi/asm-generic/fcntl.h#L80-L82).
If this open cannot be established, refuse; do not fall back to a saved lstat
tuple. Close all proof descriptors on every return/error and never inherit them
into a launched process. Retain existing serialization and trusted-operator
assumptions; this is not a new hostile same-UID filesystem security model.

Before sending anything, establish the existing exact live runner proof
(`kb_process.rb:runner_matches?`: boot, UID, PID/start, executable, argv and launch
arguments). Connect to the pinned name, verify SO_PEERCRED UID/PID against that
runner, repeat live/launch and named/opened path checks, and send the existing
schema-1 instance/run/`stop` request. Require the current bounded exact accepted
response with its matching run. No protocol fields or readiness claims change.
The proof becomes usable only after this acknowledgement; request/response
errors do not create it. A runner may exit immediately after acknowledging, so
do not require it to remain live afterward. Bind the terminal receipt to the
same captured runner tuple and launch, while allowing the runner's tracked
children to grow before its final complete receipt.

**Terminal decision.** Retain the ordinary bounded `gone?` requirement: the
process record must be complete and every recorded runner/child must pass the
existing exit-identity proof. The handoff never replaces this check. After it
passes, verify the same pinned private directory/name identities again and
inspect its complete entry list. Normal machine sockets may exist during
shutdown; they confer no cleanup permission. At retirement the directory must
be empty or contain only the same pinned `control.sock`. Any other entry refuses
before the controller removes anything. If the runner already removed its
socket, ordinary strict empty-directory cleanup succeeds. If only the unchanged
owned 0600 socket remains, recheck its named/opened identity immediately before
unlinking that exact name once, then call existing strict `cleanup_socket`.
Directory replacement, socket replacement or unsafe metadata refuses. Once an
absent socket is observed, it cannot later reappear as an authorized residual.

Keep existing claim-release ordering and stopped-phase rules. At a189 resource
release follows complete/gone proof and precedes socket cleanup; a later cleanup
refusal can therefore leave claims released without marking the phase stopped.
Tests and diagnostics must describe that actual state, not promise transactional
rollback. The new helper does not delete other names, recurse, search PIDs,
signal processes, repair process completeness or accept namespace evidence from
logs. An already-dead run without this invocation's live proof follows existing
strict cleanup only; its residual socket remains a refusal.

**Interruption and retry.** The handoff is an internal nonserializable value
whose descriptors and authority end with this locked call; it cannot be supplied
through a CLI argument, state file or a later call. Keep these outcomes explicit:

| Boundary | Supported result or retry |
| --- | --- |
| Refusal before the stop request | No shutdown request; a later call may freshly prove a still-live runner. |
| Request sent but acknowledgement is missing, invalid or times out | Shutdown may have begun; refuse without residual cleanup authority or automatic request replay. |
| Valid acknowledgement followed by peer EOF | Expected shutdown transport closure; still require complete/gone and unchanged paths. This is not capture-lease EOF semantics. |
| Controller interruption or stop deadline before complete exit | Close/discard the handoff. A later call may freshly authenticate a still-live runner, or use ordinary empty-namespace cleanup after complete exit. |
| Runner dead with residual socket after handoff loss | Refuse and retain evidence. Neither matching dev/ino nor the complete receipt recreates live authentication. No new recovery command is proposed. |
| Recorded processes appear gone but their receipt is incomplete, or a path changed/unknown entry remains | Refuse; no handoff-based unlink. Existing incomplete G4/G6 records remain outside this authority. |
| Interruption after authorized unlink, before directory/phase completion | An ordinary retry may finish strict empty-directory cleanup once existing complete/gone proof still passes. |

An update uses this same call only after its existing candidate preparation is
complete. Failed stop leaves the update non-ready at its recorded stage; retry
continues only that candidate under existing rules. A dead residual with lost
handoff can block this retry. Do not claim a stopped stage, boot the candidate,
automatically roll back, substitute a previous artifact or reset the instance
to escape that refusal. This explicit limitation is preferable to adding a
persistent adoption/recovery protocol for this bounded compatibility path.

**Predecessor and source contract.** At `tools/runtime-verify.rb:510`, change only
the old-B stop selector to the final public engine for B. Keep genuine old
resume at 511 and final live changed-source update at 516. The evidence must say
"final-controller stop of K68 runner, K68 resume, final-controller update";
it must not certify K68's own stop implementation. Preserve old source metadata,
artifact, accounts/configuration, all six credentials, disk identities and
sentinels through stop/resume. Update still proves genuinely changed software
and live guest closures. Final resume cannot accept the old prepared source.
No K68 source, package, runner, metadata or argument override is permitted.

State2/connection1/control1 and disk formats remain compatible. Successful
final stop of the old run permits the old package's supported resume; final
update keeps its existing candidate/rollback restrictions. The final runner
quiescence repair remains necessary for final-code shutdown, independently of
the compatibility handoff. No OS, generic runtime or provider behavior change
is required; root owns the normal exact K/E input reselection and hosted gates.
The lasting shutdown, interruption and predecessor command-attribution contract
belongs in K `cluster/runtime-contract.md`, with root-owned concise prose.

**Hosted verification and acceptance.** Implementer scope is the Engine owner,
`tools/test-runtime.rb` and its existing `tools/fixtures/fake-kb-runner.rb` where
needed, plus the verifier call attribution in `tools/runtime-verify.rb` and
`tools/test-runtime-verify.rb`. Keep the frozen runner/test-machine repair
separate. Use actual owned subprocesses, UNIX sockets and process receipts for
the new authority tests, with bounded fixture-local synchronization rather than
sleep-dependent race reproduction or production test hooks:

- A normal owned runner removes its socket; final public stop still succeeds
  through strict cleanup. A K68-like fixture deliberately leaves only its
  authenticated control socket after complete child reaping; final public stop
  retires it and reaches stopped. This proves the handoff, not real K68 timing.
- A same-UID wrong-PID control server, wrong launch/run, bad acknowledgement,
  early EOF, missing live proof and complete=false each refuse without the new
  deletion. Unsafe directory/socket type/mode/UID validation remains mandatory;
  do not require privileged chown or compromised-operator test infrastructure.
- Preserve the original pinned inode while replacing its name with another real
  socket; also replace the parent directory in a controlled fixture. Both must
  refuse. Unknown adjacent entries refuse before either entry is unlinked.
- Interrupt an actual fixture controller after acknowledgement, preserve its
  fixture state, and prove that a second call cannot retire a dead residual.
  A fresh live retry may authenticate again; an absent-socket complete exit may
  finish existing cleanup. Exercise descriptor closure on all failure paths.
- Retain the real final-runner quiescence tests using public stop and fully
  removed owned socket directory, with original-error/private-diagnostics
  preservation. Add focused verifier command-order attribution so old stop
  cannot silently return. Existing source, closure, six-credential and disk
  assertions remain intact.

Focused hosted selectors are `nix develop --command ruby tools/test-runtime.rb`,
`nix develop --command ruby tools/test-machine.rb` and
`nix develop --command ruby tools/test-runtime-verify.rb`; the existing canonical
hosted `nix develop --command bin/check --allow-missing` retains its suite scope.
No local CI/check, standalone reproduction or runtime action is authorized here.
Root source acceptance, exact committed hosted K/E evidence and affected final
review precede package preparation and the separately watched real campaign.
That campaign must prove genuine K68 resume and actual final live update in the
owned durable execution context. Neither hosted fixtures nor this brief certify
that real result. All incomplete campaigns, claims/growth budgets, credentials,
disks/configurations and preview remain untouched. Only design.md was appended.

### PROPOSAL: SSH child authority under supported interruption (2026-10-09)

Review9's accepted source finding is recorded in
`finish-live-handoff-review9-finding1.json`; this bounded remedy is ready for
lead source acceptance, not a remediation review result. At exact K
`d1260ed1eb3aed125f11488cf1c8ce45ed384ad4`,
`cluster/lib/kb_runtime.rb:667–716` acquires the ssh-keyscan PID without an
interrupt mask, and performs successful wait, status assignment and PID clearing
as separate interruptible steps (682–685 and 703–704). Its ensure can therefore
signal a PID after the child was reaped, or miss a child whose spawn returned
before PID assignment. The late method-level ECHILD rescue does not close the
successful-reap gap. This is source-supported; no actual PID reuse, unrelated
process signal or private-campaign manifestation was observed here.

The owner is only `Engine#ssh_keyscan` and its existing tests in
`tools/test-runtime.rb`. Follow the established
`tools/runtime-verify.rb:Commands#call` mask boundaries at 50–54, 62–68 and
78–84, without modifying Commands or creating a general process abstraction.
Use `Thread.handle_interrupt(SignalException => :never)` for these complete
ownership transitions:

1. Acquire the child's pipe endpoints into cleanup-visible locals and acquire
   the spawned PID before supported interruption can be delivered. Initialize
   PID/status and cleanup references before acquisition; include each IO.pipe
   return-to-local assignment so interruption cannot lose its descriptors.
   A failed spawn grants no PID authority. Keep the existing environment, argv,
   stdin, close_others and stream routing.
2. At **every** polling or terminal wait, keep the actual waitpid2 call, result
   assignment and `pid = nil` in the same protected region. A WNOHANG nil result
   retains ownership. A successful result records its real Process::Status and
   clears signal authority before delivery of a pending SignalException. Never
   mask only a helper's wait and leave the caller's assignment unprotected.
3. Rescue ECHILD and clear PID authority **inside that same masked wait
   boundary**, then re-raise it. ECHILD is loss of child ownership, not success;
   neither cleanup nor a retry may signal that numeric PID afterward. The
   existing caller may retain its normal invocation-error diagnostics; no
   fabricated exit status or broad exception-to-success mapping is introduced.
4. Protect deadline/output-bound termination and the entire ensure cleanup:
   signal only a still-owned unreaped child, perform the existing terminal wait,
   record status and clear authority together. Put stream closure in an inner
   ensure so a reap failure cannot skip it. Close every acquired endpoint before
   leaving this protected cleanup region, including when another supported
   interruption is pending. No detached reaper or second concurrent waiter is
   introduced.

Ordinary reads/selects and the polling loop remain interruptible; do not mask the
whole discovery operation. Preserve its absolute deadline, output limits,
existing KILL-and-wait cleanup and sole-parent/reaper model. This does not promise
new kernel-level bounds on a terminal wait or cover arbitrary asynchronous
Exception subclasses, uncatchable termination or host failure. A supported
interruption still propagates after cleanup; it must not return a normal scan
result, publish SSH trust, become a retryable empty scan or be hidden as a generic
invocation error. On ordinary completion, native stdout/stderr, exitstatus,
termsig, deadline/truncation flags and private diagnostic behavior stay intact.
Unexpected synchronous errors remain failures. No generic Software.command,
runner, guest, engine lifecycle, trust/source, schema or cleanup authority changes
are included.

Hosted regressions extend the existing real owned-child tests at
`tools/test-runtime.rb:469–519`. Wrap saved real Process methods in those tests;
use bounded fixture synchronization and supported `Thread#raise(Interrupt)`,
not a synchronous `raise Interrupt` inside the wrapper, which would not test
deferred asynchronous delivery. Required cases are:

- After a real successful WNOHANG wait, queue Interrupt before the wrapper
  returns its result. Require propagation, actual child reaping, closed pipe
  endpoints and **zero** subsequent signals to that reaped PID. Instrument kill
  so a failing regression records/refuses such a call instead of sending it;
  no real PID reuse or unrelated process is needed.
- After real spawn returns, queue interruption before returning its PID to the
  caller. Require cleanup of exactly that owned child, one successful reap and
  all endpoints closed. Cover interruption at pipe acquisition without leaked
  returned descriptors using the same small fixture boundary if needed.
- Exercise the terminal wait after deadline termination, plus interruption
  during ensure's terminal reap. Queue an additional interruption there and
  prove cleanup completes without a second post-reap kill and closes all FDs.
  Keep existing deadline and output-bound assertions; do not extend timeouts.
- Exercise ECHILD at a protected wait boundary, including queued interruption,
  and require authority invalidation before unwinding and no later signal.
  Existing real native-stream/status/argv/environment and SSH trust refusal
  tests remain unchanged in meaning.

Use only test-owned children and captured IO objects; no process search, PID
reuse, guest, endpoint or lifecycle probe is required. Focused hosted selection
is `nix develop --command ruby tools/test-runtime.rb`; existing canonical hosted
`nix develop --command bin/check --allow-missing` retains coverage of related
runtime and verifier behavior. Root chooses exact committed K/E checks and
affected review after source acceptance. NO local tests, syntax/lint, eval,
build or operation is performed or authorized by this brief. This is an internal
ownership correction with no persistent compatibility or rollback migration.
Original review9 continues on its exact unchanged objects; source pins, private
campaigns, retained claims/disks/credentials and preview remain untouched. Only
this assigned design subsection was appended.

### ACCEPTED: bounded suggestion discovery for WebUI issue 30 (2026-10-09)

The user approved this continuation plan. Application implementation waits until
the accepted real portable-runtime verification and both CS/EN
`networking/ip-address-list` KB captures finish. This section records the accepted
brief only; it does not certify runtime, screenshots or a timeout correction.
The endpoint is a verified handoff with this session still active, without new
default-branch integration, deployment, activation, production KB publication,
archive or cleanup.

**Evidence and branch correction.** The source investigation at W
`ce856841a65d72648d03b6cba1748dd7dd9af048` found that
`src/pages/app/admin/ipAddresses/useProgressiveSuggestedIpQueries.ts` starts a
12-second timer before awaiting the shared capability query, but that await
does not observe its signal. Only the subsequent GET receives it. The retained
issue description is `options-suggestion-issue.md`. This establishes a source
gap, not a browser reproduction. The owning API adapter's `haveApiCall` also
awaits description/session/envelope work, so a caller-local wait around GET is
appropriate even though the GET transport already receives an AbortSignal.

The lead subsequently verified that W PR 19 was merged on
2026-10-08T18:21:58Z, with merge revision prefix `2170fd6a`, and that main
`7152729dcde326e00d16b5af0a46d0f60b431dbb` was 40 commits ahead and zero behind
the inspected availability head. The lead's exact-main content read found the
same hook bytes. These are lead-provided upstream observations, not a fresh
fetch or independent GitHub verification by this design turn. They supersede
the prior consultation's conditional stacked-PR plan. After runtime/media work,
root will freshly fetch/reverify current main and create a separate owned
`dev/ip-suggestions-timeout` branch/worktree in this session. Use one focused PR
and one logical fix commit; preserve already merged availability history and
other contributors' changes. Do not stack on, amend or rewrite PR 19.

**Implementation boundary.** Keep production changes in the existing hook file
and add a tiny hook-local abort-aware await for a supplied promise. Keep one
existing 12,000 ms caller timer for the entire query invocation: shared capability
wait plus address GET. Check the timed signal before requesting metadata, before
starting GET, and before returning rows. Await metadata through the helper;
only an unaborted successful result may proceed to GET. Pass the same timed
signal to GET and await its promise through the same helper. Do not restart the
budget after metadata and do not race a background metadata-to-GET chain whose
losing branch can continue into GET.

The helper rejects immediately for an already-aborted signal and promptly on
abort. It removes its abort listener on resolution, rejection and cancellation;
the existing finally clears the timer and parent listener. Consume late promise
resolution/rejection without another settlement or an unhandled rejection.
Final signal checks prevent a resolved promise from bypassing cancellation at
the continuation boundary. A local deadline produces an ordinary abort error,
so the suggestion becomes errored/settled and later locations can progress.
Do not turn it into TanStack's CancelledError or cancelQueries: cancellation's
state reversion is not the timeout/error contract.

Preserve query keys, five-minute staleTime for both shared metadata and
suggestions, retry 0, focus/reconnect policy, location ordering, initial two
locations, later one-at-a-time progression, three address buckets and bounded
sampling. One suggestion's timeout/cancellation must not cancel, remove,
invalidate or replace the shared `ip-address-index-capability` query/request.
Late metadata may populate that shared cache and serve another caller. The
cancelled suggestion must issue no later `/ip_addresses` GET and must not accept
late GET rows into its own query cache. Existing cached data need not be evicted.
This is a 12-second budget per query attempt, not for every location on the page
combined; later batches retain their own budgets.

Explicit retry gives each retried suggestion a fresh local budget. It reuses
fresh successful metadata; after a settled metadata failure it may start a new
lookup through normal fetchQuery semantics. If shared OPTIONS remains pending
indefinitely, retry deliberately rejoins it and still fails within its own
budget. It does not force-restart shared discovery. This accepted limitation
closes the unbounded suggestion wait without adding a shared transport deadline
or a new request-generation policy.

Successful older-API metadata without `network_enabled` continues to omit that
unsupported filter. Metadata rejection/timeout must remain an error, never a
fallback to older-API support or an empty successful result. Retain advertised
`networkEnabled: true` before the server limit and the local
`ip.network?.enabled !== false` guard. Backend admission remains authoritative.
Do not change `fetchIpAddressIndexCapability`, `haveApiCall`, the separate
`fetchAssignableIpAddresses` consumer, assignments or any other API timeout.
This brief does not claim those consumers gain bounded discovery.

Parent QueryClient cancellation/unmount keeps its existing semantics. Consuming
the query signal already permits cancellation on last-observer removal; removing
one observer must not cancel an identical query still observed elsewhere.
`enabled: false` alone is not query cancellation. Preserve the current manual
filter switch to the separate `listQ`, and ensure suggestion completion cannot
replace filtered list data. No page-wide cancellation or loading-state redesign
is required. Existing errors, partial results, retry actions and localized copy
remain the presentation contract.

**Owners and hosted verification.** Application owners are the hook and its
existing `useProgressiveSuggestedIpQueries.test.tsx`. Add meaningful fake-time
coverage with the real QueryClient, controlled metadata/GET promises and observed
query/cache state:

- Cold stalled OPTIONS settles callers at their local deadline, issues no
  address GET for those callers and allows later location batches to start.
- Metadata resolved at 11 seconds leaves only one second for GET. Separately
  cover stalled GET, a fresh metadata cache hit and already-aborted signals.
- Late resolve and late reject after timeout, explicit parent cancellation and
  last-observer unmount issue no late GET, write no late suggestion rows and
  cause no unhandled rejection. Verify cleanup of caller timers/listeners.
- Concurrent distinct suggestion keys share one capability request; cancelling
  one leaves another usable. Also retain the same-key multi-observer behavior.
  Shared late success may warm metadata for the remaining caller; do not assert
  that the shared cache remains empty.
- Preserve five-minute warm-cache reuse, successful older-API behavior, genuine
  capability errors and disabled-network guards. Cover explicit retry after
  settled failure versus bounded rejoin of still-pending metadata, later-location
  progression, partial failures and manual-filter list isolation.

Extend the already adopted
`e2e/specs/admin/network_availability.spec.ts` with one bounded scenario in EN/CS,
tagged `@pr-smoke @pr-smoke-mobile`, using the existing admin fixture and browser
clock. Show stalled OPTIONS, timeout/progression, late metadata serving a later
batch, retry recovery and usable manual filtering. Retain desktop/mobile images
of the implemented states as synthetic evidence. The older
`e2e/specs/app/ip_addresses_environment_filter.spec.ts` is deferred; do not expand
coverage adoption merely to use it. No new dependencies, runner/workflow changes,
debt/coverage allowance or copy policy belong to this correction.

Update W's owning `docs/design/API_CONTRACTS.md`, relevant networking workflow
and REQ-050/evidence text as needed, plus a dated `docs/work-log/` entry. Keep the
bounded wait, shared-request limitation and fixture evidence understandable
without session records. No route or API adapter change is planned, so no new
adapter inventory is implied. Reuse current UI wording and terminology.

The declared focused unit selector is
`npm test -- src/pages/app/admin/ipAddresses/useProgressiveSuggestedIpQueries.test.tsx`.
The existing hosted CI performs `npm run ci:quick`, `npm run ci:tests` and
`npm run build`; retain its dependency audits and Chromium script regression.
The existing Playwright smoke workflow invokes `npm run e2e:pr:desktop` and
`npm run e2e:pr:mobile` for the tagged bilingual scenario, and retains its
unchanged `npm run e2e:touch:webkit` job. No new workflow selection is needed.
These are future hosted commands, not permission for local execution: the user's
NO LOCAL CI/tests/builds constraint remains. All intended source/docs/tests must
be committed, exact-head required hosted checks must pass, and independent
committed review must complete before accepting the fix. Fixture evidence does
not certify a real API or deployment.

**Compatibility, completion and recovery.** This is an internal frontend change;
no API/schema, persistent state, backend pin or mixed-version requirement is
introduced. Older-API behavior stays intact. Reverting this client change needs
no data migration but restores the unbounded wait gap. Root owns one eventual C
pin selection for accepted final V/W sources after the planned gates, without
debugging pin churn or default-branch integration. This React correction does
not alter the PHP generator used for the two KB PNGs and does not invalidate
their truthful generating-source provenance. Root retains the authoritative
K/media/E history and verification records.

At this checkpoint only the accepted design has been appended. Real runtime and
captures remain prerequisites for starting this application unit; no source,
repo documentation, worktree/ref, check, CI, package, VM or lifecycle action was
taken by the architect. Both incomplete campaigns and their claims, budgets,
disks, credentials/configurations and the preview remain untouched. The lead
owns the final verified handoff and active-session records.

### DIAGNOSIS / continuation proposal: isolation3 and the immutable K68 predecessor (2026-10-09)

This records a failed real verification attempt and a proposed change to its
acceptance boundary. It does not authorize another campaign, lifecycle action,
source change or replacement predecessor. Current and roster17 were rechecked;
architect0 retains Astra/xhigh/workspace_write. Only this design section changed.

**Observed result and causal limit.** `finish-direct-isolation3-failure1.json`
records native exit 1 without reserve cancellation or wrapper failure. The
current-source A startup and guest attestation passed; the genuine K68 B public
start failed while reading `processes-c7d285c9-2ff7-4414-b57f-8c09650c25f5.json`.
Its private native stderr is 213 bytes, SHA256
`85f40e8670bd51c9bc220c626145d809d9079caf8db7228f316cb9d6eeb3cb30`, and reports
`file changed while opening`. The selected predecessor remains exactly
`68aa33b451a14eb7bf4b2f1a090a8e5a2f80b52e`, paired with its genuine metadata
package `/nix/store/3l8p07gyra3xfmpqsdadmlc4m3maw90i-vpsfree-kb-runtime-source.json`
and source `/nix/store/r1b23g240p4yr44f5qgh3zhaj89qjmy0-source`.

At K68 `cluster/lib/kb_state.rb:59-73`, the named-file `lstat` and opened-file
`fstat` must have identical device/inode; a safe atomic replacement refuses
immediately. `State#write` publishes by rename, and
`cluster/lib/devcluster_runner.rb:96-101,171-172` republishes the process receipt
under its own mutex every 50 ms. `Engine#await_ready` reads that receipt through
`live?`. This establishes the old reader/writer race mechanism and the precise
observed refusal. The actual scheduling of rename between those two reads is
inferred, not traced. No failure of G027's corrected reader, resource reserve,
guest attestation or service retention follows from this result.

**B was not accepted.** Allowlisted retained-file inspection found B instance
`0ebf3601-314a-49d4-989f-fa468c13fcc3`, run
`c7d285c9-2ff7-4414-b57f-8c09650c25f5`, artifact
`14ba8af0-7be0-4843-b55a-2e8fdf757d3f`, phase `starting`, a spawned receipt and
matching runner-ready receipt. Its artifact exists, but
`prepared-14ba8af0-7be0-4843-b55a-2e8fdf757d3f.json`,
`accepted-artifact.json`, `connection.json` and `update.json` are absent. No
configuration, accounts, credential contents or complete inputs objects were
read out. A has its preparation, acceptance and connection records.

`finish-direct-isolation3-live-observations1.json` supplies the parent's fresh
17:33 UTC proof: both launch runners match, and each of their 14 currently
recorded child tuples matches. Both process receipts have `complete: false`,
which is normal while live and supplies no exit proof. These observations are
separate from the earlier wrapper's ineffective tuple comparison: that code
looked for `uid`/`exe`, whereas the recorded fields are
`owner_uid`/`executable`. Do not retroactively credit its historical tuple arrays
with ownership proof or attribute B's reader refusal to this observation defect.
The independent capacity monitoring and controller/unit admission remain their
own evidence.

**No existing public continuation completes this initial start.** At K68
`cluster/lib/kb_runtime.rb:313-336`, the runner-ready marker precedes SSH trust,
live guest source/system proof, refresh, disk validation, preparation and final
artifact acceptance. Only that successful sequence writes the missing records.
The public contracts at K68 and final
`0271532264adf5eeb33123d136d9a0663faf21b0` retain these distinctions:

- `start` refuses an existing phase; it cannot replay or attach to this run.
- `resume` requires proven stopped state, an accepted artifact and complete
  matching preparation (`175-182` in K68). A final public stop would not create
  those records. Final-source resume also cannot adopt an old-source artifact.
- `update` requires a ready predecessor, unless retrying its own recorded
  candidate journal (`195-204` in K68). B has neither prerequisite. The update
  recovery call to private `await_ready` does not authorize initial-start
  recovery, and a journal must not be fabricated.
- `status`, `connection`, `refresh`, `ssh` and `transition-adopt` do not accept an
  incomplete initial artifact. A ready marker, successful manual guest probe or
  genuine old metadata file is not a substitute for the missing public contract.

There is a separate verifier boundary: G027 `tools/runtime-verify.rb:225-230`
requires matching completed phase receipts and refuses an incomplete attempt.
The B descriptor, isolation assertions, sentinels, old resume, changed-source
update, final continuity and capture phases after line 502 were not reached.
Keep the failed attempt immutable; neither a later public stop nor an ad hoc
capture makes it complete. Do not delete the attempt, relabel source selection,
copy acceptance records or call private Engine methods.

**Recommended disposition.** Preserve the failed campaign and report exact K68
start/resume/update verification as blocked. Do not retry K68 probabilistically
or add a general recovery API solely to make this verification pass. Current
G027 requires no further reader repair on this evidence. Independently useful
final-source work on the accepted A instance would require a separately accepted
operation/evidence plan using public commands; it must not be credited as this
campaign's missing isolation/update or bilingual phase. The present finalization
gate therefore remains incomplete.

A genuine later published baseline can narrow the upgrade experiment without
fabricating an old revision. Exact `d1260ed1eb3aed125f11488cf1c8ce45ed384ad4`
has the corrected reader, bounded SSH readiness and runner shutdown ordering;
its publication is recorded in
`finish-k-live-shutdown-handoff-publish1-proof.json`. The earlier published
`74b0717db8d8686d99fac51052a99908c41dad19` also has those corrections, with
hosted evidence in `finish-k-runner-shutdown-canonical-acceptance1.json`.
Neither is automatically an approved replacement: both still contain the SSH
child SignalException ownership defect. Review9 explicitly held d126
preparation for that Important finding. G027 differs from d126 only in
`cluster/lib/kb_runtime.rb` and its tests, correcting that defect. Selecting
d126 requires an explicit disposition of that known predecessor limitation;
avoiding deliberate interruption does not eliminate reserve/exception paths.
This brief does not waive the finding or recommend launching it unresolved.

If root accepts a suitable genuine historical baseline and a narrower claim,
the smallest source adjustment is the verifier's exact predecessor selection,
its corresponding tests/assertion wording and owning verification documentation.
G027 hard-codes K68 at `tools/runtime-verify.rb:15,132`; supplying another CLI
reference alone is not supported. Preserve pairing of runtime and metadata from
one exact immutable reference, current-source capture provenance, unchanged B
configuration, all six credentials/accounts/disk identities and sentinels,
positive live guest closure/import proof, and the public stop/resume/update and
lease assertions. Do not introduce source overrides, a generic predecessor
resolver, readiness adoption or lifecycle recovery framework.

The later baselines and G027 share the same lock and guest definitions, including
vpsAdmin `ebe4fab3d50a51bda1f94014ca95c73ba2a967a8`. Such a run would exercise an
actual K host-runtime change and a newly prepared, imported and attested guest
artifact, but would not prove a vpsAdmin version upgrade or K68 compatibility.
Different guest toplevels must still be observed, not inferred from revision
strings; `cluster/nix/test.nix:1319-1320` embeds artifact/source identity, so a
different toplevel alone does not imply changed application packages. This is
an explicit reduction of the earlier K68/V5d-to-final-V claim, requiring root's
acceptance before implementation. A new campaign would need a distinct root,
real paired packages, fresh exact source/config/capacity receipts and disjoint
resources; it cannot inherit the failed attempt as a successful prerequisite.

**Recovery and next gate.** If root separately chooses to stop retained B,
the supported candidate is the selected final package's public
`vpsfree-kb-devcluster --state-root <exact-campaign>/state-b stop same-slug`.
Reprove the exact current launch/runner and named tuples under the owned unit,
then let that command authenticate the live control peer and require complete
recorded-process exit before releasing resources or retiring its proved socket.
An absent live handoff or incomplete exit refuses; copied observations do not
authorize cleanup. This stops an owned run, not recovery of old acceptance, and
is not authorized by this design entry. No unit stop, reset, manual unlink,
process search, signal/group kill or claim release is proposed here.

Any accepted verifier change needs focused hosted exact-selection/no-replay and
provenance coverage, owning docs, committed review and exact K/E package evidence
before a separately admitted real phase. Correct future observation keys without
rewriting historical measurements. Account for all retained live and incomplete
allocations, including G4/G6, in any later capacity decision; preserve the preview
and foreign state. This consultation ran no checks, probes or runtime commands
and changed no application, package, ref, input or retained campaign state.

#### PROPOSAL: use genuine published 7dc4d708 for a finite runtime-only upgrade experiment

This refines the historical-baseline option above at the lead's request; it is
not source or operation acceptance. Recommend exact published
`7dc4d70830e535f4559bccfa668cf65cdce1de2d` over d126/74 for this narrower
experiment. It predates the custom `ssh_keyscan` child-management code, so the
later SignalException/reaped-PID Important does not apply to that implementation.
It already contains the bounded atomic State reader. Its actual completed
review6 and hosted evidence are retained in
`finish-atomic-review6-acceptance.json` and
`finish-atomic-k-native-acceptance6.json`; these establish the historical source
gate, not successful real startup. No patched or artificial predecessor is
needed.

The exact 7dc-to-027 diff contains eight runtime/documentation/test paths.
`flake.nix`, `flake.lock`, `cluster/nix`, fixture source, the State/Software and
resource/process contracts, disk preparation and credential layout are
unchanged. Both pin V `ebe4fab3d50a51bda1f94014ca95c73ba2a967a8`. State2,
artifact1, connection1 and the same explicit single/local 12 GiB services-root /
16 GiB tank configuration remain source-compatible. This is a real change to
K's SSH readiness, runner session/shutdown and final-controller handling, with
unchanged application pins. Successful verification may claim that exact
K-runtime upgrade, guest artifact/import/closure continuity and final-source
captures; it may not claim a V version upgrade, successful K68 startup/resume,
old-controller stop certification or universal predecessor compatibility.

Three historical limitations remain explicit:

1. At 7dc `cluster/lib/kb_runtime.rb:514-526`, trust discovery calls
   `Software.command` once per endpoint with `ssh-keyscan -T 5`; the latter uses
   ordinary `Open3.capture3` (`cluster/lib/kb_source.rb:22-26`). There is no
   bounded readiness retry. Its earlier actual G6 run failed that call
   (`finish-direct-isolation2-failure1.json`). The precise original endpoint/
   transport failure remains unknown. Initial or resumed discovery can fail
   again. A single new, explicitly accepted experiment must stop on that native
   failure; no repeated campaigns, delayed replay, fabricated acceptance,
   patched predecessor, extra readiness API or trust substitution is implied.
2. The historical runner does not establish its own POSIX session. The already
   accepted ordinary user transient service must contain its whole lifetime;
   retain exact controller/runner PID/start/PGID/SID/cgroup proof. Never stop the
   containing unit or send a process-group signal while guests may remain.
   Native phase failure remains failure even while the service retains them.
3. Its runner still closes the listener before joining the control thread
   (`devcluster_runner.rb:207-213`). Final public stop/update must own shutdown.
   Its mode-0600 socket and schema1 stop request/acknowledgement at lines145-161
   match the final authenticated handoff. Complete exit is published before
   the old listener ordering can leave the socket. The final controller can
   retire only that unchanged, pinned residual socket during the same proven
   live handoff; every unknown entry, changed path, lost peer or incomplete
   process proof still refuses. This is supported source compatibility, not a
   prediction that a real shutdown will succeed.

No additional concrete safety blocker was found in these inspected boundaries
for one finite experiment under that service and the existing ownership gates.
The known single-scan liveness risk is material: switching the baseline cannot
promise a passing run, and a failure must not turn into another probability-based
attempt. Preserve K68 isolation3 as a failed, unsupported initial-continuation
result whatever happens to this separate experiment.

**Smallest implementation boundary if accepted.** In K
`tools/runtime-verify.rb`, select exactly 7dc through `PREDECESSOR`, retain the
exact-reference equality check and paired `kb-runtime`/`runtime-source`
resolution, and replace the two K68-specific diagnostic/assertion strings with
truthful predecessor wording. Update `tools/test-runtime-verify.rb` for the
selected exact reference, rejection of K68/other references, paired outputs,
the final-stop / genuine-old-resume / final-update command sequence and native
failure/no-replay behavior. Preserve all current continuity and final capture
assertions. Add the scope/known limitations to `cluster/runtime-contract.md`;
owning workflow examples should agree if they name the predecessor. No Engine,
launcher, protocol, schema, fixture, guest source, deadline or dependency change
is required by this selection. A separate correction of the parent measurement
field names must retain the genuine receipt schema and its earlier evidentiary
limit.

All source changes must be committed and published, receive the existing hosted
source checks (`nix develop --command bin/check --allow-missing`), exact E
composition evidence after its normal K pin update, and the applicable committed
review before package preparation or a new real campaign. No local CI is
authorized. The fixed verifier phase order remains installed-layout, one
isolation/continuity/update attempt, then bilingual capture only after success.
Use a new campaign root and new immutable selection/config/capacity receipts;
never clear isolation3's attempt or carry its A acceptance into a new campaign.

**Bounded retirement proposal before allocating another pair.** To avoid
multiplying live resources, root may separately record and accept retirement of
only isolation3's exact A and B. Preserve native campaign diagnostics, the
failed attempt and a bounded private copy/checksummed inventory of the relevant
instance/run/phase/artifact/process receipts outside the two removable cluster
trees before deletion; public evidence remains sanitized. Do not copy private
inputs or credentials into tracking. The existing campaign's top-level
receipts/diagnostics and configuration files are outside those trees and remain
immutable historical evidence. Do not reuse that campaign directory.

For each explicitly selected instance, reprove its current named launch/runner
tuple and service binding; use only the final public `stop same-slug` with its
exact `--state-root`. After that command succeeds, preserve its stopped and
complete-exit evidence, then use the same final public `reset same-slug` only
if included in root's concrete retirement boundary. G027 reset
(`kb_runtime.rb:510-529`) requires stopped state and rechecks complete exit and
the owned tree; it does not require artifact acceptance. Thus initial B's
missing acceptance does not itself prevent test-owned retirement. A failed
stop, socket refusal or incomplete proof prevents reset; no force/manual cleanup
follows. Unit retirement separately requires an empty, proven owned context.

This preserves failure evidence while allowing successful public retirement to
release the two current clusters' RAM and writable disks. Do not assume reclaimed
Nix-store space or remove retained closures by hand. Reassess actual free RAM,
shared memory, disk allocation, old G4/G6 growth obligations, missing closures
and reserve monitoring before another build/start. Preserve the preview and all
G4/G6 state/claims/disks. If current A/B cannot be retired through these ordinary
proofs, do not stack another pair by assumption; report the retained-capacity
boundary. No stop/reset/unit action or source change has been taken or approved
by this architect consultation.

### DIAGNOSIS / prerequisite: isolation3 A graceful shutdown exceeded its runner budget (2026-10-09)

This supersedes the assumption that ordinary retirement of isolation3 A/B is
currently an available prerequisite for the next finite campaign. It does not
change the accepted 7dc source selection or authorize another stop, reset,
signal, guest command or campaign. Native current and roster17 again matched;
architect0 retains Astra/xhigh/workspace_write. Guidance and the documentation
skill were reused; only this assigned design file is changed.

**Observed result.** `finish-direct-isolation3-retirement-failure1.json` records
the one final public G027 A `stop --timeout 120`: native exit 1 after
17:51:26–17:53:26 UTC with `owned shutdown incomplete; processes, paths and
claims retained`. The guarded script performed no reset and no B operation.
The 213-byte private runner log (SHA256
`a5ebd8acfbf3fd64868270dc5e33d93b9f7b04dc87d5a8297f6241b761de3b9b`)
records services stop, its `OsVm::UnrecoverableTimeoutError`, then node1 stop.

The parent's `finish-direct-isolation3-after-stop-observation1.json`, at
17:54:19 UTC, records A `complete: false`, its runner gone/nonmatching, seven
matching services-side children (QEMU and six virtiofsd processes), and the
other eight recorded tuples gone. B remains live/starting with its 15 matching
tuples. These are the parent's named observations, not new architect probes.
A's retained `phase: ready` is stale phase text after a failed stop, not live
readiness or capture authority.

**Endpoint-specific shutdown evidence.** The immutable launch's actual runner
wrapper selects G027 source
`/nix/store/myqbqhvxq1p0c2kjnvxb3j68gwfmz2xm-source` and OSVM source
`/nix/store/m7lppk7djkzqvrddvj0f2aa05sywl5d3-source`. G027's effective lock is
OS `6bdf458fd9105379860234ff33d352e55844f08f`; this diagnosis uses that actual
driver, not an earlier input revision.

Narrow inspection of the recorded `services-shell.log` poweroff block found
`COMMAND: poweroff`, status 0, elapsed 0.1 s, with empty output at 17:51:26 UTC.
Its SHA256 is
`7609ffed689fd7d0c164f2dbf7f8c4a082e2989bb8ad62af67b20209cd848592`.
The services MachineLog records start and stop, without a QEMU-exit entry
(SHA256 `ae8b416a154d0d5c589c5eb5f1d71c6aa67251377e5ad01fa43a240b9e457abe`).
The parent's `finish-direct-isolation3-shutdown-log-classification1.json`
records normal stopped guest units, console-router and RabbitMQ stop jobs,
and node1 QEMU exit status 0.

Filtering only stop-job lines from the same services console, SHA256
`1ba851172f566c44a05fb6d60b39791279db36b2bdf5112f10dcb34781e173ea`, adds an
important later observation: its final lines show the console-router stop job
at **2 min 2 s through 2 min 6 s / 5 min**. The compiled services closure
`/nix/store/4qa1qvd5xq5dhz6y3krdfimq8qhrpkip-nixos-system-vpsadmin-services-26.05pre-git`
contains `vpsadmin-console-router.service` with `TimeoutSec=300`, matching
V `ebe4fab3d50a51bda1f94014ca95c73ba2a967a8`
`nixos/modules/vpsadmin/console-router.nix:167`. RabbitMQ's unit uses
`rabbitmqctl shutdown`; the recorded progress is not evidence of a fixed
106-second shutdown bound or of RabbitMQ being the final blocker.

This proves that graceful poweroff was requested successfully and a guest stop
job remained pending beyond 120 seconds. It does not establish why Puma's
console-router shutdown stalled, whether it eventually reached its 300-second
unit limit, or whether services eventually powered down. The runner's console
reader disappearing can end the host log before guest shutdown finishes. No
credentials, seed contents or raw serial transcript were exposed.

**Three different timeout/lifetime contracts.** At exact G027:

- `cluster/lib/kb_runtime.rb:473-495` sends the authenticated stop request, then
  gives the entire run one caller-supplied deadline, 120 seconds here. Expiry
  releases the call's handoff descriptors and raises; it neither signals nor
  kills the runner/guests and does not release claims or certify stopped state.
- `cluster/lib/devcluster_runner.rb:114-125` stops machines sequentially in
  reverse configuration order, with a hard-coded `machine.stop(timeout: 120)`
  for each. It catches each failure and continues. A CLI timeout increase does
  not change this budget. With multiple machines, a 120-second aggregate wait
  cannot cover multiple full 120-second machine waits plus finalization.
- OS6bdf `osvm/lib/osvm/machine.rb:164-178` first executes the guest poweroff
  command, then waits up to that machine timeout for the QEMU reaper. NixOS's
  override (`nixos_machine.rb:15-16`) is ordinary `poweroff`. The command itself
  uses the machine's default execution timeout, not the supplied reaper timeout;
  K obtains that default from startup (`devcluster_runner.rb:242`). Here the
  shell command returned in 0.1 seconds, so the recorded driver error identifies
  the reaper wait. The later matching QEMU tuple rules out a diagnosis confined
  to a reaper thread waiting after that QEMU had already exited at the observed
  checkpoint.

The controller deadline mismatch is therefore real, but it is not the only
problem. The runner's own services deadline expired while the guest still had
a configured five-minute stop job. Merely increasing public `--timeout` would
not make this run complete.

**Why the retained run cannot be repaired by another ordinary stop.** G027
`devcluster_runner.rb:198-225` finishes the machine loop, stops its tracking
thread, computes whether all recorded children are gone, writes that boolean
as `complete`, skips machine finalization when false, removes its ready/control
endpoints and returns. The observed incomplete record followed by an absent
runner and surviving services children is consistent with this ordinary source
path; no external group teardown is required to explain it. The runner's native
exit status was not retained here, so this is not a claim of observed exit 0.
Its OSVM reaper lives in that Ruby process; it cannot later finish waiting,
retire virtiofsd children or publish completion after the owner exits.

`Engine#gone?` still requires `complete: true` plus every recorded process gone
(`kb_runtime.rb:362-364`). The failed controller's live socket handoff was
ephemeral. A new caller cannot authenticate the vanished runner, turn old tuple
facts into ownership, or manufacture a complete receipt. Even later absence of
all currently listed PIDs would not establish missing final descendant proof.
Do not retry stop expecting time alone to repair it, reset, unlink sockets,
release claims, send signals or control the containing unit. G4/G6 and the
preview remain outside any new action. The separately live B does not make A
recoverable, and B retirement has not been resumed.

**Smallest next acceptance boundary.** Hold the real campaign and captures.
Before another finite experiment, root needs a separately accepted, coherent
graceful-shutdown plan whose runner machine waits and controller aggregate
budget accommodate the actual guest shutdown contract, and whose owning runner
does not relinquish its process/receipt authority while children are still
running. The bounded source owners are K's runner/public stop coordination and
its existing runtime/machine tests and contract. Do not mask the case by reducing
guest service timeouts, forcing poweroff, relaxing complete exit, changing V/OS
behavior or inventing a recovery framework. A numeric timeout alone is not a
complete design; actual guest command, sequential waits and final drain must
fit the chosen finite budget, with explicit incomplete-failure behavior.

This also reopens a concrete **prelaunch compatibility prerequisite** for the
already selected immutable 7dc predecessor: its runner has the same hard-coded
120-second machine stop and incomplete-owner exit path, and its guest service
definitions are the same. A corrected final caller cannot change that running
old runner. The accepted final socket handoff addresses an unchanged residual
socket only after complete child exit; it cannot solve this services timeout.
The future brief must close that exact historical-runner boundary through a
supported, explicitly accepted operation or revise its verification claim. This
entry neither changes the baseline nor proposes a speculative replay/pre-stop
workaround. Without that prerequisite, finishing the tiny 7dc selector edit and
passing hosted checks cannot admit the real test.

Future hosted coverage should use the existing owned-subprocess machine fixture
to retain a child past a small simulated machine/caller budget, verify failure
without complete-exit/cleanup claims, and exercise delayed graceful completion
under the accepted owner-lifetime policy. Distinguish controller expiry from
machine expiry; preserve unknown-socket and child-identity refusals and the
existing successful quiescence tests. Such tests do not prove the actual guest
service's shutdown. Any source correction requires its normal committed hosted
checks, affected review, exact package/E composition and separately admitted real
verification. It would not retroactively recover already ownerless A.

Current missing prerequisites are both an accepted shutdown/lifetime contract
for the final and genuine predecessor run, and a valid resource disposition or
fresh measured admission that accounts for retained A/B without assuming cleanup.
The accepted retirement operation failed, so its earlier capacity premise is
unmet. No new pair is admitted; all failure evidence remains intact. This
diagnosis performed only source and bounded recorded-log reads, and appended
this section. No live probe, guest command, check, build, Git mutation or
lifecycle operation was performed by the architect.

#### PROPOSAL: conditional historical service drain and retained final-runner shutdown ownership

The practical smallest continuation is a **conditional, service-drained 7dc
runtime upgrade experiment**, coupled with a narrow prospective final-runner
fix. Do not present it as an ordinary old-runtime stop pass. This proposal needs
root acceptance before source edits or operations; the frozen selector-only
unit is insufficient. Do not silently substitute final-only verification if the
historical experiment fails. A final-only handoff would explicitly omit the
cross-version proof and requires a separate acceptance decision.

**Historical boundary through existing public SSH.** Preserve the genuine
7dc runtime and paired metadata unmodified. Its public start must first succeed
normally, with accepted preparation and retained SSH trust. The verifier's
existing `descriptor('old', old_source)` proves the ready connection, exact
guest identity and actual system closure using public commands
(`tools/runtime-verify.rb:454-465`). Only then may the verifier deliberately
quiesce the dedicated services guest's **`vpsadmin-console-router.service`**
through `engine('old', 'ssh', 'services', '--', ...)`.

This is an existing public interface: `cluster/launcher.rb:76-79` holds the gate
while `Engine#ssh` uses the recorded endpoint, dedicated key and strict retained
known-hosts file. The SSH route alone does not attest readiness, so the positive
descriptor/source proof is a mandatory prerequisite, not an assumed property of
invoking SSH. Recheck the expected guest identity-file digest and
`/run/current-system` in the same remote script before issuing the stop, binding
the mutation to the already attested artifact. Keep the proof and command native
receipts private; record only source/run/artifact, unit, status and hashes in the
sanitized result.

Use ordinary `systemctl stop vpsadmin-console-router.service`, with a finite
guest-side wait (proposed 360 seconds: the actual configured 300-second service
budget plus 60 seconds for command completion/observation). A native timeout or
transport failure fails the verification phase; it does not cancel an already
queued guest job, authorize replay or claim that the unit is stopped. After
successful command completion require the exact loaded unit to be inactive/dead,
`MainPID=0` and `Result=success`. An already inactive successful unit may be
recorded as already quiescent. A timeout/failure result is not converted to a
pass merely because systemd eventually killed or removed the service. Retain
the existing watcher/controller cancellation boundary for a lost transport;
the guest command's timeout is not a promise about an arbitrarily stalled SSH
transport.

Do this once immediately before final-controller predecessor stop, and again
after genuine old resume, its fresh live-source proof and continuity checks,
immediately before final-controller live update. The second stop targets the
service restarted by the genuine resumed guest. Keep RabbitMQ, SSH, the guest
store and other services available during preparation. The same recorded
services console explicitly contains `Stopped RabbitMQ Server`; its final stop
job is console-router. Thus one named unit is the justified minimum. Do not
expand to a broad service list, broker shutdown, target isolation, unit timeout
override, kill command or guest configuration change without new evidence.

After the first drain, final public stop must still prove complete owned exit;
genuine old resume must use the same accepted artifact and preserve all six
credentials, accounts, disks and sentinels. After the second drain, final update
still imports and validates the candidate through the old live guest before
normal shutdown and direct boot. The final boot must restore the normally
enabled console-router service before captures. The old source, configuration,
closures and trust are never relabelled or patched. Source proof alone does not
certify application health, so the result must retain both drain observations
and the post-update service-health observation.

This preparation can remove the observed long-running stop job while its broker
is healthy, but that improvement has not been executed or proven. The reason
for console-router's slow shutdown remains unknown. If its standalone stop is
also slow or fails, the single finite attempt ends. Likewise the old initial
single-keyscan risk remains. Do not repeatedly launch campaigns to obtain a
passing timing outcome. The resulting claim is exactly a genuine K-runtime
upgrade with explicit guest-service preparation; V remains unchanged, and
ordinary unprepared historical stop remains unverified.

**Small final-runner ownership correction.** Keep the existing runner, locks,
control socket, process receipts and OSVM reapers; add no supervisor, force path,
orphan adoption, process schema or persistent recovery journal. Replace the
runner's hard-coded 120-second machine wait with its existing configured machine
timeout (`opts[:timeout]`, normally 900 seconds), already used as the machine
execution default. Document this as the configured machine operation budget,
not an exact upper bound on whole-cluster shutdown. The public CLI already
defaults to 900 seconds; the failed retirement explicitly selected 120. Keep a
finite caller observation deadline, and make the verifier's chosen 900-second
wait explicit. More than one machine or a command delay can exhaust that caller
budget without authorizing termination of the owner.

The essential fix is the lifetime after a machine timeout: keep the original
runner, tracker, control listener and reaper threads alive while any owned
recorded child remains. Continue ordinary `complete: false` live publications;
do not publish it as a terminal result and return. Do not reissue poweroff,
restart a machine, call a force/kill primitive or release claims. A timed-out
public controller reports failure and may leave; it does not kill this owning
runner. A later same-run public stop can authenticate the still-live controller
and wait for that **same already-requested shutdown**, without issuing another
guest poweroff. Repeated requests must acknowledge the same run without raising
another shutdown exception through finalization. Guest shutdown may remain
blocked indefinitely; preserve the owner and report non-ready rather than
inventing exit proof or autonomous recovery.

Once OSVM's original reapers have completed and fresh tracked descendant proof
shows every child gone, quiesce the tracker, recheck that proof, publish complete
exit and finish the existing listener/socket cleanup. Only that normal owner
completion lets a public controller mark stopped/release resources. On eventual
completion after caller expiry, the final runner removes its own socket; the
next controller can use ordinary complete-exit/empty-namespace proof. It must
not recreate an expired residual-socket handoff for an old dead runner.

Retaining the runner creates a necessary readiness boundary: shutdown must not
leave a live, capture-ready instance while the guest is draining. Normal public
stop must mark its existing phase record non-ready (`stopping`, schema unchanged)
after validating the owned paths/live peer and before sending the request; keep
an update's candidate journal intact. The runner must withdraw its run-ready
marker when shutdown begins,
including its existing signal path. Public connection/status/capture admission
must require that exact marker as well as their existing phase/live/source
proofs, so controller interruption or a direct runner shutdown cannot admit a
capture during continued drain. A refusal before the request is sent remains
distinguishable from a requested shutdown; no stopped/complete state is inferred
from a missing ready marker. This is confined to K's existing readiness/stop
boundaries; any unexpected adapter validation impact must return to root rather
than broaden scope implicitly.

The likely source owners are `cluster/lib/devcluster_runner.rb`, the existing
Engine stop/readiness predicates in `cluster/lib/kb_runtime.rb`, their existing
machine/runtime tests and `cluster/runtime-contract.md`. The verifier owns only
the exact historical selection, explicit timeout, two named drain steps and
truthful evidence/assertion text in `tools/runtime-verify.rb` and its tests.
Nothing in this correction updates an already-running old runner, and it cannot
recover current ownerless isolation3 A. The historical drain is necessary
precisely because the final caller cannot change 7dc's machine wait/lifetime.

**Acceptance and current-resource limits.** Hosted tests must use actual owned
subprocesses to keep a machine alive beyond a small test budget, establish that
the same runner/tracker/control authority survives caller expiry, reject capture
while draining, accept a repeated authenticated wait without another poweroff,
and finish with complete exit/empty socket only after the controlled child exits.
Preserve all existing negative identity/socket and successful quiescence cases.
Verifier tests must prove the exact two drain positions, same-command guest
identity/closure guards, clean-inactive requirements, preserved native failures,
and no stop/update/replay after failed preparation. Do not replace these with
multi-minute sleeps or claim they certify real guest shutdown.

All intended source must be committed, pass the existing hosted K/E exact-head
checks and affected independent review, and produce genuine paired immutable
packages before any new real phase. A prospective final-code stop must also be
exercised without the historical drain workaround, so the final runner's ability
to survive ordinary slow guest shutdown is not masked by fixture preparation.
Keep the explicit historical preparation claim separate in the receipt.

Current isolation3 B is **not** an eligible drain target under this proposal:
its old initial start never produced accepted preparation/connection, and this
does not authorize establishing missing trust or completing readiness. A is
ownerless/incomplete; future code cannot adopt it. Preserve A/B and all G4/G6
evidence and resources until root selects a separately supported disposition.
Any new campaign requires an explicit fresh measured capacity decision accounting
for those retained allocations, or another accepted resource plan; the former
retirement assumption cannot be reused. No additional pair, service drain,
stop/reset, capture or source edit is authorized by this proposal.

#### PROPOSAL reconciliation: shared readiness and one-shot owned shutdown

This closes the source-owner details of the preceding proposal before root
source acceptance. Inspection used immutable K
`0271532264adf5eeb33123d136d9a0663faf21b0`, its pinned OS
`6bdf458fd9105379860234ff33d352e55844f08f`, and the owned E provider/read-validator
sources. These are source findings and prospective tests, not a runtime result.
The correction requires a small explicit E consumer change; the preceding
K-only readiness wording was incomplete.

**One readiness owner.** Add public, read-only `KbRuntime::Engine#ready?` in
`cluster/lib/kb_runtime.rb`. Under each caller's existing locks, it requires the
current phase to be `ready`, the validated launch to belong to that phase's run,
the exact run's ordinary private `ready-RUN.json` with schema 1 and matching
`instance_id`, `run_id`, `artifact_id`, `artifact_sha256`, and existing
`live?(record)` runner proof. A non-ready phase or absent marker returns false;
unsafe, malformed or foreign records retain their ordinary refusal. Catch
absence only at the marker read, not around unrelated launch/artifact reads.
Do not make `live?` mean ready: it remains process liveness for initial boot,
shutdown, update preparation and compatible management of non-ready runs.

Use this predicate in K `status` (currently line 552), `connection` (581),
capture-lease admission (865-875), and its existing 0.2-second lease monitoring
loop (877). Recheck after live guest/source verification, before emitting lease
readiness, and reject subsequent loss while holding the lease. This extends
the existing cancellation path to readiness withdrawal; it cannot undo an
already accepted remote operation. Descriptor export and status are guarded
snapshots, not promises that a guest will remain ready after return.

The first, unjournaled `update` readiness requirement (204) uses the same
predicate. Its already-journaled preparation/retry still uses its existing
live/prepared-candidate proof, since its phase is intentionally non-ready.
`await_ready` must keep its separate boot-marker/SSH/closure verification before
setting the ready phase; requiring full `ready?` at its entrance would prevent
startup. At completion, check `ready?` before returning a descriptor that the
CLI reports as ready. If shutdown withdrew the marker during verification,
refuse readiness without recreating it. Retained preparation evidence is not
permission to claim a live ready run. Pure `descriptor`, shared `verify_live`,
`gone?`, and transition adoption retain their distinct existing responsibilities.

E `dev-clusters/kb/lib/portable.rb:59-60` must replace its independent
`phase == ready && live?` expression with the selected SDK's `ready?(record)`.
Keep its noncreating/nonwaiting snapshot locks and all selected-source,
prepared-artifact, canonical descriptor, controller and digest checks.
`Provider#managed_connection` supplies both managed `connection` and lease
preflight; both thereby inherit the predicate. The actual selected K public
lease still reacquires its own gate and rechecks readiness after that snapshot.
`Provider#status` already consumes K's public `ready` result and needs no second
marker parser. E inventory and `transition_adopt` must remain independent of
readiness (`live? || gone?` remains correct management proof). No change to
managed digest translation, public dispatch, lease schemas or generation guards
is needed.

Prospective E ownership is `dev-clusters/kb/lib/portable.rb`,
`test/kb_portable_test.rb`, its `test/support/kb_snapshot_fixture.rb`, and a short
link/contract clarification in `dev-clusters/kb/README.md`. The synthetic fixture
currently creates a ready phase without a run-ready marker; make it provide the
real marker fields rather than stub the new predicate. Prove that removing it
while the exact synthetic runner remains live makes canonical export refuse,
without changing files or acquiring creating locks. Retain ready success,
foreign-marker refusal, and non-ready management/inventory behavior; the trace
must include selected `ready?` and exclude lifecycle/SSH mutations. E's exact
selected K input must include this method before the consumer ships; no
fallback to the old expression or ambient reader package. This is a bounded
additional source assignment for root to accept, not an E edit in this turn.

**Existing reapers and final exit proof.** OSVM `Machine#join` at
`osvm/lib/osvm/machine.rb:154` waits on the existing `@qemu_reaper` through
`wait_for_reaper` (710), but discards that method's timeout result. Its `nil`
return is therefore not proof of completion. `running?` (254) reads the guarded
flag; the reaper (`run_qemu_reaper`, 638) clears it only after the QEMU wait and
its console/shell/virtiofs/cleanup finalization, including the reaper's ensure.
Use these existing public `join(timeout: bounded_slice)` and `running?` methods
to observe progress. Require every started machine to be no longer running AND
fresh `ProcessIdentity.gone?` proof for every retained child before finalization.
An exception or QEMU exit alone does not establish that conjunction. Keep
native machine errors visible; they do not authorize force or owner exit while
child proof remains incomplete. No OSVM source/private-thread accessor is needed.

The runner's existing `children` map (K `devcluster_runner.rb:99-108`) remains
append-only by `(pid, start_ticks)` for the entire drain. Continue discovering
descendants and publishing `complete: false`, including children first observed
after a caller or machine wait expires. Never replace that map with only the
currently attached children: a recorded child may become reparented. Once the
machine/reaper and identity conjunction holds, cooperatively quiesce and join
the tracker, take a final fresh discovery/proof under the publication mutex,
and write complete only from that same proved snapshot. If a new live child
appears, resume tracking/drain. Do not set `complete = true` and then call a
publisher that can append an unchecked child. `Engine#gone?` continues to
require complete plus actual runner and retained-child exit before release.

**One shutdown request, repeated acknowledgement.** Keep the existing control
protocol and one coordinator; no generic supervisor. Latch shutdown before
withdrawing the ready marker and before the first machine stop. An exact valid
control request still receives the same run's `accepted: true` while draining,
but cannot schedule another `ShutdownRequested` or another machine stop.
Signals use the same one-shot notification path. Preserve invalid-peer/request
refusal. Withdraw readiness before guest drain, including signal-origin drain
where the engine phase can remain `ready`; do not let the startup path publish
the marker again once shutdown is latched.

The coordinator/ensure boundary must close an already queued notification too.
A minimal implementation can mask only `ShutdownRequested` around finalization,
allow it in the normal startup/run body, latch drain and quiesce/join its one-shot
notifier, then consume any already queued notification in a narrow rescue before
machine drain. Control requests after that point only acknowledge. Do not allow
a pending notification to surface on leaving the protected drain, replace a
primary exception, or interrupt receipt/listener cleanup. Signal handlers must
not acquire an ordinary Ruby mutex in trap context. This is confined to the
existing runner's notification and finalization code, not a general asynchronous
exception facility.

Each started, still-running machine receives at most one graceful `stop`; mark
that attempt before invoking it. A machine already proved stopped is never
stopped again. OSVM `Shell#execute` (`osvm/lib/osvm/shell.rb:133-135`) can start a
non-running machine, so repeated `stop` is not a harmless polling operation.
After timeout, use only the reaper/identity observations above. Finalize and
close the existing control listener/socket only after complete exit proof, with
the already accepted join-before-listener-close ordering. No socket deletion,
claim release or terminal incomplete runner exit replaces that proof.

**Budgets and deterministic verification.** The verifier explicitly passes
`--timeout 900` to its public stop/update waits. This is a finite controller
observation budget, not a cluster shutdown guarantee: two sequential configured
machine reaper waits can each consume 900 seconds, and guest `poweroff` command
execution uses its separate existing shell budget. `stop_locked` starts its
observation deadline after the control handshake; update also has build/import
and readiness stages. Do not describe any of these as a whole-command 900-second
limit. A caller timeout remains a native failed phase, with the live draining
runner and claims retained; it does not cancel or retry the shutdown.

Keep both historical console-router drains individually finite (the proposed
360-second service-command bound), with bounded public-command/transport
observation and separate native exit/timeout diagnostics. A transport timeout
does not prove the remote stop job was cancelled. Require the recorded clean
inactive result before proceeding; no stop/update follows a failed drain.
These guards must not inherit an unlimited wait merely because the final
runner can preserve ownership beyond its caller's budget.

The committed verifier's `Commands#call` has no elapsed-command deadline; its
ten-second deadline belongs only to interrupted-child reaping. Consequently the
drain needs an explicit, narrow prospective addition there: an optional monotonic
360-second caller limit used only for each named public SSH drain, alongside the
guest's 360-second command bound. Charge transport/handshake time to the caller
limit. On expiry record the deadline outcome, use the existing sole-child
ownership/reaper cleanup for the spawned public command only, retain its actual
exit/signal and private stdout/stderr, and fail the phase. Do not report that
observer expiry as a native guest-service timeout or claim any remote child/job
was cancelled. Other commands retain their existing behavior. This requires no
new transport, process-group authority or general timeout subsystem.

Extend existing hosted K machine/runtime tests with controlled real child/pipe
barriers, not long sleeps: keep the same runner alive after short caller and
machine deadlines; discover and retain a later child; model `join` timeout while
`running?` stays true; prove no complete receipt or cleanup until reaper and all
child predicates pass. Repeat valid control requests and TERM/INT during drain,
including a queued notification at the run/ensure boundary, and assert one
poweroff per started machine, no restart, no lost primary error, continued
receipt publication, and ordinary complete/empty-socket completion. Cover marker
loss with phase still ready and runner live through K status/connection, lease
admission and active-lease cancellation, plus the selected E snapshot test above.
Retain successful startup/resume/update and authenticated historical handoff
tests, wrong/unsafe marker tests, and all strict incomplete/unknown-socket cases.
Verifier tests assert explicit public timeouts and both finite drain boundaries;
no test silently retries a failed phase.

K owns the implementation/contract and its existing machine/runtime/verifier
tests; E consumes the selected readiness API as specified. Existing hosted
K/E package and source checks plus committed affected independent review remain
prerequisites to any new real phase. This adds no state, connection or control
schema and grants no retrospective recovery. Older callers do not acquire the
new readiness guarantee merely by reading retained state; deploy/select K and
its E consumer together through the already accepted source/pin process, without
implying installed activation. Current ownerless A, incomplete B, G4/G6 and
preview remain untouched. Root must separately accept source and any subsequent
operation; only this design record changed here.

#### DIAGNOSIS / PROPOSAL: discover children of every owned process task

This is a bounded repair proposal for root source acceptance, based on committed
K `3bb675f1e730ee9f18416363f6700f4000e44d0c` (tree
`9abba73b14f58b9c5d177387b058ec86b15fa41b`). It preserves the accepted readiness,
one-shot shutdown, reaper and final publication design above. No application
edit, local reproduction, hosted rerun or real operation was performed here.

**Observed failure and source explanation.** Retained Managed run
`37980015479` failed on this exact head. Its native `full.log:161-197` records
both delayed-shutdown cases timing out at `tools/test-machine.rb:246`, waiting
for the reported late child to enter the process receipt. Runtime 86/1116 and
closure 12/51 passed; machine 15/398 has two errors. The evidence is in
`finish-k-shutdown-owner-managed-failure1/`, whose receipt records full-log SHA256
`e66da56df35dfde4ec760749073f5c6fca0974ddf7d33d1d97a241ddf5a16b48`.
Do not relabel that native failure or infer a passing source gate.

`SessionMachine#stop` creates its command worker at test-machine lines 767-794.
The `late` command spawns the real child on that worker (772), reports its PID,
and keeps it alive on a pipe. The test receives that response before it waits
for discovery (243-250). Production `ProcessIdentity.children` at
`cluster/lib/kb_process.rb:42-45` reads only
`/proc/PID/task/PID/children`; `descendants` recursively repeats that restriction.
Runner tracking and final proof call it at `devcluster_runner.rb:104-112`,
187-198 and 253-278. A persistent child of a different task is outside that
enumeration; neither a longer timeout nor moving the test's spawn to the main
thread repairs the ownership blind spot.

The kernel documents `children` as the immediate children of the selected
PID/TID task, not the entire thread group. Normal fork assigns the creating
task as the parent; the kernel reader walks that task's child list. See the
[kernel proc documentation](https://www.kernel.org/doc/html/latest/filesystems/proc.html#proc-pid-task-tid-children-information-about-task-children),
[Linux v6.12 fork parent linkage](https://github.com/torvalds/linux/blob/v6.12/kernel/fork.c#L2352-L2416),
and [v6.12 proc child reader](https://github.com/torvalds/linux/blob/v6.12/fs/proc/array.c#L679-L731).
Together with the held worker/child, these establish the source mechanism
explaining the observed wait. No retained kernel task snapshot or new runtime
reproduction was obtained; exact historical scheduling is not claimed.

**Real driver boundary.** The selected OS revision remains
`6bdf458fd9105379860234ff33d352e55844f08f`. Its `Machine#start` spawns QEMU at
`osvm/lib/osvm/machine.rb:134` and virtiofsd through `start_virtiofs` (606-619) on
the calling thread. K currently calls `entry.machine.start` synchronously from
its main startup path (`devcluster_runner.rb:338-347`). OSVM's reaper and console
threads in the inspected source do not themselves spawn these processes.
Thus this inspection does not establish that current initial QEMU/virtiofs
launches were omitted in any real campaign. OSVM does not require its caller to
be the main thread, and the recursive ownership helper must support children
of worker tasks in a reached process. The test is exercising a real Linux
process-discovery obligation, not an invented OSVM method. No OSVM change is
needed; nothing here diagnoses earlier incomplete campaigns.

**Minimal discovery change.** Keep the public result as ordinary process
identity records, with no receipt or protocol schema change:

- In `kb_process.rb`, enumerate the numeric task IDs under the particular
  reached process's `/proc/PID/task`, read every listed
  `/proc/PID/task/TID/children`, and union/deduplicate their child PIDs. Use an
  enumerator that exposes directory-read errors; a glob that silently returns
  no entries is not a substitute. Validate numeric IDs before constructing
  paths. Task IDs themselves are not child-process receipt entries.
- Apply this at **each** recursive level, not only the runner. Resolve children
  through the existing identity reader; preserve boot/start ticks, UID,
  executable and argv rules and all `matches?`, `gone?`, runner and launch
  checks. Keep a per-traversal visited identity set so reparenting/duplicate
  observations do not create repeated recursion or duplicate records. Do not
  follow a PID whose observed parent/child identity has changed into a different
  process; use the captured identity when checking a recursive descent. An
  uncertain observation supplies no new control or cleanup authority.
- Start only at the exact owned runner and recursively reached child processes.
  Never enumerate `/proc` globally, scan by executable/name/UID, adopt a sibling,
  replace ownership with PGID/cgroup membership, or signal a discovered PID.
  Keep the runner's append-only `(pid, start_ticks)` map and final
  discovery/proof/publication mutex unchanged.

**Missing tasks and limits.** A listed task can exit before its child file is
opened. Tolerate only that specific vanished-task `ENOENT`/`ESRCH`; retain the
children already collected from other tasks. Do not turn a failure anywhere in
the aggregate into `[]`. If the task still exists but its `children` file is
unavailable, refuse the observation. The file depends on
[CONFIG_PROC_CHILDREN](https://github.com/torvalds/linux/blob/v6.12/fs/proc/base.c#L3477-L3482);
unsupported procfs, permission errors, malformed IDs or missing task data for a
still-live owned root must not masquerade as an empty tree. A disappearing
recursive process is handled only as an exit observation of that captured
identity, never as permission to traverse a reused PID or forget an already
recorded descendant. Retain existing records and refusal semantics on uncertainty.

There is a second concrete limitation in the old helper: its blanket `ENOENT`
rescue conflates an exited task with an unsupported/missing `children` file on
a live task. The distinction above belongs to this same helper repair. Initial
runner discovery occurs before machine creation, so an unsupported root procfs
must fail there. A later discovery error cannot certify complete exit or release
claims. Existing runner discovery exceptions can propagate; this proposal does
not claim that arbitrary procfs failure preserves a functioning owner, nor add
a new recovery/supervisor path. If implementation needs changed error-lifetime
behavior beyond the accepted ordinary task-exit handling, return that concrete
boundary to root before expanding source scope.

All-thread enumeration is still a sequence of procfs observations. The kernel
warns that concurrent exits can skip children. A thread disappearing and
reparenting children to an already observed task can likewise change a pass;
short-lived processes may exit between passes. Keep normal ongoing tracking,
positive OSVM reaper completion and final identity proof; do not call one empty
scan an atomic completeness certificate. Preserve every already observed child
through reparenting. This bounded fix does not establish complete history for
arbitrary daemonization, leader death or processes escaping before observation,
and does not introduce freezing, subreapers, PID searches or adoption. An
interrupted observation cannot publish `complete: true`; previous durable
receipts and claims remain the authority. This does not strengthen any old
incomplete receipt retrospectively.

**Hosted verification and owners.** Production ownership should remain
`cluster/lib/kb_process.rb`; extend existing `tools/test-runtime.rb` and preserve
both failing `tools/test-machine.rb` cases, adding only focused evidence where
needed. Keep the late spawn on its real worker, the unchanged five-second test
guard, retained-original-runner assertions, repeated control/signal coverage and
actual public stop. Do not add sleep/retry allowances or replace process evidence
with mocked machine completion.

Add a barrier-controlled owned process test: one child is spawned by a worker
that remains alive; within that child a worker spawns a grandchild and remains
alive. Assert exact identities from both levels, no thread-ID records, no
duplicates, and exclusion of a separately owned sibling outside the selected
root. Release/reap only fixture-owned children normally after assertions. Cover
task disappearance between enumeration and read without losing another task's
held child, plus live-task missing child file, permission/malformed refusal and
identity change using narrow existing test stubs/barriers. These are targeted
normal-procfs race tests, not compromised-operator filesystem tests. Preserve
the late child's receipt until it is proved gone, even after the original
machine reaper finishes; the final runner must then clean through its ordinary
public stop proof.

The existing hosted `bin/check` owns `ruby tools/test-runtime.rb` and
`ruby tools/test-machine.rb`; run those through the declared Nix/OSVM environment
as part of the exact-head hosted source checks, with the other retained suites.
No new runner, dependency, workflow or local CI is required. Add a short owning
runtime-contract qualifier about all-task discovery and its non-atomic limits;
root owns that prose and source disposition. E needs only its normal exact K
selection when root publishes the correction, not a second discovery engine.
All source/hosted/committed affected-review/package gates still precede real
work. No new campaign, retry, cleanup or action against isolation3 A/B, G4/G6 or
preview follows from this diagnosis.

**Follow-up: observed task disappearance cannot complete a final pass.** Linux
first reparents an exiting task's children to another live thread in the same
process when one exists, and moves the child list to that reaper. That thread
may already have been visited. See
[v6.12 exit/reparenting](https://github.com/torvalds/linux/blob/v6.12/kernel/exit.c#L584-L684).
Consequently, tolerating a vanished TID means continuing to retain/discover
records; it must not mean certifying that pass as complete. This tightens the
preceding missing-task paragraph without claiming an atomic tree snapshot.

Use a small **in-memory per-pass observed-disappearance flag**, alongside the
collected identity records. A genuinely vanished listed task/process, or a
changed task-ID set seen by a bounded before/after enumeration of that reached
process, sets the flag. Continue merging observed child records into the
append-only map. No scan retry loop is needed: the existing tracker/drain loop
already performs its next observation. Unexpected permission, malformed or
live-task missing-file errors remain explicit refusals, not ordinary
disappearance or an empty successful result.

The one production consumer is `devcluster_runner.rb:105`. Its existing
discovery closure must carry that local flag to both completion decisions
(253-277): a pass with an observed disappearance cannot authorize finalization
or `complete: true`, even if all previously recorded children are gone. Keep
the same runner/tracker, non-ready state and `complete: false`; proceed through
the existing drain observation path. After tracker quiescence, apply the same
rule to final discovery under the mutex and resume tracking if it cannot
support completion. Preserve the machine `!running?` and retained-child exit
conjunction; absence of this flag is only an additional condition, never a
replacement for that proof. This requires a small explicit runner call-site
change in addition to `kb_process.rb`, not a new persisted record, framework or
discovery service. Root source acceptance must include that boundary.

Deterministically exercise the interleaving with an owned worker/pipe barrier:
the parent task's child list has already been read, the worker has spawned a
held child, then the worker exits before its own child file is read. Assert that
the pass is marked inconclusive, other collected identities survive, and no
complete publication/finalization occurs. The next ordinary pass must discover
the still-live reparented child, which remains recorded until its exact exit.
Also cover a task-set change detected after reading the lists, distinct from a
live task whose child file cannot be read. Deduplicate by actual PID/start
identity and retain the existing nested-worker and public-stop fixtures.

The runner's mutex serializes its Ruby map/publication, not kernel forks or
reparenting. Two task enumerations still cannot detect all transient changes,
PID/TID reuse or escaping descendants; no global snapshot or historical-tree
guarantee follows. Existing owned-machine lifecycle/reaper proof and the stated
unsupported escape/leader-loss boundaries remain necessary. No freeze, host-wide
scan, adopted process, new deadline, test retry or real operation is proposed.

**Order reconciliation: quiesced proof before runner-invoked cleanup.** The
immutable K `3bb675f1e730ee9f18416363f6700f4000e44d0c` listing read for this
investigation confirms the implementation gap. In
`cluster/lib/devcluster_runner.rb:253-283`, the first conjunction is followed by
tracker quiescence/join (262-263), machine `finalize`/`cleanup` (264-273), and only
then another discovery/proof (275-279). Adding the disappearance condition to
those two existing conjunctions alone is insufficient: the second refusal
arrives after cleanup. This clarification supersedes that placement in the
previous follow-up; it does not certify the mutable correction draft.

Keep one existing drain loop and use this explicit order:

1. Observe reaper progress as already specified. Under the publication mutex,
   discover/merge identities and publish `complete: false`. The initial
   candidate condition is no observed-disappearance flag for this pass, every
   started machine `!running?`, and every retained child `gone?`. If it fails,
   continue the existing drain path with the tracker running.
2. Set `tracking = false` under that mutex and join the existing tracker outside
   it, preserving the current cooperative quiescence. Do not finalize machines
   or touch their cleanup resources yet.
3. **Before the `unless finalized` block**, take a new discovery/merge and full
   candidate proof under the same mutex, still publishing false. This pass has
   its own observed-disappearance result; do not reuse the earlier flag or exit
   verdict. If it is inconclusive, restore tracking/start the existing tracker
   once and continue the same drain loop. Neither `Machine#finalize` nor
   `Machine#cleanup` may have been called by this runner attempt at that point.
4. Only a successful quiesced proof admits the existing once-only machine
   finalization/cleanup block. Keep that block outside the publication mutex,
   with the tracker quiescent; do not hold the mutex across potentially blocking
   driver code. Preserve current error reporting and the existing `finalized`
   guard, so a subsequent observation does not repeat cleanup or poweroff.
5. Retain the existing **post-cleanup** discovery and full proof under the mutex.
   Write `complete: true` only if this new pass again has no observed
   disappearance, all started machines remain non-running, and every retained
   child is proved gone. Otherwise write false, restart tracking once and
   continue the same drain loop, retaining the once-only finalization state.
   This check cannot undo earlier cleanup; it prevents publishing completion
   from evidence that became insufficient afterward.
6. Only successful post-cleanup publication reaches the existing control-thread
   join, listener/socket shutdown and runner exit. Controller `gone?`, strict
   socket cleanup and claim-release authority remain unchanged.

This is a bounded insertion/reordering in the runner's existing shutdown tail,
roughly lines 253-283, plus the already proposed discovery result plumbing at
104-112. It adds a pre-cleanup quiesced observation; it neither removes the
post-cleanup guard nor adds another retry/drain loop. It does not reorder OSVM's
own reaper internals: the guarded calls here are K's explicit
`Machine#finalize`/`Machine#cleanup` calls, after the existing public machine and
identity proof. A discovery error is not permission to cross either boundary.
No new process authority, receipt format, deadline, generic supervisor or OSVM
change is required. The mutex still does not make kernel process discovery
atomic; the preceding limitations remain explicit.

Add a separate deterministic hosted runner regression using the existing owned
process fixture and a fixture-only barrier at tracker join / next main-thread
discovery. Let the initial candidate proof succeed, then make precisely the
first post-quiescence observation report a task disappearance. Before allowing
another observation, assert that the runner/control authority remains, the
receipt is false, the tracker resumes, and both finalization and cleanup call
records are absent. A companion held-child variant puts a real late worker
child into that quiesced observation and requires its identity to remain
recorded until normal fixture-owned exit. Both variants must eventually finish
through actual public stop, with one finalization/cleanup attempt per machine.

Also exercise an inconclusive post-cleanup observation: it must leave the
receipt false and the control owner alive, resume tracking, and later complete
without repeating already-attempted finalization. Assert event ordering, not
only the final presence of files. Use bounded pipe/barrier handshakes and narrow
fixture method wrapping, without production test hooks or multi-second sleeps.
Preserve byte-for-byte both existing failed delayed-child test methods and
their shared `delayed_shutdown` path, including its five-second guard; place
the new ordering cases separately. All tests remain hosted-only under the
existing declared K machine/runtime check route. Root owns source acceptance,
hosted selection, affected review and any eventual operation; this design-only
clarification leaves application drafts, all private campaigns and preview
unchanged.

### Separate screenshot operation and proportionate smoke fallback (2026-10-10)

This bounded operation proposal supersedes coupling the two KB images to the
finite historical upgrade/isolation campaign. It does not delete that campaign's
accepted criteria or report them passed. Following the user's further objection
to the remaining resource cost, recommend **no-new-VM smoke first**, with live
checks conditional on a separately proved existing environment. Canonical PNGs
remain pending unless their full capture contract can actually be satisfied.
The lead selects the operation; this section authorizes no launch or cleanup.

Source evidence is immutable K `922e71e5eb75b6eb416bf55e39160e9a7236e654`, selected
by E `2c1d3e86435292303f9c2f3f3386dc90e6b9efd0`:
`finish-stop-waiter-step9-acceptance.json` and
`finish-direct-package-realize5-acceptance.json`. Its source is
`/nix/store/6zgfm2h7wipl6ba0bqrfh03qk1lymwiq-source`; metadata is
`/nix/store/0k3n1hhck9br6663zlwppjvqrh1hhwhk-vpsfree-kb-runtime-source.json`.
It pins V `ebe4fab3d50a51bda1f94014ca95c73ba2a967a8`, including the final PHP UI
and policy-error work. The accepted package/source receipt is not guest proof.
Owning guidance already supports single-topology `ip-inventory` captures in
`docs/webui-change-workflow.md`; `cluster/runtime-contract.md` remains the
authority for runtime, source, readiness, leases and output ownership.

#### Options and their actual evidence

| Option | Smallest useful operation | Evidence and limit |
| --- | --- | --- |
| Installed package smoke, recommended now | In a new private ordinary directory, use the exact realized runtime/capture wrappers for help, noncreating status of an absent slug, and one missing-connection capture refusal. Preserve native exits and private output placement. | Exercises installed paths and refusal before fixtures without guests or new guest images. Does not prove boot, live API/PHP, allocation, leases on a live cluster, or PNG correctness. |
| Read-only live API/PHP smoke, conditional | Use an already owned reachable environment only after the lead proves its actual source, endpoint/trust and existing account authority. Inspect current-user/network/IP responses and the PHP IP list with existing data and sessions. | Can prove the observed API/PHP behavior at that exact source. Missing disabled/assigned rows mean those cases are untested. A read-only smoke cannot prove write rejection/atomicity; retain the accepted hosted V tests for those cases. No fixture provisioning, preview writes, runtime adoption or image publication. |
| Canonical CS/EN images, optional separate operation | One fresh final-source single/local cluster, or an already existing fully compatible exact-source cluster with all normal ownership/readiness/lease/fixture authority established. Use the public sequence below. | Proves the two real canonical bitmaps and the exercised initial-start/capture path only. It does not prove historical update, two-root isolation, cold continuity, all-six-credential persistence across update, or the rest of the finite campaign. |

The supplied facts do **not** establish an existing ready G922 environment.
The retained G4/G6/isolation3 resources are not substitutes; old live or copied
tuple evidence cannot establish current readiness. Preview source/readiness is
not established by this design and preview remains unchanged. Thus package
smoke is immediately specifiable; live smoke needs a concrete positive target
proof, and canonical captures need more than a reachable old page. Existing
accepted V/W/K/E hosted suites remain valid at their recorded heads: do not
rerun a broad suite or construct a new framework to relabel them as smoke.

For the finite package smoke, reuse the selected clean PATH/environment and
exact packages below. Run runtime and capture `--help`; then
`vpsfree-kb-devcluster --state-root "$SMOKE_STATE" status absent --json` against
an intentionally absent fresh state root. Expect native 0, `found:false`, and
no state initialization. From an existing private ordinary output CWD, run
`vpsfree-kb-capture --connection "$ABSENT_CONNECTION" --language en
--checkpoint networking/ip-address-list`; expect native 1 before any fixture or
browser activity, no published PNG/results, and only the package's private
artifact-lock/scratch output. That negative case is expected refusal, not a
successful capture. Preserve source/metadata hashes and exact native results in
one smoke receipt. It is sufficient to reuse an already accepted exact-head
observation of these same facts; no duplicate test campaign is required. Do not
invoke `vpsfree-kb-verify` or manufacture its phase/attempt receipts.

#### Resource reduction supported by source, and its limits

K `cluster/nix/test.nix:73–75,1907–1925,1969–1975` exposes services
`memoryMiB`, `rootDiskMiB`, node `memoryMiB` and `tankDiskGiB`. Public `start`
merges the explicit config; it does not enforce the verifier's 4096/4096 MiB,
12288 MiB root and 16 GiB tank profile. Those exact checks belong to
`tools/runtime-verify.rb:179–180`, not a universal engine minimum. The pinned
OS `tests/make-test.nix:253–266` builds a raw services image of the requested
size with the guest store included; `tests/configs/nixos/test-vm.nix` disables
mounting the host store. OS's generic default RAM or image `auto` sizing is not
evidence that this API/database/RabbitMQ/PHP guest fits or has sufficient
writable headroom. No smaller operationally qualified full profile is
established here. Do not select guessed 2 GiB RAM or 4/8 GiB disks to obtain a
nominal saving and then begin another build/boot qualification campaign.

The existing minimal fixture itself is exact: `fixtures/prepare.cjs:544–545`
requires one real VPS with one CPU, 1024 MiB RAM, zero swap and 4096 MiB disk
quota. `prepareFixtures` takes its separate `ip-inventory` branch and
`scenarios/networking.cjs` skips unrelated navigation. It needs services and
node1; no NAS/backuper/traffic fixture is needed. A smaller node must still
support that real VPS, its template, ZFS space/quota and node services. A 4 GiB
VPS quota is neither measured host allocation nor a sufficient tank size.
Lowering the fixed fixture resources, dropping the actual assigned address,
mocking the page, or replacing the guest store would be substantive new scope.
The smoke fallback avoids all such changes.

For the optional existing single-cluster profile, retain 4+4 GiB guest RAM,
12 GiB services root and explicit 16 GiB node tank. The disk formula for one
fresh instance is **2R + T = 40 GiB** of eventual image/root/tank extents:

- One 12 GiB immutable raw services image. New instance credentials/identity
  affect its closure; do not presume an earlier instance's image is reusable.
- One distinct 12 GiB writable root. K `cluster/lib/kb_machine.rb:prepare_disks`
  uses `IO.copy_stream`, so do not assume a sparse/reflink copy.
- One 16 GiB sparse tank, created by pinned OS `Machine#prepare_disks` using
  `truncate`; retain its remaining possible growth. The VPS/template occupies
  this tank, so its 4 GiB quota is not another host image charge.

This replaces the full campaign's three images, two roots and two tanks
(92 GiB) for **this screenshot operation only**. It saves 52 GiB of that
eventual-output envelope and halves the new guest RAM/shm peak to 8 GiB. It
does not establish that 40 GiB is the mathematical minimum or a universal
free-space prerequisite for screenshots.

`finish-direct-capacity-observation5.json` identifies state, store and daemon
scratch on the same device. Four retained tanks have 68,713,852,928 bytes of
unallocated possible growth; their already allocated roots are already
reflected in free space. Preserve that roughly 64 GiB obligation and the
existing 16 GiB host reserve. With the fresh 40 GiB envelope the known combined
requirement is about **120 GiB**, rather than 172 GiB, before missing closures
and temporary build use. Against the later blocker measurement of
178,829,410,304 free bytes (166.55 GiB), this leaves about **46.55 GiB** to
assess for those costs. This is arithmetic on recorded observations, **not
launch admission or a newly imposed 120 GiB screenshot floor**. The roughly
80 GiB retained-growth/reserve component is this host's existing obligation,
not new screenshot allocation. No old cleanup savings are assumed.

The parent must refresh measured free/allocated bytes and deduplicate exact
store outputs and filesystem roles; count already allocated image/root blocks
once and remaining growth once. Raw-image construction and Nix closure copies
can overlap and require temporary space. No finite scratch bound is proved.
Missing store paths, actual substitutions and chosen build headroom need an
operator assessment with live reserve monitoring, not an invented allowance.
The public `start` owns prepare/build/spawn; there is no proposed private
prepare call, fake artifact or pause between its internal phases. Its
pre-operation budget must cover the whole admitted operation. If the parent
cannot justify that headroom, use smoke and leave captures pending.

#### Optional one-cluster public capture packet

No source, schema, provider, package activation or new review lane is needed to
select this already documented path. Bind these exact installed executables:

```sh
RUNTIME=/nix/store/8z7p3bqmanmn4cam69jfw8h3wjvzd6cg-vpsfree-kb-devcluster/bin/vpsfree-kb-devcluster
CAPTURE=/nix/store/klpjidbd36w3m6p1rsvjrx24jdsxpbqp-vpsfree-kb-capture/bin/vpsfree-kb-capture
VALIDATE=/nix/store/klpjidbd36w3m6p1rsvjrx24jdsxpbqp-vpsfree-kb-capture/bin/vpsfree-kb-validate
SOURCE=/nix/store/6zgfm2h7wipl6ba0bqrfh03qk1lymwiq-source
```

Select the immutable source directly from the verified receipt, with no source
override. All path variables below are concrete
private packet inputs, not values to discover from ambient CWD/environment.
Use a new ordinary root outside checkouts and a unique slug, absent state/output
destinations, explicit disjoint local TCP ports and numeric multicast port,
QEMU DNS `10.0.2.3` and `example.test` domains. Initial config records the three
dedicated synthetic users, including level-99 `test-admin` and level-1
`test-user1`, with the accepted quota/block allocation. No ambient credentials,
role promotion or old-state adoption. Keep the unselected topology nodes and
services disabled as in the accepted single/local profile.

Reuse the accepted ordinary user-service context (`ExitType=cgroup`, explicit
unit/controller tuple and RUNNING/MainPID admission before guest work), clean
package-selected environment, private logs and one finite operation receipt.
The fresh watcher owns launching/monitoring the exact public command packet.
Never call the two-root verifier or record a fictitious completed phase.
Kernel/cache evidence must be refreshed for this exact source/config using
the already accepted public `runtimePlan` kernel projection and actual store/
substitution facts. Projection without instance credentials is kernel planning,
not final guest closure proof. Stop unexpected kernel builds under the existing
policy. Retain capacity/KVM checks, physical RAM/shm headroom and monitoring;
8 GiB is guest demand, not a whole-host sufficiency assertion. No new host
allocator, persistent supervision framework or workspace dependency is needed.

From a private ordinary CWD distinct from the existing writable `$OUT`, use:

```sh
"$RUNTIME" --state-root "$STATE" start "$SLUG" --topology single \
  --network local --config "$CONFIG" --timeout 900
"$RUNTIME" --state-root "$STATE" status "$SLUG" --json
"$CAPTURE" --cluster "$SLUG" --state-root "$STATE" --language cs \
  --checkpoint networking/ip-address-list --output-root "$OUT"
"$RUNTIME" --state-root "$STATE" connection "$SLUG" > "$CONNECTION"
"$CAPTURE" --connection "$CONNECTION" --language en \
  --checkpoint networking/ip-address-list --output-root "$OUT"
```

Create `$CONNECTION` exclusively with mode 0600 inside the private root, using
the operation's no-clobber writer, rather than an unchecked shell overwrite.
The redirection illustrates the private destination; never print its contents.
Run one additional EN invocation from `$OUT` with the same connection and no
`--output-root`, retaining native success to prove the installed default CWD
path. It replaces the EN result at the same semantic key; only two canonical
PNGs remain. Sequential languages share the same physical output lock and
source receipt. Then run the installed validator from the ordinary CWD:

```sh
"$VALIDATE" --update --output-root "$OUT"
"$VALIDATE" --output-root "$OUT"
```

No `--allow-missing`, limited-inventory validator or local `bin/check` is used.
Strict validation covers the full inventory with unchanged assets resolved
from immutable G. It is an artifact acceptance operation, not permission to
run local source CI. Missing unrelated assets still cause refusal.

`Engine#await_ready` must complete first-contact SSH trust, exact guest
metadata and `/run/current-system` checks, pool refresh, disk/prepared proof,
accepted-artifact publication and canonical `ready?`. Each capture separately
validates the leased descriptor and exact G metadata before browser/fixtures;
TLS and explicit endpoint routing remain. The fixture proves synthetic member
and admin API identities and ordinary member browser identity. It creates or
validates its dedicated `203.0.113.0/24` pool and owned unassigned
`203.0.113.10/32`, then disables only that pool. Primary pools stay enabled.
The scenario verifies the actual gray row, translated title/focus semantics,
retained links, missing obsolete Enabled column and a contrasting real enabled
assigned row. A PNG does not certify the native browser tooltip popup.

After strict validation, export only the existing five-file allowlist through
G's existing `tools/capture-export.rb` under its own artifact flock. This is a
file-export helper, not a public lifecycle command or private Engine call.
The parent can invoke it with the package-selected Ruby as a small finite
command, without adding a new CLI or wrapping its lock in a second lock:

```sh
"$RUBY" -rjson -r "$SOURCE/tools/capture-export.rb" \
  -e 'puts JSON.generate(KbCaptureArtifacts.export(ARGV.fetch(0), ARGV.fetch(1)))' \
  "$OUT" "$EXPORT"
```

The destination must be absent under a private parent. Export comprises only
both `screenshots/{cs,en}/networking/ip-address-list.png`, candidate
`captures.json`, `tmp/capture-results.json` and `tmp/capture-source.json`;
retain the helper's per-file checksums. Do not export connections, credentials,
config, raw transcripts or incidental scratch. Revalidate the exported bundle
against G with the installed validator and review both actual images for crop,
language, gray/enabled contrast and absence of secrets/production identifiers.
No bitmap editing or synthetic substitute is acceptable.

#### Acceptance, failure retention and generator-to-media provenance

The root's operation receipt records the selected alternative, exact executable/
source/config hashes, measured admission, native statuses and artifact hashes.
It records skipped proofs explicitly. Package smoke success does not set any
runtime/capture phase complete. A live smoke on another proved software revision
reports that revision; it cannot be renamed G922 evidence or used to mint a
canonical connection. No accepted hosted checks are replaced by this plan.

For actual captures, retain G922 and its original source/lock/fixture metadata
as the generator. The later reviewed media commit M may carry these two PNGs
and inventory changes but must not rewrite their provenance to M. Preserve the
one authoritative K lineage and normal input graph; the root owns eventual E
selection of M and consolidation of the existing input stream. The original
K branch must not acquire a new fixture or unrelated provenance stream. Exact
media-head hosted `workflow_dispatch` with `strict=true` remains the canonical
full `bin/check` gate; this does not call for rerunning already accepted source
suites merely to choose smoke. Visual acceptance and final pin disposition
remain pending, with no production KB publication/default integration.

On any failure, retain the private attempt/native evidence and any new owned
instance in its actual state. No automatic replay, image rollback, claim/socket
removal, GC, public reset or service-group stop follows from this plan. Unit
state is not campaign success; readiness loss prevents capture acceptance.
The parent must make a separate concrete disposition using the unchanged
public ownership/complete-exit contracts. G4/G6/isolation3 A/B, their possible
disk growth, preview and foreign resources remain untouched. Historical update,
two-root isolation and continuity verification are explicitly **deferred and
unfinished**. The session stays active for the selected verified handoff.

This is source-supported design readiness, not resource admission or execution
evidence. Only this document was appended; no application changes, checks,
evaluations, builds, live probes, guests, lifecycle actions or Git operations
were performed by the architect.

### Reduced real runtime qualification and finish plan — proposal (2026-10-10)

This supersedes the preceding recommendation to use installed help/refusal
smoke as the immediate answer to resource reduction. The user requests cheaper
**real runtime tests**. Recommend one final-source full-product cluster with
a smaller explicit profile, one public start/lease/stop/resume qualification,
and optional canonical CS/EN captures from that same instance. Remove genuine
historical-source upgrade and simultaneous two-root isolation from this
session's required real-guest acceptance. Their prior failures and unproved
criteria remain recorded as **optional, deferred proof**, not successful tests.
This is a plan for lead acceptance before source assignment or execution.

Exact inspection base remains K `922e71e5eb75b6eb416bf55e39160e9a7236e654`, E
`2c1d3e86435292303f9c2f3f3386dc90e6b9efd0`, and the immutable sources/packages
identified in the preceding section. Binding/current and retained roster 17
were reverified for this work item; architect settings are unchanged. Existing
hosted/review evidence remains valid at those exact objects. No new real run
or source gate has been established here.

#### Chosen profile and the work removed

Use one fresh `single`/explicit-local instance with this qualification target:

| Resource | Proposed value | Meaning |
| --- | --- | --- |
| Services RAM | 2048 MiB | Actual API, database, queue and PHP services remain. |
| Node1 RAM | 2048 MiB | Actual vpsAdminOS/ZFS node, not a mock. |
| Services image/root | 8192 MiB each | One immutable image and one independent writable copy. |
| Node1 tank | 8 GiB | Sparse file with its full future growth still accounted. |
| Inventory VPS | Existing 1 CPU, 1024 MiB RAM, 4096 MiB disk, zero swap | Runs inside node1; its RAM/quota is not a third VM or an additional host disk. |
| Live runtime machines | Two maximum | Services and node1; stop completes before the same two resume. |

These values are **finite qualification targets, not measured sufficient
minima**. Keep the existing CPU settings, product payload, quota checks,
synthetic accounts, explicit ports/multicast/DNS and source/trust controls. No
automatic retry with more RAM/disk or a second configuration is allowed.
This targets 4 GiB of runtime guest RAM/shm, versus 16 GiB for two former full
instances, and **24 GiB of eventual new image/root/tank extents**, versus
92 GiB. It also improves on the previous one-instance 8 GiB RAM/40 GiB proposal.
There is no predecessor package build, second instance, third service image,
closure import, historical guest preparation or live update in the new route.
Stop/resume reuses the accepted artifact and existing disks; it creates no new
guest image. Capture follows in the same environment if justified by its
observed resources; it is never conditional on broad upgrade testing.

The base verifier's excess is concrete: `installed_layout` builds a predecessor;
`isolation_continuity_update` starts A and old B concurrently, resumes old B,
updates B, resets A, and resumes B again. `remaining_growth` charges three
12 GiB service images and two roots/tanks; `capacity` retains 24 GiB RAM,
18 GiB shm and reports a 108 GiB envelope including reserve. Changing only
`validate_config` would leave those wrong requirements intact. The reduced
verifier must replace the operation graph and its accounting together.

#### Why use a smaller full cluster rather than another runtime fixture

The relevant knobs already reach OSVM/Nix at K
`cluster/nix/test.nix:73–75,1907–1925,1969–1975`. The current portable engine
does not impose the verifier's fixed 4+4/12/16 profile. Its `refresh` genuinely
waits for MySQL/API seed state and the node's ZFS/osctld/nodectld. A one-VM
lightweight fixture could be cheaper, but would require a new Nix payload plus
explicit engine refresh/profile/capability branches; advertising `ip-inventory`
for that payload would be false. It would not produce the requested PHP images
and would leave a second full environment to qualify later. Do not add that
new product/runtime branch to finish this initiative.

The pinned OS `6bdf458...` `tests/make-test.nix:253–266` supports numeric or
automatic raw-image sizing. The exact pinned
[Nix image builder](https://raw.githubusercontent.com/NixOS/nixpkgs/5dfba6236110080a54247d6460bc2ff5dda939cc/nixos/lib/make-disk-image.nix)
computes `auto` from installed payload, filesystem overhead and extra space;
the OS wrapper supplies only 512 MiB extra by default. Numeric size instead
fixes the image extent, and a payload that cannot be copied into it fails the
build. Neither automatic sizing nor NAR bytes alone proves usable database/log
headroom. The builder stages a root and image and can run its own temporary
image-finalization VM before runtime guests exist. Account this sequential
construction work separately, not as an outer runtime-test VM.

Choose the bounded numeric 8 GiB image for this one attempt, rather than an
unbounded `auto` result or a new automatic capacity policy. Record actual
payload/available-space observations. K `PreparedDisks#prepare_disks` copies
with `IO.copy_stream`; existing evidence shows fully allocated roots. A sparse
copy implementation or qcow2 overlay could reduce initial blocks but would
change retained-disk creation/dependencies and need new failure/identity tests.
It also cannot erase future guest growth. Leave that production path unchanged;
the smaller numeric image already reduces both image and copy. No host-store
mount, root substitution, speculative reflink saving or payload removal.

There is one necessary K-owned Nix correction, separate from the verifier:
`machines.services.memory = serviceMemoryMiB` controls OSVM's running guest,
but OS `tests/make-test.nix:266` independently passes
`nixos.config.virtualisation.memorySize` to the image builder. Exact pinned V
`ebe4fab...:tests/configs/nixos/vpsadmin-services.nix:249` sets that value to
8192; G922's services module has no override. Thus the 2 GiB runtime knob alone
would leave an 8 GiB image-finalization builder. In K
`cluster/nix/test.nix:servicesModule`, align
`virtualisation.memorySize = lib.mkForce serviceMemoryMiB`. This is the
existing services profile's RAM setting, not a new fixture or V/OS edit.
Qualify both the runtime machine value and actual image-derivation `memSize`
at 2048. Keep kernels unchanged. The preparation builder then has a 2 GiB
target and finishes before the two runtime guests start; its successful fit
is part of the same finite qualification, not an already established fact.

#### Small preparation measurement and finite fit boundary

After the narrow source gates below, the parent performs one measured
preparation/admission step, under the existing fresh watcher/context policy:

1. Bind the new exact immutable package/source, one private initial config and
   ordinary root. Project the public `runtimePlan` machine/memory/disk/kernel
   and image-derivation facts: two machines, 2048 MiB each, 8 GiB tank and
   expected cached kernels. The validated config and owning Nix mapping prove
   fixed image size 8192 MiB; inspect the actual image derivation's builder RAM
   rather than inventing a `diskSize` field in the resulting machine JSON.
   Inspect actual local/substitutable closure paths and their
   sizes; no private `Software.prepare/build`, fabricated credentials, guest
   identity or accepted-artifact receipt. A projection with placeholder
   credentials is planning evidence, not the final guest closure.
2. Measure shared filesystem roles/free space, existing allocated store paths,
   missing closure costs, RAM/shm availability and actual daemon build location.
   Reuse valid exact kernel/cache facts; substitute expected outputs and refuse
   unexpected kernel compilation. Limit construction concurrency to one job
   and one core in this qualification. Record what can be bounded and keep
   remaining builder scratch explicitly unknown with assessed headroom and
   live reserve monitoring. Do not build another probe image just to guess the
   intended image's footprint.
3. Before launch, refuse any projected payload already too large for 8 GiB or
   any unjustified host headroom. During the one public `start`, the **native
   fixed-size image build is the final exact pre-runtime-launch fit check**:
   `Software.build` must finish before `start_locked` reserves/spawns the
   runner. A build/copy-to-image failure ends qualification without guest
   launch. This is not a claim that all exact final image bytes can be checked
   before the public call creates its genuine credentials/artifact. No public
   prepare-only interface currently exists; do not invent a private substitute.
4. Once ready, record actual image/root lengths and allocated blocks, services
   free bytes/inodes, node ZFS available space and memory pressure. Require
   1 GiB services free space as this short qualification's writable headroom
   target before adding fixtures. Before optional VPS/capture work, preserve
   real quota checks and assess available tank space against its 4 GiB quota,
   selected template and metadata costs. A passing initial boot alone does not
   qualify capture resources. If space or memory is inadequate, stop advancing
   the experiment and report which target failed; do not resize or upscale.

This deliberately permits one bounded build/boot qualification, rather than
requiring an impossible advance measurement of future scratch or promising
that an unmeasured target fits. Failure at any preparation, image fit, readiness,
resource, lease or lifecycle stage ends the attempt. Preserve its native result
and state; no probability-based replay or automatic alternative profile.

#### Correct accounting for the reduced verifier

Replace the old 24/18 GiB admission constants and 108 GiB reported envelope.
Derive guest RAM and shm demand from the one exact validated config: 4 GiB.
Keep a separately recorded positive operator-assessed process/browser/build
overhead in the capacity receipt, refreshed against actual availability. Aim
for a qualification envelope around **6 GiB available RAM and 5 GiB free shm**
(4 GiB guests plus 2/1 GiB assessment margins), rather than hardcoding the old
two-cluster thresholds. Those margins are planning targets to assess, not
measured facts or universal requirements. Account sequential build and running
guest/browser peaks; do not add an image-builder VM to the runtime peak when
it has already exited. Use the larger phase requirement, not their sum.

Intrinsic final disk extent is one 8 GiB image + one 8 GiB root + one 8 GiB
tank. `remaining_growth` must enumerate only that instance and one distinct
image, deduct actual allocated blocks once, retain sparse future growth and
deduplicate paths/inodes/filesystems. Resume must not budget a second image.
Report `intrinsic_output_envelope_bytes = 24 GiB` separately from closures,
construction headroom and host obligations; missing service-image inventory
allows only the one planned image. During preparation, account staging payload,
image/store-import overlap and other observed build costs; during runtime,
account image+copy+tank and any remaining closure demand. Use their actual
sequential peak and never assume temporary overlap is zero without evidence.

The current host's roughly 64 GiB retained possible tank growth and 16 GiB
reserve remain protected **separate host obligations**. They are not an
intrinsic 80 GiB runtime-test requirement and confer no cleanup authority.
Already allocated old files are reflected in current free space, so do not
charge them again. There is no universal 120/172 GiB floor. Unknown scratch
cannot be replaced with a guessed allowance, and measured local scarcity still
may refuse this particular host even when the test itself is much smaller.

#### Narrow implementation boundary and real proof sequence

Implementation proposal: simplify K's existing `tools/runtime-verify.rb` to
one final-source campaign with `--config FILE`, one state root and the existing
packaged source selection. Required real phase becomes `runtime-smoke`;
`bilingual-capture` remains a separate optional phase on its accepted instance.
Keep installed-layout checks inexpensive and optional/reusable; remove their
predecessor build and their prerequisite status for real smoke. Remove the
old predecessor/two-root operation from the active verifier instead of retaining
an unused second workflow. Its exact old source and receipts remain historical
evidence; deferred future upgrade work needs a new explicit plan.

Use an explicit new verifier campaign kind to reject old finite-campaign roots
and argument combinations before mutation. Do not migrate or reinterpret old
attempts. This concerns verifier receipt/CLI compatibility only: runtime state
2, artifact 1, connection 1, public engine/runner, physical locks and E SDK
contracts are unchanged. Refactor existing helpers to select the single state,
preserving their command supervision, diagnostics, source checks and hashes.
No generic host framework, new launcher or runtime schema is needed.

The one permitted sequence is:

1. Public final-source `start`, native success and canonical readiness; obtain
   connection and recheck both guest identities and actual system closures.
   Exercise real TLS/API current-user identity and PHP ordinary member page
   access through the existing leased connection/account/browser helpers, with
   no mock responses or fixture bypass. Record read smoke separately from PNGs.
2. Reuse `tools/verify-live-lease.cjs` on this one descriptor: exact source and
   endpoint routing, wrong-source refusal before SSH, physical gate held while
   public stop/update/reset return 75 unchanged, EOF and owned-controller
   interruption followed by reacquisition. No request is queued for later
   destructive execution. Keep controller authority and complete-exit guards.
3. Write only the existing dedicated services-root and node-ZFS sentinels
   through public SSH. Retain six credential hashes, accounts hash, disk
   device/inode/length and accepted artifact identity privately. Public `stop`
   must prove complete exit; then public `resume` must use the same artifact,
   disks, credentials, accounts and sentinel data with a fresh run ID. Recheck
   source/closures/SSH trust/readiness and absence of a new image/build. Keep
   native 900-second public observation budgets and configured machine budget
   distinct; a caller timeout is failure, not permission to kill a runner.
4. If the observed smaller environment passes resource/fixture prerequisites,
   optionally capture both canonical IP-list images from this resumed instance
   using the preceding explicit cluster/connection/default-output sequence,
   strict installed validation and five-file export. Keep the real 1/1/4 VPS,
   synthetic admin provisioning/member capture, gray disabled owned row and
   enabled assigned row. No third guest, storage node or historical update.

The public capture path remains usable independently; a broad historical test
is not introduced as a screenshot prerequisite. Stop/resume in this plan is
the small runtime acceptance being requested. No final reset or deferred unit/
session cleanup is implied. On timeout/readiness loss/incomplete exit, retain
the current owner and evidence under existing rules and end qualification.

#### Files, verification gates and completion limits

Primary edits are `tools/runtime-verify.rb`, `tools/test-runtime-verify.rb`,
the one services image-builder memory alignment in `cluster/nix/test.nix`,
and the owning `cluster/runtime-contract.md`, README and
`docs/webui-change-workflow.md` examples as needed. Reuse existing
`tools/verify-live-lease.cjs` and capture/identity helpers; a small single-state
argument adjustment belongs there only if necessary. Private config generation
is parent-owned and must use the exact new profile/accounts from initial
creation. No engine/runner/disk-copy/OS/V application modification is proposed.
E needs only the normal exact K input selection with K's own graph preserved;
there is no E functional or installed-activation change.

Hosted focused verification must prove one config/instance/image, exact reduced
profile validation, no predecessor build/update/second root, correct
remaining-growth deduplication before and after resume, independent RAM/shm
margins, retained host reserve, old-root refusal, failure/no-replay behavior,
and reuse of source/credential/sentinel assertions. Include the narrow Nix
profile projection asserting both runtime RAM and image-builder `memSize`
follow 2048 MiB, and that this profile keeps the expected kernel outputs.
Its owning existing quick
command is `nix develop --command ruby tools/test-runtime-verify.rb`; if the
Node lease helper changes, include its existing affected hosted owner.
Normal exact-head K source/package and E composition checks plus independent
review of the narrow committed diff precede the one real attempt. No local CI,
new broad VM suite or rerun of unrelated accepted V/W/D suites is requested.

Retain the distinction between existing hosted evidence and the new real
proof. `tools/test-runtime.rb` already covers real filesystem/process/socket
ownership, resource conflicts, same-slug identity separation, lease locks,
safe atomic reads and synthetic-runner lifecycle/readiness. The machine tests
exercise the pinned driver with tiny files and controlled processes, including
thread descendants, delayed stop and finalization ordering. Mocked closure
tests verify import arguments/content/failure rules. They remain strong scoped
evidence, but are not actual guest boots, full-product service shutdown,
historical closure imports or two live clusters. One real final-source
start/stop/resume closes the immediate guest-driver integration gap without
repeating all hosted cases in expensive guests.

After a successful one-shot qualification, record actual peak allocation/RAM,
what ran and every omitted case. A failed optional capture does not erase a
completed separately receipted lifecycle smoke, but PNG acceptance stays open.
If either fails, return a bounded handoff with the specific failed stage; no
second qualification is implied. Retain all previous allocations and preview.
No rollback means booting an old image or adopting a failed state; source
rollback leaves the new private attempt untouched.

The finish plan then carries any approved two PNGs to media commit M retaining
their real generating G metadata, runs the existing strict hosted media gate,
consolidates E's canonical K input and C's final V/W pins, and produces a
verified handoff with the exact remaining feature heads and unmet proofs.
The lead must enumerate the actual final merge set (including any unmerged
V, W, K, E, D and C features) and seek the user's later explicit per-repository
integration direction. This plan itself approves no merge, deployment,
activation, production KB publication or session archive. No material product
choice remains in this proposal; measured fit and the user's final scope/merge
disposition remain facts/decisions for that handoff.

### Selected continuation: one corrected reduced qualification and CS/EN captures (2026-10-10)

The user's subsequent `continue` selects the unfinished real runtime smoke and
two genuine PHP KB captures after the published source handoff. This section
supersedes only that handoff's statement that no further real operation is
selected. It preserves the reduced profile, failed-attempt boundaries and all
earlier evidence qualifications. It is an operation brief for the lead, not
certification of installation, current ownership, available capacity or a pass.
No application/source change, new runtime interface or recovery mechanism is
needed for this continuation.

Current identity was checked from the exact absolute tracking directory with
`login:false` using `/home/aither/bin/dev-session current`; both environment
markers were absent. The matching live roster remains revision 17 with
architect0 at Astra/xhigh, design, workspace_write. Root owns preparation,
fresh observations, the concrete execution packet, watchers and acceptance.
Only this design section was written by the architect.

#### Exact source and retained evidence

- Generator G is K `49221a07e2fabbee4a3621979f814eac8c8bad9d`; E
  `265bd7892b334c67cf760680d06e24fcd06d5cdf` selects it with its own graph.
  `finish-final-review1-report.md`, `finish-final-review1-acceptance.json` and
  `finish-final-stdin-hosted-acceptance1.json` retain the complete source,
  history and hosted gates. They do not prove a corrected real execution.
- The immutable K source read here is
  `/nix/store/yaqalwhadk4gg7f6bcr17kpi1p12nqzi-source`. The existing metadata
  derivation `fizgapmbqxw72bmxn2r26z4hs910iwxp-vpsfree-kb-runtime-source.json.drv`
  invokes that source's metadata writer with exact G. This is source/derivation
  evidence; the lead must still accept the realized package and paired metadata.
  `flake.nix:123–180` binds runtime, capture/validator and verifier selection to
  one source. Do not supply a different `--selection`, software metadata,
  checkout, input override or ambient reader package.
- G13 remains generated by
  `9c551c6ad68650d12f3d8e91f8bf33a76e2ffe0e`. Its redacted
  `finish-runtime-reduction-real-start-proof1.json` records successful public
  start and guest identity/current-system checks, two 2048 MiB guests and three
  8 GiB logical disk files. Its runtime-smoke attempt failed before resource,
  TLS/API/PHP, lease, continuity or capture acceptance. Discarded public SSH
  stdin is corrected in G's `cluster/launcher.rb:77–83`; no G13 result becomes
  a G result. The original campaign remains nonreplayable even after shutdown.
- `finish-corrected-g13-public-status1.json` records a ready snapshot at
  19:13:16 UTC for instance `b93cead9-2548-4754-9a37-349a5c4ddffb`, run
  `af01bfda-d56c-4960-bfbf-39a6ed0d834c`. It does not establish liveness at a
  later stop. `finish-corrected-package-plan1.json` and its package assessment
  describe seven metadata/wrapper derivations and three fetched paths
  (1.5 MiB download, 7.6 MiB NAR); no kernel/image work was in that package
  dry-run. Package preparation is separate from guest construction/admission.

Authoritative source boundaries are K `cluster/runtime-contract.md`,
`docs/webui-change-workflow.md`, `cluster/launcher.rb`,
`cluster/lib/kb_runtime.rb:347–531`, `cluster/lib/kb_resources.rb:17–105`, and
`tools/runtime-verify.rb:125–276,303–487,619–682` at G. Existing state2,
artifact1, connection1 and `single-runtime-v1` contracts are unchanged.

#### G13 stop prerequisite; retained failure is not recovery input

Before any new guest start, the lead refreshes only the named G13 state,
launch/process records and durable user-service facts through the existing
read-only public/selected-SDK inspection path. Use the exact old state root
recorded in `finish-corrected-g13-public-status1.json`, slug `same-slug`, and
the same effective UID and ordinary resource registry. Compare the recorded
boot ID, runner PID/start ticks/executable/argv, launch instance/run/artifact,
named child tuples and containing unit/cgroup. Never infer ownership from a
ready string, a PID number, absence of a process, or unit activity alone.
No broad process search or access to other campaigns is part of this work.

Only when the fresh facts permit its normal authenticated live-control path,
the admitted stop command is the final G package's public launcher:

```sh
"$KB_RUNTIME/bin/vpsfree-kb-devcluster" --state-root "$G13_STATE_ROOT" \
  stop same-slug --timeout 900
```

Here `KB_RUNTIME` must be the accepted runtime output paired with G, and
`G13_STATE_ROOT` the unchanged recorded root, not a copied/adopted directory.
The launcher selects software for start/resume/update, not stop; final public
stop therefore validates the retained old launch and live control peer without
relabeling its source or replacing its runner. It needs no G13 account password
or guest fixture mutation. The engine itself takes the nonblocking gate and
operation lock, pins the owned socket/directory, verifies SO_PEERCRED plus the
runner/launch tuple, sends the normal stop request, and waits for complete exit.

Do not require `processes.complete=true` before requesting normal live shutdown:
that flag is normally false while the runner is alive. Conversely, a list of
currently matching/gone children is not a complete descendant-exit certificate.
Successful stop must establish the engine's `gone?` condition: the exact
completed process receipt and every retained runner/child identity proved gone,
then normal guarded claim/socket release and phase `stopped`. Record native
exit zero, a fresh public non-ready/stopped status and the corresponding complete
receipt identity. The public engine alone owns its ordinary socket cleanup;
there is no independent unlink, claim removal or namespace repair in this brief.

Exit 75, rejected ownership/control, missing acknowledgement, deadline expiry,
unknown socket contents or incomplete exit **holds the new launch**. Preserve
the native result; do not queue/retry a stop, signal a process/group, extend a
deadline, reset/delete state or invent orphan recovery. The 900 seconds is the
public observation budget, distinct from sequential per-machine runner budgets.
A timed-out request may have started a legitimate drain; it is not proof that
nothing happened or permission for another pair. No reset or unit retirement
follows even successful G13 stop. Keep its evidence, disks, config, credentials,
source/artifact receipts and user-service context. Do not resume/update G13 with
G, edit its failed attempt, transplant its accepted artifact or reuse it for PNGs.
G4/G6/isolation3 and the preview are outside both inspection and action scope.

#### Fresh preparation and measured admission

After the supported G13 shutdown is accepted, create one new private campaign
outside workspaces/checkouts using the existing preparation path. Retain the
same per-user registry selection: `Resources#runtime_root` derives it from
validated `XDG_RUNTIME_DIR` or the existing UID-specific `/tmp` fallback.
Record the effective choice; do not change/unset it to evade retained claims.
Choose new explicit loopback TCP ports and numeric UDP multicast port disjoint
from retained allocations. Normal registry/bind refusals remain authoritative;
no fallback ports or alternative registry are allowed.

The parent supplies a fresh initial config, immutable raw-byte digest, campaign
root and capacity-receipt path. Replace **all five exposed password values**
privately: the three explicit synthetic seed-account passwords and both web-auth
passwords, including the public synthetic defaults that appeared in G13 inputs.
Preserve the documented test-admin level 99, test-user1/test-user2 level 1,
namespace blocks, example.test identities and fixture capabilities. Do not
print values or read/copy G13's private configuration into exported evidence.
The new engine generates its own SSH/TLS credentials, instance, artifact and
run identities. No G13 identity/attempt/receipt is copied. New inputs remain
unchanged through stop/resume and both capture languages.

The profile stays single/local: services 2048 MiB, node1 2048 MiB, services
image and writable root 8192 MiB each, tank 8 GiB; DNS guests disabled,
QEMU resolver 10.0.2.3. The sequential image builder is 2048 MiB. The inventory
VPS remains 1 CPU/1024 MiB/4096 MiB inside node1, not another VM or disk image.
At most this one new services/node1 pair runs, after G13's proven stop. There
is no historical predecessor, changed-source update or simultaneous pair test.

Before invoking the verifier, root binds the newly accepted exact runtime,
capture, verifier selection, metadata/source/lock/fixture identities, raw config
digest and ordinary root to the private capacity receipt. Retain E's exact
composition proof without activating its provider. Use the existing public
runtime-plan/kernel and store facts to refresh any config/source-dependent
preparation evidence. Reuse only still-matching exact cached kernel facts;
refuse unexpected kernel compilation. Fresh credentials/source/config produce
genuine new guest artifacts: G13's successful fixed-image build is useful prior
fit evidence, not proof of the new final image. Public start's fixed-size image
build remains the exact pre-spawn payload-fit gate.

Refresh available RAM/shm and the actual state, store and daemon-scratch
filesystems. Keep one build job/core and explicit assessed construction overlap
and headroom; scratch remains unknown. Package-only download figures, NAR size
or client TMPDIR do not establish future guest-build peak or the daemon's
filesystem. The intrinsic new output envelope stays **24 GiB**, not a universal
free-space floor. Deduct already allocated bytes once per file/inode/filesystem;
charge new missing closures and remaining image/root/tank growth, plus the
existing 16 GiB reserve and protected retained-host growth. Retain G13's old
allocated disks/image in the accounting as well as the new campaign; stopping
does not reclaim them. Already allocated old bytes have already reduced free
space; their remaining writable growth is separate. Do not assume source/image
deduplication, cleanup credit or disappearance of old obligations.

Start/resume admit the full 4 GiB guests plus assessed positive overhead
(the existing planning margins are 2 GiB RAM/1 GiB shm). Construction is a
sequential 2 GiB builder plus its assessed overhead; use the actual peak, not
the sum of nonconcurrent phases. Live capture first reproves resumed continuity
and admits only additional browser/tool margins, since resident guests already
reduce available memory. Require the existing guest free-space/inode/memory,
template and 4 GiB quota guards before fixture work; no automatic upscale.

Use the existing finite measurement wrapper and durable ordinary user-service
packet, with a fresh Luna watcher as sole launcher/monitor. Before guest/build
work, prove the unique owned service's RUNNING/MainPID, wrapper PID/start/UID,
InvocationID and cgroup. Preserve `Type=exec`, `ExitType=cgroup`,
`RemainAfterExit=yes`, no restart/replay, private CWD/environment/logs and
package-selected PATH. Retain exact controller/runner/cgroup observations while
live. Native verifier result and its phase receipt govern acceptance; service
activity or eventual service success does not. Keep normal reserve monitoring
and its existing bounded owned-command cancellation policy; it grants no guest,
unit, process-group or old-state cleanup authority. Do not retire G13's unit.

#### One finite public sequence and acceptance

Resolve `KB_VERIFY` only from the accepted G package receipt. These are command
shapes for the parent's private packet, not commands executed by the architect:

```sh
"$KB_VERIFY/bin/vpsfree-kb-verify" --root "$NEW_CAMPAIGN" \
  --config "$NEW_CONFIG" --capacity-receipt "$NEW_CAPACITY" --phase runtime-smoke

# Only after that exact phase completes successfully and fresh admission holds:
"$KB_VERIFY/bin/vpsfree-kb-verify" --root "$NEW_CAMPAIGN" \
  --config "$NEW_CONFIG" --capacity-receipt "$NEW_CAPACITY" --phase bilingual-capture
```

`runtime-smoke` already performs the required sequence: public start; canonical
readiness and both guest identity/current-system checks; actual resource reads
through the corrected public SSH stdin path; authenticated TLS/API identities
and member PHP read; physical public lease, contention exit 75, wrong-source
refusal and peer-loss/reacquisition; dedicated root/ZFS sentinels; public stop
with complete exit; public resume of the same artifact; fresh run with all six
credential hashes, accounts digest, disk identities, image/artifact and sentinel
contents preserved; final guest/closure/trust/resource checks. Do not run those
mutations manually to fabricate a missing phase receipt. Installed-layout is
optional package/path evidence and supplies no runtime substitute.

After successful smoke, the dependent bilingual phase uses the same resumed
instance and exact inputs. It captures only `networking/ip-address-list`:
CS via `--cluster` and EN via the private `--connection`, sharing an explicit
output root different from the invocation CWD, followed by the existing EN
recapture from that root to prove the packaged writable-CWD default. This is
two final language artifacts, not a broader screenshot campaign. Keep ordinary
member capture, explicit synthetic admin provisioning, one real inventory VPS,
the enabled assigned row and the dedicated disabled owned/unassigned gray row.
Do not disable the primary pools or add NAS/traffic fixtures.

The same phase performs installed `vpsfree-kb-validate --update` and strict
full-inventory validation without `--allow-missing`, checks exactly two matching
language/ID result rows and immutable source hashes, then uses the existing
physical artifact-lock export. Carry back only the two canonical PNGs,
`captures.json`, `tmp/capture-results.json` and `tmp/capture-source.json`, with
their checksum receipt. Root reviews both crops, labels, gray/enabled rows and
absence of sensitive/production identifiers; title/focus assertions do not
prove a native tooltip popup is visible in the image.

All native campaign/attempt/capacity records stay private: their `inputs`
include the configuration. Export only explicit allowlisted scalar phase,
source, identity, resource and result facts plus hashes; **never serialize an
`inputs` object**, connection/accounts/credential contents or raw diagnostics.
Preserve original private evidence without repeating the G13 exposure.

One unexpected native failure, reserve cancellation, missing readiness or
ownership/fit refusal ends this corrected attempt and its dependent work.
Retain exact failure attribution and state. No automatic third attempt, replay,
resize, different config, second pair or cleanup is selected. An intentional
negative check is accepted only as explicitly asserted by the existing verifier.
A separately completed runtime receipt remains valid if the later capture
fails, but media stays unfinished. A public-stop refusal in the G13 prerequisite
holds the attempt before launch. Source/hosted evidence never overrides any of
these native results.

If both phases and visual review pass, retain actual G492 generator provenance
when root records media commit M, then obtain the already-defined exact strict
hosted media check and canonical E reselection. Preserve one authoritative K
lineage and one canonical E input stream; no legacy fixture stream or altered
generator hashes. C already selects accepted Vebe/W30cce; captures alone do not
justify another application pin. Root reconciles final source/media evidence and
exact remaining integration set in the handoff. Historical upgrade/two-root
proof stays explicitly deferred. No merge/default integration, deployment,
installed provider activation, production KB write, reset, archive or session
closure is authorized by this brief. No source blocker was found; fresh package,
G13 stop and capacity prerequisites remain operational gates, not certified facts.

### DIAGNOSIS / PROPOSAL: virtiofs pidfiles after complete G13 exit (2026-10-10)

This is a source-supported proposal for root acceptance, not source-edit or
cleanup authority. Current/session and roster 17 were freshly verified through
`/home/aither/bin/dev-session` from the absolute tracking CWD with `login:false`;
both markers were absent and architect0's Astra/xhigh/design/workspace_write
settings are unchanged. The preceding continuation is **held** at its failed
G13 stop prerequisite. The new qualification has not started.

#### Observed result and its precise limits

Read-only sanitized evidence consists of
`finish-corrected-package-realize1-acceptance.json`,
`finish-corrected-g13-context-proof1.json`,
`finish-corrected-g13-before-proof1.json`,
`finish-corrected-g13-stop-preparation1.json`,
`finish-corrected-g13-stop1.json`,
`finish-corrected-g13-stop-refusal1.json` and
`finish-corrected-g13-residual-pidfiles1.json`.

The single public K492 stop with timeout 900 exited 1 in about 24.6 seconds,
without cancellation or wrapper failure. Its error was
`unrecognized retained socket contents; no handoff deletion`. This is not a
machine/public deadline expiry. The after-failure selected-SDK observation
proves the same G13 instance/run/artifact and original G9c source, a complete
process receipt and all recorded runner plus 14 child identities gone. Public
phase remains `stopping`, ready false. Thus process shutdown completed, but the
public stop and namespace retirement did **not** succeed.

The only retained namespace entries are six ordinary UID1000/mode0600 pidfiles:
three shares (`vmSharedDir`, `vpsadmin`, `vpsadminos`) for each of services and
node1, with the exact hashed socket names/inodes recorded in the refusal.
No control socket remains. The parent's bounded NOFOLLOW/fstat reads matched
each file to its recorded inode and each digit PID to exactly one recorded
virtiofsd child. Those bytes explain the artifacts; they are not process,
signal, unlink or adoption authority. The exact own reservation file was
independently observed absent. Do not report claims as retained: this stop
released its own claims before refusing namespace cleanup. No other reservation
was inspected. The stop unit is failed/MainPID0; its earlier context snapshot
and initial verifier tuple are not current live-process proof.

No current action is inferred for this state. Native timing within the daemon,
reaper and filesystem calls was not traced. These facts establish the final
records and a matching source mechanism, not every historical syscall ordering.
They do not diagnose G4/G6/isolation3 disappearance or establish anything about
the preview, which remain outside this investigation.

#### Source owner and failure mechanism

At immutable K `49221a07e2fabbee4a3621979f814eac8c8bad9d`
(`/nix/store/yaqalwhadk4gg7f6bcr17kpi1p12nqzi-source`), the two classes in
`cluster/lib/kb_machine.rb` inherit OSVM's virtiofs lifecycle unchanged.
The effective OS source is `6bdf458fd9105379860234ff33d352e55844f08f`
(`/nix/store/m7lppk7djkzqvrddvj0f2aa05sywl5d3-source`); K's lock resolves its
nixpkgs input to `5dfba6236110080a54247d6460bc2ff5dda939cc`.

OS `osvm/lib/osvm/machine.rb:606–622` starts one virtiofsd per shared filesystem
with `--socket-path <virtiofs_socket_path>`, retaining its spawned PID in the
existing daemon array. `Machine#initialize:47–51` combines the automatic
vmSharedDir with configured shares; `virtiofs_socket_path/socket_path:835–848`
explains the observed names. `tests/make-test.nix:56,169,212,274` selects
`nixpkgs.pkgs.virtiofsd` for machine configuration.

The daemon's published v1.13.3 implementation creates `<socket-path>.pid`,
keeps a file lock, and returns an ordinary file handle; dropping that handle
does not unlink the file. Its supported `--fd` alternative consumes an already
listening descriptor and skips both pathname listener and pidfile creation.
See the primary sources
[main.rs, listener selection](https://gitlab.com/virtio-fs/virtiofsd/-/blob/v1.13.3/src/main.rs#L670-705)
and [util.rs, pidfile writer](https://gitlab.com/virtio-fs/virtiofsd/-/blob/v1.13.3/src/util.rs#L19-45).
Available local virtiofsd-1.13.3 derivations reference the same source
`5l71l9rbabjw79i1r69lfzgnksvn8kv7-source`; that source payload was not locally
available, so the daemon implementation was read from its exact upstream tag.
The sanitized G13 proof exports executable basenames, not its full daemon
store path. Confirm the selected pinned daemon in the prospective hosted
fixture; do not substitute the tool-shell's unrelated daemon package.

OSVM's QEMU reaper (`machine.rb:638–668`) closes shell/console resources,
stops and waits for the recorded virtiofs daemons (`stop_virtiofs:624–636`),
then calls `cleanup`. `cleanup:241–251` unlinks only each virtiofs socket;
`finalize:80–83` closes logs/shells. Neither removes its companion pidfile.
K's runner invokes those same finalize/cleanup methods again only after its
quiesced machine/retained-child proof, then publishes process completeness.
That flag certifies processes, not an empty socket namespace.

K `Engine#stop_locked:493–517` proves complete exit, releases claims, then
calls `retire_shutdown_socket`. Its exact error at `kb_runtime.rb:477` is the
inventory guard rejecting entries other than the pinned control socket. This
matches both the leftover names and the independently absent own claim. Keep
that guard and `cleanup_socket`'s empty-directory requirement unchanged.
Neither a longer timeout nor another call repairs this namespace: with the
runner dead/control socket absent, another stop reaches strict cleanup with
the same residual files; reset also requires ordinary proven stopped state.

#### Recommended prospective repair: use the daemon's existing listener API

Prefer one small shared adapter in **K `cluster/lib/kb_machine.rb`**, included
by both K machine classes, to provide the exact private listening UNIX socket
through virtiofsd's supported `--fd`. Keep OSVM's existing daemon PID array,
stop/wait/reaper logic and QEMU socket pathname. This avoids inventing pidfile
cleanup authority, modifying the daemon, changing OS/V inputs or creating a
second launcher. It is a prospective K-owned integration fix; the old live
runner and now-dead G13 namespace cannot acquire it retroactively.

The bounded implementation contract is:

1. Bind each existing `virtiofs_socket_path` exclusively in the already owned
   private socket directory. Refuse an existing socket, pidfile or other object
   at the expected new-listener path; never unlink to make bind succeed.
   Preserve the same share list, cache policy, sandbox and QEMU path. No PID
   value read from disk participates in ownership or signalling.
2. Pass only that listening descriptor to the configured daemon using an
   explicit child FD mapping and `--fd`; retain the ordinary spawned PID in
   OSVM's existing array. Keep all unrelated guard/control/state FDs closed to
   the child. Acquire listener/child authority and record it without an
   interruption gap; an unsuccessful spawn does not fabricate a child or lose
   ownership of an already created listener. Close the parent's listener copy
   after a successful handoff, and bound exceptional closure to this invocation.
   Do not add a second reaper, extra signals or a new retry loop.
3. Retain only transient identity proof for sockets/directories actually
   created by this machine invocation. Cleanup must accept absent owned paths
   idempotently and refuse observed directory replacement, changed inode,
   symlink, non-socket, foreign UID or unsafe mode before deletion. Pin the
   original identity while needed so inode reuse is not mistaken for ownership.
   Reuse the existing private-path conventions and guard adjacent to unlink;
   do not claim a global atomic filesystem snapshot. Use one shared cleanup
   boundary for these exact virtiofs paths, not per-machine copies or a glob.
4. Leave unexpected files, including **all** `*.sock.pid` residues from older
   runs, to the existing strict engine refusal. No pidfile whitelist or content-
   matched deletion is added. Keep OSVM reaper joins, K append-only descendants,
   final quiescence/process proof, public gate, namespace checks and normal
   claim release ordering. A cleanup error stays observable and cannot turn
   the overall public stop into success merely because processes are gone.

An upstream OSVM improvement may be useful separately, but this session does
not need an OS source/pin change to consume the already supported descriptor
API. Adding `unlink(socket + '.pid')` to either engine or inherited cleanup
would be a different ownership policy and is not this recommendation. The
adapter must not merely wrap `super` and then blindly delete leftovers.

#### Focused hosted proof and compatibility

Implementation owners are K's machine adapter and existing
`tools/test-machine.rb`, plus the short runtime-contract explanation. If
needed, expose the **existing guest-pinned** `pkgs.virtiofsd` in K's declared
test environment (one flake shell binding, no new flake dependency/input or
package version). E later needs its normal exact K pin, not provider code.
Engine, runner, verifier phases, resource profile and runtime schemas are held
unless a concrete implementation conflict is referred to root first.

Require deterministic hosted coverage through the actual machine seam and
owned child processes/listening sockets, rather than only matching argv:

- Exercise both K machine classes and all three normal shares; the child uses
  the explicitly inherited listener, and no pidfile appears. Include the real
  selected virtiofsd package as a focused host subprocess without QEMU/guests;
  a test-only sandbox-none invocation may isolate API/FD behavior from host
  namespace policy, without changing production daemon options or claiming
  production sandbox coverage. Native failure must fail, not skip, this case.
- Exercise ordinary public `Engine#stop` in the existing owned runner fixture
  with this machine-owned daemon/listener lifecycle. Preserve its real child
  reaping and complete-exit assertions, and require successful stopped status
  and an empty/removed owned socket directory. Keep existing unknown-entry
  refusal and primary/secondary diagnostic tests.
- Cover spawn failure/partial multi-share startup, supported interruption,
  descriptor closure/no inherited guard FD, repeated cleanup, and socket or
  directory replacement/unsafe metadata. Replaced or pre-existing entries and
  an unknown regular `.sock.pid` remain untouched and prevent stopped success.
  Tests act only on their own children and paths; no real PID reuse, broad
  host process scan, timeout increase or discarded assertion is needed.

The focused owning command is `nix develop --command ruby tools/test-machine.rb`,
with existing `tools/test-runtime.rb` for public cleanup boundaries and normal
K `bin/check --allow-missing`/exact E composition gates **on hosted CI only**.
All substantive changes must be committed and independently reviewed before
package preparation and the one corrected real qualification. Existing G492
review/hosted evidence remains original-object evidence, not a remediation pass.
No local test, new broad VM suite or unrelated V/W/D campaign is proposed.

There is no persistent state/protocol/credential format change. New runs use
the new adapter; old pidfile namespaces are neither migrated nor adopted.
Rollback to old machine code restores its old residue behavior and strict
refusals; it supplies no cleanup mechanism. A later G generator and exact E
selection need genuine new metadata/packages, not G492/G13 receipt substitution.

#### Explicit alternative for G13: retain completely exited state

There is no currently supported public operation that safely retires these
dead residual files under the accepted cleanup contract. Do not retry stop,
reset, manually unlink, edit phase/receipts, signal, remove claims or retire
either user service. The prospective listener fix cannot clean this old state.

Root may **explicitly revise** the preceding requirement for a successful G13
stop to permit retention of its completely exited instance while performing
one later fresh corrected qualification. That alternative relies on fresh,
unchanged exact launch/artifact/source identity, complete descendant receipt,
all named identities proved gone and the exact own claim still absent—not on
the failed unit's status alone. Keep the native stop failure, `stopping` phase,
six residual files, disks, credentials, configs, original failed attempt and
units intact. Retention is not a passing stop or a cleanup certification.

Only after root adopts that alternative, the prospective fix clears its source
gates, and fresh capacity/registry admission succeeds can the previous one-new-
campaign packet advance. Preserve G13's allocation/future-growth obligations,
fresh private replacement of all five exposed values, disjoint explicit ports
under the same registry, new identities and the single reduced profile. No
second live G13 pair, G13 replay or another automatic qualification is allowed.
The not-yet-started corrected smoke remains finite and fails closed on its
first unexpected native failure. Historical failed campaigns and preview stay
untouched. Until this explicit disposition, captures and new launch remain held.

Additional same-task context evidence:
`finish-corrected-g13-final-unit-observation1.json` at 19:53 UTC records the
original G13 invocation unchanged, active/exited with MainPID0 and empty Job
and ControlGroup. Its unit Result=success coexists with stored
ExecMainCode=1/ExecMainStatus=1; the native runtime-smoke receipt remains failed.
The exact stop unit is failed/failed, MainPID0, with empty Job and ControlGroup.
These fresh context observations support the proposed fully exited retention
boundary alongside the complete named process proof; they neither certify
namespace cleanup nor grant launch authority. Stored initial verifier tuples
and pre-wrapper-exit final_context records are historical, not current live
operation facts. Both units remain retained without an action.

### DIAGNOSIS / PROPOSAL: publish the streaming test's EOF marker completely (2026-10-10)

This is a bounded D test-fixture proposal, awaiting root source acceptance. It
does not change the production lease contract or certify a remediation. Native
`current` from the exact tracking CWD and the live same-session roster17 were
checked; architect0 remains Astra/xhigh/workspace_write. Only this design
append is authored here. K's separate listener repair and all retained runtime
state remain outside this item.

#### Observed failure and source-supported explanation

The completed E Check38083114582, exact
`874adbd3f477d04f0c81f52afc8d777b91814187`, failed its compatibility package
with the unchanged selected D
`b1ec1bf1c3bc6413b066816ca58468b67ad5e5a6`. The retained
`finish-virtiofs-listener-hosted1/e/{final.json,final-jobs.json,full.log}`
records 139 runs, 1082 assertions, one failure, zero errors and three skips.
At full.log:1496–1501, the abrupt-dispatcher-loss test expected `EOF` but read
an empty string at commands_and_locks_test.rb:150. The workflow then failed;
its downstream devcluster check was skipped. Other package instances' passing
results in the combined log do not replace this failed composition.

At D's selected head, `test/workspace_host/commands_and_locks_test.rb:128–158`
starts a real dispatcher/provider, receives readiness, kills and waits for
the dispatcher, and successfully asserts caller protocol EOF. It then waits
at line149 for the existence of `provider-ended` and reads its bytes at150.
The provider script in `with_streaming_provider`, lines337–408, reaches
`File.write(PROVIDER_ENDED, 'EOF')` only after its real stdin read/each-line
loop returns. There are three such publication sites:369,385,403.

`File.write` creates the visible path before completing its payload write
and close. A reader can therefore observe existence and read zero bytes in
that interval. This is a concrete source-supported observation race that
explains the reported value; the native log does not record syscall ordering
and does not prove that historical interleaving. Do not relabel the failed
run as passed, dismiss it as flaky, or infer a production lease failure from
this fixture assertion. The following generation-lock assertion was not
reached in the failed case.

The reached production path is `libexec/workspace-host:1158–1189`
(`dispatch_cluster`) and 2989–3110 (`system_env_streaming!` and its child
wait/cancellation helpers). It gives the provider fresh mediated pipes,
closes inherited authority descriptors and keeps ordinary cancellation and
reaping inside the generation guard. The synthetic marker is not part of
that protocol. Its correction belongs in the test, not this mediator.

#### Minimal proposed source boundary

Use one fixture-local EOF publisher inside the generated provider script.
After the existing real stdin EOF has been observed, write and close the
literal complete `EOF` payload at a sibling temporary path in that test's
unique temporary directory, then rename it to `PROVIDER_ENDED`. Route all
three existing publication sites through it. No test parent may synthesize
the marker; no early-error, exit or stalled-provider branch gains one.
Publication means **provider input EOF observed**, not provider exit or
cleanup complete. No persistent receipt, fsync protocol, dependency, generic
atomic-file framework or production helper is needed for this test signal.

Preserve all existing assertions and five-second observation bounds, the
0.2-second fixture cleanup windows, the explicit default-stdout release
barrier, exact-child reaping assertions and generation-lock checks. Do not
wait for provider exit before checking the guard: that would change the
property being tested. If publication never completes, the original bounded
wait must still fail; a temporary file is not a success marker. Do not add
sleeps, retries of the failed test, a larger timeout or an empty-string
acceptance to conceal the race.

The same publisher closes the immediate read race in
`test_capture_lease_stdout_eof_closes_the_peer_while_input_stays_open_and_guard_covers_reap`
at 224–225. The readiness/guard test at 45 and default-stdout test at 290 also
use marker existence while the provider is still in cleanup; they should
benefit from the same complete publication without new consumer protocols.
The broken-output, interruption and before/immediate-readiness tests read
the marker after the dispatcher has returned/reaped its provider and have
no demonstrated equivalent early-read gap. Keep them unchanged and retain
their shared-helper coverage. The initial provider PID marker is read after
readiness or termination; this failure supplies no reason to redesign it.

The sole proposed source owner is
`test/workspace_host/commands_and_locks_test.rb`, with a short nearby comment
explaining why path existence must imply a complete marker. The existing
real-process tests exercise the meaningful EOF/guard/reap properties; no new
generic synchronization test framework or workflow is required. Owning
`docs/workspace-portal.md:517–535` already states the production contract and
needs no behavior change for this fixture-only repair.

#### Hosted verification and compatibility

The following are proposed hosted selections, not commands executed here:

```sh
nix develop .#dev-workspace --command ruby test/workspace_host/commands_and_locks_test.rb --name test_capture_lease_abrupt_dispatcher_loss_closes_both_mediated_peer_channels
nix develop .#dev-workspace --command ruby test/workspace_host/commands_and_locks_test.rb --name '/capture_lease|non_streaming_provider_dispatch/'
nix develop .#dev-workspace --command ruby test/workspace_host_test.rb
```

The focused file loads the actual host through its existing support file;
the final command is the package's existing Ruby test entry at
`nix/workspace-portal.nix:254`. Root can use the normal exact-head hosted D
Check fast job, which evaluates checks and builds every check except the
host-module VM check, without adding a workflow or a VM campaign. After
accepted publication and the canonical mechanical E input reselection,
E's existing hosted `nix flake check --print-build-logs` must establish the
new exact composition, including `checks.x86_64-linux.compatibility-package`
that actually failed. Do not claim old E evidence covers a new D pin or
blindly rerun the unchanged failed revision. Preserve the user prohibition
on local CI/tests and the normal committed affected-review gate.

This changes only ephemeral test publication. Public commands, exit mapping,
lease channels, generation/ownership checks, on-disk schemas and package
transition policy remain unchanged. There is no state migration, activation
or operational rollback step. Reverting the fixture repair would restore the
observation race; it cannot repair or invalidate retained guest state.
Root owns acceptance, implementation assignment, Git/pins, hosted execution
and evidence interpretation. No runtime action or cleanup follows from this
diagnosis.

### DIAGNOSIS / PROPOSAL: G14 resource observation command (2026-10-10)

Identity/current and roster17 were checked from the exact tracking CWD with
both markers absent; architect0 retains Astra/xhigh/design/workspace_write.
This is source diagnosis and a proposed repair boundary, not source acceptance
or permission for another campaign. Only this appendix changes.

**Evidence and limits.** Parent reports the one G14 wrapper ended naturally
at 21:35:58 UTC, native exit1 after 9m32s, without cancellation. Its attempt is
failed/incomplete at `starting-final-runtime`; no completed runtime-smoke
receipt exists. Public start, connection, identity/current-system commands and
the first services `sh -s` command exited zero. The reported services stdout
is 174 bytes, SHA256
`24be7ccc05dd98f193afde63d2c323b6ccc6750450d5313754ec08b748ccbaa8`:
available memory509583360 bytes, root available4164870144 bytes, zero PSI
averages and one unparsed17-byte line. These are the parent's bounded native
observations, not fresh guest measurements by this investigator. No private
stdout/receipt/config/account file was independently opened here.

The exact realized G source
`/nix/store/rm2h27hrml95lbwri4vcmg6f7jlkrbqp-source`, revision
`725c325e8b4971931e5d16df86bafa8584358ecb`, has
`tools/runtime-verify.rb:580–615` generating:

```sh
printf 'available_inodes=%s\n' "$(df -i --output=iavail / | tail -n 1 | tr -d ' ')"
```

GNU `df` does not accept `-i` together with `--output`; `iavail` already selects
available inodes. Coreutils9.11's exact
[option parser](https://github.com/coreutils/coreutils/blob/v9.11/src/df.c#L1521-L1586)
exits with failure for this combination before filesystem reporting. The
[GNU manual](https://www.gnu.org/software/coreutils/manual/html_node/df-invocation.html)
documents that exclusion and field meaning. G's immutable lock/source receipt
selects guest nixpkgs `5dfba6236110080a54247d6460bc2ff5dda939cc` through OS6bdf;
the retained public services-payload baseline's `sw/bin/df` resolves to
`/nix/store/gph17gb73p6qbrqqjnypfjj5npf0ldyx-coreutils-9.11/bin/coreutils`.
That baseline supports the selected interface, not a fresh G14 executable or
liveness proof. No `df`, guest command or reproducer was executed here.

The source explains why SSH can still return zero: the pipeline returns the
last formatter's status, then the enclosing successful `printf` masks a failed
substitution. `set -eu` alone does not preserve the producer's failure here.
An empty inode payload does not match the numeric-field parser. The required
key-set assertion at599 then emits exactly `services real resource observations`.
This is an established command-interface defect and a source-supported cause
consistent with the native failure; the unparsed line and native df stderr
were not independently inspected, so their exact historical bytes are not
asserted. It is not evidence of resource exhaustion. The numeric headroom
checks follow this assertion; node observations and later read/lease/lifecycle
smoke were not reached. The supplied root byte count exceeds1GiB, but neither
that snapshot nor zero PSI averages proves overall profile/capture sufficiency.

**Proposed minimal correction.** Own `tools/runtime-verify.rb` and its existing
`tools/test-runtime-verify.rb`. Request `df --output=iavail /` without `-i`.
Capture each df result in a standalone, status-checked assignment before
formatting its captured text. Use the same producer-status discipline for the
existing memory/ZFS observations in this small method, where a substitution
inside `printf` has the same masking property. Preserve public `ssh -- sh -s`,
native stderr/exit retention and all numeric/PSI/headroom validation. Do not
substitute zero, skip inodes, weaken thresholds, increase resources or rely
solely on `pipefail` inside an enclosing successful printf. No engine, guest,
schema, provider, capacity or lifecycle policy change is needed.

The current `resource_transport` at tools/test-runtime-verify.rb:469–477 returns
synthetic numeric output without executing the supplied shell; those tests
remain useful parser/admission coverage but cannot catch an invalid df option.
Add bounded hosted coverage that executes the actual generated services script
with the declared GNU tools, checking numeric byte/inode fields independently
of the hosted machine's available capacity. A small method returning the
existing script is sufficient if needed to test its actual bytes. Cover a
controlled nonzero df producer and missing/malformed numeric output: no resource
success receipt may be published. Preserve existing insufficient-byte/inode/
memory/quota and PSI retention cases. Do not duplicate a corrected command only
in the test, add another VM campaign, or execute these tests locally.

The affected hosted selector is `nix develop --command ruby
tools/test-runtime-verify.rb`; existing `bin/check` includes it at51. Root owns
the normal exact-head source checks, committed affected review, canonical E
reselection and package evidence if it accepts this proposal. E currently
selects G through `02ed6dae758cc99b8ba58a18edb07021762c0555`; old checks do not
certify a corrected source. Reverting this verifier-only repair would restore
the measurement defect; no state conversion or operational rollback follows.

**Next supported decision.** Root can accept this narrow source repair while
retaining G14's native failed attempt unchanged. `Campaign#run` at230–253
refuses an incomplete attempt, and capture requires a completed same-input
runtime receipt. Do not replay G14, manufacture a receipt, transplant source
identity, upscale, reset, launch another pair or proceed to capture. A later
real continuation requires its own explicit root disposition and fresh owned
state/liveness/capacity assessment after the source gates; this diagnosis grants
none of those operations. G14, G13, G4, G6, isolation3 and preview remain intact.

## PROPOSAL: separate G725 retained-instance smoke and captures (2026-10-11)

This bounded continuation supersedes only the handoff's selection of no further
action. It does not turn the failed G14 campaign into a completed qualification.
Root accepts the operation packet and source correction below before execution;
this section records source analysis, not operational certification. Identity
and roster revision 17 were checked from the exact tracking directory with the absolute
public dev-session CLI, login:false and both markers absent. The retained
architect settings remain unchanged. Required workspace procedures and K owning
guidance were read; no private campaign inputs, accounts, credentials or serial
logs were opened, and no runtime/check/build/ref operation was performed.

**Recommendation and evidence.** Reuse the stopped G14 instance through ordinary
public resume with its original immutable K generator
`725c325e8b4971931e5d16df86bafa8584358ecb` (G725). Do not allocate another pair.
`finish-continuation-g14-retention1.json` records a successful separate public
stop and a fresh stopped/nonready, complete, all-recorded-processes-gone
observation, absent own claim/socket namespace and unchanged disk identities.
The instance is `31f2a709-4906-45fe-8224-dec594ce9471`; its accepted artifact is
`48591a1e-11b3-4d46-af34-8b4f3a3a5985`, digest
`7b677e1be8f1407f877e768f4d5e6af7058595cc06ae24eea3d4ef4020a11a16`.
These are retained snapshots; public resume must reprove its own prerequisites.
The failed attempt hash
`f5a7f1c287912b1beb6d1608d4e66c670599265e571dd9786317126ad5954125`
and absence of a completed campaign receipt remain unchanged.

The exact source is `/nix/store/rm2h27hrml95lbwri4vcmg6f7jlkrbqp-source`.
Its `cluster/lib/kb_runtime.rb:146–188` requires exact selected metadata,
credentials, original configuration, complete prepared artifact, retained disks,
no pending update and proven stopped state; `resume` then starts the same
artifact with a fresh run ID. It does not build an image or copy a root disk.
`cluster/launcher.rb:53–57` rejects replacement config/topology/network on resume.
The public runtime does not consult the verifier campaign. In contrast,
`tools/runtime-verify.rb:230–253` refuses the existing incomplete attempt, and
its bilingual phase requires a completed same-input runtime receipt. Therefore
do not invoke that campaign again, erase its attempt, fabricate its completion,
instantiate Campaign to call private phase methods, or place a new campaign
identity around the old state. Use a separately named finite public-operation
evidence unit outside the failed campaign, with its own native outcomes.

Final reviewed K `22e2fb772f69ec1f5e32e3a8d314ab3ffb63d3cd` differs from G725 only
in `tools/runtime-verify.rb` and `tools/test-runtime-verify.rb`; the retained
review establishes all other 257 paths/modes unchanged. This supports relevance
to unchanged runtime/capture code, not a claim that K22 guests or the whole K22
verifier passed. K22 resume would correctly reject a G725 prepared source.
Never substitute G725 metadata into a K22 runtime/capture executable.

**Exact public selection and finite sequence.** Use the genuine G725 packages:

- runtime `/nix/store/iz66p9qv5aybgkm4lq6ich7jgma04zrk-vpsfree-kb-devcluster`;
- capture/validator `/nix/store/v9j7ym82bxfp6gw1h41zww17j49afgnv-vpsfree-kb-capture`;
- metadata `/nix/store/n5vvjlikqjbvipicfs218zpvwvkcq0l6-vpsfree-kb-runtime-source.json`;
- existing selection `/nix/store/mz39kh0vk87h10xkhsn5lppw2gyc7q7p-vpsfree-kb-verify-selection.json`.

Root verifies retained package/closure availability and uses the selected
PATH/Ruby/Node/browser/font/CA environment in a private ordinary directory.
No source override, workspace provider activation, new package build or image
preparation is implicit. Use the existing durable user-service context and fresh
watcher, exact controller admission/tuple/cgroup facts, finite command deadlines
and reserve monitoring. `finish-continuation-user-lifetime1.json` confirms the
already-active user manager, RuntimePath and Linger=yes; it is not a new unit or
live-run proof. The prior controller, service status or copied PID is not
authority over the next run.

1. Bind the separate evidence unit to the failed-attempt hash, exact G725
   selection, accepted artifact, stopped snapshot, capacity decision and current
   private state-root path. Recheck normal owned state/claims/resource admission.
   Run the G725 public `vpsfree-kb-devcluster --state-root STATE resume same-slug
   --timeout 900`, without config/topology/network overrides. Retain fresh public
   status and connection privately. Require the same instance/artifact, a fresh
   run and normal exact source, guest metadata, current system closure and SSH
   host-key proof. No adoption, refresh or manual acceptance is involved.
2. Use public `ssh same-slug services -- sh -s` and the corresponding node1
   command with the exact reviewed K22 `resource_script` shell bytes. Record
   those script hashes and K22 origin separately from the G725 system under
   observation. Do not instantiate the failed verifier to obtain or run them.
   Preserve status-checked producers, numeric memory/bytes/inodes/ZFS fields,
   PSI, existing thresholds and private native diagnostics. No zero fallback or
   interpretation of a parser failure as resource success is permitted.
3. Reuse G725's existing `read_smoke` JS composition at
   `tools/runtime-verify.rb:535–578` as a finite public-operation command: exported
   `readConnection`/`openLease`/`Connection`, `inventoryIdentity`, browser `login`,
   `goto` and `assertInventoryMember`. Hold the real public lease, verify exact
   G725 source/guest closures, dedicated admin/member API identities and TLS,
   and ordinary member PHP access. Close the browser before releasing the lease.
   The helper imports existing code; it does not call Campaign or private
   lifecycle methods. Retain only allowlisted identity/result fields publicly.
4. Exercise live public lease exclusion, EOF, owned-controller interruption and
   reacquisition using the repaired observation helper described below. Retain
   wrong-source-before-SSH and explicit endpoint-routing checks. While the
   lease is held, public stop/update/reset must return 75 with protected state
   unchanged; update uses only the original private config. No queued destructive
   request, guest signal or broad process scan is allowed.
5. Establish the existing root/data sentinels through public SSH only after
   checking their exact dedicated paths are absent; never overwrite an
   unexpected file. Hash all six credential files, accounts, accepted/prepared
   artifact and original config without publishing secret contents. Record disk
   device/inode/size and guest closures. Perform ordinary G725 public stop with timeout 900,
   require stopped/complete/all-gone and normal socket/claim cleanup, then
   ordinary G725 resume with timeout 900. Require fresh run, same artifact/source/closures,
   same six credential/account bytes, same disks and sentinel hashes. Accounts
   may be atomically rewritten from the same config, so their inode is not a
   continuity invariant. Verify real resources and API/PHP identity again.
6. Only after those results and capture-specific resource admission, use the
   same resumed instance for the two selected canonical images. From an ordinary
   CWD different from the output directory, invoke packaged capture with
   `--cluster same-slug --state-root STATE --language cs --checkpoint
   networking/ip-address-list --output-root OUTPUT`. Obtain a fresh private
   public connection descriptor, then use `--connection DESCRIPTOR --language
   en --checkpoint networking/ip-address-list --output-root OUTPUT`. Retain the
   existing optional EN invocation from OUTPUT without `--output-root` if
   default-CWD proof remains selected; it replaces that same EN result, not a
   third exported bitmap. Both languages share one private writable output root.
   Existing physical artifact locks, live leases, source validation and dedicated
   ip-inventory fixture remain intact. No NAS/traffic fixture or extra host VM.
7. Run the G725 packaged validator `--update --output-root OUTPUT`, then strict
   `--output-root OUTPUT` without allow-missing. `runner/validate-artifacts.cjs`
   uses unchanged source assets for the rest of the 120-variant inventory and
   requires verified result rows for both changed images. Export through existing
   `KbCaptureArtifacts.export` under its physical output lock: exactly two PNGs,
   captures.json, tmp/capture-results.json and tmp/capture-source.json. Preserve
   source hashes, merged two-row provenance, export hashes and root visual
   acceptance; no connection/credential/config/raw transcript export.

Each stage has a native result, and the first unexpected failure ends this
finite evidence unit. No automatic retry, third qualification, upscale, new pair,
reset, unlink, unit retirement or cleanup follows. A successful bounded result
means the listed G725 public behavior was observed; the original G14 finite
verifier still failed. Historical upgrade/two-root proof stays deferred. Normal
stop/resume here is the explicitly selected continuity test, not failed-campaign
replay. G4/G6/isolation3/G13/preview and their ownership remain untouched.

**Concrete verifier defect and minimal prospective repair.** G725
`tools/verify-live-lease.cjs:76–137` recursively hashes every non-image/non-log
file and includes its inode, then compares the full maps around each contended
public operation. Its exact current `processes-RUN.json` is included. The real
runner at `cluster/lib/devcluster_runner.rb:110–134,196–208` atomically replaces
that receipt every tracker pass, including unchanged bytes, approximately every
50ms. Thus healthy publication can change the comparison; the helper cannot
truthfully require that file's inode/bytes to remain frozen. This is an
established source defect, not a claim that it caused a completed native run.

Own only `tools/verify-live-lease.cjs`, its existing
`tools/test-ip-inventory.cjs` coverage and any necessary short owning-contract
explanation. Keep the whole protected map comparison for identity, launch,
ready, phase, credentials, accounts, config, artifacts, exact claim, historical
process receipts and every other retained entry. Select at most ONE dynamic
path, `clusters/same-slug/processes-<validated-current-run>.json`, only after
descriptor/launch/instance/artifact binding. Do not ignore all JSON files,
globally ignore process files, suppress the tracker or compare only a few
convenient fields from otherwise protected records.

Read that exact live receipt under the validated private instance directory as
a bounded owned ordinary 0600 file with no symlink following and fd-based
size/mode/UID validation; expected atomic
replacement is allowed, unsafe/malformed/missing reads refuse. Validate schema 1,
all four instance/run/artifact fields, complete=false during a ready held lease,
and the exact authenticated runner identity/launch arguments. Bind runner boot,
UID, PID/start, executable and argv to the established runner tuple, using the
existing K ProcessIdentity read contract where native matching is needed rather
than introducing a second identity protocol. Validate well-formed unique child
identity keys and the same boot/UID, retaining every previously observed
PID/start identity while permitting newly discovered descendants. Recorded
children need not all still be alive; a valid tracker retains exited children.
Do not impose immutable executable/argv on an ongoing child's legitimate exec
transition: if checked, use the existing exact live-or-gone identity semantics.
The authenticated runner's append-only publisher is the receipt authority; this
snapshot is not a globally atomic process-tree or complete-exit certificate.
The public lease/ready checks and ordinary stop's complete descendant proof
continue to own those guarantees. No cleanup or signalling authority comes from
the helper's process observation.

Use deterministic barriers with real owned files/processes in the existing
hosted Node test owner: atomically rename a new inode with identical valid
receipt bytes between snapshots; then a valid append-only child publication.
Both must coexist with successful protected-state comparison. Mutate a separate
protected file or claim and require refusal. Cover wrong run/instance/artifact,
changed runner, malformed/truncated record, unsafe mode/symlink, missing or
removed retained identities and foreign boot/UID. Keep existing heldController
readiness/EOF/loss/sole-reaper tests unchanged. Do not remove assertions, extend
deadlines or execute tests locally. The focused hosted selector is
`nix develop --command node --test tools/test-ip-inventory.cjs`, followed by the
existing affected canonical source checks and committed independent review
before real helper use; root owns exact heads and E's mechanical selection.

After that repair, the separately selected immutable helper source/revision is
recorded as the observation harness; its expected subject metadata argument is
genuine G725. Runtime/capture/guest selection remains G725 throughout. This is
an explicit two-source verification relationship, not a software-metadata
override or claim that a new engine ran. No engine, guest, provider, schema,
protocol, persisted-state or source-compatibility change is needed. Reverting
the helper repair restores a false-failure oracle without changing instance
state. Until its affected gates pass, hold the lease-evidence stage; do not
silently run the broken whole-map oracle or certify a skipped check.

**Incremental resources and provenance.** The fresh capacity record reports
141,578,555,392B free, 85,881,999,360B retained writable growth including G14 and
a 17,179,869,184B base reserve: 38,516,686,848B remains before assessed additional
browser/log/evidence overhead. RAM is 42,417,541,120B and shm is 28,162,588,672B.
These are snapshots, not future admission. G14's services root is already fully
allocated; its tank has 8,587,255,808B remaining growth, included once in that
total. Resume adds zero new 8GiB images, zero new 8GiB root copies and zero new 8GiB
tanks. It needs no guest build/import or 2GiB builder. Peak live guests remain
the existing two 2GiB machines; the 1GiB fixture VPS consumes the node's configured
resources, not another host VM. Retain the measured host/browser/shm margins and
guest root/inode/ZFS/fixture quota checks; reassess before capture. Template and
VPS writes consume the already reserved tank extent, not a second full tank.
New run metadata, logs, artifacts and any actually missing tool/store paths must
be assessed; do not reuse the new-pair staging charge or invent a scratch bound.
No cleanup credit or dismissal of older growth is involved. If a required
package path is missing or resources fail, stop for a concrete disposition.

The generator for successful images is G725, with its exact final PHP/vpsAdmin
pin `ebe4fab3d50a51bda1f94014ca95c73ba2a967a8`; it is never relabelled K22 or a
later helper revision. The final media commit M may follow the current source
lineage while retaining that genuine G725 generation provenance: root carries
back only the two PNGs and candidate inventory, retains the full five-file
evidence bundle separately, and runs the existing strict hosted canonical media
gate on M. Temporary G725 result/source receipts must not be presented as
current-M live receipts or rewritten to satisfy another package. Validate the
external bundle using G725's actual package. Select M in E's one canonical input
stream after media acceptance, preserving its own graph and unchanged provider.
No merge, deployment, workspace activation, production KB write, archive or
general retained-state cleanup is implied. The outcome is a verified handoff
with this narrower real evidence and explicit unfinished broader qualification.

### Reconciliation: current process publisher's temporary files (2026-10-11)

This closes the observation boundary in the preceding helper proposal, within
the same two source/test owners; it adds no runtime or cleanup authority.
Current/binding and roster revision 17 were reverified, with retained architect
settings. Immutable G725 `cluster/lib/kb_state.rb:82–97` creates
`path + "." + SecureRandom.hex(12)` using EXCL/NOFOLLOW and mode 0600, writes,
flushes/fsyncs, closes, then renames it onto the published record. Consequently
the walker can legitimately see an empty or partially written temporary file,
or a listed entry can disappear before lstat/open. Excluding only the published
process receipt still permits false comparison/read failures. This is source
evidence, not a claim about a historical native interleaving.

After validating the current descriptor, launch, instance/artifact and private
instance directory, derive the exact published process-receipt path P. In that
directory only, distinguish P and names matching the entire escaped basename
of P followed by `.` and exactly 24 lowercase hexadecimal characters. This is
the one authenticated current publisher's unpublished-output namespace, not a
general `.json.*` exclusion. Never derive the exception from an arbitrary name
discovered during traversal. Wrong-run/historical receipt temporaries, matching
basenames in another directory, wrong suffix lengths/characters, protected
record temporaries and all unrelated entries retain ordinary comparison/refusal.

Recognized temporary entries do not belong in the durable inode/content map.
When present, they must still pass private-parent and no-symlink, ordinary-file,
current-UID, exact 0600 and existing bounded-size metadata checks. If opened for
descriptor validation, use NOFOLLOW and validate fstat against the observed
safe file; do not accept an observed inode substitution at the same temporary
name. No content parse/hash or minimum nonzero length is required: the writer
has not published a JSON document yet. The mandatory separate validation of P
still requires complete valid JSON and the bound process identities; a matching
temporary file cannot replace or excuse a missing/malformed published receipt.

Handle ENOENT only at the metadata/open boundary for one such recognized
temporary entry listed by this traversal: its rename/disappearance is expected,
so continue without retrying the walk. Do not swallow EACCES, ELOOP, ENOTDIR,
unsafe metadata or other I/O failures; an unsafe observation already made must
refuse even if the name subsequently disappears. No general ENOENT rescue for
published/protected paths, directory disappearance or arbitrary entries. A
successfully opened safe descriptor may remain valid after its name is renamed.
This is a bounded observation of the producer's publication protocol, not proof
of a globally atomic tree or permission to remove unpublished files. No State
change, producer pause, new lock, retry loop or ignored-file framework is needed.

Extend `tools/test-ip-inventory.cjs` in the same hosted-only selector with a held
atomic writer using real private files and deterministic barriers. Hold the
exact current temporary file after create, after a partial write and after
fsync/before rename; the protected snapshot must remain comparable while P
continues to validate. Release the actual rename and verify the new published
receipt through the existing dynamic-record checks. Deterministically place
rename between enumeration and temporary lstat/open, requiring acceptance of
only that missing temporary entry without sleeps or longer deadlines. Keep a
simultaneous unrelated/protected mutation detectable. Cover a historical-run
temporary, same basename in another directory, malformed suffix, symlink,
wrong mode/owner or oversize metadata, and missing/malformed published P.
Preserve the existing live-lease/control/reaper assertions and all earlier
negative cases. Source/hosted/review gates remain unchanged; no test or runtime
operation was executed for this clarification, and mutable remediation was not
inspected.

## DIAGNOSIS / PROPOSAL: node SSH identity after G14 resume (2026-10-11)

This is a source-supported diagnosis and prospective boundary for root
acceptance, not implementation or permission to retry the ended continuation.
Current was verified from the exact tracking CWD with login:false and absent
environment markers. The supplied fresh roster17 binds the same workspace,
slug and architect0 Astra/xhigh/design/workspace_write. Required workspace/K
guidance and the reached OS instructions were read or reused unchanged.
No private configuration, accounts, passwords, raw serial, live SSH/keyscan,
process probe, test, build or lifecycle command was performed here.

**Observed native facts.** `finish-continuation-public-smoke1-failure-proof.json`
records native exit1 at the first public G725 resume. The corrected observation
harness is `8e1804afce64ebe63cf623f098cf1a4032ca37e8`; the actual runtime and
prepared guests remain `725c325e8b4971931e5d16df86bafa8584358ecb`.
`finish-g14-resume-key-observation1.json` adds the named 09:50:24Z snapshot:
the same G14 instance/artifact, new run
`91c20a6a-948a-447c-aeb1-338b9581a0b4`, phase verifying, ready=false,
processes.complete=false, matching recorded runner and14 children, and retained
own claim/socket namespace. These are bounded live observations, not complete
exit proof. The original failed Campaign and new failed public unit remain
failed; resources/API/PHP/lease/continuity/captures were not reached.

The stored successful node1 scan at `[127.0.0.1]:25401` contains RSA fingerprint
`SHA256:60a2lUGJUPU0KdF0hkNxe+MEK5dQsfk9idN+9J8GGhc`; retained RSA is
`SHA256:MDzw+Oh8vPiBjVhyL60D1Rcs8FfPJaxHQZBVyceyfXA`. Its additional Ed25519
key was not in retained trust. Services' stored RSA fingerprint matches its
retained RSA exactly. The known_hosts digest remains
`43526b5eda9872d8868506788b86f3f1139c8a2139afe605ce6a81c3204d28d3`.
Thus different node RSA public-key material is established by the parent's
stored-byte comparison; this is not solely key ordering or an extra algorithm.
No private host key or historical guest key-generation event was inspected.

**Exact source path to the refusal.** In immutable G725
`/nix/store/rm2h27hrml95lbwri4vcmg6f7jlkrbqp-source`,
`cluster/lib/kb_runtime.rb:179–188,274–339` resumes the already accepted artifact
with a fresh run, waits for the runner marker, marks verifying, then establishes
SSH trust before guest source/closure attestation and readiness. At617–683,
discovery compares each normalized scan line against retained known_hosts and
refuses any newly observed untrusted line without replacing trust. Only empty
first-contact trust can be initially written, after all endpoints succeed.

`ssh_host_keys` at765–795 checks the exact endpoint, supported key type and SSH
wire structure, ignores comments/blank lines and normalizes inter-field
whitespace. Comparison is membership, so ordering and a subset of already
trusted keys do not cause this refusal. A newly observed key type absent from
initial trust can separately refuse even if another key is unchanged; native
first contact retained only RSA for both machines. That strict superset behavior
is a distinct observable limitation, not an alternative explanation for the
changed RSA. Do not weaken it or silently expand trust as part of persistence.
No transport exception, deadline expansion or retry repairs changed key bytes.

**Guest persistence source.** Exact OS source is
`/nix/store/m7lppk7djkzqvrddvj0f2aa05sywl5d3-source`, revision
`6bdf458fd9105379860234ff33d352e55844f08f`:

- G725 `cluster/nix/test.nix:1318–1327` enables SSH and supplies the client
  authorized public key, but configures no persistent host-key paths. The node
  module at1830–1860 adds source shares and networking, not host-key persistence.
  `mkNodeMachine` at1908–1930 gives the vpsAdminOS node one tank file disk and
  imports the existing pool-tank module. The source shares at1196–1240 mount
  repository sources under /mnt; they are not an SSH-state store.
- OS `tests/configs/vpsadminos/base.nix` supplies `root=/dev/vda`.
  `osvm/lib/osvm/vpsadminos_machine.rb` attaches squashfs read-only as boot
  media. `os/modules/system/boot/stage-1-init.sh:78–115,153–175` defaults to live
  mode and mounts the root on tmpfs; the squashfs provides the read-only Nix
  store with a volatile writable overlay. It does not persist /etc simply
  because a tank disk exists.
- OS `os/modules/services/networking/sshd.nix:31–48` creates /etc/ssh and runs
  ssh-keygen for each configured host-key path that is missing before starting
  sshd. `os/modules/nixos-modules.nix:47` imports the upstream SSH options.
  K leaves the host-key locations inherited. No node host-key persistence was
  found in the inspected K/OS modules. The exact effective inherited HostKey
  lines from G14's immutable node closure were not extracted in this task;
  root may close that final path-attribution detail with an allowlisted source
  read, without a guest command. Attempts to read the exact pinned upstream
  Nixpkgs SSH module through the web tool returned cache misses and supply no
  evidence. Do not represent an arbitrary other Nixpkgs checkout as that pin.
- OS `tests/configs/vpsadminos/pool-tank.nix` imports/creates the tank on sda.
  K `cluster/lib/kb_machine.rb` PreparedDisks and `kb_disks.rb` preserve and
  validate that tank's device/inode/size on resume. Only NixOS machines also
  have a retained writable root copy. OSVM preserving the node tank therefore
  does not preserve the node's volatile root filesystem.

This source arrangement supports reboot-time regeneration of missing node host
keys as the cause of the real mismatch. The exact historical syscall sequence
was not observed, and no current guest filesystem was read. The persisted
services root and its unchanged RSA provide a consistent contrast, not proof
of the node's historical file events. The six host-side dedicated credentials
contain the SSH *client* key and TLS material, not the original node SSH private
host key; unchanged six-file hashes cannot establish server-key continuity.

**Smallest prospective boundary.** Keep this in K's dedicated node configuration
(`cluster/nix/test.nix`, or a small K-owned imported node module if needed), not
an OS-wide SSH behavior change. Use the existing `services.openssh.hostKeys`
option to put each node's generated private host keys in a dedicated root-only
directory on its existing tank, for example `/tank/.vpsfree-kb-ssh`. Preserve
the selected key types/parameters and strict client discovery policy; do not
introduce hardcoded/shared private keys, store private keys in a Nix derivation,
reuse the client key as a server key, or add a host credential/state schema.

Order the node's existing runit sshd startup before its original generation
loop using the existing `waitForService pool-tank` mechanism, then positively
check the expected tank filesystem is mounted at the intended persistent path
before creating/using the private key directory. A directory named /tank on
tmpfs is insufficient. Refuse unavailable/wrong storage or unsafe existing key
paths; do not generate a fallback identity on the volatile root, copy an
untrusted current key over an old key, or overwrite existing keys. Keep existing
key generation in its owner where feasible. If preserving that owner requires
more than a small K prefix/path selection, refer the concrete deviation before
expanding source scope.

OS `os/modules/tasks/filesystems/zfs/pool-service.nix` mounts the pool/datasets
before completing its one-shot service; runit `helpers.sh:104–121` provides the
service wait, and runit/default.nix publishes the one-shot done marker only
after its run body completes. This ordering can therefore gate SSH on mounted
persistent storage without a new supervisor. Pool startup waits for osctld,
whose inspected startup path does not wait for sshd. Retain the existing public
readiness deadline and failure/retention behavior; do not create a new timeout
or kernel/resource requirement. The keys consume the existing tank and add no
new disk or VM to the reduced profile.

**Existing G14 cannot be repaired through the accepted public continuation.**
G725 public resume accepts neither a replacement config nor another source;
`validate_prepared` enforces both. A new controller cannot retrofit persistence
into that immutable guest artifact. Public update requires a ready predecessor
and strict old-trust guest attestation (`kb_runtime.rb:191–219`), which this
verifying run lacks. The original trusted private node key is not established
as recoverable by any supported public source contract. Do not edit known_hosts,
prepared records, artifact/source metadata or the guest, invoke a private shell
or Engine mutation, use a new source with old metadata, or retry for a lucky key.
The proposed persistence fix is for a new genuinely prepared source/artifact,
subject to root's separate source and later operational acceptance. It does not
authorize a new pair, stopping this run, reset, adoption or disk reuse.

**Compatibility, recovery and verification.** Runtime schema2/connection1,
disk layout, six credentials, TLS, endpoint ownership and ordinary public
commands remain unchanged. New supported instances retain their generated
server keys on the existing tank across same-artifact stop/resume. Future
updates between implementations preserving the same paths/key policy can keep
those keys. Older volatile-key instances receive no automatic migration, and
rolling a corrected guest back to the old volatile-key configuration does not
promise SSH continuity. An old controller's ability to read state or request a
proven owned stop is not an upgrade/recovery path. No production node rollout
or coordinated OS upgrade is proposed; this is the dedicated K runtime only.

Before implementation, confirm the effective node host-key paths/types and
mount/service ordering from the selected immutable/module output. Add focused
hosted coverage for the actual generated node startup configuration: storage
gate precedes key generation; initial keys are private; a second boot preparation
on the same persistent directory preserves their fingerprints/bytes; unavailable
or wrong storage refuses rather than using tmpfs. Keep current client trust
tests for changed material, wrong endpoint, malformed wire data, reordered and
partial sets, and record the intentional extra-key-type refusal. Do not mock
away key generation in the new persistence test or call fake machine resume
coverage proof of guest persistence. Existing `tools/test-runtime.rb` owns
trust assertions; K's generated-module/key-preparation coverage and short
`cluster/runtime-contract.md` explanation own the new guarantee. No local CI.

Only after the new exact source, affected hosted checks and committed review
may root consider a separately admitted finite real test: genuine initial
attestation, ordinary stop/resume, unchanged server-key fingerprints and
known_hosts plus all six credentials/disks/sentinels/source closures. That test
needs an explicit resource/state disposition and is not launched or selected
by this document. No new operation can inherit success from the two failed G14
units. Current G14 is retained nonready/live in the latest snapshot; all older
campaigns and preview remain untouched. The immediate deliverable is this
bounded prospective fix and the explicit unsupported-current-artifact limit.

### Final bounded proposal and stopped-state evidence

The later parent evidence `finish-g14-resume-refusal-stop1-proof.json`
supersedes only the preceding live-state snapshot. A separately selected genuine
G725 public stop returned native 0 in approximately 51 seconds. Its guarded
09:59:07Z observation records phase stopped, processes.complete=true, runner
and all 14 recorded children positively gone, and own claim/socket namespace
absent. The disk identities, retained known_hosts and original failed Campaign
hash are unchanged. No reset, unit retirement or readiness repair occurred.
Both failed verification units remain failed; this successful stop supplies no
resume/capture success. These are parent-provided observations, not operations
performed by the design owner.

The proposed implementation boundary is one K node-module change (directly in
`cluster/nix/test.nix`, with a small imported K module only if that makes the
generated startup testable), focused hosted coverage, and the owning runtime
contract. Keep the current OS ssh-keygen loop and select persistent paths for
its configured keys. Use `lib.mkBefore` on the node sshd run body to wait for
the existing pool service, validate the actual tank mount and prepare the
private directory before that loop. Do not replace the SSH daemon, alter the
shared services VM, add an OS input change, or alter the runtime trust reader.
The effective types/parameters must be read from the selected evaluated module
before choosing equivalent persistent declarations; an arbitrary Nixpkgs
version or guessed default is insufficient.

Hosted coverage must check the generated module, not merely search Nix source
text for a path. Evaluate the small node declaration with the repository's
pinned inputs and project the actual hostKeys, sshd run body and pool-service
dependency. Assert that every private host-key path is under the chosen tank
directory, that configured key types/parameters are intentional, and that the
storage gate precedes every key-generation command. Preserve the existing
service body and services-machine behavior. This declaration/ordering proof
does not require booting a VM or rebuilding a kernel.

For the small startup boundary, use a hosted private temporary directory and
execute the generated preparation/generation body with controlled storage
observations and real ssh-keygen. Test initial private creation and a second
invocation preserving every private-key byte and public fingerprint. A held
pool-ready condition must prevent any key generation until released. An absent
pool, tmpfs directory masquerading as /tank, wrong dataset/mountpoint, unsafe
directory/key type or mode, and preparation failure must prevent generation
and daemon start without overwriting existing keys. Mocked mount observations
prove branching and ordering only; they are not a real ZFS or reboot claim.
Do not construct a generic service simulator. Wire this focused coverage into
the existing hosted `nix develop --command bin/check --allow-missing` source
gate; `tools/test-runtime.rb` remains the owner of existing trust/refusal tests.
If a new small test owner is needed for evaluated Nix output, include it in the
same gate rather than introducing another workflow or runtime framework.

Keep the current wrong-key, malformed-wire, wrong-endpoint and no-trust-rewrite
tests. Add explicit set-order/subset/extra-type cases only where existing tests
do not already establish those semantics. A first-contact scan that records
only a subset of enabled server algorithms can still encounter the existing
extra-key-type refusal later, even after key persistence is fixed. This
separate strict-discovery limitation is not solved or silently relaxed by the
proposal; the eventual finite real proof must record the offered/retained key
sets as well as unchanged fingerprints. A concrete further source requirement
at that boundary must return to root before implementation scope grows.

Current stopped G725 remains unsuitable for readiness repair: no public resume
can apply the new node configuration to its accepted artifact, and it cannot
supply the ready, trusted predecessor required by public update. Stopping it
does not change those facts. Root must accept the prospective source boundary
and separately choose any later genuine new preparation/admission. No new
attempt, disk reuse, trust edit or resource cleanup is implied here. Only this
design file was changed; no hosted or local check was executed.

### Stable node host-key set: concrete prospective choice

For root acceptance, narrow the preceding key-declaration proposal to **one
explicit Ed25519 host key for newly prepared dedicated K nodes**, at a fixed
private path such as `/tank/.vpsfree-kb-ssh/ssh_host_ed25519_key`. This supersedes
the suggestion above to reproduce the inherited multi-key defaults. Declare
the complete node `services.openssh.hostKeys` list and verify the resulting
sshd configuration advertises exactly that key, without another inherited
HostKey entry or default-key fallback. Keep the services VM unchanged.

This is a deliberate new-guest configuration choice, not acceptance of the
Ed25519 key observed on G14. The pinned OS generation loop accepts configured
key types, the native resumed node already offered Ed25519, and G725's strict
wire parser already supports it. No new client algorithm or Engine behavior is
required. The same selected key path and algorithm remain part of the supported
node configuration across subsequent boots and compatible updates. With one
configured key, successful first-contact discovery cannot record only RSA and
later encounter an additional node algorithm. Missing or unusable persistent
storage/key preparation must prevent sshd startup; it must not enable another
key or fall back to volatile storage. Existing private keys are never replaced
merely because a client cannot authenticate them.

The source owner remains the K node module and its small pre-generation storage
gate. The order is: pool-tank completion; positive expected mounted-filesystem
proof; private-directory/key-path checks; the existing OS generation loop for
that one key; sshd start. Hosted declaration tests must inspect the evaluated
hostKeys **and actual sshd_config HostKey entries**, proving the single
Ed25519 persistent path and absence of implicit RSA/ECDSA/other paths. The
generated-startup test must run real Ed25519 generation, preserve both private
bytes and derived public fingerprint on its second invocation, and prove that
negative storage/path cases cannot reach generation or daemon start. Retain
the strict Engine test that a previously unrecorded algorithm refuses without
changing known_hosts; test first/repeated valid single-key discovery as the
positive pairing. These are hosted source checks, not guest-reboot evidence.

Compatibility is intentionally limited to newly prepared nodes with this
configuration and later configurations preserving its key contract. G14's
original RSA-only trust, its new untrusted Ed25519 key, and its old ephemeral
artifact receive no conversion or enlargement. An existing multi-key or
volatile-key artifact cannot be labelled compatible merely because the new
configuration has a stable single key. A later deliberate algorithm/path
change would need its own compatibility decision; it is not an automatic
update or rollback promise. The stopped G725 unsupported-repair boundary and
all retained evidence remain unchanged. This additional choice needs root's
source acceptance before implementation; it authorizes no operation.

### Reconciled proposal: one host-key algorithm across the dedicated K profile

`finish-g14-effective-host-key-declarations1.json` closes the effective-default
gap above. From the exact selected immutable node closure
`/nix/store/wgd3z7bipn2z5sdnsf8s59gmcj7sfhbv-vpsadminos-system-node1-26.05pre-git`,
the parent extracted two HostKey declarations and their generation arguments:
RSA 4096 at `/etc/ssh/ssh_host_rsa_key`, and Ed25519 at
`/etc/ssh/ssh_host_ed25519_key`. The evidence binds the configuration/run-file
hashes and contains no private keys. Together with the exact live-root source,
this establishes that both configured node key paths were volatile. It does
not claim observation of the historical key-generation syscalls.

The final prospective choice is **one explicitly configured Ed25519 host key
per machine throughout K's dedicated SSH profile**, not only on the node. This
supersedes the preceding instruction to leave services' key declaration
unchanged. Preserving both defaults would retain the partial-initial-scan
problem even with perfect persistence: the current Engine accepts the first
valid nonempty key set, and another valid but previously unrecorded algorithm
later refuses. Fixing that while retaining multiple algorithms would require
additional discovery/completeness policy. The single-key declaration avoids
that change; trust remains strict and is never enlarged automatically.

Use the existing shared `sshModule` in `cluster/nix/test.nix:1318` as the one
algorithm owner, parameterized only by its host-key path. Its services and
other NixOS callers use `/etc/ssh/ssh_host_ed25519_key` on their ordinary
retained writable root. Its vpsAdminOS node caller uses
`/tank/.vpsfree-kb-ssh/ssh_host_ed25519_key`, with the previously specified
pool/mount/private-path gate before the existing OS generation loop. Explicit
parameterization avoids accidentally merging a shared root-path key list with
a second node-path list. The effective list and sshd HostKey declarations must
each contain exactly one entry; unrelated old key files must not be advertised
or deleted by this change. Optional NixOS DNS machines already import this
shared module, so inherit the same root-path declaration without a separate
policy or added real-VM campaign. No guest shares another guest's private key.

Ordering remains node-specific: pool-tank completes, the expected tank mount
is positively verified, private paths are prepared/validated, the existing OS
loop creates the one missing key, then sshd starts. Services retain the normal
NixOS host-key startup owner and retained-root behavior; add no tank dependency
there. The fixed algorithm and path must persist across supported subsequent
boots/updates. Empty discovery remains a normal discovery failure, not grounds
to enable RSA, fall back to volatile keys or extend deadlines. A successful
single-key scan cannot omit another configured algorithm because there is none.

Focused hosted declaration coverage must now include both machine types:
evaluate the actual selected K module configuration and assert exactly one
Ed25519 hostKeys entry and one matching generated HostKey line for services and
node. Check that only the node has the pool/storage prefix and that the prefix
precedes generation and daemon execution. Exercise the actual small generated
node preparation/generation path with real Ed25519 keys and controlled storage
observations: repeat invocation preserves bytes/fingerprint; storage/path
refusals neither generate a fallback key nor launch sshd. Existing Engine tests
must retain wrong-key/extra-algorithm refusal and unchanged known_hosts, with a
positive initial/repeated single-key case. Do not substitute textual source
searches for evaluated declarations or claim these hosted checks prove an
actual reboot. Wire only the focused test owner into the existing source gate;
no new workflow, dependency, guest topology or engine/state schema is needed.

This profile uses Ed25519 already supported by the pinned OpenSSH and runtime
parser; it intentionally does not promise compatibility with RSA-only external
clients. These are dedicated K endpoints, not production SSH policy. Older
multi-key/ephemeral artifacts, including stopped G725, receive no automatic
retrofit, trust rewrite or compatible-update claim. New services and node
artifacts must be genuinely prepared from the new source; source/closure and
six-credential checks remain unchanged. Rollback to a multi-key or volatile
configuration is not a supported continuity promise. Root source acceptance and
later operational disposition remain separate. Fresh current/roster revision
17 were reconfirmed; only this assigned design document was appended.

### PROPOSAL: reconcile the pinned runit string option (2026-10-11)

This explicitly corrects this design's earlier `lib.mkBefore` implementation
direction. The persistent single-Ed25519-key policy, storage refusals and OS
generation ownership remain accepted requirements; the stated string-composition
mechanism was wrong for the actual pin. Root source acceptance is required
before the implementer changes the frozen source.

At published K `5bf3be8fb7ab6bd7a052ba6b8ae9522a50c33e04`, both native hosted
runs 38132390845 and 38132386751 fail every NodeSshTest case in configuration
projection, before the shell assertions. The retained failure record is
`finish-host-key-persistence-failure1.json`; full logs remain under
`finish-host-key-persistence-hosted1/{k,k-runtime}/full.log`. The earlier native
runtime 101/1263, closure 12/51 and machine 34/1244 results passed. None of those
results establishes that the new node configuration evaluates or its real key
preparation passes. E remains watcher-owned; no rerun or workflow polling was
performed for this diagnosis.

**Cause and supported interface.** Exact OS
`6bdf458fd9105379860234ff33d352e55844f08f`, immutable source
`/nix/store/m7lppk7djkzqvrddvj0f2aa05sywl5d3-source`, declares service `run` as
`types.str` at `os/modules/system/boot/runit/default.nix:18–21`; services are
`attrsOf (submodule service)` at584–587. Its SSH module supplies the single
key-generation/daemon body at `os/modules/services/networking/sshd.nix:31–58`.
There is no separate pre-start string hook in that pinned service declaration.
K's additional `run = lib.mkBefore ...` therefore supplies a second unequal
string instead of a prefix that the type can concatenate.

The committed K lock resolves root nixpkgs through root vpsadminos, then
vpsadmin/vpsadminos/nixpkgs, to node `nixpkgs_2` at
`5dfba6236110080a54247d6460bc2ff5dda939cc` (not the unrelated lock node named
`nixpkgs`). Its `types.str` uses equality merging, while a function-valued
submodule definition is imported as a full module, allowing an option
declaration scoped to one service. The pinned module system applies an option's
`apply` function to the merged value. This is the supported composition point:
[pinned types.nix](https://raw.githubusercontent.com/NixOS/nixpkgs/5dfba6236110080a54247d6460bc2ff5dda939cc/lib/types.nix),
[pinned modules.nix](https://raw.githubusercontent.com/NixOS/nixpkgs/5dfba6236110080a54247d6460bc2ff5dda939cc/lib/modules.nix),
[pinned options.nix](https://raw.githubusercontent.com/NixOS/nixpkgs/5dfba6236110080a54247d6460bc2ff5dda939cc/lib/options.nix).
Relevant lines are types526–532/1109–1114/1206–1219, modules1056–1061/1156–1158,
and options109–110/139–152. These exact public source bytes were read, not
evaluated. Two separate `apply` declarations would also refuse; do not add
fallback or override logic to hide that future conflict.

**Smallest source change.** In K `cluster/nix/test.nix` nodeModule, remove the
competing `run` value and install a function-valued module only at
`runit.services.sshd`. Extend that submodule's existing `run` declaration with
`lib.mkOption { apply = osRun: existingPreparation + "\n" + osRun; }`.
Here `existingPreparation` is the current committed pool/mount/metadata guard
body, preserved without changing its shell semantics. The prospective shape is:

```nix
runit.services.sshd = { ... }: {
  options.run = lib.mkOption {
    apply = osRun: existingPreparation + "\n" + osRun;
  };
};
```

The function-valued form is significant: the service type interprets an ordinary
attribute-set definition as configuration shorthand. Do not put `options` in
that shorthand, redefine `run`'s type/default, or read the resulting
`config.runit.services.sshd.run` from its own transform. There remains one OS
`run` definition, checked under its original string type, with K's preparation
applied once before it. No option-definition reflection, extraction of private
module internals, copied OS body, priority replacement, global runit change,
second generator or second daemon is needed. Other services and their run
options remain outside this extension.

The resulting order stays: existing runit helpers/environment; K's `set -e`,
pool wait, mount/metadata/private-key validation and umask; untouched OS missing
key generation; untouched OS daemon exec/config identity tail. The existing
generation failure still exits before the daemon because K's `set -e` remains
in that same shell. Preserve the shared services/DNS single-key declarations,
node tank path, all mode/owner/type/link checks and all readiness/trust rules.

**Hosted verification and owners.** `tools/test-node-ssh.rb:17–100` already
evaluates the selected pinned node configuration and projects the applied
`node.runit.services.sshd.run`. Keep that projection and its existing private
fixture execution; changing the composition interface does not justify bypassing
evaluation or hand-assembling the service in the test. Preserve all ten cases,
barriers, five-second bounds, real Ed25519 generation and refusal assertions.
The declaration test should additionally establish one pool-wait prefix, one
OS generation block and one daemon exec, in that order. Existing services/DNS
projections must remain unchanged and free of node storage dependencies. Adapt
only a projection assertion if necessary; do not weaken the generated-body
execution or replace it with searches of unevaluated source text.

Prospective application owners are only `cluster/nix/test.nix` and the existing
`tools/test-node-ssh.rb`. Root's runtime-contract prose already describes the
intended ordering without promising `mkBefore`; no behavior/documentation scope
expansion is needed. After a committed correction, select the existing hosted
source check (`nix develop --command bin/check --allow-missing`), which includes
`ruby tools/test-node-ssh.rb`, and the owning exact-input package/contract checks.
Root owns publication, affected review and interpretation. No local test, syntax
check, Nix evaluation, build or real operation is authorized by this brief.

There is no state/protocol/schema, OS/V/input, timeout, trust, resource or recovery
change. Rolling source back to the rejected composition restores an evaluation
failure, not a supported guest fallback. Old G725 remains stopped with retained
disks/trust and cannot be retrofitted. All failed packets/native evidence and
older campaigns remain untouched. Current and live roster revision 17 were
verified with retained architect0 settings; only design.md was appended.

### ACCEPTED FINISH BRIEF: working reduced runtime and bilingual captures (2026-10-11)

This section records `finish-working-delivery-plan1.md` and the user's explicit
clarification that finishing means getting the tooling working. A failed real
run establishes a blocker to diagnose and repair; it does not satisfy delivery.
Historical failed attempts and their limits remain unchanged. This brief adds
no product decision, runtime framework or speculative source work.

Root reports the K6645483/Efec9cd0 source, hosted checks, review and package gates
accepted. Reuse that exact-object evidence for unchanged content. Upstream
reconciliation is root-owned and starting: preserve reviewed patches and
migration lineage, resolve only actual integration conflicts, and settle the
final source selections before constructing the new environment. Accepted
source/package evidence is not current resource, guest or capture proof. Any
changed source must receive its required hosted checks and affected committed
review before the corresponding real verification; do not repeat unaffected
verification merely to restate an existing result. The no-local-CI constraint
remains in force.

**One reduced environment.** Use the existing public packaged single/local
runtime with one services guest and one node, each 2048 MiB RAM. The image
builder uses 2048 MiB and completes before the two guests start. Keep the
services image, independent writable root copy and node tank at 8 GiB each:
24 GiB intrinsic eventual file extent, not a universal admission floor. Bind
fresh source/package/configuration/identity and explicitly disjoint resources
through the existing registry and ordinary user-service lifetime context.
Refresh measured capacity, exact kernel/cache prerequisites and ports before
admission. Account retained sparse growth, closure/staging overlap, unknown
builder scratch, assessed headroom and host reserves separately; give no
unperformed cleanup credit and perform no automatic upscale.

The prepared G14 public reset still requires separate explicit approval because
it deletes its two retained test disks. Before any approved reset, root must
reprove stopped identity, complete recorded exit, own claim/socket absence and
preserved non-disk failure evidence. This brief grants no reset or unit-retirement
authority. G14 is not a source-compatible host-key retrofit candidate. Other
failed environments and preview remain untouched; neither their adoption nor
their cleanup is a prerequisite silently added here.

**Required real delivery sequence.** Through the existing immutable public
tools and normal fresh-watcher monitoring, establish:

1. A successful `runtime-smoke`: public start, exact guest identity and actual
   system-closure attestation, real resource observations, TLS/API identity and
   member PHP access, and live lease contention/loss/reacquisition semantics.
2. Ordinary public stop with positive complete exit, then supported same-artifact
   resume with a fresh run. Preserve all six dedicated credentials, accounts,
   disk identities, sentinels, server-key/known_hosts continuity and exact source;
   repeat the required live attestation. A partial boot or a source check cannot
   substitute for this continuity result.
3. From that same resumed environment, real CS and EN
   `networking/ip-address-list` captures using the existing minimal inventory
   fixture. Exercise the existing cluster, connection and packaged default-output
   paths. Strictly validate the full inventory, export only the two PNGs,
   candidate captures.json, merged results and source receipt under the physical
   artifact lock, and inspect both images. Preserve genuine generator provenance
   when media is later committed; export no private connection, account,
   credential or raw diagnostic material.
4. End the new environment with ordinary public stop and positive complete-exit
   proof. Handoff must have no running verification job or newly created guest;
   this does not authorize actions on older retained environments or preview.

**Demonstrated-blocker loop, with immutable attempts.** One native failure ends
that attempt and retains its exact receipt and private diagnostics. Diagnose the
actual failure, assign only its necessary repair from an accepted bounded brief,
add meaningful focused regression coverage when needed, and obtain the changed
source/hosted/affected-review gates. Then root may prepare a genuinely fresh
attempt using supported state/resource admission. Never replay or edit a failed
Campaign, transplant acceptance or identities, retry probabilistically, weaken
ownership/trust/storage guards, or infer cleanup permission from a failure.
An unsafe ownership/capacity refusal holds advancement until its concrete
prerequisite is resolved. The task continues toward working delivery; stopping
an individual failed attempt is not a completion claim. Historical upgrade and
two-root experiments remain deferred, not passed or prerequisites for these PNGs.

**Final source/media handoff.** Root owns final media acceptance, consolidated
E/C selections, project documentation, publication and the exact repository /
target integration inventory. Retained implementer owns actual application
repairs; retained independent reviewer owns affected review; fresh policy
watchers own uncertain-duration verification. Preserve the default-true database
migration, runtime schemas and no-old-artifact-adoption policy. Require actual
runtime/lease/continuity success, both genuine accepted images, strict validation,
consistent final branches/pins/docs and no unresolved Blocking or Important
findings before calling delivery ready. Integration, deployment, provider
activation, production KB writes and archival remain outside this approval.
The initiative stays active until exact-head integration and outstanding owned
obligations are resolved through their separately authorized paths.

Current, absent environment markers and live roster revision 17 were verified
from the exact tracking CWD with login:false; architect0 retains its saved
Astra/xhigh/design/workspace_write settings. The required workspace procedures
and documentation skill were read or reused unchanged. No concrete discrepancy
with the accepted working-delivery plan was found. Only this design section was
appended; no application investigation, source/ref/pin edit, check, CI request,
probe, package preparation or lifecycle operation was performed.

### DIAGNOSIS / PROPOSAL: inventory API version and bounded helper qualification (2026-10-11)

The real `member-read-smoke` blocker is the K inventory caller's unsupported
version prefix. Exact K87d51f0fb0a03f361ba7dfe9718d95af29772fc6,
`fixtures/prepare.cjs:455-493`, constructs `v1/RESOURCE`.
Selected V939159f27b5d627930281d5fac0c0aa9ba53bfc7 declares
`HaveAPI.implicit_version = '7.0'` in `api/lib/vpsadmin/api.rb:3`.
Its `resources/user.rb` Current action returns the authenticated user; the
existing API specs resolve the version through native OPTIONS metadata in
`api/spec/support/version_helpers.rb` and issue GET to the versioned route.
K's `tools/runtime-verify.rb:539-581` invokes `inventoryIdentity` after the
lease/source proof and before launching the member browser.

This is now native evidence, not an authentication hypothesis:
`finish-working-delivery-api-diagnosis1.json` records both dedicated accounts
receiving HTTP404 / status false / `Action not found` at
`GET /v1/users/current`. `finish-working-delivery-api-diagnosis2.json` records
both receiving HTTP200 / status true with `response.user` at
`GET /v7.0/users/current`, under the same attested instance/run/artifact and
public lease. These observations establish the route correction; they do not
establish browser, fixture, continuity or capture success. The original failed
Campaign and its native failure remain immutable.

**Minimal source boundary.** In K `fixtures/prepare.cjs`, give the inventory
caller one explicit `7.0` version constant and construct `v7.0/RESOURCE` for
all its existing resource actions. This is the contract of the selected V
input, not a configurable API version, discovery framework, fallback or retry.
Keep the existing HTTP methods, request bodies, success envelope and account
selection. Keep exact endpoint/Host/SNI/CA routing, Basic authentication from
recorded dedicated accounts, bounded responses, timeouts, lease assertions and
abort signal. Preserve member/admin identity and role checks, ordinary member
browser identity, dedicated-pool ownership/idempotence and all fixture guards.
No V, Engine, guest, server-key, profile, schema or dependency change is needed.
A nearby comment should identify the selected vpsAdmin API contract so a future
input-version change checks the caller explicitly.

The helper may improve its existing action-failure error with only the method,
known resource path and numeric HTTP status. Do not include Authorization,
account/password values, request bodies, arbitrary response messages/bodies or
query values in that diagnostic. A failure stays a failure before subsequent
fixture/browser work; it must not trigger route guessing or another request.

**Hosted regression boundary.** Own the correction in `fixtures/prepare.cjs`
and `tools/test-ip-inventory.cjs`. The existing transport mock at lines 37-63
strips `/v1/` and therefore models the erroneous caller as valid. Assert the
complete wire path before any resource normalization. In particular, assert
both identities use `GET /v7.0/users/current`, with the existing correct account,
TLS and lease fields, and verify full versioned paths for inventory actions
already exercised by the fixture tests. A `/v1/` or unversioned request must
not be accepted by the mock. Retain all current negative role/identity/lease
and disabled-pool rerun cases. Add a 404/status-false regression that refuses
before browser/mutation and, if diagnostics change, proves no synthetic secret
or raw response content reaches the error. Do not replace the wire assertion
with a test of an exported constant or a source-text check.

The existing hosted Check source route runs
`nix develop --command bin/check --allow-missing`, which includes
`node tools/test-ip-inventory.cjs`. Use that exact-head evidence and affected
committed review under the standing no-local-CI override. No new workflow,
dependency, broad test campaign or rerun of unrelated accepted evidence is
required by this brief. Root owns publication, corresponding E selection and
the source/package/review gates before any subsequent real qualification.

**Useful qualification on the existing environment.** After those gates, root
may separately select a finite read-only helper qualification without entering
or continuing the failed Campaign. Reprove the current genuine G87d public
connection, controller lease, exact G87d metadata/artifact and actual guest
closures with its matching immutable tools. Import only the corrected
`inventoryIdentity` (and unchanged member assertion, if used) from the newly
committed immutable helper source into the existing read-smoke composition.
Keep source verification directed at the genuine G87d guest metadata; record
the corrected helper revision and file digest separately. Use its two ordinary
current-user GETs, then the existing dedicated member PHP read if selected.
Do not call the provisioning fixture for this diagnostic. Preserve browser
cleanup before lease release and retain the native outcome in a new evidence
unit. This proves corrected caller compatibility against that pinned V server;
it creates no successful runtime-smoke receipt, guest update or canonical PNG.
It needs no replacement image or new VM for that limited claim.

**Final capture still requires a genuine matching artifact.** Changing
`fixtures/prepare.cjs` changes the source fixture digest. K
`lib/connection.cjs:236-264` compares the expected source with descriptor,
artifact and live guest identity, then checks actual system closures. Installed
capture from the corrected source therefore cannot accept the unchanged G87d
artifact. Do not override expected metadata, splice corrected fixture code into
an allegedly canonical G87d capture, or relabel the generator. New matching
prepared guest identity is necessary even though V and the resource profile
are unchanged.

The existing public `update` is a supported same-instance route in principle:
`cluster/lib/kb_runtime.rb:187-264` requires a live ready attested predecessor,
compatible endpoints/layout/credentials/configuration, exact candidate build
and complete closure preparation before ordinary shutdown and verified boot.
This investigation proves neither its current admission nor capacity. It also
cannot turn the failed Campaign into a completed verifier receipt. Do not make
an update or a new continuation interface an implicit extra requirement here.
For the existing required finite verifier/capture route, root can instead
select ordinary owned stop, separately approved reset when deletion is needed,
and fresh one-instance admission from the corrected immutable package. Preserve
failed evidence outside any approved deletion, remeasure resources, and never
allocate a second live pair by assumption. Root owns that concrete disposition;
this source proposal authorizes no lifecycle action or cleanup.

Current and both absent environment markers were checked from the exact tracking
CWD with login:false. Live roster revision 17 retains architect0's saved
Astra/xhigh/design/workspace_write settings. Applicable guidance and the
documentation skill were read or reused unchanged. Only this design proposal
was appended; there were no application edits, checks, live requests, probes,
package operations or lifecycle/ref changes. Review and native success of the
prospective correction remain unclaimed.

#### Reconciliation: same-instance public update, with one concrete prelaunch blocker

Root's proposed same-instance route is supported by the existing public
contracts. Once a repaired source is committed, checked, reviewed and genuinely
packaged, public `update` can transform the accepted ready G87d artifact into
an artifact for that exact source while retaining the instance, configuration,
endpoints, six credentials, host-key trust and compatible disks. This is an
ordinary repair of the selected final-source environment, not an attempt to
certify the deferred historical predecessor experiment. A failed Campaign does
not invalidate a separately accepted runtime artifact, but neither public
update nor a later success may rewrite that Campaign's failed receipt.

`runner/capture.cjs:24-108` requires the ordinary public connection/lease,
matching immutable source and actual guest closures; it does not require a
Campaign receipt. After successful update, a separately recorded finite public
member/API/PHP/lease/sentinel/ordinary-stop-resume sequence can therefore supply
the remaining real evidence. Direct capture and validation from the same new
immutable package can then generate genuine CS/EN images. Retain the original
failed campaign and new operation evidence separately; never manufacture a
completed `runtime-smoke` receipt to enter `bilingual-capture`. The direct
operation must still cover the selected checks, both selectors/default output,
physical locks, strict inventory validation and five-file export. No source
adapter, private Engine method or expected-source override is necessary.

**Source-supported blocker before selecting update.** Exact G87d
`cluster/lib/kb_closure.rb:112-119`, `ClosurePreparation#capacity`, still sends:
`df -B1 --output=avail /nix/store | tail -n1; df -i --output=iavail /nix/store | tail -n1`.
The inode invocation has the same GNU df option conflict documented at this
design's G14 resource diagnosis above. `set -eu` does not preserve a producer
failure through the successful tail; the result lacks the inode number and
the existing capacity condition refuses preparation. This is a command-source
defect, not a native update result or evidence of insufficient guest capacity.
The current `tools/test-closure.rb:30` supplies both synthetic numbers whenever
the command contains `df -B1`, so it does not execute the defective shell.

If root accepts update as the finite delivery route, the smallest additional
source scope is `cluster/lib/kb_closure.rb` plus existing `tools/test-closure.rb`:
use `df --output=iavail`, and capture both df producers in status-checked
standalone assignments before formatting their output. Preserve exact missing
closure bytes/entry counting and the 256 MiB / 10,000 inode reserves. Retain
strict numeric parsing/refusal and every source, credential, host-key, content,
GC-root and import-order proof. Add hosted coverage executing the actual
emitted capacity command with declared GNU tools, plus controlled producer
failure/malformed output that cannot reach `nix copy` or a prepared receipt.
Retain the existing insufficient-byte/inode and partial-import tests. This is
not accepted application scope until root explicitly assigns it; no local
execution or remediation was performed by the architect.

**Admission and failure limits.** Update builds while the old two guests remain
live, so assess the peak old guest RAM plus candidate image builder separately
from the original sequential first-start profile. `kb_source.rb:129-146` builds
the candidate cluster config and runner and retains their store roots. Count
the actual missing candidate outputs, a possible new 8 GiB immutable services
image, construction staging and unknown scratch; do not assume that a small
JavaScript diff makes those outputs free. Existing writable root/tank are kept
by `kb_machine.rb` / `kb_disks.rb`; do not budget another writable pair or claim
old image/closure reclamation. Import adds exact candidate NixOS store paths
to the retained services root before shutdown, with its own byte/inode reserve.
Refresh capacity and the live ready predecessor proof before the one selected
public update; the current diagnostic is not that admission.

Use the repaired package's public update with the same explicit private config,
`--topology single --network local`, original state root/slug and existing
900-second controller budget. Candidate artifact/run/closure identities must
change truthfully; unchanged disk/account/credential/trust identities must not.
One native failure ends this selected operation and leaves its genuine stage
and any update journal intact. No automatic retry, fallback artifact, resume,
reset, new pair or cleanup follows. A successful update must be freshly
attested before the separately selected smoke and captures. All later commands,
watcher/context/capacity admission and failure disposition remain root-owned.

### OPERATION PROPOSAL: ordinary G87d stop/resume after services SSH health failure (2026-10-11)

`finish-working-delivery-member-diagnosis3.json` records successful real
API7 current-user requests and ordinary member PHP read on instance
271d430a-f951-4979-b115-fe66c7516e11, run
5b83fc44-1224-44c5-bd23-49f10a42f7b2, artifact
a3406dd9-97b0-4914-98a7-86541b5062b2. The first separate lifecycle helper
changed descriptor bytes and refused before lifecycle; its diagnosis remains
in `finish-working-delivery-owned-lifecycle1-diagnosis.json`. The corrected
helper's native failure is retained in `finish-working-delivery-owned-lifecycle2.json`.
Root additionally reports that its lease failed during services SSH attestation,
and a separate public SSH read returned native255 / `Connection timed out during
banner exchange` at the recorded services endpoint 127.0.0.1:25700. Those latter
native strings and filtered console health observations are parent-supplied;
the architect did not open private diagnostics or make a live request.

The API and console-router HAProxy backend failures reported at17:04:54Z and
17:08:51Z, and the absence of matched OOM/panic lines in the bounded filter,
do not establish the root cause of guest unresponsiveness or exclude resource
pressure. Earlier boot/closure/resource/API/PHP success remains valid for its
recorded time. It is not current health or liveness proof. No new source repair,
timeout change or resource increase follows from this evidence alone.

**Supported finite next operation.** Root may separately select public
`G87_RUNTIME --state-root ROOT stop SLUG --timeout 900`, then, only after
successful stopped/complete-exit proof and refreshed admission,
`G87_RUNTIME --state-root ROOT resume SLUG --timeout 900`. Here G87_RUNTIME
means the genuine immutable G87d packaged launcher with its paired metadata,
not a newly repaired fixture package or metadata override. Resume accepts no
replacement config/topology/network. Preserve the failed Campaign and both
failed helper receipts; write any new native operation evidence separately.
This is an ordinary lifecycle operation on the accepted artifact, not Campaign
replay, a new pair or an instruction to call a private engine method.

Exact G87d `cluster/lib/kb_runtime.rb` public stop/control/stop_locked paths
authenticate the recorded launch, live runner tuple, private socket namespace
and SO_PEERCRED peer under the existing operation/gate. Unlike capture_lease,
they do not call `verify_live` or require guest SSH/API health. The runner then
uses its existing machine/test-shell shutdown and reaper path; services uses
OSVM's NixOS `poweroff` through that shell, not external SSH. Thus banner
failure does not itself block this public stop route. A guest hang can still
prevent graceful shutdown, so no success is presumed.

Before stop, reprove the exact owned launch/runner/control context using current
named evidence; a live `complete:false` receipt is normal and must not be
rewritten. Let public stop establish its own authenticated handoff and final
complete/all-recorded-processes-gone proof. Require native success, stopped
phase, complete exit and ordinary claim/socket disposition before advancing.
A refusal or expired900-second caller observation holds resume and further
work. The caller budget is distinct from the runner's sequential machine drain;
timeout supplies no force, signal, reset, unlink, process search or automatic
retry authority. Preserve any still-draining runner and its receipts.

G87d `resume` at `kb_runtime.rb:175-185` requires proven stopped state, no
pending update, accepted artifact, exact selected metadata, preparation,
configuration, credential and disk proofs. It calls `start_locked` with a
fresh run ID and the same artifact; it invokes no image build. The existing
prepared-disk adapter retains root/tank rather than copying a new root. Refresh
RAM/shm, exact resource availability and retained disk-growth admission; no
cleanup credit or extra pair is permitted. Compare the same artifact, all six
credentials, accounts, known_hosts and disk identities across the operation.
Resume must freshly establish SSH trust and actual guest identity/system
closures before its normal readiness result.

After native resume success, root may select a fresh canonical public lease,
exact-source attestation and read-only API7/member PHP observations. Preserve
the distinction between restored health at that point and an explained original
failure; restarting alone proves only the former. One new native failure ends
this selected finite sequence. Even success does not fix G87d's inventory
prefix or make campaign2 complete, and final corrected-source captures still
require the genuine source/artifact transition recorded above. No update is
currently admitted through a guest that cannot pass its required SSH proof.

Current/absent markers and live roster17 were reverified from the exact tracking
CWD with login:false; saved architect0 settings remain unchanged. Applicable
root/K procedures and documentation guidance were reused unchanged. This is a
design-only recommendation: no live proof, stop/resume, test, source/ref edit,
package work or private campaign read was performed. Root owns selection,
fresh watcher/context/admission and all native outcome acceptance; other retained
environments and preview remain outside this operation.

### SOURCE NOTE: reduced services RAM retains larger test-service defaults (2026-10-11)

The current health failure still has no established memory-exhaustion cause.
This bounded source trace does establish a relevant configuration mismatch:
G87d `cluster/nix/test.nix:2031-2050` imports V939159's
`tests/configs/nixos/vpsadmin-services.nix`, and K's services module forces
`virtualisation.memorySize` to the selected2048MiB without reducing that
module's worker/buffer settings. The imported test baseline declares8192MiB.
This is evidence about declarations, not a new evaluated configuration, actual
resident-memory measurement or explanation of the observed SSH/HAProxy failure.

The inherited settings and their existing owners are:

| Component | Source-declared setting inherited by K | Existing adjustment boundary |
| --- | --- | --- |
| API | V test module:2 Puma worker processes, threads1..8 per worker; API database pool defaults to5 per process | `vpsadmin.api.workers`, `threads.min/max`, `database.pool`; generated Puma config in `nixos/modules/vpsadmin/api/default.nix` uses these directly |
| Console router | `nixos/modules/vpsadmin/console-router.nix`: threads0..5; generated Puma config supplies no `workers` directive | `vpsadmin.console-router.threads.min/max`; no additional worker pool is declared here |
| Member PHP | Container `webui`, `nixos/modules/vpsadmin/webui.nix:215-228`: dynamic FPM, max32 children, start2, spare2..5, recycle after500 requests | Nested `containers.webui.config.services.phpfpm.pools.vpsadmin-webui.settings`; this is inside the same guest, not extra VM memory |
| MySQL | V test module: `innodb_buffer_pool_size=1024M`, max200 connections | `services.mysql.settings.mysqld`; K can override within its own test services module |
| Other MySQL buffers | V `nixos/modules/vpsadmin/database.nix:68-99`: join256M, sort512M, read128M, tmp tables96M, max heap1024M, max packet256M; read/write/purge thread settings32/16/16 remain inherited | Same existing MySQL settings; these are limits/configured buffers, not proof they are all allocated concurrently |
| RabbitMQ | V test/module enable the broker, management and Prometheus plugins; `cluster_partition_handling=pause_minority`; neither K nor V supplies a memory-watermark or Erlang scheduler override | Existing upstream `services.rabbitmq` configuration remains the owner; no exact effective broker watermark/scheduler number was established by this trace |

The test module's1GiB pool overrides the production module's `mkDefault
14000M`; it is incorrect to report a14GiB pool here. Likewise, PHP32 is a
ceiling, not32 workers proven resident, and Puma/SQL pool settings are not
measured RSS. The separate K `vpsfree` web FPM pool is conditional on the
optional web source/enable path; do not count it as present without the public
selected-configuration proof. No private configuration was read.

If later native evidence supports resource pressure, a K-only override of
existing service options is a materially narrower fit correction than increasing
the fixed2GiB services/2GiB node/2GiB sequential-builder boundary. The smallest
concurrency candidate is reducing the API's configured2 workers to1 while
retaining bounded threads and adequate database-pool capacity. The explicit
1GiB pool and large demand-dependent SQL buffers deserve measurement before
assuming that worker reduction alone solves the fit. PHP concurrency can also
be bounded at the nested pool owner if observations identify it. No new public
configuration schema, generic profile framework, production V defaults or OS
changes are necessary to express such a test-only correction.

These are available source boundaries, not accepted tuning values or a command
to apply changes now. The `extraModules.services` function parameter is not
exposed by the ordinary packaged CLI, so do not invent an ambient override to
inject changes into the retained artifact. Any selected K configuration edit
would need an exact new source/artifact and its normal affected declaration/
hosted/review gates before real use. Preserve service functionality and all
readiness, source, trust and capacity checks; do not disable dependencies to
make a smoke pass. Hold further tuning pending the current native stop/health
outcome and concrete diagnostic evidence. No retry, build, probe, service change
or resource increase is selected by this source note.

Current and absent environment markers plus retained roster17/settings were
rechecked. Applicable guidance was reused unchanged. Only this design note was
appended; no private configuration/log read, guest/process operation, test,
source edit, Git action or CI observation was performed.

### CAPTURE ADMISSION NOTE: recorded node memory zero (2026-10-11)

This assessment uses only the parent's supplied scalar observations from before
the failed member-read: services memory565198848 bytes, filesystem free4164939776
bytes /385082 inodes and zero recorded PSI values; node memory0 bytes,
tank available7800966656 bytes and empty pressure text. They are historical
snapshots, not current liveness, capture admission or the cause of the later
services hang. No private original receipt/configuration/serial was opened.

Exact G87d and committed Kf467934d3f678abc8b552f89805636d4d910438a have the same
`tools/runtime-verify.rb:580-629` measurement and admission code. The script
extracts `/proc/meminfo`'s `MemAvailable` field with awk and multiplies its kB
value by1024. There is no unavailable-measurement sentinel or zero fallback.
A missing field emits an empty value, which fails the required numeric-key
check; an unsuccessful producer exits through the standalone assignment.
For normal kernel-formatted input, recorded0 therefore means a zero available
memory estimate. The raw MemAvailable line was not inspected here, and no
formatter defect is established by the supplied numeric result.

The ordinary `resources(..., capture:false)` call validates required numeric
fields and services free disk of at least1GiB; it does not enforce guest memory
headroom. This explains how the earlier resource assertions can pass with node0.
Later `resources(..., capture:true)` checks each guest against a strictly
positive assessed memory requirement at623-624. `positive_bytes` at352-355
rejects zero thresholds. Reusing that node0 snapshot would necessarily refuse
with `assessed live guest memory headroom`, before fixture creation; no smaller
positive assessment can make zero pass. Direct capture is not permission to
skip this accepted admission requirement.

Empty node pressure text is distinct from a zero-pressure measurement. The
script emits PSI only when `/proc/pressure/memory` is readable, and pinned
OS6bdf `os/packages/linux/common-config.nix:81` declares `PSI = no`. Empty text
is consistent with that source configuration and supplies no evidence of low
pressure. The same OS source's `os/modules/config/tunables.nix:74` declares
`vm.min_free_kbytes = mkDefault (1 * 1024 * 1024)`; K's node profile has no
corresponding override. This is a concrete reserve setting to observe, not a
proved effective live value or permission to lower it. A `zfs_arc_min=1GiB`
string in `os/modules/tasks/filesystems/zfs/default.nix:321` is merely an
option example, not an assigned ARC minimum. Do not infer ARC usage or add ARC
bytes to MemAvailable. The exact kernel implementation object read did not
complete and was cancelled; no kernel-specific causal conclusion relies on it.

The inventory fixture remains one real running VPS with1CPU, memory1024MiB,
swap0 and disk quota4096MiB (`fixtures/prepare.cjs`, `INVENTORY_RESOURCES` and
the inventory preparation branch). A quota/limit is not measured resident
usage or guaranteed free host memory. The capture gate separately requires
the4GiB tank quota plus positive assessed template/metadata space. The supplied
tank snapshot leaves3505999360 bytes above4GiB, but no private assessment values
were inspected, so neither tank nor services capture sufficiency is certified.

**Smallest next observation, within the already selected next attempt only.**
After root's separately approved recovery/admission and normal ready/source
proof, before any inventory VPS/template mutation, collect one bounded public
SSH observation: the existing resource script plus allowlisted numeric node
MemTotal/MemFree/MemAvailable/Cached/SReclaimable/SUnreclaim fields, the effective
`/proc/sys/vm/min_free_kbytes`, PSI-file presence and, if present, numeric ZFS
ARC size/c/c_min/c_max fields. Preserve the exact MemAvailable value/unit and
native status so conversion can be reconciled. Compare that fresh observation
with the existing positive capture assessment for both guests and actual tank
space. If it passes, proceed only under ordinary admission; if zero recurs,
hold fixture/capture work and return those facts to root. This is one finite
diagnostic at an existing gate, not a polling/tuning loop or a new campaign.
Positive headroom admits the bounded attempt; only successful real fixture and
capture execution establishes practical fit.

No source change is selected. Do not replace MemAvailable with declared RAM,
MemFree plus guessed reclaimability, a synthetic positive value or a relaxed
threshold. Keep two2048MiB runtime guests, the sequential2048MiB builder and
intrinsic24GiB image/root/tank profile unchanged. Native cause, current capacity
and the pending recovery remain root-owned; all failed attempts and other
retained environments stay untouched. Current/markers and saved roster17
settings were verified; only this design note was appended.

### FINITE PUBLIC CONTINUATION: accepted f467 artifact and short browser TMPDIR (2026-10-11)

`finish-working-delivery-browser-path-diagnosis1.json` establishes a host-side
Chromium `SingletonSocket` path-length failure after genuine public start of
Kf467934d3f678abc8b552f89805636d4d910438a. The accepted instance is
f0cf3d9e-abac-461f-a9cc-86415da2e1ae, initial run
e7c720e8-36f2-42d9-ad78-292a154d6e0c and artifact
7209e6c4-0828-413b-b232-1b2e8377aca7, digest
c7aeecd5c6a1410c94dd13ac3278d19725633539d29f61f16c4adab5270d360c.
These are stored acceptance facts, not current liveness. Preserve the failed
attempt hash959d225ae09f624c2891d1d449226a03efd93dbbdf9eeeb9d70118c96f2e5b1d
and its absent runtime-completion receipt. No replacement artifact, image or
pair is needed solely to shorten Chromium's temporary socket path.

**Supported selection.** Use a separately recorded finite operation unit with
the same immutable f467 runtime/capture/validator, paired metadata and selected
Node/Playwright/browser environment. Give the actual browser child a newly
owned ordinary0700 short absolute TMPDIR, for example a private random directory
under `/tmp`, with ample byte-length margin for Chromium's generated suffix.
Record its ownership/path and capacity placement; do not move or symlink cluster
state, output, credentials or the failed Campaign. Keep private browser scratch
out of carryback. `lib/browser.cjs` supplies no custom user-data path or child
environment, and the packaged capture wrapper preserves TMPDIR. In contrast,
`tools/runtime-verify.rb:27-30` overwrites it with `root/temporary`: merely
prefixing another Campaign invocation with TMPDIR would not correct this path.
Do not instantiate/re-enter that failed Campaign or its command wrapper.

The selected sequence, under root's existing durable context/watcher and native
failure recording, is:

1. Reprove the same accepted current f467 instance through the public connection
   and source/guest-closure checks. Preserve canonical connection bytes exactly
   when writing a private descriptor; parsing and reformatting changes its lease
   digest. Bind the separate packet to the original failed-attempt hash and
   current artifact, config and package identities without copying nested secrets
   into public records. Root's bounded node-memory read remains diagnostic,
   not automatic capture admission.
2. Run the existing exported read-smoke composition with short TMPDIR: canonical
   public lease, matching `Connection.verify`, corrected `inventoryIdentity`,
   ordinary member login/list and `assertInventoryMember`. Close browser/proxy
   resources before releasing the lease. Then invoke the unchanged immutable
   `tools/verify-live-lease.cjs` with its real descriptor, metadata, runtime
   package, state root and original private config. It requires the retained
   slug `same-slug`; preserve it. This covers public75 contention, peer loss,
   reacquisition, routing and wrong-source refusal without private lifecycle calls.
3. After those successes, create the two existing dedicated sentinel paths only
   if absent, using public SSH and a new operation marker. Baseline their hashes,
   all six credentials, accounts, known_hosts, disk identities/sizes, immutable
   image and accepted artifact/closure identities. Preserve private bytes;
   output only their allowlisted identities/hashes. Do not overwrite a preexisting
   unexpected sentinel or use a failed Campaign receipt as the baseline.
4. Select ordinary public `stop --timeout 900`. Require native success and
   guarded stopped/complete/all-recorded-processes-gone proof before resume.
   Refresh host admission, then genuine same-source public `resume --timeout 900`
   without config/topology replacement. Require the same instance/artifact,
   fresh run, unchanged baseline/sentinels and fresh live identity/actual-closure
   and trust proofs. No image rebuild is part of resume. Repeat the member read
   with short TMPDIR and record the result independently of the failed Campaign.
5. Before fixture mutations, satisfy the existing positive guest-memory, services
   disk/inode, node template/quota and host/browser-headroom admission with fresh
   measured facts. The earlier node0 value cannot pass that gate. If fit refuses,
   stop advancement and retain the concrete result; do not reduce thresholds,
   increase resources or substitute declared RAM for measured availability.
6. Use the matching public packaged capture/validator on this same resumed run:
   CS `--cluster same-slug --state-root ROOT`, EN `--connection FILE`, both with
   `--checkpoint networking/ip-address-list --output-root OUTPUT`. Use one new
   private writable output root; repeat EN from that output CWD without an
   explicit output-root to retain the selected default-CWD proof. All browser
   invocations receive the same short private TMPDIR. Update the candidate
   inventory with the matching validator, then strictly validate without
   `--allow-missing`. Use existing `tools/capture-export.rb` /
   `KbCaptureArtifacts.export` under its physical lock for exactly the two PNGs,
   captures.json, merged results and source receipt. Retain f467 generator
   provenance when later committing media; review both genuine images.
7. Finish selected successful work with ordinary public stop and complete exit
   proof under the standing finish brief. No reset, state deletion, forced signal
   or action on other environments is implied by this sequence.

No unsupported source gate was found for this direct route. The repository's
documented public capture path does not consume a Campaign completion file;
the verifier's `bilingual-capture` phase does. Separate operation evidence must
cover the required real criteria honestly, never synthesize that file or claim
the original `runtime-smoke` passed. One native failure ends this selected
sequence and holds dependent steps. Current ownership, health and capacity
remain actual operation prerequisites, not conclusions of this source read.
Keep two2048MiB guests, the unchanged sequential2048MiB builder definition and
intrinsic24GiB disk profile; this continuation launches no builder or new pair.

Current, absent markers and live roster17/settings were verified. Applicable
workspace/K guidance and documentation skill were read or reused unchanged.
Only this design section was appended; there was no source edit, check, build,
CI request, private input read, probe or lifecycle action. Root owns the exact
finite packet, operational selection and acceptance; no new source scope is
requested by this brief.

### PROPOSAL: bounded reduced-node reserve correction (2026-10-11)

This is prospective source/operation guidance, not permission to modify the
guest or an accepted capture result. `finish-working-delivery-node-memory-observation4.json`
binds the current f467 instance/run/artifact from the preceding section and
records MemTotal2025076KiB, MemFree1178304KiB, MemAvailable0KiB and
vm.min_free_kbytes1048576KiB. ARC resident size is about11MB; PSI is unavailable.
The zero is a real reported value, not the verifier's unavailable-measurement
convention. It does not establish exhaustion or explain the earlier services
hang. `tools/runtime-verify.rb:580-629` reads MemAvailable directly and its
positive capture-memory check correctly refuses this observation.

**Smallest proposed persistent policy.** At pinned OS6bdf,
`os/modules/config/tunables.nix:74` supplies the matching1GiB `mkDefault`.
The same pinned source's `tests/suite/kernel/proactive-swap.nix:23-38` explicitly
uses65536KiB with a3072MiB test VM. Adopt that existing64MiB test reserve as the
single candidate for K's dedicated reduced node, not a claimed measured minimum
or an automatic consequence of having2048MiB RAM. Copy none of that test's
DAMON/swap/NUMA settings. There is no reason here to change ARC, services,
kernel configuration, OS production defaults, API limits or capture thresholds.

The production-code owner is only K `cluster/nix/test.nix:1831` (`nodeModule`).
Use its ordinary `boot.kernel.sysctl."vm.min_free_kbytes"` option to override
the upstream default with65536 for the existing reduced shape: single/local,
services2048MiB/root8192MiB and node2048MiB/tank8GiB. One explicit local
predicate suffices; add no configuration field, profile selector or scaling
algorithm. Nonmatching K profiles retain the inherited value. Normal module
priority is sufficient against `mkDefault`; do not use `mkForce`, change the
OS input, or alter the kernel derivation. Two2048MiB runtime guests, the
2048MiB builder, disk sizes and every positive admission criterion stay fixed.

**Optional one-value measurement before source acceptance.** If root separately
selects it, use the genuine paired f467 public
`vpsfree-kb-devcluster ssh same-slug node1 -- sh -s` under the existing owned
operation context. Reprove the exact ready instance/run/artifact, retained SSH
trust, guest identity and actual system closure immediately beforehand. Within
that guarded command, compare the identity/closure with the bound values and
require the current sysctl to be exactly1048576 before writing anything.
Record only the allowlisted numeric memory/reserve/ARC fields. Set65536 once,
verify that readback, and repeat those measurements and the unchanged numeric
capture assessment; do not create a fixture or take screenshots in this
experiment. More MemFree alone is not admission; actual MemAvailable and all
other original capture requirements must pass.

Install shell exit/signal restoration before the write. Restore1048576 only
from the expected temporary65536 value, then require a successful public
readback; an unexpected value refuses rather than being overwritten. An SSH
failure can prevent confirmed restoration, so a trap is not proof of rollback:
root must retain the failure and establish the exact current value through the
same public authority before any dependent work. No second value, automatic
retry, reboot or reset is part of this measurement. Its evidence says
"f467 plus temporary runtime sysctl experiment", never that f467 declares the
new policy or that its failed Campaign completed. A positive result justifies
the candidate; an insufficient result restores the old value and holds work.

**Same-instance source transition and its actual cost.** The existing public
`update` route is compatible with this sysctl-only K correction. At immutable
f467 source `/nix/store/xllyhnv9ba1d49f9fvdwbpgxaf04phdf-source`,
`cluster/lib/kb_runtime.rb:187-264` admits only a ready, attested predecessor,
unchanged SSH endpoints, compatible disk layout/TLS names and identical six-file
credentials. It journals and builds the real candidate, imports the exact
NixOS closure while the predecessor is reachable, then gracefully stops and
direct-boots the candidate. Root must first restore any diagnostic sysctl and
finish/release its current read/lease operation. The candidate uses the original
private configuration; retain accounts, known_hosts, persistent Ed25519 keys,
disk identities and sentinels. Accept a new artifact/run/source only after the
existing live identity and actual-system proofs. This needs no new instance or
second writable root/tank and never replays the failed Campaign.

It is **not** an unchanged-services-image or no-build route. `kb_source.rb:75-90`
creates new guest identity containing the artifact and full source metadata;
`test.nix:1319-1320` installs it in every guest, including services.
`kb_source.rb:124-145` builds the entire candidate cluster-config and records
its boot/image paths. The retained writable services root is preserved, but
the candidate services closure/image must be treated as new construction until
exact native derivation/substitution evidence proves otherwise. Its8GiB image
may coexist with the retained old image. Candidate construction occurs before
old guests stop, so an actual2048MiB image builder can overlap the existing4GiB
runtime: the initial-start sequential peak cannot be reused as update admission.
No resource setting increases, but root must assess this6GiB guest/builder peak
plus real overhead, image/staging/missing closures, retained growth and reserves.
The existing guest-import256MiB/10000-inode reserves remain enforced. If that
bounded construction/import does not fit, public update is blocked; there is no
supported no-build source relabel, in-place declaration edit or private prepare
shortcut in this proposal.

**Verification and limits.** Extend the existing actual pinned-module/profile
projection in `tools/test-runtime-verify.rb` to assert65536 for the reduced node,
1048576 for a nonmatching/default node, unchanged kernel outputs and unchanged
guest/builder/disk dimensions. Project the effective OS sysctl through the same
module evaluation pattern already used by `tools/test-node-ssh.rb`; a text-match
assertion or fake runtimePlan field is insufficient. Preserve the existing
resource producer/error and insufficient-live-memory tests, including zero
refusal. Owning hosted selection is the existing declared-shell
`ruby tools/test-runtime-verify.rb` (already included by `bin/check`); no new
workflow, broad suite or local check is requested. Add one short reduced-profile
policy/rationale paragraph in `cluster/runtime-contract.md`. Root coordinates
the narrow committed source review and ordinary exact E pin/package evidence.

After separately admitted public update, fresh numeric observation must show
65536 and satisfy the unchanged capture thresholds before fixtures. Ordinary
same-source stop/resume must preserve65536, artifact/source/closure, all six
credentials/accounts, SSH trust, disks and sentinels. Then the previously
accepted short-TMPDIR CS/EN capture/strict validation/export sequence applies,
with the genuine new generator revision retained in later media provenance.
Neither declaration tests nor the temporary experiment certify practical VPS
fit. One native failure ends the selected operation and retains its journal
and evidence; no automatic rollback, reset or third attempt follows. A source
rollback requires an explicitly selected supported update and fresh admission,
not editing accepted-artifact metadata. No schema, guest data layout, network
feature, provider behavior or production policy change is proposed.

Current/absent markers and live same-session roster17 were verified with the
absolute public CLI; saved architect0 settings remain unchanged. Only this
design section was appended. No application edit, private input read, check,
evaluation/build, probe, guest command, lifecycle action or Git/ref operation
was performed. Root owns source acceptance and any measured operation decision.

### ADDENDUM: services health blocks reserve/update advancement (2026-10-11)

`finish-working-delivery-current-services-ssh-diagnosis1.json` records native255
and a banner-exchange timeout at the exact services endpoint127.0.0.1:25700
for the same f467 instance/run/artifact. The separate public continuation ended
before browser work during fresh services identity verification. Successful
connection export and node identity/closure proof do not supply that missing
services proof. Keep the failed operation and failed Campaign results distinct
and immutable; neither completed, and no stop/resume was selected by the failure.

`finish-working-delivery-current-services-console-facts1.json` contains five
allowlisted matches, all ordinary startup messages for the OOM-killer service
or API oom-report tasks. They establish neither an OOM event nor its absence
outside that filtered evidence. The SSH timeout does not identify a memory,
daemon, scheduling or network cause. Similar G87 symptoms are historical
observations, not proof of a shared cause. The node's inherited1GiB reserve
and zero MemAvailable are a separate fit issue: changing that node policy
cannot be claimed to restore services SSH or make screenshots feasible.

**Existing diagnostic route boundary.** Source inspection of exact immutable
f467 `cluster/launcher.rb:39-87` finds public SSH but no console/test-shell
execution or attach command. `cluster/lib/devcluster_runner.rb:172-192` accepts
only the exact authenticated schema-1 `stop` request on the control socket.
It has no diagnostic RPC. The pinned OS6bdf
`osvm/lib/osvm/shell.rb:39-52,135-146` owns a UNIX listener and the QEMU-connected
shell stream inside the existing runner. Its preparation unlinks/recreates the
socket, and its execute path can start a machine. OSVM's CLI exposes only
`script`, not a retained-run attach operation (`osvm/lib/osvm/cli/app.rb:24-30`).
Constructing another Machine/Shell, writing the socket protocol directly or
using a private Engine invocation would not preserve K's existing full ownership,
serialization and source contract. None is a supported read-only substitute.

There is an existing passive source of diagnostic evidence: the original
runner's console writer (`osvm/lib/osvm/machine.rb:734-755`) writes the named
services console log. Root may separately select bounded reads of already
recorded, exactly owned console/machine evidence with its established path/
identity guards and a field/message allowlist. Keep credentials, raw serial,
configuration and account data private. Such logs can establish only the events
they actually record; they do not execute a guest command, restore live source
attestation or certify present health. No current supported non-SSH active
guest-shell route retaining all requested guards was found.

**Next decision.** Hold reserve experiments, persistent-fit transition and
capture advancement pending services diagnosis or separately accepted recovery.
`Engine#verify_live` (`kb_runtime.rb:796-807`) reads every guest identity and
actual closure through SSH; public `update` invokes it before preparing its
candidate (`:201-205`). It therefore currently has a concrete admission blocker,
not an available workaround for the health failure. The preceding64MiB proposal
remains conditional source guidance, with no inferred health benefit, source
acceptance or operation authority. Node-only success cannot waive services
proof. No timeout increase, trust change, tuning, new diagnostic framework or
lifecycle retry is proposed here. If the narrowly retained evidence cannot
explain the failure, report that limit before root selects further action.

Fresh current/absent markers and roster17/settings were verified; required
workspace/K guidance was reused unchanged. Only this addendum was appended.
No application edit, private input/raw-log read, check, probe, guest operation,
Git/ref change, lifecycle action or mutable-source certification was performed.

### PROPOSAL: operator-prepared f467 captures without source transition (2026-10-11)

The later allowlisted `finish-working-delivery-current-tls-native1.json`
records native OpenSSL success and HTTP200 from both exact CA/SNI-bound API and
PHP endpoints. `finish-working-delivery-services-ssh-bounded-diagnosis2.json`
records successful retained-key services identity verification with a diagnostic
ConnectTimeout30. Root reports that request returned in0.6s. These observations
supersede an assertion of continuous services unavailability, but do not explain
the earlier public5s failure, certify current health or change any public timeout.
The separately watcher-owned member/read/lease operation must supply its own
native result. The earlier failed continuation remains failed.

**Supported attribution decision.** An explicitly selected, documented public
SSH reserve preparation can support canonical captures from the genuine
unchanged f467 artifact. It is an operator-prepared capture environment, not a
claim that f467 declares64MiB or that the stock reduced profile passed unchanged.
This supersedes the earlier diagnostic-only restriction solely if root accepts
this bounded capture preparation. The persistent K declaration proposal remains
deferred; neither public update nor another image builder is selected.

The source basis is f467 `lib/connection.cjs:236-268`: capture verifies the exact
descriptor/artifact digest, source metadata, configuration-input identity,
guest identity and actual system closures, then records those exact values.
`runner/capture.cjs:44-90` also requires the original inventory/pinned V revision,
the physical output lock, live cluster lease and original fixture/scenario code.
A runtime write to `/proc/sys/vm/min_free_kbytes` changes none of those identities.
The provenance does not attest every mutable kernel parameter or say that all
runtime state derives exclusively from the source. Fixtures themselves prepare
mutable guest state. This contract permits explicit preparation without a
metadata override; absence of a sysctl check alone is not the acceptance case.
Reproducibility requires retaining the exact extra preparation as part of the
operator procedure and evidence, not hiding it behind an unchanged source hash.

Keep the following finite sequence, subject to root's actual operation selection:

1. Require the current normal public member/read and lease checks to pass with
   their unchanged transports/timeouts. Complete the selected sentinel and
   six-credential/account/disk/image baseline, ordinary public stop with complete
   exit proof, and genuine same-source resume before reserve preparation. Fresh
   public attestation must prove the same f467 artifact/system closures, a fresh
   run and unchanged baseline/sentinels. Require the resumed node's reserve to
   equal its declared1048576KiB. This proves normal source/artifact continuity;
   it deliberately does not claim that a transient64MiB setting persists.
2. Bind one separately recorded preparation to that exact resumed instance/run/
   artifact, public source metadata and both actual system closures. Reuse the
   preceding guarded public node SSH procedure, but retain65536KiB for this
   selected capture window instead of restoring it at the end of measurement.
   Require1048576 before the one write,65536 afterward and unchanged guest/source/
   closure identities. No persistent file, configuration input, accepted artifact
   or known_hosts changes. Record the exact preparation command/recipe digest
   and only allowlisted numeric before/after fields, never credential values.
3. Reapply the original fresh guest-memory, services disk/inode, tank-template/
   quota and host/browser-headroom admission. Use actual MemAvailable and the
   existing positive thresholds. A positive change alone is not sufficient.
   Refusal ends advancement and selects restoration, not a smaller threshold,
   second reserve value, fixture mutation or capacity assumption.
4. Use the genuine paired f467 capture/validator packages, short private TMPDIR,
   unchanged fixture/scenario and exact selected V pin. Run the accepted CS/EN
   checkpoint/selectors/default-CWD sequence on this same resumed instance and
   one output root. Recheck the prepared reserve and applicable fresh capacity
   before each capture. Public preparation/readback commands finish before a
   capture acquires its lease; never nest another public gate holder inside it.
   Each actual capture must acquire its own physical artifact/cluster locks and
   independently pass ordinary live source/system attestation. No diagnostic
   ConnectTimeout30 substitution is permitted in the accepted capture path.
5. Close all browser/SSH/lease activity before restoration. Require the same
   owned run and temporary65536 value, restore1048576 by public SSH and prove
   readback, preserving identities and private baseline hashes. The finite
   parent operation owns this cleanup even if a capture or validator failed;
   do not rely on a shell trap from the earlier, now-finished preparation call.
   Unexpected value, lost authority or failed SSH leaves restoration unproved
   and holds dependent actions; it never authorizes overwriting an unknown
   value, replay, force or reset. The existing separately selected final public
   stop remains ordinary lifecycle work, not a substitute success receipt for
   an unproved restoration. Stop/resume source defaults have already been
   measured before this capture window; no extra lifecycle cycle is required.

The finite packet must bind the preparation/restoration observations to exact
capture result/source-receipt and PNG hashes, the immutable generator and the
failed Campaign hash. Retain it as sanitized operation evidence, separate from
the unchanged canonical five-file carryback. Do not add fictitious fields to
the descriptor, artifact or capture-source schema. Strict installed validation
and actual bilingual visual review still govern the candidate media. Record a
short portable public-command preparation recipe and this qualification in the
owning capture workflow/media handoff so another operator can reproduce the
images without this workspace or an ambient sysctl setting. Documentation/media
commit M retains f467 as actual generator G; it does not retrospectively declare
the64MiB policy in G. This requires no runtime/application change or new package,
kernel, services image, writable root, tank, guest pair or broader test suite.

Acceptance can honestly establish same-source ordinary lifecycle continuity
and genuine f467 CS/EN images under recorded operator preparation. It cannot
establish unmodified-default capture fit, a persistent reduced-profile policy,
source-upgrade behavior, an explanation of the intermittent services failure,
or completion of any failed Campaign. If root requires source-declared64MiB
rather than this explicit operator-prepared condition, the earlier source/update
construction boundary still applies and cannot meet the selected no-builder-
while-pair-alive constraint by relabeling the artifact. No such update is
proposed for finishing these screenshots.

Current/absent markers and live roster17/settings were verified; applicable
unchanged guidance and exact immutable capture source were reused/read. Only
this proposal was appended. No operation, source edit, check, private input
read, CI observation, build or lifecycle action was performed or certified.

Subsequent closed evidence `finish-working-delivery-public-member-read2-proof.json`
records native0 for connection export, ordinary member browser/API/TLS read and
the unchanged live-lease helper on that same f467 instance/run/artifact.
Its original failed-attempt hash is unchanged and it expressly records no
lifecycle/fixture mutation or completed Campaign. This satisfies the services
health/read/lease prerequisite for that observation, without diagnosing the
earlier transient timeout. Root may separately select the ordinary stop/resume
step above; reserve preparation, capture and restoration remain unexecuted and
require their own fresh proofs. No failed unit is replayed or reclassified.

### RECONCILIATION: ordinary continuity without pre-stop sentinels (2026-10-11)

The separate public-continuity3 attempt failed before writing sentinels or
requesting stop. `finish-working-delivery-services-public-equivalent-diagnosis1.json`
records native255 with the unchanged5s client banner timeout;
`finish-working-delivery-services-ssh-limits-diagnosis1.json` also records255
for the subsequent30s diagnostic. Neither returned guest observation fields.
Keep both failures alongside the earlier genuine native0 member/read/lease
and strict-SSH observations. This proves intermittent success/failure, not its
cause, present liveness or a useful timeout adjustment.

Root's separately selected ordinary public stop/resume can proceed without
pre-sentinels under its existing ownership and admission requirements. In exact
f467 `cluster/lib/kb_runtime.rb:493-521`, stop requests the authenticated recorded
runner and waits for complete exit before resource/socket cleanup and stopped
phase; it does not require services SSH or a new guest source read. Resume
(`:175-185`) requires stopped/all-gone, the existing accepted artifact and valid
prepared disks, then starts a fresh run. It does not require sentinel files.
Failure/refusal/expiry still holds dependent work; no force, reset, build,
configuration replacement or automatic lifecycle retry is supplied here.

Before stop, root retains the canonical descriptor, exact validated live control/
launch tuple and private six-credential/account/known_hosts hashes, accepted
artifact/config/source/expected-closure evidence, writable disk identities and
immutable image identity/hash. Label the last successful services attestation
by its actual observation time; descriptor readiness does not refresh that proof.
For writable disks, compare device/inode/type/declared size as supported, not an
unchanged whole-image checksum while the guest legitimately writes its filesystem.
No private contents enter public evidence.

Require successful public stop900 plus independent stopped/complete/all-recorded-
processes-gone proof before fresh6GiB-RAM/5GiB-shm and retained-growth/reserve
admission and genuine same-artifact public resume900. Resume uses the exact
f467 runtime/source and takes no replacement configuration. Afterward require
the same instance/artifact, fresh run, unchanged six credentials/accounts/trust,
disks and immutable image, then ordinary public source/actual-closure and member
API/PHP verification with the original transports and thresholds. Every proof
is native evidence of this separately selected operation, not a continuation
or completion record for a failed Campaign/unit.

**Acceptance limit.** Success establishes ordinary stop/resume and identity/
artifact/storage-object continuity. It does not prove preservation of dedicated
services-root or node-ZFS payload contents: no pre-stop sentinels exist, and
post-resume writes cannot establish that missing comparison retroactively.
Retain that omission explicitly. f467 `tools/runtime-verify.rb:645-673` requires
sentinels for its full runtime-smoke receipt, so that receipt remains absent and
that full qualification remains incomplete. Do not amend the verifier guard,
forge its receipt or require another lifecycle campaign solely to erase this
known limitation.

Actual public capture uses `runner/capture.cjs:44-90` / `Connection.verify`,
whose original-source/fixture, artifact, live guest closure and physical lease
checks contain no sentinel prerequisite. Thus this narrower continuity evidence
can support the already accepted operator-prepared canonical capture route,
provided fresh post-resume health, guarded65536KiB preparation, unchanged positive
capacity gates, both real language captures, strict validation and restoration
all succeed. Record the missing payload proof in the final handoff; it neither
invalidates genuine images nor becomes an implied full runtime-suite pass.

**SSH diagnosis boundary.** Both K `Engine#ssh` (`kb_runtime.rb:606-616`) and
`Connection#ssh` (`lib/connection.cjs:207-224`) explicitly set ConnectTimeout5,
dedicated identity, strict retained host trust and no ambient SSH config. The
leased wrapper's30s child deadline is separate, not a30s handshake allowance.
K's `sshModule` (`test.nix:1318-1328`) supplies the dedicated key/authorized-key
policy but no demonstrated banner-performance correction. No source-supported
service tuning, DNS setting, keepalive or longer timeout can be selected as a
fix from these observations. In particular, absent remote numeric output is
not a measurement of sshd limits or load.

The bounded diagnostic opportunity is after the selected resume, if ordinary
public SSH works: root may separately retain allowlisted numeric memory/load,
sshd process/unit state and relevant time-bounded sshd failure events through
that same guarded public route. Exact client-stage debug output from the selected
native OpenSSH client is another diagnostic-only boundary, using the same
endpoint/key/trust and timeout, with raw output private and only negotiation
stage/timing facts exported. It cannot replace public acceptance or justify
repeating failed attempts. While SSH is unavailable, the prior no-public-console-
attach conclusion remains: only guarded passive owned logs are already available.
No diagnostic operation, preparation/tuning, restart or new source interface is
selected by this paragraph. The source does not explain the recurring banner
failure; a successful resume must be observed, not presumed to cure it.

Current/absent markers, roster17 and retained architect settings were verified;
unchanged mandatory guidance was reused. Only this reconciliation was appended.
No guest/process probe, check, application/source edit, lifecycle action, build,
CI observation, private input/raw-log read or Git/ref mutation was performed.

### PROPOSAL: exact immutable capture entry with private exception retention (2026-10-11)

`finish-working-delivery-operator-capture-window1-disposition.json` records a
native1 CS capture after positive host/guest admission, followed by successful
public reserve restoration to1048576KiB. Root verified all16 recorded stream
hashes. No accepted PNG/results exist; missing fixture-output files do not prove
that fixture mutations never began. Preserve the failed unit and its private
output unchanged. The separate `finish-working-delivery-capture-read-diagnosis1-proof.json`
records native0 for both original consumers: public connection and the original
live lease/Connection.verify/browser/CS-member-login composition, with clean
closure and no provisioning/lifecycle. Its outer summary's later missing-key
error remains an overall helper failure; it does not invalidate those recorded
native results or justify rerunning that helper.

**Source-supported diagnostic equivalent.** Exact f467
`runner/package-capture.cjs` reads metadata from argv[2],
imports `main` from `runner/capture.cjs`, and calls it with argv.slice(3), that
metadata, output default `process.cwd()` and state default
`path.join(process.cwd(), '.devcluster/v2')`. Its only error handling replaces
the exception with the50-byte generic message and sets exitCode1. The installed
wrapper at `/nix/store/6xsyrxxjf15czc4vldqw975f0hix3niq-vpsfree-kb-capture/bin/vpsfree-kb-capture`
sets the selected tools/client PATH, NODE_PATH, PLAYWRIGHT_BROWSERS_PATH and
FONTCONFIG_FILE, then invokes that exact entry with immutable metadata
`/nix/store/3jpiaycynic81567fq6n41jgpdg2sh1s-vpsfree-kb-runtime-source.json`.

Root can select a single finite diagnostic invocation whose only difference is
the outer rejection sink. A small private coordination entry imports the exact
exported `main` from
`/nix/store/xllyhnv9ba1d49f9fvdwbpgxaf04phdf-source/runner/capture.cjs`, reads that
same metadata file and supplies exactly the four package arguments. For a
normal Node script, pass `process.argv.slice(2)` as `argv`; do not accidentally
reuse the package-entry offset3 or Node `-e` argument conventions. Preserve
output/state CWD defaults exactly. On rejection, retain the original error/stack
only on the pre-established private stderr stream and set exitCode1. Do not
call process.exit, swallow the rejection, reinterpret a partial result as
success or install interception inside main. Parent must ensure stdout/stderr
and the entry/packet are private ordinary files under its owned directory;
raw exceptions may contain sensitive runtime context and are not public output.
Publish only allowlisted diagnosis and hashes after inspection.

Bind the entry bytes, full selected argv, CWD, immutable module/metadata hashes
and effective packaged environment before invocation. Use the same selected
Node, all package export values including the client PATH component, short
private TMPDIR and remaining accepted clean environment. A new private output
root preserves the failed output; "same arguments" means equality with the
packaged command for this newly selected invocation, not re-entry into the old
failed unit. Keep the real same-slug/state/checkpoint/language and normal output
selection. No mutable checkout, current verifier source substitution, checkout
metadata computation, source override, monkeypatch, alternate fixture, fake
descriptor or private Engine call is part of this equivalent.

All work remains in the original `main`: actual argument parsing, inventory and
pin checks, physical artifact lock, canonical descriptor/controller, cluster
lease, original guest/source/closure verification, browser/login, provisioning,
scenario/checkpoint, publication and finally cleanup (`runner/capture.cjs:25-115`).
Its module-relative source root remains f467. No permission or safety gate moves
into the coordination entry. In particular, invoking `runner/capture.cjs` as
its checkout-style CLI would compute checkout metadata and is not this route.
This is a finite composition of the exported entry used by the package, not
a new documented launcher, source patch or additional runtime authority.

**Finite operation boundary.** Require root's separate acceptance and fresh
same-instance/run/artifact public proof and original positive capacity admission.
Re-enter only the already accepted guarded1048576->65536 operator window, with
restoration owned by the parent even on failure. Select one diagnostic CS
invocation on the existing resumed instance. The fixture's original rerun/
ownership guards handle any partial prior preparation; do not presume an empty
guest or bypass a refusal. One native failure ends that selected capture work,
retains the exception/evidence privately and requires restoration/readback,
without automatic second capture, lifecycle retry, reset, builder or new pair.
The root-owned observer may diagnose the concrete exception afterward; this
proposal guesses no failure cause from Source/Output-only stdout.

**Canonical-output decision.** A native0 from this exact original core may
qualify its CS image as genuine f467 generated output, rather than being
diagnostic-only, because the complete original capture, source/lease checks
and result provenance are unchanged. Record that it used the diagnostic outer
entry; do not claim the installed package entry passed or change the original
failed result. A PNG alone is not acceptance: require original successful
results/source receipt, exact hashes and subsequent matching installed strict
validation plus visual review. Complete EN and the selected default-CWD proof
only in root's explicitly bounded success continuation, using the package or
the same approved equivalent with identical defaults. Keep both language results
under one genuine generator/source contract. The normal five-file locked export
remains unchanged; entry/error/preparation records stay separate private or
sanitized operational evidence. Later media commit M retains generator f467.

No application/package change or new guest artifact is necessary for this
diagnostic sink. If inspection reveals any need to change the core, its options,
fixtures, cleanup or proof, stop this equivalence claim and refer that concrete
source issue to root; a changed core would require its own genuine source/
artifact path rather than an override of the current f467 environment. Current,
absent markers and roster17/settings were verified, applicable unchanged
guidance reused, and only this proposal appended. No check, probe, application
edit, operation, private input/raw-log read, Git/ref change or passing capture
claim was made by this design task.

### SOURCE DIAGNOSIS: bounded services-periodic-work observation (2026-10-11)

Window2 failed at the services resource-read admission before invoking either
capture entry or provisioning. Its successful reserve restoration and the six
native commands remain recorded in
`finish-working-delivery-operator-capture-window2-proof.json`; the selected
diagnostic-entry flag is not evidence that main ran. The subsequent exact5s
native SSH observation reached TCP establishment but received no guest bytes
before banner timeout. The passive named-QEMU RSS/thread/cumulative CPU values
do not identify a guest process, measure a utilization interval or prove memory
pressure. Empty filtered console categories do not establish event absence.
The cause remains unknown despite the earlier genuine same-transport pass.

**Concrete source workload.** The selected V939159 services test module
(`tests/configs/nixos/vpsadmin-services.nix`) enables default API rake tasks and
the scheduler, in addition to two API workers and the1GiB MySQL buffer pool
already described at7639. Kf467 forces2GiB services RAM without suppressing
those tasks. The owning V module `nixos/modules/vpsadmin/api/rake-tasks.nix:65-99`
creates independent `bundle exec rake` oneshot services with a1h default start
budget; some prune jobs explicitly use infinity. `api/Rakefile` loads ActiveRecord,
the API and its plugins for each ordinary rake process. The named recurring
work includes:

| Unit stem (prefix `vpsadmin-api-`) | Source schedule |
| --- | --- |
| `prometheus-export-base` | Boot1min, every2min, randomized delay up to60s |
| `prometheus-export-dns-records` | Boot10min, every10min, randomized delay up to60s |
| `incident-reports`, `outage-reports-auto-resolve` | Boot5min, every2min, randomized delay up to60s |
| `oom-reports-run`, `monitoring-check`, `payments-process` | Boot5min, every10min, randomized delay up to60s |
| `requests-ipqs` | Boot5min,2min after completion, randomized delay up to10s |

These are declared schedules, not observed concurrent jobs. They provide a
specific possible source of transient Ruby/SQL work in the small guest; they
do not establish that any such invocation overlapped an SSH failure. K also
enables vpsf-status checks every30s (`test.nix:1425-1441`) and Adminer, while the
WebUI container prunes expired sessions every5min. No evidence selects any
one of these, API concurrency, MySQL buffers or RabbitMQ as the culprit.

**Smallest useful next diagnosis.** Root may separately select one bounded
public-SSH observation when the original guarded transport responds, bound to
the exact current source/artifact/closure and run. Read services MemAvailable,
swap and PSI availability/counters, load/runnable counts, and only the named
rake services/timers above. `systemctl show` can restrict output to unit ID,
LoadState/ActiveState/SubState/Result, activation/last-trigger timestamps and
CPUUsageNSec/MemoryCurrent/TasksCurrent where available. Do not print ExecStart,
Environment, journal bodies, process arguments or configuration. Unavailable
accounting is unknown, not zero. Timing should be compared with the already
retained SSH failure times; a later quiet sample cannot prove the earlier cause.
This is more discriminating than further connection-timeout variations or
QEMU lifetime counters. Another native SSH refusal ends that observation; it
does not authorize a retry loop or a console attach bypass.

**Conditional preparation boundary, not a tuning selection.** Source identifies
only two especially narrow candidates to isolate if that observation supports
periodic-job contention: `vpsadmin-api-prometheus-export-base.timer` and
`vpsadmin-api-prometheus-export-dns-records.timer`. Their task owner
`api/lib/vpsadmin/api/tasks/prometheus.rb:238-570,756-762` queries inventory/DNS
and publishes metrics files; the original `ip-inventory` fixture/scenario has
no dependency on these exporters. They are not the API request workers,
transaction supervisor, scheduler, database, broker, node daemon or member PHP.

If root explicitly accepts such preparation after the observation, require
the expected immutable services source/closure and exact loaded units, record
their initial timer active/inactive and enable states, and stop only those
two timers through ordinary public SSH. Do not stop/kill their executing
oneshot services. Timer stop does not terminate already-running work: require
the corresponding services and metrics-deploy oneshot to finish naturally and
be inactive before claiming quiescence. If they remain active within the
selected bounded window, hold rather than kill, wait indefinitely or widen
the unit set. No disable/mask/daemon-reload, service restart, environment or
database modification is part of this candidate.

Keep every capture dependency and all source/lease/capacity/timeout guards.
Root would need fresh original API/member/SSH success and capture admission
after the preparation; stopped timers alone are not a health or fit pass.
Restore only timers that were initially active after browser/lease cleanup,
leave initially inactive timers inactive, and prove final active/enable state.
Do not claim the exact prior deadline or missed-run history was rolled back;
restoration may schedule an overdue run. Retain this extra operator preparation
beside reserve/capture provenance, with no source/artifact relabeling. Losing
public SSH makes preparation/restoration unproved and stops dependent work.

No timer suspension is recommended from source declarations alone, and no broad
"disable all rake tasks", reporting-service stop or worker/buffer tuning is
selected. The source shows a reversible candidate, not its expected benefit.
If the finite observation cannot establish useful activity/resource evidence,
or SSH cannot be used safely, the concrete blocker remains unreliable mandatory
services attestation on the current2GiB guest. The existing full-service module
was declared for8GiB; its reduction is not a measured sustained-fit guarantee.
There is then no supported no-build source fix established under the standing
no-builder/no-RAM-increase/no-new-pair constraints. Hold capture and report the
missing evidence rather than repeat lifecycle/capture attempts or infer success.
The completed ordinary stop/resume proof remains valid with its explicit missing
sentinel limit; no new continuity campaign is proposed.

Fresh current/absent markers and roster17/settings were verified. Applicable
workspace/K guidance was reused; V instructions/documentation and the owning
selected module/task sources were read. Only this diagnosis was appended.
No private input/raw-log read, source edit, check, CI observation, guest/process
probe, lifecycle action, Git/ref mutation or preparation was performed.

### PROPOSAL: bounded K services workload for the reduced single profile (2026-10-11)

This is a source proposal awaiting root acceptance, not permission to change
the running environment or to start another attempt. The one selected workload
observation (`finish-working-delivery-services-workload-observation4.json`)
returned native1 after5.449s with empty stdout. It supplies no guest pressure,
exporter-activity or causal evidence. Recurring services SSH banner failure
remains unexplained. Root's final public stop900 is independently watcher-owned;
this brief neither observes nor certifies its result. Failed campaigns, both
capture windows and the successful node-reserve restorations remain unchanged.

**Concrete source mismatch and proposed owner.** Exact Kf467934d3f678abc8b552f89805636d4d910438a
at `/nix/store/xllyhnv9ba1d49f9fvdwbpgxaf04phdf-source` forces the configured
services memory in `cluster/nix/test.nix:73,1371,2034`, but imports V's services
test module at2042. The selected V939159 module
`tests/configs/nixos/vpsadmin-services.nix:250-258,510-524` was declared with
8192MiB, a1024M MySQL buffer pool,200 connections and two API workers with up
to8 threads each. Its owning database defaults
(`nixos/modules/vpsadmin/database.nix:68-104`) additionally permit256M join,
512M sort and128M read buffers,96M temporary tables and1024M heap tables.
The nested WebUI FPM pool (`nixos/modules/vpsadmin/webui.nix:215-235`) permits
32 children and starts two. These are configuration limits; they are not a
measurement of resident memory or proof that any buffer was allocated during
the failure. Their scale is nevertheless inappropriate as the deliberate
starting policy for a small, sequential documentation fixture.

Implement one K-local declaration block in `cluster/nix/test.nix`, selected
only by the existing `topology == "single" && serviceMemoryMiB == 2048`
configuration. No new JSON field, profile registry, engine interface or V/OS
module change is needed. Other topologies and the normal4096MiB configuration
retain their inherited declarations. Use these explicit qualification targets:

| Effective setting | Reduced-profile value |
| --- | --- |
| `services.mysql.settings.mysqld.innodb_buffer_pool_size` | `256M` |
| `max_connections` in that same attribute set | `64` |
| `join_buffer_size`, `sort_buffer_size`, `read_buffer_size` | `1M`, `2M`, `1M` |
| `tmp_table_size`, `max_heap_table_size` | `16M`, `16M` |
| `vpsadmin.api.workers` | `1` |
| `vpsadmin.api.threads.min`, `.max` | `1`, `4` |
| Nested WebUI FPM `pm.max_children` | `4` |
| Nested WebUI FPM start/min-spare/max-spare | `1` / `1` / `2` |

Apply the FPM declarations to
`containers.webui.config.services.phpfpm.pools.vpsadmin-webui.settings`, not
to an unrelated host PHP pool. Resolve inherited ordinary definitions with
per-leaf `lib.mkForce` where required; ordinary values suffice against the
database module's `mkDefault` buffers. Do not force entire service/module trees.
Keep dynamic FPM, its500-request recycling policy, logging, API authentication,
request/SSH deadlines and all actual SQL consistency/durability settings.
The smaller SQL workspace/table limits may spill work to disk or queue/fail
excess concurrency; that tradeoff is acceptable only for this dedicated fixture
and must be qualified. Neither64 connections nor these buffers constitute a
computed total memory cap. Keeping one API worker and four request threads
retains concurrent request handling without claiming production throughput.

Also set only the two existing
`vpsadmin.api.rake.tasks.prometheus-export-{base,dns-records}.timer.enable`
leaves to false for this profile. The V rake owner at443-469 otherwise launches
these independent full API/Ruby jobs every2/10min; their task implementation
queries inventory and publishes metrics, which `ip-inventory` does not consume.
Keep their task definitions and the metrics integration available; suppress
automatic scheduling, not arbitrary executing services. This is a prospective
declaration, not authority to stop the current timers.

Preserve all other default tasks, including authentication/session expiration,
dataset expansion, incident processing, the scheduler and supervisor. Incident
processing can perform CPU-limit transaction chains
(`api/lib/vpsadmin/api/tasks/incident_report.rb`), so treating all reports as
irrelevant would be too broad. Preserve MySQL, RabbitMQ, Redis, API/HAProxy,
nginx/member PHP, console-router, node daemons and template/provisioning paths.
Do not disable plugins, Adminer, status checks or safety-related work as another
unmeasured optimization. The real1CPU/1GiB/4GiB VPS, dedicated disabled pool,
member/admin roles, bilingual scenario, quota and positive capture thresholds
stay exact. Node reserve is a separate already-recorded operator-preparation
requirement; this services proposal does not pretend the source declares64MiB.

**Minimal implementation and verification boundary.** Application owners are
`cluster/nix/test.nix`, the existing configuration-projection coverage in
`tools/test-runtime-verify.rb`, and a short reduced-profile paragraph in
`cluster/runtime-contract.md`. Extend the existing pinned Nix projection to
read effective services and nested WebUI configuration through the selected
modules, following the repository's actual NixOS projection pattern. Assert
the table above, absence of just the two generated timers, continued presence
of their service definitions and of essential API/database/supervisor/scheduler,
authentication/session/incident/dataset tasks, and unchanged normal-profile
values. Check actual merged/generated Puma/FPM/MySQL settings where exposed,
not source-text matches. Retain the existing2x2048MiB runtime,2048MiB builder,
8GiB image/root and8GiB tank/kernel assertions. No new test runner or dependency.

User's no-local-CI rule remains. The declared focused owner is
`nix develop --command ruby tools/test-runtime-verify.rb`; use the existing
hosted `Check` route, whose source command is
`nix develop --command bin/check --allow-missing`, without workflow edits or
re-running unrelated V/W suites as a new prerequisite. Root owns source
publication, exact K package/E input composition evidence and affected committed
review before any construction. Keep the same V/OS pins and input graph. The
change has no database migration, protocol/schema, key policy or production
configuration effect. It creates a different genuine K artifact/closure; old
source attestation must never be relabeled. Reverting the declaration does not
authorize an automatic artifact downgrade or data rollback.

**Public update does not provide offline preparation.** In exact f467
`cluster/lib/kb_runtime.rb:187-234`, a previously unprepared update first requires
the old run to be ready and attested, creates its candidate, then builds and
imports exact closures while that predecessor is live. Only an already fully
prepared journal can continue offline. `resume:176-183` requires the identical
accepted source/artifact (`validate_prepared:146-173`) and cannot select the new
profile. `cluster/lib/kb_source.rb:74-96,129-147` generates a new artifact UUID
and embeds the instance/source/config identity in every guest before building
the complete cluster configuration. K's `sshModule` at1318-1323 places this
identity in the services root as well as the node. A placeholder offline build
is not that candidate and cannot establish its exact import/preparation proof.
There is no public `prepare` command or supported offline root modification.

Consequently, **stop both guests, build the fixed image, then perform a
cache-only public update preserving the same instance is not supported** for
this new, unprepared candidate. Do not create a journal privately, invoke
`Software.prepare`, substitute metadata, copy a new root or use the failed
Campaign as a preparation interface. Even if unchanged packages/kernels are
already cached, the candidate's guest identity makes a new image/closure
necessary. Its exact services import also requires reliable old SSH and guest
store headroom, neither supplied by a source review.

There are two explicit resource/disposition consequences, not new permissions:

1. Keeping the same instance/disks/credentials requires the existing public
   old-source resume and new-source update path. That requires relaxing the
   no-builder-while-guests-live rule for one2048MiB image builder alongside the
   two2048MiB old guests (6GiB guest/builder peak before host overhead), allowing
   a new8GiB candidate image while the old rooted image remains, and proving
   live import headroom. Old services SSH health makes this an uncertain route;
   source compatibility alone does not make it usable. No such exception is
   selected here.
2. To preserve the sequential2048MiB-builder/4096MiB-runtime limit, the smallest
   existing public route is an explicitly approved sequential replacement:
   after successful complete stop proof and preservation of the exact failed
   evidence outside the removable tree, public reset of **only** this disposable
   working3 instance, then one fresh public start from the new immutable K
   package/config. This sacrifices that instance's disks/credentials and creates
   fresh identities; it is not update, resume or adoption. It requires explicit
   reset/replacement and one new-image approval, presently absent. It adds no
   concurrent second pair and no engine/recovery changes. A stop/reset refusal
   ends this route before construction; no manual removal or force follows.

Recommend the second route if root/user decide to implement this profile while
keeping the strict sequential resource limit. Do not recommend a new public
offline-update mechanism solely to retain a disposable fixture. Until that
concrete disposition is accepted, the new profile has no admissible real route
under the current combined constraints. Retaining working3 instead is valid,
but does not authorize another cluster or establish room for it.

The replacement's eventual new outputs remain8+8+8GiB, not a universal free-space
floor. The old immutable image may remain in the store after public reset;
reset is not GC and promises no store reclamation. Root must account its actual
remaining blocks, new image/build staging and all other retained sparse growth
separately, crediting only observed space after an authorized operation. For a
disk-preserving update, account both immutable images plus exact imported
closures explicitly instead of calling it a24GiB total. No guessed scratch
constant, foreign cleanup or earlier capacity receipt proves this admission.

**One finite qualification after a separately accepted route.** Refresh exact
source/package/config/kernel/host admission, use the existing durable service
and reserve watcher, and let public start/update perform its real fit and
attestation checks. Reuse valid unchanged process/lease/trust/source tests and
the previous evidence at its original source. The new target needs measured
guest memory/disk/inodes and real API/member PHP/SSH/lease success, then the
already selected ordinary continuity/capture scope on that one instance and
the unchanged positive fit gates, CS+EN `networking/ip-address-list`, strict
inventory/export and visual review. Attribute any node reserve preparation to
the actual new run and restore it; do not carry f467 evidence across as native
new-source proof. A native failure ends this finite attempt with its state and
evidence retained. No automatic retuning, upscale, third attempt, broader suite
or cleanup is implied. Practical sustained fit and successful PNG generation
remain unproved until those steps succeed.

Current/absent markers and roster17 architect0 settings were reverified; the
documentation skill and required workspace/K/V guidance were read/reused.
Only this design proposal was appended. No application, private campaign,
process/guest, verification, Git/ref or lifecycle operation was performed.

### FINITE WORKING4 CONTINUATION: short browser temporary directory (2026-10-12)

Source assessment only, conditional on the original working4 native outcome.
Kcd2cfac65af26842b078617eeeaf82f346f18b07, paired E2e38a541, remains the
actual generator. Its accepted immutable source is
`/nix/store/w74cspfb7yckb4jb7ynsd4klziy7d72s-source`; package/selection binding
is recorded in `finish-working-delivery-package-realize3-acceptance.json` and
the finite admission in `finish-working-delivery-runtime-smoke4-preparation.json`.
No current guest result or liveness was observed by this assessment.

**Established caller defect.** `tools/runtime-verify.rb:20-32` keeps only four
inherited identity/runtime variables, then unconditionally assigns
`TMPDIR = root/temporary`. Therefore the wrapper's short TMPDIR cannot reach
the browser through this Commands object. The historical f467 fatal in
`finish-working-delivery-browser-path-diagnosis1.json` establishes the real
Chromium UNIX-socket path failure, not the as-yet unobserved working4 outcome.
`lib/browser.cjs:87-96` uses the ordinary packaged Chromium launch without a
different temporary-root override. No guest/image change is needed to change
this host-only child-process environment.

**Recommended separate public-operation route.** Let the original attempt end
and retain its exact native result, attempt hash and absent/present completion
facts. If failure is confined to browser preparation after genuine accepted
start, root may select one finite continuation on that same source-matched
instance. First establish fresh public status/connection and guest identity/
closure/ownership facts; an accepted historical start does not replace them.
Do not run `Campaign#run`, `runtime_smoke` or `bilingual_capture` directly to
skip their failed-attempt/prerequisite guards, and do not call start/update or
create a new campaign that claims the retained state. No live source result is
inferred from this proposal.

Use the existing finite public-driver pattern with a new private evidence
directory outside the failed Campaign. Construct the unchanged
`KbVerify::Commands.new(selection, evidence_root)` from the exact immutable
source, then assign its public `environment['TMPDIR']` to an already verified,
canonical, owned0700 short directory, such as a fresh `/tmp/kbc-<random>` root.
Record that directory identity and the exact environment exception privately;
preserve the selected PATH, browser/font/Node/Ruby packages, Nix limits and all
other environment scrubbing. Commands exposes the mutable hash via
`attr_reader :environment`; this needs no reflection or process-runner patch.
Only the new Commands object changes, not the active/finished verifier process.
The parent checks actual backing-filesystem/RAM effects in normal admission;
TMPDIR is not a builder-scratch bound. Keep it until browser/controller cleanup
finishes. Do not shorten paths by moving state or introducing a state symlink.

There is an important limit to the proposed helper reuse: Campaign's Ruby
methods are public but do not form a separate documented resumable phase API.
`read_smoke:539-577`, `resources:604-629` and `capacity:419-486` write beneath
the object's Campaign root; `engine('resume')` also invokes capacity. Changing
TMPDIR alone would thus still write new evidence into the old Campaign.
Do not treat the whole method chain as a supported resume or redirect its root
to make it discover another instance.

Instead retain the earlier finite public-driver composition: the unchanged
read-smoke JavaScript body invokes the same selected Connection.verify, native
TLS/API identities, browser/member login and lease/cleanup through Commands;
its result goes to the new evidence directory. The unchanged
`resource_script(machine)` body goes through public SSH with stdin intact,
with its original numeric parsing and positive admission checks. Bind these
copied command bodies to their exact immutable source/hash; do not modify their
assertions. Read-only `descriptor`, `identities`, `sentinels`, `continuity` and
`resource_script` logic can be reused against the original root where it only
reads retained records or invokes public commands. Do not use `send`, allocate
an uninitialized object, override Campaign methods or call private Engine
lifecycle methods. A driver that reuses the exact-source Campaign constructor
must retain its selection/configuration checks and never print its `inputs`.
Save the public connection's original bytes for descriptor-digest consumers,
not a reformatted JSON encoding.

The concrete sequence is fresh attested descriptor/resources; native member
read; unchanged `tools/verify-live-lease.cjs` with the exact package metadata,
runtime, state root and configuration; exclusive creation of the two dedicated
sentinels only if absent; six-credential/account/artifact/disk/image and sentinel
baseline; ordinary public stop900 plus complete exit proof; refreshed resume
capacity; ordinary same-source resume900; fresh source/closures/trust and
continuity comparison, resources and member read. All lifecycle calls execute
the original packaged `vpsfree-kb-devcluster` against the original root/slug.
Native command records, resource observations and the final assertion summary
belong solely to the new evidence unit. Retain the same finite failure boundary,
durable execution context and reserve monitoring. No reset, new image/pair,
resource increase or forced cleanup follows from this assessment.

**Capture can remain genuine Gcd2 evidence.** After the separate continuity
proof and original positive host/guest capture gates, invoke the genuine paired
`vpsfree-kb-capture`/`vpsfree-kb-validate` executables directly using this short
TMPDIR. The selected package wrapper sets its client PATH/browser/font/Node
environment but does not replace TMPDIR. Keep CS cluster selector, EN canonical
connection selector and packaged writable-CWD recapture on the same resumed
instance and one fresh output root; then candidate update, strict full inventory,
physically locked five-file export and visual review. Keep the already accepted
node-reserve preparation/restoration as separately attributed operator work if
required; zero or failed admission never permits fixture execution. Capture's
own locks, live lease, source/artifact/closure proof, fixtures and result merging
are unchanged. The failed verifier's `bilingual-capture` phase remains ineligible;
direct public captures and a separately completed public lifecycle evidence unit
do not fabricate its `receipts/runtime-smoke.json` or turn its failure into a pass.
G-to-media provenance remains cd2cfac65 even if a later commit records the PNGs.

**Permanent verifier correction remains narrow.** The above can finish public
operations without rebuilding guests, but does not certify the unmodified
Campaign runner for long roots. Its owning follow-up would make Commands honor
an explicitly selected valid private short TMPDIR, with focused existing
`tools/test-runtime-verify.rb` coverage that proves the spawned child receives
it while all unrelated environment/source scrubbing remains. No current source
edit is assigned here. That harness-only correction needs its own affected
hosted evidence/review if selected, not another image or unrelated V/W campaign;
its revision must not be substituted for the running cd2cfac65 generator.

Fresh current/absent markers and roster17/settings matched. Required guidance
and the documentation skill were read/reused; only this reconciliation was
appended. No active-run poll, private inputs, application edit, check, build,
guest/process operation, package/ref mutation or lifecycle action was performed.

### BOUNDED CAPTURE FIX: omitted zero-swap control and genuine Gcd2 media (2026-10-12)

Root's completed separate working4 public proof establishes API/member/TLS,
lease and ordinary stop/resume with all six credentials, accounts, retained
trust, disks/image and root/ZFS sentinels. It does not turn the original failed
Campaign into a pass. The next CS failure is independently retained in
`finish-working-delivery-capture-core-failure4-diagnosis.json`: the original
core reached `fixtures/prepare.cjs:99:51,631:39` and timed out filling swap;
no PNG was accepted and node reserve1048576 was restored. This brief proposes
the narrow fixture correction and an explicitly attributed same-pair preparation,
not new guest operations or retrospective fixture-mutation absence.

**Source mechanism and permanent two-owner fix.** At exact
Gcd2cfac65af26842b078617eeeaf82f346f18b07, `createVpsIn:64-125` fills every entry
in its supplied resources map. The inventory tuple at556 is
`{cpu:1, memory:1024, swap:0, diskspace:4096}`. Pinned V939159
`webui/forms/vps.forms.php:395-423` deliberately skips a resource row for an
ordinary member whose allocation value is exactly zero. Its
`webui/pages/page_adminvps.php:136-145` supplies omitted swap as zero on final
submission. Thus absence of that particular control is valid for this requested
tuple; waiting for it cannot make the form correct.

Change only `fixtures/prepare.cjs` and `tools/test-ip-inventory.cjs`. In the
resource loop, skip a missing control only when `name === 'swap'`, the requested
value is numeric0, and the locator count is0. Present swap still receives the
requested value, including0. Missing nonzero swap, CPU, memory or disk remains
a refusal; ambiguous/multiple controls must not be selected with `.first()`.
Do not catch a broad fill timeout, skip other zero resources or substitute a
default for an unknown field. Keep `INVENTORY_RESOURCES`, member identity,
`waitForRunning`, and `ensureIpInventory:559-619` unchanged: the real resulting
VPS must retain its owner/hostname and all four resource values, including swap0,
before dedicated IP provisioning proceeds.

Extend the existing member-form fixture at `tools/test-ip-inventory.cjs:361-455`
to model real locator absence instead of returning count1 for every field.
Exercise actual `createVpsIn`/preparation paths: missing swap+requested0 succeeds
without a fill; present swap0 is filled; present nonzero swap is filled; absent
nonzero swap refuses before final submission; each other required control's
absence refuses even if a proposed value is0. Preserve strict resulting-resource
mismatch refusal and member/admin role separation. Tests should assert the
submission boundary and observed fills, not merely match the new conditional.
The existing hosted `node tools/test-ip-inventory.cjs` owner and normal affected
K source check/review suffice; no browser/VM framework, timeout increase, V
change, schema/migration or new resource profile is involved. No check is run
by this design task.

**Immediate same-G operator preparation is source-supported.** The unchanged
module exports `createVpsIn` and accepts a caller-supplied resource map
(`prepare.cjs:713-714`). Under root's separately recorded finite operation,
the original Gcd2 Connection.verify and live lease can guard an ordinary
test-user1 browser throughout. Before final creation, prove that member identity,
the bounded owned-name lookup has no `ip-inventory` VPS, member swap allocation
and the rendered omitted-swap/default0 contract, and the existing positive
host/guest memory, quota/template/tank and TLS/source/trust admission. A partial
fixture or name/owner ambiguity is a refusal, not delete/rename/adoption authority.

Call the original exported helper with member.id, hostname `ip-inventory`,
boot=true, `Production`, `Praha`, and a new map containing only
`{cpu:1, memory:1024, diskspace:4096}` after asserting the original constant's
swap is0. Do not mutate that exported constant, replace the module, monkeypatch
its internals, switch the browser to admin or invoke a raw guest/DB shortcut.
The original PHP submission supplies swap0. Retain the returned VPS ID and
prove the real native API owner, exact hostname and numeric resource tuple
including swap0; a returned/null/missing/nonzero value must not be accepted as
the intended zero. Keep provisioning and later capture within the original
lease/source rules, with normal browser-before-lease cleanup. Failure ends
this preparation and preserves any created fixture for diagnosis.

After that proof, the original packaged Gcd2 capture uses
`findOwnedVps:26-41` and `prepareFixtures:627-633` to find the existing owned VPS,
wait for it to run, then execute its unchanged strict resource/IP/pool checks
and provisioning. It therefore avoids the broken creation branch without
changing capture code or bypassing a check. Record the preparatory member UI
operation, exact tuple and actual source beside the existing reserve window;
do not call the unmodified fixture a successful first-creation test. Preserve
the failed CS output and use the selected fresh output/evidence unit. CS/EN,
connection/default-CWD coverage, strict validation, physical locks/export and
visual acceptance remain required. No new image, artifact, VM pair or resource
increase is necessary for this caller-level preparation.

**G-to-final-media lineage must remain explicit.** Preserve the exact published
`retained-network-working-gcd2cfac6` generator ref, original immutable tools,
original G validator proof and the full allowlisted five-file export. The
permanent fixture fix changes `Software.fixture_digest`; it does not retroactively
change the actual guest/capture generator. `cluster/source-metadata.rb:5-17`
correctly refuses validation of G result/source receipts against changed
fixtures or a different checkout revision. Do not relax that check, feed an
M metadata file to G, or import G's `tmp/capture-{results,source}.json` into the
fixed M source tree as if freshly generated there.

For normal source carryback, commit only the two verified PNGs and their
candidate `captures.json` changes, preserving embedded G provenance and the
unchanged V pin/semantic contract. Keep the two supporting result/source receipts
as original-generator evidence outside that source tree. The existing validator
can strictly check M's committed inventory/PNG hashes without reinterpreting
external G results: `runner/validate-artifacts.cjs:15-25` invokes receipt/source
verification when external results/source receipts exist or `--update` is used;
ordinary validation of the already committed inventory uses its source assets.
That M check proves committed artifact consistency, while G's original strict
validation proves generation/source matching. Neither claims that M's changed
fixture has run in a guest. Retain this distinction in final review/handoff;
the new two-owner fixture behavior receives its focused hosted evidence, and
the actual PNG generation remains the operator-prepared Gcd2 execution.

Current identity, absent markers and saved roster17 architect settings matched.
Applicable workspace/K/V guidance and documentation skill were reused; owning
source and the allowlisted failure were read. Only this design was appended.
No private campaign/credentials, application edit, test/build/eval/probe, Git,
CI, guest/lifecycle or capture operation was performed.

### FINITE OPERATOR POLICY: explicit64MiB node capture margin (2026-10-12)

The window5 refusal is valid and remains a failure of the original admission:
node MemAvailable1176363008B was below1207959552B (1GiB+128MiB), before the
Node fixture helper or VPS mutation. Services308723712B exceeded256MiB and
tank7800932864B exceeded5GiB; the other recorded disk/inode gates passed.
The successful restoration to min_free_kbytes1048576 and the prior complete
same-G public continuity/member proofs remain distinct results.

**Recommendation: permit root to select one explicitly reassessed operator
attempt with64MiB extra node margin.** Its threshold is exactly1140850688B
(1073741824B requested fixture RAM +67108864B), not64MiB total available RAM.
The old window observation would exceed that threshold by35512320B, about33.9MiB,
and leaves about97.9MiB above the full requested1GiB. These calculations explain
the proposed tolerance; they are not fresh admission or proof of a future peak.
This is a proportionate limited-risk qualification policy for one disposable
1CPU/1GiB/swap0/4GiB fixture with no second VPS or simultaneous capture, not a
generally sufficient runtime margin or a diagnosis of prior service failures.

The source gate (`tools/runtime-verify.rb:614-625` at Gcd2cfac65) accepts an
explicit positive assessment and compares it with actual MemAvailable. The
128MiB addition was an operator assessment, not a minimum hard-coded by the
engine or fixture. Linux MemAvailable already accounts for kernel low-watermark
reserves; do not add separate cache, reclaimable-slab or ARC figures to it or
count a reserve reduction as an independently guaranteed amount of free RAM.
The later stock-reserve snapshot in
`finish-working-delivery-node-memory-observation1.json` reports MemAvailable0
with min_free_kbytes1048576. It does not supply the new window's available
memory. Its ARCsize11320440B, c_min64802304B and reported physical free value
establish neither reclaimable ARC credit nor a safe peak. Missing PSI is unknown,
not zero pressure. No swap is available as a fallback.

Root must record a new separately hash-bound operator assessment before the
window, referencing the original capacity4 digest, exact Gcd2/configuration,
instance/run/artifact and supporting observations. Change only the declared
extra node margin128->64MiB. Keep capacity4, the Campaign, failed window and all
original receipts immutable; do not present the new assessment as a correction
to historical measurements or a pass of the former gate. No source/schema or
validator change is required to express this separate operator decision.

Keep two2048MiB guests, the already accepted min_free_kbytes65536 preparation
and explicit restoration to1048576, full fixture resources/API verification,
positive services256MiB/inode/1GiB-disk gates, node4+1GiB tank requirement and
host2GiB RAM/1GiB shared-memory browser margins. Retained growth/base reserve,
current disk admission, source/trust/lease/physical artifact locks, member/admin
separation, genuine CS+EN, strict validation/export and visual acceptance remain
unchanged. Re-read actual positive node headroom under the proved65536 setting
before mutation; stock-reserve or previous-window values cannot substitute.
The existing driver at `finish-working-delivery-operator-capture-window5.py:189,205`
checks resources before preparation and before each capture. Preserve those
checks: provisioning can consume headroom, so passing preparation does not
guarantee that CS, EN or default-CWD recapture will be admitted.

Peak kernel/slab, ZFS, container boot and background-work demand remain unproved;
the smaller margin increases the risk of a native refusal or memory-related
failure even if admission passes. Select one finite window only. Any failed
resource/ownership/transport/provisioning/capture check ends dependent work,
retains exact partial state/results and triggers the existing guarded reserve
restoration/cleanup boundaries. No further margin lowering, min_free32MiB,
drop_caches, daemon stop, quota shrink, automatic retry/upscale, new pair or
old-state cleanup follows. Success would prove this recorded operator-prepared
capture, not stock-profile sufficiency or completion of the failed Campaign.

Fresh session/current/absent markers and roster17 settings matched. Applicable
unchanged guidance was reused. Only safe evidence/source and this design were
read or written; no admission, guest/probe, check/build/CI, application/Git or
lifecycle action was performed. Root owns policy acceptance and any operation.

### PROPOSAL: one 4+4GiB runtime with unchanged disk sizes (2026-10-12)

The user now permits modest doubling of test RAM. Assess one services guest
and one node, each4096MiB, with services root/image8192MiB and tank8GiB.
This supersedes the earlier RAM ceiling only. It does not establish capacity,
repair the current SSH failure, authorize reset, or complete a failed Campaign.
Fresh current/absent environment markers and retained roster17 matched;
architect0 remains Astra/xhigh/design/workspace_write. The documentation skill
and applicable workspace/K guidance were applied. Source evidence below is
immutable Gcd2cfac65af26842b078617eeeaf82f346f18b07, paired E2e38a541,
not the held fixture correction or another mutable implementation.

**Configuration and workload.** The public launcher already accepts this RAM
configuration: `cluster/nix/test.nix:1371,2014,2061` selects services runtime,
node runtime and services image-builder memory from the explicit configuration.
The builder consequently becomes4GiB too; preserving a2GiB builder would need
a separate source change and is not implied here. Disk sizes need not increase.
However, the current bounded SQL/API/PHP workload applies only when topology is
single and services RAM equals2048 (`test.nix:1383`). A RAM-only4096 config
restores the inherited1GiB MySQL buffer pool,200 connections, large per-query
buffers, two API workers/eight threads,32 PHP children and both metrics timers.
The owning projection test records those distinctions at
`tools/test-runtime-verify.rb:959-1000`; this is not evidence that those defaults
caused the observed SSH failures.

Recommendation: preserve the existing bounded workload when extending the
dedicated single runtime to4096MiB. The smallest prospective K change is to
extend that existing single-topology predicate to the two explicit supported
sizes2048/4096, retain its values, and adjust its owning projection test and
contract. This intentionally changes K's single4096 workload, previously left
inherited; other topologies remain unchanged. No new profile framework,
production V/OS policy or dependency change is needed. Root must accept that
small source boundary before implementation; no held source was changed here.
A config-only launch at exact Gcd2 remains supported, but it must be described
as the inherited4096 workload, not extra RAM for the previously bounded one.

**Public transition rules.** `cluster/launcher.rb:40-50` permits replacement
config only for start/update. `Engine#start` at `kb_runtime.rb:107-128` requires
fresh state and prepares its actual artifact before starting guests. `resume`
at176-184 validates the exact selected source, accepted artifact, retained
config/preparation, credentials and disks; it cannot change RAM or guest source.
Neither editing private inputs nor supplying a new config to resume is a route.

Public update at187-264 can change memory while preserving root/tank sizes,
endpoints, TLS identities and credentials: `Software.layout` at
`kb_source.rb:111-126` excludes RAM but retains disk compatibility. It first
requires a ready live predecessor and successful guest SSH/source attestation,
then builds and imports the exact candidate before ordinary shutdown/direct
boot. Current reported services SSH failure blocks this admission. A stopped
old artifact cannot prepare a new candidate offline; only an already completely
prepared update journal has that recovery path. No cache assumption bypasses
old-guest attestation, import or prepared-artifact proof.

The preferred disk-preserving route, if root establishes current guest health,
is one separately selected public update to the accepted4096 configuration.
This requires explicitly revising the prior no-builder-while-guests-live
scheduling constraint: a4GiB builder overlaps the current2+2GiB guests, then
exits before the new4+4GiB pair starts. Both peaks are8GiB plus measured host
overhead, with no second pair. This is a proposed admission change, not an
operation selected here. If that overlap or working predecessor is unavailable,
the existing route is proven ordinary stop followed by an explicitly approved
owned reset/replacement and fresh public start, building while both old guests
are stopped. RAM permission alone does not approve deleting retained disks.
An incomplete stop holds either route; no private preparation, force cleanup,
fresh pair beside a live old pair or old-state adoption is permitted.

**Node reserve and resource admission.** Exact OS6bdf
`os/modules/config/tunables.nix:74` defaults min_free_kbytes to1048576KiB,
independent of guest RAM. At4GiB, initially retain that source policy and measure
actual MemAvailable; do not presume it remains zero or estimate availability
by adding2GiB to an old observation. Keep the full1GiB fixture and original
positive128MiB extra capture margin, services256MiB and all disk/inode gates.
Doubling RAM does not require a further admission-margin reduction. If a
dedicated lower reserve is still necessary, the already bounded65536KiB policy
is the concrete existing candidate, not a new32MiB value or ARC/cache credit.
It must be selected explicitly as guarded operator preparation/restoration or
declared by a separately accepted K node module; it is not part of Gcd2's
4096 configuration. No claim of practical fit follows without the native read.

Fresh start/resume admission counts8GiB runtime RAM/shared memory plus assessed
overhead. The existing2GiB RAM/1GiB shm overhead example becomes10GiB available
RAM/9GiB free shm before runtime start, subject to refreshed actual assessment;
already-live capture counts only its additional margins. Intrinsic fresh disk
extents stay24GiB (8GiB image +8GiB writable root +8GiB tank). An update retains
the old image and creates a distinct candidate image and imported closures;
those measured allocations and temporary costs are additional, not deduplicated
because sizes match. Existing allocated bytes already reduce free space;
retained sparse growth/base reserve, missing closures and unknown builder
scratch remain separately accounted. No cleanup credit or universal disk floor.

**Evidence route and stop condition.** Current `Campaign#validate_config`
at `tools/runtime-verify.rb:144-177` explicitly refuses4096. Use separately
recorded public lifecycle/read/lease/capture operations if source is unchanged;
do not call that a completed Campaign or bypass its failed-attempt/config guard.
If the packaged verifier itself is selected for4096, its narrow profile check,
existing config/accounting tests and owning documentation must first be revised
and reviewed; the existing `memory_requirements` method already derives demand
from config. No broad verifier redesign is required or authorized here.

Only affected hosted projection/config checks and committed review are needed
for any accepted source delta; reuse unchanged evidence and preserve the user
no-local-CI rule. One admitted native qualification must prove real source,
closures, TLS/SSH, member/API/lease and ordinary same-artifact continuity, then
the same instance supplies CS/EN and strict export if positive gates pass.
Short private TMPDIR and the accepted omitted-swap boundary still apply.
Any native failure ends dependent work and retains evidence; no automatic
further upscale/replay or extra pair. Generator provenance must name the actual
new artifact's immutable source, never relabel the old Gcd2 guest. This report
is source assessment only; no operation, source edit, check or probe occurred.

### ACCEPTED IMPLEMENTATION ADDENDUM: bounded 2048/4096 profile (2026-10-12)

Root accepts the preceding RAM proposal with **one sequential fresh replacement**
as the selected route, subject to root-owned preservation, retirement and measured
admission. Old-guest update is not required. Root reports working4 shutdown after
the separately selected services pidfd TERM, complete exit of all14 children,
absent claims/socket and retained disks. This does not turn that recovery into
an ordinary graceful-stop pass. The stopped source/artifact cannot be resized
or adopted through resume; the replacement uses genuine public fresh start with
new preparation and provenance. No old failed Campaign is replayed or edited.

The minimal K implementation owners are:

- `cluster/nix/test.nix`: extend only the existing single-topology compact
  services predicate from2048 to the explicit set `[2048 4096]`. Keep every
  compact SQL/API/PHP value and the two timer selections unchanged. Other
  topologies keep their inherited settings. No new configuration mode or knob.
- `tools/runtime-verify.rb`: in the existing single/local profile validation,
  allow services RAM and node1 RAM independently to be either2048 or4096MiB.
  The selected replacement is4096/4096. Preserve exactly two guests, explicit
  networking/accounts, services image/root8192MiB, tank8GiB and all other guards.
  Keep existing memory derivation; do not add a second accounting mechanism.
- `tools/test-runtime-verify.rb`: extend the existing config, accounting and
  public Nix projection/generated-service tests. Prove compact effective MySQL,
  generated MySQL/Puma/PHP configuration and timer policy at both supported
  single services sizes. Move the inherited-workload comparison to an unchanged
  other-topology case rather than retaining the obsolete single4096 expectation.
  Cover both mixed RAM combinations as valid, unsupported values as refusals,
  unchanged disk/topology/account refusals, runtime/builder values and kernels.
- `cluster/runtime-contract.md` and `docs/webui-change-workflow.md`: reconcile
  the supported choices, chosen4096/4096 qualification, compact4096 behavior,
  sequential preparation and measured admission. No other owner is required
  by this addendum; preserve the separately held TMPDIR/zero-swap drafts.

Accounting acceptance: with the assessed2GiB RAM/1GiB shm overhead,4096/4096
requires10GiB available RAM and9GiB free shm before runtime start/resume. The
4096MiB image builder runs before runtime guests and is assessed separately;
do not sum stopped guests with it. Already-live capture requires only its
additional2GiB/1GiB margins. Tests must prove these values and the existing2048
case, including source/config binding and rejection of stale capacity evidence.
Intrinsic image/root/tank extents remain24GiB; retained growth, actual additional
closures/staging and unknown builder scratch still need root's fresh assessment.
No node reserve, capture threshold, quota, trust, lease or disk policy changes
are part of this source unit.

Use hosted affected config/accounting/projection checks and committed independent
review before package construction or the one real replacement qualification;
no local CI. Reuse unaffected evidence. Real acceptance remains public readiness,
API/member/TLS/lease, ordinary same-artifact stop/resume with credentials/accounts/
trust/disks/image/sentinels, then genuine same-source CS/EN and strict validation/
export if positive admission holds. One native failure ends dependent work;
no automatic extra pair, upscale, reset or repeat qualification. Root owns all
source assignment, Git/pins, retirement/backup/capacity and operational selection.

Current and both absent markers were checked from the exact tracking CWD with
login:false; fresh roster17 retained architect0 settings. Unchanged applicable
guidance and the documentation skill were reused. Only this design addendum
was written; no application, private-state, test/build/probe or lifecycle action.

### DISK ACCOUNTING ADDENDUM: sequential image construction and runtime (2026-10-12)

This is a receipt-assessment refinement, not a source change or admission.
Fresh current/absent markers and roster17 settings matched; unchanged required
guidance was reused. Read-only evidence is Gcd2's unchanged Engine/Software/disk
owners and exact OS6bdf/nixpkgs5dfba623 sources. No private capacity/configuration,
cache or filesystem observation was read or performed. K6cfd source/package
checks remain root-owned; no result is inferred here.

**The phases do not allocate all their files concurrently.** Gcd2
`cluster/lib/kb_runtime.rb:107-128` completes `Software.prepare` and `build`
before `start_locked` at274 creates runtime directories and spawns the runner.
`kb_source.rb:74-95,129-146` first evaluates the actual prepared identity/config,
then completes the cluster-config and runner builds. Only the runner's
`PreparedDisks#prepare_disks` in `cluster/lib/kb_machine.rb` copies the published
image with `IO.copy_stream`; the base OSVM `Machine#prepare_disks` at
`osvm/lib/osvm/machine.rb:799-805` creates the tank by truncate. Thus runtime
root-copy/tank allocation starts after successful image construction, not during
the earlier staging-root/image preparation. The tank remains a full8GiB eventual
obligation even when initially sparse. No root-copy sparsity saving is assumed.

OS `tests/make-test.nix:253-266` selects raw format, an8GiB image and no partition
table. The pinned [image builder](https://raw.githubusercontent.com/NixOS/nixpkgs/5dfba6236110080a54247d6460bc2ff5dda939cc/nixos/lib/make-disk-image.nix)
at434-494,568-597 stages an installed root, creates the raw image, copies the
payload into it and publishes raw output with `mv`. It does not unconditionally
convert raw to a second image. Same-filesystem rename needs no second full
image; cross-filesystem move or separately evidenced store-import behavior can
require additional simultaneous bytes. The pinned
[VM wrapper](https://raw.githubusercontent.com/NixOS/nixpkgs/5dfba6236110080a54247d6460bc2ff5dda939cc/pkgs/build-support/vm/default.nix)
at264-307 runs preparation, image-finalization VM and publication in that order.
None is the later runtime root copy. Actual daemon sandbox/output filesystem
semantics and retained temporary bytes still require root's evidence; a client
TMPDIR or NAR total does not establish those facts.

For a fresh instance on one proven shared filesystem, describe known prospective
allocation in two rows, excluding bytes already reflected in measured free:

- Construction: newly missing permanent closures + staging payload/workfiles +
  the8GiB image allowance + any evidenced image-publication copy overlap.
- Runtime: newly missing permanent closures +8GiB image +8GiB writable root +
 8GiB tank eventual growth, plus any construction remnants actually retained.

Use the larger row, not their sum. The eventual intrinsic output stays24GiB.
In particular, do not charge an additional16GiB root/tank in the construction
row and then add its staging charge on top of the full runtime envelope.
Keep transient substitution/import bytes in their actual phase and filesystem;
never deduct closure bytes merely because the same payload is also inside an
image. Deduplicate actual store paths/inodes, not logically similar content.

The existing verifier already charges remaining image/root/tank growth plus
missing non-image closures before `construction_overlap_bytes`
(`tools/runtime-verify.rb:398-480`). Its receipt can conservatively assess that
field as **the nonnegative construction peak excess above those already charged
outputs**, with the two rows and subtraction written explicitly in
`construction_overlap_assessment`. For fresh, single-filesystem, no-remnant
accounting this known excess is `max(0, staging + publication_overlap -16GiB)`.
That is not a claim that staging or unknown scratch is zero. Retain the separate
8GiB assessed build headroom and16GiB base reserve unchanged; unknown builder
scratch remains unknown and requires the existing live reserve monitoring.
For distinct filesystems derive each peak independently; runtime disk capacity
on one filesystem cannot offset scratch demand on another. If staging/remnant
or publication behavior lacks evidence, retain an explicit conservative
assessment rather than manufacturing a zero excess.

The old11.3GiB construction overlap is not automatically valid for the new
source/cache state, nor may it simply be deleted. Root should decompose its
meaning and rebind current realized/missing paths, exact image/payload facts,
daemon/state/store filesystems, effective one-job/core construction, phase rows
and monitoring assessment. This is supported use of existing receipt fields;
no engine/accounting framework or new tests are proposed. Preserve the original
capacity4 receipt unchanged.

Using only the supplied historical72GiB retained-growth declaration and current
125778415616B free, even zero additional overlap leaves about2.86GiB short of
72+16+8+24GiB, before any missing closures. This arithmetic is not fresh admission:
root's authorized stopped-working4 reset, if performed, changes both measured
free blocks and that instance's remaining-growth obligation. Count those changes
only after actual successful owned retirement and refreshed evidence. Existing
store images do not become free merely because their runtime was reset; no GC
credit or guessed reclaim is allowed. All other retained obligations persist.

One fresh public start follows only root's accepted evidence and measured fit.
A build failure retains its actual outputs/diagnostics and ends dependent work;
it supplies no cleanup or retry authority. Source sequencing establishes the
accounting shape, not a mathematical bound on future scratch or a passing host
capacity result. Only this design addendum was written.

### WORKING5 CONTINUATION: real source update before corrected captures (2026-10-12)

Root reports genuine K6cfd working5 runtime-smoke success, including78 native
commands and ordinary stop/resume, followed by a failed CS fixture query. Those
results and the failed bilingual Campaign remain immutable. Source inspection
used the realized K6cfd source
`/nix/store/xcv7hw7946rk8ygx3zdyih4c9mvcxpda-source`; no private state or native
response was inspected. The four GET query corrections and consuming fixture
test are root's separate implementation brief. Changing fixture/source digests
requires a genuinely prepared new artifact before its package can capture.

**Supported route, with a concrete outstanding blocker.** Public
`Engine#update` (`cluster/lib/kb_runtime.rb:187-264`) supports this same-instance
transition with the same explicit4+4GiB config,8GiB disks, V939/locked inputs,
endpoints, host keys and credentials. It attests the live predecessor, journals
the candidate, builds/imports, proves ordinary complete shutdown and boots the
new artifact. Do not stop first: an unprepared offline candidate is unsupported.
`Software.prepare/build` (`kb_source.rb:74-95,129-146`) records the real new
source/config/artifact and constructs its actual closures. There is no private
preparation, source override, metadata relabel or failed-Campaign replay.

However, the earlier prelaunch blocker at this design's7510 section remains
present in exact K6cfd: `cluster/lib/kb_closure.rb:112-120` still invokes
`df -i --output=iavail /nix/store | tail -n1`. The documented GNU df option
conflict prevents its inode measurement; successful tail can mask the producer
failure and the missing second number refuses capacity before import. Existing
`tools/test-closure.rb:30` returns synthetic numbers when it sees `df -B1`,
so its passing mocked coverage does not establish command validity. This is
source evidence, not an actual working5 update failure. A fixture-only correction
does not remove this blocker. Root must accept the already bounded two-owner
repair (`kb_closure.rb`, existing `test-closure.rb`) before selecting update:
remove `-i`, status-check both df producers before formatting, retain numeric
refusal and all reserves/proofs. Hosted execution of the emitted command plus
producer-error/malformed and existing space/inode refusal coverage belongs to
that existing owner, not a new suite/framework. No such edit is authorized here.

**Prospective measured admission.** This update differs from sequential fresh
start. Its4GiB image builder overlaps the existing8GiB runtime pair:12GiB
guest/builder demand plus assessed overhead. With the existing2GiB RAM/1GiB shm
assessment, that is a14/13GiB combined envelope; measured availability while
the8GiB pair already runs must cover the additional6/5GiB, without double
charging resident guests. After old exit, candidate runtime needs10/9GiB before
start; once live, capture needs its additional2/1GiB. No second runtime pair
is started. This builder overlap needs root's explicit operation admission;
the first-start capacity receipt does not certify it.

Build/import disk assessment must include a new8GiB immutable services image,
missing candidate closures, exact staging/publication overlap and assessed
unknown scratch. The old image/result roots remain; no GC credit. K's
`PreparedDisks` retains the existing writable root/tank and their identities,
so do not charge another writable16GiB pair. Keep their actual remaining growth
through construction, all other retained growth, base reserve and build headroom.
A tiny fixture diff does not imply a reusable image: artifact/source identity
changes the generated guest configuration. Actual new outputs/cache facts govern
the assessment; no guessed zero build or guaranteed8GiB-payload fit.

`ClosurePreparation#prepare` (`kb_closure.rb:45-90`) imports the exact recursive
candidate services closure through the old trusted SSH route before shutdown.
It requires writable guest Nix/store tools, missing NAR bytes plus256MiB and
missing path-entry count plus10000 free inodes, then verifies path contents,
references and the per-artifact guest GC root. Import consumes space inside the
retained8GiB services root; it is not another host image, but its resulting root
allocation is real. Node boots candidate read-only media with the same tank.
Retain post-update1GiB services free-space, inode, memory and tank capture gates;
passing the smaller import reserve alone does not admit capture. No GC, resizing,
old-image copy or profile activation substitutes for those checks.

**Finite operation and evidence.** After affected source gates and immutable
package binding, root may separately select the new package's public
`update SLUG --state-root ROOT --config SAME_CONFIG --topology single
--network local --timeout 900`. The existing durable service/fresh watcher must
span preparation, shutdown and replacement;900 is not a total build deadline.
Release prior capture leases first; normal nonblocking gate/refusal remains.
Before admission establish fresh old readiness/source/SSH, same config and
private continuity baselines. After success require new accepted artifact/run,
exact new guest identities/current-system closures, unchanged six credentials,
accounts/trust, disk identities and existing sentinel contents, plus current
TLS/API/member/lease and resource evidence. Do not invent another lifecycle
campaign to relabel the original passed one as a new-source full-smoke result.

Public capture has no Campaign-receipt prerequisite (`runner/capture.cjs` and
the runtime contract's connection/source/artifact sections). A new finite output
unit may therefore use the genuinely matching new runtime/capture/validator
packages, short private TMPDIR, actual physical locks and live leases, CS/EN,
both selectors/default-output evidence, strict full inventory and five-file
export. Retain prior partial fixture/output state honestly; unchanged fixture
identity/idempotence guards must validate it, never assume the failed CS did
not mutate. Preserve the actual new generator G and its immutable validation
proof when later media commit M records the PNGs; do not mix K6cfd results or
claim that M's guest ran. Original runtime-smoke remains exact-source evidence
for the unchanged mechanisms, supplemented by this actual update/capture unit.

Any source, capacity, guest-store, SSH, shutdown or candidate-attestation refusal
holds capture and preserves its journal/state. Retry, if later selected, must
use only the recorded candidate; no automatic rollback, new instance/reset or
alternate source is proposed. If adequate overlap/import capacity or the narrow
command repair cannot be established, report that exact blocker without launch.
Fresh current/absent markers/roster17 and full applicable guidance were read;
only this design was appended. No application edit, operation or passing new
source/runtime claim was made. Root owns source acceptance and any execution.

### WORKING5 UPDATE WORKSHEET: measured physical allocation assessment (2026-10-12)

Recommendation: the proposed smaller allowance is defensible for **one monitored
update as an explicitly assessed risk**, not as a bound or readiness approval.
It supersedes the earlier8GiB assessed build headroom only for this separately
recorded operation. Retained writable growth and the16GiB base reserve do not
change. Source/package gates are root-reported for Kb5e39e6/E9205957; the realized
K source is `/nix/store/9z238nf417z9ynj8qb14k7ipg0ma820k-source`. Its corrected
`kb_closure.rb:112-127` now status-checks the valid df producers, closing the
previous command-source blocker. Actual guest import admission remains unproved.

The allowlisted package5 host observation and original-build observation5 give:

| Item | Bytes |
| --- | ---: |
| Current free store space | 121636823040 |
| Other retained writable growth | 77289816064 |
| Working5 tank remaining growth | 8200409088 |
| Unchanged base reserve | 17179869184 |
| Total protected obligations P | 102670094336 |
| Free above P | 18966728704 (17.664GiB) |
| Proposed new physical image allowance | 4294967296 (4GiB) |
| Proposed additional publication-copy allowance | 4294967296 (4GiB) |
| Prior measured staging plus current missing closure NAR | 3412352328 |
| Separately assessed uncertainty/headroom | 5368709120 (5GiB) |
| Total assessed additional peak N | 17370996040 (16.178GiB) |
| Unassigned remainder above P after N | 1595732664 (1.486GiB) |

Staging3127554904 and missing closure284797424 are included once in that row.
The old image measured3615100928 allocated bytes (3.367GiB), despite its8GiB
logical length. The old successful construction's maximum net host free-space
reduction was12370911232 (11.521GiB). This corroborates an assessment below the
former sum of full logical extents; it is neither builder-only attribution nor
an upper bound on the next run. Inputs/profile/V939 are unchanged, but new
source/artifact context and concurrent host activity can change the
actual footprint. No construction success or stable future peak is inferred.

The source ordering remains `Software.build` -> exact guest import -> owned
shutdown -> direct boot (`kb_source.rb:129-146`, `kb_runtime.rb:187-264`). The
existing writable root is fully allocated and reused; tank growth is protected
above. Import must fit the guest's own byte/inode reserve independently. No new
root/tank copy is charged or created. Old immutable images remain allocated and
already reduce current free space; their holes have no future writable-growth
obligation. Prospective candidate physical allocation remains an estimate until
publication. Existing raw `make-disk-image.nix` publication uses mv, as traced
above; no same-device/rename/reflink/sparse-copy guarantee is assumed here.

In particular, the4GiB publication allowance is **not** a proven copy maximum.
A cross-mount dense8GiB copy can exceed it by4GiB. That overrun would consume4GiB
of the5GiB uncertainty allowance, leaving only1GiB for other overruns before
the unassigned remainder. Likewise, a larger candidate image consumes the same
aggregate allowance. Thus this worksheet cannot promise an independent5GiB of
scratch space after every possible copy. If root requires that guarantee, the
supplied capacity is insufficient and update must remain held. The finite
recommendation accepts a possible monitored refusal instead; it does not rename
known bytes as unknown or declare scratch bounded. No increase of this budget
is automatic if the estimate proves wrong.

Bind a fresh operation receipt to exact source/packages/configuration and actual
store/daemon-scratch/state filesystems. N is a conservative sum of the proposed
simultaneous construction components, not another24GiB fresh-instance envelope.
Post-publication/import uses the retained writable disks and actual candidate
outputs; compare phase peaks rather than summing sequential phases. Retain
possible staging remnants until evidence excludes them. If filesystems differ,
assess each independently; unused capacity elsewhere supplies no admission.

For the supplied snapshot, propose the existing watcher's early cancellation
floor **104265827000B free = P +1595732664B**, corresponding to consumption of N.
Refresh the arithmetic before launch and keep the chosen floor fixed or more
conservative during the operation; do not chase falling space by lowering it.
Also cancel/hold on observation loss or an unrelated resource/source/ownership
failure. Use only root's existing cancellation contract for the owned operation,
with its actual handling of outstanding Nix work established before launch.
Monitoring and cancellation are not instantaneous and cannot guarantee that the
1.486GiB runway prevents all overshoot. They grant no signals to guests/foreign
processes, store GC, reset or automatic retry. If that existing cancellation
contract cannot preserve the required operation boundary, this estimate is not
admissible. On cancellation retain the update journal and exact candidate;
capture remains held, with any later recovery separately selected.

Supplied RAM30909935616B/shm20534583296B exceeds the preceding proposed additional
6/5GiB builder-overlap admission, but fresh live readiness/capacity still belongs
to root. Keep original failed/pass receipts and genuine G->M attribution. G14's
already completed reset supplies no new credit; G13/G4/G6/isolation3/preview are
unchanged. Current/absent markers and roster17 retained settings matched; required
guidance was read/reused unchanged. Only safe evidence/public source and this
design were accessed; no private inputs, probes, operations or application edits.

### WORKING5 FINAL CAPACITY RECONCILIATION: hold on the fresh byte accounting (2026-10-12)

Final recommendation: **HOLD this update on the supplied fresh observation.**
The fixed3GiB uncertainty proposal does not fit even before considering whether
its operational risk is acceptable. Do not reduce it again to chase admission.
This supersedes the preceding worksheet's conditional recommendation for the
earlier, larger free-space snapshot.

`finish-working-delivery-update-admission5-refusal1.json` records free space
118001684480B and required space120324396856B, with admission false and no
context/service/update created. The additional permanent missing closure
284797424B is distinct from the staging copy and must remain charged; the
previous worksheet did not include this second physical allocation.

| Fixed proposed component | Bytes |
| --- | ---: |
| Physical candidate image assessment,4GiB | 4294967296 |
| Additional publication copy assessment,4GiB | 4294967296 |
| Measured staging3127554904 + missing staging284797424 | 3412352328 |
| Separate permanent missing closure | 284797424 |
| Final assessed uncertainty,3GiB | 3221225472 |
| Total additional assessment | 15508309816 (14.443GiB) |

Changing only uncertainty from5GiB to3GiB reduces the refused requirement by
2147483648B, giving **118176913208B required**, still **175228728B (167.11MiB)
above actual free space**. Equivalently, the refused worksheet implies protected
obligations102668603392B after subtracting its5GiB assessment. Space above those
obligations is15333081088B:15.33 decimal GB, but **14.280GiB**, not15.33GiB.
Thus the proposed0.9GiB unassigned buffer is not present in these byte figures.
This reconciliation uses the recorded requirement rather than inventing a new
tank-growth measurement; all retained growth and the16GiB reserve stay protected.

The previous successful net host peak12370911232B remains useful evidence, not
a future bound or builder-only measurement. The proposed total is about2.922GiB
larger, but that comparison cannot create the missing free space. The source's
possible dense8GiB publication copy, unknown scratch and unrelated host activity
also remain risks; no rename/sparse-copy guarantee has been established.

Root's revised cancellation boundary targets only its positively identified
direct Nix client and then the owned public CLI. It supplies no guest/foreign
signal authority and no guarantee that daemon work immediately stops. Therefore
it cannot replace prelaunch admission or justify consuming protected obligations.
Any cancellation would retain candidate/journal evidence and hold capture pending
separate diagnosis. No new cancellation mechanism is proposed here.

No operation was launched by this assessment. Preserve the refusal and current
source/guest evidence. Root owns disposition and any genuinely changed fresh
capacity evidence; there is no further allowance reduction, cleanup credit,
automatic retry or new pair recommendation. Only this design appendix changed.

### WORKING5 PREPARING CONTINUATION: bounded private guest-store preparation (2026-10-12)

Recommendation: the supplied native facts support a separately selected,
operator-prepared continuation of the **same public update candidate**, subject
to fresh guards below. This is not an application change or operation approval.
The earlier capacity refusal remains historical; root's later admitted operation
built its image without cancellation and then failed at guest prerequisites.

`finish-working-delivery-public-update5-failure-disposition.json` records native1,
operation0f96e20e-061f-44f3-ba1e-6d83592d4c8f, stage`preparing`, candidate
c7595a57-6b7f-4e90-96f8-8179b5530530 and Kb5e39e6. Its artifact digest is
bffe7687747efdd349bd881c922f4ded08f9e040882d621e0426d8fe7a1e7e97. The candidate
image has8GiB logical length and3615162368B allocated; no completed import proof
exists. The old instanceaa7bc9ad-c6d3-4541-b12c-938d03c484c2/run
e8f5d11b-28b8-4cca-be80-572d6d595c5e remains the predecessor. Neither successful
replacement nor capture is inferred.

The guarded prerequisite diagnosis5 establishes installed Nix tools, writable
database, nonwritable store and plain path-info failure, with the same query
succeeding when nix-command is explicit. Mount observation5 establishes `/`
as rw ext4 `/dev/sda`, `/nix/store` as ro,nosuid,nodev,relatime ext4
`/dev/sda[/nix/store]` with fsroot`/nix/store`, and the database on the rw root.
These are snapshots, not current authorization. Exact OS6bdf
`tests/configs/nixos/test-vm.nix:4-7` disables host-store mounting/shared VM
directories, and `tests/make-test.nix:237-267` creates the ext4 raw guest image.
The actual guarded mount facts, rather than that declaration alone, exclude a
host virtiofs/shared store here.

Root may select one ordinary authenticated public SSH preparation after proving
the exact predecessor launch/runner, strict retained keys, old guest identity and
current-system closure again. Public SSH (`cluster/launcher.rb:76-82`) holds the
gate but does not itself attest guest source: the remote script must check those
identity/closure expectations before mutations. Phase`updating` must not be
changed to ready merely to obtain access. Recheck the same root/store mount
identities, ext4 backing, fsroot, options and private owned root-disk binding;
unexpected mounts, shared storage, symlinks or changed source refuse.

For that exact private bind only, `mount -o remount,bind,rw,nosuid,nodev,relatime
/nix/store` is the proposed guest operation. It must retain mount identity and
nosuid/nodev protections, leave `/` and every host/shared mount unchanged, and
be followed by matching mount facts and writable-store/database checks. No
unmount, recursive remount, chmod of store contents or immutable path edit is
included. Record original options privately for restoration.

Enable only `extra-experimental-features = nix-command` in the dedicated root
user's ordinary mutable Nix configuration. The expected path is
`/root/.config/nix/nix.conf`, only after confirming the SSH user's HOME and Nix
configuration resolution select it; unexpected NIX_USER_CONF_FILES/NIX_CONFIG
or XDG overrides refuse rather than being silently redirected. The retained
Nix2.31.5 manual's configuration-file section documents user configuration and
the additive extra- list syntax; a fresh plain path-info query in the same public
SSH environment must prove the selected guest consumes the setting. Preserve
any prior bytes, absence, mode and ownership privately; reject symlink/unsafe
parents or files, retain unrelated settings, and create only owned private
directories/files when absent. Never change `/etc/nix/nix.conf`, profiles,
closures, guest source metadata, credentials or trust. Do not print the prior
configuration. No daemon restart, extra feature, substituter or trust change is
part of this preparation.

Then root may select **one** same-package public `update` with the identical
config/topology/network and normal900-second controller budget. Exact Kb5
`kb_runtime.rb:198-235` matches the recorded source/config, reads the existing
artifact at stage preparing and reruns closure preparation without calling
Software.build when that artifact exists. Thus no new image/builder/pair is
needed. Missing/changed candidate evidence is a refusal, not permission to
rebuild or substitute. `kb_closure.rb:45-90,92-96,112-137` still requires live
old-source proof, actual guest missing-NAR/inode capacity plus256MiB/10000
reserves, authenticated import, recursive content/reference verification and
the candidate GC root before public shutdown/direct boot. Host import growth
and current RAM/shm/reserves need fresh assessment; already allocated candidate
outputs are not charged a second time. No space or successful import is assumed.

After native success, require actual new run/artifact/Kb5 identities, system
closures, unchanged six credentials/accounts/trust/disks/sentinels and normal
resource/API/member/lease proof before separately selected canonical captures.
Restore the exact prior root-user config (or its prior absence) through guarded
public SSH and confirm the store has its original ro/nosuid/nodev state. A new
boot may already restore the immutable mount policy; observe rather than assume
it. If still rw, restore only the same proven private bind. Recheck identity and
plain read/capture prerequisites after restoration. Record operator preparation
as such; it does not become a declaration of either immutable guest source.

A preparation or continuation failure ends this selected unit and holds capture.
Preserve its native failure, exact candidate journal and any imported closures;
do not undo imports/GC roots, activate an old profile, replay the Campaign or
reset. Restore only the recorded operator config/mount changes when the current
authenticated guest/run and absence of ongoing import permit it; uncertain
identity or active work requires a hold, not blind rollback or cleanup. Later
journal recovery remains separately selected. No application edit, checks,
guest operation or new acceptance claim was made by this design assessment.

### WORKING5 NULL PRIMARY: narrow fixture correction and finite capture disposition (2026-10-12)

PROPOSAL for root source/operation selection. Native B5 update and its13-command
post-proof remain successful evidence; CS remains failed without a PNG. The
allowlisted `finish-working-delivery-location-flags5.json` binds instanceaa7bc9ad,
run7325536f and artifactc7595a57 to B5, with dedicated network4 enabledtrue and
association7 returning primarynull/autopickfalse/userpickfalse. The exact B5
`fixtures/prepare.cjs:599` rejects that legitimate output before IP registration
or disabling. This is a caller contract error, not evidence of a pickable pool.

V939's owning contract is `api/models/location_network.rb:8-15`: before save,
literal false becomes nil so its unique primary index permits multiple
non-primary associations. `api/lib/vpsadmin/api/resources/location_network.rb`
exports primary through its bool parameter and returns the saved record for
Create and Index; the actual native null confirms serialization. Create's
operation only sets primary_location when the saved association is primary.
Neither changing the API nor repeatedly requesting false can make B5's guard
work. A data-only workaround would contradict this supported model contract.

Only application owners proposed: K `fixtures/prepare.cjs` and existing
`tools/test-ip-inventory.cjs`. Accept primary only when `primary === false ||
primary === null`; retain autopick/userpick exactlyfalse. Do not use truthiness,
loose equality, nullish defaults or normalize the response. Missing primary,
true, numbers and strings refuse. Continue requesting literal primaryfalse in
the POST and leave every other resource/permission/identity check unchanged.

The existing HTTP fixture must represent the actual callback: new POST with
primaryfalse returns primarynull, and retained non-primary records default to
null. Cite the owning V model in the test rather than inventing a coercion rule.
Exercise both new and retained null, explicit false compatibility, and a disabled
valid-null rerun with no writes. Table-test missing/true/0/1/string primary and
missing/null/true/numeric/string autopick or userpick: refuse before IP POST or
network disable. For new association responses, the association POST itself may
already have succeeded; do not assert that nothing was created. Preserve the
full API7 wire paths, namespaced filter/pagination assertions and literal false
request assertion. Extend the same existing fixture tests, without a new
database/browser framework, to retain representative wrong charge/prefix/address
and enabled-flag refusals before disable; no further production fix is supported
by this source inspection.

Remaining fixture-output trace, separate from unexecuted future capture:

| Fixture expectation | Owning contract and conclusion |
| --- | --- |
| VPS1CPU/1024MiB/zero swap/4096MiB, member/node/location IDs | VPS resource params expose the four cluster resources (diskspace is total_diskspace); resourceId handles association object or scalar ID. Existing real creation and strict tuple checks stand. |
| Dedicated pool role/purpose/address/prefix/managed/enabled | Network common params expose enums as strings and integer prefixes; model requires managed/enabled actual booleans. Keep exact checks and enabled creation; null accommodation applies only to association primary. |
| Detached203.0.113.10/32, size/ownership/charge | IpAddress.Create parses the supplied CIDR and requires the user's location to belong to the network. IpAddress.register derives charged_environment from that location, charges one IPv4 unit transactionally and creates the allocation without an interface. Output addr omits the CIDR suffix, prefix is integer32 and charged_environment is an association. |
| Correct charge/quota environment | K test.nix selects Production/Praha; production-shape declares userIpOwnershiptrue. Its standard package has one IPv4 and captureUserResourceHeadroom adds one. seed-production-shape.rb adds these values, yielding two units for the assigned VPS and detached address; it does not bypass quota. |
| Existing assigned enabled IPv4 | IpAddress.Index's namespaced vps/version filters join the VPS interface/network; Ip::Allocate records the VPS owner in the ownership-enabled Production environment. Primary network enabledtrue remains mandatory. |
| Disable and bilingual rerun | Network.Update returns the saved boolean false without reassigning existing service. The fixture rereads through the administrator, validates owner/null-interface/charge, and performs no duplicate charge or reenablement on a complete disabled rerun. |

Relevant server owners inspected are the location_network operations/resource,
network resource/model, ip_address resource/model(register), Ip::Allocate and
VPS/node/location resource outputs. K owners include production-shape.json,
seed-production-shape.rb and test.nix seeding. This identifies no additional
incompatible output assumption; actual remaining IP creation/quota/disable and
both language captures are still unproved, not certified by mocks or source.

After one logical fix is committed/published, use the existing hosted Check
(`nix develop --command bin/check --allow-missing`, which invokes
`node tools/test-ip-inventory.cjs`) and affected committed review under the
standing no-local-CI rule. Root owns the mechanical exact E selection and normal
composition evidence; no workflow, dependency, V/OS, engine or SSH batching
change belongs to this remedy. Reuse unaffected accepted evidence.

There is **no supported image-free source switch**: Software.prepare/build and
Engine.update bind a new artifact to the changed fixture/source digest and build
its services image. Resume requires the matching old source; a changed capture
package cannot claim B5 generated it. Ordinary update remains supported, but
retains candidate construction/import and full path verification costs even if
most paths already exist. The observed44-minute import is not addressed here.

Recommended finite finish disposition is one sequential fresh replacement,
only if root separately selects its destructive boundary: seal the B5 successes,
failed Campaign/captures and private evidence/continuity backups; ordinary public
stop must prove complete owned exit; only then public reset of this disposable
instance, followed by freshly admitted public start at the corrected immutable
source. Preserve source/metadata receipts and failure evidence outside reset.
Keep4+4GiB guests,4GiB sequential builder and8GiB image/root/tank; never overlap
two pairs. Credit only actual verified released allocation, not an assumed reset
or immutable-store GC. Existing images still occupy host space. A refused stop,
reset or fresh capacity check holds the route; this proposal authorizes none.

Use the new source's genuine accepted guest identities/closures, TLS/API/member,
lease and resource proof before direct same-source CS/EN captures and strict
validation/export. Existing lifecycle proofs remain attributed to their original
generators; no new completed Campaign receipt is fabricated. Preserve new G
through later media commit M, visual review and exact-media hosted strict Check.
One native failure ends the selected unit without automatic retry/reset/upscale.
Root may retain B5 instead if replacement is not selected; then capture remains
blocked. Only this design was appended; no application or runtime work occurred.

### WORKING5 REPLACEMENT CHOICE: current named-disk accounting (2026-10-12)

Recommendation: select **one sequential replacement**, contingent on a sealed
private evidence backup, ordinary proved stop, explicitly selected public reset
and fresh admission. Do not select another same-instance update at these disk
figures: it retains the old writable disks and repeats the supported expensive
closure-import proof. There is no source-attested image-free switch. This is an
operational proposal, not permission to stop/reset or a claim of available fit.

Current/absent markers and roster17 matched saved architect0 settings. The
restart observation5 binds B5/run7325536f/artifactc7595a57 and records both QEMUs;
it is not a new guest-health or stop proof. Read-only lstat of only the named
disks from update-admission5 matched every retained device/inode, UID1000 and
ordinary0600 file. No contents, credentials, process probes or guest operations
were read/run. The changed figures are small additional allocated tank extents:

| Current named writable growth | Bytes |
| --- | ---: |
| G4 tank | 17179869184 |
| G6 tank | 17179869184 |
| isolation3A tank | 17177071616 |
| isolation3B tank | 17165471744 |
| G13 tank | 8586313728 |
| Other retained growth total | 77288595456 |
| Working5 tank remaining growth | 8195731456 |
| Working5 root allocated / remaining growth | 8590065664 / 0 |
| Working5 tank allocated | 394203136 |
| Working5 allocated total | 8984268800 |

All other named writable roots are fully allocated. Old immutable image holes
are not future writable obligations; their existing allocated bytes already
reduce free space. No old state or image is removed by this proposal except the
separately selected disposable working5 tree through its own public reset.

Against root's supplied free113633284096B, current retained growth plus the
unchanged16GiB reserve totals102664196096B, leaving10969088000B (10.216GiB) for an
update. That is below the previous fixed14.443GiB construction assessment. The
old observed net peak11.521GiB is also greater; neither observation is a future
bound and neither supports lowering headroom to make this update fit.

If, and only if, public reset actually releases working5's8984268800 allocated
bytes and removes its8195731456 future-growth obligation, conditional free above
the remaining other-growth+16GiB reserve becomes28149088256B (26.216GiB), before
backup bytes and unrelated host changes. This counts freed allocation and removed
obligation separately, once each. It does not reclaim store outputs, presume GC,
credit G14 again or certify that unlink has released blocks while descriptors
remain. Root must measure actual free space after complete exit/reset/backup.

Use separate phase peaks for the fresh same4+4GiB/8GiB-disk profile:

1. Construction has no runtime guests or writable replacement disks yet.
   Software.prepare/build finishes before start_locked spawns the runner. Retain
   the prior4GiB image +4GiB possible publication copy + measured staging and
   separately missing permanent closure + fixed3GiB assessed uncertainty as a
   reference, currently14.443GiB using the old missing-path numbers. These missing
   paths may now be cached, but new source/package facts must establish that;
   take no assumed reduction. The actual prior image3615162368B supports the
   physical4GiB estimate, not an8GiB logical-length bound. Scratch remains unknown.
2. Runtime provisioning retains one new immutable image and creates one fully
   copied8GiB root plus an8GiB tank. Charge the whole new16GiB writable extent
   once, including future sparse growth. With a4GiB physical image assessment,
   the same3GiB uncertainty and prior284797424B permanent-missing reference, this
   phase is24980859376B (23.265GiB), leaving about2.951GiB before backup/new
   closure differences. Do not add construction's transient publication copy
   and staging again once actually gone. If remnants overlap provisioning,
   their measured/assessed bytes belong in this phase; no assumed cleanup credit.
3. Capture reuses that pair/image/root/tank. Deduct actual writable allocations
   and retain their remaining growth, plus measured evidence/browser/log output.
   Do not recharge a24GiB fresh extent or rebuild for the second language.

For comparison, the full logical24GiB image/root/tank extent alone would leave
only2.216GiB, before new permanent closures/backup/headroom. Thus the route is
plausible under the established monitored physical-image assessment, not a
guaranteed worst-case fit. Dense/larger image or retained staging, other host
consumption and builder scratch can still refuse it. Keep the3GiB assessment
fixed; do not progressively reduce reserves/headroom. Root's existing watcher,
phase accounting and owned cancellation retain their limits, especially no
guarantee of immediate Nix-daemon cessation. No new allocator/monitor is proposed.

The minimum backup is evidence, not a bootable disk clone: preserve the failed
Campaign and successful runtime/B5 update/post-proof receipts unchanged; retain
all owned non-disk reset-tree records, source/artifact/config/launch/disk receipts,
private six credentials/accounts/trust and native diagnostics/fixture outputs
outside the reset target, with checksums, original path/identity metadata and
private permissions. Preserve result-link targets as provenance without copying
store trees. Root measures backup size and verifies the backup before reset.
Secrets remain private and no backup receipt confers adoption authority. This
deliberately discards disposable guest database/VPS disk contents; B5 cannot be
resumed from that evidence backup. A full same-filesystem disk copy would consume
roughly the release being relied on and needs a different capacity decision;
do not quietly take that backup and still claim the release credit.

After final source/hosted/affected-review gates, the selected public stop must
prove complete runner/descendant exit; a refusal holds reset and replacement.
Then public reset, fresh measured capacity and one fresh public start create
new source/artifact/run/credentials without transplanting any old identity or
Campaign receipt. New package/kernel/missing-closure facts, measured backup,
post-reset free/store/scratch placement and RAM/shm are the remaining admission
facts. Builder4GiB is sequential with the8GiB runtime pair; no simultaneous pair.
Require fresh guest/source/TLS/API/member/lease/resource proof before direct
same-generator CS/EN capture, strict inventory/export and visual acceptance.
Existing lifecycle/import proofs keep their B5/G6cfd attribution and need no new
historical campaign. One native failure holds the selected unit; no automatic
retry/upscale/reset or source substitution. Root owns the concrete operation
selection. Only this design appendix changed.

### FINAL TARGET RECONCILIATION: preserve G while preparing current integration heads (2026-10-12)

READY as a source-only proposal for root, not branch, deployment or operation
acceptance. Current slug, both absent environment markers and live roster17
matched the retained architect0 Astra/xhigh/workspace_write binding. This
checkpoint supersedes no failed receipt or WORKING5/6 operation. Only design.md
is appended; the frozen M/E review and watcher remain their owners' work.

The allowlisted public-start6/post-start6, direct-capture7/proof, visual-media7
and working6-stop7 receipts establish genuine Gd0b4f407 source/closures,
TLS/API/member/lease, packaged CS/EN/default-CWD captures, typed fixture,
strict full inventory/export and final ordinary complete stop. Runner and15
children are gone; disks remain. They do not establish a completed G Campaign,
an M guest, current production deployment or freshness of every retained image.
The original failed CS attempt and its unknown cause remain recorded.

The exact Gd0b4f40708cc8b59aab7c91ae05fba695abc233c is M706b9d8's direct parent.
Their diff contains only captures.json and the two networking/ip-address-list
PNGs. Keep M706b9d8c18edde528af4fb5279786491aedd47fa and its K application,
fixture, runtime, lock and contract bytes unchanged. K's own flake:5-7 selects
V939159f27b5d627930281d5fac0c0aa9ba53bfc7 and OS6bdf458. This remains the
canonical consumed graph, even when a patch-equivalent V feature moves onto
the current production target. Preserve V939 under a dedicated exact published
retained ref BEFORE rewriting its existing feature ref: the inspected local
and origin-tracking refs currently expose it only through that feature branch.
Retain G through the unchanged published M ancestry and the frozen receipts.
Do not substitute new V/M metadata for G or regenerate images just for unrelated
default advances. K runtime-contract's Source proof/Source and artifacts and
webui-change-workflow sections2-4 require truthful exact selection, not equality
with every other consumer's newest target.

The smallest target preparation, after root releases the frozen review refs:

| Owner | Necessary action and source evidence |
| --- | --- |
| V | Rebase the same four logical feature commits from base8a50010 onto master7d911899. The two upstream commits change packaged HaveAPI dependencies and services-up documentation tests; their changed-path set has NO intersection with the feature. Preserve the migration and feature bytes, prove range-diff equivalence and publish the resulting V head. This inspection predicts a clean rebase; none was executed. |
| D | Rebase the existing three-commit series from17222c onto master1a27453. Upstream leaves libexec/workspace-host, its streaming tests, operation_state_test.go, flake inputs and host-path declarations unchanged. Shared docs/workspace-portal.md hunks are separate. In operation_state.go, upstream adds archived-mode validation at273, while the feature retains the transition guard/original deadline and adds the post-proof deadline check around341. Upstream server_test.go changes other tests, not the two completed-delete retry cases. Preserve all newer archive/portal/artifact behavior and prove patch equivalence; a real semantic conflict goes to the implementer rather than being discarded. |
| C | Rebuild the TWO existing channel-pin commits on master1697613 with normal confctl generation, after final V is published: channel/role vpsadmin/vpsadmin selects that V; vpsadmin-webui/vpsadmin-webui remains exact W30cce68142. flake.nix:103-111 owns these mappings; WebUI's vpsadmin follows vpsadminServices. Preserve current monitoring, staging OS, web and devWorkspace1a27453 changes. Do not resolve a lock conflict by restoring an old whole lock or hand-editing nodes. Keep generated changelogs and one final commit per existing pin stream. |
| E | Once rebased D is published, change only its exact dev-workspace selector and generated lock, folding that into the existing single paired-input commit. Keep K=M706b9d8, its complete independent graph, ordinary devcluster sibling graphs/follows, and the provider commit's content/message unchanged. flake.nix:6-7 selects D/K independently; there is no K follows to E's ordinary V/OS. Retain two logical E commits, not another superseded selector tail. |

Wnetworkce856841 is already an exact ancestor of current main7152729 through
external integration. W30cce681424b866f6a51cbc0a1e4daa226ed33fc07 has that exact
main as its parent and remains unmerged PR39. Neither needs source work or a
rebase at these recorded targets. Preserve both histories and W30's existing
review/native evidence; root's eventual fresh fetch can detect later movement.

HaveAPI compatibility is concrete source evidence. Comparing tags
v0.29.8=22fae15809b37e66ffea53a1162544e6321d09ab and
v0.29.9=784e113c216b16586c482e710ee4a0e0a04e6f8e shows documentation packaging,
release/version updates and an ENOENT-to404 guard only for /doc/json-schema
(servers/ruby/lib/haveapi/server.rb:533). Action, parameter, metadata, pagination
and model-adapter logic are unchanged. action.rb:688-732 still separates the
singular input namespace from _meta; actions/paginable.rb still caps namespaced
limit at1000; actions/default.rb:14-28 keeps _meta[count]/total_count. Protocol
version stays2.0. V api/lib/vpsadmin/api.rb:3 still selects API7.0, and the
location_network model's false-to-nil callback remains unchanged. Thus the
actual K /v7.0 routes, namespaced filters/limit, nullable primary and strict
autopick/userpick/enabled output assumptions have no identified new conflict.
This is not a running .29.9 API or packaging certificate; the new V packages
must retain their own hosted evidence. No source finding requires K to repin.

Keep deployment and rollback boundaries explicit. V's existing
docs/upgrade-network-availability.md remains authoritative: migration
20261006120000 directly follows20260914190000, adds NOT NULL/defaulttrue, and
has already been consumed by disposable/preview systems. Do not rewrite it or
invent production/release consumption. Apply schema before enforcing writers;
replace all old allocation writers before disabling pools, then deploy capable
interfaces. Older writers ignore the flag; schema rollback loses policy.
No node-protocol or coordinated OS update is introduced by these rebases.
D's rebase must preserve upstream lifecycle formats; it supplies no promise of
rolling an installed package back across newly created upstream archive state.

E source selection does not activate the runtime. The current workspace's
flake.nix:8 overrides D to1a27453, matching C's current devWorkspace selection.
Leave that pair unchanged in this integration-preflight scope. A later decision
to install new E/D must align the workspace's direct nested D selector and C's
dev-workspace/devWorkspace channel, then run the existing deployment-contract
check. Merely updating E's lock cannot override the consuming workspace's D.
This is a deployment prerequisite, not a reason to expand this source plan or
change K, its guest, or the generated media.

Verification is finite and respects NO LOCAL CI. Root's quick source work is a
fresh target inventory, preserved V/G reachability, V/D range-diffs and complete
histories, unchanged migration blobs, C semantic channel/lock comparison and E
provider/K/sibling graph comparison. These checks distinguish patch equivalence
from exact consumed source. For changed heads use the existing hosted V API,
migration/PHP and selected CI evidence, including services-up's packaged shared
documentation check introduced by7d911899; D's Check fast package/streaming/Go
contracts; and E's ordinary composition/provider/host-path checks at the final
D selector. Do not add host-migration or guest-capture campaigns for this
patch-equivalent target move. C has only daily-update workflow, so do not call
its pins configuration-tested without an actually selected owning check; any
later deployment retains its normal build/admission gate.

Reuse the unchanged M source/runtime/strict-media watcher and real G receipts;
their final acceptance remains root/reviewer-owned, not inferred here. After
the changed-head quick gates, give the retained reviewer only the affected
rebase/composition delta plus final whole-branch/consolidation/migration
inventory. Earlier frozen review is not certification of newly rebased heads.
No compatibility blocker was found in the inspected upstream delta. Remaining
gates are actual rebase/lock results, published retained V proof, final hosted
and affected-review acceptance, and explicit repository/target integration
approval. V/D/C/E/K defaults and W30 integration remain unapproved; W's already
integrated feature is historical fact. No deployment, KB publication, session
closure, cleanup or new runtime operation follows from this checkpoint.

### TARGET11: D/C upstream advance with frozen V/K/media (2026-10-13)

READY as a bounded source proposal. Fresh current/absent markers and roster17
match retained architect0 Astra/xhigh/workspace_write. Reused unchanged routed
guidance, reread current session/lifecycle and D/C/E instructions and provider
documentation. Root's finish-target11-remote-tips.json supersedes target7
freshness: D master is7c07b540a5e45cac4b39351f713cf3528e4df614; C master is
bfb1d89c95308024a9269974c207bf7cefe1fb1c. No rebase or operation was performed.

Preserve published D16d949b39e162870cc21a6f23d2d138b2e642887,
E78463762fcf79b94ae026ea1acc3a36354938cd1 and
Cd275b5f3455fd25633a053e49989fc1d33f1c620 as historical provenance before
replacing their feature refs. V4a21dd25b23de9832166def98526f410416b651e,
W30cce681424b866f6a51cbc0a1e4daa226ed33fc07, K/M706b9d8 and actual Gd0b4f407
remain unchanged. Root reports corrected V/API/RuboCop/i18n and final history
review complete; this target advance does not invalidate or rerun that evidence,
the media, or their immutable failed predecessors.

D's five upstream commits add provider routing, popup cancellation behavior and
test scheduling. Comparing1a27453..16d949b against1a27453..7c07b54 finds exactly
TWO shared feature paths: libexec/workspace-host and docs/workspace-portal.md.
Upstream does not change operation_state.go, operation_state_test.go,
server_test.go or commands_and_locks_test.rb. The portal server.go advance is
a call-site dependency of the deadline patch, not an overlapping feature file.

Rebase all THREE D owners unchanged where possible:0910a387 streaming,
50f3cf4e post-proof deadline/CAS and16d949b3 completed-delete retry fixture.
In workspace-host, keep upstream require/include CodexProviderHost beside the
feature's input:$stdin initializer/@input, preserve new provider dispatch and
admission/package checks, and retain the capture-lease-only streaming branch
inside dispatch_cluster's existing shared generation lock. The new module has
no initializer or streaming-helper name collision. Its exclusive transition
lock therefore remains excluded while the relay holds its generation guard
through child reap. Do not conflate Codex routing providers with cluster
providers or alter their cancellation policies. Docs add an upstream provider
guide link at the beginning and feature relay text in Extension catalog;
preserve both. Adjacent initializer context may require textual reconciliation;
root owns rebase/range-diff and implementer owns any necessary application edit.

Keep requireCurrentHostProfile's NEW requireProviderAdmission call
(7c07 server.go:859) before the feature reconciliation helper. Preserve the
original deadline across receipt/journal proof and CAS retries, and the check
after proof before acceptance. Do not bypass provider reservation to recover
old test behavior. The deletion tests still model actual journal removal and
retained receipt/attempt/force identity. No semantic conflict is established by
inspection; clean application and all-three-owner equivalence remain unproved.

Upstream adds provider state schema1/transition policy1 to
portal/internal/session/runtime-contract.json. workspace-codex-providers.rb:
164-190 rejects applying/recovery-required admission and packages unable to
load retained provider state; waiting requests retain upstream rules. Its
docs/codex-providers.md owns native compensation and forward-only package
recovery. Preserve the new helpers, package installation, contract fields,
host module/worker and codex-web5f15b929 source/Go pairing. E's
nix/organization-tools.nix:74 reads authority policy1 and installs the selected
contract, so the added fields do not establish an E incompatibility. This is
composition evidence, not certification of upstream provider implementation
or permission to switch providers. Old D16d/E784 cannot be promised as installed
rollback targets after new provider state; recover through a compatible newer
package under the owning contract, never by deleting state.

C must regenerate only its TWO existing confctl streams on bfb1d89c:
`vpsadmin/vpsadmin` selects unchanged V4a21dd25 and
`vpsadmin-webui/vpsadmin-webui` selects unchanged W30cce68142. Keep generated
history and normal hooks; preserve every other upstream selection and file,
including devWorkspace7c07, aitherdev provider configuration, operations guide
and mkdocs entry. Do not hand-resolve the lock to an old whole graph. After D
publication, E folds the new D selector into its existing ONE paired-input
commit, retaining its separate optional-provider commit's normalized bytes and
message. Its expanded D graph must match new D, including codex-web5f15b929;
its expanded K706 graph and all non-D siblings/follows must remain equivalent.
An unchanged old D graph is no longer the correct acceptance criterion.

Actual consuming-workspace flake.nix:7-8 and flake.lock now select extension
7157c8098dcf60127aa4df823fab82b4185ad22a with direct nested D
7c07b540a5e45cac4b39351f713cf3528e4df614. Cbfb's devWorkspace selects the same D
and NAR sha256-Mtx3cvEFS+f6rXBJjNF2xWI1KDlU1STG53iZIVx2JtY=.
These source selectors replace the earlier1a27453 observation; they prove no
installation, health or guest state. E's new D pin alone cannot override the
workspace selector. Leave these consuming selections intact now. Later feature
activation needs matching workspace nested-D/C devWorkspace selections and
the existing deployment-contract gate, as C's codex-providers-aitherdev guide
requires. No deployment, schema change or new upgrade policy is added here.

Acceptance: root preserves prior refs/evidence, obtains three-owner D range-diff
equivalence or records each explicit conflict deviation, compares C's two
semantic channel deltas and E's single input stream/expanded graphs, and keeps
normal hooks without local CI. Run only affected new-head hosted D/E package
checks under existing ownership. D Check fast includes package/Go/Ruby/browser
and protocol contracts; its host job (host-module-idempotency and
session-recovery-boot) is skipped on feature pushes unless separately selected.
Record that skip; it is not installed provider or rollback proof. E Check owns
flake composition/provider contracts plus devcluster-check; retain any native
skip/failure as such. No new provider-switch, migration-VM or guest/media
campaign is selected. C lock generation has no configuration-build claim.
Give final changed heads, range-diffs and complete history to the retained
independent reviewer for affected delta/consolidation/compatibility acceptance;
the previous review cannot certify new D/E composition. Other evidence stays
at its genuine source. Final named-default approval, future target refresh,
Git execution and durable state remain root-owned. Only this design was edited.

### SCOPE12: remove disabled-network media refresh; retain portable runtime (2026-10-13)

READY for root acceptance as a bounded proposal. Current slug, absent environment
markers and fresh same-session roster17 match architect0 Astra/xhigh/design/
workspace_write. Applicable workspace routes, documentation/handoff skills and
K/E instructions were read. The user's “ok, proceed” accepts the reduced scope;
it is not named-default integration, package activation or KB publication approval.

Root now reports the refreshed media owner M706b9d8c18edde528af4fb5279786491aedd47fa
removed locally from both K worktrees, leaving the original two commit objects
and clean Gd0b4f407 heads. M706/E4c869 provenance refs were published first;
active refs are not yet published and E still selects M pending final K.
Dropping M alone is incoherent: Gd0b4f407's fixtures/prepare.cjs:557-624 still
creates a disabled dedicated pool, and scenarios/networking.cjs:41-64 requires
its gray row/title/focus before ordinary IP-list capture. Keep the small real
ip-inventory fixture but make its dedicated pool enabled. Keep disabled-network
product regression coverage in V unchanged; do not add a capture mode, optional
edge-case fixture, new campaign or replacement test framework.

The narrow implementation owners are these SIX K files:

- fixtures/prepare.cjs: rename the pool label to `Documentation inventory` and
  the returned disabledIpId/disabledNetworkId/disabledAddress fields to
  inventoryIpId/inventoryNetworkId/inventoryAddress. Keep inventoryVpsId. After
  selecting or creating the exact pool, require enabled === true before any
  location-association/address write. Remove the final enabled:false PUT and
  disabled-state success condition. Never disable or re-enable a retained pool.
  Keep the real CPU1/memory1024/swap0/diskspace4096 VPS, primary pools, detached
  owned 203.0.113.10/32 and genuinely assigned IPv4, exact API7 wire paths and
  namespaced filters, nullable-primary contract, charge/assignment/resource/
  ownership checks and all source, account, member-browser and live-lease guards.
- scenarios/networking.cjs: use the neutral returned address; require its actual
  owned detached row and the actual assigned VPS link to be visible. Remove
  gray-row, disabled title/focus, disabled-only no-assignment and contrasting-row
  assertions/comment. Preserve member verification, checkpoint selection and
  ordinary content capture. Do not hide rows, manufacture content or change
  unrelated networking/traffic checkpoints.
- tools/test-ip-inventory.cjs: adapt the existing fixture/scenario tests and
  expected return names, preserving their coverage. Enabled new/retained pools
  succeed; a completed rerun is read-only. Assert no network PUT, disable or
  re-enable request. Disabled, missing, null and nonboolean enabled values refuse
  before association/IP writes; old fixture identity mismatches also refuse.
  Replace obsolete successful-disable/disable-response expectations with these
  admission cases. Retain real caller coverage for API7/full query namespaces,
  pagination/truncation, both identities, lease loss, swap controls/resources,
  new/retained primary:false-or-null, invalid pickability, ownership, address,
  prefix, charge and assignment. Keep wrong-member scenario refusal.
- README.md:80-87, cluster/runtime-contract.md:470-end and
  docs/webui-change-workflow.md:102-141: describe the enabled assigned/detached
  inventory and remove disabled-row/tooltip visual acceptance. Keep public
  runtime/capture/validation/export, reduced resources and provenance guidance.

The label/address collision check deliberately refuses an old disabled fixture;
this is no adoption or data migration. The guard does not promise that all
fixture work is mutation-free: prepareFixtures can already have created its VPS
before ensureIpInventory runs. No reset, repair or old-guest reuse is selected.
Engine/state/runner/resource thresholds, Nix profiles, pinned V939159, validators,
lease helper, runtime verifier, exports and V product tests remain unchanged.

The THREE media paths return exactly to Gd0b4f40708cc8b59aab7c91ae05fba695abc233c:
captures.json and screenshots/{cs,en}/networking/ip-address-list.png. This removes
only M's generated inventory fields and bitmap replacements, retaining G's V939
pin, ip-inventory capability and all 60 concepts/120 variants. Do not restore the
whole inventory from the earlier base or delete the semantic screenshot entries.
Retained pre-M PNG SHA256 values are CS
ec1a7aec65b1314720535a0d00053ec875d959d1b047de3462463a6587dc4975 (671x312), EN
d3b02a2bdc8a0cda93ab31fa544d9d0e0a9c51eec9750628ae7b95a353ef4706 (646x312).
Restore their existing schema-5 metadata/review status exactly. They are older
retained assets, not newly generated G or final-source screenshots. No KB article
source was changed or published; no page, navigation contract or wiki edit is
needed for this scope reduction.

Root preserves publicly resolvable exact G, M, consumed V939 and historical E
objects/refs and their genuine capture/runtime/failure evidence before history
consolidation. Keep first K V-pin owner1f5e6e46 unchanged; fold this narrow normal
fixture correction into the portable-runtime owner and omit M from the active
series, leaving two logical K owners rather than an add/revert media tail.
The rewritten runtime commit has a new identity. Do not relabel G receipts or
PNGs, rewrite historical failures, or claim that the new fixture ran in G guests.
Root owns final history inventory and publication; implementer owns the six
source/doc paths above. Exact media restoration is root-owned Git work.

E4c869ab's existing paired-input owner changes only the kb-runtime selection in
flake.nix:7 and its generated flake.lock graph to final published K. Preserve
Dfea04c6de25448751239099eca7101c43cb495c2, all non-K siblings/follows, and the
separate optional-provider owner's normalized bytes/message. K's dependency
graph is unchanged. E selects the complete final K graph; no local override,
new selector stream or K/media/source attestation exception is needed.

No new guest or PNG generation is required to accept this scope removal.
Root selects affected existing test-ip-inventory/source checks and strict full
retained-inventory validation on the final committed tree, without --update or
--allow-missing and without old temporary capture results contaminating that
source context. Preserve those results as evidence rather than deleting them to
make validation pass. runner/validate-artifacts.cjs and runner/validate.rb allow
unchanged original inventory assets; strict success proves their bytes/contract,
not new-source native generation. Use normal hooks and affected new-head hosted
K/E source/package checks plus independent delta/history review. Reuse unchanged
V/runtime evidence at its real source; do not rerun the guest/media campaign.
After those checks, the changed neutral fixture has source-test evidence only;
its native recapture remains unperformed. Future capture requires matching source/artifact
admission. Only this design was appended; all operations and merge decisions
remain with root under their separate authority.
