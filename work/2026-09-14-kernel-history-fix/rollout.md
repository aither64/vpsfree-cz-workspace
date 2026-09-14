# Prepared rollout and node1 repair

These commands are prepared for a later approved rollout. They have not been
executed against production. Run configuration commands from this session's
`vpsfree-cz-configuration` worktree and its `nix develop` environment.

## Exact revision preflight

Before a future rollout, verify the reviewed configuration and package pin:

```sh
test "$(git rev-parse HEAD)" = 09b3370c2d628bcc7ab5eb7bbdf19edbcf8be347
git diff --exit-code
git diff --cached --exit-code
jq -e '.nodes.vpsadminServices.locked.rev == "337c9257f5e11f36afe81eba4951e267b83e2fc7"' flake.lock
```

Stop if any assertion fails. A later revision needs its own review and approval.
All 11 `cz.vpsfree/vpsadmin/*` consumers built successfully at this pin,
generation `2026-09-14--13-07-10`. No staging, production, or vpsAdminOS channel changed.

## Package and migration rollout

Both API hosts run supervisor writers, and `vpsadmin.databaseSetup.autoSetup`
is false. Activation alone does not run migrations. Keep both supervisors masked
through the first API activation, migration, and second API activation.

```sh
confctl ssh 'cz.vpsfree/vpsadmin/int.api?' systemctl mask --runtime --now vpsadmin-supervisor.service
confctl ssh 'cz.vpsfree/vpsadmin/int.api?' systemctl show --property=UnitFileState --property=ActiveState vpsadmin-supervisor.service
```

Inspect the host-labelled results for **both API1 and API2**. Require
`UnitFileState=masked-runtime` and `ActiveState=inactive` on each host. Stop for
missing output, a command failure, or any other state. The installed `confctl
ssh` prints individual remote failures without necessarily failing its overall
command, so its exit status alone is insufficient.

```sh
confctl deploy --no-health-checks 'cz.vpsfree/vpsadmin/int.api1' switch
confctl ssh 'cz.vpsfree/vpsadmin/int.api?' systemctl show --property=UnitFileState --property=ActiveState vpsadmin-supervisor.service
```

Again require both hosts to be runtime-masked and inactive before migrating.
The temporary deployment health-check bypass accommodates the paused
supervisors; perform the final service checks after restarting them.

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

Confirm migration `20260914120000` succeeded. It adds nullable
`node_kernel_events.last_confirmed_at` without a default or data rewrite.
Do not set existing confirmation values to the current time.

Back in the configuration worktree:

```sh
confctl ssh 'cz.vpsfree/vpsadmin/int.api?' systemctl show --property=UnitFileState --property=ActiveState vpsadmin-supervisor.service
confctl deploy --no-health-checks 'cz.vpsfree/vpsadmin/int.api2' switch
confctl ssh 'cz.vpsfree/vpsadmin/int.api?' systemctl show --property=UnitFileState --property=ActiveState vpsadmin-supervisor.service
```

Require the same masked/inactive state on both hosts before and after the second
switch. Once both packages and the schema are ready:

```sh
confctl ssh 'cz.vpsfree/vpsadmin/int.api?' systemctl unmask --runtime vpsadmin-supervisor.service
confctl ssh 'cz.vpsfree/vpsadmin/int.api?' systemctl restart vpsadmin-supervisor.service
confctl ssh 'cz.vpsfree/vpsadmin/int.api?' systemctl show --property=UnitFileState --property=ActiveState vpsadmin-supervisor.service
confctl ssh 'cz.vpsfree/vpsadmin/int.api?' systemctl is-active vpsadmin-api.service vpsadmin-supervisor.service
```

Check each host's output: supervisors must be unmasked and active, and both API
services must be active. Check both supervisor journals for ingestion or
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

## Separate node1 repair preview

On an updated API host, enter `vpsadmin-api-shell` and run:

```sh
NODE_ID=400 bundle exec rake vpsadmin:node:repair_kernel_history_bounds
```

Review every proposed event, interval, and supporting evidence ID. The August to
September interval can be tightened only if a retained immutable snapshot proves
the prior state inside it and on the same boot. Production rows were not
inspected during diagnosis or implementation, so a successful node1 repair is
not assumed. Current snapshots, raw logs, and uname-only samples are excluded.
The repair also skips snapshots whose reconstructed content does not match its
stored digest, including older evidence that cannot reproduce that digest.

Each invocation computes a new candidate set. `APPLY=1` does not consume or bind
itself to a previous preview. For a later approval of exact proposed repairs,
pause both supervisors with the mask command above and verify both hosts are
runtime-masked and inactive. Prevent other history maintenance during this
window. Capture a fresh preview on the API host, using the same batch size for
all invocations:

```sh
set -o pipefail
NODE_ID=400 BATCH_SIZE=1000 bundle exec rake vpsadmin:node:repair_kernel_history_bounds | tee node400-approved-preview.txt
```

Obtain separate approval of that saved output. Keep the writers paused. Just
before applying, repeat the preview and require an exact match:

```sh
NODE_ID=400 BATCH_SIZE=1000 bundle exec rake vpsadmin:node:repair_kernel_history_bounds > node400-preapply-preview.txt
cmp node400-approved-preview.txt node400-preapply-preview.txt
```

Stop if the preview fails or differs, a writer resumes, or another history
maintenance operation runs. Review and approve a fresh preview before
continuing. With the same output and writers still paused, apply immediately:

```sh
NODE_ID=400 APPLY=1 BATCH_SIZE=1000 bundle exec rake vpsadmin:node:repair_kernel_history_bounds
NODE_ID=400 BATCH_SIZE=1000 bundle exec rake vpsadmin:node:repair_kernel_history_bounds
```

Inspect the apply results and final preview, then unmask/restart both supervisors
and check each host's health as above. If approval is deferred, restore normal
supervisor operation and repeat the paused preview procedure later.

Use any positive `BATCH_SIZE` consistently if 1000 is unsuitable. Reruns are
idempotent without new supporting evidence. Changes between inspection and
writing within one invocation are skipped under the node lock. Repairs preserve
upper bounds, classifications, confidence, effective times, and evidence, while
normal `updated_at` updates invalidate public revisions.

## Rollback

Pause both supervisors and verify their masks before rolling back application
packages. Older code ignores the nullable column but resumes the old bound
selection behavior. Keep the additive column and evidence-supported historical
repairs. Do not run a schema rollback or automatically restore the overly broad
historical intervals.
