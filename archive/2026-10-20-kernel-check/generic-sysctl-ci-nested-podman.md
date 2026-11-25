# Nested Podman: local CI failure evidence

Read-only diagnosis of `upgrade/from-6.18-nested-podman` in CI `39767770407`,
head `846bb469505789ba0b2a405fa5905ba6d8253006`. Only this test's preserved
native logs were examined; no test, build, VM, remote query or Git mutation ran.

The direct network prerequisite failure is a DHCP-client sandbox permission
error on the pinned predecessor, before target activation. The logs establish
this boundary; they do not identify the exact policy or syscall responsible
for the permission error.

Artifact directory below `generic-sysctl-ci-39767770407-600s-failure-119793311317/`
is `artifacts/os-test-logs-39767770407-1-native/`
`os-test-upgrade__from-6.18-nested-podman-3db70126/`.
All line references below are within that directory.

| Time, 2026-10-22 CEST | Direct evidence |
| --- | --- |
| 15:23:40 | `test-runner.log:1`: script starts. |
| 15:24:29 | `machine-shell.log:104`: host connectivity probe returns HTTP 200; `:136` reports kernel `6.18.49`; `:145` and `:172` identify running system `/nix/store/h772xsck07kn6w9zyw32l6q9gs0xyfhq-vpsadminos-system-vpsadminos-26.05pre-git`. |
| 15:28:53–15:29:05 | `machine-shell.log:2297`: Debian `latest` container creation succeeds. |
| 15:29:13–15:29:17 | `machine-shell.log:2349`: container start succeeds; daemon later reports it RUNNING. |
| 15:29:18.319028 | `machine-failure-diagnostics.log:2054`: dhcpcd reports `ps_managersandbox: seccomp: Permission denied`. |
| 15:29:18.321715–18.461259 | Same file `:2056`: ifup fails to bring up eth0; `networking.service` exits 1 and fails. |
| 15:29:17–15:43:21 | `machine-shell.log:2360` through `:3860`: 126 online probes all return status 2. Each reports temporary DNS resolution failure, with curl/wget absent. |
| 15:44:17 | `test-runner.log:2-8`: script fails after 1237.2 seconds waiting for container `nestedpodman` to come online. |

The failure snapshot records `nestedpodman` running with init PID 5169
(`machine-failure-diagnostics.log:1799-1812`). Its eth0 is UP with only
link-local IPv6, no IPv4 address and no default route (`:1886-1910`). Its
resolver is `1.1.1.1` (`:1926`), `/etc/network/interfaces` configures DHCP on
eth0 (`:1955-1982`), and `/usr/sbin/dhcpcd` is installed (`:1985-2014`).
The image is Debian 13.7; package versions are ifupdown `0.8.44+deb13u1` and
dhcpcd-base `1:10.1.0-11+deb13u4`. The container's LXC error log is empty
(`:4285`), so it supplies no more specific denial explanation.

The observed sequence is DHCP sandbox denial → failed interface configuration
→ no guest IPv4/default route → repeated DNS-dependent readiness failure.
Missing curl/wget remove fallbacks; they are not the first network-start error.
Host connectivity succeeded earlier, which does not certify the container path.

## Exact source boundary and limits

At `846bb469505789ba0b2a405fa5905ba6d8253006`:

- `tests/suite/upgrade/from-6.18-nested-podman.nix:2` selects the inherited
  workload scenario. `from-6.18.nix:4-6` pins predecessor OS
  `3cb830e596a7fed900bec49f50c9b6cf51e76bb5`, kernel prefix 6.18.49 and its
  unstable configuration (kernel source `fbda79346b89b2d2486edd22e4bbbca0154d96b7`).
- `tests/suite/upgrade/common.nix:314-337` boots the predecessor's daemon,
  LXC, kernel, ZFS and policy. Only the test-shell transport follows current
  source. The current target is retained in `system.extraDependencies`, not
  activated by construction.
- `common.nix:1239-1246` creates/starts the container and calls
  `wait_until_container_online` before installing Podman or activating the
  target. The normal target activation occurs later (`:2047`).
- `osvm/lib/osvm/vpsadminos_machine.rb:124-152` tries ping, curl, wget and
  getent against `check-online.vpsadminos.org`, with a default 900-second
  overall deadline and 60-second probe limit. The final trace expires while
  reserving time for another complete probe. It is a readiness timeout, not
  an observed stuck osctl call.

The complete shell command log contains zero `switch-to-configuration` or
sysctl commands; the failure service listing contains no sysctl service.
Thus the incoming generic service was not executed in this failing scenario.
This conclusion rests on this run's source/runtime boundary, not a historical
failure comparison. It does not establish that every other CI failure is
independent or that the generic branch can merge without passing CI.

The exact denial mechanism remains unresolved: these artifacts do not capture
the failed syscall arguments, the relevant effective filter/credentials, or a
client stack. No claim is made about which component introduced it, whether it
is intermittent, or whether changing DNS, DHCP options or seccomp policy would
fix it. No repair or rerun is selected by this note.

SHA-256 of primary preserved logs:

```text
b930fadc0b9082b96a5a95ca475b9dd829b954ab495341c5e8565a335ab3d240  test-runner.log
dcfe64ff65e0d9f350c82cbef031653a800ddf3be439b082361890585e9124b2  machine-shell.log
5b8cf68a3fe7deacd93acad877f67dea824945fc411e3ccb5c3162bc52010f04  machine-failure-diagnostics.log
880f54f5219d373d8b7ba0f5cd77ba0cbe21ca4a47686a2fcab0ddcbe3d853d7  machine-console.log
```
