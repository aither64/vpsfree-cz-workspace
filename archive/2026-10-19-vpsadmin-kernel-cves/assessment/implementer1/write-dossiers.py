import json,pathlib,hashlib,sys
P=pathlib.Path('assessment/implementer1');W=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-vpsadmin-kernel-cves/security-advisories')
REV='1dfea587406b7dd79973831d1677fb2418e5e9aa';OS='87fc13aac3fc8ce3d6c71c7ef3a8e72a5993a088';CNA='56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9'
requirements={r['cve']:r for r in json.load(open(P/'requirements.json'))['rows']}
records={r['cve']:r for r in json.load(open('research/cve-evidence/range-records.json'))}

def nver(v):
 p=v.split('.');return '.'.join(p+['0']*(3-len(p)))
def key(v):return tuple(map(int,nver(v).split('.')))
def bounds(d):
 git=[v for a in d['affected'] for v in a['versions'] if v.get('versionType')=='git' and 'lessThan' in v]
 sem=[v for a in d['affected'] for v in a['versions'] if v.get('versionType')!='git']
 intro=next(v['version'] for v in sem if v['status']=='affected' and 'lessThan' not in v and 'lessThanOrEqual' not in v)
 main=next(v['version'] for v in sem if v.get('versionType')=='original_commit_for_fix')
 fixes=[v for v in sem if v['status']=='unaffected' and v.get('lessThanOrEqual','').endswith('.*')]
 assert len(git)==len(fixes)+1,(len(git),len(fixes))
 rules={}
 for i,v in enumerate(fixes):
  br=v['lessThanOrEqual'][:-2];start=nver(br)
  if key(intro)>key(start) and '.'.join(intro.split('.')[:2])==br:start=nver(intro)
  rules[br]={'affected_from':start,'fixed_in':nver(v['version']),'fixed_commit':git[i]['lessThan']}
 # Explicit semantic-version backport introduction intervals.
 for v in sem:
  if v['status']=='affected' and ('lessThan' in v or v.get('lessThanOrEqual','').endswith('.*')):
   br='.'.join(v['version'].split('.')[:2]);rules.setdefault(br,{'fixed_in':None})['affected_from']=nver(v['version'])
 # Older supported/EOL LTS families covered by the checked CPE/global range.
 for br in ['4.4','4.9','4.14','4.19','5.4','5.10','5.15','6.1']:
  if key(nver(br))>=key(intro) and key(nver(br))<key(main) and br not in rules:
   rules[br]={'affected_from':nver(br),'fixed_in':None}
 for i,v in enumerate(fixes):
  rules[v['lessThanOrEqual'][:-2]]['introduced_commit']=git[i]['version']
 unbounded=[v for a in d['affected'] for v in a['versions'] if v.get('versionType')=='git' and 'lessThan' not in v]
 backports=[v for a in d['affected'] for v in a['versions'] if v.get('versionType')=='semver' and v['status']=='affected' and 'lessThan' in v and not rules['.'.join(v['version'].split('.')[:2])].get('fixed_commit')]
 # Bippy lists remaining Git introductions and their semantic backports in order.
 assert len(unbounded)==len(backports),(len(unbounded),len(backports))
 for g,v in zip(unbounded,backports):
  br='.'.join(v['version'].split('.')[:2]);rules[br]['introduced_commit']=g['version']
 return nver(intro),nver(main),dict(sorted(rules.items(),key=lambda x:key(x[0]))),git

def yaml(v,level=0):
 # JSON scalar quoting is YAML-compatible; keep human text as folded blocks.
 pad='  '*level;out=[]
 if isinstance(v,dict):
  for k,val in v.items():
   k=json.dumps(k,ensure_ascii=False) if '.' in k or k.isdigit() else k
   if isinstance(val,dict) and val or isinstance(val,list) and val:
    out.append(pad+k+':');out.extend(yaml(val,level+1))
   elif isinstance(val,str) and len(val)>130:
    out.append(pad+k+': >-');out.append(pad+'  '+val)
   else:out.append(pad+k+': '+json.dumps(val,ensure_ascii=False))
 elif isinstance(v,list):
  for val in v:out.append(pad+'- '+json.dumps(val,ensure_ascii=False))
 return out

platform_links=f'''- [vpsAdmin feature defaults](https://github.com/vpsfreecz/vpsadmin/blob/fb2f51222503a45f2e5a42af505f719e44279ed0/api/models/vps_feature.rb)
- [Container identity and security-profile generation](https://github.com/vpsfreecz/vpsadminos/blob/{OS}/osctld/templates/ct/config.erb), [common/userns includes](https://github.com/vpsfreecz/vpsadminos/blob/{OS}/osctld/configs/lxc/common.conf)
- [Pinned LXC user-namespace capabilities](https://github.com/vpsfreecz/lxc/blob/267e7844c122b9be56ca8a1ccc3d2f4d8986c326/config/templates/userns.conf.in), [default syscall filter](https://github.com/vpsfreecz/lxc/blob/267e7844c122b9be56ca8a1ccc3d2f4d8986c326/config/templates/common.seccomp)
- [Module preload/autoload policy](https://github.com/vpsfreecz/vpsadminos/blob/{OS}/os/modules/config/kernel.nix), [kernel tunables](https://github.com/vpsfreecz/vpsadminos/blob/{OS}/os/modules/config/tunables.nix)
- [Kernel build policy](https://github.com/vpsfreecz/vpsadminos/blob/{OS}/os/packages/linux/common-config.nix), [frozen 6.12.95 recipe](https://github.com/vpsfreecz/vpsadminos/blob/c065fa2f8485399737e20e8ef9e44299d0766654/os/packages/linux/boot-6.12.95.nix)
- [Canonical historical livepatch coverage](https://github.com/vpsfreecz/vpsadminos/blob/{OS}/docs/os/livepatches/6.12.95.md)'''


def write(c,s):
 raw=(P/'primary'/c/'record.json').read_bytes();d=json.loads(raw)['containers']['cna'];intro,main,rules,git=bounds(d);req=requirements[c]
 data={'schema_version':1,'cve':c,'name':s['name'],'affected_from':intro,'fixed_from':main,'version_rules':rules,'platform':{'configuration_assessed':True,'history_required_since':req['history_required_since'],'affected_node_roles':req['affected_node_roles'],'required_options':req['required_options'],'required_sysctls':req['required_sysctls'],'accepted_kernel_builds':[],'accepted_livepatches':[],'accepted_ebpf_programs':[]},'impact':s.get('impact',{'vps_root':'possible','node_root':'possible','cross_vps':'unknown','node_availability':'plausible'}),'texts':{'en':{'summary':s.get('summary_en','Kernel memory corruption'),'description':s['en'],'response':s['response_en']},'cs':{'summary':s.get('summary_cs','Poškození paměti jádra'),'description':s['cs'],'response':s['response_cs']}}}
 dest=W/'advisories'/c;dest.mkdir(parents=True,exist_ok=True)
 (dest/'advisory.yml').write_text('\n'.join(yaml(data))+'\n')
 files=sorted({f for a in d['affected'] for f in a.get('programFiles',[])})
 primary=f'https://github.com/CVEProject/cvelistV5/blob/{CNA}/cves/2026/{c.split("-")[-1][:-3]}xxx/{c}.json'
 rows=['| Branch | Affected from, inclusive | Fixed from, exclusive boundary | Corrective commit |','| --- | --- | --- | --- |']
 for br,r in rules.items():
  commit=r.get('fixed_commit');rows.append(f"| {br} | {r['affected_from']} | {r['fixed_in'] or 'open-ended; no same-branch fix listed'} | "+(f'[{commit}](https://git.kernel.org/stable/c/{commit})' if commit else 'not listed')+' |')
 metrics=[]
 for m in d.get('metrics',[]):
  for kind,val in m.items():
   if kind.startswith('cvss'):metrics.append(f"Linux CNA {kind}: {val.get('baseScore')} ({val.get('baseSeverity','unlabelled')}), `{val.get('vectorString')}`.")
 if not metrics:metrics=['No formal CVSS metric is supplied in the reviewed Linux CNA container.']
 patch=P/'primary'/c/'stable-fix.patch';sha=records[c]['fixes'][0]['sha']
 linuxlinks='\n'.join(f'- [{f}](https://github.com/vpsfreecz/linux/blob/{REV}/{f})' for f in files)
 analysis=f'''# {c} — {s['name']}

Reviewed 2026-10-19. This dossier assesses the tenant-configured networking path; it is not a claim about every host service or every historical node configuration. The per-node evaluation is a separate evidence product.

## Primary defect and evidence strength

{s['primitive']}

{s['strength']}

{' '.join(metrics)} The score and any CNA scenario assertions are source attribution, not a demonstrated vpsAdminOS escape or a substitute for the prerequisite analysis.

## Introduction, stable fixes and exceptions

The primary Linux CNA record places the global introduction at **{intro}**, commit [`{git[-1]['version']}`](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id={git[-1]['version']}), and the mainline fix at **{main}**, commit [`{git[-1]['lessThan']}`](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id={git[-1]['lessThan']}). The 6.12 correction is [`{sha}`](https://git.kernel.org/stable/c/{sha}) in **{req['first_fix_release']}**.

{chr(10).join(rows)}

Stable semantic-version entries, Git fix references and CPE applicability were checked together. The older LTS rows without a listed fix remain explicitly open-ended within the CNA global/CPE affected scope; their absence from the fix list is not evidence of safety. Branch-specific backport introductions, where listed, override the global mainline introduction. Other release families remain governed by the global boundary rather than an invented same-branch fix.

{s.get('exception','No correction exception changing this 6.12 fix boundary is established by the reviewed record and patch.')}

## Tenant prerequisites and current downstream source

{s['gates']}

The inspected vpsAdmin feature policy, generated LXC config, userns capability reset and default seccomp profile do not remove the cited namespace-scoped networking path. Full capabilities inside the container user namespace do not confer initial-user-namespace module-loading authority. Source defaults are not a measurement of a node or a tenant namespace. The explicit required interface options are `{json.dumps(req['required_options'],sort_keys=True)}`; an explicit disabled necessary interface can prove unreachability for that exact build. Compiled modules alone cannot prove actual load state.

Current downstream Linux source reviewed at `{REV}`:

{linuxlinks}

Platform sources used to bind the gates:

{platform_links}

## Impact and protections

{s['outcomes']}

The archived 6.12.95 build enables allocator randomization/freelist hardening, zeroing on allocation/free and FORTIFY. It lacks HARDENED_USERCOPY. These are source/configuration facts for that archived build, not universal fleet facts. They can change reuse opportunities or catch some bounds violations, but do not repair the missing lifetime/reference or inconsistent-size operation. They do not establish that this exact primitive is prevented. Default seccomp does not filter the networking operations used here; initial-userns module-loading restrictions do not undo an already available interface. Runtime LSM/profile overrides require the shared typed evidence and further source qualification when relevant. Kernel warning monitoring can detect failed triggers; it is not prevention and does not establish whether production exploitation occurred.

## Role, history and mitigation contract

Only role `node` is included because the assessed path uses VPS-controlled sockets, network namespaces or tenant device/configuration lifecycle. Storage nodes do not run VPS workloads. A separately established real host-service use would need its own scope review; old release age alone is not sufficient to add storage.

The required history begins `2026-01-01T00:00:00Z` as a review window, not an asserted introduction or deployment date. No lifecycle start override or historical attestation is inferred or copied. A current fixed release does not prove earlier safety; affected historical stable releases with missing configuration are conservatively affected after this reachability review. Missing baseline/transition evidence remains unknown under the existing evaluator.

{s['sysctls']}

Runtime module/type registration and tenant protocol/device state are not generic schema predicates. They remain explicit prerequisites rather than ignored YAML keys or manual per-node status edits. Empty accepted-build/livepatch/eBPF lists make no assertion that a historical livepatch was absent. Exact observed source identities and function-replacement coverage must be reconciled before accepting tuples; the canonical coverage page alone proves neither activation nor a safe deployment. Quarantined livepatch v6 is not recommended for application, while independently source-correct, observed enabled/stable historical protection must still be preserved. No mitigation date or livepatch activation is asserted by this source-only draft.

## Reproducible source receipts and remaining evidence

- [Primary CVE record]({primary}); [CVE record view](https://www.cve.org/CVERecord?id={c}). CNA snapshot `{CNA}`; retained record SHA-256 `{hashlib.sha256(raw).hexdigest()}`.
- [Exact stable fix](https://git.kernel.org/stable/c/{sha}); retained patch SHA-256 `{hashlib.sha256(patch.read_bytes()).hexdigest()}`. Missing local partial-clone objects were read only via exact stable-maintainer mirror HTTP patches, never by repository fetch.
- Current Linux source snapshots and hashes are retained in the session's `assessment/implementer1/source-manifest.json`; exact fix access methods/URLs/hashes in `fix-source-manifest.json`.
- Archived configuration SHA-256 `c10922b492fdf39ed3027b9c8f7ce2846a5d3799d57d417a161595fa81a64969`, Linux `a2384967b90f24d2470c9eb15f0e66d938df7e08`; scope is the archived build, not fleet history.
- Shared typed node snapshot/evaluation and exact historical livepatch content/identity/activation reconciliation remain separate dependencies. They must establish actual booted/current identities, needed options/modules, role and transitions. No independent collection, exploit test, kernel build or remote draft write was performed for this source dossier.
'''
 (dest/'analysis.md').write_text(analysis)
 print(c,req['first_fix_release'],len(rules),'branch rules')

SPECS={}
SPECS['CVE-2026-74668']={
'name':'AF_PACKET TX_RING inconsistent header-length race',
'primitive':'`tpacket_snd()` formerly read `dev->hard_header_len` separately for allocation, frame limits and construction in `tpacket_fill_skb()`. Concurrent device reconfiguration can leave too little reserved headroom or a negative copy length. The stable fix snapshots the length once and passes it through all these operations; the concrete primitive is an out-of-bounds packet-buffer write.',
'strength':'The fix and CNA describe the size inconsistency and memory corruption. CNA scenario text infers privilege escalation from that primitive. This review did not reproduce a host exploit or establish controlled node execution.',
'gates':'`packet_create()` checks `ns_capable(net->user_ns, CAP_NET_RAW)`, not initial-userns authority. The concurrent device change additionally needs CAP_NET_ADMIN in the device namespace. The current OS preload list includes af_packet and suitable configurable network devices. A VPS administrator can arrange the ring and its own device reconfiguration; an ordinary process lacking these capabilities has no established direct path. No special physical hardware or delegated device is required.',
'outcomes':'A capability-bearing process may use a kernel overwrite to escalate inside its VPS; an already-root VPS administrator is instead targeting the shared kernel. Node-root compromise is possible from the overwrite, but the reviewed record/fix does not establish a complete platform escape. Cross-VPS access remains unresolved, rather than being ruled out by CNA scope wording. An invalid buffer expansion can BUG/oops and disrupt all VPSes on the node.',
'sysctls':'No host-wide sysctl is established as the necessary trigger gate. Network-device settings belong to the tenant namespace; host namespace defaults cannot prove their absence.',
'exception':'This is the TX_RING path, distinct from published CVE-2026-74582 in the non-ring send path. The primary fix explicitly leaves the separate SOCK_DGRAM hard_header_len/header_ops consistency problem outside its scope.',
'en':'AF_PACKET transmit rings can use inconsistent packet-header sizes when a VPS process with raw-packet and network-administration rights changes its network device concurrently. The resulting out-of-bounds write could let a process with those delegated rights gain root inside the VPS. A VPS administrator already has that access but could use the same shared-kernel corruption to attempt node compromise. The reviewed Linux record and fix do not establish a complete node escape or a specific route to another VPS. Failed attempts can crash the shared kernel. Kernel warnings that may indicate this bug was triggered are monitored.',
'cs':'Při souběžné změně síťového zařízení může AF_PACKET použít pro vysílací kruhový buffer rozdílné velikosti hlavičky paketu. Proces k tomu potřebuje práva pro práci s raw pakety a správu sítě ve VPS. Zápis mimo vyhrazenou paměť by mohl procesu s těmito delegovanými právy umožnit získat root ve VPS. Správce VPS již tato oprávnění má, ale stejné poškození sdíleného jádra by mohl využít k pokusu o ovládnutí node. Analyzovaný záznam Linuxu a oprava nepopisují úplný postup úniku na node ani konkrétní cestu k jinému VPS. Neúspěšný pokus může shodit sdílené jádro. Varování jádra, která mohou naznačovat spuštění této chyby, jsou monitorována.',
'response_en':'The upstream 6.12 branch includes the correction from Linux 6.12.104. The fix uses one consistent header length throughout transmit-ring processing. Namespace capabilities limit who can set up the race but do not protect the shared kernel from a VPS administrator.',
'response_cs':'Ve větvi Linuxu 6.12 je oprava obsažena od verze 6.12.104. Při zpracování vysílacího kruhového bufferu se po opravě používá jedna konzistentní délka hlavičky. Oprávnění v síťovém jmenném prostoru omezují, kdo může souběh připravit, ale nechrání sdílené jádro před správcem VPS.'}
SPECS['CVE-2026-80841']={
'name':'AF_PACKET vmalloc TX_RING mapping use-after-free',
'primitive':'Transmit skbs retain ring-frame pointers. Page references preserve page-backed blocks, but not a vmalloc virtual mapping. Ring replacement or socket closure could unmap vmalloc storage while late completion still writes a timestamp/status. The fix orders pending decrements after frame stores, rechecks replacement under pg_vec_lock, and defers vmalloc vector destruction until sk_wmem_alloc accounting shows the skbs finished; pending_refcnt lives until final socket destruction.',
'strength':'The reviewed source establishes late stores through an expired mapping, rather than merely a retained page reference. No complete code-execution chain or platform escape is supplied by this review.',
'gates':'The socket creation gate is namespace-scoped CAP_NET_RAW in packet_create(). A tenant process with that right can allocate a TX_RING, submit traffic and close/replace its ring. The vulnerable lifetime additionally requires a vmalloc-backed allocation and outstanding transmit completion; not every ring uses vmalloc. CONFIG_PACKET is enabled and af_packet is explicitly preloaded in the inspected OS source. Network administration may help arrange completion timing but is not the socket creation check.',
'outcomes':'Kernel writes through a stale mapping make VPS-root escalation and host-root compromise possible if the stale address can be usefully reclaimed. The primary fix does not establish that exploitation chain or a cross-VPS access mechanism. A bad completion access can fault the shared node kernel and interrupt other tenants.',
'sysctls':'No host sysctl is shown to gate the vmalloc-ring lifetime. Runtime memory geometry and pending completion are prerequisites, not presumed protective settings.',
'exception':'The inspected .113 source contains later AF_PACKET changes as well. In particular the subsequent CVE-2026-98503 fix must not be confused with this lifetime correction or used to move its first fixed boundary away from 6.12.111.',
'en':'An AF_PACKET transmit ring backed by a virtual memory mapping can be released while a transmitted packet still refers to it. A VPS process with raw-packet rights can reach this path, and late completion can write to the released mapping. Exploitation could potentially give that process root inside the VPS or compromise the shared node kernel. The reviewed Linux record and fix do not establish a complete node escape or a specific route to another VPS. A failed access may crash the shared kernel. Kernel warnings that may indicate this bug was triggered are monitored.',
'cs':'Vysílací kruhový buffer AF_PACKET uložený ve virtuálně mapované paměti může být uvolněn, přestože na něj odeslaný paket stále odkazuje. K této cestě má přístup proces ve VPS s právy pro raw pakety a pozdější dokončení přenosu může zapisovat do uvolněného mapování. Zneužití by takovému procesu mohlo umožnit získat root ve VPS nebo ovládnout sdílené jádro node. Analyzovaný záznam Linuxu a oprava nepopisují úplný postup úniku na node ani konkrétní cestu k jinému VPS. Neplatný přístup může shodit sdílené jádro. Varování jádra, která mohou naznačovat spuštění této chyby, jsou monitorována.',
'response_en':'The upstream 6.12 branch includes the correction from Linux 6.12.111. It retains the virtual mapping until transmit completions have finished. Allocator hardening does not extend a mapping lifetime and is not a fix for this bug.',
'response_cs':'Ve větvi Linuxu 6.12 je oprava obsažena od verze 6.12.111. Virtuální mapování se po opravě zachovává až do dokončení přenosů. Zpevnění alokátoru neprodlužuje životnost mapování a tuto chybu neopravuje.'}
SPECS['CVE-2026-74586']={
'name':'SCTP ASCONF new_transport use-after-free',
'primitive':'An authenticated ASCONF can add a transport and delete it again through wildcard DEL-IP while leaving asoc->new_transport dangling. The cached pointer is then used for a queued HEARTBEAT; after RCU frees the transport, successful local-address replacement releases the heartbeat and sctp_outq_select_transport reads the freed transport state. The fix clears new_transport when that peer is removed.',
'strength':'The upstream report describes a KASAN reproducer succeeding in 2/2 unpatched runs, with a four-byte read of transport->state. That is a concrete stale-object read, not a demonstrated arbitrary write or complete privilege-escalation chain. CNA Critical scoring is kept separate from that narrower evidence.',
'gates':'The target association must use SCTP address reconfiguration and authenticated ASCONF, with the local-address replacement sequence described by the fix. SCTP sockets pass the default syscall filter. The OS preloads sctp. ADDIP/auth controls are per-netns and can be enabled by a VPS network administrator; their disabled host defaults do not exclude a tenant-configured association. A peer that can authenticate to the prepared association can supply the ASCONF sequence.',
'outcomes':'The demonstrated primitive is a kernel UAF read and resulting fault, so a complete VPS-root or node-root escalation remains unresolved. Reclaiming transport memory might widen consequences, but the reviewed record/fix does not establish that chain or access to another VPS. Shared-kernel availability is a credible consequence of the invalid access.',
'impact':{'vps_root':'unknown','node_root':'unknown','cross_vps':'unknown','node_availability':'plausible'},
'sysctls':'net.sctp.addip_enable/auth_enable and related ADDIP policy are namespaced. No value read only from the host namespace proves all tenant endpoint state. Accordingly required_sysctls is empty rather than falsely treating a restrictive host default as prevention.',
'en':'An authenticated SCTP peer can leave a freed transport referenced by a queued heartbeat when address reconfiguration and local address replacement are used. A VPS administrator can enable the required SCTP features in the VPS network namespace. The reported failure is a read from freed kernel memory; the reviewed Linux record and fix do not establish a complete escalation to VPS root, node control or another VPS. The invalid access can crash the shared kernel and interrupt other VPSes. Kernel warnings that may indicate this bug was triggered are monitored.',
'cs':'Ověřený protějšek SCTP může při změnách adres a nahrazení místní adresy zanechat ve frontě heartbeat odkaz na uvolněný transport. Potřebné funkce SCTP může správce VPS zapnout ve svém síťovém jmenném prostoru. Popsaným selháním je čtení z uvolněné paměti jádra; analyzovaný záznam Linuxu a oprava nepopisují úplný postup k získání root ve VPS, ovládnutí node ani přístupu do jiného VPS. Neplatný přístup může shodit sdílené jádro a přerušit provoz dalších VPS. Varování jádra, která mohou naznačovat spuštění této chyby, jsou monitorována.',
'response_en':'The upstream 6.12 branch includes the correction from Linux 6.12.104. The cached new-transport pointer is cleared when the transport is removed. Host defaults for SCTP address reconfiguration do not protect associations configured separately inside a VPS.',
'response_cs':'Ve větvi Linuxu 6.12 je oprava obsažena od verze 6.12.104. Při odstranění transportu se po opravě vymaže i uložený ukazatel na nový transport. Výchozí nastavení změn adres SCTP na hostiteli nechrání asociace nastavené samostatně uvnitř VPS.'}
SPECS['CVE-2026-74587']={
'name':'SCTP cached ASCONF chunk use-after-free and second release',
'primitive':'Peer restart invokes sctp_asconf_queue_teardown while the association stays alive. It freed the outbound ASCONF chunk without clearing addip_last_asconf. A delayed authenticated ASCONF_ACK can reuse that pointer and release the chunk again. The fix clears the cached pointer and consumes a stale T4 timer expiry when no outstanding ASCONF remains; stopping the timer alone does not wait for another CPU callback.',
'strength':'The source establishes dangling-chunk use and a second release, plus the timer race addressed by the correction. CNA scenario impact is not a reproduced exploitation chain on this platform.',
'gates':'Requires an SCTP association using outbound address reconfiguration, a peer restart and a delayed authenticated ASCONF_ACK. The OS explicitly preloads SCTP and ordinary SCTP sockets pass default seccomp. A namespace administrator can enable ADDIP/auth settings for its own association. Authenticated peer control and protocol state are material; arbitrary unrelated network traffic is insufficient.',
'outcomes':'UAF and a second free are memory-corruption primitives from which VPS-root and node-root escalation are possible. The reviewed fix does not establish reliable controlled execution or cross-VPS access. Corrupted allocator/protocol state or the related stale timer can fault the shared kernel.',
'sysctls':'SCTP ADDIP/auth policy is per network namespace. No host sysctl value is treated as a tenant-wide mitigation; actual endpoint negotiation and namespace state remain source prerequisites.',
'en':'During an SCTP peer restart, the kernel can free a cached address-reconfiguration request but keep its pointer. A delayed authenticated acknowledgement can then use and release the object again. A VPS administrator can enable the required protocol features, and exploitation could potentially give a process root inside the VPS or compromise the shared node kernel. The reviewed Linux record and fix do not establish a complete node escape or a specific route to another VPS. Failed attempts can crash the shared kernel. Kernel warnings that may indicate this bug was triggered are monitored.',
'cs':'Při restartu protějšku SCTP může jádro uvolnit uložený požadavek na změnu adres, ale ponechat na něj ukazatel. Opožděné ověřené potvrzení pak může objekt znovu použít a uvolnit. Potřebné funkce protokolu může správce VPS zapnout a zneužití by mohlo procesu umožnit získat root ve VPS nebo ovládnout sdílené jádro node. Analyzovaný záznam Linuxu a oprava nepopisují úplný postup úniku na node ani konkrétní cestu k jinému VPS. Neúspěšný pokus může shodit sdílené jádro. Varování jádra, která mohou naznačovat spuštění této chyby, jsou monitorována.',
'response_en':'The upstream 6.12 branch includes the correction from Linux 6.12.104. It clears the cached ASCONF pointer and safely ignores a timer expiry left over from the cleared request. Namespace-local SCTP controls can be changed by a VPS administrator, so host defaults do not prevent this path.',
'response_cs':'Ve větvi Linuxu 6.12 je oprava obsažena od verze 6.12.104. Vymaže uložený ukazatel ASCONF a bezpečně přeskočí doběhnutí časovače pro již odstraněný požadavek. Nastavení SCTP ve vlastním síťovém jmenném prostoru může správce VPS změnit, takže výchozí hodnoty na hostiteli této cestě nebrání.'}
SPECS['CVE-2026-74588']={
'name':'SCTP stale chunk transport after retransmit-list move',
'primitive':'__sctp_outq_flush_rtx moves a gap-acknowledged chunk to another transport transmitted list without updating chunk->transport. Peer ASCONF Delete-IP can free the old transport while the chunk resides on the new list and evades the old-list scrub. Later SACK reneging clears tsn_gap_acked and processing reaches tchunk->transport->flight_size -= sctp_data_size(tchunk) in the freed object. The fix rebinds chunk->transport at the list move.',
'strength':'The upstream report supplies a KASAN UAF read, and the cited read-modify-write statement establishes a stale-object write target. This is stronger primitive evidence than the read-only first fault in 74586, but still not a complete reviewed node exploit.',
'gates':'The target uses SCTP with authenticated address reconfiguration, retransmission/gap acknowledgements and subsequent peer-controlled transport deletion and SACK reneging. The preloaded SCTP module and permissive socket syscall profile expose the interface. Tenant network administrators can enable the namespaced ADDIP/auth prerequisite; a prepared authenticated peer supplies the protocol sequence.',
'outcomes':'The stale flight_size update can corrupt shared kernel memory. VPS-root and host-root compromise are possible consequences, while a working controlled-execution chain and cross-VPS mechanism are unresolved in the reviewed record and patch. The invalid transport access can crash the node kernel.',
'sysctls':'The required SCTP ADDIP/auth setup is namespaced and endpoint-specific. The host default is not used as evidence about every VPS network namespace; no generic reviewed host-sysctl predicate is declared.',
'en':'SCTP can move an acknowledged packet to another transport list while retaining a pointer to its old transport. An authenticated peer can remove the old transport and later cause the kernel to update its freed memory. A VPS administrator can enable the required address-reconfiguration features. The memory corruption could potentially lead to VPS-root or node compromise, but the reviewed Linux record and fix do not establish a complete node escape or a specific route to another VPS. Invalid accesses can crash the shared kernel. Kernel warnings that may indicate this bug was triggered are monitored.',
'cs':'SCTP může přesunout potvrzený paket do seznamu jiného transportu, ale ponechat u něj ukazatel na původní transport. Ověřený protějšek může starý transport odstranit a později přimět jádro k zápisu do jeho uvolněné paměti. Potřebné funkce pro změny adres může správce VPS zapnout. Poškození paměti by mohlo vést k získání root ve VPS nebo ovládnutí node, ale analyzovaný záznam Linuxu a oprava nepopisují úplný postup úniku na node ani konkrétní cestu k jinému VPS. Neplatné přístupy mohou shodit sdílené jádro. Varování jádra, která mohou naznačovat spuštění této chyby, jsou monitorována.',
'response_en':'The upstream 6.12 branch includes the correction from Linux 6.12.104. Moving a chunk between transport lists now also updates its transport pointer. Allocator hardening can make reuse harder but does not prevent the stale write.',
'response_cs':'Ve větvi Linuxu 6.12 je oprava obsažena od verze 6.12.104. Při přesunu mezi seznamy transportů se po opravě aktualizuje také ukazatel na transport. Zpevnění alokátoru může ztížit opětovné využití paměti, ale nebrání zápisu přes neplatný ukazatel.'}

if __name__=='__main__':
 for c in sys.argv[1:] or SPECS:
  write(c,SPECS[c])
