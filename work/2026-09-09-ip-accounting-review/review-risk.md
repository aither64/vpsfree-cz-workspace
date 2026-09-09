# Risk and compatibility review

Reviewed `vpsfree-maintenance-tasks` commit
`9ec505df9b67bc19f7983c1bb5c34ad160eddd05` against
`6eea682ede8d8e2634b2d41e5b11cf0f02231bc6`, using the unchanged vpsAdmin
checkout at `19971f039771500d5d0304610f91fe6f4af5fed3` as the model and accounting
contract reference.

## Findings

### Important — the all-user snapshot has unbounded query fanout on the live database

`2026-09-09-check-ip-accounting/check_ip_accounting.rb:18-22` scans every
default-scoped user, and each iteration starts separate resource, package,
owned-address, and assigned-address relations at lines 70-139. Eager loading
adds further queries for their nested associations. `find_each` bounds only the
number of `User` objects in memory; it does not batch these dependent queries.
All of that work runs inside the single repeatable-read transaction at lines
196-202.

This creates two coupled production risks: database query load grows by many
round trips per user, and InnoDB must retain versions needed by the old snapshot
for the full scan while normal writers continue. The task can therefore put
material load on the live API database or fail before publishing a report,
despite the README saying that no maintenance window is required. A follow-up
benchmark on the narrowly amended implementation at `2522835` measured 14,046
queries and 43.259 seconds for 1,000 synthetic users. The authoritative
`UserClusterResource#used` delegation in that follow-up adds some queries, so
those exact numbers do not describe `9ec505d`, but they confirm the scaling risk
in the unchanged user-rooted traversal.

Bulk-load the four input sets for each user batch, or record an explicit
operator decision that the known production user count and database activity
make the measured runtime acceptable. If accepting the current implementation,
the runbook should give a quiet-period expectation and a way to stop the audit
when database pressure or snapshot age becomes excessive.

### Advisory — an error after publication can leave a report behind with failure status

`2026-09-09-check-ip-accounting/check_ip_accounting.rb:212` publishes the
report, after which lines 233-236 still access and write the summary. An I/O
error from `warn` (for example, a closed or failed stderr sink) enters the broad
rescue at lines 238-240 after the destination already exists; the rescue's own
`warn` can fail for the same reason. A temporary-file cleanup error after the
hard link is created has the same published-file outcome. This contradicts
`README.md:14-16`, which defines exit 1 as audit failure and says a failure
leaves no new report. It can also make an automated retry fail with `EEXIST`
even though the first run wrote complete JSON.

Once the hard link succeeds, keep subsequent logging failures from changing
the report's success/findings exit status, or explicitly remove the just-linked
destination when a later operation fails. Add a focused post-publication error
test so exit status and file presence remain an unambiguous contract.

## Compatibility and residual risk

The report is a new schema-version-1 artifact with no existing parser or pinned
consumer, so it introduces no mixed-version deployment ordering. It reads the
current vpsAdmin schema and models and writes no database, API, node, or
configuration state. Decimal strings preserve the source columns' precision,
and private no-overwrite publication protects the report during normal
operation.

The snapshot can still observe a transaction chain between its separately
committed steps. The README's requirement to review and rerun findings before
reconciliation is an adequate boundary for this read-only audit. Orphaned IPs
whose ownership chain cannot resolve to a scanned user remain outside the
accepted user-account audit boundary; the follow-up README clarification at
`2522835` makes that limitation explicit.

No Nix shell, database, or test process was started for this lane. The review
used the packet's verification evidence and the coordinator's follow-up scale
measurement.
