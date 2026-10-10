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
