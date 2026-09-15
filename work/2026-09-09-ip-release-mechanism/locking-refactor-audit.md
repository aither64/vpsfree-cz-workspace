# Locking and accounting separation audit

Completed audit for the accepted September 15 follow-up. This supplements
`locking-notes.md`. Final review findings and their verified resolutions are in
`review-split-results.md`; the maintained implementation documentation is in
vpsAdmin `docs/ip-locking.md` and `docs/ip-release.md`.

## Generic provider

`adjust_resource!` shares allocation/validation with the absolute setter. It
locks a separate owner instance to preserve dirty caller attributes, reserves
the user resource with the existing vpsAdmin lock, and uses current SQL reads
for the allowance, usage row and aggregate validation. Absolute setters retain
their prior persistence, return values and first-use confirmation behavior.

82 provider/concurrency examples pass. The 35 absolute examples also pass when
loading the original upstream provider. 110 provider and real consumer examples
pass, including VPS resources, dataset quota/refquota and automatic expansion.

## Writer gaps addressed

- Export creation selects an IP before locking and previously did not reload or
  revalidate the selection. Export destruction also reads the selected host
  and IP before taking the corresponding locks.
- Internal DelRoute calls previously computed quota before reserving/reloading all IPs.
- Clear previously invoked DelRoute separately for routed and direct addresses; multiple
  deferred deductions can overwrite the same usage row. SoftDelete/Destroy
  repeated the issue across interfaces. The new bulk clear combines deltas before confirmations.
- Network batch allocation releases by owner identity from an ensure block even
  if acquiring the lock failed. Keep the acquired lock handle and release only
  that handle. Reload current metadata before choosing batch addresses; reset
  the cached parsed network after the reload.
- Automatic allocation and migration replacements need current selection
  checks, including location and purpose, after reserving the IP.

## In-memory and composite constraints

Export grant creation inside AddRoute intentionally uses an IP whose assignment
is pending confirmation. Reloading every already-reserved instance would lose
that state. Shared helpers need an explicit reserved-object path as well as a
fresh current-state path for public entry points.

Clone already sums addresses across interfaces before changing quota. Verify
that behavior through the actual clone chain. Multi-interface migration is
explicitly unsupported; preserve its rejection instead of expanding support.
Opposite-direction ownership/environment transfers must lock accounting owner
rows in a consistent order. Do not modify the generic Lockable or transaction
engine contracts to implement these domain requirements.


## Composite verification

Real Clear, SoftDelete and Destroy chains now each stage one summed deduction
for four public IPv4 addresses split between two interfaces and direct/via
routes. All pass; stored quota/assignments stay unchanged before confirmation.
The clone chain verifies one summed addition for two public IPv4 allocations
across two interfaces, alongside private IPv4 and IPv6 buckets. Separate SQL
sessions pass stale-snapshot additions and opposite-direction ownership
transfers. Generic absolute APIs and non-IP consumers retain their prior tests.
