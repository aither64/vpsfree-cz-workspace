# Locking in the IP release prerequisite

Examined commit: [664e1e184, api: serialize IP ownership changes and cleanup](https://github.com/vpsfreecz/vpsadmin/commit/664e1e184f5d0d823d38ad6674d462206793df6e).
This is the historical analysis that led to the accepted split. The later
implementation separates and hardens these responsibilities; see
[commit-map.md](commit-map.md), [locking-refactor-audit.md](locking-refactor-audit.md)
and [review-split-results.md](review-split-results.md) for the final series.

## Two existing mechanisms

| Calls | Mechanism | Lifetime |
| --- | --- | --- |
| `lock(ip)`, `chain.lock(host)` | vpsAdmin resource locks, stored in `resource_locks` | Through the asynchronous transaction chain, including ordinary rollback |
| `object.acquire_lock { ... }` | The same vpsAdmin resource lock mechanism | The synchronous block; SQL visibility remains subject to the surrounding transaction |
| `lock!`, `reload(lock: true)`, relation `.lock` | ActiveRecord pessimistic SQL row locks | Until the enclosing database transaction ends |

The locking frameworks themselves were not introduced or rewritten by this
commit. See `api/models/lockable.rb:24` and
`api/models/transaction_chain.rb:270`. Resource locks normally reject a
conflicting operation with `ResourceLocked`; the call sites here do not opt
into the existing blocking/retry mode. They are not SQL locks held open while
a node executes commands.

`TransactionChain.fire2` prepares a chain in a database transaction
(`api/models/transaction_chain.rb:73`). SQL locks protect this preparation.
Resource locks remain after that transaction commits, until NodeCtld finishes
execution or ordinary rollback. A fatal chain retains its resource locks for
recovery (`libnodectld/lib/nodectld/command.rb`, `close_chain`).

There are no week-long IP locks associated with an announcement. The campaign
stores the original ownership and requested addresses. Release attempts acquire
locks when an administrator initiates release.

## Why both are used

The resource lock reserves an address across queued work. A subsequent locking
reload obtains its current database state before checking ownership, assignment
and eligibility. This also avoids a stale ordinary read under MySQL's
REPEATABLE READ isolation. A resource lock alone does not refresh an already
loaded ActiveRecord object; a SQL row lock alone does not survive the commit
that queues node work.

Three concrete races motivate the changes:

1. An address can be checked as unassigned while another operation is assigning
   it. Previously route assignment already took an IP resource lock, but after
   earlier checks; ownership changes did not share that lock. Taking the same
   lock and rechecking current state closes that gap.
2. Host/PTR cleanup can require node work and can restore records on rollback.
   Clearing ownership before cleanup completes makes the address reusable while
   the old chain can still restore old DNS or access grants. `Ip::Update` now
   retains ownership and quota until the final successful confirmation when
   cleanup has queued work (`api/models/transaction_chains/ip/update.rb:35`).
3. Two different IP operations can adjust the same quota total. Computing both
   changes from an old total loses one adjustment. A deferred confirmation can
   also overwrite a newer synchronous total. Short row locks serialize current
   delta calculation; the existing user-resource lock protects deferred totals
   (`api/lib/vpsadmin/api/cluster_resources.rb:259`).

Locking only the new campaign code would not be sufficient: the competing
writers have to honor the same reservation. This is why the prerequisite also
touches assignment, ownership changes, host addresses, PTR changes, DNS transfer
grants, NFS export clients, migration and VPS ownership changes.

`HostIpAddress#lock_with_ip!` centralizes the parent-IP and child-host reservation,
current reads and optional owner recheck. Migration reserves its IPs and hosts
across the whole chain, because routing may be temporarily detached in the
middle. Otherwise a campaign could interpret that intermediate state as an
unused address.

The later campaign commit additionally locks the original user during release
cleanup to serialize account deletion with resource accounting. That user lock
is in `api/models/transaction_chains/ip_release/release.rb:16`; it is not part
of the prerequisite commit named above.

## Scope and costs

The prerequisite contains 56 files, 1,368 added and 188 removed lines. Of these,
15 test files account for 604 additions and three generated localization files
for 283. The remaining 38 runtime files still contain 481 additions and 167
deletions: it is a broad runtime change despite the test/catalog contribution.

It also bundles behavior beyond acquiring locks:

- Relative quota updates in the shared resource-accounting helper.
- Recording the charge environment for newly owned allocations, and refusing
  operations on existing owned allocations whose charge provenance is missing.
- Restricting network role/IP-version changes while allocations exist, to avoid
  changing the quota category underneath them.
- Deferring disownership until cleanup succeeds, with the WebUI waiting for
  that completion before continuing its disown-and-remove flow.

These are distinct accounting, validation and completion changes, not merely
lock plumbing. Common IP/host locking is necessary for the chosen cleanup
design, but that does not make every change in this commit inseparable. The
accounting and validation parts should be reviewed and presented separately
before integration; this explanation does not silently rewrite the branch.

There are real availability costs. Pending cleanup or migration rejects
conflicting operations on its IPs/hosts until the chain finishes. A deferred
quota update reserves the user's resource type in that environment, so an
operation on another address can also conflict with it. In a bulk campaign
release, a later address belonging to the same user can therefore require
another administrator attempt after the first cleanup finishes (also recorded
in review-packet-v3.md). A fatal chain can keep
those reservations until recovery. SQL locks are short-lived but can still
wait or deadlock; ordering known row sets reduces, rather than eliminates,
that risk. Campaign release records a failed attempt for such contention and
supports a later administrator retry.

This relies on cooperating writers: all API processes must run the updated
paths, and old in-flight chains must be accounted for before using campaign
release. Existing owned addresses without charge provenance need the planned
operator reconciliation. There is no claim that these locks make arbitrary
direct database writes safe, or that an old API process observes the new rules.

The prior initiative reviews and tests cover the wider implementation. The
September 15 CI failure was an email assertion substring collision and provides
no evidence of a locking defect; see `ci-investigation.md` for the reproducer.
