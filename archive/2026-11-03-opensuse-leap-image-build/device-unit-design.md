# Milestone 2: openSUSE device units require udev

Architect0 owns this brief. The lead accepted the causal runtime proof and
assigned source/Git ownership to implementer1 after Milestone 1 delivery
`57871a8e3f8f429e86e3ad6abf16de99a44e9416`. This is the user's requested actual
openSUSE fix. The earlier expectedFailure-extension proposal remains withdrawn.

## Proven cause and evidence

The image bootstrap installs with `--no-recommends` but omitted `udev`.
Libudev and `99-systemd.rules` were present, while the udev daemon/administration
binaries and all service/socket/trigger units were absent. There was no udev
process, device database or systemd tags. Unit LoadState was not-found, not a
failed container condition. The host's regular `/run/udev/control` stub and
the existing/up eth0 were correct. PID 1 showed loaded but inactive device units
with empty SysFSPath. Missing userspace udev processing explains the failure.

The controlled native-zypper experiment installed the signed udev dependency
closure: 15 new packages, none removed. All temporary runtime IPv4 addresses,
routes and resolver contents were restored **before** offline installation.
Normal container stop/start changed PID 3134 to 6034, retaining the original
eth0 with no IPv4 address. Udevd was active/running, its trigger active/exited,
eth0.device active, and dummy0 absent then active after ordinary interface
creation. Both interfaces had `systemd` udev tags. No manual daemon start,
daemon reload, event replay, host privilege or namespace change produced this
result. The package closure plus normal boot supplied the missing processing.

This is causal evidence on the retained AA container, not final-source build
acceptance. Preserve the observations, network-only negative control, native
solver package/signature inventory and restart/device assertions in the
implementer's result records. The prepared and executed sequence is described
in [package experiment](device-unit-package-experiment.md); it contains older
superseded preparations, so the final result must identify the executed input.

Runtime installation emitted a reload connection-refused/Lua transfiletrigger
warning before the first udev boot. Implementer1 must explain it from the
accepted raw packet and distinguish it from the original old-builder missing
Lua APIs. Successful restart does not waive clean-image bootstrap checks or
justify suppressing scriptlets. No further generic investigation is requested.

## Preserved identity

- AA source `aa963dce42859ae4251cdfaded91920d67b3a46e`, tree
  `d4a264295678a50eac25732074dc942e637850e4`; backup ref
  `refs/backup/2026-11-03-opensuse-leap-image-build/tested-dedicated-aa963dce4`.
- Immutable `/nix/store/6n06fybbvbrkm4ixybr4qjns26isgz5j-source` matches all
  2,373 AA archive files/symlinks. Runner, config, hashes and native command:
  [immutable inputs](device-unit-immutable-inputs.md).
- Failed/diagnostic VM state:
  `/tmp/2026-11-03-opensuse-leap-image-build-device-units/os-test-systemd__device-units-e983cb16/`,
  retained container `testct-553b`. Lead owns its current operation/status.
- Original image SHA256
  `254523b59106db1d27bcf98e43e942c8ea1d7f0c15238542ca17e21612017214`;
  [matrix receipt](candidate-matrix-result.md) and `aa963dce4-device-units-*.log`
  preserve the pre-experiment failure. The image had passed its 15 ordinary
  checks and start-stop; those did not establish working device units.

## Accepted minimal source boundary

| File | Change |
| --- | --- |
| `image-scripts/include/opensuse.sh` | Add explicit `udev` to existing EXTRAPKGS; native package management resolves dependencies. Keep `--no-recommends`, existing network-only trigger override and all other configuration. |
| `tests/suite/systemd/device-units.nix` | Remove obsolete openSUSE expectedFailure declaration and its immediate-command conditional. Use the existing normal wait path and preserve every eth0/dummy0 assertion and normal cleanup. |

These changes form one coherent third commit after the shared-builder and
new-image commits. Source removal of the exception is now authorized by the
lead; final passing tests are the readiness gate, not a new pre-edit approval.
No new helper/framework, osctld change, service mask or device exposure is needed.
A brief nearby rationale may explain why a minimal image explicitly needs udev;
do not add a separate generic documentation subsystem.

Actual shared-helper consumers are **Leap 15.6, 16.0, 16.1 and Tumbleweed**.
The three Leap images use the upgraded shared stable builder; Tumbleweed uses
its existing builder. All retain their target identity and repositories.
Rebuilt images/new containers gain udev; already existing containers are not
changed by publishing scripts. A documented package install followed by normal
restart is a separate operator remedy, not a deployment performed here.
Old/new hosts remain compatible: no persisted host format/API/protocol change
or coordinated fleet upgrade. Preserve user namespaces, `/run` ownership,
restricted devices, networking and clean lifecycle behavior.

## Final checks

Run syntax/config checks and repository hooks, commit all intended source, then
obtain retained independent review of the complete three-commit history before
long final-source checks. Do not review or validate an incomplete source head.
Implementer owns diagnosis; fresh utility watchers launch/monitor long checks.

Combine shared-builder regression with helper regression in one normal image
test batch for `image-scripts/test@opensuse-{leap-15.6,leap-16.0,leap-16.1,tumbleweed}`.
Use one quoted native selector, bounded jobs (at most 2), stop-on-failure and
fresh session-owned disks. The existing session-only 8 GiB sizing interface and
exact-final-revision metadata from [Milestone 1](design.md) apply. Never reuse
the name-derived old Leap 15.5 builder. Record actual builder identity, final
source/config, output hashes and native results. Every image must pass its
normal suite and complete the package transaction without the old Lua API,
unpack or unexplained scriptlet failures. Explain any new warning before acceptance.

Then execute the original device assertions against each rebuilt helper consumer
using the existing candidate-repository/manual-PTY method. Explicit 16.1 uses
`systemd/device-units#opensuse-leap-16.1`. Other versions can reuse the unchanged
`systemd/device-units#opensuse-latest` script with a temporary **local test**
`latest` alias pointing to exactly one recorded candidate at a time; record its
real version/archive hash and do not alter public tags or add permanent matrix
entries solely for this check. These are four image/device combinations, not
a historical-release campaign. Check the removed exception's ordinary success
path; no failure, timeout or dummy0 omission counts as success.

Crucially, production `opensuse/latest` denotes Leap (public 16.0 before rollout,
intended 16.1 after it); Tumbleweed uses `latest-tumbleweed`. Tumbleweed alone
cannot validate the Leap exception removal. Candidate-backed 16.0 and 16.1
coverage establishes both relevant Leap meanings. Retain service-absence/URL
readback assertions and exact artifact mapping from
[candidate checks](candidate-checks.md); do not resurrect URL-only automation.

Finish remaining 16.1 `/run`, routed networking and cgroup v1/v2 checks as planned
and retain clean start-stop evidence. Report actual passes and any limits;
publication, integration and deployment remain separately authorized.
