# Predecessor nested Podman: findings

Current repair-phase outcome: **original permission denial not reproduced** in
the separately selected VM2 diagnostic. PID164's NNP/filter entry both return0
at retained trace lines230/231; eight complete pairs succeed. A truncated trace
tail, ptrace/foreground service effects and unavailable original image prevent
causal exclusion or a justified product patch. See the source/log-supported
[VM2 findings](repair/podman/capture-2/findings.md) and
[repair brief](repair/podman/brief.md). Diagnostic fixture commit405a802 owns
retention improvements, not a DHCP/security-policy repair. No further run selected.

The following is the accepted **historical investigation-phase** record.
Owner: implementer1. Investigation only, at target
`846bb469505789ba0b2a405fa5905ba6d8253006`. Ready for lead reconciliation.
No application change, Git mutation, test, build, VM, rerun or lifecycle action
was performed. Source-session artifacts were read only. The current run was
not queried remotely. Documentation belongs here because these are incident
findings and proposals, with no accepted change to the product contract.

## Conclusion

Keep the nested Podman upgrade case and revise its prerequisite diagnostics and
provenance. This attempt fails when the predecessor's Debian DHCP client enters
its sandbox. Interface configuration fails, the guest has no IPv4/default route,
and 126 readiness probes fail before a 900-second timeout. Neither Podman
installation nor target activation is reached. The incoming generic sysctl
service cannot cause this executed failure path; this excludes no other test.

Matching Debian package source narrows the error to sandbox entry: either
`prctl(PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0)` or the following
`prctl(PR_SET_SECCOMP, SECCOMP_MODE_FILTER, ...)` returned failure. It does not
identify a later DHCP syscall denied by dhcpcd's installed filter. The exact
failed call, effective credentials/filter, runtime kernel configuration and
introducer remain unknown. In particular, the predecessor kernel contains
additional authority-guard EACCES paths, so the usual missing-capability
explanation alone is insufficient.

## What the test protects

A user can run Podman application containers inside a vpsAdminOS system
container, comparable to running applications inside their VPS. Replacing host
management userspace must preserve that already-running nested workload,
its data and its ability to create another constrained application container.
A fresh Podman test cannot prove survival of an old daemon's live workload.

The [upgrade contract](evidence/podman/source/target/docs/os/testing.md)
(“Userspace upgrades between versions”) requires a pinned predecessor and a
current target, while retaining the boot kernel and boot identity. It permits
retiring unsupported predecessor paths, rather than silently repinning a case.
[Updates guidance](evidence/podman/source/target/docs/os/updates.md) likewise
distinguishes userspace activation from reboot/kernel replacement.

The exact [fixture](evidence/podman/source/target/tests/suite/upgrade/common.nix)
creates the system container on the old OS, installs Podman, checks overlay
storage, pulls Alpine, starts an application writing `inherited-podman-data`,
and records outer init PID/birth time and nested container ID/PID
(:1233–1273). After activation it checks the marker, those identities, Podman
operation and a new container's 64 MiB memory limit (:2284–2294).

Both nested launches use `--network none`. Thus this case protects nested
process/data/storage/cgroup continuity, not continuity of a Podman bridge,
NAT, nested DNS or application HTTP connections. Its Debian network is a
setup prerequisite for APT and image pulls. The current attempt establishes
no result for the nested assertions. The inner PID is compared without its
birth time; checking that as well would strengthen restart/PID-reuse detection.

## Observed failure and identities

Primary original artifacts are under
`../2026-10-20-kernel-check/generic-sysctl-ci-39767770407-600s-failure-119793311317/artifacts/os-test-logs-39767770407-1-native/os-test-upgrade__from-6.18-nested-podman-3db70126/`.
References below are to files in that directory. Compact numbered excerpts and
SHA-256 identities are preserved in [current-log-excerpts.txt](evidence/podman/current-log-excerpts.txt)
and [current-observation.json](evidence/podman/current-observation.json).

| Identity | Evidence |
| --- | --- |
| Predecessor OS | `3cb830e596a7fed900bec49f50c9b6cf51e76bb5`, selected by [from-6.18.nix:4](evidence/podman/source/target/tests/suite/upgrade/from-6.18.nix) |
| Running kernel | `6.18.49`, `machine-shell.log:136`; predecessor source `fbda79346b89b2d2486edd22e4bbbca0154d96b7` in [available-kernels.nix:10](evidence/podman/source/predecessor/os/packages/linux/available-kernels.nix) |
| Running system | `/nix/store/h772xsck07kn6w9zyw32l6q9gs0xyfhq-vpsadminos-system-vpsadminos-26.05pre-git`, shell :145/:172 |
| LXC | package `6.0.6`, source `d510d66005fb974b19425fb6a12b87bbde8ae36c`, [package definition:27](evidence/podman/source/predecessor/os/packages/lxc/default.nix); runtime store `/nix/store/y2w16d8k1pgpnf14dp87fc05xv18vm46-lxc-6.0.6`, diagnostics :1209 |
| Guest | Debian `13.7`, diagnostics :1913–1923; `ifupdown 0.8.44+deb13u1`, :1984–1994; `dhcpcd-base 1:10.1.0-11+deb13u4`, :2006–2019 |
| Container image | requested `debian/latest`, shell :2297; resolved major version 13, diagnostics :1805; original archive digest/build timestamp unavailable |

Times in this table are UTC on 2026-10-22; primary logs show CEST (+02:00).

| Phase | Direct observation |
| --- | --- |
| 13:23:40 | Script begins, `test-runner.log:1`. |
| 13:24:29 | Earlier host HTTP probe succeeds, shell :104. This checks host connectivity, not the later Debian guest path. |
| 13:28:53–13:29:17 | Debian creation/start commands succeed, shell :2296–2356. Running does not mean DHCP is ready. |
| 13:29:18.319028 | `ps_managersandbox: seccomp: Permission denied`, diagnostics :2054. |
| 13:29:18.321715–.461259 | ifup fails eth0 and `networking.service` fails with exit 1, diagnostics :2056–2063. |
| 13:29:17–13:43:21 | All 126 online probes exit 2, shell :2360–3868; DNS fails and curl/wget are absent. |
| 13:44:17 | Readiness deadline expires; total script elapsed 1237.2 s, runner :2–8. |

The failure snapshot shows init PID 5169 still running, eth0 UP/LOWER_UP,
only IPv6 link-local on eth0, no IPv4/default route, resolver `1.1.1.1`, and
generated `iface eth0 inet dhcp` (diagnostics :1805, :1886–1927, :1951–1975).
The LXC container log is empty (:4285); absence of a message is not absence of
a policy rejection. This establishes a DHCP-start prerequisite failure with
network consequences, not a DNS-only outage. Installing curl, changing the
resolver or assigning a static address would not diagnose the sandbox failure.

## Source mechanism and causal limits

The target [wrapper](evidence/podman/source/target/tests/suite/upgrade/from-6.18-nested-podman.nix)
selects `nestedPodman = true`. `common.nix:308–330,3325–3328` uses predecessor
dependencies and configuration and replaces only its test-shell transport.
The current generation is an extra dependency, not the running OS.
`common.nix:1239–1246` starts Debian and waits online; APT installation follows
(:1250–1251), with ordinary activation later (:2047). That source ordering,
the predecessor runtime identity and the complete command log ending at this
wait establish nonexecution of the incoming service here. A negative text
search alone would be insufficient.

The fixture uses `osctl ct netif new bridge --link lxcbr0` and adds `/dev/net/tun`
(:1241–1243). [Bridged veth documentation](evidence/podman/source/predecessor/docs/networking/veth-bridge.md)
and [networking guidance](evidence/podman/source/predecessor/docs/user-guide/networking.md)
specify DHCP on this bridge. The predecessor test configuration enables lxcbr;
[dnsmasq configuration](evidence/podman/source/predecessor/os/modules/services/networking/lxcbr-dnsmasq.nix)
offers `192.168.1.100–200/24` with gateway `192.168.1.1`. Source establishes
the intended server, not proof of DHCP packet exchange. Debian's configurator
selects ifupdown; its [bridge template](evidence/podman/source/predecessor/osctld/templates/dist_config/network/ifupdown/bridge.erb)
emits `inet dhcp`, matching the recorded file.

Exact Debian [ifupdown source](https://sources.debian.org/src/ifupdown/0.8.44%2Bdeb13u1/inet.defn/#L98)
prefers dhclient, then udhcpc, then dhcpcd. Only dhcpcd is installed in the
snapshot. The package's [networking unit](evidence/podman/external/ifupdown/debian/networking.service)
runs `/usr/sbin/ifup -a --read-environment`. This connects the observed service
failure to the selected client without assuming a standalone dhcpcd service.

Exact dhcpcd [package rules](evidence/podman/external/debian/rules) select
`--privsepuser=dhcpcd` and do not disable seccomp.
[privsep.c:633–682](https://sources.debian.org/src/dhcpcd/1%3A10.1.0-11%2Bdeb13u4/src/privsep.c/#L633)
attempts chroot, group/UID changes and resource limits through `ps_dropprivs`
before calling `ps_entersandbox`; its Linux branch calls `ps_seccomp_enter`.
Some launcher EPERM cases are tolerated, so source does not prove the final
effective UID or capabilities. [privsep-linux.c:509–525](https://sources.debian.org/src/dhcpcd/1%3A10.1.0-11%2Bdeb13u4/src/privsep-linux.c/#L509)
short-circuits the two prctl calls described above. `EINVAL` becomes `ENOSYS`,
which the manager treats as unavailable; the observed permission error follows
the fatal path. Debian's complete patch series was checked: it does not change
these entry calls. Its relevant filter patch adds `rt_sigprocmask` to the
allowlist. A later unexpected syscall normally invokes `SECCOMP_RET_KILL`
(:148–152), a different mechanism from this logged setup error.

Predecessor [generated LXC configuration](evidence/podman/source/predecessor/osctld/templates/ct/config.erb)
includes distribution defaults, explicit UID/GID maps and a seccomp profile
(:1–30); `container.rb:1255–1256` defaults to `/etc/lxc/config/common.seccomp`.
The exact [LXC profile](https://github.com/vpsfreecz/lxc/blob/d510d66005fb974b19425fb6a12b87bbde8ae36c/config/templates/common.seccomp)
denies selected module/kexec/file-handle calls with errno 1 (EPERM) and rejects
forced umount. It does not list prctl. The included
[userns defaults](evidence/podman/external/lxc/userns.conf.in) reset the general
capability drop list for user namespaces. Those defaults do not establish a
DHCP manager's later capabilities, all effective stacked filters or any
guest systemd drop-ins. No effective generated nestedpodman LXC config,
per-process `NoNewPrivs`/`Seccomp` state, filter program or credentials were
retained. `/dev/net/tun` permission does not resolve prctl authorization.

The exact boot-kernel source has several source-compatible EACCES routes:

| Candidate | Exact source and discriminating observation |
| --- | --- |
| Denied NNP transition | [kernel/sys.c:2711–2721](https://github.com/vpsfreecz/linux/blob/fbda79346b89b2d2486edd22e4bbbca0154d96b7/kernel/sys.c#L2711) returns EACCES for `AUTH_GUARD_MUTATION_REJECTED`. Trace must first identify whether NNP itself failed. |
| Ordinary filter-install precondition | [kernel/seccomp.c:937–945](https://github.com/vpsfreecz/linux/blob/fbda79346b89b2d2486edd22e4bbbca0154d96b7/kernel/seccomp.c#L937) requires NNP or CAP_SYS_ADMIN in the current user namespace. If NNP succeeded and remains 1, simple capability loss does not explain this check. |
| Guarded filter transition | [kernel/seccomp.c:2284–2329](https://github.com/vpsfreecz/linux/blob/fbda79346b89b2d2486edd22e4bbbca0154d96b7/kernel/seccomp.c#L2284) has separate EACCES branches at transition begin/expected-state validation. A failing install with NNP=1 needs these and other policy paths investigated. |
| Earlier filter or LSM | An inherited filter can reject the setup prctl before its handler; [sys.c:2546–2548](https://github.com/vpsfreecz/linux/blob/fbda79346b89b2d2486edd22e4bbbca0154d96b7/kernel/sys.c#L2546) also consults the LSM hook. An EPERM-returning outer rule differs from the recorded EACCES wording. Arbitrary effective ERRNO rules must be measured, not inferred from the default profile. |

[Selected kernel configuration](evidence/podman/source/predecessor/os/packages/linux/common-config.nix)
(:43–46,459–461) requests authority guards on 6.18. The boot binary's actual
configuration/state and a corresponding rejection record are absent. This is
a concrete candidate, not a proven guard bug or introducer. The exact kernel
object was unavailable locally; immutable official source was read over HTTPS
without fetching or mutating the Git repository. Source URL/time/hash receipts
are in [external/manifest.json](evidence/podman/external/manifest.json).

## History, usefulness and cost

The collector froze the [latest 15 completed runs](evidence/history/sample-lock.json)
before classifying signatures; current run 39767770407 is context only.
Implementer3 owns [recurrence.tsv](recurrence.tsv). Its 15 unique runs contain
seven executed-pass runs, five cancelled runs, one prebuild failure and two
unexecuted harness failures. There are eight executed-pass observations because
one benchmark has two legs. Zero of those eight available executed observations
reproduces the exact sandbox-denial chain. Fifteen is not the executed-test
denominator, and the current failure is outside this historical sample.

Five native artifact passes were independently inspected locally:

| Run | Script elapsed seconds | Evidence |
| --- | --- | --- |
| [39600028637](https://github.com/vpsfreecz/vpsadminos/actions/runs/39600028637) | 2601.05 | artifact 12359659166 |
| [39414347376](https://github.com/vpsfreecz/vpsadminos/actions/runs/39414347376) | 2628.42 | artifact 12280302845 |
| [39413777406](https://github.com/vpsfreecz/vpsadminos/actions/runs/39413777406) | 2975.38 | artifact 12274604662 |
| [39358414083](https://github.com/vpsfreecz/vpsadminos/actions/runs/39358414083) | 2552.46 | artifact 12242049622 |
| [39309610523](https://github.com/vpsfreecz/vpsadminos/actions/runs/39309610523) | 3640.52 | artifact 12233118146 |

[historical-pass-inspection.json](evidence/podman/historical-pass-inspection.json)
binds those rows to immutable collector paths and exact log lines. Each boots
6.18.49, requests Debian/latest, briefly fails its first DNS probe, then
succeeds on its second probe and installs Podman `5.4.2+ds1-2+b2` from trixie.
Their logs lack DHCP package version, point release and image hash, so they
cannot establish that the failing image passed previously. Brief startup DNS
failure in a passing case is not the sustained sandbox-denial chain.

Collector job logs also establish native pass 39381114351 (4306.23 s) and
benchmark 39305352549 legs A/B (3367.21/3197.03 s). The latter tested product
checkout `a2ccd72d08dc67f678d7f115a92ed5eeca50c1a1`, distinct from workflow
head `295b814a`; benchmark legs are not independent runs. Full identities and
categories remain authoritative in the collector's table.

The five artifact script durations span 42.5–60.7 minutes, excluding later
cleanup. The three job-log observations instead report whole-test durations
of 53.3–71.8 minutes, including runner preparation/cleanup; these measures
must remain separate. Both include substantial shared upgrade work and do not
measure a Podman-only increment. This failure consumes 20.6 minutes of script
time, including a 15-minute
readiness wait and 126 repetitive errors after DHCP failed immediately.
Maintenance dependencies include a historical OS closure, a moving Debian
image, APT repositories, Podman packages, an Alpine tag and registry access.
There is no measured long-term failure rate or basis to call the test flaky.

The test has valuable distinct coverage, and the failure exposes a real
prerequisite incompatibility rather than an obsolete assertion. Its present
diagnostics attribute that failure poorly and consume excessive time without
reaching the central upgrade contract. Removal is unjustified without evidence
that this predecessor path is unsupported or its continuity contract redundant.

## Prioritized proposals and acceptance

1. **Diagnose the entry error once.** Use the bounded, predecessor-only
   [trace proposal](evidence/podman/diagnostic-proposal.md). Capture the failed
   prctl, arguments/errno and effective state before selecting a repair. No
   blanket seccomp disablement, privilege grant, static-IP substitution or
   client replacement is supported by present evidence.
2. **Report failing readiness layers promptly.** Capture link, address, route,
   resolver, guest service journal and package identities at the first persistent
   failure. After startup grace, a terminal networking-service failure should
   explain a failed prerequisite directly. Preserve bounded retries for normal
   DHCP/DNS startup, and distinguish external endpoint errors. Do not mask DHCP
   failure or turn the test green after an unexplained fallback.
3. **Record immutable setup identities.** Keep this supported predecessor pin;
   record resolved image vendor/variant/architecture/version, archive digest,
   build metadata and package manifest, plus Podman/image digests. Consider a
   reproducible continuity fixture alongside separately reported latest-image
   compatibility coverage. [Repository documentation](evidence/podman/source/predecessor/docs/container-images/repositories.md)
   permits image replacement/cache refresh, while [Debian image scripts](evidence/podman/source/predecessor/image-scripts/include/debian.sh)
   bootstrap and upgrade from live repositories. Pinning the OS or major Debian
   release alone cannot freeze these inputs. Do not silently replace the old
   compatibility boundary to hide the failure.
4. **Repair the demonstrated owner and preserve nested assertions.** A proved
   daemon/image-client incompatibility needs a supported version policy or a
   compatible fix; a proved kernel guard defect needs a kernel repair and
   predecessor/release handling. Changing only target userspace cannot fix
   this preactivation execution. Any later rollout must specify mixed-version
   support, ordering and rollback separately; no rollout is selected here.

Regression acceptance requires the supported predecessor/image tuple to acquire
IPv4/default route via DHCP with confinement retained, then separately prove
DNS and required endpoint access. Trace must show both sandbox-entry calls
succeed, with expected NNP/filter state; intended prohibited operations must
remain prohibited. Continue through Podman installation, overlay assertion,
old nested workload/data and outer identity retention across activation, and
new 64 MiB-constrained workload creation. Retain unchanged kernel/boot identity.
Do not label successful networking alone nested-workload continuity, or add a
nested-network claim without an explicit new networked workload assertion.
Keep failure cases that distinguish permanent DHCP setup rejection, ordinary
startup delay, DNS outage and external mirror/registry failure.

Read-only checks completed: source/log line consistency, source/download hashes,
126/126 failed probe count, zero activation/install commands, phase ordering,
five artifact pass inspections and collector reconciliation. No product check
or independent change review applies to this investigation-only deliverable.
The lead owns state/portal updates and commits. Session remains open:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-ci-failure-analysis/>.
