# Kernel CVEs proposed for assessment

**Proposed batch: 60 CVEs.** This follows the clarified policy: serious threats can merit an advisory explaining why vpsAdminOS was not affected. Selection value is separate from platform exposure. No advisory dossier or vpsAdmin draft has been prepared.

The proposal retains the original 41 tenant-path candidates and adds 19 cases: five informative exact-build exclusions, three privileged-program cases, and eleven cases previously conditional on a host feature or prepared mount. The previous [proposal](selection-for-approval.md) and [selection ledger](research/selection.json) are retained as the policy-version-1 checkpoint.

The latest published advisory is #56, **CVE-2026-72472**, published on 23 August 2026. All 57 known published CVEs were checked for duplicates. The inclusive first-fix range is **6.12.95 through 6.12.113**; a fix shipped in 6.12.95 does not mean that release remained vulnerable. Introduction boundaries and later corrective fixes are retained in the evidence.

Scores are Linux CNA CVSS 3.1 ratings where supplied. A High or unscored defect can still qualify through a supported serious primitive. A Critical score alone does not prove host escape. These are research selections; exact node exposure and history need the repository assessment workflow after approval.

## Retained serious tenant-path candidates (41)

| CVE / primary source | First fixed | CNA score | Why it is useful / relevant exposure condition |
| --- | --- | --- | --- |
| [CVE-2026-53388](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-53388.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.95 | 7.8 High | FUSE abort/copy race uses freed request data; delegated FUSE device and user-namespace mount. |
| [CVE-2026-63824](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-63824.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.95 | 7.8 High | Asymmetric-key operation overflows a heap output buffer; built-in public-key/RSA path. |
| [CVE-2026-74581](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-74581.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.103 | 9.8 Critical | Suppressed IPv6 route result retains a freed pointer and is released again; tenant routing rules. |
| [CVE-2026-80714](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-80714.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.103 | 9.8 Critical | IPVS synced one-packet connection is freed while still hashed; tenant-configured synchronization and expiry sequence. |
| [CVE-2026-74586](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-74586.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.104 | 9.8 Critical | SCTP ASCONF transport pointer survives removal; tenant-enabled ADDIP/auth and address changes. |
| [CVE-2026-74587](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-74587.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.104 | 9.8 Critical | SCTP peer restart and delayed ASCONF-ACK use and release a freed cached chunk. |
| [CVE-2026-74588](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-74588.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.104 | 9.8 Critical | SCTP acknowledgement updates a freed transport after authenticated address removal. |
| [CVE-2026-74615](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-74615.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.104 | 8.8 High | VXLAN timer writes through freed list links; tenant-created device need not have carried live VXLAN traffic. |
| [CVE-2026-74630](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-74630.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.104 | 7.8 High | IPv6 multicast/device teardown can resurrect a freed device and write through it. |
| [CVE-2026-74656](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-74656.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.104 | 7.8 High | IPv4 MTU updates access freed nexthop exceptions; tenant-controlled MTU/routes and traffic. |
| [CVE-2026-74668](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-74668.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.104 | 7.8 High | AF_PACKET TX_RING headroom race causes out-of-bounds access; tenant network capabilities. |
| [CVE-2026-74669](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-74669.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.104 | 9.8 Critical | IPVS tunnel ICMP handling reuses stale IPv4 option offsets and overwrites stack storage. |
| [CVE-2026-74688](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-74688.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.104 | 9.8 Critical | Queued SCTP control chunk retains a freed transport across address changes. |
| [CVE-2026-74724](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-74724.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.104 | 7.8 High | IPVS ICMP NAT can write out of bounds with matching state and locally mutable packet fields. |
| [CVE-2026-74730](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-74730.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.104 | 9.8 Critical | NFSv4.1+ FREE_STATEID uses a freed server object; tenant mount of a controlled server. |
| [CVE-2026-68159](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-68159.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.105 | 9.8 Critical | Controlled Ceph OSDMap length overwrites a fixed stack array; tenant CephFS mount and placement operation. |
| [CVE-2026-74517](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-74517.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.105 | 9.3 Critical | Delayed KVM IOAPIC interrupt work outlives its vCPU; delegated KVM with emulated irqchip. |
| [CVE-2026-74662](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-74662.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.106 | 9.8 Critical | Fragment queue timer fires before publication, leaving a stale hash entry; tenant sets nondefault timeout. |
| [CVE-2026-80725](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-80725.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.106 | 9.8 Critical | BIG TCP GRO writes before the packet head; tenant-enabled large aggregation and specific packet geometry. |
| [CVE-2026-74753](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-74753.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.108 | 7.8 High | Perf accepts a freed event-group leader; own per-task events under suitable perf policy. Affected 6.12.96–6.12.107. |
| [CVE-2026-89478](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-89478.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.109 | 9.8 Critical | SCTP receive republishes a removed transport; association, ADDIP/auth and receive timing required. |
| [CVE-2026-89479](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-89479.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.109 | 9.8 Critical | Bundled SCTP chunks delete an association then access freed state; suitable endpoint/peer traffic. |
| [CVE-2026-89653](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-89653.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.109 | 9.8 Critical | Controlled Ceph MDS export rank sets a bit outside a stack bitmap; tenant CephFS mount/session transition. |
| [CVE-2026-89656](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-89656.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.109 | 9.8 Critical | Malformed CRUSH bucket IDs select undersized workspace and cause an out-of-bounds write; controlled Ceph monitor. |
| [CVE-2026-89929](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-89929.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.110 | 8.8 High | Nested Intel VMX invalidates translations on the wrong CPU; nested VMX/VPID required. |
| [CVE-2026-89930](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-89930.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.110 | 9.3 Critical | Failed nested Intel VM entry skips required TLB flushes and retains stale mappings. |
| [CVE-2026-89932](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-89932.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.110 | 8.8 High | Recycled nested VPID can reuse mappings from another vCPU or VM; Intel nested VMX/VPID. |
| [CVE-2026-90151](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-90151.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.110 | 9.8 Critical | Failed NFSv4.0 client initialization leaves a freed callback IDR entry; controlled server and failure/callback timing. |
| [CVE-2026-80521](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-80521.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.111 | 7.8 High | AF_UNIX descriptor-passing garbage collection traverses freed graph entries; ordinary processes. |
| [CVE-2026-80841](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-80841.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.111 | Not supplied | Packet transmit completion writes after vmalloc TX_RING storage is freed; tenant raw-packet access. |
| [CVE-2026-93817](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-93817.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.111 | 7.8 High | Perf address-filter ranges freed before readers/writers finish; Intel PT hardware and suitable perf policy. |
| [CVE-2026-72463](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-72463.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.112 | 9.8 Critical | Asynchronous XFRM receive mishandles device references; configured IPsec/XFRM interface and lifecycle race. |
| [CVE-2026-97594](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-97594.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.112 | 7.8 High | Landlock parent-dentry race permits stale pointer/refcount operations; Landlock must be active. |
| [CVE-2026-98229](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-98229.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.112 | 7.8 High | XFRM secpath reset frees a state before later dereferences; configured interfaces/namespaces or depth-error path. |
| [CVE-2026-98260](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-98260.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.112 | 7.8 High | Failed threaded exec leaves a freed CPU timer linked in a tree; ordinary process operations. |
| [CVE-2026-98368](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-98368.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.112 | 7.8 High | ESP zerocopy output prematurely releases managed pages; specific crypto and managed-fragment path. |
| [CVE-2026-98370](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-98370.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.112 | Not supplied | 32-bit compat XFRM ALLOCSPI translation races shared request storage; namespace network administration. |
| [CVE-2026-98586](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-98586.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.112 | Not supplied | SCTP timer rearm races lifetime references; endpoint and transport cleanup. |
| [CVE-2026-98720](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-98720.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.113 | Not supplied | Stale eVMCS MSR bitmap permits access to host TPR state; Intel nested VMX and eVMCS. |
| [CVE-2026-98858](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-98858.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.113 | Not supplied | io_uring SQPOLL task-work lifetime race includes writes to freed kernel objects; effective io_uring/LSM policy matters. |
| [CVE-2026-99999](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-99999.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.113 | 9.3 Critical | Malformed TUN/TAP or packet checksum metadata corrupts IPv4 processing. CNA reports microVM-to-host execution; vpsAdmin exploit not reproduced. |

## Informative exclusions for the exact archived build (5)

The necessary feature is absent in the **exact archived 6.12.95 build**. This supports a not-affected conclusion for that build only. It does not establish that every node or historical interval used it; later dossier evaluation must bind the claim to actual node/build history.

| CVE / primary source | First fixed | CNA score | Why it is useful / relevant exposure condition |
| --- | --- | --- | --- |
| [CVE-2026-53260](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-53260.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.97 | 9.8 Critical | TCP request-queue protection on PREEMPT_RT kernels. The exact archived 6.12.95 build is not PREEMPT_RT. |
| [CVE-2026-72069](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-72069.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.101 | 9.8 Critical | Incorrect RCU protection in RT spinlock unlock. The exact archived 6.12.95 build is not PREEMPT_RT. |
| [CVE-2026-80585](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-80585.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.105 | 9.4 Critical | MPTCP Fast Open subflow state/data handling. MPTCP is disabled in the exact archived 6.12.95 build. |
| [CVE-2026-80586](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-80586.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.105 | 9.8 Critical | Malformed MPTCP DSS option state. MPTCP is disabled in the exact archived 6.12.95 build. |
| [CVE-2026-80587](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-80587.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.105 | 9.8 Critical | Conflicting incoming MPTCP suboptions. MPTCP is disabled in the exact archived 6.12.95 build. |

## Serious privileged-program cases (3)

Container user-namespace root does not automatically have the required initial-user-namespace or BPF-token authority. Existing host programs, explicit tokens and runtime configuration remain unmeasured; these are useful assessments of a serious threat, not a claim of ordinary unprivileged access.

| CVE / primary source | First fixed | CNA score | Why it is useful / relevant exposure condition |
| --- | --- | --- | --- |
| [CVE-2026-63830](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-63830.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.95 | 9.4 Critical | SK_MSG can modify shared file-backed pages. Requires the relevant privileged BPF program, host attachment or delegated authority. |
| [CVE-2026-74616](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-74616.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.104 | 9.8 Critical | XDP clone metadata/tailroom corruption. Requires the relevant privileged XDP redirect program and packet geometry. |
| [CVE-2026-98039](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-98039.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.111 | Not supplied | Per-CPU kptr type confusion permits kernel read/write or invalid free. Requires the relevant privileged BPF program/map/kfunc authority. |

## Host feature or prepared-mount cases (11)

These cases are worth assessing under the clarified policy even though the tenant trigger is not established by default. A missing sample is not proof of non-exposure. CIFS is preloaded but cannot be mounted by the inspected tenant user namespace; its cases need a host-prepared or delegated mount.

| CVE / primary source | First fixed | CNA score | Why it is useful / relevant exposure condition |
| --- | --- | --- | --- |
| [CVE-2026-64383](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-64383.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.96 | 9.8 Critical | SMB2 replay double free; requires a host-prepared or otherwise delegated CIFS mount, not ordinary tenant mount capability. |
| [CVE-2026-64384](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-64384.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.96 | 9.8 Critical | SMB2 replay double free; requires a host-prepared or otherwise delegated CIFS mount, not ordinary tenant mount capability. |
| [CVE-2026-64385](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-64385.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.96 | 9.8 Critical | SMB2 replay double free; requires a host-prepared or otherwise delegated CIFS mount, not ordinary tenant mount capability. |
| [CVE-2026-64386](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-64386.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.96 | 9.8 Critical | SMB2 replay double free; requires a host-prepared or otherwise delegated CIFS mount, not ordinary tenant mount capability. |
| [CVE-2026-64387](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-64387.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.96 | 9.8 Critical | SMB2 replay double free; requires a host-prepared or otherwise delegated CIFS mount, not ordinary tenant mount capability. |
| [CVE-2026-64597](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-64597.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.96 | 9.8 Critical | SMB2 replay double free; requires a host-prepared or otherwise delegated CIFS mount, not ordinary tenant mount capability. |
| [CVE-2026-74597](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-74597.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.104 | 9.8 Critical | IPv6 tunnel error handling consumes stale HAO metadata; tunnel is built in, but required mip6 types are not preloaded. |
| [CVE-2026-74746](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-74746.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.105 | 9.8 Critical | Flowtable publication/GC race causes use-after-free; host-enabled flowtable/offload modules required. |
| [CVE-2026-89783](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-89783.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.110 | 9.8 Critical | Mobile IPv6/XFRM secpath out-of-bounds state-pointer write; host must make mip6 types available. |
| [CVE-2026-98222](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-98222.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.112 | Not supplied | Encrypted-key allocation truncation causes a large heap write; encrypted_keys module must be registered by host. |
| [CVE-2026-89633](https://git.kernel.org/pub/scm/linux/security/vulns.git/plain/cve/published/2026/CVE-2026-89633.json?id=56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9) | 6.12.113 | 9.8 Critical | SMB1 server-controlled DataOffset permits heap read/write; host-prepared CIFS mount and legacy dialect negotiation. |

## What the proposal establishes

Candidate relevance, exact upstream fixes and scoped source prerequisites have been checked. None of the proposed CVEs overlaps the public 57-CVE prior-report set. The previous 41 entries remain unchanged. Private existing drafts are still outside the anonymous dedup view and must be checked before later draft creation.

For CVE-2026-99999, the Linux CNA reports demonstrated host disclosure and code execution in a microVM-to-TAP setup. This is attributed to that scenario; this research did not reproduce a vpsAdmin container escape. Other lifetime, corruption and isolation primitives are described according to their evidence, without claiming a complete exploit.

Current kernel mitigation and historical non-exposure are separate. Source defaults and the archived build do not establish current node sysctls, LSMs, loaded modules, devices, service roles, CPU features, mounts or livepatch activation. Historical livepatch v6 is quarantined and this proposal gives no recommendation to activate it.

The range join covers 3,493 CNA records across all 19 releases. The focused and supplemental screens account for 317 new records; 3,128 new records remain mechanical-only and unresolved, mainly High or unscored. This proposal is a prioritised selection, not a full manual audit or a claim that the rest are safe.

## Supporting records

- [Revised exact selection and independent exposure fields](research/member-selection.json)
- [Revised member relevance and control decisions](research/member-classification.md)
- [Bounded informative-negative/conditional evidence](research/member-relevance.md)
- [Platform gates and archived build evidence](research/platform-baseline.md)
- [Complete source range and focused screening](research/cve-candidates.md)
- [Supplemental Critical-rated screen](research/supplemental-critical.md)
- [Original borderline/deferred reasoning](research/classification.md)

Approval of the exact selected IDs authorizes the next dossier/draft phase within that scope. It does not approve publication, email, deployment or repository integration. The repository procedure and existing evidence contract govern later per-node evaluation and draft synchronisation.
