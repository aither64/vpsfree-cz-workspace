# P3 two-worker smoke and dependent consumer evidence

## Current accepted verification summary

Fourth smoke passed at actual tested **8d5093e3d65f561dd305898074dd8add5e49323e**:
three Alpine images,45 existing image tests, both tar/zfs formats, three durable
verified receipts and a sealed run view. Two VMs overlapped; worker0 reused its
VM and builder for the third assignment. All acknowledged scratch payloads and
owned worker processes/disks/sockets were absent after native completion.
[Exact source/digests/HTTP hashes](artifacts/p3-successful-smoke-proof.json).

Dependent r3 consumer passed **status0**,1test/1example in240.24s,
23:05:19–23:09:19UTC: normal common readiness/new-daemon settings, sealed guest
HTTP and exact tar hash, loaded release3.24.4, one-action runtime install/default
assertion/firstfetch, missing-tuple failure and explicit/default repository
persistence across same-pool export/import. [Consumer proof](artifacts/p3-consumer-r3-acceptance-proof.json)
and [seven canonical access events](artifacts/p3-consumer-r3-access.jsonl) retain
actual commands, bytes and receipt identities. Native QEMU exited0; no owned
QEMU/virtiofs/sockets remain. Retained32GiB sparse tank.img allocates55099392bytes;
no operator cleanup, service stop or session lifecycle action occurred.

Published final **fab23ed26aefaed635c41cdb89ff30bf82632c61** differs only in
COMPAT generator style. [Scoped source/input proof](final-source-identity.md)
and [fresh final service/OSVM builds and binary proof](artifacts/final-packages-acceptance.json)
support reuse within their stated limits; executions remain labelled8d509,
without whole-machine closure equality. [P3 packet](p3-implementation.md) has
exact derivations, post-package capacity and retained historical failures.

Limits: one externally admitted8192MiB/2CPU consumer; standalone JSON scheduler
resource accounting remained zero. No ordinary scheduler, full CI, publication,
production SSH/admission or speedup claim. Lead tracks independent full CI and
overall acceptance. All following sections are historical checkpoints; pending
preparation/amend/launch wording is superseded, not a request to execute it.

## Historical fourth preparation

Source `8d5093e3d65f561dd305898074dd8add5e49323e`, tree
`07cfd04ee3f9ee86167fad88b9dc79b4e5d4c397`, is clean. Fourth fresh root
`/tmp/p3-smoke-8d5093e3d65f` is prepared with the original three-image plan,
strict producer adapter, current SHA/root/run-ID status wrapper, expected worker
JSON, source/lock/AssignedConfig hash manifest and six verified checksums.
Shell syntax passes; watcher inputs/links are untouched. No build/VM ran here.
Actual worker JSON remains 8192 MiB, cpus=2/cores=2/threads=1/sockets=1.

Canonical exact-revision receipt `artifacts/p3-permissions-final-eval.{json,log,status}`
records unchanged service pqw1..., OSVM bnfx5z22hydz3zf1yqc0by7gr65dddnx and
worker 8sl0xwj81qf1r1xs3ylaw36x2x2w5r7b derivations. Full identities are in
preparation.json. Lead must realize changed closures and verify installed
permission code before registering this root's run-driver.sh with a new loopback
URL/service/producer.sock. Retain actual realized identities if local --file
context differs. All three failed roots/receipts/services stay preserved.
Third attempt booted and reused workers but failed mapped-builder setup with
runner permission denied (exit 126); it was not a preboot/kernel failure.
No verified-image/test/seal acceptance is claimed. Conditions below still apply.

## Third fresh preparation after topology fix

Current source `d741d88408a589c745e98c7809972a8323af0c31`, tree
`3f9061f384626fa8ab768710df38da4dab1be085`, is clean. The checked topology
correction is folded into P3 with unchanged service/COMPAT parents; the focused
actual-JSON/parser/QEMU test passed two examples before the amend. Third root
`/tmp/p3-smoke-d741d88408a5` is fully prepared, not launched. Both failed roots,
run receipts and registered services remain preserved.

Canonical git+file evaluation pinned to that exact revision passed, recording
`artifacts/p3-topology-final-eval.{json,log,status}` and source path
`/nix/store/xc9i6acsn7f3vb38xgpgqkypiqmczzvx-source`. Derivations:

- Service: `/nix/store/pqw1r6h689y75phgsdbb490lqybxnvsn-osctl-repo-server-26.05.drv`, unchanged.
- OSVM: `/nix/store/clgwj3xgkdikabgx82fcijscfl1rkabn-osvm-26.05.0.drv`.
- Worker: `/nix/store/mhyk51f8ixl61wiyj7a3l2iw5yap3kra-os-test-image-pipeline-worker.json.drv`.

The actual `expected-worker.json` has cpus=2, cores=2, threads=1, sockets=1;
the checked QEMU rendering is `-smp cpus=2,cores=2,threads=1,sockets=1`.
No silent expansion to four CPUs. Lead's fresh watcher must realize the changed
worker/OSVM outputs and bind current input metadata before registration/launch.

Fresh files are source-plan.json, plan.json (same three original Alpine entries,
tags/order/defaults and exact scoped dependencies; GC []), expected-worker.json,
bin/ssh, run-driver.sh, preparation.json and prepared.sha256. The manifest binds
full source/tree/lock, canonical source path and derivations. All six checksums
and both shell syntax checks pass. Producer adapter and atomic-status wrapper
use only this third root and unique run ID; watcher-owned inputs.json and
worker-config/osvm links were not created or overwritten by preparation.

Later registered command, after source/cache/build and immediate capacity checks:

```sh
bash /tmp/p3-smoke-d741d88408a5/run-driver.sh http://127.0.0.1:CHOSEN_PORT
```

Producer socket must be `/tmp/p3-smoke-d741d88408a5/producer.sock`, backed by new
disposable service state. Acceptance and stopping conditions below still apply.
No build/guest/service action ran during this preparation.

The second attempt at f2ba098c also failed before guest boot: every worker's
console records invalid CPU topology (4 cores versus admitted 2 CPUs), QEMU
exited 1, and stream closure followed during cleanup. Exact owned worker disks,
sockets and processes were reconciled absent; other host resource use is not
attributed to this run. Both failed roots/receipts and registered repositories
are preserved. The minimal pending closure fix sets cores=cpus, threads=1,
sockets=1 alongside the existing admitted cpus count. No shared defaults or
stream-error semantics change. An actual evaluated-JSON/parser/QEMU regression
for 2 and 3 CPUs awaits one lead-owned watcher run; its Nix subprocess has a
120-second deadline after the original 45-second evaluation timeout. No repeated
inline evaluation, guest retry or success claim is made.

After the three-image/two-worker smoke succeeds, the next dependent local check
is common repository readiness on an updated daemon: runtime pool install plus
first fetch in one shell action, sealed three-image URL reachable through the
user-network host endpoint, actual payload/hash proof and preservation of an
explicit repository fixture. Lead chooses the bounded command then; it is not
implemented or run by this CPU-fix package. Actual-runner full CI stays P0-blocked.

Owner: implementer0; lead authorizes the next batch and assigns a fresh watcher.
First-attempt source: `ffe83296d682a72076f942c5b6b10dd480a71b36`.

The lead realized worker config (108s), OSVM (9s) and input metadata, then
registered the disposable Go service on loopback port 19481 and the driver.
The driver naturally exited 1 almost immediately; driver.status is 1, verified
is empty, image-5/-6/-7 failed unbound at attempt 0, and no URL was emitted.
Producer result receipts identify `KeyError: key not found: "network"`.
No qemu/virtiofs process was observed; this is not guest boot/runtime acceptance.
All first-attempt artifacts and service state remain preserved. Do not reuse
`/tmp/p3-smoke-ffe83296d682` or its run identity, stop services, or relaunch it.

Diagnosis: ImageBuildWorker replaced network opts with only hostForward=nil.
MachineConfig accepts opts wholesale rather than merging its defaults;
UserNetwork's deferred QEMU rendering then requires missing network/host/DNS.
The bounded source fix omits opts to use canonical complete user-network defaults
with no forwarding. Share assembly already matches sharedFileSystems' string
map and retains separate exports/source read-only guest mount. A real parser,
machine-construction and QEMU-rendering regression covers two workers without
starting VM processes or guest commands. Lead assigns fresh state only after
the fixed source is committed and its derivations/cache plan are reconciled.

## Fresh preparation after the network fix

Fixed source: `f2ba098c707b416c356f4af00723f0b82c3bc93a`, clean worktree/index.
Fresh root: `/tmp/p3-smoke-f2ba098c707b`; its original source-plan, three-image
plan, producer adapter, driver wrapper, preparation manifest and SHA-256 receipt
are prepared and statically checked. IDs/order/tags/defaults/dependencies/GC and
resource/capacity gates match the first fixture, while every root/source/run ID
in the wrapper and adapter is bound to this fresh attempt. Old artifacts were
not overwritten. Watcher-owned inputs.json and worker-config/osvm links are absent
until the lead's realization step supplies them.

Post-fix pure identities: service remains
`/nix/store/pqw1r6h689y75phgsdbb490lqybxnvsn-osctl-repo-server-26.05.drv`;
OSVM changes to `/nix/store/8zx63k3jlfyb7841h2r4pjc56mqbxcyw-osvm-26.05.0.drv`;
worker changes to
`/nix/store/52mfm4x3ifwbd3f71ipiqqjiqrkc2s7w-os-test-image-pipeline-worker.json.drv`.
The prior worker realization does not apply. Lead must inspect the new cache
plan/realize the changed outputs before registering the next driver. Later command:

```sh
bash /tmp/p3-smoke-f2ba098c707b/run-driver.sh http://127.0.0.1:CHOSEN_PORT
```

Its service socket must be `/tmp/p3-smoke-f2ba098c707b/producer.sock`, with new
service data and registered ownership. Logs/status are fresh-root driver.log and
driver.status. No service/VM was launched during this preparation.

Realization/provenance gate now passes: lead realized worker output 861yg... from
exact 52mfm... drv and OSVM output xy4sism... from canonical lcp0c2... drv. The
previous 8zx... was a different local-path evaluation context; current canonical
`nix eval --raw .#osvm.drvPath` returns the realized lcp0c2... identity. Actual
installed worker source matches current f2ba098c byte-for-byte and contains the
network fix. Prepared hashes, clean source, input metadata revision/lock and links
verify. [Provenance receipt](artifacts/p3-smoke-provenance.json). Ready for the
lead's registered retry; no build, VM or service action ran in this reconciliation.

## Prepared local artifacts

The following artifacts describe the preserved first attempt, not a retry.
The root and executables are mode 0700, plan/manifests mode 0600.

- `source-plan.json`: exact source plan evaluated from the clean pinned checkout.
- `plan.json`: original image-5/order 5/alpine-3.22, image-6/order 6/alpine-3.23,
  image-7/order 7/alpine-3.24; only .24 has original latest/stable tags. Original
  defaults retained, GC [], three exact Alpine version/minimal/x86_64 dependencies.
- `preparation.json`: source SHA/tree, source flake.lock SHA-256, package identity,
  resource fixture and explicit watcher ownership of inputs/links.
- `prepared.sha256`: hashes source plan, fixture plan, preparation manifest,
  adapter and wrapper; verification passed.
- `bin/ssh`: strict four-argument local-producer adapter to the exact built
  service package's `ctl --socket /tmp/p3-smoke-ffe83296d682/producer.sock`.
  Unexpected flags/targets exit 64. Stdin/stdout/process status pass through;
  no role field/API, publisher/admin socket or guest credential exposure.
- `run-driver.sh`: later registered parent command accepts one explicit loopback
  URL. It writes complete `driver.log` and atomic numeric `driver.status`,
  preserving the engine's exit status. It refuses existing log/status/run state,
  wrong/dirty source, changed preparation hashes, missing watcher inputs/links or
  missing producer socket. Immediately before the normal engine command, it
  requires >=64 GiB filesystem space, >=20 GiB shm, >=24 GiB available RAM and
  readable/writable KVM. It captures runtime input hashes/closure paths separately.

Both scripts passed `bash -n`. Exact plan membership/defaults were compared with
the complete source plan. No `inputs.json`, `worker-config` or `osvm` link was
created or overwritten; the lead's fresh watcher owns them. No application source
changed. Lead will register the Go service and this parent command after accepting
the realization/source/cache receipts:

```sh
bash /tmp/p3-smoke-ffe83296d682/run-driver.sh http://127.0.0.1:CHOSEN_PORT
```

The lead supplies a verified unprivileged loopback port and supervises the
registered process group. A forced kill that prevents the EXIT trap leaves the
status absent and must be reported incomplete, never inferred successful.

Pre-realization wiring correction: the lead's worker dry-run passed at previous
source `2120ec2de70b9daa38588a8ad79a8296ec3e6167`
(44 small userspace/gem/system/squashfs derivations and five tiny fetches,
no Linux kernel build), but `.#osvm` was absent from flake package exports.
The assigned minimal fix adds `osvm = pkgsWithOverlays.osvm;` to flake.nix,
reusing the existing current-source package. Attribute evaluation now passes:
`nix eval --raw .#osvm.drvPath` returns
`/nix/store/qygdvcyzfcnw1dy88yic0hrbqb0ksd0q-osvm-26.05.0.drv`.
Logs/status: [artifacts/p3-osvm-export-eval.log](artifacts/p3-osvm-export-eval.log),
[status](artifacts/p3-osvm-export-eval.status). The one-line fix is folded into
the new source above; service and COMPAT parents are unchanged. Post-amend service
drvPath is the same successfully realized
`/nix/store/pqw1r6h689y75phgsdbb490lqybxnvsn-osctl-repo-server-26.05.drv`;
post-amend OSVM drvPath matches the one above. No realization ran. Bind the next
worker cache/closure/input receipts to the exact new revision before smoke.

The corrected function evaluation at the previous source passed (exit 0 within
the 45-second limit):

```sh
timeout 45s nix eval --impure --raw --expr '(import ./tools/image-pipeline.nix { memoryMiB=24576; cpus=2; diskSize="32G"; }).drvPath'
```

Result: `/nix/store/wqx2n31bcyd9iaf3jphb65arzq96rzp9-os-test-image-pipeline-worker.json.drv`.
[p3-worker-eval.log](p3-worker-eval.log), [status](p3-worker-eval.status).
Those resource values were evaluation fixtures only. No retry was needed.

## Local observation and proposed admission

Read-only local aitherdev observation: 64 CPUs; 96,537 MiB RAM total,
76,471 MiB available; no swap. Root filesystem had 145 GiB available.
`/dev/shm` had approximately 48 GiB capacity, only 168 KiB used.
`/dev/kvm` was readable/writable by this user; no qemu/virtiofs processes were
observed (pgrep exit 1 means no matches). These observations are not reservations
or production-runner admission. Recheck before launch and account for other jobs.

Propose two workers, each 8,192 MiB / 2 CPUs / 32 GiB sparse disk; aggregate
admission 16,384 MiB / 4 CPUs. Their virtiofs memory backing consumes about
16 GiB of /dev/shm, leaving substantial headroom; two 24 GiB evaluation fixtures
would approach/exceed the current mount limit. Reserve host/service/export/cache
headroom separately. If free filesystem space falls below 64 GiB or /dev/shm
below 20 GiB, do not start this batch. These are conservative smoke bounds,
not measured weekly-run settings. P0's actual-runner/production blockers remain.

## Source/cache preparation, then one smoke

Run from the feature worktree. Require HEAD to equal the source above and no
application changes. Lead assigns one fresh watcher per related long batch,
with logs/status under this session. First inspect the exact realization plan:

```sh
nix build --dry-run --impure --file tools/image-pipeline.nix --arg memoryMiB 8192 --arg cpus 2 --argstr diskSize 32G
nix build --dry-run .#osvm
```

Stop and report if a kernel would build locally; inspect cache/input provenance
before authorizing realization. After the lead accepts that plan, build the same
worker expression with `--out-link "$SMOKE_ROOT/worker-config"` and OSVM with
`--out-link "$SMOKE_ROOT/osvm"`. Keep SMOKE_ROOT outside the source checkout.
The guest and host gems use current-source overrides in os/overlays/osctl.nix;
do not substitute older packaged source merely because its version is identical.
Save `nix flake metadata --json`, source/closure identities and realization logs.

Use the already built exact-final service package:
`/nix/store/g4434b8c720bhdjgcxs2ygfh1z7qfqxl-osctl-repo-server-26.05`.
Start a disposable service only through `dev-session service run`, with its own
registration, root, sockets and loopback HTTP port. The lead supplies the verified
registered-service invocation. No production service/data/credentials are used.
Suggested finite fixture flags (all sizes in bytes):

```text
serve --root $SMOKE_ROOT/service --listen 127.0.0.1:$SMOKE_PORT
--repository vpsadminos --instance p3-smoke
--producer-socket $SMOKE_ROOT/producer.sock
--publisher-socket $SMOKE_ROOT/publisher.sock --admin-socket $SMOKE_ROOT/admin.sock
--max-bytes 8589934592 --reserve-bytes 68719476736 --max-upload-bytes 2147483648
--max-runs 4 --max-lease 2h --export-lease 1h
--access-log $SMOKE_ROOT/access.jsonl --access-log-max-bytes 10485760
--access-log-files 2 --stats-days 2 --stats-max-rows 1000 --event-queue 128
```

No public baseline is required for this targeted smoke. Derive a fixture plan from
the exact source plan: retain configured `alpine-3.22`, `alpine-3.23`, `alpine-3.24`
items with their original IDs/order/tags/defaults, require those three exact
vpsadminos/minimal/x86_64 Alpine versions, and set fixture GC to []. Assert all
three configured entries exist. This explicitly scoped dependency view is not a
full-CI-ready claim; the full plan must retain all suite requirements. Three
images on two workers prove reuse. They use the existing Fedora 44 builder;
public bootstrap fetch plus upstream Alpine downloads remain explicit network
dependencies. No Guix/Gentoo build is needed for this first smoke.

Use the actual Control/Coordinator/ImageBuildPool/ImageBuildWorker engine. A
host-only disposable `ssh` shim in a private PATH can recognize only the exact
`local-producer` target and the fixed Control flags, then execute the service
binary's `ctl --socket "$SMOKE_ROOT/producer.sock"` unchanged. Fail any other
arguments. Unset IMAGE_SSH_KNOWN_HOSTS for this local fixture, forward stdin/
stdout/status verbatim, and expose no publisher/admin socket through the shim.
This is a test transport adapter, not a product interface or production SSH proof.
The shim, receipts and sockets stay outside the guest's source/exports shares.

The watcher runs the normal driver (variables resolve to the paths above):

```sh
"$SMOKE_ROOT/osvm/bin/osvm" script tools/image-pipeline.rb \
  --machine-config "$SMOKE_ROOT/worker-config" --plan "$SMOKE_ROOT/plan.json" \
  --source-dir "$PWD" --state-dir "$SMOKE_ROOT/run" \
  --workers 2 --max-memory-mib 16384 --max-cpus 4 \
  --producer local-producer --url "http://127.0.0.1:$SMOKE_PORT" --images all \
  --run-id local-p3-smoke --attempt 1 --event workflow_dispatch \
  --ref refs/heads/2026-11-04-container-image-build-pipeline \
  --input-graph "$SMOKE_ROOT/inputs.json" --lease-seconds 7200
```

## Acceptance and stopping boundary

Retain run.json, producer request/responses, all assignment/result/command logs,
worker shell/console logs, input graph and closure/source identities. Require
three verified receipts, one sealed targeted URL, exactly two worker identities,
overlapping build/test intervals, and a second assignment on an existing worker.
Inspect builder creation/setup logs for reuse rather than inventing a timing claim.
Confirm all assigned sources/digests/tuples/formats, no retained test CT/build
children after each assignment, and acknowledged scratch removal. Fetch sealed
INDEX plus one archive/stream and compare bytes/hash to its verified receipt.

Stop/report on the first kernel build, wrong bytes/source/tuple, unexpected
authority, cleanup uncertainty, or resource-bound breach; no watcher retries or
optional expansion. The engine's recorded one worker replacement retry is part of
its contract. Lead sets the batch deadline after cache planning; network/setup
time is unmeasured. This smoke does not prove mixed-failure publication, full CI,
production SSH or P0 runner admission. Session/service lifecycle actions remain
separately authorized; completion does not authorize stopping this session.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-04-container-image-build-pipeline/)
