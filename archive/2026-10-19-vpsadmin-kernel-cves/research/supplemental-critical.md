# Supplemental CNA Critical screen

Completed by implementer2 on 2026-10-19. Research only; no advisory/draft,
application edit, commit, branch, build, exploit, deployment or external write.
The architect owns final impact/selection decisions; the lead owns approval.

## Bounded accounting

The pinned Linux CNA/stable join contains 3,493 records first corrected in
6.12.95–6.12.113. **269** have a Linux CNA CVSS metric of at least 9.0.
**46** are already in the existing 109-record manual screen and were not
re-audited here. This package accounts for the remaining **223**: **15** are
already publicly reported and **208** are new to this bounded screen.

All 223 have a disposition in [dispositions.json](supplemental-critical-evidence/dispositions.json),
with primary URL, exact stable SHA/release, full supplied metrics, source refs
where reviewed, primitive excerpt, reason and evidence limit. The full retained
input rows are in [critical-remainder.json](supplemental-critical-evidence/critical-remainder.json).
[Summary/checks](supplemental-critical-evidence/summary.json) and
[reproducible disposition script](supplemental-critical-evidence/dispose.py)
record zero missing dispositions, zero duplicate IDs and zero overlap with
manual109. Range membership and the CNA snapshot were reused from package B;
no duplicate download or complete range revalidation was needed.

This is a focused Critical-only omission screen, with primary descriptions and
candidate-specific source checks plus subsystem/configuration screening. It is
**not** an exhaustive manual audit of the 3,493 records, the High/unscored
remainder, other CNAs, or production exposure. Unknowns remain unknown.

## Seven strong additional leads

These are proposals for architect reconciliation, not automatic additions to
an approved list. Exact source gates are independently reconciled in
[the platform baseline](platform-baseline.md). Each ID links to its current
primary record through the machine-readable ledger.

| CVE | First fix | Specific primitive | Tenant prerequisite and uncertainty |
| --- | --- | --- | --- |
| CVE-2026-68159 | 6.12.105 | Monitor-controlled OSDMap pg_temp/upmap length exceeds 32 and copies into fixed stack ceph_osds array | Tenant admin can mount a controlled CephFS cluster: exact .95 FS_USERNS_MOUNT and Ceph/libceph preload confirmed. Primary reproducer uses RBD, while shared libceph placement logic is relevant to CephFS; exact CephFS trigger untested. |
| CVE-2026-89653 | 6.12.109 | Monitor-controlled MDS export rank is used as a bit number beyond a fixed stack bitmap | Same tenant CephFS mount gate; specific malformed map. Out-of-bounds set_bit is source-described, host execution unverified. |
| CVE-2026-89656 | 6.12.109 | Malformed CRUSH bucket ID aliases another bucket's smaller workspace; permutation write escapes workspace | Same tenant CephFS/controlled monitor gate. KASAN reports a four-byte OOB write; exploit control/reliability untested. |
| CVE-2026-80714 | 6.12.103 | Synced IPVS connection inherits ONE_PACKET and expiry frees it without removing its hash node | IPVS/schedulers preloaded. NEW_DAEMON/destination commands use GENL_UNS_ADMIN_PERM and netnsok=true; tenant configures own synchronization backup and late destination. Freed hash-node primitive, no demonstrated escape. |
| CVE-2026-74581 | 6.12.103 | Suppressed IPv6 rule drops a route but returns its stale pointer, followed by another put | Built IPv6, tenant network admin controls suppressing rules/routes. Exact freed-object reuse and escalation remain untested. |
| CVE-2026-72251 | 6.12.97 | SIP NAT helper keeps a data pointer across reallocation of a cloned skb | SIP NAT/conntrack helpers preloaded; tenant namespace helper/NAT configuration and cloned traffic. Primary discounts fragmented input and the expected TCP branch; complete exploitation unverified. |
| CVE-2026-90151 | 6.12.110 | Failed NFSv4.0 client initialization leaves callback IDR pointer; later lookup references freed nfs_client | Downstream tenant NFS mount support/client preload, controlled server, allocation-failure and callback timing. No platform trigger/exploit run. |

**CVE-2026-74669** is also outside manual109, but was already accepted in the
architect's historical IPVS proposal. Its ledger disposition is
`already-in-existing-proposal`; it is not an eighth new lead.

## Six qualified Ceph leads

The exact six IDs in `additional-qualified-tenant-lead` are
**CVE-2026-80558, CVE-2026-89649, CVE-2026-89650, CVE-2026-89651,
CVE-2026-89655 and CVE-2026-89990**. Tenant-controlled CephFS mounts and
preloaded modules support further assessment. Primary descriptions respectively
identify invalid OSD-index OOB access, oversized final xattr value, MDS-map
export-array overread, MDS-capability string overread, flushing-cap list UAF
read, and cap-authorization-array UAF read. Their stronger confidentiality or
integrity consequences need individual assessment. This category does not
assert arbitrary read/write, a demonstrated escape, or final eligibility.

The separate libceph locker/watcher decoders **68082, 80561 and 80557** remain
`unknown-tenant-api`: ordinary CephFS mountability alone does not establish
that the RBD/class-method caller is available. **89652** requires CephFS NFS
re-export. These were not silently promoted with the other Ceph leads.

## Conditional and excluded paths

The ledger keeps these distinctions explicit:

- **14 CIFS client records** require an operator-prepared or delegated mount.
  CIFS is compiled/preloaded, and legacy dialects are compiled/default allowed,
  but cifs/smb3 lack FS_USERNS_MOUNT in the exact .95 source. Generic superblock
  creation refuses tenant-userns mounts. The six SMB2 replay double-frees
  **64383–64387 and 64597** are all first corrected in **6.12.96** (an early
  peer message mistakenly placed 64597 in .97; the retained join is authoritative).
  The explicit SMB1 DataOffset OOB read/write **89633** is fixed in .113 and
  additionally needs legacy negotiation/runtime allowance. These are meaningful
  conditional host-mount leads, not default tenant-mount findings.
- **28 specialised module/feature rows**, **6 RDMA rows**, **10 filesystem/device
  rows**, plus SEV, vhost and re-export cases retain exact availability questions.
  Built `m` is insufficient where default autoload is disabled and the module
  is absent from the preload list. Device and mount delegation are separate gates.
- **55 host-service/storage rows** remain unresolved for actual NFSD, ksmbd,
  NVMe target, RPC/RDMA, cluster filesystem or storage role/workload. Network
  reachability and compiled/preloaded code alone do not establish that service.
  These are not blanket safe/excluded findings.
- **3 MPTCP rows** are excluded by CONFIG_MPTCP being unset. **7 architecture**
  and **28 host-device** rows have concrete architecture/probe/DMA/storage paths
  outside standard tenant device delegation. One record affects userspace perf.
- **8 BPF/XDP/SK_MSG/SOCK_OPS rows** require program-type authority in the initial
  user namespace or explicit host token/delegation. Unprivileged socket-filter
  BPF availability does not authorize those program types. One audit rule path
  similarly requires initial-userns audit control.
- Availability, narrow disclosure, route/firewall policy and protocol-authentication
  cases remain separate from escalation candidates. For example IPv6 DAD double
  list deletion establishes a crash, while torn VXLAN neighbour MAC reads do not
  establish arbitrary kernel corruption merely because CNA scores them Critical.

There are also **5 unknown-not-qualified**, **3 unknown-tenant-api** and
**4 unknown-tenant-impact** rows. Every row has an explicit reason; these
categories preserve incomplete evidence rather than inventing a rejection.
[summary.json](supplemental-critical-evidence/summary.json) contains all exact
category counts without combining qualified leads with accepted candidates.

## Evidence and limits

[Source manifest](supplemental-critical-evidence/source-manifest.json) records
input SHA-256 hashes and local read-only source snapshots/URLs at exact frozen
Linux **a2384967b90f24d2470c9eb15f0e66d938df7e08**. The historical configuration
hash is **c10922b492fdf39ed3027b9c8f7ce2846a5d3799d57d417a161595fa81a64969**.
The inherited CNA snapshot is **56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9**.
Current vpsAdminOS source defaults are pinned by package A and remain distinct
from actual Node configuration. No production modules, boot identities, mounts,
sysctls, service roles, livepatch activation or exploitation were measured.

All records retain Linux CNA scores as attributed source ratings. A memory
corruption report alone does not demonstrate host-root or cross-VPS success.
Private drafts are unknown from public dedup. Historical livepatch coverage,
including quarantined v6, is not evidence of current safe activation. The lead
must obtain user selection approval before any advisory/draft phase.
