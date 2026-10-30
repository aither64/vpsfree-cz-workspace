# Recorder shutdown correction

Source prepared under the lead-selected contract in `design.md`, **Selected
recorder shutdown correction after final review**. The separately selected
native C syntax/actual-helper compilation and **41-case mocked regression pass**
(exit0, 2.287s). Corrected packaged C/BPF build and runtime remain pending.
One selected Nix metadata operation subsequently evaluated the corrected
derivation and failed its post-check on JSON-v4 basename handling; the separately
selected retained-only checker passes without repeating Nix. No Git, Nix
realization, BPF, VM, hotplug or aging operation has run for this correction.
The reviewed original head remains `9bea27c93beb22d08c3be2eb481bce4ef57300a6`.

Only shipping `hotplug-recorder.c` and the existing CPU hotplug diagnostics
section of `docs/os/testing.md` changed. The documentation prefix and full
shutdown-diagnostics suffix match the authenticated original; the owned section
is now 28 lines. Qualification, BPF source, event header and Nix recipe retain
their recorded hashes. No pins, attach scheme, ABI, deadlines, size limits or
first-hotplug wiring changed.

The C path requires QUERY support for ordinary GLOBAL before attachment.
Shutdown disables the map, completes GLOBAL grace one, reads live perf-link
missed counters, destroys and nulls every acquired perf/raw handle, completes
GLOBAL grace two, then drains and checks stable statistics against output bytes.
Any failed barrier/destruction skips an authoritative final drain/accounting
claim, retains failure and still frees/closes owned resources. The existing
`probe=... missed=...` records remain compatible; a new `missed_scope` line and
comments/docs state the capture-window snapshot, conservative disabled-window
extras, and exclusion of full probe lifetime through destruction. A monotonic
abort latch prevents a later SIGUSR1 from upgrading an earlier abort, including
one delivered during cleanup. The exact-kernel/config RCU proof belongs to the
architect's design; no mock establishes that kernel guarantee.

## Frozen source and check inputs

All paths below are under this session unless a product path is named.

| File | SHA256 |
| --- | --- |
| Product `hotplug-recorder.c` | `4bf11e25f04d444b5af5ac4cc506ab566c13ba50d96e67bf2c72c5b774005b00` |
| Product `docs/os/testing.md` | `a5fddc497e44614a04478752b1b042e8c3848ef5c13506d77ced36798b8280bb` |
| `repair/hotplug/shutdown-check.c` | `cba46a46c6139080c4e45b934b3af4cf2a0e545921ce83b92409002a914dad94` |
| `repair/hotplug/old-shutdown.inc` | `3ee25442fb60badaabfe8a733fe673db647f8efcd2b767fe69f36c5923a616b2` |
| `repair/hotplug/run-shutdown-check-1.sh` | `81d831885f35457e9e4690cc18878ca3758a6eb68cc9072680bff94a8691722d` |

The old include is a mechanical extraction of the original `report_losses`
function and `done` block from the retained original C, authenticated SHA256
`fdbf4429808966f5bd1bfe9b6e3674a8daceb8cb8868be1291f499cb3edfae4f`.
Only its function wrapper and argument bindings are added. It gives the check
the actual old code order, rather than a separately rewritten faulty algorithm.

The prepared 41 controlled cases include raw/perf admitted events released at
grace one with final event identities and emitted/byte equality, a late missed
hit, pin-map-error released at grace two, partial/all-null handles, unsupported
or failed QUERY, each barrier failure, map disable, every one of 15 destructor
failure positions, missing/wrong-type counters, map/drain/write/cap/fsync/close
and byte-accounting failures, prior/late abort and SIGUSR1 completion. The old
cleanup must return success with two later events still queued, reproducing
false completeness. No sleep, actual BPF call or kernel membarrier is used.
The helper exercised by the check is the actual new `shutdown_capture`; only
native boundaries are faked. Session check files are excluded from shipping.

Completed preparation checks: Bash `-n` passes; old-source authentication,
documentation prefix/suffix preservation and unchanged four peer-source hashes
pass. Native syntax/compile logs are empty, and the actual mocked outcome is
recorded below. No live kernel synchronization or BPF result is claimed.

## Selected single native check, completed once

Exact argv selected by lead (source/check/script hashes frozen above):

```sh
DEV_SESSION_SLUG=2026-10-22-ci-failure-analysis \
DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz \
/run/current-system/sw/bin/systemd-run --user --scope \
  --unit=ci-failure-hotplug-shutdown-check-1 \
  --property=MemoryMax=1073741824 --property=MemorySwapMax=0 \
  --property=TasksMax=32 --property=CPUQuota=200% \
  /nix/store/bhv6xyvqw6gjs3j488gi1z6wdv18bdpa-coreutils-9.11/bin/timeout \
  --signal=TERM --kill-after=5s 120s \
  /nix/store/jnyfsf2mp08d1xyz2m72ic2vz2kcx0sd-bash-5.3p9/bin/bash \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/hotplug/run-shutdown-check-1.sh
```

The script authenticates the selected C/header/check/old-code/tool inputs,
performs native `-fsyntax-only` on the shipping C, compiles the actual-code
mock check, and runs only that check. It uses the already cached declared
GCC15.3 wrapper `dy6j7267...`, exact libbpf1.7 headers `l0j5869...`, and normal
libc. Uncalled loader code is discarded by section GC; no real libbpf is linked
for the mock. No Nix evaluation, substitution, realization or BPF compilation.

Disposable owned path is exactly
`/tmp/ci-failure-analysis-2026-10-22/hotplug/shutdown-check-1`, with child `tmp/`;
the script requires its absence and canonical owned parent, then writes ownership.
No metadata/output roots change. Expected physical growth is under 8MiB; selected
ceiling proposal is 128MiB including compiler temporary/output coexistence and
receipts, with independent 40GiB free floor. All tools are present; no closure
fetch/build forecast. Scope enforces 1GiB process-tree RAM/no swap, two CPU quota
and 32 tasks; all work is native in the scope, with no daemon-side builders.
Overall timeout is 120+5 seconds. Per-receipt streams are capped at 1MiB (three
logs, aggregate output under 4MiB); no process-wide file cap, core dumps disabled.
Script records start/end df/du and guards physical/floor between phases; continuous
sampling/cancellation during compilation belongs to the fresh selected watcher,
so sampled disk limits may overshoot. Failure retains artifacts with no retry.
After native process/group/cwd/fd effects are reconciled, retain compact check
evidence and remove only its stopped owned scratch if separately selected.

The previous q4 recorder and frozen admission image/launcher remain pre-fix and
held. A corrected packaged build is a separate bounded selection after this
check, using the unchanged recipe/header and a fresh exact drv/cache plan; never
reuse old binary success as corrected-source evidence. Git folding, all-eight
message work and targeted review remain lead-serialized; no new fixup commit.

## Actual native outcome and effects

Authoritative watcher evidence is
`shutdown-check-1-watcher-evidence/{identity,result}.json`, `samples.jsonl` and
bounded stdout/stderr. Native exit0/2.287s; scratch `exit=0`, syntax/compile logs
are empty. The 21,860-byte `check.log` ends with:

```text
PASS 41 controlled shutdown cases; actual cleanup; old false-complete reproduced; no BPF/kernel barrier execution
```

Mock executable SHA256 is
`6e4d378509a3a327e29a5549f42498d53b1926cca280cb39756c411fa0bdb39f`.
Five watcher samples measured scratch maximum139264B, watcher receipts16384B and
minimum shared free133745016832B; these are sampled values, not proof of an
unsampled peak. The selected scope supplied RAM/CPU/task limits. Original
reviewed head9bea identifies the source baseline; fixed C4bf11e25 and docs
a5fddc49 above identify the uncommitted tested correction.

Independent `shutdown-check-1-effects.json` at18:11:17Z verifies all six sampled
PID/birth identities and the watcher supervisor absent, no members of recorded
group569989, exact scope not-found/inactive/dead with its cgroup absent. No
readable canonical attempt/evidence/script/check/include/C/header references
remain among1519 examined processes. Permission gaps (2061 cwd/root/exe,
691 fd directories,2418 fd links) qualify this readable view; protected foreign
descriptors were not inspected. No signal, retry or cleanup was taken. Scratch
and compact evidence are retained as directed. Owner0 received exact PASS/hash
evidence with package/runtime limits via messageef5574c8.

## Corrected package metadata proposal, subsequently executed once

The following records the selected metadata proposal before its actual result
below. First proposed command is metadata only, using unchanged
recipe/header/locks and the tested C. Prepared script
`run-recorder-fixed-metadata-1.sh` SHA256
`4fb6dab45c1453c0d4cf8f0834ebab56ba29194913392ccb68512962c49f62f5`
passes Bash `-n`. It authenticates inputs, registers only the new metadata root,
records exact output/derivation and native dry-run cache plan, verifies the
copied four sources/header, and refuses any source build other than the new
recorder. It performs no realization. Exact proposal:

```sh
DEV_SESSION_SLUG=2026-10-22-ci-failure-analysis \
DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz \
/run/current-system/sw/bin/systemd-run --user --scope \
  --unit=ci-failure-hotplug-recorder-fixed-metadata-1 \
  --property=MemoryMax=1073741824 --property=MemorySwapMax=0 \
  /nix/store/bhv6xyvqw6gjs3j488gi1z6wdv18bdpa-coreutils-9.11/bin/timeout \
  --signal=TERM --kill-after=5s 300s \
  /nix/store/jnyfsf2mp08d1xyz2m72ic2vz2kcx0sd-bash-5.3p9/bin/bash \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/hotplug/run-recorder-fixed-metadata-1.sh
```

New owned attempt is exactly
`/tmp/ci-failure-analysis-2026-10-22/hotplug/recorder-fixed-metadata-1`, new root
`/tmp/ci-failure-analysis-2026-10-22/hotplug/gcroots/recorder-fixed.drv`.
The existing q4/boot/JSON/shared-runner roots are untouched; no roots enumeration.
Proposal bounds:1GiB physical including possible new source copies and metadata,
1GiB evaluator scope RAM/no swap,300+5s,8MiB per receipt and64MiB total output,
independent40GiB free floor. Start/end df/du are native receipts; the fresh watcher
must own continuous resource observation and cancellation. No daemon compiler is
expected or permitted; IFD is false, max-jobs0 and builders empty. Metadata/root
effects are retained for exact post-operation reconciliation, no auto cleanup.

Read-only filesystem checks found the original eleven cache-fetched tool paths
all absent now. The retained original dry-run was136.0MiB download/1.4GiB unpacked
(`repair/support/preflight-batch2-recorder-dryrun.log`), not a fresh cache promise.
The next metadata receipt must establish actual cache availability and any new
missing paths before substitution/build selection. No compiler, kernel, SDK,
ZFS or Nix source-build fallback is allowed.

Once exact identities/cache plan are accepted, the smallest separately selected
build uses the captured new drv, `nix-build --out-link` at a new corrected output
root, max-jobs1/cores2/builders empty/fallback false/IFD false, max-build-log-size
16MiB and540s native build timeout under600+5s outer. Use the default native
daemon-secure build directory, unlimited FSIZE/core0. Proposed cumulative bound
for metadata plus realization is4GiB physical (do not reset it between stages),
64MiB logs and a fresh40GiB floor. The initial3GiB aggregate sampled RAM proposal
is unresolved: root/nixbld observation is protected, and the client cgroup cannot
hard-limit or authenticate daemon-side builders. Architect/lead own its revised
contract before a final watcher package. Exact cache bytes and the unresolved
past-allocation limit determine whether the physical envelope is enough.
The unchanged recipe compiles native C and BPF with its existing warning/error
flags; CLI validation is `--help` exit0 and missing args/bad offset/unsupported
seconds each exit1, with no object load or attach. Record new loader/BPF hashes,
output NAR/physical/runtime closure; retain the corrected output root pending
separate admission. The runnable fixed build script can be finalized around
the actual drv/output after metadata; no guessed hash or actual build here.

## Metadata failure, retained-only PASS and independent build commands

Watcher3 ran the original4fb6 script once: native1/7.087s. Failed original
receipts/root are retained. The post-check failed at payload line6 because
Nix2.34 JSON-v4 `derivations` keys are store basenames, rather than absolute
paths. Output `path` is also a basename; `env.out` is absolute. This is a
validator assumption, not a source/build/kernel failure. No metadata rerun was
made, and original `selected-plan.json` remains absent.

Exact evaluated drv is
`/nix/store/zm13vhsm8d1rsfnxihpf6pqsvk4yrmhf-livepatch-first-hotplug-recorder-1.drv`,
SHA256 `0d5f02b10631902cddecd4144b01a8530a5f6792068ab76106dc6d48f65419ea`;
output is
`/nix/store/kpkcdfxp2g9w1a3s6z67ci7fvj36rnc8-livepatch-first-hotplug-recorder-1`.
Metadata root `gcroots/recorder-fixed.drv` still names this exact drv. The output
was not realized. The retained dry-run lists only that recorder source build
plus the same11tool substitutes (136.0MiB download/1.4GiB unpacked).

`check-retained-recorder-metadata-1.py` SHA256
`35fa6bc3cc9e96ced9fa6ed154c4495aa376a263029e2ce3efa8c086531a8747`
checks only authenticated retained receipts/copied source/header and strict
version4 identities. Lead selected its exact direct systemd/timeout/Python-I
argv once; it passed native0/0.159s, stdout2103B/stderr117B. New receipts are
`retained-metadata-check-1/`; stdout SHA256 is
`cef82d730042cef566112e6da47bd2abda359fd3691905f668a3f1c90ca32a94`.
No Nix, fetch, evaluation, root change or store write occurred in this checker.

The checker scope is not-found/inactive/dead with its cgroup absent. Its
launcher723328/birth1208840028 and group are absent; no readable canonical check
references remain among1508 examined processes. `effects.json` qualifies
protected descriptor views. Original metadata reconciliation is separately
`recorder-fixed-metadata-1-effects.json`: recorded launcher672813/birth1208784404
and group absent, scope/cgroup gone, no readable canonical owned references;
no supervisor/child identities were invented.

Retain the original watcher limitations: all16 cgroup member samples were empty
because its positional `--value` parser used `active` as the cgroup path; the
actual cgroup was the third line. The4908B metric sums `st_size`, not physical
allocation. Its condition omitted the selected independent shared-drop stop.
Native end-du was36864B, later45056B including final receipts. Hidden/cumulative
store materialization is unknown; shared decline is not owned allocation proof.
No metadata replay can repair these past observation gaps.

Independent source-bound build/CLI commands are prepared in
`run-recorder-fixed-build-1.sh`, SHA256
`dfc25761e685bf0aad405dcd04bbfe0058a7a1c82fab7613c5e96785565d61c3`.
Bash `-n` passes; the driver has not run. It authenticates exact drv/accepted
retained-plan/source/header, requires new attempt
`/tmp/ci-failure-analysis-2026-10-22/hotplug/recorder-fixed-build-1` and output root
`gcroots/recorder-fixed` absent, and reruns only a native current dry-run (no
evaluation) before any realization. The fresh plan must retain sole exact
recorder build and a subset of the eleven approved substitutes; any new source
build/fetch or fallback stops. Actual command inside the unselected driver:

```sh
/nix/store/z4wkkj3ncr69vgrb3020saqx1c8mfsjj-nix-2.34.9/bin/nix-build \
  /nix/store/zm13vhsm8d1rsfnxihpf6pqsvk4yrmhf-livepatch-first-hotplug-recorder-1.drv \
  --out-link /tmp/ci-failure-analysis-2026-10-22/hotplug/gcroots/recorder-fixed \
  --max-jobs 1 --cores 2 --builders '' --option fallback false \
  --option allow-import-from-derivation false --option keep-failed false \
  --option max-build-log-size 16777216 --timeout 540
```

The native daemon-secure build directory remains default; FSIZE unlimited/core0.
The script captures build/CLI native statuses, checks help0 and three parser1
cases only, then records loader/BPF SHA256, deriver/NAR hash/size/runtime closure.
No loader object/attach command is invoked. All roots/results are retained;
there is no cleanup or metadata-root removal in the script. Client log caps are
4MiB dry-run,16MiB build and1MiB each CLI/query receipt; native build log16MiB,
leaving margin within the proposed64MiB aggregate. Native540s build timeout and
proposed600+5s outer do not prove daemon effects ended on client exit.

**Initial dependency, now resolved for preparation below:** architect0 owned
the nonprivileged daemon-accounting/effects contract or explicit revised claim.
A bounded `sudo -n true` access probe requires a password; no privilege was
obtained. No names/timing-only association, local-store alternative, recipe
change, privileged retry or broad framework is proposed. The driver is only
the independent exact drv/cache/CLI preparation, not the pending resource guard.

Known current full physical references measured independently by `du -s -B1`
are metadata attempt45056B, watcher3evidence40960B, retained checker45056B,
native shutdown-check147456B, its watcher evidence24576B, copied source45056B,
header2772992B and drv4096B: subtotal3125248B for these named paths. This is not
exclusive/new growth or a complete cumulative-store upper bound. Future
accounting must carry prior known allocations monotonically, including receipt
growth, without deletion/GC/refund discounts, and disclose unknown past store
materialization independently from shared movement. Final memory/CPU/disk
cancellation, exact child and daemon-builder ownership, correct named cgroup
parsing, physical `st_blocks*512` samples, independent shared-drop cancellation
and effects escalation remain the architect/lead prelaunch dependency.

## Selected revised tripwire: frozen build package ready for inspection

Lead explicitly selected the architect's whole-service contract recorded in
`design.md`. The earlier per-builder identity/RSS promise is withdrawn. The
[exact watcher brief](recorder-fixed-build-1-watcher-brief.md) is now the current
prepared execution package, not permission to realize it.

Frozen gated driver SHA256 is
`0d0b9e3768f0f3375474c649a6087f6d43c8be58eb656fd415a7f170428e986e`;
fixed guard SHA256 is
`2d2e8466a7cbe8595d45c13002330d4fd31d9eaf1f76053b8076316407a669cd`.
The source-bound drv/output/cache/CLI commands remain unchanged. The driver
waits on the guard's private admission FIFO before any Nix command. The guard
binds fresh named daemon MainPID/birth/InvocationID/cgroup device-inode and owned
client PID/birth/group/scope identity, reads all five required memory files,
verifies hard client1GiB/noSwap, and admits only below the sampled whole-daemon
plus client3GiB threshold. There is no baseline subtraction or claimed hard
builder aggregate. Child PID/birth snapshots are from the actual client cgroup;
daemon builders remain protected/unattributed.

Known physical samples are st_blocks*512 with monotonic per-path maxima;
shared-space decreases are separately accumulated without refunds from later
increases. Known4GiB and shared-decline3GiB stops plus fresh43GiB admission and
40GiB floor are explicit, without claiming unknown past/hidden allocation fits
a cumulative4GiB bound. Visible receipts/logs have48MiB stop plus16MiB native
Nix log reservation within64MiB. Native build540s/client600+5s are preserved;
guard loss/breach sends INT only to the birth-authenticated owned launcher.
Five-second unresolved cancellation escalates while keeping watcher ownership;
no guessed builder or daemon signal, automatic cleanup or retry. Native timer
completion does not prove protected effects ended.

Bash syntax and the guard's inert self-test pass for the frozen hashes. Tests
exercise named/reordered fields, required-field loss, hard-limit refusal,
summed-threshold equality, disk/log boundaries, no-refund behavior and process
birth mismatch. They execute no subprocess, Nix, filesystem inspection or
signals; guard run mode has not run. The new script is fixed to this one
operation, without recipe/local-store/privilege/API investigation or a general
monitoring framework. Source C4bf11e25/docs a5fddc49 and failed metadata/root,
old runtime/boot/JSON/runner roots are preserved. Execution needs lead inspection
and one fresh selected watcher; no realization, Git or runtime is authorized.
