# P3 implementation evidence

Owner: implementer0. Bounded producer/consumer verification completed; lead owns overall acceptance, review and integration.

## Current accepted verification summary

Actual producer and consumer executions are pinned to **8d5093e3d65f561dd305898074dd8add5e49323e**.
Published final source is **fab23ed26aefaed635c41cdb89ff30bf82632c61**; its only
source delta is the COMPAT generator style correction (3 additions/2 deletions).
[Source/input proof](final-source-identity.md) records unchanged P3/framework/daemon
bytes and lock graph plus the identical runner derivation. These executions are
not relabelled as final-head runs; no whole-machine closure equality is claimed.

The fourth two-worker smoke passed driver status **0**: image-5/-6/-7
(Alpine3.22/3.23/3.24),15 existing tests each, all45 passed, durable verified
tar+zfs receipts and a sealed run view. Worker0/image5 (22:20:47–22:29:07UTC)
and worker1/image6 (22:20:49–22:29:22UTC) overlap; worker0 then handles image7
(22:29:12–22:35:14UTC) in the same VM/builder CTID, without a second builder
setup. This proves concurrency, VM reuse and builder reuse, without a speedup claim.
All six acknowledged scratch exports and owned worker disks/sockets/processes
were absent after native completion; no operator cleanup occurred.
[Smoke proof](artifacts/p3-successful-smoke-proof.json) retains source/config
digests, three verified response paths and HTTP size/hash matches: INDEX831bytes;
Alpine3.24 tar9790464bytes SHA256`c802f7e739a4cc581847aa109738520c3a0acdc8122793df1723903ab452ac1b`;
zfs10012672bytes SHA256`9702858a9279155f991ec4985efbac1ff9bded616be831fb6a93ff788792ff07`.

The dependent r3 consumer also passed driver status **0**,1test/1example,
240.24s total (23:05:19–23:09:19UTC; recovery observer120s is not test duration).
Normal evaluator/common-module readiness supplied the sealed URL and evaluated
new-daemon setting. Fresh-cache/endpoint-only guest egress, canonical tar hash,
loaded Alpine release **3.24.4** in both ordinary and runtime containers,
**one shell action** installing runtime pool/asserting its default/firstfetch,
missing-tuple failure, and distinct default plus disabled explicit repository
preservation through the same pool's export/import all passed.
[Consumer proof](artifacts/p3-consumer-r3-acceptance-proof.json) retains exact
shell blocks, hashes, lease/source/generation and [seven access events](artifacts/p3-consumer-r3-access.jsonl),
including two canonical ZFS GETs (tank and runtime firstfetch) of10012672bytes.
Native QEMU exit0; no owned QEMU/virtiofs or sockets remain. Retained r3 tank.img
is32GiB sparse/55099392 allocated bytes; files and services remain open.
Post-package snapshot: disk115559497728bytes/shm37190111232bytes available,
RAM65440120KiB available. No operator cleanup was performed.

The consumer used lead-approved external admission for one8192MiB/2CPU VM;
the standalone JSON entry point's zero scheduler resource accounting is recorded,
not treated as ordinary scheduler/production-capacity acceptance. Producer
full-CI dependency coverage, production SSH/admission, publication, performance
and full-CI runtime acceptance remain outside these bounded results. Full CI is
tracked separately by the lead; no blanket success is inferred here.

Final service/OSVM packages were freshly built at fab23 in211s, exit0:
service drv`xjb3rcq192kg3b5pyfy98j4629xgcp4m`,output`xqg8733plf4y28nvav4s4376y9xi006i`;
OSVM drv`c3aaprivwjqaqp2br07aww92crxx775b`,output`5rpgj050bvvq9k5njwm1ckkzsc6d2xi9`.
[Final package receipt](artifacts/final-packages-acceptance.json) records full paths
and service binary SHA256`0412a98d8f5e00913112f71f432c1225739e549bbf5722c27c5bc7012f162a8c`,
identical to the actual smoke service binary. The pinned runner is
`/nix/store/1a0gnrc2i2im69779823b6i030dr6l8c-test-runner`,drv`gf2m6b4g511rdvq25jssg8f1i4v52c7s`.

All sections below are historical checkpoints, preserving failures and actions
as recorded then. Their pending/amend/preparation instructions are superseded
by this summary and are not outstanding launch or source-change requests.

## Historical postreview verification continuation

The assigned copied-tree permission fix is now folded into current P3 head
`8d5093e3d65f561dd305898074dd8add5e49323e`, tree
`07cfd04ee3f9ee86167fad88b9dc79b4e5d4c397`. Previous d741d884 is retained at
`refs/backup/2026-11-05-p3-assigned-permissions-d741d8840`. Exact old/new diff is
only AssignedConfig and its focused spec (22 insertions, one deletion). The
original P3 message is byte-identical; normal Nixfmt/RuboCop hooks passed.
Parent/COMPAT remains 39f7e737 and service remains 463704f2, unchanged in content.
Commit completed before worktree/index clean proof and window release. Receipt:
`artifacts/p3-permissions-amend.log`. Fourth preparation root is
`/tmp/p3-smoke-8d5093e3d65f`, entirely separate from all three failed roots.

Fourth preparation is complete: six hashes/shell syntax pass, exact source plan,
private producer-only adapter/status wrapper and expected-worker JSON, plus fixed
AssignedConfig source hash for installed-code proof. Canonical git-revision eval
passed with unchanged service pqw1..., OSVM
`bnfx5z22hydz3zf1yqc0by7gr65dddnx-osvm-26.05.0.drv` and worker
`8sl0xwj81qf1r1xs3ylaw36x2x2w5r7b-os-test-image-pipeline-worker.json.drv`.
Actual JSON has 8192 MiB, cpus=2/cores=2/threads=1/sockets=1. Receipt:
`artifacts/p3-permissions-final-eval.{json,log,status}`. No realization/VM,
watcher-output overwrite or failed-root reuse. Lead owns fresh realization and
registered retry; [current smoke boundary](p3-two-worker-smoke.md).

Authoritative terminal evidence supersedes the third attempt's earlier boot-only
snapshot: it naturally exited 1 at 21:58:15.303284Z after about 6m45 from launch,
with three bound attempt-1 failures, no verified images/tests/seal. The workers
did boot, come online, capture configs and run Fedora builder setup concurrently;
worker-0 then took image-7, proving VM reuse. Every command.log records `env:
'/build/basedir.<id>/bin/runner': Permission denied`, builder setup exit 126.
Actual cause: the assigned private scripts copy retained mktmpdir's 0700 root,
while Builder::Create bind-mounts it with map_ids:false for a mapped builder UID.
No host/kernel blocker is established. Exact owned QEMU/virtiofs processes and
worker image/socket files were reconciled absent after natural exit; no operator
cleanup or foreign-state action occurred. Both earlier failed roots and third
failure receipts/services remain preserved.

Approved narrow permission fix changes only AssignedConfig plus its focused
spec. The private copied tree uses `u+rwX,go=u,go-w`, granting mapped-UID
read/traverse and executable access without group/world write. The regression
showed Ruby FileUtils X covers directories only: go+rX leaves a private 0700
runner at 0744, so copying owner bits before removing go-write is required.
Original source/host share is untouched. The capture fixture now makes root,
nested directories and runner/test private, static config/build/test files 0600;
it checks copied access/no-go-write, unchanged original modes/content, and
actual build/test wrapper sourcing across rollover/auxiliary data/retry twice.
AssignedConfig+CLI 33 examples pass, scoped two-file RuboCop/whitespace pass.
Logs: `artifacts/p3-assigned-permissions-{spec,lint}.log`. Source is unstaged
pending its short amend window; no realization/VM/root reuse occurred.

One lead-requested diagnostic snapshot of the third running attempt was taken at
2026-11-05 21:55:29 UTC (launch 21:51:29, four minutes, not the watcher's unsupported
15-minute statement). Only exact-root worker console/shell logs were read:
worker-0 and worker-1 consoles were 320 bytes, last modified 21:51:33 UTC,
ending in SeaBIOS/iPXE `Booting from ROM...`; shell logs were empty since 21:51:32.
No explicit fatal error, Linux boot, guest shell or image-build stage was proven.
A single exact-root process snapshot found live QEMU PIDs 4039452/4039457 under
driver PID 4039156, correct two-CPU argv and explicit kernel/initrd/ttyS0/init,
plus each guest's three virtiofs launchers and three servicing processes.
Owned VM effects therefore remained live, without evidence of build progress.
No driver log/status polling, guest commands, source changes, signals or
lifecycle actions occurred; diagnosis stopped and watcher ownership remained.

A second explicitly bounded source/input comparison at 21:59:25–22:00:37 UTC
found no concrete missing boot field. The realized worker's kernel/initrd,
toplevel/squashfs and append/ttyS0 shape match the existing OSVM and repository
builder seam; the ordinary image test uses the same base/tank/channel setup
(with 24 GiB memory). Kernel is a valid Linux x86 bzImage 6.12.113 and initrd is
Zstandard data. Test-shell is enabled, and virtserialport maps to the same
org.osvm.shell0 device supplied by the driver. Existing argv has no QMP endpoint.
This does not establish a host/kernel defect or successful Linux boot. No process
re-poll, guest command, new debug endpoint, baseline VM or source change occurred.
The lead was advised to retain the native 900-second boot deadline and watcher;
after a real native failure, a separately authorized ordinary direct-OSVM
baseline using existing artifacts can isolate orchestration from the shared
boot/runtime path. No quiet-output cancellation or speculative fix is justified.

The corrected topology check passed (two examples / zero failures, exit 0 in
55s) in the lead's fresh watcher, with
`artifacts/p3-topology-context-spec.log/status` and topology-context-watch-result.txt.
The five-line closure fix and 26-line regression are folded into current P3 head
`d741d88408a589c745e98c7809972a8323af0c31`, tree
`3f9061f384626fa8ab768710df38da4dab1be085`. Parent/COMPAT remains
`39f7e73746d0157bdd8b734a76d13f9b974b7890`; service remains
`463704f2046b1a888ae18777ba4932e9d118872e`. Exact previous f2ba098c-to-new
diff contains only tools/image-pipeline.nix and image_build_worker_spec.rb,
31 insertions total. Backup ref
`refs/backup/2026-11-05-p3-worker-cpu-f2ba098c7` retains the failed-attempt source.
Existing commit message is byte-identical, normal Nixfmt/RuboCop hooks passed,
and command completion preceded clean worktree/empty-index proof and release.

The first amend stopped before commit for a stale stored Overcommit config
signature. One owned unstage took effect before the index hook refused too.
The actual .overcommit.yml was read and proved unchanged from HEAD, then normal
overcommit --sign restored its signature without bypass. The remaining owned
entry was unstaged and empty index verified before release; the lead allocated a
fresh retry window. No source/check changes or repeated sign loop occurred.
Successful receipt: `artifacts/p3-topology-amend-retry.log`; first refusal:
`artifacts/p3-topology-amend.log`.

Post-release canonical git+file evaluation pinned to the new revision passed
within the 45-second bound, yielding unchanged service pqw1..., OSVM
`clgwj3xgkdikabgx82fcijscfl1rkabn-osvm-26.05.0.drv` and worker
`mhyk51f8ixl61wiyj7a3l2iw5yap3kra-os-test-image-pipeline-worker.json.drv`.
Full paths/source context and actual worker JSON are in
`artifacts/p3-topology-final-eval.{json,log,status}`. The embedded worker has
cpus=2, cores=2, threads=1, sockets=1, matching the regression-proven QEMU argv
`-smp cpus=2,cores=2,threads=1,sockets=1`. This fixes the concrete startup
invariant without expanding the admitted CPU budget.

Third entirely fresh root `/tmp/p3-smoke-d741d88408a5` is prepared with original
three Alpine IDs/order/tags/defaults, scoped dependencies/GC [], exact-source plan,
expected-worker JSON, private producer adapter and current-source/root/run-ID
atomic-status wrapper. Source/tree/lock/canonical source path/derivations are
bound by preparation.json and six hashes; all hash/syntax checks pass. No
watcher-owned input metadata or links were overwritten. Both failed roots and
services remain. See [current launch boundary](p3-two-worker-smoke.md).
Lead owns fresh realization and later registered smoke; no build/VM ran here.

The second real smoke at f2ba098c failed, with no verified images/sealed URL.
All three worker console logs identify QEMU's explicit invalid topology:
cores(4) * threads(1) * sockets(1) differs from maxcpus(2). QEMU exited 1 before
guest boot; generic `IOError: stream closed in another thread` is the subsequent
stream cleanup symptom, not an established host-permission/environment failure.
Exact owned workers have no surviving QEMU/virtiofs, image disks, socket entries
or osvm-images directories. Their virtiofs logs record disconnect/shutdown.
Concurrent host resource changes were not attributed to this run; no cleanup or
foreign-state action was taken. Both failed attempts and service records remain.

The approved bounded correction adds five lines to tools/image-pipeline.nix:
qemu.cpu cores=cpus, threads=1, sockets=1. It preserves the resource-admission
CPU count without global defaults or shared error-semantics changes. The worker
spec evaluates actual closure JSON for 2 and 3 CPUs, parses it with MachineConfig
and renders QEMU -smp, asserting both the count and topology product. No guest.
Nixfmt, scoped RuboCop and whitespace checks pass. The first combined JSON eval
timed out at 45s, exit 124, with only an interrupt diagnostic; no app failure or
kernel build is claimed. Lead approved only this test's timeout increase to
120 seconds and one fresh watcher execution (expected 1–2 minutes, escalation
at 3 minutes). Source remains unstaged until the check proves the correction.
Initial logs: `artifacts/p3-worker-topology{.json,-eval.log,-eval.status}`.
The exact pinned-Ruby command was sent to the lead; no inline rerun occurred.

That watcher run finished with exit 1 (not timeout): Nix builtins.fromJSON rejects
the generated worker JSON's store-path string context. This is a test-expression
error, not product behavior. Original `artifacts/p3-topology-spec.log/status` and
topology-watch-result.txt remain intact. The bounded correction returns the actual
derivation.text values through `nix eval --json` and parses those JSON texts in
Ruby, preserving the same real MachineConfig/QEMU assertions without changing
product semantics or discarding context unsafely. Scoped lint/whitespace checks
pass. One fresh watcher rerun was requested with separate
`artifacts/p3-topology-context-spec.log/status`; no inline repeat, staging or guest
action was performed. The five-line product topology candidate is unchanged.

The first real-engine smoke at ffe83296d failed before guest boot. Lead's worker
and OSVM realizations passed, but all three selected items failed unbound at
attempt 0 with `KeyError: key not found: "network"`. run.json has no verified
items and URL null; driver.status=1. The original root, registered services and
receipts are preserved; no retry/stop/reuse was performed by this owner.

Bounded diagnosis used the actual realized worker JSON and current MachineConfig
constructor/network renderer. `opts` replaces canonical defaults; the worker's
partial hostForward-only opts therefore omitted network/host/DNS. The minimal
fix uses `{type: user}` without opts, preserving no-forwarding user networking.
The sharedFileSystems map is already valid and deliberately discards inherited
host shares. A new ImageBuildWorker spec constructs two actual machines through
the canonical parser and renders QEMU argv while stubbing only runtime/guest
operations. It verifies default network values, unique MAC/state/disk/socket/
shared-dir paths, isolated exports, no inherited path/host ports, unchanged input
JSON and source read-only/export writable mount commands. Worker + pool focused
checks: three examples pass; scoped two-file RuboCop and whitespace checks pass.
Logs: `artifacts/p3-worker-config-{spec,lint}.log`. Fix commit/amend window pending;
no further realization/VM until lead assigns fresh state and exact source proof.

The two-file correction is now folded into P3 head
`f2ba098c707b416c356f4af00723f0b82c3bc93a`, tree
`0cc4b516636d6685bdaccd2bf66008981eba4cda`. Old head ffe83296d is retained at
`refs/backup/2026-11-05-p3-worker-config-ffe83296d`. Old/new diff contains only
the worker's canonical network configuration (3 added / 1 removed lines) and the
61-line construction regression. Original commit message is identical; normal
Nixfmt/RuboCop hooks passed. Parent/COMPAT and service commits remain unchanged;
worktree/index were checked clean after completion and the window released.
Receipt: `artifacts/p3-worker-config-amend.log`.

After release, the combined pure derivation evaluation passed (exit 0): service
is unchanged `pqw1r6h689y75phgsdbb490lqybxnvsn-osctl-repo-server-26.05.drv`;
OSVM is now `8zx63k3jlfyb7841h2r4pjc56mqbxcyw-osvm-26.05.0.drv`;
8 GiB/2 CPU/32G worker is now
`52mfm4x3ifwbd3f71ipiqqjiqrkc2s7w-os-test-image-pipeline-worker.json.drv`.
The latter differs from the earlier realized worker's
`x9zqqmfvpbhn9gcxwp15dlzlnjwiglnh-os-test-image-pipeline-worker.json.drv`;
only service realization is reused. Logs/status/identities:
`artifacts/p3-worker-fixed-drvs.{json,log,status}`. No build or VM was launched.

Fresh private preparation root `/tmp/p3-smoke-f2ba098c707b` has the same exact
three original Alpine plan entries/defaults/tags, scoped dependencies and GC [],
strict producer-only adapter and driver wrapper pinned to the new full SHA/root
and unique run ID. Source-plan evaluation, manifest verification and shell syntax
pass. New `preparation.json` binds the source tree and lock hash; no watcher-owned
inputs.json/worker-config/osvm links exist or were written by preparation.
The old failed root remains unchanged. Lead owns fresh cache/realization and
registration/launch; do not run the prepared wrapper before that step.

Lead subsequently realized the fixed worker (143s, output
`/nix/store/861yg3xkbvq3h4dbfjg1dk2l41xhm2a3-os-test-image-pipeline-worker.json`)
and OSVM (15s, output
`/nix/store/xy4sism02zp3mjrjibndsbj8nm5khq9l-osvm-26.05.0`), plus metadata.
Actual canonical OSVM derivation is
`/nix/store/lcp0c2y8yq6zg174kimllxr9955vqzw7-osvm-26.05.0.drv`, confirmed by
new known-quick `nix eval --raw .#osvm.drvPath` (exit 0), output deriver and build
receipt. The earlier 8zx derivation came from `builtins.getFlake (toString ./.)`
local-path source context, while canonical .# uses git+file at the exact revision.
Their gem source paths/NARs differ; they are not equal derivations. Scoped
OSVM/libosctl source comparison found 176 equal entries, no differences.

The realized installed image_build_worker.rb SHA-256 is
`ce8151ab2507ac0842db6dd220a31d1a0271d0b6dbe34437c7611fffc14170a1`, identical
to the clean fixed checkout and containing the canonical no-opts network fix.
Current HEAD, metadata revision, lock hash, prepared manifests and actual links
all match. No source defect or retry blocker remains at this provenance boundary.
Evidence: `artifacts/p3-smoke-provenance.json`,
`artifacts/p3-osvm-canonical-drv.{log,status}`. No new build/VM/service action
was performed during reconciliation. Lead owns the fresh registered retry.

Lead accepted bounded smoke preparation at `/tmp/p3-smoke-ffe83296d682`.
The exact-source three-Alpine fixture plan, strict producer-only SSH-to-ctl
adapter, private driver wrapper, source/lock manifest and SHA-256 receipts are
prepared and checked; see [artifact paths/flags/acceptance](p3-two-worker-smoke.md).
Driver output/status paths are independently observable by the lead's watcher.
Watcher-owned inputs.json and worker-config/osvm links were not touched.
No service/VM launch or product edit occurred. Lead owns source/cache realization
and the explicit subsequent registration/launch step; production P0 blockers
and full-CI/runtime gaps remain unchanged.

The lead's subsequent cache plan found an actual export omission: the workflow
uses `.#osvm`, while the flake exported no such package. A narrow approved
flake.nix-only correction exposes existing `pkgsWithOverlays.osvm`. The one-line
patch has no input/lock/wrapper/API change. `timeout 45s nix eval --raw
.#osvm.drvPath` passes (exit 0), returning
`/nix/store/qygdvcyzfcnw1dy88yic0hrbqb0ksd0q-osvm-26.05.0.drv`.
Nixfmt check, Nix parse and whitespace checks pass; no realization occurred.
Logs/status: [artifacts/p3-osvm-export-eval.log](artifacts/p3-osvm-export-eval.log),
[status](artifacts/p3-osvm-export-eval.status).

The export is folded directly into logical P3 head
`ffe83296d682a72076f942c5b6b10dd480a71b36`, replacing
`2120ec2de70b9daa38588a8ad79a8296ec3e6167`; new tree
`0a5b137f47e1ca62e2429f03a07561e4a6778a1d`. Parent/COMPAT remains
`39f7e73746d0157bdd8b734a76d13f9b974b7890` and service remains
`463704f2046b1a888ae18777ba4932e9d118872e`. Old/new diff is only this
flake.nix line; service/package content is unchanged. Backup ref
`refs/backup/2026-11-05-p3-osvm-export-2120ec2d` retains the old head.
Exact existing commit message was preserved with amend -F. Normal Nixfmt and
RuboCop hooks passed; commit finished before clean worktree/empty-index proof
and window release. [Amend log](artifacts/p3-osvm-export-amend.log).

Post-release new-head attr evaluations both passed (exit 0): service remains
`/nix/store/pqw1r6h689y75phgsdbb490lqybxnvsn-osctl-repo-server-26.05.drv`,
identical to the lead's successful realization; OSVM remains
`/nix/store/qygdvcyzfcnw1dy88yic0hrbqb0ksd0q-osvm-26.05.0.drv`.
The existing service Nix build therefore applies without a redundant rebuild or
native rerun. Logs/status: `artifacts/p3-final-{osctl-repo-server,osvm}-drv.{log,status}`.
The service eval recorded an ignored busy Nix evaluation-cache warning, then
returned the exact derivation successfully; no retry was needed.

At exact final `2120ec2de70b9daa38588a8ad79a8296ec3e6167`, the corrected explicit
worker-function evaluation passed within its 45-second bound (exit 0):
`(import ./tools/image-pipeline.nix { memoryMiB=24576; cpus=2; diskSize="32G"; }).drvPath`.
Result: `/nix/store/wqx2n31bcyd9iaf3jphb65arzq96rzp9-os-test-image-pipeline-worker.json.drv`.
Logs/status: [p3-worker-eval.log](p3-worker-eval.log),
[p3-worker-eval.status](p3-worker-eval.status). Values were evaluation fixtures
only. No worker build, VM, local service or source change occurred.
The lead separately reported source-plan evaluation and the final service Nix
package build green. The initial unapplied-function checker failure was a check
invocation error, not an established application failure.

[Prepared two-worker smoke brief](p3-two-worker-smoke.md) records read-only local
aitherdev capacity/KVM observations, a smaller proposed 8 GiB/2 CPU per-worker
budget, source/cache gate, scoped three-Alpine-image plan, disposable direct-ctl
transport and real-engine invocation. It is not execution/admission evidence.
Lead allocates a fresh watcher only after accepting capacity and cache plans;
actual runner/production P0 blockers and remaining runtime proof stay explicit.

## Previous consolidated revision (before OSVM export)

- Final P3/whole head: `2120ec2de70b9daa38588a8ad79a8296ec3e6167`.
  Parent/COMPAT: `39f7e73746d0157bdd8b734a76d13f9b974b7890`;
  service: `463704f2046b1a888ae18777ba4932e9d118872e`.
- Old complete head: `fcf49d91c618abf6ab2a766d3a7c4fdc8ede91c3`.
  Both complete trees are exactly `ec81e39192b08402eea967a1bdb1978761e36e2a`;
  explicit tree diff is empty and worktree/index are clean.
- Independently compared old aggregate P3 patch (initial base to old complete
  head, restricted to the 36 owned paths) with final COMPAT-to-P3 commit.
  Both stable patch IDs are `26cb365f4ab2fff91585564fecf156c77b15314f`;
  complete changed path sets match. Caused P3 fixes are folded into one owner.
- Original review target `932937390c876e4afcc5df6e0da653a39177af58` remains
  the original target; it is not relabeled as final-head review. The three
  finding fixes below have their own quick-check receipts. Lead owns remaining
  review and watcher/P0-admitted runtime checks. No source changes or redundant
  tests were made for this history-only consolidation; no P3 migrations/pin or
  externally consumed state require preserving an intermediate P3 commit.

## Assigned review fixes

Lead assigned three Important findings on reviewed head `932937390c876e4afcc5df6e0da653a39177af58`.
The combined bounded patch is committed as
`c2231c9df9b1f20378b1b3c72a03f55e0bf260fd`, parent
`0870311705f8c10920a57c32307a5e199fb879f3` (peer P2 fix).
Commit tree: `e89454af817a875aaf01d331dd74d80e90fe893e`;
stable patch ID: `db69bf9c9b1ada054c17f32ea248ea6d354f9d46`.
Exactly 11 owned paths, 356 insertions / 115 deletions including formatting and
spec-group nesting. Normal Nixfmt/RuboCop hooks passed, commit-msg hooks passed
with advisory width warnings; no bypass. Commit finished before empty-index
verification and window release. Unrelated core/logging dirty files were
preserved. No peer files or index entries changed. Lead-owned final consolidation
will fold these caused fixes into P3; original review provenance remains above.

- Decode a structured service error before rejecting nonzero SSH status. Actual
  child-process fixtures emit conflict/superseded JSON and exit 1; both become
  ControlError and retain the response receipt. Non-JSON exit 255 preserves
  status/stderr diagnostics without echoing stdout. A success JSON with nonzero
  exit is still rejected. Existing wire, forced-command role and authentication
  are unchanged.
- Automatic detector output intersects the configured plan; manual unknown names
  still fail. A devuan-4 source name outside that plan no longer aborts an
  automatic run. Shared image-scripts/tests changes select all source images,
  then the configured intersection. No configured selection exits before begin,
  so no baseline-only candidate/test-config is advertised for that case.
- Full-CI dependencies now come from source-owned
  `tests/image-repository-requirements.nix`: ordinary distribution selectors,
  CLI default stable aliases, explicit Debian/Ubuntu latest aliases and pinned
  NixOS 22.11/minimal plus 24.05/impermanence. The resolver suite imports that
  same pinned list. Preflight resolves explicit vendor/variant/architecture and
  exact versions or tags. A missing unchanged required variant raises before
  test-config emission, even when the baseline contains that release/minimal.
  No automatic rebuilding of untouched dependencies is added.

Bounded suite source inventory: distributions.all covers cgroups/mount,
dist-config/start-stop/netif/rundir and systemd/device-units; plain CLI stable
consumers use Alpine/Arch/Debian and crashdump's AlmaLinux/Alpine/Arch/Debian/Ubuntu
sample (`osctl/lib/osctl/cli/container.rb:1830` is the default). Docker/Podman/
Incus/Snap selectors use existing ordinary versions plus Debian/Ubuntu latest.
`tests/suite/dist-config/nixos-resolvers.nix:18` and the impermanence upgrade
test at `tests/suite/upgrade/impermanence-from-2abbe3cc1c10.nix:275` fetch the
pinned NixOS tuples. `nixos-persistence-upgrade` uses skip-image/local derivations;
declarative NixOS/systemd eBPF containers are built locally. ct-image-fetch's
explicit flaky/dead/truncated/garbage/badgzip repositories are intentional
fixtures and remain excluded; its initial Alpine preload is included.

Trigger/selector audit: images expand abstract links, builders select their
consumers, distribution includes select dependents, bin/common include/tests
select all, and nixos-container selects NixOS. osctl-image/osvm/tools/workflow/
repository policy and requirements/distributions changes select all configured
items. Non-runtime image-scripts README/LICENSE/shell-test-flake changes may skip
when no configured item is affected. No source parser or dependency graph added.

Review-fix quick checks: 12 examples pass in the existing coordinator spec
(includes two prior examples and ten new regressions); scoped six-file RuboCop
passes, as do Nixfmt, three Nix parses, workflow YAML and whitespace. Logs are
[p3-review-fix-spec.log](p3-review-fix-spec.log) and
[p3-review-fix-lint.log](p3-review-fix-lint.log). Same pinned Ruby/OSVM wrapper
command below, limited to `osvm/spec/osvm/image_pipeline_coordinator_spec.rb`.
The readiness fixture evaluates only the pure declarative requirements with
`nix-instantiate --eval --strict --json`; no derivation build/evaluation or VM ran.
Commit receipt: [p3-review-fix-commit.log](p3-review-fix-commit.log).

## Revisions and ownership

- Final post-consolidation P3/whole head: `932937390c876e4afcc5df6e0da653a39177af58`,
  parent `9f78583b57d03bcda7e7a42d2acd196c4ee04d7a` (COMPAT), preceded by
  consolidated service `a9ce2d4f79775873b35a34cb596792515f761a98`.
- Independently verified old/new P3 stable patch ID:
  `428c99b5bbe405a6cd929388755c6961df0e5649`. Both final trees are exactly
  `3844d6372319f75f2c3ff92094a8a83ab0ad978e`; explicit tree diff is empty.
  Worktree/index are clean. Existing P3 quick-check evidence applies to the
  unchanged source; no tests were repeated solely for the history rewrite.
- Investigated baseline: vpsadminos `2951a632c4254a44747a8da326e3dde897eaa0e2`.
- Implementation initial base: `d2fe1489f0b0b213fb247aeee6e081d349adaf42`.
- Pre-consolidation P3 parent: `e7d0f28b2cc47e1dbcda8aeecdb30e3276500302`.
- Pre-consolidation P3 head: `121d349f5a96a1bc3c92463ebe0e6bd76143ab7a`.
- Final tree before lead-owned consolidation: `3844d6372319f75f2c3ff92094a8a83ab0ad978e`.
- Exactly 32 assigned files, 1392 insertions / 152 deletions. `git show --stat`
  and `git diff HEAD^ HEAD` are the exact P3 inventory/diff. Clean worktree and
  empty index verified after commit completion; window released to lead.
- One logical P3 commit. No schema migration, dependency/pin update, obsolete
  P3 history, deployment or externally consumed P3 state. Lead-approved core
  consolidation preserved the complete final tree and P3 patch unchanged.

## Delivered behavior and files

- `image-scripts/bin/config`, `osctl-image/lib/osctl/image/{assigned_config,
  assigned_result}.rb`, CLI app/image and manpage: dispatch-time inert config,
  source/config digest, auxiliary SPIN/SPINVER, private scripts copy, retry reuse,
  serial existing image tests and validation of actual exported tuples/formats.
- `osvm/lib/osvm/image_build_{pool,worker}.rb`, osvm.rb: bounded warm VM workers,
  dynamic queue, quick-work capacity while Guix/Gentoo run, soft affinity,
  separate disks/state/sockets/network/exports and one replacement retry using
  the original descriptor. Uncertain cleanup cannot return a worker to reuse.
- `tools/image-pipeline{,-publish}.rb`, `tools/image_pipeline/{control,
  coordinator,publisher}.rb`, two Nix helpers and workflow: source/input snapshot,
  role-separated SSH, strict current P1 DTOs, uploaded result acknowledgements,
  finish/seal, independent successful-subset publication and one sealed full-CI URL.
  Equal-source stale admission uses P1's distinct superseded response and a fresh
  status before a no-policy receipt. No build-all/test-all phase barrier.
- Approved daemon primitive in `osctld/lib/osctld/{config,db/repositories}.rb`:
  optional default_repository_url only creates a missing default; unset public
  URL and persisted/custom state remain unchanged.
- `test-runner/nix/{lib,image-repository}.nix`, test_evaluator.rb and
  `osvm/lib/osvm/vpsadminos_machine.rb`: common static-pool defaults, new daemon
  setting, exact URL/enabled/no-fallback assertions after repository readiness.
- Focused specs: assigned_config, image_build_pool, image_pipeline_coordinator,
  vpsadminos_machine and daemon config/repositories. Docs: creating.md,
  image-pipeline.md, testing.md and osctl-image manpage. Main lead copy pass
  accepted. Configured IMAGE variable replaces a release-specific capture example.

## Quick checks

All checks used current worktree source; helpers below alter only Ruby load paths.
The installed Nix wrapper supplies matching gem/native closures. No project
Gemfile, lockfile or native extension was modified to make tooling available.

Pinned Ruby: `/nix/store/m0nfdb4mhfgwkgss4ymyqmvviwy30i6y-ruby-3.4.9/bin/ruby`.
Temporary launcher `/tmp/container-image-rspec.rb` contains:

```ruby
require 'rubygems'
wrapper = ENV.fetch('SPEC_WRAPPER', '/nix/store/1ywyikqab9jsczazbsa39a8gn3yjajpz-ruby3.4-osctl-image-26.05.0/bin/osctl-image')
Gem.paths = {'GEM_PATH' => (File.read(wrapper).scan(%r{"(/nix/store/[^\"]+/lib/ruby/gems/3.4.0)"}).flatten + [File.expand_path('~/.gem/ruby/3.4.0')]).join(':')}
$LOAD_PATH.unshift(ENV.fetch('SPEC_ROOT'))
require 'rspec/core'
exit RSpec::Core::Runner.run(ARGV)
```

From the project root, with `RUBY` set to the exact pinned executable above:

```sh
SPEC_ROOT=osctl-image/spec "$RUBY" /tmp/container-image-rspec.rb osctl-image/spec/osctl/image/assigned_config_spec.rb osctl-image/spec/osctl/image/cli/image_spec.rb --format progress
SPEC_ROOT=osvm/spec SPEC_WRAPPER=/nix/store/bmg0hkflwfz9w4wfzqql5qjqjf2d3fx8-ruby3.4-osvm-26.05.0/bin/osvm "$RUBY" /tmp/container-image-rspec.rb osvm/spec/osvm/image_build_pool_spec.rb osvm/spec/osvm/image_pipeline_coordinator_spec.rb osvm/spec/osvm/vpsadminos_machine_spec.rb --format progress
SPEC_ROOT=osctld/spec "$RUBY" /tmp/container-image-rspec.rb --require libosctl --require spec_helper osctld/spec/osctld/config_spec.rb osctld/spec/osctld/db/repositories_spec.rb --format progress
```

Results: 33 + 22 + 10 examples, zero failures. Logs:
[p3-image-spec.log](p3-image-spec.log), [p3-osvm-spec.log](p3-osvm-spec.log),
[p3-osctld-spec.log](p3-osctld-spec.log). CLI spec deliberately prints a failing
image-test fixture; the RSpec result is green. Config fixture executes the actual
copied shell build/test wrappers twice across rollover, including variant and
SPINVER. Pool fixtures prove streaming/reuse/replacement. Mixed-outcome coordinator
fixture proves a queued failure does not prevent a good image's publication.

Scoped RuboCop 1.91.0: 22 files, no offenses ([log](p3-rubocop.log)). Exact
executable `/nix/store/1vqyn32nbd4d2x2h8yqwssw5mlm5xnjd-ruby3.4-rubocop-1.91.0/bin/rubocop`;
GEM_PATH was `$HOME/.gem/ruby/3.4.0` for standalone lint. Nixfmt 1.4.0 --check
passed for the four P3 Nix files; each also passed `nix-instantiate --parse`.
`bash -n image-scripts/bin/config`, Psych YAML parsing and `git diff --check` passed.
Normal commit hooks reran Nixfmt/RuboCop successfully ([log](p3-commit.log));
commit-message width warnings were advisory (all lines satisfy the repo's <=80 rule).

The first test-runner devshell attempt failed to load rspec/core (environment,
not a test failure); the pinned wrapper closure resolved it. The first commit
attempt's explicit GEM_PATH hid default rexml from Overcommit. No commit occurred;
owned entries were unstaged and the index reconciled empty before repairing.
Retry used ordinary Ruby/default gem lookup plus packaged linter bins, with no
hook bypass or installation. All commands finished before window release.

## Compatibility and bounded gaps

- Common module belongs to test-runner itself, not a suite-relative path.
  Canonical vpsadmin source `b83b26e1ba1c8e869ae3ffbcb5801ed071c3844e` imports
  mkTests/mkTestsMeta at flake.nix:148/157, makeTestLib at tests/all-tests.nix:12,
  and makeTest at tests/make-test.nix:34. Its vpsadminos pin is
  `8e44a5124439b1f3048ffc56b1717614a5360358`; no pin changed.
- Absent imageRepository preserves existing consumers. An older pinned daemon
  does not acquire runtime-pool default_repository_url support from the new
  framework alone. Declarative static-pool overrides use the existing module
  contract; arbitrary historical runtime-pool support is not claimed.
- Persisted/imported/custom defaults are preserved; readiness fails if that state
  cannot satisfy the requested sealed URL. Explicit repository fixture flows stay
  explicit. The runtime install-and-first-fetch-in-one-shell acceptance needs an
  actual updated-daemon VM check; unit tests cover the creation boundary only.
- The initial ordinary-distributions-only preflight gap is addressed by the
  assigned review fix above. Actual full-suite runtime proof remains pending;
  declarative inventory is maintained with suite fetch selectors.
- Source-plan and worker-function evaluation now pass as recorded above. No
  worker build, KVM boot, production SSH control transport or full CI ran for P3.
  Source parsers and queue/control fixtures are not those runtime proofs.
- P0 trusted runner/secret admission and measured resource/storage limits remain
  prerequisites to privileged workflow execution. Finite lease must cover full CI
  after build heartbeats stop; expiry must fail explicitly. No speedup claimed.
- Official latest compatible refs were checked via upstream SSH ls-remote:
  actions/checkout v7 `3d3c42e5aac5ba805825da76410c181273ba90b1`,
  upload-artifact v7 `cf430e030ddbb5b0abf93d22962f4752f3646cd9`,
  download-artifact v8 `9000827ccba6bdab643e8b6fd33ac0654aef8333`.

## Next verification boundary

Lead owns final committed-deliverable review, then fresh watcher long batches.
First source/input-only commands (not launched here):

```sh
nix eval --impure --json --file tools/image-pipeline-plan.nix
nix build --impure --file tools/image-pipeline.nix --arg memoryMiB "$IMAGE_WORKER_MEMORY_MIB" --arg cpus "$IMAGE_WORKER_CPUS" --argstr diskSize "$IMAGE_WORKER_DISK_SIZE" --out-link "$PIPELINE_STATE/worker-config"
nix build .#osvm --out-link "$PIPELINE_STATE/osvm"
```

Resource values must come from P0, not guessed defaults. Stop unexpected kernel
builds and investigate cache provenance. After admission, use the exact workflow
producer invocation with disposable service state and selected fast/slow fixtures;
prove two overlapping warm workers, same capture on replacement, mixed-failure
publication, one sealed baseline/new-image view and new runtime pool first fetch.
Full CI's exact consumer entry point is:

```sh
./test-runner.sh test --test-config "$TEST_CONFIG" --state-dir "$FRESH_STATE" --fresh --jobs auto -t ci
```

Stop on wrong tuple/bytes, authority violation, uncertain cleanup or budget
exhaustion. No further application edits while the lead consolidates history.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-04-container-image-build-pipeline/)
