# One predecessor-only sandbox-entry trace — proposal, not executed

Purpose: distinguish the two prctl failures and their credential/filter context
without installing Podman or activating the target. One disposable predecessor
`3cb830e596a7fed900bec49f50c9b6cf51e76bb5`, kernel `6.18.49`, one Debian
system container, one network startup. A fresh `latest` image is not an exact
reproduction unless the recorded failing archive is recovered and verified.
The original archive digest is currently missing; label a newly captured image
a new sample, rather than inventing equivalence.

No commands below were run. Tool staging, a disposable runner and this diagnostic
need separate lead/user selection. Prepare instrumentation offline; no APT
installation, target closure activation, local kernel build or security-policy
change is part of the diagnostic. Stop at first permanent error or 60 seconds
after network startup. A successful startup is a bounded non-reproduction,
not permission to retry until failure.

## Identities and setup

Before starting, retain boot/current-system paths, boot ID, kernel command line,
`uname -a`, exact kernel and LXC store paths/hashes, actual kernel `.config`
(including AUTH_GUARD/SECCOMP), source/input receipts and tracer version/hash.
Preserve the image archive/hash, resolved repository metadata and package
manifest. Retain guest `/etc/os-release`, dhcpcd binary hash/package version,
`/etc/dhcpcd.conf`, `/etc/network/interfaces*`, `/etc/default/networking`,
`systemctl cat networking.service`, and all relevant unit/drop-ins.

Use the source fixture's exact container setup, stopping before its wait/APT:

```sh
osctl ct new --distribution debian --version latest nestedpodman
osctl ct unset start-menu nestedpodman
osctl ct netif new bridge --link lxcbr0 nestedpodman eth0
osctl ct devices add -p nestedpodman char 10 200 rwm /dev/net/tun
osctl ct set dns-resolver nestedpodman 1.1.1.1
```

Image selection above is acceptable only with the provenance qualification
stated at the top. Do not fetch a moving image and call it the incident image.
Before the first start, save `osctl --json ct show nestedpodman` and the generated
LXC config. The config path comes from exported `lxc_dir` plus `/config`, not
a guessed storage path. Resolve every `lxc.include`, `lxc.seccomp.profile`,
raw config and guest systemd filter/capability setting; preserve bytes/hashes
and UID/GID maps. Do not infer effective filters from profile names alone.

## Single bounded trace

Instrument the **networking.service launch**, retaining its original environment
and unit restrictions, rather than invoking an unrelated interactive DHCP client.
The recorded package unit uses `/usr/sbin/ifup -a --read-environment` followed
by a conditional hotplug command. Verify the actual unit before preparing a
temporary disposable-only ExecStart wrapper. Preserve the second ExecStart.

The exact syscall-trace invocation for that first ExecStart is:

```sh
/diagnostic/strace -ff -ttt -T -s 256 -v -yy \
  -o /run/podman-diagnostic/ifup.trace \
  -e trace=%process,%creds,prctl,seccomp,chroot,chdir,setrlimit,prlimit64 \
  /usr/sbin/ifup -a --read-environment
```

`/diagnostic/strace` denotes a pre-staged, hashed compatible binary, not an
existing tool assertion. Retain exit status and all per-process outputs. Do
not use syscall injection, seccomp-bpf tracing acceleration, `--noprivsep`,
debug builds of dhcpcd or a relaxed LXC/systemd profile. Record tracing as an
instrumentation difference; a ptrace-sensitive guard may behave differently.

At the wrapper entry capture `/proc/self/status`, UID/GID maps and namespace
links. Trace successful/failed setgroups/setgid/setuid/capability transitions
for each descendant. To claim the **effective state at the failing prctl**,
prepare a syscall-stop-capable collector that records, before resuming that
call, the exact TID/birth identity, `/proc/<tid>/status` fields `Uid`, `Gid`,
`Groups`, `CapInh`, `CapPrm`, `CapEff`, `CapBnd`, `CapAmb`, `NoNewPrivs`,
`Seccomp`, `Seccomp_filters`, namespace identities and parent lineage.
This requires a tracer extension or equivalent debugger setup prepared before
the one attempt; plain strace does not supply these snapshots automatically.
Do not attach two ptrace owners simultaneously. If this extension is not
prepared, report the simpler trace's effective-state gap rather than claiming
it resolved that portion of the mechanism. Preserve inherited filter programs
through a permitted tracer interface when available; mode/count alone do not
identify filter rules. A collection refusal is evidence, not grounds to weaken
the sandbox.

Then perform only the first start:

```sh
osctl ct start nestedpodman
osctl ct exec nestedpodman ip -d link show dev eth0
osctl ct exec nestedpodman ip -4 address show dev eth0
osctl ct exec nestedpodman ip -4 route show table all
osctl ct exec nestedpodman cat /etc/resolv.conf
osctl ct exec nestedpodman systemctl show networking.service \
  -p ActiveState -p SubState -p Result -p ExecMainStatus
osctl ct exec nestedpodman journalctl --no-pager -o short-precise \
  -u networking.service -u 'ifup*' -u 'dhcpcd*'
```

Capture the same host bridge/address/route, dnsmasq lease/log, kernel guard/LSM
messages and process snapshots with UTC and monotonic timestamps. In the
disposable runner, use independent bounded command timeouts and one 60-second
startup deadline; stop collection at the first permanent error. Do not let
the original 900-second online wait consume the diagnostic. Network namespace
state should be cross-checked through the exported container init PID as well
as `osctl ct exec`. Retain failed collection commands and their statuses.

## Interpretation and stop criteria

- First prctl returns EACCES: filter installation was not attempted by that
  invocation. Compare the saved outer filter/LSM and predecessor guard state;
  this is not evidence of a missing entry in dhcpcd's later allowlist.
- NNP succeeds, filter prctl returns EACCES: verify NNP=1 on that same TID.
  Ordinary missing-NNP/CAP_SYS_ADMIN authorization cannot explain the normal
  precondition if NNP is set; inspect the explicit guarded-transition and other
  effective policy paths. A guard cause still needs its rejection evidence.
- Either call returns EPERM: errno 1 from an outer filter is a distinct result
  from the incident wording. Identify the actual rule/LSM; do not equate the
  default LXC module denylist with a prctl denial.
- Both calls succeed, then SIGSYS/kill occurs: investigate the later offending
  syscall and filter action. This differs from the retained manager-entry error.
- Both succeed and DHCP works: record a non-reproduction with exact identities
  and instrumentation differences. No retry loop or causal exclusion follows.

Preserve original bytes and complete trace before any later proposed change.
No package installation or target activation follows this diagnostic. A repair
requires a separate regression run covering confined DHCP and the full nested
workload assertions described in `podman-findings.md`.
