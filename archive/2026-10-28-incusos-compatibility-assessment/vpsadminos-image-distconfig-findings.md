# IncusOS: vpsAdminOS image and distconfig evidence

Owner: implementer0, under architect0. Read-only investigation, 2026-10-28.

**Verdict:** packaging an already container-compatible root filesystem is routine;
making upstream IncusOS preserve its appliance boot, storage, management and update
behavior inside a system container is a substantive port. Adding image scripts and
a distribution handler alone does not establish that compatibility. Immutable
stores are not themselves the obstacle: current vpsAdminOS has explicit NixOS,
NixOS impermanence and Guix container integrations.

## Source identity and limits

- Session and environment binding verified:
  `2026-10-28-incusos-compatibility-assessment`, workspace
  `/home/aither/workspace/ai/vpsfree.cz`.
- Current assessment pin: vpsFree.cz/vpsadminos default `staging`,
  **`f40afdf844223410767a04d2a96215b1d796b967`**, supplied by architect0 after
  the lead's GitHub API check. Relevant files were read independently through
  immutable raw GitHub URLs. Links below bind file and line evidence to this pin.
  Current [AGENTS.md](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/AGENTS.md)
  was read in full. The recursive GitHub tree response was not truncated and
  contained no Incus-named image or distconfig paths.
- The initial authorized bare-repository `origin/master` inspection was historical:
  `4658d40f8ca459194b578aa30b0f9bb344cd7ee2`, dated 2023-06-06; there was no
  local `master` ref and no AGENTS.md at that old revision. The current pin was
  unavailable as a local object, so the authorized refresh used HTTP reads without
  fetching. Current conclusions below supersede the historical pass.
- No deployed-node revision was inspected. No source edits, Git mutations, builds,
  imports or runtime tests were performed. Only this assigned evidence file was
  written. Upstream IncusOS details below are explicitly architect-supplied;
  this package independently verifies the vpsAdminOS side.

## Image build, export, import and start contract

1. **The build product is a directory tree, not a bootable disk.** Each image has
   `config.sh` and `build.sh`; the latter must populate `$INSTALL` with the guest
   filesystem. Image attributes include distribution, version, architecture,
   vendor, variants and optional ZFS subdatasets
   ([image-scripts/README.md:88–136](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/image-scripts/README.md#L88-L136)).
   The builder creates output datasets, uses `private/` as the install directory,
   binds it into a build container, runs the script, then exports the result
   ([build.rb:133–169](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/osctl-image/lib/osctl/image/operations/image/build.rb#L133-L169),
   [197–227](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/osctl-image/lib/osctl/image/operations/image/build.rb#L197-L227)).

2. **Exports contain osctld metadata/configuration plus filesystem payloads.**
   The exporter sets distro attributes, accepts `container.yml` overrides and
   emits metadata/configs plus a rootfs tar archive, when enabled, and a ZFS
   stream archive
   ([export.rb:13–71](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/osctl-image/lib/osctl/image/operations/image/export.rb#L13-L71),
   [container_config.rb:17–27](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/osctl-image/lib/osctl/image/container_config.rb#L17-L27)).
   The script defaults the init command to `/sbin/init` and writes that command
   into image configuration
   ([runner:124–140](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/image-scripts/bin/runner#L124-L140)).

3. **Import does not reconstruct a machine boot chain.** It requires
   `metadata.yml`, dispatches only `zfs` and `tar` formats and, for tar, extracts
   `rootfs/base.tar.gz` into the container rootfs, including file capabilities
   ([importer.rb:26–33](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/osctld/lib/osctld/container/importer.rb#L26-L33),
   [204–244](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/osctld/lib/osctld/container/importer.rb#L204-L244),
   [331–355](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/osctld/lib/osctld/container/importer.rb#L331-L355)).
   LXC receives a `dir:` rootfs, UID/GID mappings, security profiles, a UTS
   hostname, and an init command
   ([ct/config.erb:11–50](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/osctld/templates/ct/config.erb#L11-L50)).
   **Inference:** extracting IncusOS disk partitions into this format can carry
   files, but does not preserve firmware boot, UKI verification, partition
   identities, TPM measurements or a guest-controlled disk update mechanism.

## Distribution configuration contract

| Concern | Current source behavior | Implication for IncusOS |
| --- | --- | --- |
| Dispatch | Exact configured distribution symbol selects a registered class; unknown names use `Other` ([dist_config.rb:12–45](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/osctld/lib/osctld/dist_config.rb#L12-L45)). `Other` warns for hostname/network ([other.rb:14–27](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/osctld/lib/osctld/dist_config/distributions/other.rb#L14-L27)). | Importability is distinct from integrated guest configuration. A new handler would need explicit contracts. |
| Start | Before guest init, the base handler applies configured hostname, DNS and networking through a rootfs helper ([base.rb:105–124](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/osctld/lib/osctld/dist_config/distributions/base.rb#L105-L124), [288–306](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/osctld/lib/osctld/dist_config/distributions/base.rb#L288-L306)). Most standard configuration errors are logged; DNS errors are re-raised ([dist_config.rb:37–44](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/osctld/lib/osctld/dist_config.rb#L37-L44)). | A successful container start is insufficient evidence that appliance services or guest configuration work. |
| Hostname | Base invokes distro persistence plus `/etc/hosts`, then a live hook ([base.rb:140–166](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/osctld/lib/osctld/dist_config/distributions/base.rb#L140-L166)). Arch illustrates writable `/etc/hostname` plus `hostname -F` ([arch.rb:8–31](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/osctld/lib/osctld/dist_config/distributions/arch.rb#L8-L31)). LXC also sets the initial UTS name. | An appliance daemon can subsequently own/reset hostname. Initial UTS naming does not settle persistent API configuration ownership. |
| DNS | Current generic support prepares NetworkManager ownership policy and writes `/etc/resolv.conf` with nameservers and `options edns0` ([configurator.rb:97–158](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/osctld/lib/osctld/dist_config/configurator.rb#L97-L158)); base coordinates live reload ([base.rb:210–228](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/osctld/lib/osctld/dist_config/distributions/base.rb#L210-L228)). | These are file/NetworkManager contracts, not an IncusOS configuration API integration. Persistence across appliance reconciliation must be established. |
| Users/passwords | Generic password changes execute guest `chpasswd` for the specified existing user, with `run: true` ([base.rb:230–255](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/osctld/lib/osctld/dist_config/distributions/base.rb#L230-L255)). Stopped execution uses `init.lxc` rather than guest init ([exec.rb:7–13](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/osctld/lib/osctld/container_control/commands/exec.rb#L7-L13)). | This does not provision appliance-managed users, API trust, or initial setup. Guest tool availability and persistence must be checked separately. |
| Writable files | The helper checks the owner's write mode bit; an absent file is considered writable ([common.rb:3–17](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/osctld/lib/osctld/dist_config/helpers/common.rb#L3-L17)). | This is an opt-out convention, not support for read-only mounts, verified images, or appliance reconciliation. |

### systemd-networkd and startup hooks

- The backend is selected by a distro handler, not automatically for every
  systemd guest. Its usability check requires `/etc/systemd/network`, an
  unmasked service, and an enabled link in
  `/etc/systemd/system/multi-user.target.wants/`
  ([systemd_networkd.rb:8–20](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/osctld/lib/osctld/dist_config/network/systemd_networkd.rb#L8-L20),
  [common.rb:20–44](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/osctld/lib/osctld/dist_config/helpers/common.rb#L20-L44)).
- It writes/removes `/etc/systemd/network/<interface>.network`; the backend
  itself contains no guest API or live-reload call
  ([systemd_networkd.rb:23–59](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/osctld/lib/osctld/dist_config/network/systemd_networkd.rb#L23-L59)).
  Routed configuration disables DHCP, adds addresses, a gateway reachability
  route with IPv4 `Scope=link`, and a default gateway; bridged configuration
  supports DHCP/static addresses and explicit non-DHCP gateways
  ([routed.erb:6–24](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/osctld/templates/dist_config/network/systemd_networkd/routed.erb#L6-L24),
  [bridge.erb:6–18](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/osctld/templates/dist_config/network/systemd_networkd/bridge.erb#L6-L18)).
- Generic systemd startup support creates a namespace-owned tmpfs `/run` and a
  `/run/udev/control` stub so systemd can monitor network device events. Detection
  special-cases NixOS or checks the `/sbin/init` symlink for `systemd`
  ([base.rb:36–102](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/osctld/lib/osctld/dist_config/distributions/base.rb#L36-L102),
  [309–323](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/osctld/lib/osctld/dist_config/distributions/base.rb#L309-L323)).

These hooks address containerized systemd device handling. They do not supply an
IncusOS machine boot/storage environment. Architect0 reports IncusOS regenerates
networkd configuration under `/run`; that does **not** mean it directly deletes
osctld's `/etc` files. File selection, overlapping interface matches, API-visible
state and reconciliation still need one authoritative owner.

## Existing immutable/declarative guest precedents

- **NixOS:** the image builder deliberately builds a container template and
  extracts its tarball, including a separate impermanence variant
  ([nixos.sh:26–55](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/image-scripts/include/nixos.sh#L26-L55)).
  The guest module sets `boot.isContainer`, enables an init script, acknowledges
  the absence of an initrd and supplies a unit consuming host-generated
  `/ifcfg.add` and `/ifcfg.del`
  ([stable/vpsadminos.nix:219–275](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/os/lib/nixos-container/stable/vpsadminos.nix#L219-L275)).
  Its minimal image creates a tarball containing the Nix closure and `/sbin/init`
  ([minimal.nix:120–136](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/os/lib/nixos-container/stable/minimal.nix#L120-L136)).
  Host distconfig generates the scripts, handles impermanence init setup, and
  explicitly declines hostname/hosts support
  ([nixos.rb:8–78](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/osctld/lib/osctld/dist_config/distributions/nixos.rb#L8-L78)).
- **Guix:** `guix system init` builds into `$INSTALL`, followed by a custom init
  ([build.sh:53–79](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/image-scripts/images/guix/build.sh#L53-L79)).
  Its container module removes bare-metal/firmware services, uses a dummy kernel
  and rootfs, excludes efivars, consumes host `/ifcfg.add`, and disables DHCP's
  resolver hook because osctld owns DNS
  ([vpsadminos.scm:30–99](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/image-scripts/images/guix/vpsadminos.scm#L30-L99),
  [101–136](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/image-scripts/images/guix/vpsadminos.scm#L101-L136)).
  Distconfig supplies special shutdown and password behavior
  ([guix.rb:36–102](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/osctld/lib/osctld/dist_config/distributions/guix.rb#L36-L102)).
- **Explicit limits remain:** image tests skip external hostname configuration
  for NixOS/Guix and DNS for NixOS; stopped-password testing skips NixOS
  impermanence and initially boots other NixOS/Guix images to establish `/etc`
  ([hostname.sh:15–18](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/image-scripts/tests/hostname.sh#L15-L18),
  [dns_resolver.sh:24–27](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/image-scripts/tests/dns_resolver.sh#L24-L27),
  [passwd_stopped.sh:1–20](https://github.com/vpsfreecz/vpsadminos/blob/f40afdf844223410767a04d2a96215b1d796b967/image-scripts/tests/passwd_stopped.sh#L1-L20)).

## IncusOS-specific conclusion and remaining uncertainty

Architect0's upstream inspection is pinned to
`539f012e716a7434e8429faf3232568a7aafb1d4`. Its reported decisive constraints are
bootable disk output with signed UKI/verity; `run` invoking
`CheckSystemRequirements` before startup; refusal when Secure Boot is disabled
**and** a physical TPM is absent; partition-based source-device discovery;
local LUKS/ZFS initialization; and disk-oriented system updates. This package
does not independently certify those upstream paths; architect0 owns their
exact citations and final reconciliation.

Do not claim that an absent SecureBoot EFI variable alone is fatal: architect0
corrected that interpretation because missing EFI variables are handled as empty
values. The stronger appliance requirements, and their combination with the
directory-rootfs contract demonstrated above, establish the non-routine scope.

An IncusOS container variant could be investigated, but must deliberately define
replacements or supported omissions for boot verification, TPM/key handling,
partition discovery, local storage, updates and configuration ownership. A
rootfs that starts systemd while its appliance daemon fails is not successful
IncusOS support. Runtime feasibility, exact required patches, supported upstream
update behavior and security equivalence remain unproven. This assessment makes
no recommendation about installing ordinary Incus on another distribution.

## Bounded future POC plan — not executed

1. **Gate on a container contract.** Pin the intended vpsAdminOS runtime and
   IncusOS source/image; record which appliance behaviors must survive. Resolve
   the upstream requirement/partition/storage/update paths before writing broad
   distro integration. Stop if the proposed variant requires unsupported host
   TPM, raw-disk, kernel-global ZFS or lockdown access without an acceptable
   isolation design.
2. **One disposable guest, boot first.** Produce one explicitly labeled IncusOS
   container rootfs, wrap it in the existing image format and import it. Verify
   PID 1, appliance daemon readiness, first boot and restart. Record every
   bypass/change; stop if only systemd starts or the appliance must be disabled.
3. **One configuration owner.** Test bridge DHCP and routed static IPv4/IPv6
   address/default-route cases; verify guest connectivity, hostname, DNS and
   API-visible configuration after boot, daemon restart, a configuration change
   and container restart. Check `/etc` versus `/run` networkd matches explicitly.
   Define account/API-trust provisioning and test password operations only when
   the proposed supported contract includes them.
4. **Persistent appliance behavior.** Write a known payload in the intended
   persistent storage, export/import and verify its checksum and ownership.
   Test one supported appliance update and rollback with daemon readiness,
   configuration and payload preserved. Failure to support those operations
   narrows the product to a modified experimental image; it does not establish
   upstream IncusOS compatibility.

No fleet-wide coordinated update follows from this investigation. Any future
handler/image should initially be additive, with old nodes kept from scheduling
the new image until supported; a host security/storage exception would require
a separate design and mixed-version/rollback assessment.

Handoff: evidence package complete for architect/lead synthesis; no review,
commit, build or deployment requested. Session remains open.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-28-incusos-compatibility-assessment/)
