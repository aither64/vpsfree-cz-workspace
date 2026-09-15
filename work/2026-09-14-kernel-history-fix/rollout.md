# Prepared rollout and all-node repair

These commands are prepared for a later approved rollout. They have not been
executed against production. Run configuration commands from this session's
`vpsfree-cz-configuration` worktree and its `nix develop` environment.

## Exact revision preflight

Before a future rollout, verify the reviewed configuration and package pin:

```sh
test "$(git rev-parse HEAD)" = b792c50e3baa17a73989dda1129cb17ba0e63587
git diff --exit-code
git diff --cached --exit-code
jq -e '.nodes.vpsadminServices.locked.rev == "c38839d5be62e9d40d055b23a84844e2037ba4db"' flake.lock
```

Stop if any assertion fails. A later revision needs its own review and approval.
All 11 `cz.vpsfree/vpsadmin/*` consumers resolve to this exact pin. All eleven built successfully as generation
`2026-09-15--10-59-39`, selected explicitly below. No staging, production, or
vpsAdminOS channel changed.

## Package and migration rollout

Both API hosts run supervisor writers, and `vpsadmin.databaseSetup.autoSetup`
is false. Activation alone does not run migrations. Keep both supervisors
stopped throughout the first API activation, migration and second activation.

On **each API host**, run this block as root to install a temporary start guard:

```sh
set -e
install -d -m 0755 /run/systemd/system/vpsadmin-supervisor.service.d
touch /run/vpsadmin-kernel-history-writers-paused
cat > /run/systemd/system/vpsadmin-supervisor.service.d/90-kernel-history-pause.conf <<'UNIT'
[Unit]
ConditionPathExists=!/run/vpsadmin-kernel-history-writers-paused
UNIT
systemctl daemon-reload
systemctl stop vpsadmin-supervisor.service
```

The marker makes the added start condition false. The runtime drop-in applies
to the NixOS unit under `/etc` and survives package activation. Keep both API
hosts running while the guard is needed; files under `/run` do not survive a
host reboot.

From the configuration worktree, verify the guard on **both API1 and API2**:

```sh
confctl ssh 'cz.vpsfree/vpsadmin/int.api?' test -f /run/vpsadmin-kernel-history-writers-paused
confctl ssh 'cz.vpsfree/vpsadmin/int.api?' systemctl cat vpsadmin-supervisor.service
confctl ssh 'cz.vpsfree/vpsadmin/int.api?' systemctl show --property=LoadState --property=DropInPaths --property=ActiveState vpsadmin-supervisor.service
confctl ssh 'cz.vpsfree/vpsadmin/int.api?' busctl --json=short get-property org.freedesktop.systemd1 /org/freedesktop/systemd1/unit/vpsadmin_2dsupervisor_2eservice org.freedesktop.systemd1.Unit Conditions
```

Require the marker check to succeed on each host, the exact condition above in
the displayed drop-in, `LoadState=loaded`, the pause file in `DropInPaths`, and
`ActiveState=inactive`. The effective Conditions array must include
`["ConditionPathExists", false, true, "/run/vpsadmin-kernel-history-writers-paused", ...]`.
The last integer records evaluation state and need not have a particular value.
Stop for missing output or any mismatch. The installed
`confctl ssh` can report an individual remote failure without failing its
overall command, so inspect the host-labelled results.

After those checks, prove that a start is blocked on both hosts:

```sh
confctl ssh 'cz.vpsfree/vpsadmin/int.api?' systemctl start vpsadmin-supervisor.service
confctl ssh 'cz.vpsfree/vpsadmin/int.api?' systemctl show --property=ActiveState --property=ConditionResult vpsadmin-supervisor.service
```

Require `ActiveState=inactive` and `ConditionResult=no` on both hosts. A skipped
start can return success, so check these properties explicitly.

```sh
confctl deploy --generation 2026-09-15--10-59-39 --no-health-checks 'cz.vpsfree/vpsadmin/int.api1' switch
```

Repeat the guard checks and blocked-start probe on both hosts before migrating.
The temporary health-check bypass accommodates the paused supervisors; check
service health after restarting them.

On API1, run the migration with the database account and the newly activated
package. The setup service's working directory identifies that package without
copying credentials or depending on the API account having DDL privileges:

```sh
db_dir=$(systemctl show -p WorkingDirectory --value vpsadmin-database-setup.service)
db_package=$(dirname "$db_dir")
systemd-run --unit=vpsadmin-kernel-history-migration --wait --collect --pipe \
  --service-type=exec --working-directory="$db_dir" \
  --uid=vpsadmin-database --gid=vpsadmin-database \
  --setenv=RACK_ENV=production \
  --setenv=SCHEMA=/var/lib/vpsadmin/database/cache/schema.rb \
  "$db_package/ruby-env/bin/bundle" exec rake db:migrate
```

Confirm migrations `20260914180000` and `20260914190000` succeeded. They add
nullable `node_kernel_events.last_confirmed_at` without a default and an empty
private `node_kernel_evidence_checkpoints` table. Neither rewrites history or
seeds confirmation times. Do not set existing confirmations to the current time.

Back in the configuration worktree, repeat the guard checks and blocked-start
probe on both hosts, then activate API2:

```sh
confctl deploy --generation 2026-09-15--10-59-39 --no-health-checks 'cz.vpsfree/vpsadmin/int.api2' switch
```

Repeat the guard checks and blocked-start probe after API2 activation. Once both
packages and migrations are ready, run this block as root on **each API host**:

```sh
set -e
rm /run/systemd/system/vpsadmin-supervisor.service.d/90-kernel-history-pause.conf
rm /run/vpsadmin-kernel-history-writers-paused
systemctl daemon-reload
systemctl restart vpsadmin-supervisor.service
systemctl show --property=ActiveState vpsadmin-supervisor.service vpsadmin-api.service
```

Check each host's output: both supervisors and both API services must be active. Check both supervisor journals for ingestion or
unknown-column errors. From `vpsadmin-api-shell`, choose a node whose current
public baseline and report establish a complete stable state:

```sh
read -r -p "Node ID with complete stable evidence: " CONFIRM_NODE_ID
export CONFIRM_NODE_ID
bundle exec ruby -r ./lib/vpsadmin -e 'n = Node.find(Integer(ENV.fetch("CONFIRM_NODE_ID"))); e = n.node_kernel_events.kernel_history.find_by(current: true); p e&.attributes&.slice("id", "observed_after", "observed_before", "last_confirmed_at", "updated_at")'
```

Repeat after later reports arrive. `last_confirmed_at` should advance for the
same stable state while the original bounds and `updated_at` stay unchanged.
An incomplete or legacy-ambiguous baseline may remain unconfirmed; inspect its
evidence instead of forcing a value. Confirm normal API and supervisor health.
No node update, patch unload, or reboot is required.

## Separate historical repair

Use the reviewed `2026-09-14-repair-kernel-history-bounds` task from maintenance
revision `2fdc9f2889ac419136cd0cde0e0955c015ae7107` on an updated API host. Verify
the checkout before entering the task directory:

```sh
test "$(git rev-parse HEAD)" = 2fdc9f2889ac419136cd0cde0e0955c015ae7107
git diff --exit-code
git diff --cached --exit-code
cd 2026-09-14-repair-kernel-history-bounds
```

Keep the checkout readable by the installed API service account.
The shebang selects the installed vpsAdmin API runtime. Run it from the task
directory; no node argument means all eligible node/storage hosts, including
inactive hosts. A subset remains available for investigating node1 alone:

```sh
./repair_kernel_history_bounds.rb
./repair_kernel_history_bounds.rb --node 400
```

Review the node/event IDs, proposed intervals and supporting evidence IDs.
Retained immutable evidence must prove the previous state inside each interval
and within the same boot. Production rows were not inspected, so tightening the
node1 interval is not assumed. Mutable snapshots, private recovery checkpoints,
raw logs and uname-only samples are excluded. Altered snapshot digests are
skipped. Software, sysctl and other component histories are outside this repair.

For approval of exact proposed repairs, install the start guard on both API
hosts using the block above. Verify the guard and blocked start on each host.
Keep other history writers paused too. Capture a fresh all-node preview:

```sh
set -o pipefail
./repair_kernel_history_bounds.rb --batch-size 1000 | tee approved-preview.txt
```

After approval, with writers still paused, repeat the preview and compare it:

```sh
./repair_kernel_history_bounds.rb --batch-size 1000 > preapply-preview.txt
cmp approved-preview.txt preapply-preview.txt
```

Stop if either command fails or the output differs. If a writer resumes or the
preview changes, review a fresh preview before applying. With matching output:

```sh
./repair_kernel_history_bounds.rb --apply --batch-size 1000
./repair_kernel_history_bounds.rb --batch-size 1000
```

Inspect the apply results and final preview, then remove only the pause
drop-in and marker on each host, reload systemd, restart both supervisors and
check each host's health as above. If approval is deferred, restore normal
supervisor operation and repeat the paused preview procedure later.

Use repeated `--node ID` options consistently across these commands to limit an
approved run to a subset. Each invocation freezes its own node/event candidate
set; apply does not consume a saved preview. Before each write it revalidates the
target, predecessor and evidence under the node lock. Concurrent changes and
insufficient evidence are reported as skips. Repairs preserve the upper bound,
classification, confidence, effective time and evidence; normal `updated_at`
updates invalidate revisions. Reruns without new evidence make no changes.
An interrupted apply retains earlier committed repairs and can be rerun.

## Rollback

Install and verify the start guards on both API hosts before rolling back
application packages. Keep both supervisors stopped until rollback is ready. Older code ignores the nullable column and private checkpoint table
but resumes the old recording behavior. Keep both additive schema changes and
all evidence-supported historical repairs. Do not run a schema rollback or
automatically restore the overly broad historical intervals.
