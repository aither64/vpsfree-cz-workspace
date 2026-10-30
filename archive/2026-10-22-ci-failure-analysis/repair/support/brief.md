# First-switch impermanence diagnostic preparation

Implementer3 owns this support package under the architect repair design.
Session/env/access and worktree were verified; hook setup is complete and its
exclusive Git mutation window is released. This brief authorizes no additional
launch: lead schedules a fresh watcher and the one diagnostic VM.

## Owned paths and source selection

Application paths: `tests/suite/upgrade/common.nix`, `tests/all-tests.nix`,
`tests/suite/upgrade/from-6.12-guests-first-switch.nix`, and
`tests/suite/upgrade/impermanence_first_switch.rb`. The Ruby helper uses the
repository's required snake_case filename. Normal cases retain their original
matrix/flags; the focused case has a unique name, manual tag and an explicit
`VPSADMINOS_ENABLE_UPGRADE_DIAGNOSTICS=1` registration gate.

Disposable source snapshot: `/tmp/ci-failure-analysis-2026-10-22/support/baseline-source`.
Disposable native state: `/tmp/ci-failure-analysis-2026-10-22/support/attempt-1`.
These paths belong to this session/support package. The baseline source was
created at 2026-10-22 under this brief; native attempt-1 has not been created.
Never reuse either path if existing ownership/contents differ. Do not touch the
source session's runner or source files. Snapshot exact Git archive
`846bb469505789ba0b2a405fa5905ba6d8253006`, then overlay only the four support
paths above. Concurrent writer/reader/hotplug/Podman edits are excluded. Preserve
archive SHA256, exact support diff/hashes and `flake.lock` alongside this brief;
a revision marker alone does not establish product/source equivalence.

The immutable old writer remains
`3cc31e39ba2880a311a1a5889521d2bc0d7e3e0f`. Architect and lead accepted a
focused-case-only `activationTargetRevision` argument, allowing only exact
`846bb469505789ba0b2a405fa5905ba6d8253006` behind `firstSwitchCapture` and
removed before predecessor construction. Target uses that exact GitHub flake;
diagnostic scripts use the source snapshot. Ordinary targets stay local. This
avoids archive-path `self.rev` loss and excludes concurrent writer/reader edits.
See [frozen source identity](baseline-source.md) and
[complete support overlay](baseline-support.diff). Snapshot allocation is
346853376 bytes; free space after copying was114247143424 bytes. The later
manual Podman registration in the worktree is deliberately absent from this
frozen support-only snapshot.

## Capture and native behavior

Capture after the impermanent container starts, immediately before the first
switch, and after target pool import before the existing equality assertions.
Keep all original first-activation assertions. A narrow catch handles only the
intentional successful stop after that activation; equality/other exceptions
propagate to the native failure result and cleanup. `Timeout.timeout(1800)`
bounds script runtime after configuration preparation. Native evaluator cleanup
stops/kills owned guests, destroys managed disks and finalizes runtime state.

Each capture writes JSON plus decoded raw files into the test's state directory,
so before-switch evidence survives later assertion failure and native disk
cleanup. The guest recorder does not change runtime metadata, GC, root selection
or service application. It opens the expected init's proc directory across the
capture, records full stat/birth before/after, root device/inode and mount
namespace, and marks any identity change. Raw init mountinfo and explicit `/`
and `/private` mount fields preserve device/root/source without inferring a
root dataset from a symlink or prefix. Candidate dataset path stats are a raw
inventory, not an adoption algorithm.

Fields: runtime config/GC raw bytes with size/inode/times/hash; container API;
full init stat/birth/status/root/ns; host+init mountinfo; ZFS name/GUID/mountpoint/
mounted/origin and mountpoint/private stat; persistent+ephemeral marker bytes;
daemon full stat; kernel/boot ID/booted/current generations and CPU topology;
sysctl current log, applied/done stamps, generated check source/read-only check
status and configured-key value readbacks. No `sysctl --system`, `sv start`,
service restart or extra apply is run. Missing/truncated/inaccessible fields
remain explicit evidence limits; errors are not replaced with guessed values.

Capture subprocesses have8s bounds; the whole guest recorder has120s, with130s
host command allowance. File reads and recorded subprocess output are capped;
raw bytes are Base64-encoded with truncation indicators. Total retained output
is capped at64MiB by the lead watcher; if growth approaches that cap, stop owned
execution, retain the three compact capture directories and first-error logs.
Do not silently discard overflow and call capture complete.

## Resource and cache preflight

Accepted provisional incremental disk budget:24GiB, with40GiB shared free floor.
Snapshot is about331MiB; Nix may copy it once into the store. The inherited
machine declares one10GiB sparse managed disk; its *physical* growth can reach
10GiB. No transferpeer/cross-pool mode is selected.8GiB is a host reservation,
not a fixture memory override. Read primary configured memory/CPU/disk list
from evaluated native JSON; common.nix's explicit4GiB applies to the inactive
transferpeer branch, so do not infer primary memory from that line.

Allow at most12GiB additional missing Nix closure/build output within the
24GiB total budget, after including source/store copies, max managed disk,
compression temporary outputs and logs. A dry-run must establish what is cached,
substituted or built before launch. Any required Linux kernel build is a blocker;
no unexpected kernel build may start. If measured closures/temporary copies do
not fit conservatively, report instead of substituting global GC or deleting
foreign artifacts. Current free space at hook completion was106.1GiB; refresh
`df -B1` before each operation and during any long operation.

Known quick checks: Nix parse and prepared nixfmt; Ruby host+embedded-guest
syntax; prepared RuboCop (existing deprecated PredicateName configuration warning
only). No Nix evaluation/build or VM was launched by implementer3.

## Exact no-build preflight, ready for lead watcher

Working directory:
`/tmp/ci-failure-analysis-2026-10-22/support/baseline-source`.

```sh
VPSADMINOS_ENABLE_UPGRADE_DIAGNOSTICS=1 VPSADMINOS_CONFIG= nix-build /tmp/ci-failure-analysis-2026-10-22/support/baseline-source/test-runner/nix/evaluate-tests.nix --arg repoRoot /tmp/ci-failure-analysis-2026-10-22/support/baseline-source --argstr system x86_64-linux --argstr mode testJson --argstr testPath upgrade/from-6.12-guests-first-switch --argstr testArgsJson '{}' --arg testConfigPath /tmp/ci-failure-analysis-2026-10-22/support/baseline-source/tests/test-configs/ci.nix --option allow-import-from-derivation false --dry-run --no-out-link
```

This evaluates the focused case's derivation and reports missing builds/cache
substitutions, with no intended realization or VM. If an import from derivation
is required, it refuses; report its exact derivation rather than allowing a
hidden build. Capture full stdout/stderr and exit. Also obtain selected metadata
without realization using the same helper/arguments, `nix-instantiate --eval
--strict --json`, and `--argstr mode testsMetaOne`. Assert one machine, one
attempt, manual-only tags, actual primary configured RAM/CPU and complete disk
list before accepting a VM forecast. These details must come from evaluated
config/metadata, not source search guesses.

After no-build evaluation succeeds, lead separately selects cached preparation
and obtains complete derivation/input graph and realized config. Bind the target
store path against the preserved original846bb first-switch shell receipt,
including expected OS source/lock/kernel identities. A different target closure
is a blocker to explain, not an assumed equivalent result. Save immutable config,
all input paths, dry-run missing byte estimates, physical allocated sizes and
exact identities before VM launch.

## Native selection after accepted cache/resource preparation

Do not run until lead accepts the preflight and prepared config/closure identity.
The capture has its own1800s script deadline after preparation; no global
command timeout should kill preparation and be mistaken for a guest failure.

```sh
VPSADMINOS_ENABLE_UPGRADE_DIAGNOSTICS=1 VPSADMINOS_CONFIG= ./test-runner.sh test --fresh --jobs 1 --prebuild --stop-on-failure --max-memory-mib 16384 --memory-reserve-mib 8192 --max-shm-mib 16384 --shm-reserve-mib 8192 --max-cpus 4 --state-dir /tmp/ci-failure-analysis-2026-10-22/support/attempt-1 --test-config /tmp/ci-failure-analysis-2026-10-22/support/baseline-source/tests/test-configs/ci.nix upgrade/from-6.12-guests-first-switch
```

Configured RAM/CPUs must fit these reservation ceilings without overrides.
Default destructive cleanup removes managed disks. Preserve the first-switch
capture directory before any later exception result cleanup; native cleanup
removes disks, not captured text/raw files. A reproduced baseline dataset
assertion is expected diagnostic evidence, not a passing repair check.

## Shutdown and cleanup contract

Lead watcher owns the exact runner process and its fresh handle. At reserve
floor/output/deadline escalation, send INT to that owned runner, allow its native
ensure cleanup to stop/kill guests and destroy managed disks; reconcile native
child/process handles before deleting anything. Do not signal daemon-wide Nix
builds, unrelated processes or another session's VM. Forced escalation needs the
exact owned process tree retained, not a broad process-name match.

After effects end and compact evidence is copied/hashed, verify no owned process
or active test lock, then remove only this support attempt's disposable files
and snapshot. No namespace-wide deletion, Nix GC, branch deletion or session
lifecycle action. Preserve raw phase captures, first error, native result/config,
source/input/derivation identities, peak/final physical `du` and free-space
observations in the session. Retain an active snapshot if needed for an accepted
repeat; otherwise reclaim it after proof is saved.

## Preflight batch 1 assessment (2026-10-22)

Authoritative receipt files: dryrun.exit=0, dryrun.elapsed=98s;
metadata.exit=0, metadata.elapsed=6s. The watcher summary's literal shell
placeholders are not values. The unrelated AMD inspector failed before launch
because `/usr/bin/time` was absent; its replacement belongs to its own watcher.
Support made no duplicate AMD observation.

Native config extracted through `nix-instantiate` and `nix derivation show`,
without output realization: `3k70877r1v12vgd90ml599ya02wxs5zj-os-test-upgrade-from-6.12-guests-first-switch.json.drv`,
output `/nix/store/hd3by52cz1wrza2k28av89iflad1j4ly-os-test-upgrade-from-6.12-guests-first-switch.json`.
Full config/script saved in native-config.json/native-script.rb; script syntax
passes. It confirms one8192MiB/4CPU machine, one10G managed file disk, user
network, no extra disks. Kernel path is
`/nix/store/ii8f7mj2a82cjvx0f84pjpz31lncpnxv-linux-6.12.95/bzImage`,
initrd `/nix/store/3jcr32gn651ppxk7hqpj1ic53v1q04c0-initrd/initrd`, predecessor
toplevel `/nix/store/r20c14nbmqy8mv4hml15crj375n5fvz2-vpsadminos-system-vpsadminos-26.05pre-git`.

Target identity is a blocking difference to explain: diagnostic exact GitHub
flake target `/nix/store/3nl6c9yx07skwfid44dd95xbzm8wvcr3-vpsadminos-system-vpsadminos-26.05.git.846bb46`
versus preserved original6.12-guests switch
`/nix/store/gnf7wyg9p1yjvgfihm1d4056xy08mwmp-vpsadminos-system-vpsadminos-26.05.git.846bb46`
(source-session machine-shell.log2836,3011). Target osctld gem also differs
(new63mrvm..., original5ya177...), whereas predecessor41f5f... matches.
Neither target nor original target gem/deriver is local; publiccache narinfo
queries return404. Exact original fullgraph cannot be compared from those
receipts alone. No equivalence or instrumentation-only classification is made.

216 local builds include no Linux/ZFS source compilation. `zfs.drv` only
creates an empty module directory; Linux modules union/depmod and shrunk closure
assemble already produced/substitutable outputs. Kernel itself is not currently
local but is substitutable, confirmed publiccache NAR metadata/deriver.178
substitutions report100.2MiB compressed/607.4MiB unpacked. Local builds include
156 writeText/scripts,12Ruby wrapper assemblies,2module assemblies,1squashfs,
4small native tool/probe compilations and41other assemblies. These categories
are evidence interpretation, not permission to build. Complete216 derivations,
full5794-node source/input graph and target3248-node graph boundary are retained.

The24GiB provisional budget remains conservative but unaccepted until target
boundary and squashfs/closure temporary-copy sizes are checked. Dryrun free space
moved104022102016→102504562688bytes; metadata-end111489970176bytes, showing shared
filesystem changes, not isolated support allocation. Do not attribute them to
this operation. Baseline snapshot remains346853376bytes.

### Superseded original-fixture comparison (failed batch2)

Lead watcher only, same snapshot cwd, no realization/VM and IFD disabled:

```sh
VPSADMINOS_CONFIG= nix-instantiate /tmp/ci-failure-analysis-2026-10-22/support/baseline-source/test-runner/nix/evaluate-tests.nix --arg repoRoot '(builtins.getFlake "github:vpsfreecz/vpsadminos/846bb469505789ba0b2a405fa5905ba6d8253006").outPath' --argstr system x86_64-linux --argstr mode testJson --argstr testPath upgrade/from-6.12-guests --argstr testArgsJson '{}' --option allow-import-from-derivation false
```

This evaluates the *unmodified original fixture* from exact846bb and its normal
local-target resolution, not the diagnostic override. Save stdout/stderr/exit;
then read that returned drv with `nix derivation show`, decode env.text, compare
switch target and source gem/config inputs with preserved originalgnf and
current3nl. A refusal or a third identity is useful evidence, not license to
realize anything. Bound this evaluation to180s in the watcher; no retry. Cache/
closure queries can follow only known resulting paths and remain read-only.

Batch2 executed that proposed query and failed before producing a derivation:
exit1 in4s. Keep `preflight-batch2-original.{stdout,stderr,exit,elapsed}` intact.
The expression passed a context-bearing `getFlake.outPath` string as `repoRoot`.
`evaluate-tests.nix` imports the suite through that string; original common's
`getFlake (toString ../../..)` then rejects the retained store-path context.
This is an argument-boundary failure, not a product/configuration observation.

### Conservative physical growth calculation pending target decision

All1297 already-local output paths in the full input graph total4166776504 NAR
bytes (3.881GiB); this deliberately includes build-time outputs as an upper
bound, not only the guest runtime.178 missing substitutions add607.4MiB
unpacked. Squashfs streams tar directly into sqfstar; it does not make a full
uncompressed root copy (`09pf...squashfs.img.drv` buildCommand). Its source
closure roots only the predecessor toplevel, which retains the target through
extraDependencies. Use5GiB as a conservative uncompressed/compressed-image
ceiling from the measured4.49GiB existing+substituted inputs plus assembled
scripts/module closures, until a prepared closure-info total can confirm it.

Peak incremental allocation allowance:10GiB managed guest disk;10GiB for two
simultaneous5GiB squashfs output/copy instances;1GiB for module closure/initrd
and small native temporary products;1GiB for snapshot/store source copies;
0.6GiB substitutions;0.1GiB logs/evidence. Total22.7GiB, rounded up to the
accepted provisional24GiB. The10GiB image allowance is intentionally pessimistic:
Nix often renames the build result rather than making a second same-filesystem
copy, but that optimization is not required by this budget. Stop preparation
if actual intermediate products exceed the allowance. No Linux/ZFS source tree
or kernel compiler work directory is allowed by this forecast.

8GiB guest memory/shared memory is a RAM/tmpfs reservation, not10GiB additional
root-disk allocation. Check /dev/shm and memory admission separately. Refresh
free-space before a selected launch and refuse if free minus24GiB would cross
40GiB. This forecast does not resolve the target store/input mismatch and grants
no realization/VM permission. After selected preparation, remeasure closure-info,
all outputs and physical `du` before the VM is accepted.

Native reservation correction after reading ResourcePool::CapacitySource:
`--max-memory-mib`/`--max-shm-mib` are ceilings **before** subtraction of the
8192MiB reserves. Set each ceiling16384 and each reserve8192 explicitly to leave
8192MiB usable for the configured8192MiB guest. The earlier8192 ceiling would
leave zero preparation capacity; it must not be launched. This does not change
guest configuration or permit runtime overcommit. Local input physical allocated
size measured4567683072bytes (4.254GiB); its NAR total3.881GiB differs because
filesystem block accounting includes overhead. These inputs already exist and
are not charged again as incremental allocation except when a builder copies
runtime content into the bounded image products.

## Pending support derivation GC root

Shared store GC removed pending derivations during another owner's inspection.
Do not broaden store retention or change global GC. Own only this root:
`/tmp/ci-failure-analysis-2026-10-22/support/gcroots/config.drv`.
It roots the exact instantiated support config derivation (and its input graph),
not realized output. The root directory belongs to this support package; create
it only after confirming no conflicting/symlink ownership. Remove this exact
root after the diagnostic and all dependent inspection/preparation are complete,
after compact source/input/derivation evidence has been preserved. Eventual
realized JSON/output closure needs its own native root during selected preparation.

Prepared command, **not yet executed**. Lead's current batch2 owns original
fixture comparison and recorder metadata. Wait for that batch's completion;
never duplicate those queries. Then use the identical support evaluation with
IFD disabled and explicit native root registration:

```sh
mkdir -p /tmp/ci-failure-analysis-2026-10-22/support/gcroots
VPSADMINOS_ENABLE_UPGRADE_DIAGNOSTICS=1 VPSADMINOS_CONFIG= nix-instantiate /tmp/ci-failure-analysis-2026-10-22/support/baseline-source/test-runner/nix/evaluate-tests.nix --arg repoRoot /tmp/ci-failure-analysis-2026-10-22/support/baseline-source --argstr system x86_64-linux --argstr mode testJson --argstr testPath upgrade/from-6.12-guests-first-switch --argstr testArgsJson '{}' --arg testConfigPath /tmp/ci-failure-analysis-2026-10-22/support/baseline-source/tests/test-configs/ci.nix --option allow-import-from-derivation false --add-root /tmp/ci-failure-analysis-2026-10-22/support/gcroots/config.drv --indirect
```

No output realization or VM is part of this command. Because GC may have removed
evaluation inputs, cached timing is not guaranteed; use a fresh lead watcher if
completion is uncertain beyond one minute. On success verify symlink target
matches the selected support config derivation, inspect target existence, and
record result. If the derivation changed, compare exact source/input graph
before accepting it; do not silently call a different path equivalent.

## Corrected no-build batch3, prepared for lead watcher

`run-preflight-batch3.sh`, SHA256
`2933bb38c0b656390c88bdb7801ac0257deccc4153f6008fbe989b18b9a9e32b`,
combines support-root registration with the corrected original comparison.
Shell and embedded Python syntax pass. Only the tiny path-context probe was
executed inline; `batch3-context-probe.json` records identical path bytes before/
after, original context true and cleaned context false. The full batch has not
been launched by implementer3.

Exact fresh-watcher launch, from workspace root with the verified session
environment retained:

```sh
timeout --signal=TERM --kill-after=5s 540s bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/support/run-preflight-batch3.sh
```

The script's source cwd is the frozen disposable baseline snapshot. It checks
session binding, five frozen source/lock hashes and free space above42GiB;
rejects conflicting/symlink root directories; and permits no silent repeated
batch. Exact commands, output paths and per-step deadlines are in that script.
Support instantiation uses the identical first-switch arguments and CI config,
with180s limit and native `--add-root .../gcroots/config.drv --indirect`.
The original query retains batch2's original fixture arguments (no test-config
override); only its CLI `repoRoot` expression becomes:

```nix
builtins.toPath (builtins.unsafeDiscardStringContext
  (builtins.getFlake "github:vpsfreecz/vpsadminos/846bb469505789ba0b2a405fa5905ba6d8253006").outPath)
```

Context is discarded only for the flake reference boundary; the evaluated
configuration JSON retains its ordinary derivation input contexts. IFD stays
false. The original config receives its own native indirect root at the new
owned `.../support/gcroots/original-config.drv`. Both roots keep derivations and
their input graphs alive during inspection; neither realizes output. Remove
both exact roots when the diagnostic/dependent preparation has ended and compact
evidence is preserved. Eventual selected realized JSON/closure needs separate
native retention. This grants no global GC or lifecycle action.

After queries, the script reads support's immediate derivation and original's
recursive graph without realization, extracts raw native config JSON/system
paths, and records actual exits, elapsed seconds, free space and physical owned
allocation even on failure. Per-query limits180s, support inspection30s and
original graph90s fit the540s outer budget. Per-file output cap32MiB; expected
full graph below24MiB and total new receipts below25MiB. No kernel compilation,
Nix realization, runner or VM command is present. A changed support drv is
recorded and returns nonzero; no different identity is silently accepted.

### Diagnostic boundary if the incident graph cannot be recovered

The original `gnf7...` target and `5ya1...` osctld output/deriver are absent
locally and return404 from the checked public cache. The retained shell receipt
binds their output names but does not reconstruct their recipes/full graph.
This query can explain the difference between reproducible original-fixture
path evaluation and the explicit GitHub diagnostic target; it cannot manufacture
the missing incident graph. Store-path/source naming and flake metadata are
candidate mechanisms, not yet established explanations of `gnf7...`.

If exact incident identity remains unavailable, propose to lead/architect the
following explicit experiment boundary rather than claim equivalence: retain
the exact old writer/predecessor kernel, frozen support-only overlay and exact
846bb application source/lock inputs, while declaring the newly evaluated
target packaging/evaluation identity and any module-source/transport provenance
differences. Capture whether this immutable old writer actually saves stale
base-dataset YAML/GC ownership while the held live root points at a temporary
dataset, and what that declared target loads on first import. That can establish
the missing old-writer/runtime-state evidence and constrain reader recovery.
It cannot certify incident-exact target binaries, equal guest-image inputs,
absence of other incident contributors or generic-service causal exclusion.
No VM is selected until the lead assesses this boundary and the physical plan.

## Batch3 passed; identity boundary assessed

All batch3 exits0; actual files record support41s, original35s, graph4s.
The selected support drv/output/hash are unchanged and both native derivation
roots resolve correctly. [Identity comparison](identity-comparison.md) accounts
for all15 differing nodes in the two5794-node graphs;5779 complete node objects
match. The reproducible difference is target revision/version metadata and its
propagation plus diagnostic JSON/script. Both use the same target osctld63mr...
recipe, kernel/initrd/module and target test-shell inputs. The original
incident's gnf7.../5ya... recipes remain unavailable and are not reconstructed
by this comparison.

Recommend lead select the explicitly bounded old-writer state capture described
there. Exact rooted preparation command and post-preparation closure/image
measurements are in that comparison. Refresh no-build requirements first and
reject any new local builds outside the inspected216; no Linux/ZFS source build
is authorized. No realization or VM was launched by implementer3. Host runner
launcher preparation is still separate from realizing the selected config;
do not call launch fully prepared solely from JSON/image readiness.

## Lead-selected local preparation, no VM

Lead accepted the explicitly declared old-writer-state boundary after the15-node
comparison. New task-specific script [run-local-preparation.py](run-local-preparation.py),
SHA256 `4e8be96e1c15b460e03f143d0dd21a36f032168d68c363d9d4e4d0cfcd6ac94b`,
is prepared, not executed. Exact fresh-watcher launch, workspace cwd and matching
session environment:

```sh
python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/support/run-local-preparation.py
```

The script operates only on fixed store paths, with empty remote builders,
fallbackfalse, IFDfalse, at most2local jobs/4cores and16MiB native build-log cap.
It first roots the original6.12.95 **output path**, not its derivation, with
max-jobs0 and no remote builders: only substitution or already-local reuse is
possible. It checks its expected NAR hash. Then the refreshed dry-run must be a
subset of the approved216builders/178substitutes; newly local outputs shrink
the plan without requiring new approval. Any unknown requirement refuses.
During realization it also stops on advertised unapproved builds/substitutions.
The fixed3k708 configdrv is realized/rooted as gcroots/config.json; known
closure-info drv is rooted separately for actual measurement, without runner/VM.

Admission requires free space above64GiB (24GiB budget plus40GiB floor).
During each command it checks each second and initiates owned-client cancellation
at44GiB free, a24GiB shared-filesystem decline,20minutes total,64MiB retained
command output, or external INT/TERM/HUP. Shared free-space changes are not
attributed to this package. Cancellation targets only its recorded client
process group: INT, then TERM after10s and KILL after20s; up to30s reaping grace.
No detached monitor, global GC, foreign signaling or automatic cleanup exists.
If a Nix daemon build remains shared/uncertain after client cancellation, the
watcher reports that uncertainty; it must not signal unrelated daemon work.

On success it checks exact config output/hash, roots closure-info, records its
actual NAR bytes and squashfs apparent/allocated bytes, native machine JSON,
kernel image hash, complete config-output closure paths/physical du and owned
support du. More than5GiB closure/image exceeds the provisional forecast and
refuses VM admission. Receipts use local-preparation-1-*; a start marker prevents
silent retry. Roots kernel-6.12.95,config.json,closure-info remain until dependent
work ends; the script removes none. No attempt-1 VM state is created.

Final syntax/216-and178-plan parsing, normal owned-client exit and deadline
cancellation checks passed against harmless short Python subprocesses; both
clients reaped. [Quick-check receipt](local-preparation-final-guard-check.json)
binds the script hash. No Nix realization or VM occurred in those checks.

### Separate stock-runner and transport admission

Implementer1 reports existing valid stock runner
`/nix/store/mjlc8sc8qp6vpzf08r65jwl1y38jbgjm-test-runner`, deriver
`/nix/store/bpfa9x3qxbq6a795kp4lnvral15s5526-test-runner.drv`, direct JSON wrapper
SHA256 `c90f4d93145671d8cc0c6434b5b6cdeb65c84971f2f6fdfed87e23abd587d5f2`.
Closure37paths/313125960NAR bytes. Their root-only step is pending lead selection;
retention is not yet certified. Owner1 retains runner-cache ownership; this
script neither builds nor roots that runner. Receipts:
`../podman/runner-identity-1{.json,-wrapper.txt,-closure.json}`.

Independent support check: its JSON has no testShellTransport, so the stock
host defaults virtconsole. Its boot guest's exact graph service2a577...run
uses `/dev/hvc0`; these match. [Stock transport source](stock-runner-transport-source.json)
shows installed machine_config.rb/shell.rb byte-identical to846bb. The target's
service ryk6...run instead names `/dev/virtio-ports/org.osvm.shell0`. The module
sets onChange="ignore", preserving the existing shell during activation; the
selected first-switch diagnostic does not restart it. This is a continuity
dependency, not a claim that a newly started target shell would match this VM.
Legacy virtconsole can drop output under backpressure; malformed/missing capture
must remain a failed/incomplete observation, never an inferred state.

After selected realization, verify actual boot guest service and both transport
identities again before admitting a VM. Normal native prebuild via mutable
test-runner.sh is not selected. The existing native test-json-runner can use
the exact frozen prepared JSON without source resolution/rebuild; it retains
native Executor cleanup but omits Test.resources metadata, so scheduler admission
would reserve0. A direct-JSON launch therefore needs explicit external admission
of actual8192MiB RAM/SHM,4CPUs and one VM, plus lead acceptance of this native
entry point before launch. Preserve the original CLI's900s default command
timeout for this support case; helper/activation commands keep explicit bounds.
No stock runner readiness command that can boot a VM has been run here.

Preparation1 stopped safely on one additional fetch before config realization;
see [reconciliation](local-preparation-1-reconciliation.md). Lead accepted exact
same-graph61KiB stdenv output/hash and selected preparation2 from the distinct
f4d42... script with fresh logs. All216builder restrictions remain; no blanket
substitute approval. Implementer3 preserves source and makes no duplicate
observation while its fresh watcher owns execution. Owner1 has now confirmed
the shared runner root succeeded: native/overall0 in0.94s, exact mjlc8...output
and c90f... wrapper. Root ownership/retention stays with owner1/lead through
selected consumers; no duplicate root or build is created here.

Preparation2 completed and lead selected the frozen direct-JSON first-switch
guardian for the next one owned VM. Current exact command, measurements,
ownership/resource/cleanup limits and interpretation are in
[first-switch-vm.md](first-switch-vm.md). Source/guardian are frozen during the
lead watcher's operation; implementer3 makes no duplicate live observation.

Capture1 completed and compact evidence is retained at
[capture-1/findings.md](capture-1/findings.md). Actual pre-switch YAML/base versus
same-ID GC/held temporary root proves stale saved selection in this execution.
Post-import recorder failed on nil length-read; no post-root/data/API/equality
result exists. Native effects-ended independently reconciled, exact empty
scratch removed, slot-release proof sent lead; no baseline retry selected.
Reader implementation is unblocked by architect acceptance of raw root layout.

Lead authorized the one-line owned helper correction to normalize nil to empty
binary bytes. Worktree helper SHA2569da85be832bf52420267be875c39f47ff621031d9e367f4ebc0ecd957be61a3c;
frozen baseline/helper/JSON/capture unchanged. Actual-function regression
[check_capture_file.rb](check_capture_file.rb) passes empty bytes/hash/stat,
binary exact-limit/truncation and missing-file distinction; the identical check
against immutable old helper reproduces NoMethodError. Host and embedded guest
Ruby syntax pass; targeted RuboCop1file/nooffenses (existing renamed-cop warning).
See [check receipt](capture-file-fix-checks.json). Fold this caused correction
into the diagnostic fixture's logical owner under a later lead Git window;
no commit/Git mutation or VM/test rerun has occurred.
