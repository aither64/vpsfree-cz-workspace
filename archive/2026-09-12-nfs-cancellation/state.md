---
lifecycle: abandoned
---

# NFS cancellation repair

## Abandoned on 2026-09-17

The user explicitly requested cleanup and abandonment. Development and
verification are stopped. No implementation was merged into a default branch
or deployed. Branches and source worktrees are retained; the session has not
been archived, deleted or stopped.

Cleanup removed 15 recorded disposable VM directories, the session scratch
area and its Nix output roots, and the OS worktree's generated .native, .gems
and result directories. No shared Nix-store garbage collection was invoked.
All build/VM jobs and branch CI had already finished; one stale review git
search was terminated. Curated crash traces, passing protocol/legacy logs,
object-build checks and final 6.12.109 build output paths are retained in evidence/.
See [abandonment.md](abandonment.md) for final heads, limitations and cleanup.
The remaining work described below is historical and will not be pursued.

## Implementation at abandonment

User authorized implementing the accepted plan and explicitly directed fixing
our existing 6.12.95 kernel entry. No new version entry or livepatch variant.
The daemon implementation and two mandatory review rounds are complete. All 44
protocol cases pass on the preceding 109 candidate, but migration exposed a
regression in our RPC sysfs follow-up on both kernels. Its correction and the
focused general/architecture/risk review are complete; one architecture finding
was fixed by moving sysfs setup into RPC registration. The corrected 6.12.109 builds completed, but runtime tests did not run.
The corrected 6.12.95 source download remained rate-limited, leaving its
downstream pin and replacement builds unfinished. See implementation-review-reconciliation.md. No production
deployment or default-branch integration has occurred.

| Repository/worktree | Branch | Base | Current head |
| --- | --- | --- | --- |
| vpsadminos | 2026-09-12-nfs-cancellation | 15802517e2d92dda4ddc07ebac3d1d7ea087b430 | 18332a06dda48702d0421eff8d9dc31fdd298b85 |
| linux | 2026-09-12-nfs-cancellation | 9ccd5d6597a6ddbe5b44fb885ddf96e4dbc332dd | 7c66ab3c284a5fb5b615f874a99cb16501d6de23 |
| linux-6-12-95 | 2026-09-12-nfs-cancellation-6-12-95 | 563bbb35e8753e1bb34dad19ebeec8962ee3c1cd | a2bdcc5b5067dcb7b8f36ef955cd6ee29c9c215a |

Worktrees are under `worktrees/2026-09-12-nfs-cancellation/`. Linux heads are
pushed. The corrected 6.12.109 archive is verified and pinned; the 6.12.95 archive
fetch failed with HTTP 429. The local OS amendment is not pushed and still
pins the preceding 6.12.95 candidate. Its
latest origin/staging fetch is unchanged at the base above. OS commits separate
userspace behavior/native tests/docs, kernel pins/identity fixture, and VM
regressions with diagnostic outputs/cache publication. No dependency changes,
so gem metadata regeneration is unnecessary.

## Changes

- Both kernels retain a stable network namespace reference for published NFS
  sysfs objects. Initialization errors drain sysfs before client teardown;
  migration retains the original namespace; final allocation release follows
  the kobject release callback, including delayed debug release.
- Default 6.12.109 receives full namespace-tree cancellation plus the locked
  NLM helper prerequisite. Annotate RPC-client initialization for fault injection.
- Existing kernel entries point to the repaired sources. Retained nfs-cancel
  module is rebuilt against the exact base. Legacy a238 boot fixture unchanged.
- osctld uses only shutdown_tree when available, re-probes capability, persists
  original authenticated namespace pins and terminal intent, and restores them
  before monitoring. Missing/unprovable state disables cancellation for that
  run while ordinary killing remains available.
- Shared forced-stop orchestration budgets cancellation headstart (5 seconds),
  worker lifetime (30), and total forced stopping (60). Cancellation/freezer
  errors still reach killing. Recovery begins on LXC failure or by second 50.
- VM fixtures explicitly cover repaired 95/109, diagnostic builds, older-kernel
  cgroup v1/v2, init namespace departure plus restart, failure/unmount sysfs races.

## Quick verification

- Focused osctld suite: 213 examples, zero failures, seed 62810. Includes native
  namespace sidecar/coalescing tests, PID/run identity, unsupported controls,
  monitor/pre-mount, all forced-stop entrypoints, distribution handlers, and
  real subprocess EOF/timeout/oversized-response cases.
- Daemon and daemon CLI: eight examples, zero failures, seed 8028.
- RuboCop: 23 affected files, no offenses. Every OS commit ran Overcommit;
  Nixfmt and RuboCop hooks pass. Commit text-width warnings are advisory; all
  lines satisfy the repository's 80-character maximum.
- Packaged osctld build passes from the exact feature source using repository
  overlays and patched Ruby. No kernel was built by this package check.
- Both C helpers compile with -Wall -Wextra -Werror. Evaluated generated Ruby
  scripts for diagnostic NFS and legacy fixtures both pass ruby -c.
- Nix testsMeta evaluation includes all seven intended NFS/legacy/identity
  instances. Retained/default and default diagnostic toplevel derivations
  evaluate with new pins. This is evaluation, not a kernel build or VM pass.
- Retained Linux checkpatch: zero errors/warnings. Default final check: zero errors, one generic new-file/MAINTAINERS warning;
  the new ABI document is explicitly covered by the updated NFS entry.
- Existing retained cumulative livepatch inputs apply in sequence to repaired
  source; frozen historical boot fixture has no diff. Building the module and
  exercising exact/mismatch guards remain outstanding.
- Official GitHub release API verified checkout v7.0.1 and install-nix-action
  v31.11.1 when updating kernel workflow. Diagnostic outputs now publish there.

Reproduce native suite using `nix develop .#vpsadminos --command bash` with
`scratch/run-unit.sh` and the focused spec paths recorded in that script/logs.
Use this dev shell's patched Ruby for native extensions. Keep dev-shell entries
serialized because its Bundler installation shares `.gems` in the worktree.

## Review and remaining verification

Mandatory classification: high (host behavior, tenant isolation, persisted state,
kernel ABI and mixed-version operation). Review model gpt-5.6-sol, xhigh; general,
architecture, scope and risk lanes required. Packet: implementation-review-packet.md.
Both four-lane review rounds completed. Blocking and Important findings are
remediated as described in implementation-review-reconciliation.md. Userspace
is committed in 123711f64; initial pins in 64fb63cef; VM fixtures in 2bb3c251b;
real migration coverage and final kernel pins in af42c679c. Latest focused
verification passes 259 daemon and 24 library examples, plus 36 pool/console
examples after the frozen restart fix. Required hooks and full RSpec CI pass.
Kernel archive hashes were recomputed after the final RPC-link refresh.
Both real old-kernel compatibility VMs and the historical AMD livepatch VM
pass. Final repaired normal/diagnostic kernel builds and their VM matrix are
pending. Real migration preserved data on the preceding repaired kernel and
exposed stale sysfs links; their repair has a committed regression. A focused
concurrent replacement/shutdown probe is prepared and awaits the final build.

All feature heads are pushed. Draft PR creation to staging was retried but
GitHub rejects createPullRequest with the current token; branch CI still runs.
Continue the repaired normal/diagnostic NFS fixtures, matching/mismatched
identity tests, and the historical Intel lifecycle. Investigate failures before
reruns. Do not treat a native test or successful Nix evaluation as VM validation.

## Compatibility and rollout

Userspace works with older kernels and can update first without reboot. Boot
repaired kernels incrementally; no coordinated fleet update. Kernel repair is
compiled into the base and requires reboot. Old osctld ignores the sidecar;
rollback loses cancellation persistence/forced-stop guarantees. Namespace pins
may remain until reconciliation/reboot. Terminal kernel cancellation is sticky.

## Earlier investigation and operational notes

Initial tracking commit: 941bf0a. Original findings remain in review.md,
backward-compatibility.md and verification.md; their selection artifacts describe
the pre-repair state. CI 34630335805 actually booted 6.12.109 and oopsed through
legacy shutdown_store/rpc_cancel_tasks; exact stale pointer unproven. The 6.12.95
initialization unwind race is independently source-proven.

Linux bare clone has ~64k promisor packs. A multi-pack index improved lookup;
first diff/commit/push operations can still take minutes. Do not repack/remove
shared objects or other sessions' artifacts. See the initiative's Linux note.
Overcommit partial commits reject unrelated intent-to-add entries; keep future
new files untracked until their actual commit instead. Sequential livepatch
application matters: two patches in one --check do not compose their effects.

## Session and artifacts

Leave session open: no archive, delete, stop, or scheduled cleanup. Owned native
build artifacts `.native/` and ignored `.gems` remain for verification. Scratch
contains reproducible logs/source captures and is not a portal artifact. Shared
root has unrelated working changes, which were preserved. Initial tracking is
committed; consolidate later checkpoints under workspace policy.

Stable portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-12-nfs-cancellation/

Read-only CI preparation: Actions run/job metadata is accessible; runner
inventory API returns token-scope HTTP 403. This does not block feature CI.
Base staging CI 34688125397 built successfully and passed AMD/Intel historical
livepatch lifecycle jobs; its general VM job failed only NFS cancellation and kernel identity, confirming
the same two failures this initiative repairs (full failed-job log inspected).

## Current build and review checkpoint (13:11 UTC)

All six generated NFS and legacy test scripts parse at OS 5e586fbf6. Final
packaged osctld builds to /nix/store/yh19iad464fkk2ixf3qpk9yfgwsmiy3h-osctld-26.05.0.
Both cumulative livepatch inputs apply sequentially to final retained source.
Second review packet is implementation-review-packet-v2.md; fresh general,
architecture and risk reviewers are running, with scope queued for capacity.
The rerun is justified by the changed parent-Recovery/external-command boundary.

Started local compilation with `nix build .#ci-toplevel-kernel-6_12_95 --no-link
--print-out-paths --max-jobs 4 --cores 16` at 13:11 UTC. Local kernel rebuilding is
intentional because this initiative changes the kernel source; CI has not yet
published these revisions. This compilation overlaps review; VM integration
remains gated on completed review. Logs: scratch/kernel95-build.log and .out.
CI/cache publication will still be verified after the feature push.

Migration runtime prototype is prepared in scratch/migration-prototype.rb;
see migration-validation.md. It is unexecuted and not committed product code.

Second-pass reviews completed; all lanes independently reported the same two
remaining gaps (transient-PID completion barrier and unbounded parent/state lock
acquisition). Narrow owner-level remediations are in progress; see reconciliation.
No additional kernel source findings. Scope's advisory no-deadline EOF behavior
change was removed. No third review rerun is needed for these direct fixes.

First retained build failed before compilation because GitHub archive download
returned HTTP 429. Investigation also found the pin prefetch had used unpacked
NAR hashes although this repository uses fetchurl's flat archive hash. Re-prefetched
compressed archives from GitHub's codeload endpoint with exact fetchurl names,
compared extracted fs/nfs/sysfs.c bytes against each committed source, corrected
both pins, and restarted the build using the now-cached exact archives.
Correct flat hashes: retained sha256-4HdPnxHLB5UlhkeFz6upt++NPOf5zXQu0xHEPQZpGv0=;
default sha256-SYqViJCugtDarN9JFdLBj4K2fMqbx+JykdLlGK0biZ8=.
The replacement build is scratch/kernel95-build-flat.log; its kernel configuration
phase passes. This is a investigated retry, not an ignored source-fetch failure.


## Published implementation and integration (13:32 UTC)

All code is committed in the three OS commits at the current table heads and
pushed over SSH. Both review rounds are reconciled; direct fixes passed 259
focused daemon examples (seed 47201), 24 libosctl examples (seed 14917), the
container spec after fixture/style cleanup, and all required Overcommit hooks.
Only .native/ is untracked in the project worktree. No default branch merged.

CI run 34696541621 and RSpec run 34696541624 are running at 0f085bfea; RuboCop run
34696541630 passed. Draft PR creation is blocked by the available GitHub token:
both gh pr create (GraphQL createPullRequest) and REST POST /pulls return
Resource not accessible by personal access token. The exact reviewable title/body
are prepared in scratch/pr-body.md. No approval question is needed for ongoing
implementation/testing. The kernel-specific workflow currently triggers on
staging push or pull request, so its feature run cannot start through this token.
General push CI still builds and publishes the default kernel. Local builds of
other intentionally changed kernels continue; no broad CI trigger policy change.

Started real legacy-kernel VMs with ./test-runner.sh test --no-destructive
--state-dir <initiative>/scratch/vm-legacy -f --jobs 2 'osctl/forced-stop-legacy*'.
This tests cgroups v1 and v2 on 6.12.48. Logs: scratch/legacy-vm.log and vm-legacy/.
Repaired retained kernel compilation continues in scratch/kernel95-build-flat.log.
Its intermediate OS closure is from pre-final dirty source; only the kernel and
livepatch outputs are reusable evidence. VM tests must use the final committed
OS source, rebuilding the small closure as necessary.

Legacy VM attempt 1 failed before either guest booted: the deep state directory
produced a 121-byte UNIX socket path (108-byte limit). Logs were inspected and
preserved under scratch/vm-legacy. Rerun uses a unique short /tmp path recorded in
scratch/legacy-state-path.txt, with log scratch/legacy-vm-short-path.log.
No product change was made for this invocation error.
Started the 6.12.95 diagnostic kernel build at final OS 0f085bfea, max-jobs 2,
cores 12; logs scratch/kernel95-debug-build.log/.out. This source/config is
intentionally changed, so local compilation is authorized while PR-only cache
publication is unavailable through the current GitHub token.

## Runtime findings and build progress (13:55 UTC)

RSpec CI passes at both 0f085bfea and a9546fe13. Kernel CI 34696541621
failed fetching the source archive with HTTP 429. Added the equivalent GitHub
codeload URL as a fetchurl mirror in the existing Linux package wrapper; normal
kernel output identities remain unchanged. Run 34696973051 also failed before
compilation: both endpoints return HTTP 429 on gh-runner1. Exact archives are
cached locally and local codeload HEAD returns 200. Existing SSH access to this
runner is denied for aither and root, so no runner cache change was made. Full
failed logs are retained under scratch/ci-<run>-failed.log. Local builds continue
because kernel sources/configuration are intentionally changed by this task.

Legacy VMs did boot. Non-frozen kill/restart/reuse passed on both cgroup v1 and
v2 with kernel 6.12.48. Both frozen cases killed processes but timed out on exit
completion. Guest logs show Pool#load_cts reconnects tty0 only for :running,
skipping :frozen; no console completion callback then fulfils the new promise.
The narrow fix restores the same console path for :freezing/:frozen. Existing
VM regression already exercises the failure. No completion barrier is bypassed.
Failed guest diagnostics were collected; after guest poweroff stalled, only the
two verified QEMUs belonging to this failed test attempt were terminated. The
development session remains open and its tracking/worktrees are preserved.

Diagnostic retained configuration failed because DEBUG_KOBJECT_RELEASE depends
on DEBUG_OBJECTS_TIMERS, itself depending on DEBUG_OBJECTS. Added both explicit
prerequisites after checking exact 6.12.95 Kconfig. The corrected configuration
build is scratch/kernel95-debug-build-v2.log. Default 6.12.109 local compilation
is also started in scratch/kernel109-build.log; retained normal compilation
continues in scratch/kernel95-build-flat.log. No kernel/diagnostic VM pass yet.

Frozen console and diagnostic dependency fixes were folded into their owning
commits and pushed with explicit lease at OS 2bb3c251b8be913363b11809a2c0793213820ba2.
Final series: userspace 123711f64, pins 64fb63cef, tests 2bb3c251b.
Quick pool/console checks: 36 examples, zero failures, seed 10994; both commits'
hooks pass. Corrected retained diagnostic configuration passes and compilation
has started. Default normal compilation has started; default diagnostic build
is now scheduled too. Current CI 34697775063 / RSpec 34697775040 are in progress,
RuboCop 34697775067 passes. No superseded branch workflows remain active.
Legacy rerun uses scratch/legacy-vm-v4.log with short state path recorded in
scratch/legacy-state-v4-path.txt and default 900-second boot timeout. Attempt v3
was interrupted before guest launch to undo an unnecessarily short invocation
boot timeout, after the prior log proved boot takes over five minutes here.

## Legacy compatibility passed (14:09 UTC)

At OS 2bb3c251b both real 6.12.48 VM tests pass, cgroup v1 and v2.
All four examples pass, including non-frozen/frozen containers, osctld restart,
explicit kill, a subsequent start, and payload write/read. Runtime was 668s
including guest boot and image preparation. Logs: scratch/legacy-vm-v4.log and
/tmp/nfs-cancel-legacy-v4.UADM6N. This confirms the pool console-reconnect fix.
Full RSpec CI 34697775040 and RuboCop 34697775067 also pass at this exact head.

CI 34697775063 repeats the source-fetch HTTP 429 before compilation; full failed
log inspected. Historical livepatch attempt also failed before boot fetching
unchanged a2384967 source. Direct codeload prefetch is rate limited too and is
backing off. Its exact compressed source is absent from the public binary cache;
available SSH credentials cannot access the cache push account or runner.
No default branch, production host, or service configuration was changed.

A scratch migration-trigger probe uses the cached 6.12.48 kernel with the standard
NFS VM setup. Its only purpose is to validate a real nfs4_update_server trigger
before adding/running the race regression on repaired kernels; no cancellation
pass can be inferred from it. Config: scratch/migration-probe.nix; harness:
scratch/run-migration-probe.rb; log: scratch/migration-probe-vm.log; state path:
scratch/migration-probe-state-path.txt. The probe is still running.

Historical archive prefetch succeeded after its automatic backoff at 14:11 UTC.
Hash sha256-QlwV4uFeX7ZbWHMuU14rFXswmpqpb1hdVmYUAGOWRh8= matches the unchanged
fixture, and its exact fetchurl store path is now available. Restarted the AMD
historical lifecycle test in scratch/livepatch-legacy-vm-v2.log. No historical
kernel pin, module selector, or expected checksum was changed.

Migration probe attempt 1 reached target-server setup but used the name
migration-target, producing overlong nfsns-/nfshost- interface names. Source
inspection of osctl-exportfs Operations::Server::Spawn confirms that limit;
changed the scratch name to server2 and bounded readiness to 60s. The interrupted
probe retained logs. Attempt 2 uses scratch/migration-probe-vm-v2.log and the
path in scratch/migration-probe-state-v2-path.txt, 4 GiB guest memory and only
one client. It includes a scratch USR1 debug hook which evaluates a local
state-dir/debug.rb against the existing evaluator, allowing further fixture
diagnostics through its serialized shell without rebuilding or restarting.
This hook is local probe tooling, not committed product code.

After local archive download recovered, requested --failed rerun of CI
34697775063. Attempt 2 is building (14:17 UTC); its final logs still need checking.
Historical livepatch retry is compiling its candidate with the unchanged cached
boot kernel. This local output has not been published by the current branch's
responsible CI runner, so local construction is permitted by workspace policy.
No historical boot kernel source/configuration was changed to accommodate it.

At 14:20 UTC the repaired 6.12.95 plain kernel completed compilation and
installation successfully (drv 36z1asl0vffb6rm3hhgrwvc6ksmrk8al). The normal OS
build has advanced to built-in ZFS preparation, then its final kernel/module
outputs. This proves compilation, not runtime. Full log retained in
scratch/kernel95-plain-full-build.log.

Preparing an early full NFS suite run on the already compiled repaired 6.12.95
plain kernel with boot.zfsBuiltin=false and livepatch disabled. This is a
scratch fixture using the existing external ZFS module option, not a new kernel
entry or a production configuration change. Its purpose is to expose NFS
runtime failures while the final built-in-ZFS kernel compiles. Final standard
fixture validation remains required. Build: scratch/nfs95-external-zfs.nix;
log: scratch/nfs95-external-zfs-build.log; generic prebuilt-fixture harness:
scratch/run-configured-test.rb. External ZFS is building against the exact
completed repaired kernel dev output, cores=8/max-jobs=2.

Migration probe v2 reached target startup but raced rpcbind/NFSD setup after
publication of the server PID. Also fixed nsenter working directory to --wdns=/
(--wd=/ opens the host directory before chroot and causes getcwd warnings).
Probe v3 waits for positive NFSD thread count, sets its UTS hostname, and writes
8 to /proc/fs/nfsd/threads; nfsd_svc updates the server scope from the caller UTS
name on that path. It uses a TTY/Pry on failure for live diagnostics instead of
rebooting after each scratch-fixture error. Logs: scratch/migration-probe-vm-v3.log;
state path: scratch/migration-probe-state-v3-path.txt. Active executor IDs are in
scratch/active-runs.json; do not treat intermediate source closures as final OS
runtime validation, even when their kernel outputs are the exact repaired ones.

At 14:29 UTC external ZFS built successfully against the repaired 6.12.95 plain
kernel. The full existing NFS suite is running via the standard evaluator in
scratch/nfs95-external-vm.log, state path scratch/nfs95-external-state-path.txt.
Fixture JSON: /nix/store/3gl6bm2dfjv7hry6lzrq9ixkdlbbrnkl-os-test-osctl-nfs-cancellation.json.
At 14:31 UTC the retained final built-in-ZFS configuration passed and its kernel
compilation started (j280gxgwp60hkdqjsi1kkpd5di397dx5). This is the pre-mirror
recipe with the same proven final kernel output identity as the current recipe.

At 14:47 UTC the early repaired95 NFS run has passed its first five examples:
outage/checksum, shared cancellation/isolation, blocked mount, graceful fallback,
and remote lock isolation. The processless descendant example is underway.
The old migration probe reached nfs4_update_server after adding PID namespace
entry to exportfs; it reproduced the old kobject reinitialization warning, but
subsequent data access failed. That is trigger evidence, not a migration pass.
Repaired95 migration now runs as executor 46821, state /tmp/nfs95-migration.iijoWZ,
log scratch/migration95-vm.log. Old probe exited and its owned VM was closed.

At 14:52 UTC repaired95 migration succeeded with a kretprobe result of zero,
preserved payload checksum, and verified a destination write. EPERM in the
initial probe was traced to the existing replacement transport's unprivileged
port versus the export's secure default; the regression uses insecure exports.
The probe reproduced stale RPC sysfs links. Follow-up kernel commits refresh
both links using namespace-aware removal and export sysfs_delete_link for
modular NFS. Product migration regression is being added before pin refresh.
All eleven NFSv3 scenarios pass, including restored handles after osctld restart
and both dirty PID1 exit cases. NFSv4.0 scenarios are continuing.

At 15:03 UTC OS af42c679c commits the real migration regression and refreshed
kernel pins. Checkpatch, generated Ruby parsing, RuboCop, Nixfmt, and all commit
hooks pass. Final kernel heads are 6090ca00cbec50ca2a4ad785de361eaeaf1db529
(retained95) and cb16974b66f518b920226285b50f0b1f4416852e (default109), pushed.
Verified flat source hashes are in scratch/kernel-{95,109}-links-prefetch.json;
archived sysfs.c was byte-compared to each committed source. Superseded local
kernel builds were interrupted by exact verified PID; new normal/debug builds
started at the updated sources. Current executor IDs are in active-runs.json.
The historical livepatch and preceding-kernel full NFS suite continue, with
nineteen NFS examples passed. Plain-shell OS push hit an Overcommit signature
mismatch; retry uses the same Nix shell as the successful commit hooks.

At 15:06 UTC the early external-ZFS suite ended after twenty passing examples.
The two next dirty-init setups failed before any push_file guest command, then
the next context could not use the stopped container. The scratch fixture and
its Nix helper paths had disappeared: the custom harness used --no-out-link and
overrode TestConfig.build without retaining the standard configuration GC root.
This is a harness failure; final product VM validation remains pending. Both
scratch harnesses now retain the fixture with an indirect config.json GC root,
and the full-suite harness prints each underlying example exception. The NFS3
cases and NFS4.0 through unexpected init exit passed; NFS4.1/4.2 were not run.
Migration probe finished its data/link investigation and its owned VM was closed.
The OS push succeeded through the same Nix shell as commit hooks. Superseded
old-head CI 34697775063 was cancelled after verifying its head; current-head CI
is 34701121709 and RuboCop 34701121706.

At 15:13 UTC the standard final matrix selected exactly five fixtures: normal
and diagnostic NFS cancellation on 6.12.95 and 6.12.109, plus matching/mismatched
livepatch kernel identity. Command uses one brace glob, --no-destructive, -f,
--jobs 4, /tmp/nfs-final-oppnaoh3, and NIX_CONFIG cores=12/max-jobs=2 with the
evaluation cache disabled to avoid concurrent SQLite contention. Executor85546,
log scratch/final-vm.log. It shares the active kernel derivations and retains
the standard config.json output roots. Existing cumulative and uname livepatch
inputs apply sequentially to latest retained6090ca00; evidence in
scratch/livepatch-apply-links.log. Current RuboCop CI34701121706 passes.

At 15:39 UTC the historical AMD livepatch build completed successfully and its
VM script started. Existing historical source/image inputs remain unchanged.
The user asked to retry after account verification; PR creation was retried
through gh and still returned GitHub GraphQL Resource not accessible by personal
access token (createPullRequest). Kernel work and local testing are proceeding.
A focused migration/sysfs race prototype is prepared in
scratch/migration-race-prototype.rb; syntax passes, runtime awaits final95
external-ZFS fixture builder38365, whose output has a persistent GC root.

At 15:46 UTC the historical AMD 6.12.95 livepatch lifecycle passed (executor
2369, exit 0). The guest exercised patch enable/disable, cumulative replacement,
rejection of an incompatible older patch, and KVM smoke checks. Its script took
387.46s after the 82-minute module build; the unchanged historical kernel and
module inputs remain intact. Final repaired normal/diagnostic kernels and their
VM matrix continue building. Current-head CI 34701121709 is still compiling.

At 15:58 UTC the additional historical Intel attempt stopped before loading a
patch: its GenuineIntel precondition failed on this AMD EPYC host. The fixture
labels cpuVendor=intel select a matching CI runner; explicitly naming #intel
does not emulate Intel hardware. No Intel lifecycle pass is claimed. Preserve
the existing vendor guard; branch CI schedules the intel-kvm runner after its
OS build completes, independently of the PR-creation token limitation.
Executor 31198 exited 1 and its owned guest powered off. AMD lifecycle remains
passed. A one-line documentation correction to the final retained kernel hash
is pending in the OS worktree and will be committed with the final test updates.

At 16:09 UTC an attempted faster migration-race fixture reuse was stopped.
Its dry run required 43 small derivations and no kernel build, but GC removed
unrooted outputs of the old e232 kernel before the actual builder registered
them. The build plan then expanded to 50 derivations including old kernel
36z1asl0. Only the exact scratch builder PID 3261286 was interrupted, during
configuration and before old-kernel compilation. Final builds were unaffected.
Do not retry old outputs without rooting them before preflight. The focused
race now awaits final95 fixture 38365 as originally planned.

At 16:13 UTC current-head CI 34701121709 reports successful OS/kernel build
and binary-cache publication, plus successful AMD livepatch lifecycle. Intel
lifecycle and the full test suite are running. The repaired 6.12.109 normal
kernel's exact outputs are now substituting locally. Added executor 8234 to
retain the four exact CI toplevel derivations through indirect GC roots at
scratch/final-ci-result*. These closures explicitly retain both final and plain
kernel dev outputs, as required for subsequent module builds and diagnostics.

Current-head CI build/cache publication completed at 16:09:47 UTC, historical
AMD lifecycle at 16:12:34, and historical Intel lifecycle at 16:14:02, all
successfully. The local Intel CPU-precondition failure is superseded by the
proper Intel runner's successful result. Full CI VM suite continues.

At 16:21 UTC normal109 fixture builder PID 2278276 was deliberately interrupted
before any guest boot so it could replan using the newly published final kernel.
Its old Nix dependency plan still waited for the original plain-kernel build.
Only this fixture was interrupted; the original matrix now runs its queued
109-debug case alongside 95 normal/debug and identity. The rescheduled normal
109 suite is executor 68563, scratch/final109-vm.log, with the state path in
scratch/final109-state-path.txt. Its source differs from af42 only by the pending
documentation hash correction; daemon and test code remain identical. Account
for the deliberate interruption separately from runtime test failures.

At 16:25:10 UTC the rescheduled final109 fixture built successfully from cached
kernel outputs and began booting. JSON aldflrxdgw7h675rf87qwh97papliq32 is rooted
by the standard runner. At 16:29 UTC started the focused concurrent migration
probe against that same final kernel, independently of the still-building 95
fixture: executor 6299, scratch/migration-race109-vm.log, state path in
scratch/migration-race109-state-path.txt. The scratch harness adds its own GC
root before reading the fixture and uses a separate 4 GiB disposable guest.

At 17:48 UTC, the rescheduled normal 6.12.109 suite completed all 44 protocol
examples successfully (NFS3/4.0/4.1/4.2, including osctld restart, both dirty-init
namespace modes, processless namespaces, locks and tenant isolation). Its one
migration example failed before triggering migration because BusyBox readlink
has no -e option; the pending test change uses test -e plus readlink -f.
The overall suite is correctly reported FAILED, not a full pass.

Focused probes reproduced a real NULL dereference on BOTH final candidate
kernels: cb16974b 6.12.109 clean migration and 6090ca00 6.12.95 race setup.
The crash is sysfs_delete_link+0x23, called by nfs_sysfs_link_rpc_client from
nfs4_update_server. clnt->cl_sysfs is NULL. The newly added link refresh exposed
that rpc_switch_client_transport destroys the RPC sysfs client and does not
recreate it before returning success. This is a regression in our follow-up,
not a passing migration result. Both first-oops traces are retained in
scratch/migration{109,95}-null-sysfs.txt. Correct the transport replacement
sysfs lifecycle and handle optional sysfs allocation failure before rebuilding.
The two crashed disposable probe guests were closed after capturing evidence;
the development session and feature worktrees remain open.

At 17:54 UTC amended the narrow migration-link commits to include RPC sysfs
recreation before both transport registrations, NFS link refresh on rollback,
and optional-allocation handling. New Linux109 head4459e6f4f8958910fdfe5cd966450b5cab099449,
Linux95 headec548c1a4ee1a41645fcfe84a9180ccce7a30796. Both feature branches pushed
with explicit old-head leases after fetching unchanged upstream bases.
Checkpatch --strict: 0 errors/warnings/checks on the full amended patch;
both kernel diffs pass whitespace checks. OS migration fixture syntax and
readiness corrections await its pin refresh and commit. Focused general,
architecture and risk review reruns will assess the RPC lifecycle change;
scope remains within the already-reviewed real migration requirement.

Stopped only the eight owned build clients for superseded kernel outputs and
fixtures at 17:53 UTC. All four queued matrix guests were interrupted before
boot; their reported failures are deliberate build cancellation, not runtime
results. Retained available old plain normal/debug kernel outputs and exact
109 final output/dev closure through scratch/pre-migration-fix-roots for
comparison. No disposable guests remain running; /dev/shm is effectively empty.
CI34701121709 still runs its full suite; build/cache and historical AMD/Intel
lifecycle jobs pass. After publishing the corrected OS head, cancel this
superseded branch run as required and monitor the replacement.

At 18:04 UTC all six focused object builds passed without compiler warnings:
fs/nfs/sysfs.o, fs/nfs/nfs4client.o and net/sunrpc/clnt.o for corrected95 and109,
using copies of current source directories and the retained matching configured
kernel dev trees. Commands in scratch/compile-migration-objects.sh, output in
scratch/compile-migration-objects.log. This verifies compilation, not migration
runtime. The generated full NFS Ruby script passes syntax, migration.rb passes
RuboCop, and OS amendment c9260bbbe68c4368e2acab1ba32ae7612a763b43 passed all
Overcommit hooks. Three fresh gpt-5.6-sol/xhigh reviewers are assessing the
migration delta using packet-v3. All tracked implementation paths are committed.
The dev shell closure is now rooted at scratch/dev-shell-root to avoid repeated
GC-driven tooling builds.

Both canonical GitHub archive URLs and the already-supported codeload mirror
returned HTTP429 for the new heads. Initial canonical retries were stopped
before using the configured mirror; mirror requests now honor exponential
backoff. Hashes cannot be guessed or reused from old revisions. OS pins and
its final push remain pending the exact archive bytes. Current CI runs the
preceding head; no superseded branch run has been cancelled yet because the
replacement OS push is not ready.

At 18:12 UTC focused review round3 is complete. General found no issues.
Architecture reported one Important finding: the sysfs setup/register pair was
repeated at initial creation, replacement and rollback, while registration
owned its failure cleanup. Accepted and fixed by passing the selected xps into
static rpc_client_register and moving setup into that existing owner. This is
a direct narrow remediation with no public contract change, so general and
architecture reruns are unnecessary under skill step9. The still-running risk
review inspected the amended heads and found no issues. Final kernel heads:
109 7c66ab3c284a5fb5b615f874a99cb16501d6de23;
95 a2bdcc5b5067dcb7b8f36ef955cd6ee29c9c215a.
Both are pushed with explicit old-head leases after upstream fetch. Full
checkpatch --strict passes (70 lines, 0 errors/warnings/checks), and recompiled
SUNRPC objects pass for both versions without warnings. Full evidence in
scratch/compile-migration-objects-v3.log. No source ABI/layout changes beyond
the already-reviewed repair, and the existing livepatch variant remains intact.

Authenticated codeload access also returned HTTP429; no credentials were
printed or written to disk. Superseded source retries were stopped after the
review amendment. Final-head prefetches now run with normal Nix exponential
backoff: executor94751 retained95 and11594 default109. JSON/log files are
scratch/kernel-{95,109}-links-v3-prefetch.{json,log}. Do not accept hashes from
old heads. Once downloads succeed, verify the three changed files byte-for-byte
against the committed worktrees, amend both OS rev/hash pairs plus the livepatch
documentation SHA, run hooks, push OS, cancel old-head branch CI, and run the
focused migration plus the normal/diagnostic/identity matrix. Final kernel
builds/tests have not started while the source-pin update is blocked.

The corrected109 source archive downloaded successfully and is rooted at
scratch/kernel-109-v3-source. Flat hash:
sha256-/PiHSS9A1oYWg95k1e1yzjKgbClehMtUSh1LyvsDsTA=.
All four changed source files byte-match the reviewed commit. Amended OS head
18332a06dda48702d0421eff8d9dc31fdd298b85 pins this109 source and passes all hooks.
The95 pin remains6090 while the exact a2bdcc5b archive is still rate-limited;
this intermediate amendment will be folded into the same final OS commit when
its hash is available. No new OS push yet.

Started corrected109 normal and diagnostic CI toplevel builds using rooted
outputs, max-jobs2/cores18: executor25335 and85157, logs
scratch/kernel109-build-v3.log and kernel109-debug-build-v3.log. These are
intentional local kernel builds for the reviewed source repair, before the
responsible CI runner can publish it. Existing CI outputs explicitly retain
plain/final dev closures for subsequent module and diagnostic use. The pending
95 pin update must leave these109 kernel derivations unchanged; verify that
when completing the pin amendment. The95 prefetch is at normal Nix backoff
attempt4 (about10 minutes); no further permission is needed for the kernel work.

The user asked whether our GitHub API token applies to the archive failures.
Normal gh API calls use the configured token; Nix generic archive downloads do
not inherit gh authentication. A direct authenticated codeload attempt returned
429. The documented authenticated tarball API was also tried with gh api
repos/vpsfreecz/linux/tarball/a2bdcc5b5067dcb7b8f36ef955cd6ee29c9c215a; it returned
HTTP/2.0 429 with a GitHub request ID, not an archive. Filtered status is in
scratch/kernel95-api-tarball-status.json. Raw response headers were discarded;
no credentials were printed or persisted. GitHub's documentation confirms that
this API accepts fine-grained tokens with repository Contents/read permission.
Existing authenticated metadata and CI queries still work; no assumption of a
missing token or approval block is justified by this archive failure.

A focused109 external-ZFS fixture is building (executor27475), sharing the same
corrected plain kernel so clean and concurrent migration can be checked before
the final built-in-ZFS kernel finishes. Root scratch/nfs109-v3-external-config;
logs nfs109-v3-external-build.{out,log}. Prepared combined clean+race scratch
probe passes Ruby syntax. Full normal/diagnostic tests remain required after it.

## Final cleanup record

On 2026-09-17 the original local corrected109 normal and diagnostic toplevel
builds and external-ZFS fixture were found completed successfully. They did
not proceed to corrected-head runtime tests. Source95 a2bdcc5b still lacked a
verified archive hash and the OS entry remained pinned to6090ca00. CI34701121709
had finished with failure; there were no queued/in-progress branch workflows
to cancel. Its failure was not reinvestigated after the abandonment request.
No test rerun or new build was started during cleanup.

The previously retained log paths under scratch/ and the disposable /tmp/nfs*
directories are historical references; those transient outputs were removed.
Selected evidence is now under evidence/. The exact removed paths are listed
in cleanup-record.json. The local OS head18332a06d is newer than remoteaf42c679c;
it remains preserved locally. Both Linux heads are preserved locally and were
pushed before abandonment. No branches or source worktrees were deleted.
