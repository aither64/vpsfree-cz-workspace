# Restore shared seed state in committed concurrency fixtures

IP release concurrency specs need independent database connections. Their
setup refreshed SpecSeed.node/NodeCurrentStatus outside RSpec's normal rollback.
Later GenerateMigrationKeys specs then found that fresh seeded node as an extra
eligible pool and generated two keys instead of the expected one.

An ordered run of ip_release_concurrency_spec.rb followed by
transaction_chains/cluster/generate_migration_keys_spec.rb reproduced all three
failures (17 examples). Snapshotting/restoring the shared node and status rows,
including fixture-created audit versions, makes the same 17 examples pass.
Always account for mutations to shared seed rows, not only newly inserted rows,
when fixtures commit on independent connections.

Related initiative: work/2026-09-09-ip-release-mechanism; failed CI35153252867.

For a completed failed job inside a still-running workflow, `gh run view
--log-failed` refuses to return logs. Download the job endpoint instead:
`gh api --allow-escape-sequences repos/vpsfreecz/vpsadmin/actions/jobs/JOB_ID/logs
> /tmp/job.log`. gh 2.100 otherwise rejects ANSI sequences even with redirected
output. Read only relevant failure sections; fixture logs can contain test
credentials and recovery tokens.
