# Persistent PHP UI review fixture

Executed C2/C3; actual IDs/counts/hashes are in i1-review-cluster-final-data.json,
i1-review-cluster-final-payload.json and i1-evidence.md. The following records the
prepared normal sequence. Execute only after lead's normal public start, complete applied boot
proof and healthy API/supervisor/nodectld/pools. Source is clean backend
140f0769e222dd2aa51e64d08f11cd5e8dae397b. No DisableBackups call, plan deletion,
fixture teardown, service stop or storage profile. Keep successful objects.

Use public `/home/aither/bin/vpsadmin-devcluster ssh
2026-11-25-backup-disable-design services -- ...`; capture command results in
private mode-0600 files and expose IDs/confirmations only. Guest `vpsadminctl
--raw` uses its configured authentication, never credentials on argv/output.
For in-process API construction, copy the existing `api_ruby` loader from
`tests/runner/extensions/vpsadmin_services.rb:302`: obtain `vpsadmin-api`
WorkingDirectory from systemd, set API_DIR/RACK_ENV=production, load its `lib`,
require `vpsadmin`, and invoke that package's `ruby-env-wrapped/bin/ruby`.
Use the existing storage helper's normal User.current/UserSession.current admin
context when firing chains. Do not alter confirmed/resource rows manually.

1. Discover active seeded admin/member IDs by login, regular node IDs by their
   configured names/IPs, node1's online confirmed hypervisor `tank/ct` pool, and
   an enabled vpsadminos OS template compatible with node1. Save IDs before any
   creation. Verify no object with our exact hostname/label already exists;
   unexpected presence requires reconciliation, never an automatic duplicate.
2. Create one normal pool on node2:
   `vpsadminctl --raw pool create -- --node NODE2 --label backup-review
   --filesystem tank/backup-review --role backup --is-open --max-datasets 10
   --refquota-check`. Await its real chain done and online confirmation.
3. Create one VPS owned by the discovered seeded member:
   `vpsadminctl --raw vps new -- --user MEMBER --node NODE1 --os-template TEMPLATE
   --hostname backup-ui-review --cpu 1 --memory 1024 --swap 0 --diskspace 10240
   --start --ipv4 0 --ipv4-private 0 --ipv6 0`.
   Await real chain done/running. Discover its logical Dataset and primary DIP.
4. Copy the existing ensure_dataset_in_pool helper: fire
   `TransactionChains::Dataset::Create.fire(pool, src, [dataset],
   label: src.label, properties: {})` under the normal admin session, record
   chain/DIP IDs, await done/confirmed. Require the new DIP belongs to our new
   backup pool and the same logical dataset.
5. Bind actual registered `daily_backup` definition to the source environment
   using existing ensure_dataset_backup_plan logic (EnvironmentDatasetPlan
   find_or_create, user_add/user_remove true). Attach via public
   `vpsadminctl --raw dataset.plan create DATASET --
   --environment-dataset-plan ENV_PLAN`. Record membership and actual scheduled
   backup/group actions/tasks, including cron/next behavior.
6. Set retention only on the two new fixture DIPs with existing scoped helper
   semantics: min_snapshots=10, max_snapshots=10, snapshot_max_age=86400. This
   metadata update protects evidence; it fabricates no snapshot/confirmation.
7. Via public node1 SSH and ordinary `osctl ct exec VPS`, write
   `/root/backup-ui-review-marker` with `backup-ui-review-s1\n`. Create primary
   snapshot with public `dataset.snapshot create DATASET -- --label review-1`.
   Record returned snapshot ID/name and await real confirmed SIP. Fire normal
   `TransactionChains::Dataset::Backup.fire(source, destination)` under admin
   context, record receipt and await done. Require snapshot1's backup SIP and
   branch entry confirmed and physical backup snapshot marker equals s1.
8. Change marker to s2, create/await `review-2`; change marker to s3, create/await
   `review-3`. Do not run another backup. Require three distinct confirmed
   primary snapshot IDs/names and at least the first confirmed backup SIP;
   newer snapshots remain an ordinary preservable suffix, with no older gap.
   Verify primary historical markers s1/s2/s3 and live marker s3 through exact
   fixture dataset/snapshot paths; verify backup s1 via its actual branch path.
9. Confirm every owned chain done, resource locks released, VPS running,
   retained real plan attached, pools online and current-source PHP form visible.
   Inspect default-on preservation checkbox and plan removal explanation without
   submitting. Record safe IDs/counts/checksums/chain IDs and effective schedule.
   This supplies review data; it does not certify full storage acceptance.

Safe handoff URLs: `https://webui.aitherdev.int.vpsfree.cz/`, dataset edit
`?page=dataset&action=edit&role=hypervisor&id=DATASET`, backup listing
`?page=backup&action=vps`, receipt `?page=transactions&chain=CHAIN`.
Credentials stay in the provider's protected account view. React remains
unavailable for this PHP-first cluster. Leave cluster and review objects intact.
