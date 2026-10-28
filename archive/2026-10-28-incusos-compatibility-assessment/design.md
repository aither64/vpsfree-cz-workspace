# IncusOS as a vpsAdminOS system container: assessment

Owner: architect0. Assessed 2026-10-28. Scope: investigation only; no application
edits, builds, runtime tests, deployment or integration. Ordinary Incus running
inside another distribution is established by the user and outside this verdict.

## Verdict

**Stock IncusOS is incompatible with the current osctld system-container model.**
A root filesystem could be extracted and packaged, but an image recipe and
distribution configuration would not preserve the IncusOS appliance. Its daemon
requires machine boot/security and disk state during normal startup, and its
storage and update mechanisms continue to depend on that state afterward.

A container port is conceivable as a maintained derivative. It would replace or
remove central IncusOS contracts, not merely add distribution support. No such
port has been demonstrated here. A full VM preserves the relevant execution
model; running one inside a VPS would be a separate VM deployment, not IncusOS
as the osctld system container. No VM deployment is proposed or authorized.

## Evidence and source identity

Current published sources were pinned through GitHub API/raw reads:

- IncusOS `main`: [`539f012e716a7434e8429faf3232568a7aafb1d4`](https://github.com/lxc/incus-os/tree/539f012e716a7434e8429faf3232568a7aafb1d4), 2026-10-28 16:34 UTC.
- vpsAdminOS default `staging`: [`f40afdf844223410767a04d2a96215b1d796b967`](https://github.com/vpsfreecz/vpsadminos/tree/f40afdf844223410767a04d2a96215b1d796b967), 2026-10-28 13:21 UTC.
- vpsAdmin default `master`: [`4cb66436558d4c494d658042192f7b743eddb54d`](https://github.com/vpsfreecz/vpsadmin/tree/4cb66436558d4c494d658042192f7b743eddb54d), 2026-10-28 12:55 UTC.

The initial cached vpsAdminOS `origin/master` was historical; its evidence was
superseded with current `staging`. These pins describe source, not deployed
nodes or the exact IncusOS stable-channel image. Official documentation was read
on the assessment date and checked against pinned source.

| Boundary | Decisive evidence and consequence |
| --- | --- |
| Image and boot | IncusOS [`mkosi.conf`](https://github.com/lxc/incus-os/blob/539f012e716a7434e8429faf3232568a7aafb1d4/mkosi.conf#L10-L48) builds a bootable disk with signed kernel images and verity. Current osctld [`ct/config.erb`](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/osctld/templates/ct/config.erb#L11-L50) supplies a directory rootfs, user namespace and init command under the host kernel. A container restart cannot boot the supplied IncusOS kernel. |
| Actual startup refusal | [`main.go:254`](https://github.com/lxc/incus-os/blob/539f012e716a7434e8429faf3232568a7aafb1d4/incus-osd/cmd/incus-osd/main.go#L254-L274) calls `CheckSystemRequirements` before normal startup. [`install.go:45–64`](https://github.com/lxc/incus-os/blob/539f012e716a7434e8429faf3232568a7aafb1d4/incus-osd/internal/install/install.go#L45-L64) rejects disabled Secure Boot combined with no working physical TPM. This is not merely an installer requirement. |
| Further startup dependencies | Even bypassing that guard leaves unconditional [`GetLUKSVolumePartitions` / PCR checks](https://github.com/lxc/incus-os/blob/539f012e716a7434e8429faf3232568a7aafb1d4/incus-osd/cmd/incus-osd/main.go#L520-L544). The [partition lookup](https://github.com/lxc/incus-os/blob/539f012e716a7434e8429faf3232568a7aafb1d4/incus-osd/internal/util/luks.go#L14-L46) requires `/dev/disk/by-partlabel/swap` and derives the root partition from its number. Fresh installs also [enroll recovery keys using TPM unlocking](https://github.com/lxc/incus-os/blob/539f012e716a7434e8429faf3232568a7aafb1d4/incus-osd/internal/systemd/cryptenroll.go#L35-L74). A normal directory rootfs lacks these devices. |
| Storage ownership | Startup [loads local storage](https://github.com/lxc/incus-os/blob/539f012e716a7434e8429faf3232568a7aafb1d4/incus-osd/cmd/incus-osd/main.go#L1106-L1117); [`zfs.LoadPools`](https://github.com/lxc/incus-os/blob/539f012e716a7434e8429faf3232568a7aafb1d4/incus-osd/internal/zfs/zfs.go#L36-L123) imports encrypted pools and creates `local` on `/dev/disk/by-partlabel/local-data`. A host-managed ZFS dataset is not guest pool administration. Additional device grants do not provide an independent boot or prove safe delegation. |
| Updates and rollback | [A/B updates](https://github.com/lxc/incus-os/blob/539f012e716a7434e8429faf3232568a7aafb1d4/doc/reference/partitioning-scheme.md) switch signed UKIs and disk partitions. The [updater](https://github.com/lxc/incus-os/blob/539f012e716a7434e8429faf3232568a7aafb1d4/incus-osd/internal/systemd/sysupdate.go#L160-L189) adjusts boot/encryption bindings and mounts `/dev/mapper/usr` before `systemd-sysupdate`; its [transfer target](https://github.com/lxc/incus-os/blob/539f012e716a7434e8429faf3232568a7aafb1d4/mkosi.images/base/mkosi.extra/usr/lib/sysupdate.d/12-usr.transfer) is a partition. Repacking or disabling updates cannot claim equivalent update/recovery behavior. |

The security qualification matters: upstream permits either disabled Secure Boot
or an in-OS software TPM for degraded operation, [not both](https://linuxcontainers.org/incus-os/docs/main/getting-started/requirements/).
Missing EFI variables alone are handled as absent rather than necessarily fatal;
disabled Secure Boot can use embedded certificates. Neither fallback provides a
container mode. Exposing the host's firmware/TPM would measure the host boot, not
an independent IncusOS boot. The official [Incus installation guide](https://linuxcontainers.org/incus-os/docs/main/getting-started/installation/virtual-incus/)
explicitly creates a VM with a virtual TPM.

## Configuration and secondary integration

The current [image build contract](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/image-scripts/README.md#L88-L136)
populates `$INSTALL`; export/import carries filesystem payloads and osctld
metadata. There is no current IncusOS image or distconfig handler. Immutability
alone is not the blocker: existing NixOS and Guix integrations deliberately build
container variants. For example, [Guix's container module](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/image-scripts/images/guix/vpsadminos.scm#L30-L136)
uses a dummy kernel/rootfs, removes firmware services and defines host/guest
network ownership. That precedent illustrates the required port boundary.

Networking is tractable **after** choosing a derivative contract. IncusOS already
represents static addresses, routes including on-link gateways, DNS and hostname
in its [network API/seed](https://linuxcontainers.org/incus-os/docs/main/reference/system/network/).
However, incus-osd [sets hostname and regenerates networking](https://github.com/lxc/incus-os/blob/539f012e716a7434e8429faf3232568a7aafb1d4/incus-osd/internal/network/networkd.go#L109-L128)
from its own state, [replacing `/run/systemd/network`](https://github.com/lxc/incus-os/blob/539f012e716a7434e8429faf3232568a7aafb1d4/incus-osd/internal/network/networkd.go#L1039-L1089).
osctld's `/etc` writes are not directly deleted there, but two independent
configuration owners would conflict. A port needs one authoritative model and
explicit translation across create, live changes, restart and update. Upstream
seed ingestion also assumes a seed partition rather than a conventional rootfs
provisioning file.

vpsAdmin's template metadata can name a compatible derivative without an intrinsic
schema/client change. Its existing password, SSH-key and osctl configuration
operations do not provision IncusOS's authenticated API. Those controls must be
mapped or gated, certificate enrollment defined, and unsupported script/cloud-init
features disabled. Dataset backup/migration must include every persistent key,
application database and storage dependency; existing outer snapshots alone do
not prove appliance recovery.

## Boundaries if a port is requested later

No implementation is authorized. The lead must first accept the loss/replacement
of upstream appliance guarantees and a separately named derivative boundary.

1. Appliance-port package: upstream build, `incus-osd` startup/security/storage/update
   files; define container-safe persistence, honest security status and a working
   update/rollback protocol without host EFI/TPM/pool/kernel administration.
2. vpsAdminOS package, dependent on that contract: image recipe, distconfig and
   tests; preserve user namespace/device isolation, define one network/hostname
   owner and handle all persistent datasets.
3. vpsAdmin package, dependent on the image/config contract: template data,
   provisioning/trust and capability handling; preserve reinstall, restore and
   migration data semantics. New public API fields are conditional, not assumed.

Quick checks would inspect image metadata, generated configuration and forbidden
device/capability requirements. Longer isolated checks must prove startup, live
network changes, restart, update/failure/rollback and complete data recovery across
outer migration. Old/new guest and node combinations need explicit support gates;
rollback must load newly written state or restore a documented complete snapshot.
No coordinated fleet update is justified by this assessment. The current verdict
requires no runtime POC; no tests were executed.

## Supporting findings and handoff

- implementer0: [current image/distconfig evidence](vpsadminos-image-distconfig-findings.md).
- implementer1: [runtime/device/storage evidence](vpsadminos-nesting-findings.md).
- implementer2: [vpsAdmin integration evidence](vpsadmin-integration-findings.md).

Lead owns state/portal reconciliation and user-facing delivery. The handoff skill
is applied without lifecycle action. Session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-28-incusos-compatibility-assessment/

Disposable read-only upstream source snapshot used for this investigation:
`/tmp/incusos-assessment-20261028-architect0/lxc-incus-os-539f012`.
No project refs or worktrees were changed.
