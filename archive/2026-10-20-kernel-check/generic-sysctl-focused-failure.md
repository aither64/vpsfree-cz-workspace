# First focused sysctl VM attempt

Exact head `88486d43f7d47917b6ab796163abf8cd1f0be94a`; command
`./test-runner.sh test system/sysctl` executed once, exit 1, elapsed 187 seconds
(native runner 159.54 seconds). No rerun was performed at this checkpoint.
[Full command output](generic-sysctl-focused-vm-88486d43f.log).

The existing watcher recorded OS/cache job `119758301061` success at
2026-10-22 10:07:28 UTC (12:07:28 CEST). The focused command started at
12:09:47 CEST, after that job succeeded, while overall CI remained active.
There was no requirement to wait for the whole pipeline. Local watcher log:
`generic-sysctl-ci-39759039117.log`.

The kernel image `/nix/store/4k5kg0x1msvl4kffpr2g7cidpnwbnkhk-linux-6.12.113`
was copied from cache.vpsadminos.org (native runner line 118). Kernel modules
and shrunk modules derivations were locally assembled; the log does not show
a kernel-image compilation. All initial and five switch OS closures were built
before the guest attempt.

The failure occurred in before-suite setup, before any example. QEMU started
at 12:11:51 CEST; the 60-second `/service/sysctl/check` deadline expired at
12:12:52. The runner then terminated QEMU and destroyed its disposable guest.
Native result is `unexpected_failure`.

Preserved native files are copied under
`generic-sysctl-focused-first-failure/` from
`/tmp/os-test-runner/os-test-system__sysctl-8ae7035e/`:
[runner](generic-sysctl-focused-first-failure/test-runner.log),
[console](generic-sysctl-focused-first-failure/machine-console.log),
[shell](generic-sysctl-focused-first-failure/machine-shell.log),
[machine lifecycle](generic-sysctl-focused-first-failure/machine-log.log),
[configuration](generic-sysctl-focused-first-failure/config.json) and result.
Console contains only firmware/iPXE/Booting-from-ROM output before harness TERM;
the shell log contains only its initial header, no command record. No guest
sysctl log, runtime value, stamp or supervisor evidence was obtainable from this
attempt. The service was not shown to execute, succeed or fail.

Source establishes a fixture setup defect: `Machine#start` defaults to
`wait_for_boot: false` (`osvm/lib/osvm/machine.rb:221`), whereas `Shell#execute`
waits for test-shell readiness inside the supplied command deadline
(`osvm/lib/osvm/shell.rb:156`). The fixture immediately used its 60-second
service budget after asynchronous start, including the whole readiness wait.
The unknown reason for firmware-only output within that time is not explained
by this finding.

Implementer0 corrected only the setup call to
`machine.start(wait_for_boot: true)`, using the existing 900-second boot/shell
readiness budget before the separate 60-second service check. This changes
timeout classification and budget, not product behavior or guest settings.
Quick format/parse/full-render/Ruby syntax checks passed in
[the fixture receipt](generic-sysctl-i0-verification.md). The caused correction
belongs in the generic owner v2; affected independent review precedes
publication and any second focused attempt. A subsequent readiness failure
must be reported as a boot/shell failure, not as sysctl-service evidence.

## V2 baseline after the readiness correction

The exact `895870606` attempt started once at 10:41:03 UTC (12:41:03 CEST).
The fixture waited for guest readiness under its existing 900-second budget,
reached examples at 12:45:59 and completed native output at 12:47:40. Six of
eight examples passed; examples 7 and 8 failed because their expected-failing
custom completion check returned 0. The actual outer command exit receipt is
unavailable after the watcher CLI was interrupted; this is a monitoring gap,
not a claimed numeric exit code. Native result is `unexpected_failure` and
all runner/worker/QEMU processes ended. Full log and native artifacts are
retained under `generic-sysctl-focused-vm-895870606*` in this session.

The successful examples establish boot/application, unchanged-input retention,
dry/boot behavior, effective-target file application/precedence, source changes,
rename and removal/null for that snapshot. Shell evidence shows expected
values 7/9/11/12 and 111/112/113. The failed cases did not create an actual procps
error: pinned `--system` sets IgnoreError and ignores an absent sysctl key.
Implementer0 traced this and the existing numeric-handler EINVAL path in
[the failure-injection proof](generic-sysctl-failure-injection.md). V3 replaces
the unknown key with a nonnumeric value for a known benign numeric key; there
is no product parser or missing-key policy change.

The independent literal-path content bug was also reproduced on 895 and is
corrected separately within the same generic logical owner v3. Ordinary
text/store graphs are unchanged; the old VM fixture did not cover literal-path
same-name content edits. V3 still requires all-four-lane final review and a
new selected focused run before claiming its behavior verified.
