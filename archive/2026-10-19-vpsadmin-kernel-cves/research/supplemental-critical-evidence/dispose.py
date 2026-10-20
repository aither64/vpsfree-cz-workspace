"""Bounded Critical-only accounting; judgments below are research dispositions."""
import collections, hashlib, json
from pathlib import Path
BASE = Path(__file__).resolve().parent
RESEARCH = BASE.parent
rows = json.loads((BASE / 'critical-remainder.json').read_text())
manual = {r['cve'] for r in json.loads((RESEARCH / 'cve-evidence/manual-triage.json').read_text())}
published = set((RESEARCH / 'platform-evidence/dedup-cves.txt').read_text().split())
OVERRIDES = {}
def group(ids, disposition, reason, refs=()):
    for suffix in ids.split():
        OVERRIDES['CVE-2026-' + suffix] = (disposition, reason, list(refs))
group('68159 89653 89656', 'additional-strong-tenant-lead',
      'CephFS is namespace-mountable (FS_USERNS_MOUNT), Ceph/libceph preloaded. Tenant admin can choose a controlled monitor. Concrete shared-kernel out-of-bounds write; no host-root exploit verified.', ['fs/ceph/super.c','net/ceph/osdmap.c','fs/ceph/mdsmap.c','fs/ceph/mds_client.c','net/ceph/crush/mapper.c'])
group('80714', 'additional-strong-tenant-lead',
      'IPVS and schedulers preloaded; NEW_DAEMON and destination controls use GENL_UNS_ADMIN_PERM and netnsok=true. Configure own sync backup plus late ONE_PACKET destination; expiry leaves freed connection in hash. No platform exploit verified.', ['net/netfilter/ipvs/ip_vs_ctl.c','net/netfilter/ipvs/ip_vs_sync.c','net/netfilter/ipvs/ip_vs_conn.c'])
group('74581', 'additional-strong-tenant-lead',
      'Built IPv6; tenant network admin controls own routes and suppressing rules. Released route pointer is returned and put again. Shared-kernel lifetime/refcount concern; exact trigger/reuse and host-root outcome unverified.', ['net/ipv6/fib6_rules.c','net/core/fib_rules.c'])
group('72251', 'additional-strong-tenant-lead',
      'SIP conntrack/NAT helpers preloaded; namespace network admin can select helper/NAT and crafted cloned traffic. CNA establishes stale data pointer after skb reallocation; primary explicitly discounts fragmented input and expected TCP branch. No demonstrated escape.', ['net/netfilter/nf_nat_sip.c'])
group('90151', 'additional-strong-tenant-lead',
      'Downstream NFS namespace mounts and preloaded client allow tenant admin to choose NFSv4.0 server. Failed client initialization leaves callback IDR pointer, later lookup takes freed-object reference. Allocation-failure/callback prerequisites untested.', ['fs/nfs/client.c','fs/nfs/nfs4client.c'])
group('74669', 'already-in-existing-proposal', 'Outside manual109 but architect classification already accepts this historical IPVS stack overwrite. Account once; no new proposed ID.', ['net/netfilter/ipvs/ip_vs_ctl.c'])
group('74398', 'borderline-tenant-availability', 'IPv6 DAD failure versus tenant-controlled address deletion causes double list_del of poisoned links. Concrete shared-kernel crash; controlled reuse/write beyond poisoned-list failure not established.', ['net/ipv6/addrconf.c'])
group('43198', 'unknown-tenant-impact', 'IPv4-mapped IPv6 child publication races use of listener ipv6_pinfo. TCP/IPv6 tenant reachable; terse primary description does not establish controlled corruption/privilege gain.', ['net/ipv4/tcp_ipv4.c','net/ipv6/tcp_ipv6.c'])
group('68136', 'borderline-tenant-availability', 'GRO reaggregation corrupts frag_list and panics during segmentation. Veth/forwarded GRO geometry is plausible; exact tenant producer and stronger integrity consequence unresolved.')
group('68161', 'unknown-tenant-impact', 'SCTP UDP-port sysctl is tenant-netns configurable and SCTP preloaded; forgotten tunnel sockets survive namespace teardown. Description does not establish a specific exploitable freed-object access.', ['net/sctp/sysctl.c','net/sctp/protocol.c'])
group('68300', 'borderline-protocol-authorization', 'SCTP preloaded; missing AUTH permits a required-auth chunk under stated COOKIE-ECHO/clone-failure conditions. Protocol authentication bypass is real; host-root/cross-tenant consequence is not established.')
group('74287', 'borderline-tenant-read', 'SCTP ASCONF embedded address length exceeds outer bounds. Preloaded stack and optional tenant ADDIP/auth state; reviewed evidence establishes out-of-bounds parse read, not shared-kernel write.')
group('74473 74474 80681', 'borderline-tenant-read', 'VXLAN preloaded and tenant namespace admin can configure route-shortcircuit/ARP/ND paths. Nonlinear header pulls create out-of-bounds/stale reads. Complete escalation or cross-VPS disclosure not established.')
group('74406', 'borderline-tenant-availability', 'VXLAN GRO races socket release to NULL user_data. Preloaded namespace network surface; primary primitive is NULL dereference.')
group('74475', 'excluded-insufficient-platform-impact', 'VXLAN neighbour MAC read lacks seqlock and can tear. Primary describes inconsistent MAC, not shared-kernel corruption or serious cross-VPS read/write; Critical score does not establish those outcomes.')
group('68477', 'excluded-insufficient-platform-impact', 'IPVS IPv6 transport offsets wrong, but primary explicitly says official FTP helper is harmless because netfilter mangles ports without sequence adjustment. No alternative in-tree serious trigger established.')
group('72020', 'borderline-tenant-disclosure', 'IPVS sync accepts stale slab sequence adjustment data and can leak via forwarded TCP sequence/ack fields. Tenant can configure own sync/helper, but bounded leak/corruption of forwarded flow is not proven kernel execution.')
group('72421 72320 72348', 'borderline-network-policy', 'Primary describes route/firewall rule evaluation bypass. Tenant-controlled namespaced policy reachable; serious platform boundary consequence beyond affected policy requires actual host rules/service context.')
group('72436', 'unknown-tenant-impact', 'Preloaded ipset hash types; lockless RCU readers lack acquire ordering. Tenant hash configuration is plausible; primary gives no concrete corrupt-object/escape demonstration. Preserve as unresolved, not safe.')
group('80603', 'borderline-tenant-read', 'Preloaded IRC helper reads one stale/uninitialized byte within extra allocation; may change DCC expectation address/port. Description does not establish broad read or controlled kernel write.')
group('90110', 'borderline-network-side-channel', 'Predictable inetpeer eviction resets ICMP token buckets, supporting UDP-port inference/rate-limit bypass. Source rates Critical but this is a side-channel/policy primitive, not demonstrated host-root or memory corruption.')
group('64216', 'unknown-tenant-impact', 'Netfs preloaded and used by tenant filesystems; abandoned read folio index accessed after ownership returns. Specific supported netfs consumer/trigger and impact beyond stale folio read need qualification.')
group('80558 89649 89650 89651 89655 89990', 'additional-qualified-tenant-lead', 'CephFS namespace mount/preloaded modules support controlled server or local workload. Primary describes OOB read/UAF; serious disclosure/corruption extent remains candidate-specific and unresolved, below explicit write leads.', ['fs/ceph/super.c','fs/ceph/xattr.c','fs/ceph/mds_client.c','net/ceph/osdmap.c'])
group('68082 80561 80557', 'unknown-tenant-api', 'Libceph locker/watcher decoding lacks bounds. Modules present, but the recorded class-method operation may be RBD-specific; CephFS namespace mount alone does not establish this exact caller. Keep unresolved.', ['net/ceph/cls_lock_client.c'])
group('89652', 'conditional-reexport-service', 'Ceph name copying overruns NAME_MAX, but exact caller is CephFS NFS re-export get_name. Requires supported active NFSD export path, not ordinary CephFS mount alone.')
group('80528 90042', 'borderline-tenant-availability', 'CephFS mount reachable; primary reports reclaim/journal_info confusion or vmalloc crypto-address oops, with runtime filesystem/architecture prerequisites. No reliable write/control/escape proven.')
group('80671', 'excluded-userspace-tool', 'tools/perf sched parses untrusted perf.data in userspace. Kernel CVE record does not make this a tenant-to-host kernel path.')
group('63830', 'excluded-initial-userns-program-privilege', 'Concrete page-cache write requires a later writable SK_MSG BPF verdict program. Loading this type requires initial-userns CAP_BPF/CAP_NET_ADMIN or explicit host-delegated BPF token; tenant userns caps and unprivileged socket filters are insufficient.', ['kernel/bpf/syscall.c','kernel/bpf/token.c'])
group('64355 74476 74612 74616 74665 81002', 'excluded-initial-userns-program-privilege', 'XDP/DEVMAP/CPUMAP program loading and redirect/adjustment is not ordinary unprivileged socket-filter BPF. Requires initial-userns BPF/network authority or explicit token/delegation; no such delegation established. Do not infer tenant reachability from CONFIG_XDP_SOCKETS=y.', ['kernel/bpf/syscall.c','kernel/bpf/token.c'])
group('74268', 'excluded-initial-userns-program-privilege', 'Requires installed BPF SOCK_OPS callbacks; tenant userns caps do not authorize that program type. Primary shows warning on failed child setup, not a separate unprivileged primitive.', ['kernel/bpf/syscall.c'])
group('89643', 'excluded-initial-userns-audit-privilege', 'Needs installed AUDIT_DIR/AUDIT_EXE rules and autoremove. Audit control is an initial-userns capability surface, not granted by tenant userns root; no host rule path established.', ['kernel/audit.c'])
group('63940', 'conditional-sev-hardware', 'SEV guest port-I/O scratch underflow/zero-length hardening. KVM delegation alone does not establish SEV context creation or /dev/sev access; stronger primitive beyond length handling unverified.')
group('74310', 'conditional-vhost-device', 'vhost-net zerocopy completion UAF requires /dev/vhost-net backend and cloned skb completion. Standard device list and KVM feature do not delegate this vhost device; operator device/module exposure unresolved.')

def classify(r):
    ident=r['cve']; title=r['title'].lower()
    if ident in published:
        return ('already-publicly-reported', 'Known public vpsAdmin dedup; no new advisory candidate.', [])
    if ident in OVERRIDES:return OVERRIDES[ident]
    if any(k in title for k in ['smb: client','smb/client','cifs:']):
        return ('conditional-host-prepared-mount', 'CIFS/smb3 preloaded but lack FS_USERNS_MOUNT in exact .95; fs/super requires initial-userns mount. A tenant needs an operator-prepared/delegated mount. Legacy SMB additionally needs runtime protocol negotiation. Not default tenant mount.', ['fs/smb/client/cifsfs.c','fs/super.c'])
    if title.startswith('mptcp:'):
        return ('excluded-config-disabled', 'Exact frozen .95 has CONFIG_MPTCP unset. Optional tenant settings cannot enable absent code.', [])
    if any(k in title for k in ['kvm: arm64','kvm: s390','s390/','um: vector','scsi: xen:']):
        return ('excluded-unrelated-architecture', 'Architecture/virtualization backend differs from x86_64 container host; no shared host-kernel path through tenant KVM configuration.', [])
    if any(k in title for k in ['ksmbd:','nfsd:','sunrpc: zero','svcrdma:','nvmet','rtrs-srv','scsi: target','ib/isert','scsi: libiscsi','drbd:','ocfs2:','dlm:','xprtrdma:']):
        return ('unknown-host-service-or-storage', 'Requires exact active server/storage/RDMA role and workload from this CVE description. Preloaded code or tenant network packets alone do not establish the role; no live service evidence collected. Not a safe/excluded finding.', [])
    if any(k in title for k in ['exfat:','ntfs3:','isofs:','ext4:','orangefs:','9p: avoid']):
        return ('conditional-filesystem-mount-or-device', 'Requires crafted filesystem/mounted backend or device/interface not delegated by standard VPS device set; no matching initial-userns mount/userns support established in this bounded pass. Keep conditional/unresolved.', [])
    if any(k in title for k in ['tipc:','batman-adv:','net/smc:','net/x25:','phonet:','openvswitch:','ila:','amt:','rxrpc:','afs:','net/9p:','gue:','espintcp:','sch_codel:','sch_fq_codel:','net: ife:','net/sched: cls_api:','macvlan:','ipvlan:']):
        return ('conditional-host-module-or-feature', 'Required specialised protocol/qdisc/netdevice module is not in the platform default preload list (autoload disabled). If host makes it available, exact namespace/operation and primary primitive still need qualification. Compiled m alone is not default availability.', [])
    if any(k in title for k in ['rdma/siw:','rdma/rxe:','rdma/srpt:']):
        return ('conditional-rdma-service-device', 'Requires RDMA queue/device/service or software RDMA module not in default preload/delegation. Host hardware/module/service state unknown; not an ordinary tenant socket path.', [])
    if any(k in title for k in ['serial:','spi:','crypto:','net: ethernet:','qede:','gve:','mana:','igbvf:','rtase:','iommu/','vdpa/','qla2xxx:','rdma/bnxt_re:','nvme','md/raid10:','block:']):
        return ('excluded-unrelated-host-device-path', 'Primary requires host device probe/DMA/storage management or device-provided metadata, not standard delegated VPS devices. No tenant-controlled affected device/path established; actual host hardware exposure remains outside this bounded screen.', [])
    return ('unknown-not-qualified', 'No complete tenant trigger and serious platform impact established in this bounded pass. Retain explicit unknown instead of treating score as exploit evidence.', [])
ledger=[]
for r in rows:
    dis,reason,refs=classify(r)
    paragraphs=r['description'][0]['value'].split('\n\n',2)
    primitive=' '.join(paragraphs[-1].split())[:1600]
    ledger.append({'cve':r['cve'],'title':r['title'],'disposition':dis,'reason':reason,'primary_primitive_excerpt':primitive,'fixes':[{'sha':f['sha'],'release':f['release']}for f in r['fixes']], 'metrics':r['metrics'],'primary_url':r['cna_url'],'source_refs':refs,'review_level': 'focused primary-description/source review' if r['cve'] in OVERRIDES else 'bounded subsystem/configuration gate screen; full source audit not performed','evidence_limit':'No exploit run, no current node measurement; plausible corruption is not demonstrated host execution.'})
assert len(rows)==223 and len(ledger)==223
assert len({r['cve'] for r in ledger})==223
assert not manual.intersection(r['cve'] for r in ledger)
assert sum(r['cve'] in published for r in ledger)==15
(BASE/'dispositions.json').write_text(json.dumps(ledger,indent=2)+'\n')
counts=dict(sorted(collections.Counter(r['disposition']for r in ledger).items()))
summary={'range_records':3493,'critical_total':269,'critical_in_existing_manual109':46,'critical_outside_manual109':223,'outside_manual109_already_published':15,'novel_critical_remainder':208,'disposition_count':len(ledger),'counts':counts,'unassigned_dispositions':0,'duplicate_ids':0,'manual109_overlap':0,'scope_limit':'Critical Linux CNA metric>=9.0 only; High, unscored, external CNAs not comprehensively screened. Per-record accounting is not exploit qualification.'}
(BASE/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
