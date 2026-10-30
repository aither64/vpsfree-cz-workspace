# Podman predecessor repair: first entry trace

Owner: implementer1, session `2026-10-22-ci-failure-analysis`, trusted workspace
`/home/aither/workspace/ai/vpsfree.cz`. Lead schedules every long operation with
a fresh watcher. VM1 failed before trace retrieval; VM2 retained a trace but
did not reproduce the original denial. No kernel/LXC/client repair is chosen. Hook
release was received from lead.

## VM2 completed: permission denial not reproduced

Lead selected and solely executed the frozen package described below. Native/
guardian0 in325.404s is successful capture/retention, **not** a network repair
or nested continuity result. Cause-first findings and exact source/log citations
are in [capture-2/findings.md](capture-2/findings.md): PID164 trace230/231 NNP0/
filter0, eight successful pairs and no captured EACCES; guest IPv4/default route
present. Archive/binary hashes match the earlier diagnostic sample only. Trace
106,496 bytes ends midline/no ifup terminal exit; service60s timeout/Brokenpipe
is instrumentation-affected, and copy `incomplete=false` does not certify full
lifecycle coverage. No product/source-owner fix is justified; no untraced run,
probe, kernel change or retry is selected. Historical launch proposal follows
as immutable provenance, not permission to repeat it.

Raw55files/783,140 bytes were retained once with SHA256SUMS. Our earlier
post-result reconciliation and owner3's separate independent proof record
effects ended within their qualified scopes. All original process/FD/disk/
socket/lock limits are recorded. Lead accepted retention and the independent
proof, then directed stopped-data cleanup. [capture-2/cleanup.json](capture-2/cleanup.json)
records verified retention and removal of only attempt2 `state`, `vm-scratch`,
`metadata-scratch` and `preparation-scratch`; all nine prepared/input/shared-runner
roots remain unchanged. No new process scan or Git operation was performed.

Preparation2 passed once: wrapper/native0,41 seconds, all nine approved assembly
derivations and exact JSON/helper/binary checks passed. New planned-store growth
411,181,056 bytes, scratch4096, logs514,183, end free113,035,014,144 bytes.
`preparation-2.reconciliation.json` verifies the prepared root and seven input/
cache roots,629 runtime paths /1,966,459,256 NAR /2,129,076,224 physical bytes,
empty own scratch and no exact own process reference (four permission-restricted
same-UID services qualified). No prior client birth was retained, so the receipt
does not invent that comparison. No cleanup or live observation occurred; these
are completed preparation receipts. The first watcher guard-only invocation
without its required marker had no Nix/path effects; no product retry follows.

Exact proposed command, launched only by the lead's fresh sole watcher:

```sh
env CI_FAILURE_ANALYSIS_PODMAN_VM=attempt-2 \
  /home/aither/.nix-profile/bin/bash \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/podman/run-vm-2.sh
```

| Package | SHA256 |
| --- | --- |
| `run-vm-2.sh` | `a72f60a2c578119e9b644d288aaaca7fe9b5c37b0bf75e02f77956d4102d1b92` |
| `guard-vm-2.py` | `ca72c0df750c1272bcdee2a21ce73664825d2f9bbded014915734338a8901ba6` |

The fixed native invocation is `timeout --signal=INT --kill-after=120s 1500s
/nix/store/mjlc8sc8qp6vpzf08r65jwl1y38jbgjm-test-runner/bin/test-json-runner
/tmp/ci-failure-analysis-2026-10-22/podman/attempt-2/prepared
/tmp/ci-failure-analysis-2026-10-22/podman/attempt-2/state`, with
`TEST_PATH=upgrade/nested-podman-sandbox`, `TEST_TIMEOUT=120`, jobs1,
recreate-disks/destructive cleanup and x86_64-linux. It uses the existing shared
runner root at attempt1; it neither rebuilds nor duplicates that root. Source
visibility changes after feature commits cannot reevaluate this immutable JSON.
Rooted config is w9ik, prepared output x5vs, exact JSON SHA256
`615f76adca40be39b5de225e514a726c04bb2c7401b5fd4443c9523fead72af2`.
Launcher checks exact JSON/config/runtime/shared runner roots, runner/helper/
guardian hashes and all prepared binaries. There is no Nix command at runtime.

Timing is now explicit and accepted by architect for lead selection: fixed
script's900-second body starts around VM startup/setup, includes the single CT
start and one monotonic60-second window plus optional bounded fields, and saves
the first observer exception. Outside that block, independent CT stop, root
collection and VM shutdown have up to525 seconds of exposed native command
allowances as listed below. Native total1500 allows900+525+75 seconds of slack.
The75 seconds is startup/host-I/O/Executor slack, **not** a proven completion
bound; kernel-error draining and other host effects remain qualified. GNU
timeout issues the ordinary1500-second INT. Guardian does not duplicate it;
it authenticates the native group's birth/PGID, sends KILL at1615 if still owned,
and uses the last5 seconds of the1620 envelope for reaping/observation. A resource
breach instead sends INT immediately, uses its own earlier120-second interval,
and never restarts that deadline or waits until1500. Unknown ownership is never
signal authority. Any survivor, failed final scan or escaped own reference
returns incomplete125 and retains watcher/owner reconciliation; no deadline
certifies effects ended or permits cleanup.

Fresh admission requires one session-owned VM slot selected by lead, at least
64GiB free (full **remaining24GiB** forecast plus40GiB reserve), more than4GiB
MemAvailable, more than2GiB free `/dev/shm`, and affinity capacity for two CPUs.
Native fixed guest remains2GiB RAM/SHM, two CPUs/2x1x1 and one10G disk. Native
runner reserves zero, so the literal selection plus external fresh checks matter.
No host cgroup/RAM cap is claimed. Continuous guards retain the44GiB stop margin,
24GiB cumulative growth,2GiB scratch, host no-swap observation and2GiB minimum
MemAvailable. Preparation's411,181,056-byte store growth is counted once in
cumulative accounting. Fresh remaining24GiB is not discounted by already-realized
closure bytes:10GiB managed-disk growth +2GiB scratch +1GiB host transfers/logs/
evidence +11GiB contingency. The1GiB allowance includes up to128MiB trace copies
(CT, VM retained path, native pull staging, final evidence); they are one trace
with duplicate physical allocations, not four observations. The measured2.13GB
store closure is already present, retained and not an implicit runtime build.

Existing trace limits stay32MiB per captured trace and16MiB total nontrace/log
output including host receipts; a full trace is incomplete and triggers stop.
Guardian classifies the new `--podman-sandbox-retained--trace.log` pull name as
trace, while all copies still count toward physical growth. VM-internal trace/
retained allocations sit within guest resources/disk; the external watcher must
retain the output/physical qualifications rather than claim a host file quota
sees every guest-internal byte. Trace writer/helper caps enforce their declared
byte bounds. Original observer error is never converted to success by a copy.

The lane declares only new `attempt-2/state` and `attempt-2/vm-scratch` disposable
paths. Existing markers/state/scratch refuse another launch. Canonical reference
checks cover Podman attempts1/2, declared support attempt1 and hotplug admission
attempt; foreign VMs are aggregate resource context and never signalled. Final,
error and lost-parent scans retain detached own references even with an empty
group; readonly observer exemption requires executable **and** safe invocation.
The sole watcher and owner must reconcile exact native PID/birth, descendants/
QEMU/virtiofs, managed disks, native lock, sockets/kernel UNIX refs and open FDs
after completion, qualifying permission gaps. Only after all effects end retain
compact raw snapshots/trace/image identities, then natively remove stopped owned
disposable data. Keep prepared/runtime/shared runner roots for pending consumers;
no global GC, source-session data, foreign path deletion or lifecycle action.

`vm-2-inert-checks.json` records Python/embedded admission compile and fake-process
tests, with no live process scans, child launch, real signal or VM. Checks cover
foreign/sibling/own path boundaries, readonly and mutating observer distinctions,
no duplicate native INT, KILL1615/final1620 timing, immediate resource INT and
KILL115 seconds later, and incomplete125 for detached final refs. Bash syntax
passes. Source/JSON/helper bytes remain the accepted16-example correction; no
additional product edit or Git operation occurred.

This capture remains ptrace-sensitive; foreground tracing can hold the systemd
oneshot open. Separate early failed-prctl/ifup evidence from instrumentation-
affected service state. No APT, Podman installation or target activation occurs.
Another mutable latest fetch is a **new image sample** unless exact prior archive
hash/provenance is recovered. Neither preparation nor a new-sample trace proves
the original incident cause, owner fix or full nested continuity.

Authorized observer-correction quick checks own
`/tmp/ci-failure-analysis-2026-10-22/podman/observer-check-1/` as TMPDIR.
No VM/daemon runs: focused RSpec fakes exercise original fixture control flow,
ordinary owned temporary files exercise FD/no-follow retention. Forecast <80 MiB
temporary allocation, <64 KiB logs, <60s; retain results in this brief, remove
only these stopped test directories through native RSpec temporary-file cleanup.
No runtime/new JSON/root/build/Git action is selected by these checks.

## VM1 actual result and observer correction

Lead's authoritative watcher ran the selected fixed JSON once: native status 1,
217.8567 seconds, guardian reason null, final scan complete, no own references.
This is an **observer failure**, not evidence for either failing prctl.
`capture-1/` retains 45 raw files (~545 KB), their `SHA256SUMS`, independent
`post-result-reconciliation.json` and `cleanup.json`.

- `capture-1/machine-shell.log:10859`: the one CT start succeeded in 12.01s.
- `:10870`: the first `osctl ct exec ... systemctl show networking.service`
  observation ran 7.06s, returned outer timeout status 124 and `error: SIGTERM`.
  `:10879` records `PHASE: replies_consumed` and the complete framed 124 reply.
  This does **not** establish lost legacy-console bytes or its source/introducer.
- Executed fixture `capture.rb:112–115` gives that poll only ten seconds.
  Exact packaged `osvm/lib/osvm/shell.rb:345–353` reserves 20% plus 10% for
  protocol/kill handling at this bound, leaving about seven seconds for the
  guest command; `:396–398` raises on an outer 124/137 after consuming the reply.
  The bounded observation did not complete; why its attach/systemctl path did
  not return in that interval is not measured.
- Unhandled timeout unwinds the example before `capture.rb:124–162` can save
  post-start snapshots, entry or trace. The ensure (`:164–175`) stops the CT
  then VM. `capture-1/machine-log.log:14` records QEMU exit 0 and `:28` destroy.
  **No retrieved trace is not proof no trace was generated or no denial occurred.**
  `/run` trace bytes and the fetched archive were inside the native managed disk,
  already destroyed by ordinary cleanup; only their captured identity survives.

All 24 prestart snapshot fields report complete/status 0/nonempty. This new
image sample is Debian 13.7 with dhcpcd-base `1:10.1.0-11+deb13u4`, ifupdown
`0.8.44+deb13u1`, libc6 `2.41-12+deb13u4`, systemd `257.13-1~deb13u1`
(`capture-1/podman-sandbox/package-versions.txt:2`). dhcpcd binary SHA256 is
`a9215b8a2efc63481ef781069917e1bae2b293744d544fd18566c7abb37a955c`;
image archive SHA256 is
`e0a89f751487eadf0e198f7251550e92aba100ddb8d3c8bd920140b557281ad4`
(`image-cache-hashes.txt:3`), INDEX SHA256
`0572fb88a58d8db3c4e042f4da7ab01bcb7a12402c5a9c12267d087274295bc6`.
The matching package labels strengthen source applicability but cannot establish
identity to the unrecovered incident archive/binary. No authentic archive bytes
were retained outside the disk, so a later fetch is again a sample unless its
exact hash is checked and provenance recovered.

Actual `/proc/config.gz` is complete for this prepared kernel and includes
`CONFIG_AUTH_GUARD_CORE=y`, `CONFIG_AUTH_GUARD=y` at captured lines 9012/9015,
plus `CONFIG_SECCOMP_FILTER=y`. This closes the config-selection gap for this
diagnostic binary only. No failed prctl, effective failing-task credentials,
NNP/filter or actual guard rejection was captured; the incident mechanism and
owning fix remain unresolved. No APT, Podman install or target activation ran.

Independent effects reconciliation passed before cleanup: native PID 52308 /
birth 1200892540 absent, group/session and canonical references across all three
declared roots empty, managed disks/sockets/kernel UNIX references/openfds empty,
test lock independently available. Kernel permissions hide unrelated UID fd
tables (708), explicitly qualified in the receipt; no own process remained.
Only stopped `state`, `scratch`, `vm-scratch`, `guardian-check-1/2` were removed
after compact retention/path/UID verification. The known inert-test symlink was
unlinked within its own test tree, never followed. Remaining attempt allocation
16,384 bytes; free after cleanup 100,392,976,384 bytes. **Shared runner root and
all prepared/config/kernel/LXC roots remain retained**, no store deletion/GC or
session lifecycle action. One-VM slot effects are ended.

The accepted narrow correction is now **implemented and checked without a VM**
in the assigned fixture. It writes entry/trace to CT
`/var/log/podman-sandbox`, removes the repeated short service poll, and waits
once for the remainder of the monotonic 60-second window from the single start.
Optional snapshots record head/field status, timeout, empty and truncated
qualifiers; timeout without returned bytes makes empty/truncated unknown.
The first observer exception is re-raised after independent CT-stop, retrieval
and VM-shutdown attempts. Collection/cleanup errors are retained separately.

Before startup, the fixture records the exact CT pool/id/dataset/private path,
ZFS GUID/mountpoint, and private-root device/inode. Host helper `retain.rb`
rechecks device/inode, pins directory descriptors and opens only fixed
`var/log/podman-sandbox/{entry.txt,trace.log}` components with `O_NOFOLLOW`.
It rejects symlinks, nonregular files and other devices; entry and trace have
independent 256-KiB and 32-MiB copy caps. A bad entry cannot skip trace copying.
Dataset GUID/mountpoint and any available current CT identity must agree.
An unavailable CT-status reply is retained as a secondary gap: only the
already-mounted, independently authenticated recorded root may then be read,
and the result is partial with state/active writers unknown. Contradictory CT
identity refuses copying. Native mounting is allowed only for that same
confirmed stopped CT; no unknown-state mount, start, recreation or deletion.

Focused no-VM checks pass: **16 examples, zero failures**, including injected
observer plus stop failure preserving the exact primary exception, failed stop
plus unavailable CT status still retrieving before shutdown, changed CT/GUID/
device/inode refusals, safe stopped remount, unknown-state remount refusal,
independent entry/trace retrieval, symlink/FIFO refusals and empty/capped fields.
Ruby syntax, repository RuboCop 1.75.8, nixfmt 1.5.0 and Nix parse pass.
`observer-correction-2-checks.txt` retains exact commands, tool paths, environment,
statuses and hashes. RSpec alone adds the installed user RSpec libraries;
RuboCop uses only the existing worktree hook GEM_PATH. The earlier
`observer-correction-1-checks.txt` records a mixed-GEM_PATH invocation selecting
a different ambient RuboCop; the corrected command does not change hook policy.
Own test temporary children were removed natively; TMPDIR allocation remains
4,096 bytes. Final free space was 108,852,678,656 bytes. No VM/daemon, new
derivation/root, realization, build, Git mutation or sandbox change occurred.

Current source SHA256 (worktree HEAD remains `274e826dae6d5b7230857174a25afa1f91ab4ffb`):

| Assigned path under `tests/suite/upgrade/` | SHA256 |
| --- | --- |
| `nested-podman-sandbox.nix` | `57b6e71b7e3b7b364be2c98936bea41bed76e50e4b634efab1ba863577138558` |
| `nested-podman-sandbox/capture.rb` | `6ad10c59bf8dd3868c8a5b84aed57b62e18eb797619f03991286fa801b882e3b` |
| `nested-podman-sandbox/retain.rb` | `9180d75e2be7ddab6a9624b56171bf310f0113c172fdf3786017a47e6cf1df4d` |
| `nested-podman-sandbox/capture_spec.rb` | `a401f5d12f870dbc5b57574a898f46c11a34014ab26c4e5125e001310df2dd8f` |

This fixes evidence retention, not the unresolved product mechanism. Ptrace and
foreground oneshot effects remain; retrieval with active writers is partial.
No next runtime is selected. A later proposal must name a distinct frozen JSON,
new attempt and complete resource/cache forecast, including exact predecessor
`pkgs.ruby` and helper inputs and existing native transfer command bounds. The
added Ruby/helper closure has not been evaluated or measured. Existing
32/16-MiB and 900+120 outer resource/cancellation contracts remain constraints;
native effects must still be reconciled after any deadline. Re-fingerprint the
archive/packages: another `latest` fetch is a new sample unless the prior exact
archive hash and provenance are recovered. Never overwrite/reuse VM1 receipts
or infer repair of the incident tuple from a new-image pass.

The remaining sections describe the historical VM1 admission package and
earlier proposals. They do not authorize launching the changed fixture.

## Attempt 2: prepared no-build metadata command, not executed

**Authoritative result now received:** this metadata command ran once and
passed, native exit0/51 seconds (watcher wall estimate about47 seconds). Its
following command description is retained as execution provenance, not a retry.
`cache-preflight-2.*` are the actual receipts. Watcher stdout was empty and its
requested outer log was not created; no replacement capture is fabricated.

Lead requested a new attempt's metadata/root/cache proposal; architect accepted
the final four source files and focused receipt. This lane declares ownership
of the new disposable
`/tmp/ci-failure-analysis-2026-10-22/podman/attempt-2/`, its `gcroots/config.drv`
indirect Nix root and `metadata-scratch/`. The directory does not yet exist.
Only the selected watcher may create it after canonical ancestor/UID checks;
an existing attempt or metadata receipt refuses reuse. Attempt 1 and its shared
runner/root consumers remain untouched.

Exact proposed watcher command (lead selects and launches):

```sh
/run/current-system/sw/bin/timeout --signal=TERM --kill-after=10s 330s \
  env CI_FAILURE_ANALYSIS_PODMAN_METADATA=attempt-2 \
  /home/aither/.nix-profile/bin/bash \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/podman/run-cache-preflight-2.sh
```

Script SHA256:
`eb676abe76629a8117015d49ca15ae7d105916accf2b1e8fdcf68f01c44f79ed`.
Bash syntax, all five embedded Python blocks and whitespace checks pass; the
script itself has **not** run. It requires the verified session environment,
canonical owned worktree/branch and accepted-base ancestry. Nine exact source
hashes cover the four fixture files, native evaluator/library, flake/lock and
test-shell module; before/after hashes must agree. It records actual HEADs,
without asserting unrelated peer edits are the prepared fixture's runtime.

The first native operation is `nix-instantiate` on
`test-runner/nix/evaluate-tests.nix`, with `repoRoot` the canonical worktree,
`system=x86_64-linux`, `mode=testJson`,
`testPath=upgrade/nested-podman-sandbox`, `testArgsJson={}`, explicit diagnostics
opt-in and empty `VPSADMINOS_CONFIG`. It creates only the indirect config **drv**
root, with IFD disabled, zero local jobs, empty remote builders and fallback
disabled. The next operations read its native derivation, input graph/requisites
and perform **dry-run only** against that immutable derivation. No output is
realized or substituted; no runner build, production target or VM is requested.

The command recovers exact native JSON bytes from `env.text`, records their
SHA256/output store path, and checks manual/attempts1, one VM, 2048-MiB RAM/SHM,
two CPUs/2x1x1, one 10G disk, user network and original 6.18.49 kernel path.
It compares the generated script to exact substitutions of the frozen source.
It captures Ruby/helper/tracer/wrapper recipes; helper bytes must match the
accepted source hash and wrapper paths must be persistent. Already-local Ruby
and tracer outputs get binary hashes, recursive NAR/closure metadata and
physical `du` for every closure member; Ruby's FD/no-follow APIs are checked
without a VM. An unavailable local output is explicitly recorded; no implicit
fetch/build fallback occurs. Missing-output recipes from the native cache plan
are recorded for parent assessment. No JSON or binary identity is guessed
before this first metadata evaluation.

Resource proposal: metadata only, up to two host CPUs/2-GiB RAM, no VM/SHM.
Allow **4 GiB total** conservative incremental physical allocation: up to
2-GiB cached/source input materialization, 256-MiB own TMPDIR, 16-MiB compact
metadata/logs, remainder for Nix metadata/transient source copies/contingency.
Require at least 44 GiB free and preserve the 40-GiB floor. Script checkpoints
record `df`, physical `du`, elapsed time and metadata bytes; reject more than
4-GiB free-space decline, 256-MiB scratch, or 16-MiB metadata. Native command
output is piped to the remaining budget with a 1-MiB final-receipt reserve;
cap/truncation/nonzero stops this package. The fresh watcher must continuously
enforce the same aggregate physical/scratch/log limits, including its own logs,
and retain ownership on a cancellation or surviving client. No shared daemon,
foreign process or global GC manipulation is allowed. Native stages share a
300-second budget and ten-second TERM/KILL allowance; the external 330+10-second
bound covers bookkeeping. A deadline does not prove all command effects ended.

Retain `cache-preflight-2.*` receipts and exact config-drv root for parent
reconciliation; there is no prepared-output root yet. After all selected
consumers/commands finish, remove only this attempt's exact temporary root and
stopped scratch under a separately selected cleanup; never delete store paths.
This script performs no cleanup, Git mutation or lifecycle action.

For a later **separate VM** proposal, retain the full **remaining 24-GiB**
forecast and require at least 64 GiB freshly free after preparation, with actual
closure/cache/squashfs/image measurements first. The native transfer is material:
`pull_file` copies through the VM's shared directory using a command with the
default `TEST_TIMEOUT=120`, with no per-call timeout argument. During retrieval,
the 32-MiB trace can coexist in CT root, VM `/tmp` retained copy, host pull staging
and final evidence: up to **128 MiB** total trace allocations, plus entry,
snapshots and native logs. Staging is additional transient physical growth;
it is not another independent trace or evidence observation.

The source correction preserves independent cleanup attempts, not a guarantee
that they finish within the guardian's 120-second cancellation allowance.
Worst exposed command allowances are CT stop20 + CT status20 + ZFS20 + optional
mount20/ZFS20 + helper20 + two pull commands120 each + VM shutdown's default
poweroff-command120 and reaper-wait45 = **525 seconds**, excluding host file I/O
and native Executor cleanup. `machine.stop(timeout:45)` bounds the reaper wait,
not its preceding poweroff command. The existing guardian cancels at900 and
escalates against authenticated owned group by1020; it can interrupt collection
or cleanup and therefore still requires incomplete-result/effects reconciliation.
The next runtime admission must address this explicitly; metadata does not
select new runtime bounds or authorize source changes to them.

Any later image fetch remains a new sample unless exact prior archive bytes/hash
and provenance are recovered. Metadata/source checks do not establish product
cause, security-policy repair, original-image equivalence or full Podman
continuity. Ptrace/foreground oneshot qualifications remain unchanged.

### Attempt 2 metadata findings and next preparation proposal

Sources and HEAD stayed stable at `c2c5a006b49730d8b72d103ff063a1e89bba1ee2`.
The native input is rooted derivation
`/nix/store/w9iksk0scppw4wjd264g2x2xpf5sfyb8-os-test-upgrade-nested-podman-sandbox.json.drv`,
output `/nix/store/x5vs9a7bn0w1bd29r5cfln6n75csi2fm-os-test-upgrade-nested-podman-sandbox.json`,
exact native JSON SHA256
`615f76adca40be39b5de225e514a726c04bb2c7401b5fd4443c9523fead72af2`.
The kernel, initrd, QEMU, virtiofsd, all disks/topology/resources and networking
match VM1; predecessor toplevel/squashfs and diagnostic script differ as intended.
No production activation target is in this graph.

The nine missing local derivations are baseline stage2-init substitution,
sshd configuration check and wrapper-path existence check; the new ifup wrapper
and retention helper; predecessor toplevel assembly, closure-info, squashfs and
JSON. The first three are byte-identical recipes from preflight1, not new kernel
work. No kernel, LXC, Ruby or strace compilation is listed. Only two substitutes
are missing: `bzk2jf62ksz06jqlkz9bf7xk8iidhcwk-jq-1.8.2-dev` and
`24lz9z364d9dymy8izf99av7j2vmw753-squashfs-4.7.5`, totaling280.5KiB download /
695.4KiB unpacked. Nix did copy the declared source input `snkd91zf...-source`
during instantiation; no config/kernel/tool runtime output was realized.

Exact native Ruby is `5shv7ihqxa98r1psfz995q3j2cwk22sa-ruby-3.4.9/bin/ruby`,
binary SHA256 `b858ac0a0732cd46dc470fe1226536b189eeb82e8c3bcf8e3969509dedea1106`.
Its11-path closure is98,399,032 NAR /109,268,992 physical bytes. The unchanged
strace has25 paths,75,374,552 NAR /78,225,408 physical bytes. Their unique union
is28 paths /127,725,568 physical bytes; do not add shared library allocations
twice. Ruby's required FD APIs exist. Native helper recipe
`vh6xk4829ar6z7ym09gv4m615i3j3mcv` -> `xm7771cxn159vsscsrsbhs3wvdpwpz8j`
contains the exact accepted source bytes. The prepared helper output itself is
not realized yet. All source/substitution/helper checks passed.

Actual metadata is about4.68MB, scratch4096 bytes; end free space was
103,269,691,392 bytes. Final independent same-UID exact canonical reference scan
found no attempt/script/drv argv/cwd/root/open-FD references; the config root
matches and scratch is empty, total attempt allocation16,384 bytes, no VM state
or disks. `cache-preflight-2.reconciliation.json` qualifies nine transient or
permission-restricted same-UID processes; readable identities are ordinary
user/session services, not evidence of a metadata child. The previous native
client PID/birth was not retained, so do not invent a prior-birth comparison.
Authoritative watcher reported exit; no process was signalled or data removed.
One native `nix-store --query --roots` confirmed our exact root but also
automatically removed two unrelated already-stale coordination-notification auto
links. No global GC or store-data deletion was requested. This side effect was
reported; do not repeat that query. Exact root and empty scratch remain retained.

Preparation-only proposal, **not executed or selected**:

```sh
/run/current-system/sw/bin/timeout --signal=TERM --kill-after=10s 1250s \
  env CI_FAILURE_ANALYSIS_PODMAN_PREPARATION=attempt-2 \
  /home/aither/.nix-profile/bin/bash \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/podman/run-preparation-2.sh
```

Script SHA256 `65b6450c5781daa333bccba8f83c2457c383dc6b3917fa1274679c37e24803ca`;
Bash syntax/five embedded Python compile/whitespace checks pass. It validates
the exact root, accepted receipts/source bytes and unlimited inherited FSIZE;
checks then separately roots already-valid kernel/LXC/Ruby/tracer outputs with
zero jobs/empty builders, refusing a disappeared runtime output. Fresh native
dry-run permits only a subset of the nine captured recipes and the two captured
substitutes; new graph work stops. Fetch/root each of those two outputs with
zero jobs/empty builders/fallbackfalse, recheck the native plan, then realize
only the rooted exact JSON derivation with jobs1/cores2/empty builders. No kernel
build, runner build, source reevaluation, retry or VM command is selected. Capture
actual recursive output closure/NAR/physical allocation, binary hashes and
byte-identical prepared JSON/helper before any later VM proposal.

Preparation's conservative physical ceiling is10GiB new planned-store outputs
+2GiB scratch; require52GiB freshly free above the40GiB floor. This includes
new squashfs and its transient build allocation, rather than only the small
JSON/helper. Prior runtime closure was1,966,450,176 NAR bytes and old squashfs
410,038,272 bytes; tool closures are mostly shared/present, but only actual new
prepared closure can establish the final delta. Use these as scale evidence,
not a guaranteed compression ratio or exact new image size. Native stages share
1200 seconds with10-second TERM/KILL, outer1250+10; own scratch is the newly
declared `attempt-2/preparation-scratch/`. Script checkpoints planned-store
growth, scratch, logs and free space. Pipe caps reserve1MiB final metadata within
16MiB total logs; no small RLIMIT enters Nix. The sole fresh watcher must
continuously enforce these limits, stop unexpected kernel/build-graph activity
and retain ownership until command/daemon effects are reconciled. Jobs1/cores2
are native build settings, not a host cgroup/RAM cap claim.

Retain exact prepared root, config drv and six output/cache roots for selected
consumers; no cleanup is embedded. Remove only stopped owned scratch/roots after
all consumers/effects end under lead selection; never delete store paths. Later
VM admission still needs the full remaining24GiB forecast/fresh64GiB free,
measured actual closure, explicit525-second ensure/cancellation treatment and
new-image provenance qualification. No runtime permission follows preparation.

### Four-file source Git packet (window required)

**Completed in lead's granted window:** feature commit
`405a802857093176883e0f173589b433756a9647`, parent c2c5a006, tree
`29b00319a5aedaa44a56d60bc6d0b70083a8ac16`. Normal isolated Nixfmt/RuboCop and
commit-msg hooks passed (72-column advisory only; every line<=80). Committed
focused tests passed16/0 in0.118s. Exact four source hashes/modes match, shared
index is empty and2399 peer files' bytes/modes are preserved through feature FF.
`fixture-commit-result.json` and linked hook/FF/backup receipts retain proof.
Initial checkout hook64 was an environment failure: GEM_PATH excluded the
selected Ruby's bundled rexml gem. Adding that exact Ruby default gem directory
restored normal post-checkout hook success; no gem installation or bypass.
All native commands ended and canonical own-reference scan is empty with four
permission gaps qualified. Git window explicitly released before cleanup.
Clean detached checkout remains346,939,392 physical bytes pending separately
selected native removal; recovery backup retained. No push or runtime result.

Commit only the four accepted paths/hashes in the source table above. Their
bytes still match the16-example/format/check receipt. Message file is
`repair/podman/fixture-commit-message.txt`, SHA256
`73431d669dbfc9c8474c00455be7387c6c211674792e64096cd1535b3a901c8f`,
subject `tests/upgrade: capture predecessor DHCP sandbox entry`. This is one
logical diagnostic owner, with future direct refinements folded into it; no
product root-cause patch is claimed. Owner3's registration/common/docs commit
must follow this fixture parent.

Lead now granted the narrow serialized four-path Git window at parent c2c5.
Use a clean detached native checkout at
`worktrees/2026-10-22-ci-failure-analysis/vpsadminos-podman-commit`, conservative
1GiB physical/8MiB output/40GiB reserve, unlimited file-size limit. Direct commit
in the shared dirty checkout is rejected because Overcommit can automatically
stash unstaged peer edits. Before mutation snapshot every tracked and ordinary
untracked peer file's bytes/mode/link identity, require empty shared index,
verify parent/hash and preserve checked copies of the exact four new files in
`repair/podman/commit-backup/`. Create the detached checkout at that exact parent,
copy/stage only the four files there, require its entire staged set equals those
paths, and run focused checks and normal commit hooks. Use the already prepared
declared hook environment (Ruby m0nfdb4...3.4.9, nixfmt ffrsk7...1.5.0, primary
worktree `.gems/bin`, GEM_HOME/GEM_PATH only primary `.gems`); no shell bootstrap,
hook bypass or new tool installation.

After the isolated commit's exact four-file diff, parent, hashes and normal
pre-commit/commit-msg success are verified, recheck shared parent/index/owned
hashes and every peer byte/mode. Lead's window explicitly permits the scoped
feature fast-forward: remove only those **four exact owned untracked files**
after checked backup, leaving their directory and every other path alone, then
`git merge --ff-only <verified-isolated-commit>` on the session feature branch.
No tracked old-blob restore is needed for four new paths. Verify final head,
empty index, exact owned bytes and all peer bytes/modes against the original
snapshot, and retain recovery copies through reconciliation. Any conflict,
hook failure or uncertain effect stops for reconciliation; no shared stash,
reset or clean. Release the Git window explicitly after proof and before
separately selected clean native isolated-checkout removal. No push/default
integration/cleanup or runtime launch follows this window.

## Historical VM1 admission package: preparation and execution complete

Historical prepared/accepted package below was executed by lead's watcher as
VM1 above. No next VM is selected by these recorded commands.

This section supersedes the preparation-time proposals below. Lead's fresh
watcher ran `run-preparation-1.sh`: exit 0 in 168 seconds, all kernel/LXC/config
steps 0. Prepared JSON store path and exact bytes match the no-realization
receipt, SHA256 `1610ffb3b8b94689f5c59a9d5ec6a33b4072c682b23909f84b2ebbeeb25930a2`.
The author rechecked these bytes and all five binary hashes in
`preparation-1.binary-hashes`. Realized runtime closure is 628 paths,
1,966,450,176 NAR bytes (`preparation-1.realized-closure.json`). Preparation
measured 798,420,992 new planned-output physical bytes, 4,096 scratch bytes
and 221,872 config-log bytes; free space ended at 109,957,259,264 bytes.
Preparation is not execution or causal attribution.

The unchanged fixture hashes below generated rooted config derivation
`wl582zy4s8csr86ll3xhi9cfzsl7k0vp` at HEAD `274e826dae6d5b7230857174a25afa1f91ab4ffb`.
Peer edits can now change the worktree; runtime must consume the immutable JSON,
not reevaluate it. **Do not run the earlier `test-runner.sh` launch example.**

The stock runner is already valid locally; no runner build is required:

- Output `/nix/store/mjlc8sc8qp6vpzf08r65jwl1y38jbgjm-test-runner`;
  deriver `/nix/store/bpfa9x3qxbq6a795kp4lnvral15s5526-test-runner.drv`.
- Native wrapper `bin/test-json-runner` SHA256
  `c90f4d93145671d8cc0c6434b5b6cdeb65c84971f2f6fdfed87e23abd587d5f2`;
  closure 37 paths, 313,125,960 NAR bytes, already present.
- `runner-identity-1.json`, `runner-identity-1-wrapper.txt`,
  `runner-identity-1-closure.json` and `runner-identity-1-source-hashes.txt`
  retain identity/transport/source receipts. Packaged direct JSON entrypoint,
  machine, machine_config and shell match worktree source. The wrapper sets
  immutable RUBYLIB/GEM paths; no local source override is used.

Native `test-runner/bin/test-json-runner` reads the supplied JSON and replaces
`TestConfig.build` with a file copy. `TestEvaluator` therefore receives the
frozen machine/script config without Nix, current-root evaluation, or an
implicit runtime build. This entrypoint omits `resources:` when constructing
`Test`, so scheduler reservation logs show zero. **External admission must
enforce the actual one VM, 2,048 MiB RAM, 2 CPUs, 2,048 MiB shared memory** and
single 10G disk; the launch script checks those JSON fields. This is an existing
entrypoint limitation, not a selected runner change.

Transport is matched: frozen old-framework JSON omits `testShellTransport`,
host `MachineConfig` defaults to `virtconsole`, and the realized guest service
`/nix/store/8qzjabjxwr3x0ibxkynqdhmbpqv58gkx-sv-test-shell-run` uses `/dev/hvc0`
(SHA256 `c856fd05ddfe7804753bfd92ed25f30226c464449f6b4b6bbf48482173d82383`).
It is still legacy transport; a capped 256-KiB snapshot can suffer backpressure.
Missing/truncated transport output is an evidence gap, not a DHCP conclusion.

### Exact next commands for lead selection

Shared runner retention **passed**, separately from VM admission. Lead's fresh
watcher ran the command below: native/overall exit 0, 0.94 seconds reported by
watcher (whole-second shell elapsed receipt is 0). Consumed `runner-root-1.*`
confirms the exact root/deriver/wrapper; no owned client remains. Implementer2
and implementer3 were notified; neither duplicates the root/build.

```sh
/home/aither/.nix-profile/bin/bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/podman/run-runner-root-1.sh
```

Script SHA256 `0cd579b9b69317081d3d339c0859ac535b43c00f1a1605fa4f1ce7e59cd3c5cd`.
It verifies session/path/JSON/wrapper identity and uses only native
`nix-store --realise /nix/store/mjlc8sc8qp6vpzf08r65jwl1y38jbgjm-test-runner
--max-jobs 0 --builders '' --add-root
/tmp/ci-failure-analysis-2026-10-22/podman/attempt-1/gcroots/runner --indirect`.
No evaluation, builder or VM. Deadline 300 seconds plus 10 seconds termination;
physical growth forecast was zero store output, <1 MiB root/log metadata, 1 MiB
log ceiling. Receipts `runner-root-1.{start,exit,native-exit,elapsed,log,deriver,
wrapper-hash,df-start,df-end,du-start,du-end}`. Nonzero stops; no retry/fallback.
The single shared runner root must remain held until lead-selected Podman,
support and hotplug consumers finish; peers have been told not to duplicate it.

Only after this step succeeds and lead explicitly selects the one-VM slot:

```sh
CI_FAILURE_ANALYSIS_PODMAN_VM=attempt-1 /home/aither/.nix-profile/bin/bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/podman/run-vm-1.sh
```

VM script SHA256 `f255bdc5786cdd2c42c68686553b366bc201ae44011fc25e7ef9f340dc08295b`;
fixed guardian `guard-vm-1.py` SHA256
`b02087d33e9c74307050a06bb8f87f030b47a5cda525f66ad2c11cc5232c6195`.
These replace the unlaunched `daaa5abe`/`5ffef389` package after the scoped
architect corrections. Native JSON, binary/resource gates, command, root
retention and 900+120-second envelope are unchanged.
Shell syntax/Python compile and inert-process quick checks pass. The VM script
and fixed VM command have not been executed. The script also authenticates the
guardian bytes and requires the literal lead-selection flag above. It verifies
both successful preparation receipts, immutable
root targets/JSON/wrapper/binary hashes, one attempt and exact machine resources,
owned path ancestry/UID, fresh absent state/scratch, >4 GiB MemAvailable,
>2 GiB free `/dev/shm` and **fresh free minus the full 24-GiB forecast >=40 GiB**
(at least 68,719,476,736 free bytes /64 GiB). This check precedes VM scratch
creation and the guardian repeats it immediately before native launch. No
measured-residual discount is used; previously realized stores are not proposed
for recreation. The 44-GiB running stop margin is separate. The script calls
only the hashed guardian, which owns this exact native invocation:

```sh
VPSADMINOS_ENABLE_UPGRADE_DIAGNOSTICS=1 \
TEST_PATH=upgrade/nested-podman-sandbox TEST_TIMEOUT=120 TEST_JOBS=1 \
TEST_RECREATE_DISKS=1 TEST_DESTRUCTIVE=1 TEST_SYSTEM=x86_64-linux \
TMPDIR=/tmp/ci-failure-analysis-2026-10-22/podman/attempt-1/vm-scratch \
  /run/current-system/sw/bin/timeout --signal=INT --kill-after=120s 900s \
  /nix/store/mjlc8sc8qp6vpzf08r65jwl1y38jbgjm-test-runner/bin/test-json-runner \
  /tmp/ci-failure-analysis-2026-10-22/podman/attempt-1/prepared \
  /tmp/ci-failure-analysis-2026-10-22/podman/attempt-1/state
```

`TEST_RUNNER_REPO_ROOT` is unset. CWD is the owned attempt. `TEST_TIMEOUT=120`
is a per-command default, not the VM deadline. The fixture body has 900 seconds;
the native command sends INT at 900 seconds and KILL after at most another
120 seconds. The guardian reserves the final five seconds of its cleanup
allowance for reaping/observation, escalating a still-authenticated group at
115 seconds. Timeout signals the owned process group, including
descendants; native cleanup is attempted, not guaranteed. If its monitored
process exits before surviving descendants, timeout does not prove they ended.
Forced/nonzero exit or absent completion evidence requires process reconciliation.

### Runtime resources, observations and end effects

Guard correction quick-check ownership: this lane owns only
`/tmp/ci-failure-analysis-2026-10-22/podman/attempt-1/guardian-check-2/` and
`repair/podman/guardian-check-2/` for these inert checks. They use imported code
with an in-memory inert command/root binding and a process provider restricted
to test-created PIDs; no live VM process/status scan is performed. A detached
test child is retained by exact birth/pidfd for owner termination after the
guard has returned and proved that it did not signal a path-only reference.
Synthetic foreign/sibling/shared-coreutils/find cases and owned temporary
symlinks exercise matching without reading any other lane's runtime state.
No VM, Nix, fixture/input change, root duplication or new VM attempt is selected.

The exact corrected guard passed all focused checks in 2.29 seconds;
`guardian-check-2/results.json` binds its SHA256. Absolute argv, QEMU `file=`/
`path=` symlink aliases and deleted-cwd suffix normalization resolve to the
canonical own root. Foreign/sibling paths remain foreign. Exact read-only
`cat` passes; shared-coreutils `rm`, dispatch override, `find -delete` and
`find -exec` remain ambiguous own references. The real inert detached child
survived native-parent exit with an empty old group: guardian status 125,
native status 0, exact child birth/PGID/reference retained, no guard signal.
The test owner then stopped only that child through its retained pidfd.
Transient observer failure and final-rescan failure also return 125; the latter
marks `final_scan_complete=false`, rather than claiming an empty successful scan.
Only test-created PIDs were read; no live support/other VM state was inspected.

Guardian quick-check ownership: the inert-process checks below may create only
`/tmp/ci-failure-analysis-2026-10-22/podman/attempt-1/guardian-check-1/` and
`repair/podman/guardian-check-1/`. These are this lane's disposable check data;
no VM, Nix command, fixed production entrypoint or new VM attempt is invoked.
Checks import the guardian without its fixed VM entrypoint, bind its command/
paths in memory to those empty owned directories and an inert Python child, and
use a 16-KiB simulated output threshold. They verify ordinary exit/reaping and
cap cancellation without a VM. Initial global-QEMU refusal was observed before
any child; this rule was removed under architect/lead clarification. Revised
checks use the unchanged session-reference policy with no foreign-process filter:
normal exit 0 (1.12s), cap exit 125/native SIGINT (3.06s), no remaining children.
Canonical sibling-path/no-ownership and own-root/ambiguity checks pass.
Final-hash checks also pass: normal exit 0 (1.15s), cap exit 125/native SIGINT
(3.08s), native birth retained, no remaining children; see
`guardian-check-1/final-results.txt`. `guardian-check-1/revised-results.txt`
retains the earlier checks. Binding flags during
these inert checks is not a VM launch selection. Retain compact results; no
deletion or cleanup outside these paths is authorized.

Keep the accepted **24-GiB full envelope**: 10-GiB disk, 10-GiB incremental
store ceiling (already measured ~0.744 GiB), 2-GiB prep scratch, 0.5-GiB logs/
transfers and 1.5-GiB contingency. No runtime store realization is selected.
The Debian fetch/cache/import/tracer copy all live inside that one disk. Rooted
runner is reused and shared-memory RAM is separate host memory, not an extra
disk. Latest read-only free space is 108,778,348,544 bytes, attempt physical
20,480 bytes, `/dev/shm` free 50,613,547,008 bytes. These moving observations
are not reservations. Retain 40-GiB floor and stop growth at <=44 GiB available.

The guardian is a synchronous, single-attempt supervisor; its one child is the
native timeout/runner in a new session/process group. It samples after each
one-second sleep plus probe time, retaining physical/apparent start/end receipts,
minimum free/RAM/SHM, peak physical growth/output and PID birth/PGID/argv of its
owned group. No Nix, retry, source change or data deletion. The fresh watcher
owns the guardian and its tool handle, checks `vm-1.guardian-latest`/result and
escalation receipts at most five seconds apart, and retains responsibility until
native effects end. There is no separately detached guardian or delayed cleanup.

**One VM means one session-owned diagnostic.** Declared canonical roots are
`podman/attempt-1`, `support/attempt-1`, `hotplug/probe-admission-1` beneath
`/tmp/ci-failure-analysis-2026-10-22/` (the last confirmed by implementer2).
The guardian matches full absolute argv atoms, QEMU `file=`/`path=` fields,
cwd/root links and canonical path components. Generic QEMU names and loose
substrings do not establish ownership. Its own proven ancestor/group processes
and exact native read-only file observer **executable plus invocation name**
are excluded (`cat`, `du`, `df`, `stat`, `readlink`, `sha256sum`, with coreutils
dispatch overrides refused). No `find` invocation is exempt. An active or ambiguous
other process referencing a declared attempt refuses admission or requests
our cancellation/reconciliation. It never signals that process. Foreign VMs
are only aggregate available-memory/SHM/CPU/disk context; their existence alone
does not refuse admission and no foreign argv is retained. Lead serialization
and the literal selection flag remain required; this is not a reservation system.

Stops are >24-GiB cumulative physical growth (measured 798,420,992 preparation
store bytes plus positive attempt/VM-receipt growth), >2-GiB scratch, <=44-GiB
free, any new host pswpin/pswpout, <2-GiB MemAvailable, trace >=32 MiB or
non-trace >=16 MiB. Count native runner/console/outer/guardian logs, snapshots,
entry/summary/transfer copies as non-trace except trace copies; the largest
trace copy is compared with 32 MiB while **all** physical copies count toward
growth. Fixed config.json, disk payload and lock files are not runtime output.
Earlier preflight receipts are not new runtime logs. The fixture pipe hard-caps
the captured guest trace at 32 MiB. **Aggregate host-output enforcement is
sampled detection/cancellation, not an absolute byte-perfect 16-MiB quota:**
bytes can arrive during a probe/sleep. Retain and label any overshoot/truncation;
do not call it complete evidence. This limitation is explicit for lead admission.

A stop sends INT only to the birth-authenticated owned native process group;
ordinary timeout owns its 900-second INT so the guardian does not repeat it.
The guardian continues observations through cleanup, reserves five seconds at
the end of the 120-second allowance for reaping after targeted KILL, and returns
125 with surviving identities when cleanup/ownership remains incomplete.
Observation failure also initiates cancellation rather than continuing
unobserved. A reserve threat during cancellation is an immediate watcher
escalation, not a reason to wait silently or touch foreign processes. Root/state
retention remains mandatory through reconciliation; a guardian result is not
proof that every possible escaped descendant ended.

At native-parent exit, observation error, lost group authentication and final
completion the guardian freshly rescans all three roots without excluding the
former native group. `guardian-result.final_own_references` retains matching
birth/PGID/executable/canonical references even when `remaining` is empty.
Any such reference or incomplete rescan returns 125 and requires watcher/owner
reconciliation; references alone never authorize a signal or deletion.

Native state is exactly `state/os-test-upgrade__nested-podman-sandbox-f01b7e09/`;
socket directory is `state/socks/`, disposable shared-dir is under that native
test state, and `TMPDIR` is the owned `vm-scratch`. Receipts are absolute
`repair/podman/vm-1.{start,exit,native-exit,guardian-exit,elapsed,log,guardian.log,
identity-check,admission,df-start,df-end,du-start,du-end,apparent-start,
apparent-end}` plus `native-process`, `admission-conflicts`, `guardian-start`,
`guardian-latest`, `guardian-peaks`, `guardian-result` and error/conflict receipts
when applicable. Native status, guardian outcome and entire script status are
separate; `native-exit: null` means the native process was not proved reaped.
Completion also records `final_scan_complete` and `final_scan_error`; on a
failed final scan any retained process/ref fields are previous observations,
not proof of absence. Before data/root release the parent still verifies exact
own process effects, native test lock availability, managed-disk removal,
socket state and physical df/du receipts. Guardian exit and an empty PGID alone
do not satisfy that disk/lock/socket/process reconciliation gate.

Fixture cleanup attempts this CT's stop (20-second command timeout), then
`machine.stop(timeout: 45)`; that method's poweroff command separately inherits
the 120-second command default. Runner `TestEvaluator#do_run` ensure invokes
QEMU reaper TERM (60-second join, then KILL), managed disk/shared-dir destruction,
log finalization and socket cleanup. `kill_after_kernel_failure` can drain up to
600 seconds, so exceptional native cleanup can exceed the selected 120-second
allowance and must be labelled interrupted by the outer stop. Watcher retains
ownership through runner/fork/QEMU/virtiofsd completion; a dead client alone is
insufficient. No deletion is performed by the launch script. Once all effects
end, retain compact native `podman-sandbox/` evidence, logs/hashes and outcomes;
then lead may remove only this attempt's stopped disposable state/scratch and
exact indirect roots. Preserve the shared runner root until all selected users
finish. Never delete store paths, foreign data or invoke global GC/lifecycle
actions. The trace still has ptrace/foreground-service observer effects and new
image provenance limits; no owner fix or original-tuple repair is established.

Stable session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-ci-failure-analysis/>.

## Preparation-time details (superseded where noted above)

### Owned metadata GC root

Lead authorized no-build re-instantiation after shared GC removed pending
derivation metadata. The already declared attempt root now also owns
`/tmp/ci-failure-analysis-2026-10-22/podman/attempt-1/gcroots/config.drv`, an
indirect native Nix GC root created with `nix-instantiate --add-root ...
--indirect` and the same testJson arguments/`allow-import-from-derivation=false`.
Check every ancestor for symlinks and the owned subtree for matching UID before
creation; never replace an existing foreign/nonmatching root. This does not
realize an output. Compare frozen fixture hashes, resulting derivation and
native JSON before accepting source/input equivalence. The lead must root any
later realized `prepared` JSON separately. Remove these **exact owned roots**
after the operation has finished and evidence/identities are retained; they
must not become indefinite input-retention roots. No shared/global GC behavior
is changed. Removal remains pending until that operation is complete.

### Cache preflight result and resolved inputs

Lead's `run-cache-preflight-1.sh` ran at HEAD
`274e826dae6d5b7230857174a25afa1f91ab4ffb`, with the frozen fixture hashes
below. Fixture dry-run exited 0 in 25 seconds; runner dry-run exited 0 in five
seconds. Neither built or launched a VM. See `cache-preflight-1-{fixture,runner}`
logs/exit/elapsed and df receipts. Dry-run reported 188 local derivations and
140 substitution paths, 1.7 MiB download/262.4 MiB unpacked. The runner reported
no missing build/substitute work, only the dirty-tree warning.

Native JSON was recovered without realization from `.drv` `env.text`, retained
as `cache-preflight-1-native-config.json`. The native derivation is
`/nix/store/wl582zy4s8csr86ll3xhi9cfzsl7k0vp-os-test-upgrade-nested-podman-sandbox.json.drv`;
its output will be
`/nix/store/08djk5zsfm3pjys6gr9l1r654sra7gq0-os-test-upgrade-nested-podman-sandbox.json`.
The recovered text SHA256 (without the receipt's added newline) is
`1610ffb3b8b94689f5c59a9d5ec6a33b4072c682b23909f84b2ebbeeb25930a2`.
It resolves **one** machine, RAM 2048 MiB, two CPUs, topology 2 cores × 1 thread
× 1 socket, one file disk `{machine}-sda.img` size `10G`, no implicit root disk,
squashfs boot, one user network and no extra shared filesystems/QEMU options.
It has manual-only tags, one attempt and one test-shell channel.

| Input | Exact selected store identity |
| --- | --- |
| Kernel | `/nix/store/fmdhcn3ppkqavl6p6isa7wiahaa0p19x-linux-6.18.49/bzImage` |
| Kernel source | kernel derivation `g4hykqld77rwdz59m6zyfsmx2q7vmm9s-linux-6.18.49.drv`, `src=/nix/store/yk4sm56w22wnm4bs9jkc2qagh7225n3p-fbda79346b89b2d2486edd22e4bbbca0154d96b7.tar.gz` |
| Kernel config | `/nix/store/3pk4dxbica1zpjs367i6cvd83ifqcjnn-linux-config-6.18.49` (substitute, not yet read) |
| Initrd | `/nix/store/43kf2qmcadgpx0i04igr7z72lrsksa7n-initrd/initrd` |
| Guest system | `/nix/store/c4wsms6z0fq01i20cni9zgsg7vav8q1m-vpsadminos-system-vpsadminos-26.05pre-git` |
| Squashfs | `/nix/store/m4kh8png375l4ja1whl6i9dlyhkxqyf9-squashfs.img` |
| LXC | `/nix/store/y2w16d8k1pgpnf14dp87fc05xv18vm46-lxc-6.0.6` (substitute) |
| Tracer | `/nix/store/fm52yr0c85y35l2n0k9xc68nbz93y9bj-strace-7.2/bin/strace` |
| QEMU | `/nix/store/liim1i7qfgzaz4mkwsq2vziic3708niz-qemu-host-cpu-only-for-vm-tests-10.2.4` |
| virtiofsd | `/nix/store/kc617vcqcgf08gqzdfxz2r2hv6d1dc6w-virtiofsd-1.13.3` |

The resolved tracer already exists, executable SHA256
`d4c306137a10295a7e473a5666ec409450e49c75655262db37d7b4c07b3d3f5c`.
Its 25-path closure is 75,374,552 NAR bytes and 78,225,408 physical bytes;
the native path-info/closure receipt is `cache-preflight-1-tracer-closure.json`.
This is the actual selected tracer, distinct from the earlier ambient candidate.
The exact native input graph is `cache-preflight-1-input-graph.dot`, 4,261,108
bytes, SHA256 `46eef6158d851af573e8f20ed851a6323f8298b3487a6f02e38ed2251185bb65`.
Native selected/all-missing-builder recipes are retained alongside it.

Inspection distinguishes work from compilation: the actual kernel derivation
is **absent** from the build list and its binary is in the substitute list.
`linux-6.18.49-modules` is a prefer-local symlink union plus depmod over that
kernel; `modules-shrunk` copies the needed closure. `zfs.drv` here creates an
empty output directory. These are not a kernel/OpenZFS compilation. Most other
builders produce scripts/wrappers, runtime closure metadata, initrd and
squashfs; `mdadm-4.4` does require a small userspace C build. No tracer build is
needed. This baseline userspace build is disclosed for the lead's preparation
decision; it is not an owning-component repair or kernel-build authorization.

Shared GC removed 34 unrooted recipe paths during inspection. Lead-authorized
`nix-instantiate --add-root .../gcroots/config.drv --indirect` completed in
42.53 seconds, no realization, at the same HEAD/hashes. It copied a source path
from the cache, returned **the same derivation**, and its native JSON is
byte-identical to the first receipt. All 188 recipes then existed and were
captured completely in `cache-preflight-1-build-derivations.json`. Rooting logs,
exit and source HEAD are retained. The exact root is currently held for the
pending operation, with removal obligation above.

### Physical forecast and next preparation proposal

Resolved disk/RAM/topology match the existing 24 GiB envelope. The entire
Debian archive, repository cache, imported rootfs, tracer copy (~75 MiB), guest
logs and ZFS transient/copy-on-write growth live **inside the single 10 GiB
disk**, whose full physical capacity is already budgeted. No separate host
Debian download/image copy is selected. Original-image provenance is still
unavailable; this remains a new image sample. Its exact package/archive hashes
must be captured during this one startup, and success cannot certify repair of
the original image.

For host preparation, retain the conservative **10 GiB incremental store
allowance** for the 262.4 MiB known substitutions plus all generated outputs,
module union/copy, initrd and compressed system image; actual generated output
sizes cannot be measured until built. Retain **2 GiB scratch** for serial,
two-core userspace/wrapper/image generation and **0.5 GiB transfers/logs** plus
1.5 GiB contingency. Existing tracer closure is reused in the store; its guest
copy is inside the disk allowance. The full build-time graph contains existing
compiler/kernel-source inputs but does not imply realizing them when cached
kernel outputs are substituted. Any unavailable expected kernel substitute,
unexpected compiler output, >10 GiB store growth or >2 GiB scratch blocks this
proposal rather than widening it silently.

Latest read-only df is 111,387,168,768 bytes free on the shared filesystem and
50,613,547,008 bytes free on `/dev/shm`; lane receipts use ~4.7 MiB physical.
After the full 24 GiB ceiling, ~79.7 GiB would remain, above the 40 GiB floor.
These are current observations, not a reservation. Recheck immediately before
the scheduled operation and enforce the 44 GiB stop margin.

Proposed next **fresh watcher** preparation, not executed: first substitute and
root the exact kernel and LXC output paths using `nix-store --realise <output>
--max-jobs 0 --add-root <attempt>/gcroots/{kernel,lxc} --indirect`. This phase
must be substitution-only; it must not realize a kernel derivation. Once those
outputs are present and retained, realize the **rooted exact config derivation**
with `nix-store --realise <attempt>/gcroots/config.drv --add-root
<attempt>/prepared --indirect --max-jobs 1 --cores 2`. Use the already accepted
20-minute preparation ceiling, physical limits and stop on any actual
kernel-source build. A missing input/changed dependency receipt requires new
inspection. Root the prepared JSON explicitly; compare its bytes with the
recovered native JSON, and record actual kernel/config/LXC/system/squashfs
hashes plus physical store/attempt/df totals before any separate VM launch.
No realization or VM has yet been performed by this lane.

Exact proposed preparation commands, for the lead's fresh watcher only:

```sh
nix-store --realise /nix/store/fmdhcn3ppkqavl6p6isa7wiahaa0p19x-linux-6.18.49 \
  --max-jobs 0 --add-root /tmp/ci-failure-analysis-2026-10-22/podman/attempt-1/gcroots/kernel --indirect
nix-store --realise /nix/store/y2w16d8k1pgpnf14dp87fc05xv18vm46-lxc-6.0.6 \
  --max-jobs 0 --add-root /tmp/ci-failure-analysis-2026-10-22/podman/attempt-1/gcroots/lxc --indirect
nix-store --realise /nix/store/wl582zy4s8csr86ll3xhi9cfzsl7k0vp-os-test-upgrade-nested-podman-sandbox.json.drv \
  --add-root /tmp/ci-failure-analysis-2026-10-22/podman/attempt-1/prepared --indirect --max-jobs 1 --cores 2
```

Stop on any nonzero command; no retry or fallback to building the kernel.
Every exact GC root above belongs to this attempt and shares the recorded
post-operation removal obligation. No command in this block has been run.

### Selected preparation script, not executed

Lead accepted **preparation only**, with no VM or implicit runner build.
Exact runnable script:
`/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/podman/run-preparation-1.sh`,
SHA256 `d9113357cd5f50e6cc606b861439819080b5b9985bfb7614b8f1fb52e4b27db6`.
`bash -n` passed and all absolute executable paths exist. Run it once through
a fresh watcher, using the 1200-second preparation deadline and accepted native
termination/reconciliation policy. No part of the script was executed by its
author.

The script guards the complete session environment/current slug, frozen fixture
hashes, exact config-root target and expected native JSON text hash. It checks
owned path ancestry/UID, refuses preexisting output roots or completed attempt
receipts, then uses only absolute commands and the immutable rooted derivation.
Both output-substitution steps specify `--max-jobs 0 --builders ''`; config
realization specifies `--max-jobs 1 --cores 2 --builders ''` after checking the
kernel and LXC outputs valid. First substitution failure stops without retry.
The native step exit statuses, complete bounded logs, start/end df, physical
du/apparent size, source hashes, current HEAD, elapsed time and overall exit
are recorded as `repair/podman/preparation-1*`.

`TMPDIR` is exclusively
`/tmp/ci-failure-analysis-2026-10-22/podman/attempt-1/scratch`. New physical
store bytes are measured against the pre-step baseline for the native
preflight's exact planned outputs/substitutes, without a whole-store du or
foreign cleanup. Checkpoints enforce the 44 GiB free-space margin, 2 GiB
scratch and 10 GiB incremental store limits **between steps**. During a running
Nix command, the fresh watcher must also monitor growth/output against those
same limits and stop the owned operation when exceeded; these checkpoints do
not claim continuous enforcement. Keep total preparation logs below the
16 MiB other-output budget. A timeout/stop must retain ownership until any
Nix daemon builder effects are reconciled; a dead client alone is insufficient.

On success, the script compares the exact prepared store path, SHA256 and
JSON bytes against the no-realization receipt; checks machine/disk/resource
identities and selected stores; captures kernel/initrd/squashfs/LXC/tracer
binary hashes and the native realized runtime-closure receipt. It does not
launch a VM, evaluate a changed source, build a runner or choose any fix.

Pending retained roots are exactly `gcroots/config.drv`, `gcroots/kernel`,
`gcroots/lxc` and `prepared` under this attempt. The corresponding substituted
outputs are the exact kernel/LXC paths in the table above; store paths are
never manually deleted. Keep only the roots needed for the separately selected
diagnostic; after its effects end and compact evidence is retained, remove
these exact indirect roots and owned scratch through the lead's native cleanup
handoff. Failed/uncertain effects keep them held. This is disposable-data/root
cleanup only, with no session lifecycle action or global GC.

## Source and first result

Owned worktree:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-ci-failure-analysis/vpsadminos`.
Verified branch `2026-10-22-ci-failure-analysis`, base/HEAD
`846bb469505789ba0b2a405fa5905ba6d8253006`, workspace-write access.
Assigned uncommitted files are `tests/suite/upgrade/nested-podman-sandbox.nix`
and `tests/suite/upgrade/nested-podman-sandbox/capture.rb`. Implementer3 owns
registration in `tests/all-tests.nix`; requested manual-only registration.
Lead owns all Git mutation windows. Record final HEAD/diff/file hashes after
registration before scheduling preparation; no unrecorded source change may
enter the selected operation.

Prepared file SHA256 (after observer-effect revision, base HEAD unchanged):
`nested-podman-sandbox.nix`:
`50adb5e71e118eee475724bae3c411ece42cecb339b228652e79f624678dd961`;
`nested-podman-sandbox/capture.rb`:
`89fa3430cdce7999c6d9815ebe90f3c5acb3d759f3999554b9d894621d53004c`.
Ruby syntax and Nix parsing passed. Hook lint/evaluation are still pending.

Minimum result: exact arguments, return/errno and ordering for
`PR_SET_NO_NEW_PRIVS` versus `PR_SET_SECCOMP` from one Debian DHCP startup.
Plain merged strace records forks, UID/GID/capability transitions, prctl,
seccomp, chroot and resource limits. The original networking unit's first
`ExecStart=/usr/sbin/ifup -a --read-environment` is replaced by a trace wrapper;
the remaining unit commands/restrictions are preserved. A diagnostic
`TimeoutStartSec=60s` bounds this one network startup. The original and altered
unit, effective configuration, input files and this instrumentation difference
are retained. No APT/Podman, second container start or target activation.

Foreground `strace -f` remains attached to daemonized dhcpcd children after
ifup exits. This can keep the oneshot ExecStart running until the imposed
60-second service timeout kills it. **Networking-service timeout/failure under
this wrapper is instrumentation-affected, not the natural DHCP outcome.** No
untested detach mode is introduced. The trace's original ifup PID/exit record
and early prctl arguments/results are summarized separately; absent PID/exit
identification stays explicitly unresolved. Only a trace-linked early syscall
denial can support recurrence of the original setup chain. Successful early
calls followed by the imposed timeout do not establish a DHCP defect.

Ptrace, its extra parent/child processes, the added tracer closure and the
unit deadline can affect a guard/timing-sensitive failure. The wrapper-entry
status and successful credential-changing syscalls do not supply exact
`/proc/<failing-tid>/status`/filter bytes at the failing prctl. The first trace
does not wait for an elaborate recorder. Any remaining effective-state gap is
reported; a non-reproduction cannot exclude the recorded incident mechanism.
Capture completion is not a DHCP or upgrade acceptance pass.

## Immutable inputs and current identity gaps

- OS predecessor: `3cb830e596a7fed900bec49f50c9b6cf51e76bb5`, its locked
  nixpkgs `e4bae1bd10c9c57b2cf517953ab70060a828ee6f`, and its unstable config.
  Only test transport follows the current source; no target closure is added.
- Kernel: predecessor selects 6.18.49 from
  `fbda79346b89b2d2486edd22e4bbbca0154d96b7`; OpenZFS source
  `4ded9ca89108e507377ff3d613038bea16018b2d`; LXC 6.0.6 source
  `d510d66005fb974b19425fb6a12b87bbde8ae36c`. Actual prepared kernel/initrd/
  squashfs/system store paths, hashes, config and closure graph must be
  captured before launch. Runtime `uname`, boot ID, boot/current paths and
  actual kernel config are captured, not inferred from source.
- Historical system
  `/nix/store/h772xsck07kn6w9zyw32l6q9gs0xyfhq-vpsadminos-system-vpsadminos-26.05pre-git`
  and LXC `/nix/store/y2w16d8k1pgpnf14dp87fc05xv18vm46-lxc-6.0.6` are absent
  locally. The diagnostic system closure will differ because it has no target
  extraDependency and does include trace tooling. Same kernel release alone
  does not prove identical binary/configuration.
- Failing image: Debian 13.7, dhcpcd-base `1:10.1.0-11+deb13u4`, ifupdown
  `0.8.44+deb13u1`. Original archive/hash was not retained in the incident
  artifacts; no recoverable owned archive has been identified. The fixture's
  `debian/latest` fetch is a **new sample**, whose repository cache file hashes,
  package identities and config are captured before its first start. Never
  call a new-image success repair of the original tuple. If an authentic
  archive becomes available, coordinate input adaptation before selection.
- Tracer selected by fixture: `pkgs.strace` from the exact predecessor
  nixpkgs input, closure copied into the stopped guest root before first start.
  Its **resolved path/version/hash and complete runtime closure await native
  evaluation/cache preflight**. No static tracer build or broad store mount.
  Ambient `/nix/store/3ckzaiiy8xnzv2f5cqs82gywsylhc0mf-strace-7.2` exists,
  closure 75,432,480 bytes and executable SHA256
  `9096a9cafe3673bae8a9bb3d4c3de3df63c78b8149870120c01b0440531ed52d`;
  it is a measured fallback candidate, not silently substituted for fixture
  tooling. A change to use it needs an explicit input amendment.

## Exact preparation and run commands

Run from the owned worktree. Before any operation the lead/watcher records
`git rev-parse HEAD`, `git diff --stat`, fixture SHA256 values, untracked fixture
bytes and registration diff. Recheck session binding and the no-other-VM rule.

First command is a **cache/preparation query only**, after registration and
creating the declared empty owned attempt directory. It is scheduled separately
with a 5-minute ceiling, at most 2 MiB output, no VM and no local build:

```sh
VPSADMINOS_ENABLE_UPGRADE_DIAGNOSTICS=1 nix-build test-runner/nix/evaluate-tests.nix \
  --arg repoRoot /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-ci-failure-analysis/vpsadminos \
  --argstr system x86_64-linux --argstr mode testJson \
  --argstr testPath upgrade/nested-podman-sandbox --argstr testArgsJson '{}' \
  --out-link /tmp/ci-failure-analysis-2026-10-22/podman/attempt-1/prepared \
  --dry-run --max-jobs 0
```

Inspect the complete dry-run build/substitute paths and sizes. A required local
Linux kernel build is a blocker. Lack of cache proof does not authorize one.
Record missing lightweight derivations separately (test JSON, squashfs,
wrapper), their dependencies and conservative physical size before preparation.
Derivation/input inspection may be scheduled next without executing the VM.
Resolve the exact tracer and actual boot stores in the resulting native JSON;
the local-build allowance, substitution sizes and full identities are still
**pending**, so no preparation/launch is ready yet.

Once this query is accepted, the preparation command is the same command with
`--dry-run --max-jobs 0` replaced by `--max-jobs 1`. It has a separate 20-minute
ceiling and must stop if unexpected kernel compilation begins or measured
growth exceeds the envelope. The lead must also preflight the stock runner
(`VPSADMINOS_ENABLE_UPGRADE_DIAGNOSTICS=1 nix build --dry-run .#test-runner`)
and prepare it before the VM; wrapper
`test-runner.sh` otherwise builds it implicitly. No VM runs during preparation.
The lead must also arrange source visibility for Nix's Git-filtered flake
snapshot: the new fixture files are currently untracked, and adding/staging
them requires a lead-issued Git window. The explicit direct test-JSON query
can read working-tree paths, but ordinary registered metadata may use the
filtered flake. Do not mistake missing source visibility for a cache failure.

After all inputs are prepared and the one-VM slot is available, exact native
launch is:

```sh
VPSADMINOS_ENABLE_UPGRADE_DIAGNOSTICS=1 ./test-runner.sh test --fresh --jobs 1 --timeout 120 \
  --state-dir /tmp/ci-failure-analysis-2026-10-22/podman/attempt-1/state \
  upgrade/nested-podman-sandbox
```

Native `--timeout 120` is the default for individual guest commands, **not**
an overall test or build deadline. The fixture encloses boot/setup/capture in
Ruby `Timeout.timeout(900)`; the watcher enforces the 15-minute VM-body bound
plus at most 120 seconds of native termination/cleanup. Preparation is a
separate 20-minute operation. At runtime only one `osctl ct start` is issued.
The unit has a 60-second startup deadline and the poll has a 60-second monotonic
deadline; there is no 900-second online readiness retry. A terminal service
outcome ends observation early, with the observer-effect qualification above.
No networking success/failure is inferred from diagnostic completion or the
instrumented unit result.

## Ownership, physical allocation and hard stops

Declared disposable root, not yet created:
`/tmp/ci-failure-analysis-2026-10-22/podman/attempt-1/`.
Its `state/`, `prepared` symlink, operation logs and transfers belong only to
this session/attempt. Reject existing nonempty/foreign/symlinked roots. The
resolved root must remain under this exact owned path; no source-session state
or runner/VM is reused. Compact retained results go under this session's
`repair/podman/`, with source/input hashes and exact outcomes in this brief.

One VM: 2048 MiB RAM, two vCPUs, one 10 GiB file-backed ZFS disk. Budget the
disk at **10 GiB physically allocated**, even though initial sparse allocation
is small. No NixOS root image, swap image, target-generation copy, Podman image
or new kernel output is selected. Conservative incremental envelope:

| Consumer | Physical allowance |
| --- | ---: |
| Sparse test disk, including guest image cache/tracer/rootfs | 10 GiB |
| New substituted Nix closures, including kernel/system/initrd/squashfs | 10 GiB |
| Lightweight preparation scratch and copies | 2 GiB |
| Trace/log/shared transfer copies and retained output | 0.5 GiB |
| Contingency | 1.5 GiB |
| Total stop threshold | 24 GiB |

These are source-declared allowances, not resolved resource proof. Before VM
launch, inspect the prepared native JSON's complete `machines` mapping, actual
RAM/CPU/topology and **all disks** (including implicit boot/root disks), actual
kernel/initrd/squashfs paths and the tracer closure. Compare every resolved
store against its cache/physical-size receipt. Any discrepancy or extra disk
blocks launch until the lead revises/accepts the budget. Source release names
do not substitute for binary input identity.

Host memory is separately 2 GiB plus QEMU overhead; `/dev/shm` backing, if used,
must be counted against its own 2 GiB availability rather than assumed disk
growth. If memory causes host swapping, stop this operation. The actual Nix
closure shortfall is not yet measured; a >10 GiB shortfall blocks this envelope.

Read-only preflight observed `/dev/vda1` free 113,905,709,056 bytes (~106.1 GiB).
This is a measurement, not a reservation. Immediately before preparation and
VM launch record `df -B1 /tmp /nix/store /dev/shm`, physical `du -x -B1 -s` on
the owned attempt and `du --apparent-size -B1 -s` separately. Record the same
after preparation, at peak if practical, before cleanup and after cleanup;
include new store-path physical totals, not an entire `/nix/store` walk.

The lead's watcher rejects any projected free space below 40 GiB. Stop owned
growth at <=44 GiB available (4 GiB margin) or >24 GiB measured incremental
allocation. Never start another VM or compensate with global GC/foreign data
deletion. Capture stops at 32 MiB trace or 16 MiB other logs. The trace pipe
uses `head -c 33554432`; a trace exactly at that cap is incomplete, not proof
of a complete call chain. Each named snapshot field has its own command exit
marker; `head_status` is explicitly only the pipe reader status. A missing
marker, cap-sized output, nonzero field status or empty field is marked in the
capture and must not count as successful config/unit/identity evidence.
Per-field output is capped at 256 KiB; the fixture reserves metadata space and
refuses after its 16 MiB other-output budget. Watcher also counts runner,
console and outer operation logs toward that other-output limit and terminates
owned execution if reached. Do not let kernel-failure dump draining overrun
the accepted time/output bound; preserve a labelled truncated dump.

## Termination, native cleanup and causal decisions

Normal fixture cleanup stops this container then calls `machine.stop(timeout:
45)`; the runner's `do_run` ensure calls the owned QEMU reaper's `kill`,
`destroy`, `finalize`, `cleanup`. Managed disks are deleted by default; do not
select `--no-destructive`. Evidence is copied out of shared transfer state
before destruction to the native test state's `podman-sandbox/` directory.

On outer time/space/output stop, interrupt the exact runner operation so its
native ensure can execute; retain the watcher handle until its runner, QEMU,
virtiofsd and Nix clients/build effects have ended. If native cleanup cannot
run, report the exact residual PID/process birth/command/paths and reconcile
through the owned native process handles before removal. Do not run broad
`pkill`, kill foreign VMs or delete data while processes hold it. Only after
shutdown/effects are proved ended may this attempt's disposable disk/transfers
be removed, retaining compact logs/hashes. No cleanup command is authorized
against any other path; no lifecycle action is selected.

Interpretation: NNP EACCES means filter entry was not reached in that call;
NNP success followed by filter EACCES distinguishes guard/LSM/outer-filter
paths from the ordinary missing-NNP precondition. EPERM from a measured outer
filter differs from the incident's EACCES wording. Both prctls succeeding
followed by SIGSYS/kill is a later-filter mechanism. No denial/owner conclusion
without actual trace linkage. A proven owning-component change needs source
allocation, compatibility/provenance and packaging/build plan through the lead
and architect; there is no speculative security exception or predecessor repin.

Prepared quick checks: Ruby syntax and Nix parse pass for allocated fixture;
no Nix evaluation/build, VM or product regression has run. Registration,
complete source hashes after registration, resolved tracer/kernel stores,
substitute availability/size, actual image provenance and the scheduled watcher
remain prerequisites. Implementer3 confirmed registration under the explicit
`VPSADMINOS_ENABLE_UPGRADE_DIAGNOSTICS=1` option alongside first-switch;
default unfiltered suite excludes both manual diagnostic fixtures. Future
accepted fix needs confined DHCP plus full nested
Podman continuity regression and mandatory independent review at the completed,
committed deliverable boundary, following the repair design.

Lead independently accepted the final fixture receipts and explicitly released
the owner1 Git window before cleanup. Native removal of only the clean
`vpsadminos-podman-commit` checkout is authorized; owner3 now owns Git.
Coordination message `7f843472-60d2-466a-bf49-197863ed2cc8` offers removal
inside owner3's window or after its release. No concurrent Git cleanup is run.
The cleanup receipt remains pending that serialized operation, not another
source acceptance gate.

Authorized serial cleanup is complete after owner3 support checkout removal.
`fixture-checkout-removal-result.json`: native `git worktree remove` exit0 in
0.285s for only the clean detached405a Podman checkout; directory/registration
absent, exact own refs empty with four permission gaps qualified, command ended.
Feature HEAD stays87e6bd4a and index empty. No force, signals, source changes,
root or backup removal. Free space113,448,812,544 bytes after removal (moving
shared-host observation). Lead's fresh watcher owns preparation2 exclusively;
no owner launch/query/observation occurred.
