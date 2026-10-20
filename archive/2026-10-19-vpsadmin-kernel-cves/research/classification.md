# Architect classification reconciliation

Policy checkpoint: this document and `selection.json` preserve the initial
exposure-focused proposal. Subsequent user steering requests high-threat
member-relevant assessments even where vpsAdminOS was not affected. The revised
research is in `member-relevance.md`; these original 41 recommendations and
their source findings are retained, not silently reclassified.

Final research recommendation, 2026-10-19: **41 CVEs proposed for drafting
approval**, with 11 conditional and 9 borderline entries outside that batch.
The authoritative exact IDs are in [selection.json](selection.json). This is a
selection proposal, not advisory text or a per-node assessment. Source enumeration
belongs to [package B](cve-candidates.md); platform identity and prerequisites
belong to [package A](platform-baseline.md). No exploit was run.

## Interpretation and scope

The inclusive upstream interval is Linux 6.12.95–6.12.113. Start with the full
set and remove previously reported CVEs; the publication checkpoint is advisory
56, CVE-2026-72472 (2026-08-23). A later CVE number is not evidence that a defect
is new. Package B joined 3,493 primary Linux CNA records to exact stable commits;
19 upstream changelogs independently match those release intervals. This is a
complete mechanical join at the recorded snapshot, not a manual security audit
of all records. The manually assessed selection below is separate from the
mechanically screened remainder.

The initial 14 candidates all have a 6.12 fix inside the requested interval,
a primary affected range beginning before 6.12.95, and no entry in the public
57-CVE dedup set. Their score values below are Linux CNA CVSS 3.1 values;
“unscored” means the saved CNA record supplies no metric, not low severity.
Platform priority additionally depends on the attacker path and shared-kernel
primitive. Formal Critical is preserved as a source rating, not asserted from
our own impact judgement. Other authorities may rate the same flaw differently.

Build/source applicability is supported; exact running Node configuration,
module presence and historical mitigation are not established in this research
phase. The original frozen .95 kernel configuration was extracted with its
archive hash verified. Defaults may differ from deployed or optional profiles.
Livepatch v6 is quarantined: historical correction coverage cannot be treated as
a rollout recommendation or evidence of successful activation.

## Initial candidate decisions

The tier identifies the required access. “Ordinary process” means no tenant
administrator privilege is inherently needed. “VPS administrator” refers to
capabilities in that VPS's user/network namespace, not host privileges.
Potential escalation describes a reachable corruption primitive; it is not a
claim of a complete demonstrated exploit unless explicitly attributed.

| CVE | First fixed | CNA score | Access and primitive | Recommendation / confidence boundary |
| --- | --- | --- | --- | --- |
| [CVE-2026-99999](https://www.cve.org/CVERecord?id=CVE-2026-99999) | 6.12.113 | 9.3 Critical | Malformed checksum metadata via TUN/TAP or packet path; header corruption and subsequent unsafe parsing | Highest priority. CNA reports demonstrated microVM-to-host memory disclosure, crash and administrator code execution. A vpsAdmin container exploit was not reproduced here. TUN default delegation and namespace network capabilities support platform relevance. |
| [CVE-2026-98858](https://www.cve.org/CVERecord?id=CVE-2026-98858) | 6.12.113 | Unscored | Ordinary process using io_uring SQPOLL; task-work publication races context destruction, including a freed-memory write | Include. IO_URING enabled; no mandatory host capability for SQPOLL. Effective io_uring sysctl/LSM restrictions need later runtime verification. |
| [CVE-2026-98260](https://www.cve.org/CVERecord?id=CVE-2026-98260) | 6.12.112 | 7.8 High | Ordinary process CPU timer plus failed threaded exec; timer freed while linked, later tree removal uses freed object | Include. POSIX timers enabled and involved own-process syscalls allowed. Shared-kernel corruption supports escalation concern; no complete exploit is established by the reviewed source. |
| [CVE-2026-97594](https://www.cve.org/CVERecord?id=CVE-2026-97594) | 6.12.112 | 7.8 High | Ordinary process enters Landlock then races its own filesystem operations; stale parent dentry reads/refcount writes | Include. Landlock built and in default LSM list; no host privilege required with no_new_privs. Actual boot LSM activation remains a runtime prerequisite. |
| [CVE-2026-74632](https://www.cve.org/CVERecord?id=CVE-2026-74632) | 6.12.104 | 7.8 High | Ordinary process faults/reclaim of transparent huge zero page; shared page misidentification and unsafe split/accounting | Lower-confidence serious-impact candidate with THP/huge-zero runtime condition. Frozen .95 has THP enabled, default madvise, and dynamic huge-zero implementation. CNA describes potential kernel metadata exploitation; controlled escalation remains unresolved. |
| [CVE-2026-74668](https://www.cve.org/CVERecord?id=CVE-2026-74668) | 6.12.104 | 7.8 High | VPS administrator AF_PACKET TX_RING plus netdevice reconfiguration; inconsistent header length creates insufficient headroom/unsafe copy size | Include. Packet module preloaded; CAP_NET_RAW and relevant netdevice administration are namespace scoped. |
| [CVE-2026-80841](https://www.cve.org/CVERecord?id=CVE-2026-80841) | 6.12.111 | Unscored | VPS administrator AF_PACKET TX_RING; completion stores can outlive vmalloc-backed ring mapping | Include. Distinct from .104 headroom correction; raw packet access is available through delegated namespace capability. |
| [CVE-2026-74666](https://www.cve.org/CVERecord?id=CVE-2026-74666) | 6.12.104 | 7.8 High | VPS administrator packet ring reconfiguration; stale/NULL ring storage dereference | Retain, lower confidence on privilege gain than explicit write primitives. Reviewed primary description supports stale-pointer access; do not turn the CNA score into proven host execution. |
| [CVE-2026-74586](https://www.cve.org/CVERecord?id=CVE-2026-74586) | 6.12.104 | 9.8 Critical | SCTP association with authenticated ASCONF/address changes; stale new_transport reused for heartbeat | Include in specialised protocol group. Module preloaded; required protocol settings are tenant-netns configurable. Raw network exposure is conditional on a suitable association/configuration. |
| [CVE-2026-74587](https://www.cve.org/CVERecord?id=CVE-2026-74587) | 6.12.104 | 9.8 Critical | SCTP restart plus delayed authenticated ASCONF-ACK; stale cached chunk use and second release | Include in specialised protocol group; explicit UAF/double-release primitive. Authentication/association prerequisites remain visible despite CVSS PR:N. |
| [CVE-2026-74588](https://www.cve.org/CVERecord?id=CVE-2026-74588) | 6.12.104 | 9.8 Critical | SCTP peer removes transport then sends relevant acknowledgments; write through freed transport metadata | Include in specialised protocol group; explicit stale-object update is stronger integrity evidence than read-only crash evidence. |
| [CVE-2026-74688](https://www.cve.org/CVERecord?id=CVE-2026-74688) | 6.12.104 | 9.8 Critical | SCTP queued control chunk retains freed transport across address reconfiguration | Include in specialised protocol group; full exploit remains unestablished in reviewed materials. |
| [CVE-2026-89783](https://www.cve.org/CVERecord?id=CVE-2026-89783) | 6.12.110 | 9.8 Critical | VPS networking/XFRM setup with full secpath and Mobile IPv6 option/header; array write past xvec | Conditional host-enabled module group. Receive code is compiled with IPV6_MIP6=m, but valid DSTOPTS/routing states require XFRM types registered by mip6. It is not default-preloaded and module autoload is disabled. Once available, tenant namespace administration can configure states. Write remains inside sec_path allocation; broader controlled corruption is unresolved. |
| [CVE-2026-74746](https://www.cve.org/CVERecord?id=CVE-2026-74746) | 6.12.105 | 9.8 Critical | Flowtable GC races partially inserted flow; freed-memory read/write | Conditional host-enabled feature group. Required flowtable/offload modules are built but absent from the default preload list; module autoload is disabled by source defaults. Tenant configuration alone does not establish availability. |

## Evidence distinctions used in the table

For 99999, the CNA record's `metrics[].scenarios` is more informative than its
short description: it reports guest-supplied virtio-net metadata through a
VMM's existing TAP descriptor, host information disclosure and demonstrated
host command execution. Attribute those statements to the Linux CNA. Neither
the report nor our source inspection alone proves the same exploit on the
vpsAdminOS build and hardening configuration. The supplied 9.3 score assesses
that microVM scenario and must not be silently presented as a bespoke vpsAdmin
container score.

For Landlock, the CNA scenario explains lockref writes and dentry teardown
through a stale parent, beyond its KASAN read report. For io_uring the primary
report includes a freed-memory write in queue_work_on. For POSIX timers the
released object remains in a mutable tree. These details support priority for
further advisory assessment without inventing exploit reliability.

SCTP is preloaded by the inspected source, but addip/authentication settings
are off by default and are per-network-namespace. Thus a tenant administrator
can arrange the relevant protocol state. This differs materially from requiring
a host administrator to enable an unavailable module. A malicious peer still
needs the association and message sequence stated in the CVE; CVSS AV:N does
not mean every Internet packet can reach it.

A build-only “MIP6 is a module, therefore the receive code is absent” shortcut
is invalid for 89783: IS_ENABLED(CONFIG_IPV6_MIP6) includes that code for a
module selection too. Package A's subsequent path review establishes the
decisive additional gate: the matching valid DSTOPTS/routing XFRM state needs
the types registered by mip6. The module is absent from the default preload
list and automatic loading is denied by default. Thus it joins the conditional
host-enabled group; it does not join default tenant-reachable XFRM solely
because receive call sites exist. Actual loaded-module evidence remains absent.

## Additional historical candidates: accepted selection

The six rows below are accepted additions to the main proposal. Together with
six strong default-surface entries and four SCTP entries in the initial table,
this establishes **16 recommended CVEs** before the later-release expansion.
All six are new to the public dedup set and were previously unassigned entries
in the historical livepatch document. Source SHA mappings and exact prerequisites
are in package A's historical-fix table and JSON; their primary records were
also read during architect reconciliation.

| CVE | First fixed | CNA CVSS 3.1 | Serious primitive / relevant tenant path |
| --- | --- | --- | --- |
| [CVE-2026-74730](https://www.cve.org/CVERecord?id=CVE-2026-74730) | 6.12.104 | 9.8 Critical | NFSv4.1+ delayed FREE_STATEID uses a freed nfs_server. Tenant administrator can mount a controlled server through downstream user-namespace NFS support; client modules are preloaded. |
| [CVE-2026-74724](https://www.cve.org/CVERecord?id=CVE-2026-74724) | 6.12.104 | 7.8 High | IPVS ICMP NAT writes outside the validated area when locally mutable packet fields race repeated reads. Preloaded IPVS and tenant namespace network administration; needs matching NAT state and mutable packet producer. |
| [CVE-2026-74669](https://www.cve.org/CVERecord?id=CVE-2026-74669) | 6.12.104 | 9.8 Critical | IPVS tunnel ICMP processing reuses stale option offsets and can overflow fixed stack option storage. Requires configured IPVS tunnel traffic and crafted ICMP, not arbitrary unrelated traffic. |
| [CVE-2026-74656](https://www.cve.org/CVERecord?id=CVE-2026-74656) | 6.12.104 | 7.8 High | MTU updates race freed IPv4 nexthop exceptions, including stale PMTU field writes. Tenant administrator controls own network-device MTU and traffic. |
| [CVE-2026-74630](https://www.cve.org/CVERecord?id=CVE-2026-74630) | 6.12.104 | 7.8 High | IPv6 device reference resurrection permits a freed-object mutex write during multicast/device teardown. Tenant administrator controls own device lifecycle. |
| [CVE-2026-74615](https://www.cve.org/CVERecord?id=CVE-2026-74615) | 6.12.104 | 8.8 High | VXLAN timer remains queued after a never-up device is freed; timer processing writes through freed list links. VXLAN is preloaded, and tenant administrator can create/change/delete the device without a live VXLAN deployment. |

The historical scan also yields **CVE-2026-74597** (.104, 9.8 Critical), kept
conditional: stale HAO metadata in IPv6 tunnel ICMP can corrupt skb_shared_info.
The frozen kernel has IPV6_TUNNEL=y, so an earlier suggestion that an absent
ip6_tunnel module blocks the path is superseded. Required valid outer HAO/XFRM
state still depends on mip6 type registration, which is not default-preloaded.
Keep the conditional mip6 gate visible rather than claiming default exposure.

**CVE-2026-74598** (.104, 7.5 High; up to eight bytes disclosed through an
IPv6 route prefix) and **CVE-2026-80717** (.103, 7.5 High; four receive-buffer
bytes returned in an SCTP INIT ACK cookie) stay outside the escalation-focused
main list as disclosure-only borderline cases. These are separate defects,
not covered by the SCTP transport UAF proposals.

No CVE assignment was found for the historical GRE/PPTP keymap correction
(upstream b0f02608, first stable .97) or bridge-netfilter headroom correction
(upstream b2870fc, first stable .103) within the pinned 17,817 published and
322 rejected record snapshots. They remain in the non-CVE appendix; this is a
snapshot-scoped search result, not a claim that assignment cannot exist later.

## Accepted KVM additions

These five additions bring the current main proposal to **23 CVEs**. KVM is a
default-enabled tenant feature with /dev/kvm delegated, rather than a host-only
surface. Intel-specific nested virtualization cases apply only to matching
hardware and enabled nested features; neither the default nor exact CPU state
has been measured on running nodes. CVSS scenarios describe potential
cross-VM effects; no platform exploit was executed.

| CVE | First fixed | CNA CVSS 3.1 | Primitive / required configuration |
| --- | --- | --- | --- |
| [CVE-2026-74517](https://www.cve.org/CVERecord?id=CVE-2026-74517) | 6.12.105 | 9.3 Critical | Delayed emulated I/O APIC EOI work outlives VM/vCPU destruction, dereferencing freed vCPU state while delivering interrupts. Tenant VMM controls VM creation/run/teardown and emulated irqchip. |
| [CVE-2026-89929](https://www.cve.org/CVERecord?id=CVE-2026-89929) | 6.12.110 | 8.8 High | Intel nested VMX invalidates VPID on the wrong physical CPU after migration, leaving stale translations. Requires nested VMX/VPID and tenant-controlled L1/L2 execution. |
| [CVE-2026-89930](https://www.cve.org/CVERecord?id=CVE-2026-89930) | 6.12.110 | 9.3 Critical | Failed nested VM entry updates tracked VPID without servicing required TLB invalidations, retaining stale read/write mappings across a later entry. Intel nested VMX path. |
| [CVE-2026-89932](https://www.cve.org/CVERecord?id=CVE-2026-89932) | 6.12.110 | 8.8 High | First use of a recycled nested VPID may use translations from an earlier vCPU or another VM. Explicit cross-VM stale-mapping primitive; Intel nested VMX and reuse conditions required. |
| [CVE-2026-98720](https://www.cve.org/CVERecord?id=CVE-2026-98720) | 6.12.113 | Unscored | Stale enlightened-VMCS MSR bitmap permits nested guest reads/writes of L0 TPR after toggling TPR virtualization. This is a concrete host-state boundary violation, not independently proven arbitrary host execution. KVM_HYPERV=y and tenant VMM can enable eVMCS through normal capability ioctl; Intel nested VMX runtime required. |

## Decisions outside the main proposal

BPF **CVE-2026-98041** is deferred: source enables unprivileged BPF, but the
reviewed verifier still validates a speculative alternate path unless
bypass_spec_v1 applies (mitigations disabled or initial-namespace/token
CAP_PERFMON). The proposed ordinary-user bypass was not established through
that gate. **CVE-2026-63823** is deferred pending an accessible host request-key
helper/authentication context; tenant keyctl availability alone does not suffice.
**CVE-2026-98573** is deferred because its skb producer path lacks specific
platform confirmation.

**CVE-2026-98503** is borderline: the source establishes early TX_RING payload
reuse, but effect beyond attacker-owned packet bytes is unresolved here.
**CVE-2026-98222** is conditional on a host-registered encrypted-key type;
it is compiled as an unpreloaded module with automatic loading disabled.
The asymmetric-key case **63824** is separate and is accepted below because its
public-key path is built in.

Nineteen NFSD/SUNRPC host-service records and six privileged-BPF records from
package B remain deferred unless a real service or initial-namespace delegation
path is established. They are research leads, not a blanket conditional approval
request. Package B and the supplemental ledger retain exact IDs and reasons.

## Accepted follow-up additions and final impact distinctions

Twelve further additions bring the accepted main proposal to **35 CVEs**,
before the completed supplemental additions below. Primary descriptions
were read and package A's candidate-specific source gates were reconciled.

| CVE | First fixed | CNA CVSS 3.1 | Accepted reason / condition |
| --- | --- | --- | --- |
| CVE-2026-63824 | 6.12.95 | 7.8 High | Asymmetric-key operation allocates output using too-small caller size, enabling heap overflow. Built-in asymmetric/RSA/X509 support and own searchable public-key encryption give a tenant path without initial-namespace capabilities. Already fixed in .95; inclusive boundary inclusion does not imply .95 vulnerability. |
| CVE-2026-74753 | 6.12.108 | 7.8 High | Perf accepts an exited group leader, leaving a freed leader pointer. Own per-task exclude-kernel events work under source default paranoid=2. The affected stable interval starts .96 and ends .108, so .95 is not affected. Actual perf policy remains unmeasured. |
| CVE-2026-93817 | 6.12.111 | 7.8 High | Perf address-filter range array is freed before RCU users finish; CNA describes subsequent range reads/writes. Requires Intel PT PMU on this x86 platform and permissive per-task perf policy. Ordinary software perf alone does not reach it. |
| CVE-2026-74662 | 6.12.106 | 9.8 Critical | Fragment timeout before hash publication creates a stale queue node. Namespace administrator can set zero/negative fragment timeout and drive fragments; nondefault timeout is tenant configurable. |
| CVE-2026-80725 | 6.12.106 | 9.8 Critical | BIG TCP GRO accepts insufficient pre-MAC room, then memmove writes before skb head. Tenant network administrator can raise own device GRO_MAX_SIZE and arrange packet geometry; not default generic network traffic. |
| CVE-2026-89478 | 6.12.109 | 9.8 Critical | SCTP receive republishes a removed transport into last_data_from; later SACK follows freed state. Requires association/authenticated ASCONF and tenant-enabled protocol configuration. |
| CVE-2026-89479 | 6.12.109 | 9.8 Critical | Bundled SCTP chunks delete an association then write through the freed transport. Own listener/peer and socket backlog suffice; the described path does not require ADDIP. |
| CVE-2026-98586 | 6.12.112 | Unscored | SCTP timer rearming before holding its lifetime reference permits refcount operations on freed association/transport. Own endpoint lifecycle; ADDIP not established as a prerequisite. |
| CVE-2026-72463 | 6.12.112 | 9.8 Critical | XFRM asynchronous receive changes skb device without balancing references, causing device UAF. Built-in XFRM interface callback provides a tenant path without requiring the unpreloaded VTI module; async crypto and interface lifecycle conditions apply. |
| CVE-2026-98229 | 6.12.112 | 7.8 High | XFRM secpath reset can free the current state before protocol/type dereferences finish. Built-in XFRM interfaces, cross-netns path or depth-error path qualify; tenant controls states and own namespaces. |
| CVE-2026-98368 | 6.12.112 | 7.8 High | ESP out-of-place output mishandles managed zerocopy fragment ownership and prematurely releases pinned pages. Built-in ESP and tenant IPsec setup with appropriate zerocopy/crypto path; runtime io_uring restrictions still apply. |
| CVE-2026-98370 | 6.12.112 | Unscored | Compat XFRM ALLOCSPI adds then frees shared request child while receiver copies it, causing UAF and overread. COMPAT/IA32 and XFRM_USER_COMPAT are built; namespace network administration plus 32-bit messages/receiver required. |

**CVE-2026-74705** (.104, CNA 10.0 Critical) remains a lower-confidence
candidate: the reviewed stable patch moves the UDP-header pointer after a
potentially reallocating pull; observed direct stale-pointer consumers read
length/checksum. The possible surrounding packet effects is not
established here as controlled host compromise. Tenant tunnel/GSO access is
supported, but the formal score alone does not close the impact question.

**CVE-2026-98369** (.112, 7.8 High) also remains lower-confidence: missing
RCU, destination and device references on deferred XFRM reinjection create a
credible lifetime hazard; the primary report shows an RCU warning rather than
a controlled corruption/exploit. It is not in the main proposal.

**CVE-2026-98573** is deferred because the required skb producer path has not
received candidate-specific platform confirmation. No unreviewed assumption is
used to expand the main list.

## Final supplemental decisions

The assigned supplemental screen is complete. Six additional candidates bring
the final main proposal to **41 CVEs**. These have primary serious-impact
mechanisms and candidate-specific tenant access reviewed by package A.

| CVE | First fixed | CNA CVSS 3.1 | Accepted reason / required setup |
| --- | --- | --- | --- |
| CVE-2026-68159 | 6.12.105 | 9.8 Critical | Malicious accepted Ceph OSDMap placement list overflows a fixed stack array. CephFS user-namespace mounts and preloaded libceph reach the shared mapper; the RBD reproducer does not require a tenant block device. |
| CVE-2026-89653 | 6.12.109 | 9.8 Critical | Monitor MDSMap export-target rank becomes an unchecked bit index in a fixed stack bitmap. Requires controlled CephFS monitor and applicable MDS session/map transition. |
| CVE-2026-89656 | 6.12.109 | 9.8 Critical | Malformed CRUSH bucket IDs alias smaller workspace and cause a write past its allocation during placement. Tenant-controlled CephFS cluster maps/OSD operation; not arbitrary unauthenticated packets. |
| CVE-2026-80714 | 6.12.103 | 9.8 Critical | IPVS synced connection inherits ONE_PACKET and expires without unhashing, leaving freed connection nodes. Namespace-scoped sync configuration is tenant-accessible; imported connection/destination order and expiry are required. |
| CVE-2026-74581 | 6.12.103 | 9.8 Critical | Suppressed IPv6 route remains returned after release, leading to stale route use and another reference put. Tenant policy rules and matching traffic can arrange the no-replacement condition. |
| CVE-2026-90151 | 6.12.110 | 9.8 Critical | Failed NFSv4.0 client initialization leaves callback IDR pointing to freed client; callback lookup writes its refcount. Tenant-controlled userns NFS mount and callback namespace qualify. Requires failure after IDR insertion and stale-id callback; reliable induction and escape were not tested. |

**CVE-2026-72251** (.97, 9.8 Critical) is borderline rather than main. SIP NAT
retains a stale data pointer after cloned-skb reallocation, but the CNA scoring
narrative invokes a TCP rewrite path that the primary fix explicitly regards
as not expected to be reachable. The reviewed source excludes fragmentation
here because SIP conntrack linearizes packets. Tenant NAT/helper access is
supported; precise stronger integrity consequence is unresolved. Do not inherit
the score's broad exploit claim without resolving that source inconsistency.

The six other Ceph leads have explicit dispositions:

| CVE | Decision and basis |
| --- | --- |
| CVE-2026-89649 | Borderline disclosure: attacker-controlled xattr length copies adjacent kernel heap to userspace. More substantial than a fixed four-byte leak, but the reviewed evidence establishes disclosure rather than write/escape; outside present escalation-focused main list. |
| CVE-2026-80558 | Deferred impact: invalid OSD indices cause out-of-bounds array reads; stronger isolation consequence not established. |
| CVE-2026-89650 | Deferred impact: export-target decode overread stores values internally; primary explicitly does not establish disclosure to attacker. |
| CVE-2026-89651 | Deferred impact: large session-string overread leads to kernel crash; primary supports availability, not controlled overwrite. |
| CVE-2026-89655 | Deferred impact: flushing-cap list traversal uses freed entry after lock release; stronger controlled integrity effect is unqualified. |
| CVE-2026-89990 | Deferred impact: auth-array traversal races session replacement/free; primary shows a fault in access checking, without a qualified wider privilege-gain path. |

Seven CIFS candidates are **conditional on a host-prepared/delegated mount**:
CVE-2026-64383, 64384, 64385, 64386, 64387 and 64597 (all first fixed
**6.12.96**, replay response double frees), plus CVE-2026-89633 (.113,
server-controlled SMB1 DataOffset heap read/write). Exact .95 and .113 CIFS/SMB3
filesystem declarations lack FS_USERNS_MOUNT, so tenant namespace root cannot
create these kernel mounts. Preloading the module is insufficient. 89633 also
requires negotiated SMB1; legacy support exists in the inspected build/defaults.
The earlier informal .97 attribution for 64597 is corrected to primary .96.

## Final proposal and evidence limits

[selection.json](selection.json) is the authoritative exact decision/ID/score/
fix-SHA list: **41 recommended, 11 conditional host-enabled, 9 borderline,
and 8 explicitly deferred leads**. Only the 41 recommended entries are the
present proposed drafting batch. Conditional and borderline entries require
separate selection; user approval has not been supplied for any draft.

The primary stable-fix join covers all 19 inclusive releases: 3,493 CVEs, of
which 48 are already reported and 3,445 are new. Package B examined 109 new
records. The supplemental screen accounts for 223 different CNA Critical
records, including 15 prior reports and 208 new records. Therefore **317 new
records received focused screening and 3,128 new records remain mechanical-
only/unresolved**, mainly High/unscored. Per-record accounting and focused
source inspection are not a comprehensive manual audit or proof that every
relevant CVE has been identified.

All proposed IDs were matched to primary stable fix evidence and the complete
public 57-CVE dedup set. No new drafts, service writes, commits, kernel builds,
exploit execution or deployment occurred. Private pre-existing drafts and
current node mitigation/activation remain unknown from public/source evidence.
No automatic final change review is triggered by these research findings.

Before any advisory preparation, the user selects/approves the CVEs. The next
phase must establish exact affected/mitigated node histories and resolve relevant
runtime prerequisites through the repository's supported evidence workflow.
This research is complete within the stated screening scope; leave the session
open for that approval and follow-up.
