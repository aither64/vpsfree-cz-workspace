# G1a disposable storage diagnosis trial

This record covers the session-owned storage-topology cluster on bridge
networking. It is an executed disposable trial, not a shared-host rollout or a
repair authorization. The source was the reviewed vpsAdmin feature head
`fa7cec3a89e433e91516a369f10b1b17b6eddfef`, with the reviewed
`dcad075a1` osctld provider in the cluster. Site configuration pins and
production systems were not changed.

## Preparation and recovery material

The cluster was running and ready. Before the update, it was at `read_write`
epoch 2, with no waiting transactions, active or unresolved chains, blocking
intents, or started/uncertain attempts. A private MariaDB dump was retained at
`/tmp/storage-redesign-db-backup.ly7GFN/db.sql.gz`; the directory is mode
0700, the dump is mode 0600, and gzip validation passed. Its SHA-256 is
`d85bacf31b355020bed0cc6a4e203ec73ad1237baf53c6b4b14070aff84f39b4`.
The services and three node generations were recorded before switching.
Private update logs are under `/tmp/storage-g1a-devcluster-update.Dr3cRN9F/`.
Do not publish the dump, cluster URLs, tokens, signed inputs, or raw captures.

An authenticated direct-admin API request changed the singleton freeze from
`read_write` epoch 2 to `read_only` epoch 3. It created one transition with the
direct actor and session. Services, then node1, node2 and storage1 were updated
sequentially while frozen. Database setup applied migration `20260926100000`
before the captures. MySQL, API, Supervisor and nginx were active with success
results; NodeCtld and osctld were running on all three nodes. The installed
Supervisor package identified exact source `fa7cec3a89e433e91516a369f10b1b17b6eddfef`.

## Observed execution

Two earlier attempts exposed real fail-incomplete boundaries. On the earlier
`e7f91a2` source, the service's pooled READ-COMMITTED isolation caused DB
capture to fail before inventory dispatch. The reviewed `851be5a` follow-up
sets a consistent READ-ONLY REPEATABLE-READ session snapshot and restores the
prior session level before publication. The next attempt exposed a RabbitMQ
exchange declaration mismatch before 5290 staging. The reviewed `fa7cec3`
follow-up makes both inventory endpoints declare the existing transient node
exchange. Neither earlier attempt sealed a complete capture or granted
readiness.

At exact `fa7cec3`, an interactive operator signer unlock ran
`activity-report` through the installed Supervisor wrapper. The command
returned its expected exit 2 with `state=sampled_incomplete` after about
100 seconds. It completed two private Pool captures, with eight successful
signed 5291 transactions and two successful signed 5290 transactions. The
report covered nodes 101 and 102 and Pools 1 and 2. It observed the osctld
`gc_trash_v1` signal, stable generations, complete inventories and empty Node
queues. Both Node child coverage samples were `unknown`; the reported reason
was `child_lifetime_unproved`. Consequently `node_quiet=false`,
`repair_ready=false`, and `executable=false`. The private report is at
`/var/lib/vpsadmin-storage-reconciler-g1a/activity-24880152-5022-42a8-bdf3-316b571db4b9/report.json`
inside the disposable services VM.

Capture runs 3 and 4 each sealed a complete source manifest `(2,2)` with
record version 1 and collector version 2. They retained freeze epoch 3,
selected-node scope, `historical_terminal_coverage=unknown`, and selector
coverage for current catalog, pending snapshot evidence, and observable node
work. Terminal history was explicitly `not_enumerated`; confirmation coverage
was `selected_chains_only`. The two ZFS passes matched per Pool: 17/17 and
12/12 records. Their DB captures contained 16 and 4 records respectively.
`complete` describes the requested diagnostic collection only.

For run 3, fresh offline `compare`, `dry-run` and `plan` processes all exited
successfully and produced the policy-2 report/advisory files and policy-3
candidate files. The six candidates were all nonexecutable and each retained
the `historical_terminal_coverage_unknown` proof blocker. Cold offline replay
did not require API, database or RabbitMQ startup.

## Return to ordinary service

Before release, authenticated status still showed `read_only` epoch 3,
`db_drained=true` and `repair_ready=false`. SQL found zero waiting
transactions, active or unresolved chains, blocking intents and
started/uncertain attempts. Service and node process checks were healthy.
An authenticated expected-epoch API transition returned the cluster to
`read_write` epoch 4. A fresh GET confirmed epoch 4 and repair readiness still
false. SQL confirmed exactly one epoch-4 transition with copied actor user,
session and login. The cluster remained running and ready. No repair/APPLY,
identity publication or production strict mode was exercised.

## Remaining gates

Exact-head CI was still running at this record's checkpoint. The 40,000-object
scale case passed without retained locks; the global retained-lock selector's
correlated probe needs a populated cohort including unrelated-node locks
before live diagnostic use. Capture has a 10-second statement timeout and
fails incomplete if that query cannot finish, so this is a liveness risk, not
a complete-but-truncated result. Test pooled-session restoration failures and
the existing max-statement-time restore behavior before wider rollout.
This trial does not prove Node child lifetime, continuous exclusion, complete
historical terminal settlement, repair readiness or APPLY. Milestone G1b's
maintenance owner and runtime exclusion remain design work.
