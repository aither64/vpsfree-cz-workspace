# Prepared candidate checks

Prepared for committed source `aa963dce42859ae4251cdfaded91920d67b3a46e`.
The primary image test passed with this stable Leap 16.0 builder; extraction
and focused checks remain pending. The earlier
`fe9182dd2fb1ba627c30d54c39c1acd7b140df69` failed using the old builder;
original evidence is preserved. Lead owns watcher delegation and verification
after affected-lane review of the substantive builder change.
Run from the session's vpsadminos worktree. Stop on unexpected local kernel
builds. These commands use existing runner/debug/repository interfaces and do
not modify project source or production repositories.

Every runner/debug command below requires the session-owned
[test-revision.nix](test-revision.nix), directly or through the separate
export-only module. It supplies exact revision metadata missing from immutable
runner snapshots; see
[diagnosis](runtime-revision-diagnosis.md). Keep its revision matched to the
tested source if the feature head changes.

Capture command/REPL transcripts in this session as `image-test.log`,
`candidate-extract.log`, `candidate-http.log`, `candidate-start-stop.log`,
`candidate-rundir.log`, `candidate-cgroup-v1.log`, `candidate-cgroup-v2.log`,
`candidate-device-units.log` and `candidate-netif-routed.log`.
Keep native test-runner logs under the explicitly owned state directories below.

## Primary test and retained artifact

```sh
env VPSADMINOS_CONFIG=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/test-revision.nix ./test-runner.sh test --no-destructive --state-dir /tmp/2026-11-03-opensuse-leap-image-build-image image-scripts/test@opensuse-leap-16.1
```

Record exact tested source, result and native runner logs. On success, retain
this owned state until extraction and focused verification finish. Default
destructive mode would delete the candidate's data disk. The first 24 GiB export
boot stalled before a guest shell; [diagnosis](export-lockup-diagnosis.md) records
the evidence and uncertainty. The single proposed recovery reopens the same
test/disk with separate [8 GiB export config](export-revision-aa963dce4.nix),
SHA256 `d62ca05d0bd7c26af345f538e561cf77f346144b11c062793eee715cf1128b4a`:

```sh
env VPSADMINOS_CONFIG=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/export-revision-aa963dce4.nix ./test-runner.sh debug --state-dir /tmp/2026-11-03-opensuse-leap-image-build-image image-scripts/test@opensuse-leap-16.1
```

Allocate a PTY with live stdin for this command, wait for the Pry prompt, and
evaluate the fixed [Ruby input](candidate-extraction-aa963dce4.rb). Its SHA256 is
`feb4df2ff8c042fac40a7dc729a0296f4dcc59a5fc3932070b30a1775366b6fc`.
Keep that input unchanged; any later correction gets a new input file/hash.

```ruby
eval(File.read('/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/candidate-extraction-aa963dce4.rb'), binding, 'candidate-extraction-aa963dce4.rb')
exit
```

The input records the retained `builder-d5ddc633` container's distro/version,
actual `/etc/os-release` and `rpm --version`, starting/stopping only that builder
to query it. It hashes any existing Leap 16.0 archive/stream in the standard
repository cache; absence is recorded as unknown, with no downloads or forensic
search. If both formats exist, record both hashes without claiming which was
used unless existing metadata establishes that. Then it hashes/exports the
successful 16.1 candidate through the already prepared repository path. Capture
the full PTY as `candidate-extract.log`, and verify native debug exit before
starting focused VMs.

Keep the successful primary's 24 GiB configuration unchanged. For this export
recovery verify fresh RAM/shm headroom and new JSON's 8192 MiB memory with the
same kernel/initrd/disk before the eval. The first guest watchdog is an immediate
escalation; use normal interrupt/Pry exit, retain the disk and stop rather than
repeat automatically. Capture this recovery in `candidate-extract-recovery.log`.

If the directory already exists from an interrupted attempt, inspect it before
resuming; `mkdir` deliberately refuses to mix candidate repositories. Record the
printed image SHA256, source head, exported repository SHA256 and state path.
On the host:

```sh
mkdir /tmp/2026-11-03-opensuse-leap-image-build-candidate-repo
tar -xf /tmp/2026-11-03-opensuse-leap-image-build-candidate-repo.tar -C /tmp/2026-11-03-opensuse-leap-image-build-candidate-repo
sha256sum /tmp/2026-11-03-opensuse-leap-image-build-candidate-repo.tar
python3 -m http.server --bind 127.0.0.1 --directory /tmp/2026-11-03-opensuse-leap-image-build-candidate-repo 18080
```

Keep this server foreground in a separate owned terminal. Default QEMU user
networking reaches the host loopback server at `10.0.2.2:18080`. Stop it through
its terminal after all focused checks. Do not reuse an occupied port blindly.

## Native batch considered: repository readiness limit

A separate module importing `./test-revision.nix` and setting
`osctl.pools.tank.repositories.default.url = "http://10.0.2.2:18080"` merges
through the existing pool/repository submodules. It does not change the primary
revision module. Native selection supports one quoted flat brace pattern:

```text
{dist-config/start-stop,dist-config/systemd-rundir,cgroups/mount-v1,cgroups/mount-v2,systemd/device-units,dist-config/netif-routed}#opensuse-leap-16.1
```

`TestScript#path_matches?` uses `File.fnmatch?` with `FNM_EXTGLOB`; the CLI reads
only `args[0]`, so six positional patterns are not a substitute. A future native
batch could bound concurrency with `--jobs 2` and yield standard aggregate
results, provided repository readiness is established first.

The requested URL-only shape does not establish that prerequisite. Its
`repositories-tank` service runs asynchronously after the pool becomes active,
while `wait_for_osctl_pool` only waits for that active state. The first
`osctl ct new` can therefore race the URL update; `systemd-rundir` does not even
wait for networking. Existing runit options provide no depends/after readiness
field for this ordering. Architect0 independently confirmed the limit. Under
the no-new-hook constraint, no executable focused-candidate module or native
batch has been created. Retain the manual sequence below, where setting the
default URL completes before invoking each selected script. No expensive probe,
listing, test or server was started to assess this option.

This asynchronous setter is introduced by the proposed URL module. The actual
manual baseline has empty pool/repository declarations, revision-only test
configuration, no optional `os/configs/tests.nix`, and no `repositories-tank`
service. Pool setup loads repositories before marking the pool active, so the
manual setter runs after initial default creation. It synchronously saves the
candidate URL; subsequent VM restarts load that saved default instead of
replacing it. Thus start-stop and routed-network restarts preserve manual
candidate selection. Assert the baseline and read back the exact URL before
running any script, as below. An unexpected service or URL stops setup.

## Exact focused scripts in existing debug REPL

All six fixtures use `boot.qemu.memory = 8192` MiB and `cpus = 4` defaults
from `os/modules/system/boot/qemu.nix`; their tank/with-tank fixtures and the
revision module add no overrides. `tests/make-test.nix` passes those values to
the VM. Two concurrent PTYs therefore require 16 GiB RAM, 16 GiB shared memory
and 8 vCPUs; six would require 48 GiB and 24 vCPUs. Finish and exit the 24 GiB
extraction VM first, then check actual free memory and `/dev/shm` before the
lead's fresh watcher schedules at most two focused PTYs concurrently. Keep
manual URL preparation in every PTY; no readiness hook is introduced.

Every debug invocation, including extraction above, requires an allocated PTY
with stdin kept open. With the tool runner, use `exec_command` with `tty: true`,
wait for the Pry prompt, and send the Ruby batch through `write_stdin` on that
live session. Capture the prompt/output and final native exit. A plain non-TTY
launch can close stdin and exit before inspecting anything; do not count that
as verification or repeat it without the explicit input strategy.

Open each of these commands separately; use a new terminal transcript/native
runner logs beneath this session for each. No focused script is run by `debug`
until invoked in the REPL below.

```sh
env VPSADMINOS_CONFIG=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/test-revision.nix ./test-runner.sh debug --state-dir /tmp/2026-11-03-opensuse-leap-image-build-start-stop 'dist-config/start-stop#opensuse-leap-16.1'
env VPSADMINOS_CONFIG=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/test-revision.nix ./test-runner.sh debug --state-dir /tmp/2026-11-03-opensuse-leap-image-build-rundir 'dist-config/systemd-rundir#opensuse-leap-16.1'
env VPSADMINOS_CONFIG=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/test-revision.nix ./test-runner.sh debug --state-dir /tmp/2026-11-03-opensuse-leap-image-build-cgroup-v1 'cgroups/mount-v1#opensuse-leap-16.1'
env VPSADMINOS_CONFIG=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/test-revision.nix ./test-runner.sh debug --state-dir /tmp/2026-11-03-opensuse-leap-image-build-cgroup-v2 'cgroups/mount-v2#opensuse-leap-16.1'
env VPSADMINOS_CONFIG=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/test-revision.nix ./test-runner.sh debug --state-dir /tmp/2026-11-03-opensuse-leap-image-build-device-units 'systemd/device-units#opensuse-leap-16.1'
env VPSADMINOS_CONFIG=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/test-revision.nix ./test-runner.sh debug --state-dir /tmp/2026-11-03-opensuse-leap-image-build-netif-routed 'dist-config/netif-routed#opensuse-leap-16.1'
```

These six scripts cover every newly scheduled explicit 16.1 public-image matrix
case identified in the CI inspection. This is a prepared candidate check list;
the commands require separate lead-owned execution after the primary image test.

The device-unit test expects success for explicit `leap-16.1`. Its existing
expected-failure exception covers only `opensuse/latest`; preserve that scope.
A 16.1 failure needs actual candidate/runtime diagnosis before considering any
image change or expected-failure classification.

In each REPL, prepare its VM's existing default repository and execute exactly
the selected prepared script using the fixed
[focused input](candidate-focused-aa963dce4.rb), SHA256
`260bf1802900fdb8c3842788928feef0a31c906e66ec587b33d53509e9bf9987`:

```ruby
eval(File.read('/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/candidate-focused-aa963dce4.rb'), binding, 'candidate-focused-aa963dce4.rb')
exit
```

Keep the input unchanged during execution. It retains setup/selected-script
guards, exact URL readback and the existing `run_script` JSON result, and raises
on any setup or script failure. It emits `CANDIDATE_FOCUSED_PASSED` with the exact
selected path and source only after `successful?` is true. The watcher must
require this marker and record raised failures even if Pry remains open; a
normal debug process exit alone does not prove a script passed. Send `exit`
normally after recording the result and confirm native VM exit.

`run_script` is the existing evaluator method used by normal execution; no new
runner wrapper or test script is introduced. REPL results are manual verification
evidence rather than a standard `test` command aggregate report. Keep the JSON
success result and native VM log with source/artifact identity. If this manual
path encounters a framework/interface problem, report the exact gap and stop;
do not expand test infrastructure. Retained VM disks and candidate files remain
owned test data until normal verification cleanup; this does not close the
development session.
