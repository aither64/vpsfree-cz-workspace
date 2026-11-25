# Quota diagnosis — bounded discriminator result reconciled

## Current conclusion and ordinary-source restoration

One root-admitted diagnostic run on82c9b35f/tree6533022a completed successfully:
operation9f4d23d5, native85310 joined0. Exact source is
`/nix/store/2lrz5yb4zkczhgabv9yvry0k81rl52j2-source`, pinned OS
8e44a5124439b1f3048ffc56b1717614a5360358; actual config is
`/nix/store/5j6ya9l5w9x678mbbfjkhig3d4fgb2j4-os-test-tasks-dataset-expansion-enforce-and-resolve.json`.
The retained result receipt SHA256 is
2c1d4e286a05fdaf54cd5362c3f42707ff19e79f6731e157799409bb85da356b.
All eight native-log lengths/hashes were independently verified before unchanged
copies were retained under `../nov16-quota-diagnostic/quota-result-retained/`.
Original source refs b876/82c9, reviewed snapshots and failures remain intact.

The real task emitted one target1 diagnostic at services-shell.log:3288:
selected, expansion_count1, branch stop_returned. At before_stop_submission it
saved original_refquota10240, null last_vps_stop, referenced row23/value10250,
VPS1 active and status row1/runningtrue/uptime7200. Its actual constants remained
MAX_EXPANSIONS=-1, OVERQUOTA_MB=1, COOLDOWN=0 and strict9/102400. The original
ordinary conjunction passed. The expanded cached refquota11264 is separate from
the original_refquota10240 used by the predicate.

Fixture telemetry records the same referenced row23/value10250/updated_at09:10:53Z
and status row1/runningtrue/uptime7200/update_count1/updated_at09:10:17Z. Those
values remain in the saved cache at decision time09:11:07.972245Z. The second
identical status write retains the existing timestamp; timestamps do not prove
writer identity or precise commit order. The later fixture write records
referenced0. The exact compiled default script contains the original stop chain,
physical stopped-state, shrink chain, refquota-restored and resolved-state
assertions; its single original example succeeded. `fire` returning alone is not
used as the physical-stop proof.

This is a **non-reproduction**, not proof the historical failure was unrelated,
environmental or supervisor-caused. The failed CI attempt below never captured
its actual decision values, so its missing gate/cause remains unknown. No quota
eligibility fix, timeout change, fixture rewrite or further quota run is justified.
See `../nov16-quota-diagnostic/quota-observation-reconciliation.json` for bounded
marker/timing/source evidence. Native overall script982.9220189s, ordinary
command982.6382171s, default script721.53s and example268.74s are nested clocks,
not additive. The early watcher overrun assertion was incorrect at7m34s after
registration; it remains separate from authoritative native timing.

Root accepted exact-run terminal effects: both guests started once, QEMU exits
reaped0, normal destroy, both virtiofs disconnects and no new disks/sockets/shared
dir/helper entries. Native runner ended0; no extra cleanup was invoked and no
old-campaign/global-host quiescence claim follows. Original failed CI remains
failed with its own already-accepted exact-attempt effects conclusion.

The checkout is now clean ordinary feature
f9a523731700dfdef44ee96381091ce6930409a6/tree14ff2a7df370d9432262c45f0352454e0dbba728.
Normal trusted-hook git switch removed all diagnostic changes from the deliverable;
all three quota files equal published1ada. Diagnostic branch82c9 and b876/82c9
refs remain unchanged; nothing was cherry-picked or deleted. Ordinary delta is
only the accepted SMTP-negative scenario correction, not a quota product change.
No publication/export/client/pin/build or new long test was launched. Root owns
fresh admission for the remaining physical incident retry/history/transfer/data
scenario; `smtp-next-validation.md` describes that prepared boundary.

## Historical exact-attempt evidence, preserved

Source:1ada4b072229cb332492478cf754e0dd926d42fa; CI43765668910/attempt1,
job132970076360. Retained native data is artifact14196351535.zip; raw digesta384239a...
The terminal-coverage-effects-receipt.json and selected-script-outcomes.json record
complete run coverage/cleanup. No additional provider/guest execution is required
for reading these files.

The quota test's services-shell.log member is
os-test-tasks__dataset-expansion-enforce-and-resolve-e2924ff6/services-shell.log.
It records refquota10240/dataset1 at1671, expansion creation with stop_vps=true,
enable_shrink=true/max_over_refquota_seconds0 and chain4 at1697–1723. Expansion
chain4 is done at1894. The fixture writes every dataset1 referenced property10250
at1962–1976 (host23:53:34–39+0100), then status=true/running=true/uptime7200 at
1992–2009 (23:53:39–44). Both helper calls print only ok:true, with no row count
or readback. Rake runs at2021–2031 (23:53:44–50), exact MAX_EXPANSIONS=-1,
OVERQUOTA_MB=1,COOLDOWN=0, native0; only header Stopping VPS with datasets over
quota, no StopOverQuota chain. Wait after chain4 expires. Final chain table at
15297–15305 confirms no such chain. Native test-runner.log: one example failed
in1023.48s, entire script1209.16s. Missing eligibility values at actual decision:
no precise failed gate can be established retrospectively. No unrelated/environmental
attribution or timeout change is justified by this evidence.

Existing seams: tests/suite/tasks/dataset-expansion-enforce-and-resolve.nix:79–105
has synthetic property/status writes and separate rake invocation; shared
common.nix:23 runs existing bundle exec rake in a fresh process with supplied env;
common.nix:234/245 implement the two writes. Real enforcer is
api/lib/vpsadmin/api/tasks/dataset_expansion.rb:59–113 stop_vps. Its query requires
active expansion/stop_vps=true and active VPS; within-loop gates are referenced
minus threshold > original quota, last-stop cooldown, active/running VPS, nonnil
uptime >= cooldown, then expansion count > MAX_EXPANSIONS or over-quota duration.
ResourceLocked is caught separately. Preserve all original constants/order/assertions.

DatasetProperty.updated_at exists and is assigned the node report time by
api/lib/vpsadmin/supervisor/node/storage_status.rb:37–68, which directly updates
referenced from actual storage values. Fixture update! normally writes the model
timestamp; task also updates last_over_refquota_check/over_refquota_seconds.
Dataset#referenced is generated by api/lib/vpsadmin/api/dataset_properties.rb:81,
returning the first matching associated property's value; do not silently substitute
a diagnostic fresh projection for values actually consumed. Exact VpsCurrentStatus
additional timestamp columns were not established in this bounded read.

All six relevant quota fixture/common/task/expansion/stop-chain/storage-reporter
files are byte-identical to base537b (hashes available in command evidence). This
bounds changed scope but does not prove the failure unrelated. Architect owns the
smallest diagnostic observation design; no quota source edit/run has been made.
