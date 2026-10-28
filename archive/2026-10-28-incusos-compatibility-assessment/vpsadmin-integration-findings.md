# vpsAdmin integration evidence for IncusOS

Assessment only, 2026-10-28; owner `implementer2`, under `architect0`.
Session identity and both environment markers matched
`2026-10-28-incusos-compatibility-assessment` and
`/home/aither/workspace/ai/vpsfree.cz` before session access.

## Verdict and source scope

**Registering a hypothetical osctld-compatible IncusOS derivative would not
intrinsically require a database migration, new distribution enum or generated
client change. Registration alone does not provide IncusOS support.** vpsAdmin
assumes an osctld-managed container root filesystem, host-owned networking and
managed ZFS datasets. Its existing guest credential operations set a root
password and edit root's SSH keys; these do not implement appliance/API trust
enrollment. The architect's IncusOS boot/storage/update assessment remains the
primary feasibility boundary.

Current-source pin: `vpsfreecz/vpsadmin@4cb66436558d4c494d658042192f7b743eddb54d`,
supplied as current default `master` by architect0's GitHub API lookup.
This object was absent locally. Read current `AGENTS.md` and retrieved 36
decisive source/guidance files from immutable `raw.githubusercontent.com` URLs;
each was byte-identical to the initially inspected local `origin/master`
`08c3bd7e3cb4dc324a0381df6a1eec190daab1a7`. Local `master` was
`b4ef8535a629ee8c9cd753afecdb05e0895d0eea`; neither local ref is presented as
current upstream. All citations below identify the current pin. No inference
about deployed node versions, source edits, fetches, builds or runtime tests.
Normal-distro Incus is outside this final package per user steering.

Citation prefix **V** is
[`vpsadmin@4cb66436558d4c494d658042192f7b743eddb54d`](https://github.com/vpsfreecz/vpsadmin/tree/4cb66436558d4c494d658042192f7b743eddb54d).
Paths and line numbers below are relative to that exact tree.

## Decisive mappings

| Area | Source evidence at V | Consequence for IncusOS |
| --- | --- | --- |
| Registration | `api/db/schema.rb:1497–1527`; `api/lib/vpsadmin/api/resources/os_template.rb:9–28,124–150`; `api/models/os_template.rb:64–65` | Family and template are data. Distribution/version/vendor/variant/arch are strings; hypervisor and cgroup are the enums. Admin registration accepts YAML config. The derived template name has a 64-character database limit. Metadata can describe a compatible image without a new API field. |
| Capability metadata | `api/models/os_template.rb:18–36,44–59`; `api/lib/vpsadmin/api/resources/os_template.rb:14–22,48–54` | Available controls include enabled/supported, cgroup version, hostname/DNS defaults, script/cloud-init flags, and YAML datasets/mounts/features. These are not an appliance provisioning or trust schema. `supported` is a declaration, not a runtime proof. |
| Create/image ownership | `api/models/transactions/vps/create.rb:13–25`; `libnodectld/lib/nodectld/commands/vps/create.rb:6–27` | The image tuple passes to `osctl ct create`. Image-carried mounts are cleared explicitly so vpsAdmin owns mounts. Merely making an image discoverable cannot add a disk installer, boot firmware or appliance provisioning. |
| Extra storage/default features | `api/models/transaction_chains/vps/create.rb:41–128,154–190`; `api/models/vps_feature.rb:25–36` | Template config can create managed subdatasets, bind mounts and defaults for a fixed feature set. It does not express arbitrary disks, firmware/TPM, IncusOS API configuration or trust credentials. Existing feature flags do not change this management model. |
| Hostname/DNS | `api/lib/vpsadmin/api/operations/vps/create.rb:20–22`; `api/models/transaction_chains/vps/create.rb:258–266`; `libnodectld/lib/nodectld/commands/vps/hostname.rb:6–11`; `libnodectld/lib/nodectld/commands/vps/dns_resolver.rb:6–15` | Creation can opt out of host-managed hostname/DNS through template flags. Otherwise changes use `osctl ct set hostname` and `ct set dns-resolver`; a working distribution adapter or a deliberate IncusOS management bridge is needed. |
| Network | `api/models/transaction_chains/vps/create.rb:192–201`; `libnodectld/lib/nodectld/commands/network_interface/create_veth_routed.rb:6–20`; `libnodectld/lib/nodectld/network_interface.rb:15–50` | Default interface is routed `venet0`; IPs and routes use `osctl ct netif` primitives. There is no IncusOS-specific configuration call in this path. Address allocation and appliance network ownership must agree across reboot and updates. |
| Password/SSH/API trust | `api/lib/vpsadmin/api/resources/vps.rb:676–703`; `libnodectld/lib/nodectld/vps.rb:42–43`; `libnodectld/lib/nodectld/commands/vps/deploy_public_key.rb:6–8,18–25,70–79`; `api/models/transaction_chains/vps/create.rb:270–272` | Password reset is exposed generically and invokes `osctl ct passwd`. Auto-add keys write `/root/.ssh/authorized_keys` in the guest. Template metadata has no password-reset or SSH-deployment capability flag. Neither action enrolls a client certificate or configures API trust. A supported IncusOS offering must map, gate or replace these operations and define trust/secret handling. |
| User data | `libnodectld/lib/nodectld/vps_user_data/script.rb:43–61`; `libnodectld/lib/nodectld/vps_user_data/cloud_init.rb:13–30,35–66,74–128`; `api/models/os_template.rb:44–59` | Script init installation and cloud-init package/service setup use explicit distro cases with no IncusOS entry. Disable their template flags unless implemented and verified. Generic cloud-init also disables its network configuration; it is not an existing IncusOS seed/provisioning adapter. |
| Reinstall | `api/lib/vpsadmin/api/operations/vps/reinstall.rb:18–29`; `api/models/transaction_chains/vps/reinstall.rb:12–38,49–66`; `libnodectld/lib/nodectld/commands/vps/reinstall.rb:6–18` | Checks cover hypervisor/cgroup compatibility. Reinstall backs up managed datasets, stops, applies an osctl image tuple, clears image mounts, reapplies existing VPS features and attempts automatic key deployment. It does not rerun the create path's template dataset/mount/default-feature setup. A different IncusOS state layout needs explicit reinstall semantics. |
| OS version reporting | `api/lib/vpsadmin/supervisor/node/vps_os_release.rb:39–75,89–126` | Version reporting can change the template record only when reported distro/version matches another registered tuple. Define how a derivative's reported OS identity and atomic updates map to templates; this mechanism does not perform the appliance update. |

## Backup, restore and migration boundary

- Managed snapshots are dataset operations, not Incus application backups:
  `V:api/models/transaction_chains/dataset/snapshot.rb:8–30` and
  `V:libnodectld/lib/nodectld/commands/dataset/snapshot.rb:3–8` invoke the
  dataset snapshot primitive without an IncusOS quiesce/export step.
- VPS restore wraps dataset rollback with outer stop/start:
  `V:api/models/transaction_chains/vps/restore.rb:5–29`. State outside the
  managed dataset tree is not established as recoverable by this path.
- Migration selects the managed dataset subtree, checks cgroup compatibility,
  copies configs/rootfs, stops the source, sends final state, rebuilds mounts
  and restarts the destination:
  `V:api/models/transaction_chains/vps/migrate/base.rb:93–123,158–175`;
  `V:api/models/transaction_chains/vps/migrate/os_to_os.rb:37–49,73–78,112–159`.
  Node primitives are `osctl ct send rootfs` and `ct send state`
  (`V:libnodectld/lib/nodectld/commands/vps/send_rootfs.rb:6–7`,
  `V:libnodectld/lib/nodectld/commands/vps/send_state.rb:6–17`). This does not
  establish portable TPM-bound/encrypted appliance state, application-consistent
  Incus database backup, or preservation of external storage.

## Future acceptance checks if a container derivative is pursued

These are proposed checks, not executed validation or a recommendation to
implement support for stock IncusOS.

1. First satisfy the architect's boot, storage, security and update/rollback
   requirements. Specify the maintained derivative boundary before registration.
2. Register a disabled test template and verify tuple lookup, cgroup placement,
   create/start/stop, network address/route changes, hostname and DNS ownership
   across reboot and update. Keep unsupported script/cloud-init modes disabled.
3. Define provisioning and certificate trust enrollment/revocation separately
   from root password and SSH access. Verify exposed actions either work as
   documented or reject before partial mutation. If new public actions/fields
   are needed, update API contracts and clients; a new distro row alone does not
   justify schema/client churn. An operator-owned provisioning path may avoid
   public API additions but still needs a tested node integration contract.
4. Exercise reinstall from/to the derivative with its full persistent layout;
   verify intended data retention and fresh provisioning. Verify known payload
   contents and Incus database/workload recovery after local snapshot rollback,
   remote restore and outer-node migration. Include credential/encryption state,
   external storage and supported source/target node versions.

Only the assigned findings file was written. The lead owns session state/link
updates. Stable session portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-28-incusos-compatibility-assessment/
