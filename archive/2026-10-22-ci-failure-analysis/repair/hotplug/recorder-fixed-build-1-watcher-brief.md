# Fixed recorder build1: diagnostic-only source package

**Diagnostic-only source preparation. No next operation selected.** The original
frozen guard7b298d45 ran once: helper1/1.341s, native-2, admitted=false. It retained
an empty assertion cause, collected scope and no readable known survivors. No
package build/output/CLI validation was accepted. This delta adds failure evidence
without changing admission predicates, paths, native graph or resource policy.
Lead must separately select any future operation, its fresh paths and watcher.
Do not run this guard against the preserved failed build1 paths or replay metadata.

The architect's selected shared-service contract is in `design.md`, **Corrected
recorder realization monitoring, lead-selected contract adjustment**. This
package replaces the unproved per-builder RSS/identity promise with the selected
coarse whole-service tripwire. It makes no kernel/runtime admission claim.

## Frozen identities and command

| Input | SHA256 |
| --- | --- |
| `watch-recorder-fixed-build-1.py` | `506bdb380f786c0bcbf377dbea1f0925009b2e5b1a6942c40a7ea2cce4126849` |
| `run-recorder-fixed-build-1.sh` | `01eee7e332c11de0c217b74740815c021003607b2881cd41c565bea3a177d1d3` |
| Exact immutable `zm13...drv` | `0d5f02b10631902cddecd4144b01a8530a5f6792068ab76106dc6d48f65419ea` |
| Accepted retained-plan stdout | `cef82d730042cef566112e6da47bd2abda359fd3691905f668a3f1c90ca32a94` |
| Shipping C | `4bf11e25f04d444b5af5ac4cc506ab566c13ba50d96e67bf2c72c5b774005b00` |
| Shipping diagnostics docs | `a5fddc497e44614a04478752b1b042e8c3848ef5c13506d77ced36798b8280bb` |

Worktree is exactly
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-ci-failure-analysis/vpsadminos`.
Tracking is exactly
`/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis`.
Reviewed Git9bea is a baseline containing the old committed C; the selected
working-tree C4bf11e25 and immutable copied source are authoritative. Do not
compare the coordination repository's HEAD or committed fdbf C to this selection.
No Git operation is needed for this fixed drv build.

Before execution, verify the thread binding with `dev-session current`, both
environment values matching or absent as policy permits, exact absolute hashes,
and absence of the three new paths below, including dangling symlinks. No other
operation owns these paths. Do not run Nix to discover the derivation again.
The following argv is retained for provenance only. Its build1 paths have been
used; **do not launch it**. No new paths or execution identity are allocated by
this diagnostic correction (environment applies to this historical invocation):

```sh
DEV_SESSION_SLUG=2026-10-22-ci-failure-analysis \
DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz \
/nix/store/jy00n3jp5xj8s40n1fbldmkcr5n7avxc-python3-3.13.15/bin/python3.13 -I \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/hotplug/watch-recorder-fixed-build-1.py
```

Do not append a period, `--self-test`, another argument or a shell source path.
A separately selected guard operation would own one native systemd-scope launch. Its exact native argv is
the literal `LAUNCH_ARGV` array in the guard: named client scope
`ci-failure-hotplug-recorder-fixed-build-1.scope`, hard MemoryMax1073741824 and
MemorySwapMax0, client CPUQuota200%, native timeout INT600s/kill-after5s, prepared
Bash/driver. The guard's admission FIFO blocks the driver before any Nix command.
The actual driver first writes its PID/birth and immediate timeout-parent PID/birth through
an atomic private handoff. The guard independently verifies both exact cached
executables/argv, their immediate parent relation, driver/timeout membership in
the named client cgroup, and ancestry to the retained Popen PID/birth. It accepts
the observed exec or synchronous-parent launch form; it assumes neither a
launcher PID nor signal forwarding. Failed or missing handoff remains unadmitted.
Required cgroup/service identities, memory fields, hard limits and resource
checks also precede FIFO release. Native driver `--timeout540` applies to the
selected build.
No recipe, source, ABI, module, pin, SDK or local-store change is involved.

## Actual graph and build/CLI scope

Exact drv:
`/nix/store/zm13vhsm8d1rsfnxihpf6pqsvk4yrmhf-livepatch-first-hotplug-recorder-1.drv`.
Exact output:
`/nix/store/kpkcdfxp2g9w1a3s6z67ci7fvj36rnc8-livepatch-first-hotplug-recorder-1`.
Metadata root `hotplug/gcroots/recorder-fixed.drv` is retained and authenticated.
Source `rvh27pyjc9q22adsqmarmkrb5xmy6x03-source` has the copied four hashes,
including fixed C; exact copied header `l61xkjj7...-hotplug-vmlinux.h` is
82ac9ea144b1f92f35b8cc2eb947ce672cfca6d06a60fe9e925a40ff30e51484.
Both were checked by retained-only native0/0.159s, no Nix replay.

The captured plan is one source build plus eleven tool substitutions,136.0MiB
download/1.4GiB unpacked. The driver first performs a fresh native dry-run against
the exact drv; it accepts that sole recorder build and only a subset of those
eleven paths in authenticated `retained-metadata-check-1/stdout.log`. Any other
source build/fetch stops. No kernel, ZFS, Nix, compiler or SDK source fallback.
Actual build: max-jobs1/cores2, builders empty/fallback false/IFD false, native
daemon-secure default build directory, keep-failed false, native log16MiB.
Max-jobs/cores and client CPU quota do not hard-limit daemon CPU; possible daemon
CPU activity is disclosed, no affinity or exclusive capacity claim.

After C/BPF compilation, only `--help` exit0 and missing arguments/bad offset/
unsupported seconds exit1 run. Each stops before valid object loading. No BPF
load, verifier, attachment, count experiment, VM, hotplug, population or aging.
Record loader/BPF SHA256 and native output deriver/NAR hash/size/runtime closure.

## Resources and implemented cancellation

The guard binds fresh `nix-daemon.service` MainPID/birth, InvocationID and canonical
`/system.slice/nix-daemon.service` device/inode. It reads named ControlGroup
properties, never positional `--value` fields. It retains the Popen launcher
handle and its PID/birth, then authenticates the
actual Bash driver and its immediate cached native timeout parent. Exact driver
argv is `[cached-bash, absolute-driver-path]`; timeout argv is the cached
coreutils timeout with `--signal=INT --kill-after=5s 600s`, cached Bash and the
absolute driver path. The observed timeout is either the Popen process itself
or its immediate child under the exact systemd-run executable/argv. The guard
records the resolved systemd-run executable before launch; Bash and timeout are
fixed cached paths. Both actual driver and timeout must be in the named scope.
The launcher may remain their parent outside that scope. The helper records
scope InvocationID/device/inode and actual child PID/birth/group/command
snapshots. It does not identify protected daemon builders.

Required readable fields in each cgroup are memory.current, memory.peak,
memory.events, memory.max and memory.swap.max. The client limits must be exactly
1GiB/zero swap before releasing the FIFO. Before launch daemon current must be
below3221225472B; before admission and during execution the cancellation threshold
is the sampled sum of the WHOLE named daemon memory.current and client
memory.current, with no baseline subtraction. Includes foreign activity and
charged cache; may false-cancel. Required field/identity loss or sum>=3GiB refuses
admission/cancels only the authenticated native timeout PID/birth with SIGINT.
No signal targets the service or a guessed builder. Independent lifetime peaks
are context, not simultaneous aggregate peaks. The two reads are non-atomic;
no per-builder RSS, hard aggregate, containment or unsampled-peak proof.

Physical accounting uses `st_blocks*512`, without following symlinks. A per-named-
path maximum starts from all retained metadata/check/evidence/source/header/drv
paths and adds the new watch/build/output/eleven-cache paths. Maxima never shrink
or credit deletions/GC. Known measured files>=4GiB cancels; hidden/past sandbox/
store materialization is unknown, so this is not a4GiB cumulative-owned proof.
The previous named-path subtotal3125248B is a measured subset, not a whole-store
upper bound; the guard remeasures it and retains maxima.

Fresh shared free must be>=43GiB. A40GiB floor applies throughout. The independent
shared-decline stop is3GiB: sum only sampled decreases and never subtract later
increases, so foreign frees cannot refund observed declines. Shared movement
may include foreign work and cause false cancellation; unobserved movements can
be missed and it is not owned-allocation proof. This reserves1GiB admission
margin relative to the previous4GiB proposal, without pretending past unknown
allocation was measured or bounded. Expected newly fetched/compiled physical
cost is below3GiB, based on1.4GiB unpacked tools plus download coexistence,
registration/inode rounding, tiny source/output and logs; actual peaks remain
sampled and qualified.

Sampling target is0.5s, with actual elapsed timestamps; native property reads and
filesystem walks can lengthen it. The observer itself is outside the hard client
scope. Native client timeout is600+5s; protected daemon effects are not bounded
by that timer. At a tripwire, send SIGINT directly to the authenticated native
timeout only while its PID/birth still match. PGID/cgroup are observations, not liveness or
direct-PID authority. Changed group/scope retains that surviving owned birth and
causes cancellation/incomplete evidence; it never grants group-signal authority.
After5s without reconciled client completion, emit escalation
and keep the helper/watcher owning the run. No additional KILL or unsafe signal
fallback: native timeout's selected own-client kill-after is distinct from
permission to signal the service. Surviving readable client children or scope
keep observation active even if the original parent exits. Report to lead while
retaining the watcher; do not claim timeout/cancellation proves protected effects
ended. Roots/evidence remain for owner reconciliation.

Visible receipt/log stop is48MiB, with16MiB reserved for Nix's native capped log
within64MiB aggregate. Guard stdout/stderr capture<=1MiB and samples<=8MiB;
driver caps4MiB dry-run,16MiB client build log and1MiB each CLI/query. Core dumps
disabled/FSIZE unlimited. Nothing imposes a log-sized process-wide file cap.

## Owned paths, result and handoff

Historical build1 preconditions (the watch path now exists and is preserved):

- `/tmp/ci-failure-analysis-2026-10-22/hotplug/recorder-fixed-build-1-watch`
- `/tmp/ci-failure-analysis-2026-10-22/hotplug/recorder-fixed-build-1`
- `/tmp/ci-failure-analysis-2026-10-22/hotplug/gcroots/recorder-fixed`

Watch dir700 contains ownership, admission FIFO, the atomic driver-handoff.json,
authenticated-handoff.json, identity.json, cgroup-binding.json, samples.jsonl,
bounded stdout/stderr and result.json. The diagnostic delta also defines a
first-failure.json receipt of at most64KiB. Native build dir, if a later separately
selected operation reaches it, contains exact command
statuses/logs, output hashes/closure, df/du and native exit. A passing guard
result requires native0 with no cancellation reason and readable client scope/
recorded children reconciled; it still makes no ended-protected-effects claim.
Refusal/failure preserves artifacts/root state, without automatic retry/cleanup.

The fresh utility must capture its exact helper launch/exit/elapsed once and
return raw artifacts to lead promptly. After native completion perform one
bounded readable canonical cwd/exe/fd scan for the exact watch/build/driver and
corrected output/root references, retained births/groups/scope; record permission
gaps. Protected daemon views remain uninspected. Do not enumerate Nix roots
(that earlier query pruned foreign notification links). Owner2 independently
reconciles after lead delivery. No root cleanup, store deletion, foreign signals,
branch work, source edit, retry, diagnosis or further build by the utility.

Corrected output root is retained for separately selected admission; metadata,
old q4, boot, JSON and shared-runner roots are preserved. This operation does not
refresh the old admission image or authorize a first-hotplug/aged experiment.

The diagnostic delta is frozen for lead acceptance. Original accepted
driver01eee7e3/guard7b298d45/brief632866fe bytes and full hashes were preserved in
[recorder-fixed-build-1-diagnostics](recorder-fixed-build-1-diagnostics/), together
with a byte/mode/target inventory of failed watch1, raw utility receipts and the
metadata root. These inputs remain unchanged. The earlier prelaunch correction's
original0d0b9e37/2d2e8466 evidence remains separately retained. Only this guard,
this brief and own evidence changed; the driver and all shipping inputs did not.

Every native guard assertion now has an invariant stage/name and explicitly
selected expected/observed fields. All58 original assertion predicates remain
present, with only single-read aliases expanded for AST comparison. The helper
retains the first latched failure's operation stage, invariant, source location,
up to five file/function/line traceback frames, and bounded relevant query rc,
scope properties, identity and attempted handoff/revalidation observations.
There is no frame-local, environment or source-line dump. Diagnostic strings,
collections and JSON are bounded; no unbounded raw query output is retained.

A first-failure.json write is attempted once, including before the first sample.
The same immutable first cause is carried into result.json. Later successful
authentication cannot replace it. A diagnostic write failure remains secondary
and uses the existing bounded stderr fallback with first-failure stage/name/
location; it cannot upgrade the run to success or unwind supervision. Admission,
signalling, scope collection, cancellation and all resource thresholds remain as
previously selected. This does not recover the first attempt's missing failure
observation or establish its root cause.

Actual permitted checks: Bash `-n`, guard AST, no remaining unnamed native guard
assertions; **PASS149 inert assertions**. New actual-control fixtures require
exact first-failure stage/name/data for first-iteration scope and authentication
failures and a changed second handoff read. They prove first-cause retention
through later valid authentication, preserve pre-FIFO expected/observed PGIDs,
and cover diagnostic-writer failure and the actual bounded stderr fallback.
Native entry points are poisoned or explicitly faked. The self-test performs no
real subprocess, filesystem inspection, signal, sleep, Nix, build or runtime
operation. The final check group exited0 in0.21996562s (tool wall time).
These checks establish diagnostic control behavior with fakes, not systemd or
kernel runtime behavior. No new operation identity, retry, build, evaluation,
fetch, Git action, cleanup or owner0 final validation/freeze is selected.
