# IncusOS tenant boot, device and storage boundaries

Owner: implementer1, evidence package for architect0. Inspected 2026-10-28.
Session identity and both environment variables match
`2026-10-28-incusos-compatibility-assessment` in
`/home/aither/workspace/ai/vpsfree.cz`.

## Conclusion

Stock IncusOS does not fit the existing osctld system-container contract.
An image script and distribution configuration cannot give a container its own
firmware boot, kernel, boot-disk partition layout or measured OS update cycle.
Passing through additional devices would expand tenant privileges without
supplying that missing execution model. This is a source/documentation
compatibility conclusion; no IncusOS container was built or started.

The user confirms that Incus in an ordinary distribution already works. This
package therefore makes no claim about general Incus nesting limitations and
does not propose revalidating that established case.

## Source identity and limits

All vpsAdminOS evidence below is from current default `staging` commit
`f40afdf844223410767a04d2a96215b1d796b967`, supplied and authorized by the lead
and architect. The object was unavailable in the canonical bare clone, so the
exact commit's raw GitHub files were read, including its complete `AGENTS.md`.
No refs were fetched or changed. Initial inspection of legacy cached
`origin/master` (`4658d40f8ca459194b578aa30b0f9bb344cd7ee2`, June 2023) is
superseded and does not support the findings below. Official IncusOS `main`
documentation was read on 2026-10-28; it is a moving documentation version.
No deployed-node configuration or device inventory was inspected.

## Decisive boundaries

| Requirement | Current source evidence | Consequence for IncusOS |
| --- | --- | --- |
| Independent boot and kernel | [`osctld/templates/ct/config.erb`, lines 11–15, 19–32, 49–50](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/osctld/templates/ct/config.erb#L11-L50) selects a `dir:` rootfs, emits UID/GID maps and seccomp, optionally selects AppArmor, and starts the configured init command. | The container executes under the host kernel. Restarting it does not execute an IncusOS UKI or change the running kernel. The official [container/VM explanation](https://linuxcontainers.org/incus/docs/main/explanation/containers_and_vms/) confirms this distinction. |
| Private boot disk and encrypted system state | [`docs/containers/datasets.md`, lines 1–14](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/docs/containers/datasets.md#L1-L14) places the rootfs in a host-managed dataset's `private` directory and deliberately hides `.zfs`. | This directory is not IncusOS's partitioned system disk. IncusOS's [partitioning scheme](https://linuxcontainers.org/incus-os/docs/main/reference/partitioning-scheme/) includes an ESP, two verified root slots, LUKS system/swap partitions and an encrypted `local` ZFS pool. Extracting one root filesystem omits those relationships. |
| Tenant-controlled device access | [`os/modules/osctl/standard-devices.nix`, lines 1–85](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/os/modules/osctl/standard-devices.nix#L1-L85) allows basic character devices; wildcard block/character entries grant only `m` (node creation). No block read/write, TPM, ZFS-control or KVM access is listed. [`docs/containers/devices.md`, lines 10–17, 75–93](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/docs/containers/devices.md#L10-L17) requires host-admin grants through parent groups. | Creating a device node does not grant use of a disk or control device. These are standard defaults, not proof that every configured VPS lacks extra devices or that explicit passthrough is impossible. |
| Nesting configuration | [`osctld/configs/lxc/nesting.conf`, lines 1–2](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/osctld/configs/lxc/nesting.conf#L1-L2) adds proc/sys mounts; the template includes it conditionally at lines 6–8. | Existing nesting does not add firmware, a TPM, a boot disk or a private kernel. It cannot resolve the IncusOS appliance requirements. |

IncusOS normally requires UEFI Secure Boot and TPM 2.0. Its documented evaluation
exceptions permit disabling Secure Boot or using a software TPM, but not both.
Those exceptions still describe a booted machine; they do not provide a
container mode. Exposing host firmware state would describe the host's boot,
not an independent IncusOS boot. The [system requirements](https://linuxcontainers.org/incus-os/docs/main/getting-started/requirements/)
and [security design](https://linuxcontainers.org/incus-os/docs/main/reference/security/)
tie the trusted boot state to disk-unlock keys. Architect0 owns the separate
pinned incus-osd startup/refusal-path evidence.

Host ZFS backing is also distinct from granting IncusOS control of a ZFS pool.
osctld owns the backing datasets and their export/mount relationships
([datasets, lines 42–49 and 101–115](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/docs/containers/datasets.md#L42-L49)).
IncusOS's [storage API](https://linuxcontainers.org/incus-os/docs/main/reference/system/storage/)
expects to manage encrypted pools and their devices. Whether a narrowly delegated
ZFS arrangement could support a modified daemon was not tested. A `/dev/zfs`
grant alone is not evidence of appropriate delegation or safe pool isolation.

IncusOS updates replace the inactive UKI/root slot and activate it on reboot.
The [update documentation](https://linuxcontainers.org/incus-os/docs/main/reference/system/update/)
also expects regular OS updates and reboots. A container restart cannot activate
the shipped kernel, so preserving this API while skipping its effect would give
incorrect update/rollback semantics. Its [kernel API](https://linuxcontainers.org/incus-os/docs/main/reference/system/kernel/)
also includes module and PCI operations requiring an explicit tenant-safety
assessment if retained in any derivative.

## Existing tests and future POC boundary

The current [`tests/suite/cgroups/devices-v2.nix`, lines 74–94](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/tests/suite/cgroups/devices-v2.nix#L74-L94)
expects reads/writes to a manually created host-disk node to fail with `EPERM`.
This is relevant existing test coverage, not a test result from this assessment.
No builds, runtime tests, deployments, source edits or Git mutations were run.

No POC is needed to establish the boot-model mismatch. If separately requested,
an isolated experiment would need to define its product boundary first:

- For a container derivative, verify that startup, storage and update APIs work
  without host EFI/TPM access, host-pool administration or host-wide kernel/PCI
  operations; specify which upstream security/update guarantees are replaced.
- Verify encrypted persistent-data integrity across container restart, upgrade,
  failed upgrade and rollback, including the displayed running OS/kernel state.
- A VM experiment must supply independent UEFI/TPM/disk state and prove update
  and recovery there. KVM availability is a separate host/device authorization
  question; its absence from the standard list is not proof of universal
  impossibility. Running a VM inside a VPS would not be IncusOS as an osctld
  system container.

These are proposed acceptance checks only. Any removal of IncusOS boot/security
checks or replacement of its storage/update model is substantive derivative
work, not a distribution image/configuration addition.
