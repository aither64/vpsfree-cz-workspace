# Completed native openSUSE image cases

Implementer1 audited only the frozen `session/native-completed-16.0/` and
`session/native-completed-16.1/` evidence supplied by the lead. Both normal
image cases pass at source `742eb30cb1a8b6766c85e915d26b0400e38244b1`.
No original Lua `rpm.exec`/`rpm.execute`, cpio/unpack error, failed RPM scriptlet
or failed post-transaction script appears in either complete build transcript.
The logs contain the diagnostics described below; this is not a warning-free
build claim. No live batch files, guest, source or Git operations were used.
The later 15.6/Tumbleweed frozen-only audit below completes normal coverage of
all four images; parallel candidate export logs were not read or overlapped.

## Native completion and observed packages

| Evidence | Leap 16.0 | Leap 16.1 |
| --- | --- | --- |
| Normal image assertions | 15 run, 15 succeeded, 0 failed | 15 run, 15 succeeded, 0 failed |
| Native result | `expected_success` | `expected_success` |
| `osctl-image test` status | 0, 824.95 s | 0, 793.8 s |
| Package transaction | 207 done, error 0, skipped 0 | 241 done, error 0, skipped 0 |
| Target `udev`, `systemd`, `libudev1`, `libsystemd0` | `257.13-160000.4.1.x86_64` | `257.13-160100.3.5.x86_64` |
| Target RPM package | `4.20.1-160000.4.1.x86_64` | `4.20.1-160100.3.2.x86_64` |
| Target release package | `Leap-release-16.0+leap-lp160.264.1.x86_64` | `Leap_immutable-release-16.1-lp161.12.1.x86_64` |
| Native default script finished | 2026-11-03 22:32:26 +0100 | 2026-11-03 22:31:49 +0100 |
| QEMU exit | 0 at 22:33:07 +0100 | 0 at 22:32:20 +0100 |

Versions above come from the actual target installation records, not a later
`rpm -q` query or the builder's RPM executable. Both logs identify shared builder
`opensuse-leap`, container `builder-98c1959d`; they do not contain its actual
`/etc/os-release` or `rpm --version` output. Those observations remain for the
already prepared retained-builder export if the builder survives. Each trace
shows the correct release repository, explicit `udev` in `EXTRAPKGS` and
`zypper install --no-recommends`, successful proc/sys/dev mounts, bootstrap
status 0 and successful cleanup. Target udev installation ends `done]` without
the earlier diagnostic runtime reload/Lua trigger failure.

## Diagnostics retained and interpreted

- Initial `osctld.sock`/pool-not-found responses belong to native pool readiness
  polling; both progress through importing to active before the build.
- Zypper announces enabled automatic GPG-key import and excludes not-yet-downloaded
  packages from its preliminary file-conflict check. Both repositories have GPG
  checking enabled and metadata reports signed validation. The printed additional
  key inventory includes expired unrelated keys; no signature failure is reported.
- Permission-check output says `failed to obtain ACL: Operation not supported`
  (16.0 shell lines 1361–1685; 16.1 lines 1471–1829). Each affected installation
  completes. Missing file capabilities are set, and the later exporter explicitly
  finds `clockdiff`, `newuidmap` and `newgidmap` capabilities. This does not prove
  POSIX ACL support; it distinguishes these permission-check diagnostics from
  extraction or scriptlet failure.
- `pam-config` prints `ERROR: module /lib64/security/pam_pwquality.so is not
  installed.` at 16.0 line 1471 / 16.1 line 1593. Its following generated
  password configuration disables `pam_pwquality` and enables `pam_unix`;
  installation and posttrans complete. Console login, password and SSH tests
  subsequently pass. This evidence does not claim password-quality enforcement.
- Both scripts warn that nobody UID 65534 exceeds `SYS_UID_MAX` 499, then finish
  that account installation. Wicked's `Running in chroot, ignoring command
  'daemon-reload'` describes installation into the unbooted target.
- After the successful RPM transaction, `/tmp/configure.sh` prints
  `sed: can't read /etc/systemd/system.conf: No such file or directory`
  (16.0 line 1974 / 16.1 line 2169), then configuration/build return 0.
  The bounded source followup below explains its intended setting and baseline
  relationship. It is outside the RPM transaction; no failed RPM scriptlet or
  Lua/cpio failure is being waived.
- Host console messages concern keyboard ioctl, initial hostname resolution
  fallback and NTP rate limiting followed by successful clock setup. Virtiofsd
  records its FD limit and uid/gid/file-handle restrictions, disables file handles,
  serves requests and disconnects normally. These are fixture messages, not target
  package-install errors.

## Missing system.conf: bounded source followup

Exact source 742, `image-scripts/include/opensuse.sh:69`, appends this command
inside `configure-opensuse`:

```sh
sed -i 's/#DefaultTimeoutStartSec=90s/DefaultTimeoutStartSec=900s/' /etc/systemd/system.conf
```

Its purpose is to raise the manager's default unit start timeout from 90 seconds
to 900 seconds (15 minutes), where an individual unit does not set its own
timeout. It assumes an existing file containing the exact commented default.
With no `/etc/systemd/system.conf`, sed fails to open the target and applies no
setting. The appended configuration has no `set -e`; subsequent commands create
RPM macros, the journal directory and the existing network udev trigger override.
The later commands complete, so the generated script can return 0 despite this
failed intermediate sed command. `common.sh:102–139` appends the payload and
propagates the generated script's final status, rather than each command's status.

The command and the surrounding configuration functions are unchanged between
branch baseline `dd188397abe37d0bc33f4c5dfb3605206ce5e326` and final
`742eb30cb1a8b6766c85e915d26b0400e38244b1`. The complete diff of `opensuse.sh`,
`common.sh` and `systemd.sh` contains only the explicit udev package/comment in
`opensuse.sh`. Thus this is a preexisting ineffective configuration step in the
shared helper, exposed in both successful rebuilt Leap logs, not a newly added
timeout change or a failure of the udev installation.

Systemd v257's [configuration manual source](https://raw.githubusercontent.com/systemd/systemd/v257/man/systemd-system.conf.xml)
recognizes main configuration in `/etc`, `/run` and `/usr/lib/systemd/system.conf`,
with corresponding `system.conf.d` directories. Its
[configuration template](https://raw.githubusercontent.com/systemd/systemd/v257/src/core/system.conf.in)
explicitly supports vendor configuration in `/usr` and recommends local drop-ins
under `/etc/systemd/system.conf.d`. Absence of the `/etc` main file is therefore
valid systemd configuration layout, while this helper's in-place edit assumes
the older location. The upstream v257
[build option](https://raw.githubusercontent.com/systemd/systemd/v257/meson_options.txt)
defaults the system unit start/stop timeout to 90 seconds. These sources establish
supported locations and the upstream default; they do not prove the exact
openSUSE RPM's build override, installed vendor file/drop-ins or effective
`DefaultTimeoutStartUSec`. The attempted Leap packaging-source lookup was
unavailable (public OBS package path returned 404), and no guest query was run.
The evidence therefore supports **no applied 900-second override from this sed**,
not an asserted measured target timeout of 90 seconds.

Acceptance consequence: nonblocking for the assigned builder/release and device
unit milestones, with the limit retained. Those changes promise working image
bootstrap and actual eth0/dummy0 activation; they do not introduce a new global
15-minute startup-timeout guarantee. The original device test has its own
60-second observation waits; a longer manager start timeout cannot replace the
missing udev daemon/events/database. Normal 16.0/16.1 checks passed with this
warning. These results do not validate services needing the intended extended
timeout, and no claim that the 900-second policy is effective should accompany
the final package. No source fix, candidate-input change or additional runtime
check was made for this bounded followup.

## Exact successful primary inputs

All four frozen JSON copies match the lead's expected SHA256 and native runner
output paths. All set `expectFailure = false`, one attempt, four CPUs, 8192 MiB,
and mount clean source `/nix/store/m1n49nc1qdf1f3j298zcmjjb5ni43iag-source`.
The embedded test command names exact revision `742eb30cb1a8b6766c85e915d26b0400e38244b1`
and its respective image. These identities must match before candidate export.

| Case | Native JSON path | SHA256 |
| --- | --- | --- |
| 15.6 | `/nix/store/fbn2vwka2qdnbyrkqsp3jpqqgmjjhgsq-os-test-image-scripts-test-opensuse-leap-15.6.json` | `4e08e5486ab3df102f681a001158e6245e7541bcf058fababb2ea2d55af715f5` |
| 16.0 | `/nix/store/dw0qknr27z2gyqv4k7b6glrhy988dk8g-os-test-image-scripts-test-opensuse-leap-16.0.json` | `07052fb31996fd48b84c4e9f48ab9e9b7c60c9569e2d6cc00a9fd6ae9099f8fa` |
| 16.1 | `/nix/store/j50dk28jfqwz1nvlmrm8s0nbg3jln0i0-os-test-image-scripts-test-opensuse-leap-16.1.json` | `aadb815caca564460f176718719ed8eba3608b0b059d61c7f6dcb7389144aae9` |
| Tumbleweed | `/nix/store/a6z3vcbfx1j1qycms0rzk1bmllqsbbj7-os-test-image-scripts-test-opensuse-tumbleweed.json` | `cc959e564a7119d3a8360b25e5d3a393a4007a02aadd2231a6a2f03f496c4942` |

Common actual VM paths: kernel
`/nix/store/b043pwyanxjfz22hbiibv5wipqqcl932-linux-6.12.113/bzImage`, initrd
`/nix/store/p1a2p526kvg1zsz7j5wwmg68i9m1z2zm-initrd/initrd`, system
`/nix/store/hq96hymxp4wp8j9bhcy51lp6j5nffnpf-vpsadminos-system-vpsadminos-26.05pre-git`,
squashfs `/nix/store/97xwp1v7pc4xxdjv6xghdk5g0iyvfdh0-squashfs.img`.

## Final two-case audit: Leap 15.6 and Tumbleweed

Inputs were only `session/final-images-native-742-result.md` and frozen
`session/native-completed-{15.6,tumbleweed}/`. The complete bootstrap,
installation and posttrans output has no original Lua API failure, cpio/unpack
error or failed/unexplained RPM scriptlet. Routine successful package progress
was collapsed during reading; scriptlet output and diagnostics were retained.
No test, VM, server, probe, source or Git action was performed.

| Observed evidence | Leap 15.6 | Tumbleweed |
| --- | --- | --- |
| Normal assertions / native result | 15/15, `expected_success` | 15/15, `expected_success` |
| `osctl-image test` | status 0, 878.42 s | status 0, 774.1 s |
| RPM transaction | 205 done, error 0, skipped 0 | 206 done, error 0, skipped 0 |
| Target udev/systemd/libudev1/libsystemd0 | `254.10-150600.2.3.x86_64` | `261.4-1.1.x86_64` |
| Target RPM package | `4.14.3-150400.59.13.1.x86_64` | `4.20.1-11.1.x86_64` |
| Target release package | `openSUSE-release-15.6-lp156.417.4.1.x86_64` | `openSUSE-release-20261102-4384.1.x86_64` |
| Builder name / container | `opensuse-leap` / `builder-98c1959d` | `opensuse-tumbleweed` / `builder-c5d5c229` |
| Default script finished | 22:53:22 +0100, 1184.54 s | 22:50:31 +0100, 1037.08 s |
| QEMU exit | 0 at 22:53:57 +0100 | 0 at 22:51:02 +0100 |

Versions are actual target installation records, not builder RPM/OS queries or
archive identities. Both traces show explicit udev installation, successful
proc/sys/dev mounts, bootstrap status 0 and cleanup. Additional diagnostics:

- Leap 15.6 refreshes its repositories, then reports update metadata expired
  since `2026-10-14 00:33:04 CEST` (shell 452–457). Passing against the served
  set does not establish current upstream metadata/support. Its `clockdiff`
  permission entry is missing (1383); account operations warn about unavailable
  `/usr/sbin/nologin` (1545/1574) before util-linux installation (1600), then finish.
  No final executable-path query is present. Kbd/udev posttrans explicitly skip
  initrd regeneration because dracut is absent (1711–1715), consistent with a
  container using its host kernel. `rpmdb --rebuilddb` reports selecting ndb for
  the existing NDB database instead of bdb (1767), completes, and the packages
  test passes; no database-format failure is reported.
- Tumbleweed's ACL-read diagnostics finish normally; capabilities are set and
  found by the exporter. Missing `pam_pwquality` (1468) is followed by that module
  disabled / `pam_unix` enabled, complete install/posttrans and passing
  login/password/SSH tests. Nobody UID and chroot reload notices finish normally.
- Both repeat the accepted preexisting missing `system.conf` warning (15.6 1771,
  Tumbleweed 1977). No source change or effective 900-second timeout claim.
  Fixture startup/virtiofs fallbacks are as described above and close normally.

Tumbleweed console line 126 records:

```text
[  732.301151] [ test-4a-4351 ] systemd-journald[30]: Failed to send stream file descriptor to service manager: Connection refused
```

This is a container journald runtime descriptor handoff refused by its manager
endpoint, outside package installation. Bootstrap/export had finished before
the disposable-container tests. The abbreviated `test-4a` prefix is consistent
with `test-4af7c259` for `passwd_started` (shell 2027–2030), which passes and then
cleans up. This association is an inference: the frozen console lacks a full
container ID, precise wall-clock timestamp and manager/socket journal context
to prove a specific teardown race. All 15 assertions and native shutdown pass;
no repeated failure is recorded. Retain this nonfatal runtime warning and its
limited attribution, without calling the run warning-free or inventing a new
bootstrap/udev/kernel defect. No live export logs were read.

## Frozen evidence integrity and remaining scope

Each directory retains the complete shell, console, runner, machine/virtiofs logs,
native result and primary JSON. SHA256 values for the principal transcripts:

| File beneath frozen case directory | 16.0 SHA256 | 16.1 SHA256 |
| --- | --- | --- |
| `machine-shell.log` | `7ad56467656cc906236260c85379a7c08240d1f509271fbdc99e032dff1d9fd7` | `ef6cafb627c4038a0f3e3b2b527ea721d781756add098be2156b08da6a95b281` |
| `machine-console.log` | `d0be3282f5f50609e931191d44651424274da74922f4dd9538ab1882e611fddf` | `800a30625ee062008afb22f53606d3678ba8c728e9c7ee340e9304bf5ecdc1ce` |
| `test-runner.log` | `97d711121a5a62d43e4b95615689c08d4400d4ea041cf89f2bb76e11d722ad23` | `b8eb55fdcee44c8b10458d7d3af01f78a287abc99a67e2cbe3e5ac5d8ba2f6bd` |

Additional frozen transcript SHA256 values:

| File | Leap 15.6 | Tumbleweed |
| --- | --- | --- |
| `machine-shell.log` | `5f1d4269bae0ba349d1d1243bc8aae0a07902f852b214aac23f6f18b33f4d14c` | `e65a2e8612db58a28fa2692d8c56b508cf422d5eea530c76f3cfca8cdb1d308e` |
| `machine-console.log` | `6027322c51f58187bc72b3485099dc03766cd663656d602761027af61fa9c300` | `93f72a8af3587a18587c403a82c77188a6682137fe6f06e5a7555c9df451d0c8` |
| `test-runner.log` | `84537c2e82da7cc1f8061614426d3f5df1fa4a7fa9ce4d414558b3b1f947891c` | `9986804f4670f9f40d887a2f5025018370e515e453f758255533e9d8593aee0f` |

Normal image coverage for all four cases is accepted with the documented
diagnostics. The [native batch](session/final-images-native-742-result.md) exits
0: four passes, no failed/expected-failure cases, retries or cancellation.
Archive hashes, archive release metadata, retained builder runtime identity,
four original device-unit assertion completions and the five focused 16.1 cases
remain pending [candidate execution](final-candidate-checks-742eb30cb.md).
Neither fixed Ruby candidate input was changed. Lead retains live batch ownership
and final readiness/integration decisions. This receipt makes no publication or
merge claim.
