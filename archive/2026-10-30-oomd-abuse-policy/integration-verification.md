# Published application integration verification

Current cleared and published head is
`4d72e3e754fd47b598de1e54e05b3c5d26c62200`. Lead reports retained reviewer0
cleared the separate test-environment commit and complete history with no
Blocking or Important findings. Fresh SSH fetch required no rebase; exact
force-with-lease from `5a59ead40a283f74d211c7afde4d4d69aab28785` succeeded, and
`ls-remote` verified the corrected feature head and unchanged master
`ac10a62f1cb0fc890378ae83cdf18dd0e29f049a`. Proof reached lead and KB owner3.
Historical publication/build receipts below retain their actual source identity.

User-requested disk cleanup now takes priority. The owned final-source build was
interrupted through its verified Nix client (PID 2405219), native exit 1 after
156 seconds; log records `interrupted by the user`, with no kernel build and no
guest scenario launch. `final-image-build.{log,json,pid,exit}` retains the
attempt. The PID is absent and the exact temporary state root
`/tmp/oom4d.GPsawj` was empty, containing no images or GC root links. It was
removed after that reconciliation. Final-source rebuild/runtime are deferred.

Both old-head test JSONs and service image store paths were already absent at
cleanup inventory; the old build used `--no-link` and no explicit old-image GC
roots exist. Final test JSONs had not been realized. The worktree-specific manual
DB root `/run/user/1000/vpsadmin-test-db-594156217b47` is absent; all owned
automatic DB operations completed with native helper cleanup. No unknown DB or
peer session root was removed.

Removed reproducible, ignored, unused caches in this exact worktree:
`api/.gems` (103,661,568 allocated bytes) and `.gems` (50,569,216 bytes). All owned
test, utility and hook processes had exited. Three completed check scripts were
removed from `/tmp`; their exact contents survive in `retired-check-commands.txt`.
Source, Git refs, review evidence and logs remain intact. Root free bytes were
46,816,894,976 before interruption and 45,752,578,048 after owned cleanup; this
machine-wide delta is not an attribution of bytes reclaimed by this package.
No direct store deletion or profile-generation pruning occurred. No extra roots
are needed for the deliberately deferred build: exact Git source, locked input
graph and store receipts are preserved. After the lead confirmed coordinator
collection completion (exit 0, no held rows removed), a fresh catalog Luna/low
utility launched one ordinary `nix-store --gc`. It owns the native command and
will retain `nix-gc.{log,exit}`, before/after `df` snapshots and elapsed time.
The utility's own bounded observation shows actual store deletion progress,
not a GC-lock wait. It completed normally: exit 0 in 315 seconds, native totals
1,000 store paths deleted and 2.3 GiB freed. Root/Nix/tmp available bytes changed
from 45,346,455,552 to 48,477,487,104 (machine-wide increase 3,131,031,552 bytes).
`/dev/shm` changed from 35,225,849,856 to 35,225,845,760 bytes. Full native log,
exit, elapsed and snapshots are `nix-gc.log`, `nix-gc.exit`,
`nix-gc-elapsed.txt`, `nix-gc-before.txt` and `nix-gc-after.txt`; watcher summary
is `nix-gc-watcher-result.txt`. No cleanup operation remains running. No image
rebuild or guest execution resumed after reclaim.

New exact-head hosted runs are integration CI `41121263152` and API specs
`41121263198`. Normal cancellation of superseded queued integration run
`41115698406` was acknowledged; it remained queued and force-cancel returned
HTTP 409 (not in progress). This unresolved remote cancellation is accounted;
no current-head or unrelated workflow was canceled. Original failed API native
evidence is preserved. Neither required runtime scenario has passed yet.

The superseded integration run later completed with `cancelled`. Current-head
API run `41121263198` again failed its foundation groups: full 1,459 examples /
72 failures (seed 37763), core 1,459 / 2 failures (seed 10889). These are different
from the original snapshot errors; original affected six-file failures no
longer appear. Current native results/environments and complete job logs are
retained in `ci-41121263198-attempt1/`. This is evidence preservation only:
diagnosis and any source/test work were held for the cleanup milestone. Current
CI acceptance remains unresolved; local passes are not a full-suite proof.

## Source and publication

Reviewed and published vpsAdmin feature head:
`5a59ead40a283f74d211c7afde4d4d69aab28785`, tree
`55ba156994507edd4ebe334adadffd9767f73814`. Backend commit:
`dbfd2bbf060237189797aafa7db359ea0edbd797`.

Fresh SSH fetch required no rebase. Authoritative `git ls-remote --heads origin`
returned feature `5a59ead40a283f74d211c7afde4d4d69aab28785` and master
`ac10a62f1cb0fc890378ae83cdf18dd0e29f049a` on
`git@github.com:vpsfreecz/vpsadmin.git`. Proof was sent to lead and KB owner3.
No merge or deployment was performed.

The source/input receipt is `vpsadmin-published-flake-metadata.json`, including
the complete locked graph. Published source store path:
`/nix/store/710id7lral4hqcjkv8aimqfvmadk88sk-source`, NAR hash
`sha256-NSETbm2yBSjs4nzC+NUl9L/awqvmAHBXglrUzZpFSW8=`. vpsAdminOS input:
`8e44a5124439b1f3048ffc56b1717614a5360358`.

## Hosted selection and status

Exact-head integration run:
<https://github.com/vpsfreecz/vpsadmin/actions/runs/41115698406>.
The fresh catalog Luna/low watcher returned an accounted queued result: no
runner, steps, scenario selection preview or scenario results yet. Its JSON
status snapshots are `published-ci-41115698406-{status,jobs,api}.json`.

Selection **source proof**, distinct from hosted execution: the actual
`tools/select_ci_tests.rb` run over the published base-to-head changed paths
returned `mode=full`, `filter=tag=ci`, reason
`full rule matched api/db/migrate/20261030180000_add_vps_oom_policy.rb`.
Published `testsMeta.x86_64-linux` confirms both required scenarios carry `ci`:
`alerts/oom-abuse-policy` (display name `alerts-oom-abuse-policy`) and
`webui#oom-policy`.

Neither scenario has an integration pass at this checkpoint. Physical stop,
SMTP retry, restart, cooldown, ownership transfer/data and browser assertions
remain unexecuted. Do not infer those results from source or unit checks.

## Local fallback admission preparation

No guests or heavy builds started. The native fresh utility launch for this
preparation did not complete correctly; the parent is using the monitoring
skill's visible minimal-output fallback. The earlier CI watcher exited without
abandoning a local command; remote queued CI remains accounted here.

Pinned runner metadata requests 16 GiB RAM/shm and 12 CPUs for the OOM scenario;
24 GiB RAM/shm and 16 CPUs for the legacy browser scenario. Preserve those VM
sizes and use one scheduler with `--jobs 1`, a short private `--state-dir`, and
`--stop-on-failure` if local runs are admitted.

The pinned runner's unmodified ResourcePool reports 42.6 GiB memory capacity,
24.8 GiB shm capacity and 96 CPU budget after its default 8 GiB RAM and shm
reserves. Both scenarios fit separately. Disk remains the admission dependency:
42,576,625,664 bytes available at the observed checkpoint. KB owner3's bounded
source shell uses about 296.5 MiB; no concurrent KB VM/capture admission exists.
Coordinate any heavy allocation with owner3 before launch.

The no-build Nix plan completed with exit 0 using `nix build --dry-run --json
--no-link` for the two existing test derivations. It lists 188 builds and 40
substitutions (198.7 MiB compressed, 303.9 MiB unpacked). Kernel and modules are
substitutions, with no kernel compilation listed. Retained outputs are
`local-scenario-dry-run.{json,log}`. Exact derivations and outputs:

- `/nix/store/pi354x5frz56798mmxz61pml8yjvxql9-os-test-alerts-oom-abuse-policy.json.drv`
  produces `/nix/store/fpnd05hran0mbr0s4gbbl6ji0s2f2y7j-os-test-alerts-oom-abuse-policy.json`.
- `/nix/store/szbfv0g6xi1yczkp1lh88v228ikl2lzq-os-test-vpsadmin-webui.json.drv`
  produces `/nix/store/7hg9br63h5n21pw8jsgnrrf9j7z3lbms-os-test-vpsadmin-webui.json`.

The existing image derivations calculate root image size from their installed
closure, 512 MiB extra space and filesystem overhead. Runtime copies that root
image; node data disks use sparse `truncate`, 20G per node. Preserve those
defaults. Exact image derivation inspection is `local-image-derivations.json`.

KB owner3 confirmed no impending heavy allocation and keeps capture/runtime
unadmitted during a staged image build. A fresh standalone catalog Luna/low
utility now owns this one operation with explicit `danger-full-access`/`never`:
build the above two derivations using `--no-link --json --max-jobs 1 --cores 4`.
It may interrupt only its own build for unexpected kernel compilation or root
free space below 20 GiB. No runtime scenarios are authorized in this utility;
actual completed image sizes must be measured before guest admission. Logs and
exit receipt will be `local-image-build.{log,json,exit}` and
`local-image-build-watcher-result.txt`; its event stream is
`local-image-build-watcher.jsonl`. No build or guest pass is claimed yet.

That utility interrupted its own build after one second (exit 1), because its
monitor incorrectly matched a pre-existing foreign kernel command in global
`ps`. The reported make process had started over three hours earlier. It did
not signal that process. The assigned Nix log contains a plan and interruption,
with no `building` or `copying path` start. The utility and assigned Nix command
are exited. This is a monitor false-positive, not a kernel-cache or application
failure. Preserve its original artifacts; do not accept its escalation as proof
that these derivations compile a kernel.

After diagnosis and reconciliation, the parent launched the same bounded build
with minimal supervision using only its owned log/PID and root free-space
observations. This attempt has separate `local-image-build-2.{log,json,pid,exit}`
receipts. It retains the 20 GiB free-space stopping condition, single build job,
four build cores and kernel escalation rule. No guest scenario is started.

Attempt 2 completed with exit 0 in 461 seconds, with no kernel compilation.
The realized exact old-head test configurations are the output paths listed
above. `local-image-measurements.json` records each node/service profile and
image. Service root images are 5,313,134,592 and 6,016,729,088 bytes apparent,
3,579,817,984 and 4,191,973,376 bytes allocated. Node squashfs images are
427,360,256 bytes each. Root free after completion was 37,009,141,760 bytes.
These profiles predate the text correction below and are reusable cache inputs,
not corrected-source physical verification. No runtime guest test has run.

## Hosted foundation failures and narrow mail correction

Exact-head API specs run 41115698380 reported 30 foundation failures in each
mode (1,459 examples; full seed 13701, core seed 14766). Native results,
environments, manifests and job logs are retained separately under
`ci-41115698380-attempt1/`. VPS and platform-operations groups passed in both
modes. All new OOM model examples passed in both foundation groups.

One failure concerns this feature: the existing built-in template-content
assertion rejects site branding and membership wording. Lead approved replacing
the membership paragraph in both built-in English OOM bodies with exactly
"If your workload needs more memory, you can increase your VPS's memory."
and removing the external incident-KB paragraph. The vpsFree site templates
remain unchanged. The resulting diff is two files, two inserted lines and
sixteen deleted lines; the existing generic-content assertion is unchanged.
`generic-mail-fix-specs.{log,json,exit}` proves 29 examples, zero failures,
exit 0, including the full existing mail-template group, real OOM renderer and
ordinary incident New/Send groups (19.96 seconds plus 13.62 seconds load).

The other 29 failures are concurrency/reconciliation errors in unchanged
baseline files, primarily snapshot-conflict errors and resulting savepoint or
source-marker conflicts. A controlled representative diagnostic isolates the
database setting: the same existing cluster-resource concurrency example passes
on local MariaDB 11.4.12 / REPEATABLE-READ / snapshot isolation OFF, and fails
with the exact hosted record-changed error when only snapshot isolation is ON
in its own disposable DB. Evidence:
`local-concurrency-diagnostic.{log,json}` (1/0) and
`local-snapshot-on-diagnostic.{log,json,exit}` (1/1, exit 1, intentional diagnostic).
No production or source default was changed by these experiments.

Hosted logs show Ubuntu resolute MariaDB package 11.8.6-5ubuntu0.1. Official
MariaDB source at
<https://github.com/MariaDB/server/blob/mariadb-11.8.6/storage/innobase/handler/ha_innodb.cc#L865>
declares `snapshot_isolation` with default `TRUE`. This supports an upstream
test-environment default change as the concurrency-failure cause. A previous
successful default-branch run's native artifacts have expired, so they are not
claimed as a current baseline reproduction.

Lead authorized and inspected the bounded compatibility correction. Existing
`tools/test_db.rb#start_server!` now passes
`--innodb-snapshot-isolation=OFF`; its existing startup path queries/logs actual
server version, transaction isolation and snapshot setting. `tests/README.md`
documents why this test-only setting preserves current supported semantics and
why future database upgrades need qualification. No production/application
setting, runtime SQL retry or assertion changed.

Both hosted API modes execute normal RSpec without a configured `DATABASE_URL`;
`api/spec/spec_helper.rb` uses `SpecDbSetup.establish_connection!`, whose
`auto_database_url` requires this helper and calls `TestDb.auto_start!`. Thus the
same startup flag reaches both matrices. No workflow or action change was
needed. Actual server settings are recorded in existing job test output rather
than a new evidence registry.

A fresh Luna/low utility ran only the six affected existing files, sequentially
in core and full modes, each with a fresh automatic disposable DB. Both passed:
64 examples / zero failures / exit 0 in each mode (59 and 66 seconds elapsed).
`test-db-compat-{none,all}.{log,json,exit}` contains native evidence; helper output
in both confirms MariaDB 11.4.12, REPEATABLE-READ and snapshot isolation OFF.
`test-db-compat-watcher-result.txt` records the completed operation. No process
remains running. Scoped Ruby lint (one file) and whitespace checks passed.
Hosted MariaDB 11.8 validation of the corrected source is still pending.

## Corrected three-commit review packet

Base remains `ac10a62f1cb0fc890378ae83cdf18dd0e29f049a`. Final local series:

1. `8beecad4492840be353a14a1f861e2d535847323` — backend feature with the
   lead-inspected generic fallback correction folded into its owning commit.
2. `52b794ef8fdd92474e558ec000cafebbe2be3934` — unchanged legacy UI patch.
3. `4d72e3e754fd47b598de1e54e05b3c5d26c62200` — separate disposable-testDB
   compatibility setting, actual-setting log and test documentation.

Final tree `588e65a8a13e3da69483cbf4c44cdfac84694a9e` equals the complete tested
pre-consolidation tree exactly (`cmp` exit 0). Relative to published
`5a59ead40a283f74d211c7afde4d4d69aab28785`, only four files changed: the two
approved template bodies, test helper and test README (24 insertions, 16
deletions). `generic-mail-range-diff.txt` binds old and new complete ranges:
backend differs only in those approved body passages, legacy patch is `=`, and
the third test-environment commit is additive. No superseded functional fixup
remains in the final series.

Old publication and pre-consolidation source are retained at
`refs/review/2026-10-30-oomd-abuse-policy/vpsadmin-before-generic-mail-fix` and
`.../vpsadmin-before-generic-mail-consolidation`. Earlier original review ranges
and remediation refs remain preserved as recorded in `remediation.md`.

The sole final additive migration `20261030180000_add_vps_oom_policy` and core
schema are byte-unchanged from the cleared published source (`git diff
--exit-code` exit 0). It remains unmerged, unreleased, undeployed and not
externally persisted. No new migration or compatibility path was introduced.

Normal pre-commit and commit-message hooks passed for both correction commits;
normal Nix-shell rebase completed with exit 0. Logs:
`generic-mail-fix-commit.log`, `test-db-compat-commit.log` and
`generic-mail-consolidation.log`. The test-environment commit's message-width
hook issued advisory 72-column warnings; every line satisfies the workspace
80-column maximum and the hook passed. Tracked tree/index are clean; only the
pre-existing `webui/.phpunit.cache/` is untracked.

Lead retains independent app/source clearance and direct prose acceptance.
The same retained reviewer will assess only the new test-environment/history
change through the applicable bounded lanes. No new push or guest runtime is
authorized before that clearance. The original integration run remains queued
at the last observed checkpoint; no scenario pass is claimed.

## Exact check and input receipts

Corrected-source metadata is `vpsadmin-corrected-flake-metadata.json`, including
the complete locked input graph. It identifies revision
`4d72e3e754fd47b598de1e54e05b3c5d26c62200`, source path
`/nix/store/z81haclmc5xbb3p0m2fxfym5x0w9s5qp-source`, NAR hash
`sha256-UMUwSBHp6HqMYC4ucoDAvOiuQEJesYhqgGWVK9HPc1g=`. `flake.lock` is unchanged
from the original published head. The older realized build's complete store
reference/NAR graph is `local-old-head-build-store-graph.json`; it is bound only
to its original test JSON outputs, not to the corrected head.

`mariadb-11.8.6-default-source.txt` retains the exact official source URL,
complete-source SHA256 and extracted default declaration. Hosted package
version and original failures remain in the downloaded attempt-1 logs and
native JSON; they were not replaced by corrected local results.

The fresh helper batch ran from the repository root for `MODE=none` and then
`MODE=all`:

```sh
VPSADMIN_PLUGINS=MODE nix develop .#api -c bundle exec rspec \
  spec/models/mail_templates_spec.rb \
  spec/models/cluster_resource_adjustment_concurrency_spec.rb \
  spec/models/ip_ownership_concurrency_spec.rb \
  spec/models/ip_assignment_owner_concurrency_spec.rb \
  spec/models/ip_release_concurrency_spec.rb \
  spec/models/operations/authentication/mfa_factor_concurrency_spec.rb \
  --format documentation --format json --out <tracking>/test-db-compat-MODE.json
```

`test-db-compat-commands.txt` preserves the exact executed shell invocations,
including absolute artifact paths and exit capture. Native core results:
seed 29034, 36.92 seconds for examples; full: seed 18986, 38.78 seconds. Each
ran 64 examples with no failures, pending examples or outside-example errors.
The watcher elapsed times include shell/schema startup and native cleanup.

The mail correction batch used the same Nix API shell, core mode, with:

```sh
bundle exec rspec spec/models/mail_templates_spec.rb \
  spec/models/transaction_chains/vps/oom_policy_mail_spec.rb \
  spec/models/transaction_chains/incident_report/new_spec.rb \
  spec/models/transaction_chains/incident_report/send_spec.rb \
  --format documentation --format json --out <tracking>/generic-mail-fix-specs.json
```

The OFF/ON control selected only
`spec/models/cluster_resource_adjustment_concurrency_spec.rb[1:1]`, using
`VPSADMIN_PLUGINS=none nix develop .#api -c bundle exec ruby -I spec -r spec_helper`.
Its Ruby program prints `SHOW VARIABLES WHERE Variable_name IN (...)` for the
version/isolation/snapshot values, then calls `RSpec::Core::Runner.run` with
that exact example ID and documentation/native JSON formatters. OFF used the
fresh server's unmodified defaults. The ON diagnostic inserted only these two
statements before the query/runner:

```ruby
ActiveRecord::Base.connection.execute('SET GLOBAL innodb_snapshot_isolation=ON')
ActiveRecord::Base.connection.execute('SET SESSION innodb_snapshot_isolation=ON')
```

The ON failure was intentional cause isolation, not accepted verification. All
control databases were created by the existing automatic helper and cleaned
through its native exit handlers. The subsequent six-file pass used the actual
corrected startup flag without manual SQL settings.

Stop and investigate any unexpected local kernel build. Preserve the first real
failure's logs/effects and diagnose before any retry. Do not duplicate equivalent
hosted successful scenario runs, clean foreign state, lower fixture resources or
perform production operations.
