# Architecture and repetition review

Reviewed maintenance commit
`9ec505df9b67bc19f7983c1bb5c34ad160eddd05` against
`6eea682ede8d8e2634b2d41e5b11cf0f02231bc6`, with the unchanged vpsAdmin
reference at `19971f039771500d5d0304610f91fe6f4af5fed3`.

## Findings

### Important — the user-rooted traversal has no coverage for broken ownership chains

`2026-09-09-check-ip-accounting/check_ip_accounting.rb:18` starts from the
default-scoped `User` relation, and lines 103-139 only look for addresses whose
`user_id` equals that already-found user or whose joined VPS has that user's
ID. An allocated address with a dangling `user_id`, or a userless assigned
address with a missing network interface, VPS, or VPS owner, matches neither
scope and is silently absent from the report. The relevant core tables have
indexes but no foreign keys enforcing those relationships, so this is a data
shape the database permits. It also bypasses the validation at lines 110-115,
despite the review packet's guarantee that missing or broken references either
become findings or abort publication.

This can produce a clean report while an accounting-relevant IP is omitted
from every user's inventory. Enumerate the accounting-relevant IP inventory as
an owning input, resolve its effective owner (the vpsAdmin model exposes
`IpAddress#current_owner` at `api/models/ip_address.rb:195`), and explicitly
skip the intentionally excluded hard-deleted-owner case while reporting or
failing on unresolved ownership chains. A focused test should cover a taken IP
whose non-null ownership or assignment reference cannot resolve.

### Important — recorded usage reimplements the provider's accounting rule

`2026-09-09-check-ip-accounting/check_ip_accounting.rb:147` independently
defines recorded use as the sum of association rows for which `enabled &&
confirmed?`. The owning vpsAdmin implementation is
`api/models/user_cluster_resource.rb:14-27`, where `UserClusterResource#used`
defines both the eligible states and the query scope. The spec at
`check_ip_accounting_spec.rb:109-119` repeats the maintenance implementation,
so it will remain green if the provider's eligibility or aggregation rule
changes.

The README promises that `recorded_used` matches `UserClusterResource.used`.
If the live provider changes confirmation-state handling or the set of rows it
aggregates, the audit can silently report false usage drift and drive the later
reconciliation from a different rule. Obtain the total from `resource.used`,
or expose one read-only provider relation/calculator used by both call sites;
the report can still serialize all associated rows as evidence.

### Important — the whole-cluster snapshot performs query fanout per user

The loop at `2026-09-09-check-ip-accounting/check_ip_accounting.rb:18-22`
executes separate resource, package, owned-address, and assigned-address
relations at lines 70-139 for every user. Even before eager-load queries for
populated associations, this is at least four database queries per user. The
entire fanout runs inside the single repeatable-read transaction at lines
196-202.

Runtime and query count therefore grow with both the number of users and the
nested preload sets. On a production-sized user table, the audit can hold an
old InnoDB snapshot for a long time, retain undo history while normal writers
continue, and fail before it publishes any report. That conflicts with the
documented no-maintenance-window execution model. Iterate in user batches and
bulk-load/index the four input sets for each batch (or build global indexes
once where bounded), then perform the same in-memory grouping. Record a query
count or representative large-fixture timing so this all-user path cannot
regress back to per-user relation loading.

## Assessment

The finite `RESOURCE_NAMES` list is an intentional schema-1 audit boundary,
and IP-to-resource mapping correctly delegates to `IpAddress#cluster_resource`
rather than reproducing `Network#cluster_resource`. Recomputing package totals
is necessary to compare the stored limit with its source data; the current
vpsAdmin calculator is mutation-oriented, so that repetition is reasonable for
this dated read-only task. The report schema, documentation, and focused tests
remain together in the owning task directory, and no shared registry or
speculative framework was introduced.

No Nix, Bundler, database, or other test processes were run in this review
lane; the review used the packet's completed verification evidence.
