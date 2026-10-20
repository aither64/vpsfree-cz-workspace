"""Render owned factual dossier candidates from pinned primary records and reviewed notes."""
import json,re,sys
from pathlib import Path
B=Path(__file__).resolve().parent;S=B.parent.parent;W=Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-vpsadmin-kernel-cves/security-advisories')
IDS=json.loads((S/'assessment/packages.json').read_text())['groups']['implementer2'];R={x['cve']:x for x in json.loads((S/'research/cve-evidence/range-records.json').read_text())};REQ={x['cve']:x for x in json.loads((B/'requirements.json').read_text())['rows']}
L='1dfea587406b7dd79973831d1677fb2418e5e9aa';F='a2384967b90f24d2470c9eb15f0e66d938df7e08';O='87fc13aac3fc8ce3d6c71c7ef3a8e72a5993a088';V='fb2f51222503a45f2e5a42af505f719e44279ed0';C='a2ad6da408715de811cc6d8ea7b29ac55ea341ec'
META={
'74730':dict(name='NFS delayed FREE_STATEID server use-after-free',fix='Pin the NFS server superblock while asynchronous FREE_STATEID is in flight, releasing it only when the RPC completes.',en='A VPS administrator can mount a controlled NFSv4.1 or newer server. Delaying an asynchronous FREE_STATEID request while the mount is torn down can leave its callbacks using a freed server object.',cs='Správce VPS může připojit server NFSv4.1 nebo novější, který ovládá. Pokud se asynchronní požadavek FREE_STATEID zdrží při rušení připojení, jeho callbacky mohou použít již uvolněný objekt serveru.',fcs='Oprava udržuje server NFS platný po celou dobu asynchronního požadavku FREE_STATEID.',group='nfs',sources=['fs/nfs/nfs4proc.c','fs/nfs/super.c']),
'90151':dict(name='NFSv4 callback client identifier use-after-free',fix='Remove the callback identifier before freeing a client whose initialization failed, so later callbacks cannot find the released client.',en='A VPS administrator can mount a controlled NFSv4.0 server. Failed client initialization can leave a callback identifier pointing to a freed client; a later server callback can then update its freed reference counter.',cs='Správce VPS může připojit server NFSv4.0, který ovládá. Neúspěšná inicializace klienta může ponechat identifikátor callbacku odkazující na uvolněného klienta. Pozdější callback serveru pak může změnit jeho již uvolněné počítadlo odkazů.',fcs='Oprava před uvolněním klienta po neúspěšné inicializaci odstraní jeho identifikátor callbacku.',group='nfs',sources=['fs/nfs/client.c','fs/nfs/nfs4client.c','fs/nfs/super.c']),
'68159':dict(name='Ceph OSD map placement stack overwrite',fix='Bound pg_temp, pg_upmap and pg_upmap_items lengths by CEPH_PG_MAX_SIZE before decoded entries reach fixed-size placement arrays.',en='A VPS administrator can mount CephFS from a cluster they control. An oversized placement list in an OSD map can make the kernel client write past a fixed-size array on its stack.',cs='Správce VPS může připojit CephFS z clusteru, který ovládá. Příliš dlouhý seznam umístění v mapě OSD může přimět klienta jádra k zápisu za konec pole pevné velikosti na zásobníku.',fcs='Oprava omezuje délky seznamů umístění v mapě OSD před jejich zpracováním.',group='ceph',sources=['fs/ceph/super.c','net/ceph/osdmap.c','net/ceph/osd_client.c']),
'89653':dict(name='Ceph MDS export target stack bitmap overwrite',fix='Reject MDS export target ranks outside CEPH_MAX_MDS before check_new_map uses them as bit indices in its stack bitmap.',en='A VPS administrator can mount CephFS from a cluster they control. An invalid export target in a metadata-server map can make the client set a bit outside a fixed-size bitmap on the kernel stack.',cs='Správce VPS může připojit CephFS z clusteru, který ovládá. Neplatný cíl exportu v mapě metadatových serverů může přimět klienta k nastavení bitu mimo pole pevné velikosti na zásobníku jádra.',fcs='Oprava odmítá neplatná čísla cílů exportu v mapách metadatových serverů.',group='ceph',sources=['fs/ceph/super.c','fs/ceph/mdsmap.c','fs/ceph/mds_client.c']),
'89656':dict(name='Ceph CRUSH bucket workspace overwrite',fix='Require each decoded CRUSH bucket ID to match its array slot, preventing a large bucket from aliasing a smaller bucket workspace.',en='A VPS administrator can mount CephFS from a cluster they control. A malformed CRUSH map can make one placement bucket reuse another bucket’s smaller workspace, causing a write beyond allocated kernel memory.',cs='Správce VPS může připojit CephFS z clusteru, který ovládá. Poškozená mapa CRUSH může přimět jeden blok umístění k použití menšího pracovního prostoru jiného bloku a způsobit zápis za přidělenou paměť jádra.',fcs='Oprava ověřuje, že identifikátor každého bloku mapy CRUSH odpovídá jeho pozici.',group='ceph',sources=['fs/ceph/super.c','net/ceph/osdmap.c','net/ceph/crush/mapper.c']),
}
for n,operation,csoperation in [('64383','FLUSH','vyprázdnění zápisu'),('64384','CHANGE_NOTIFY','oznámení změny'),('64385','IOCTL','řídicí operace'),('64386','QUERY_INFO','dotaz na metadata'),('64387','QUERY_DIRECTORY','výpis adresáře'),('64597','CLOSE','uzavření souboru')]:
 META[n]=dict(name='CIFS SMB2 '+operation+' replay double-free',group='cifs',en='If an operator has prepared or delegated a CIFS mount, a malicious SMB2/3 server can return a replayable error to an '+operation+' request. If the next attempt fails before replacing the response buffer, cleanup can free the old buffer twice.',cs='Pokud správce node připravil nebo předal připojený souborový systém CIFS, škodlivý server SMB2/3 může vrátit chybu umožňující opakování požadavku '+operation+' ('+csoperation+'). Jestliže další pokus selže před nahrazením vyrovnávací paměti odpovědi, úklid ji může uvolnit podruhé.',fix='Reset the response-buffer pointer and ownership type before each replay attempt.',fcs='Oprava před každým opakováním požadavku vynuluje ukazatel odpovědi i záznam o vlastnictví její paměti.',sources=['fs/smb/client/smb2pdu.c','fs/smb/client/cifsfs.c','fs/super.c'])
META['89633']=dict(name='CIFS SMB1 TRANS2 response coalescing heap overwrite',group='cifs',en='If an operator has prepared or delegated an SMB1 CIFS mount, a malicious server can supply unchecked offsets in multipart TRANS2 responses. Combining the responses can read or overwrite memory beyond the kernel response buffers. Legacy SMB1 must be negotiated; ordinary VPS administrators cannot create this mount through a tenant user namespace.',cs='Pokud správce node připravil nebo předal připojený souborový systém CIFS s protokolem SMB1, škodlivý server může poslat nekontrolované offsety ve vícedílných odpovědích TRANS2. Jejich spojení pak může číst nebo přepisovat paměť za vyrovnávacími pamětmi odpovědí v jádře. Musí být vyjednán starší protokol SMB1; běžný správce VPS takové připojení v uživatelském jmenném prostoru vytvořit nemůže.',fix='Validate both source and destination data areas against the complete response bounds before copying or modifying headers.',fcs='Oprava před kopírováním nebo změnou hlaviček ověřuje meze zdrojové i cílové oblasti odpovědi.',sources=['fs/smb/client/smb1ops.c','fs/smb/client/cifsfs.c','fs/super.c'])
for n,name,en,cs,fix,fcs in [
 ('80585','MPTCP data-less Fast Open state confusion','A data-less TCP Fast Open SYN can incorrectly mark an MPTCP subflow as carrying early data. Later handshake processing can accept inconsistent connection state.','SYN bez dat při TCP Fast Open může chybně označit dílčí spojení MPTCP jako spojení s časnými daty. Pozdější zpracování navázání spojení pak může přijmout nekonzistentní stav.','Mark the MPTCP Fast Open subflow only after confirming queued SYN data.','Oprava označí dílčí spojení pro Fast Open až po ověření, že SYN skutečně obsahoval data.'),
 ('80586','MPTCP malformed DSS option stale fields','A malformed MPTCP data-sequence option can leave flags set while its sequence fields were not initialized. A following option can make the connection consume inconsistent mapping or acknowledgment data.','Chybná volba MPTCP s datovými pořadovými čísly může ponechat nastavené příznaky, přestože její číselná pole nebyla inicializována. Následující volba pak může přimět spojení ke zpracování nekonzistentních údajů mapování nebo potvrzení.','Clear all DSS-related flags when the option length is invalid.','Oprava při neplatné délce volby vynuluje všechny související příznaky.'),
 ('80587','MPTCP conflicting suboption state confusion','Conflicting or duplicate MPTCP suboptions can be combined into inconsistent connection state. A remote peer can influence acknowledgment, data mapping and connection management.','Konfliktní nebo opakované dílčí volby MPTCP se mohou sloučit do nekonzistentního stavu spojení. Vzdálený protějšek tak může ovlivnit potvrzování, mapování dat a správu spojení.','Reject incompatible incoming MPTCP suboption combinations.','Oprava odmítá nepřípustné kombinace příchozích dílčích voleb MPTCP.')]:
 META[n]=dict(name=name,group='mptcp',en=en,cs=cs,fix=fix,fcs=fcs,sources=['net/mptcp/fastopen.c' if n=='80585' else 'net/mptcp/options.c','net/mptcp/ctrl.c','net/mptcp/protocol.c'])

for n,name,en,cs,fix,fcs,paths in [
('72463','XFRM asynchronous receive device use-after-free','A VPS administrator can configure IPsec and an XFRM or VTI interface in the VPS network namespace. Asynchronous receive processing can release the wrong network device reference after a callback changes the packet’s device, leaving a freed tunnel device in use.','Správce VPS může v síťovém jmenném prostoru VPS nastavit IPsec a rozhraní XFRM nebo VTI. Asynchronní zpracování přijatého paketu může po změně rozhraní v callbacku uvolnit odkaz na nesprávné síťové zařízení, a poté použít již uvolněné zařízení tunelu.','Preserve the original packet device reference and extend RCU protection across receive callbacks and transport completion.','Oprava zachovává odkaz na původní zařízení paketu a chrání zpracování callbacků i dokončení přenosu před souběžným rušením zařízení.',['net/xfrm/xfrm_input.c','net/xfrm/xfrm_interface_core.c','net/ipv4/ip_vti.c']),
('98229','XFRM input state use-after-free after secpath reset','A VPS administrator can configure IPsec state and relevant interfaces, then race state deletion with received traffic. Resetting the packet’s security path can release its final state reference while receive processing still reads the released object.','Správce VPS může nastavit stav IPsec a příslušná rozhraní a souběžně rušit stav při příjmu paketů. Zrušení bezpečnostní cesty paketu může uvolnit poslední odkaz na stav, zatímco zpracování příjmu z uvolněného objektu dále čte.','Save the needed protocol and address-family values before callbacks or error paths can reset the security path.','Oprava ukládá potřebné údaje o protokolu a rodině adres před callbacky nebo chybovými cestami, které mohou bezpečnostní cestu zrušit.',['net/xfrm/xfrm_input.c','net/xfrm/xfrm_interface_core.c','net/ipv4/ip_vti.c']),
('98368','ESP zerocopy managed page reference corruption','A VPS administrator can configure IPsec in the VPS network namespace. Local io_uring sends using registered zerocopy buffers can reach ESP output that changes fragment ownership without taking the required page references, allowing a registered page to be released while it remains in use.','Správce VPS může v síťovém jmenném prostoru VPS nastavit IPsec. Lokální odesílání přes io_uring s registrovanými buffery bez kopírování může dosáhnout výstupní cesty ESP, která změní vlastnictví fragmentů bez potřebných odkazů na stránky. Registrovaná stránka se pak může uvolnit, přestože se stále používá.','Convert managed fragment references to ordinary page references before ESP changes the fragment array.','Oprava před změnou pole fragmentů v ESP převede spravované odkazy na běžné odkazy na stránky.',['net/ipv4/esp4.c','net/ipv6/esp6.c','net/xfrm/xfrm_user.c']),
('98370','XFRM compat ALLOCSPI translated request use-after-free','A VPS administrator using the32-bit compatibility interface can send an IPsec ALLOCSPI request. Redundant translation attaches a temporary child buffer to the request; a concurrent compatibility receiver can access that buffer after request cleanup frees it.','Správce VPS může přes32bitové kompatibilní rozhraní poslat požadavek IPsec ALLOCSPI. Opakovaný překlad připojí k požadavku dočasný podřízený buffer, k němuž může souběžný kompatibilní příjemce přistoupit po jeho uvolnění při úklidu požadavku.','Remove the redundant request translation while retaining the correct response translation.','Oprava odstraňuje nadbytečný překlad požadavku a zachovává správný překlad odpovědi.',['net/xfrm/xfrm_user.c']),
('89783','XFRM IPv6 full security path pointer overwrite','If the host makes Mobile IPv6 support available, a VPS administrator can configure matching IPsec state. A packet with a full security path and a Mobile IPv6 option can write one state pointer beyond its array, within the containing kernel allocation.','Pokud hostitel zpřístupní podporu Mobile IPv6, správce VPS může nastavit odpovídající stav IPsec. Paket s plnou bezpečnostní cestou a volbou Mobile IPv6 může zapsat jeden ukazatel na stav za konec pole, ale stále uvnitř přiděleného objektu jádra.','Reject an already-full security path before appending another state pointer.','Oprava odmítá již plnou bezpečnostní cestu před přidáním dalšího ukazatele na stav.',['net/ipv6/xfrm6_input.c','net/ipv6/mip6.c','net/ipv6/exthdrs.c','net/xfrm/xfrm_user.c'])]:
 META[n]=dict(name=name,group='xfrm',en=en,cs=cs,fix=fix,fcs=fcs,sources=paths)

def norm(v):return v+'.0'if len(v.split('.'))==2 else v
def key(v):return tuple(map(int,re.match(r'\d+(?:\.\d+)*',v)[0].split('.')))
def boundaries(c):
 r=R[c];vv=[v for a in r['affected']for v in a['versions']];globalintro=next(v['version']for v in vv if v['status']=='affected'and'lessThan'not in v and'lessThanOrEqual'not in v and v.get('versionType')!='git');globalfix=next(v['version']for v in vv if v.get('versionType')=='original_commit_for_fix');gits=[v for v in vv if v.get('versionType')=='git'];fixes=[v for v in vv if v['status']=='unaffected'and'lessThanOrEqual'in v and v.get('versionType')=='semver'];gitfixes=list(dict.fromkeys(v['lessThan']for v in gits if 'lessThan'in v));assert len(gitfixes)==len(fixes)+1,(c,len(gitfixes),len(fixes))
 rules={};mainintro=next(v['version']for v in gits if v.get('lessThan')==gitfixes[-1])
 for f,sha in zip(fixes,gitfixes[:-1]):
  branch='.'.join(f['version'].split('.')[:2]);intro=norm(globalintro)if branch=='.'.join(globalintro.split('.')[:2])else branch+'.0';explicit=[v for v in vv if v.get('versionType')=='semver'and v['status']=='affected'and'lessThan'in v and v['version'].startswith(branch+'.')]
  if explicit:intro=explicit[0]['version']
  gi=next(v['version']for v in gits if v.get('lessThan')==sha)
  rules[branch]={'affected_from':intro,'fixed_in':norm(f['version']),'introduced_commit':gi,'fixed_commit':sha}
 # Explicit affected backport branch without a same-branch fix (e.g.6.19.13).
 for v in vv:
  if v.get('versionType')!='semver'or v['status']!='affected'or'lessThan'not in v:continue
  branch='.'.join(v['version'].split('.')[:2])
  if branch not in rules:rules[branch]={'affected_from':norm(v['version']),'fixed_in':None}
 # Known LTS/EOL branches after global introduction are covered by CNA default affected.
 for branch in ['2.6.32','3.2','3.4','3.10','3.12','3.14','3.16','3.18','4.1','4.4','4.9','4.14','4.19','5.4','5.10','5.15','6.1','6.6','6.12','6.18']:
  if len(branch.split('.'))!=2 or branch in rules or key(branch)<key('.'.join(globalintro.split('.')[:2]))or key(branch)>=key(globalfix):continue
  rules[branch]={'affected_from':norm(globalintro)if branch=='.'.join(globalintro.split('.')[:2])else branch+'.0','fixed_in':None,'introduced_commit':mainintro}
 if c=='CVE-2026-64387':rules['6.12']['fixed_in']=None;rules['6.12'].pop('fixed_commit',None)
 return norm(globalintro),norm(globalfix),dict(sorted(rules.items(),key=lambda x:key(x[0]))),gitfixes[-1],mainintro

def render(c):
 n=c.split('-')[-1];m=META[n];r=R[c];req=REQ[c];intro,fix,rules,mainsha,introsha=boundaries(c);group=m['group'];stable=r['fixes'][0];humanfix=stable['release'];generic='This path already requires administrator access inside the VPS. Corruption of shared kernel memory could compromise the node and other VPSes, but the reviewed primary record and fix do not establish a complete exploit on vpsFree.cz. A failed trigger can crash the shared kernel. Kernel warnings that may indicate this bug was triggered are monitored.';gcs='Tato cesta již vyžaduje oprávnění správce uvnitř VPS. Poškození paměti sdíleného jádra by mohlo ohrozit node i ostatní VPS, ale analyzovaný primární záznam a oprava nepopisují úplný postup zneužití na vpsFree.cz. Neúspěšný pokus může shodit sdílené jádro. Hlášení jádra, která mohou naznačovat spuštění této chyby, jsou monitorována.'
 response=f'Upstream Linux includes the fix from {humanfix} on the 6.12 branch. '+m['fix'];rcs=f'Ve větvi Linuxu 6.12 je oprava obsažena od verze {humanfix}. '+m['fcs']
 if n=='74730':response+=' Historical cumulative vpsAdminOS live patch 6.12.95.6 also carries this correction; its inclusion does not establish activation on an individual node.';rcs+=' Opravu obsahuje také historický kumulativní vpsAdminOS live patch 6.12.95.6; její přítomnost sama nepotvrzuje aktivaci na konkrétním node.'
 platform={k:req[k]for k in ['history_required_since','affected_node_roles','required_options','required_sysctls']};platform.update(configuration_assessed=True,accepted_kernel_builds=[],accepted_livepatches=[],accepted_ebpf_programs=[])
 
 if group=='cifs':
  generic='The ordinary VPS mount path is blocked by this filesystem’s namespace restriction. If the prerequisite mount exists, the corruption could affect the shared kernel and other VPSes; the reviewed primary record and patch do not establish a complete exploit on vpsFree.cz. A failed trigger can crash the node. Kernel warnings that may indicate this bug was triggered are monitored.';gcs='Běžná cesta připojení z VPS je u tohoto souborového systému omezena uživatelským jmenným prostorem. Pokud požadované připojení existuje, poškození paměti může zasáhnout sdílené jádro i ostatní VPS; analyzovaný primární záznam a oprava však nepopisují úplný postup zneužití na vpsFree.cz. Neúspěšný pokus může shodit node. Hlášení jádra, která mohou naznačovat spuštění této chyby, jsou monitorována.'
 if group=='mptcp':
  generic='The archived vpsAdminOS Linux6.12.95 build has MPTCP disabled, so this path is unavailable in that build. The reviewed primary record describes connection-state corruption and availability failures on enabled kernels; it does not establish VPS-root gain, node takeover or cross-VPS access. This conclusion does not extend to uninspected kernels or historical overrides.';gcs='Archivované sestavení vpsAdminOS s Linuxem6.12.95 má MPTCP vypnuté, a tato cesta v něm proto není dostupná. Analyzovaný primární záznam popisuje poškození stavu spojení a výpadky dostupnosti v jádrech se zapnutým MPTCP; neprokazuje získání root ve VPS, ovládnutí node ani přístup do jiného VPS. Tento závěr se nevztahuje na neověřená jádra nebo historické změny konfigurace.'
 d={'schema_version':1,'cve':c,'name':m['name'],'affected_from':intro,'fixed_from':fix,'version_rules':rules,'platform':platform,'impact':{'vps_root':'not_applicable','node_root':'possible','cross_vps':'possible','node_availability':'plausible'},'texts':{'en':{'summary':'Kernel memory corruption','description':m['en']+' '+generic,'response':response},'cs':{'summary':'Poškození paměti jádra','description':m['cs']+' '+gcs,'response':rcs}}}
 if group=='xfrm' and n=='98368':d['impact']['vps_root']='possible'
 if group=='xfrm' and n=='89783':d['impact']['node_root']='unknown';d['impact']['cross_vps']='unknown'
 if group=='mptcp':
  d['impact']={'vps_root':'unlikely','node_root':'unknown','cross_vps':'unknown','node_availability':'plausible'};d['texts']['en']['summary']='Network connection state corruption';d['texts']['cs']['summary']='Poškození stavu síťového spojení'
 dest=W/'advisories'/c;dest.mkdir(exist_ok=True);(dest/'advisory.yml').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
 sourcelinks='\n'.join(f'- [Current pinned Linux `{p}`](https://github.com/vpsfreecz/linux/blob/{L}/{p})'for p in m['sources']);versiontable='\n'.join(f"| {b} | {v['affected_from']} | {v['fixed_in']or'No same-branch fix listed; open-ended'} | {v.get('introduced_commit','Explicit CNA stable interval')} | {v.get('fixed_commit','—')} |"for b,v in rules.items());metric=json.dumps(r['metrics'],ensure_ascii=False,indent=2)
 reach={'nfs':'NFS/NFS4 are registered with downstream FS_USERNS_MOUNT. Current LXC namespace mapping retains namespace CAP_SYS_ADMIN and the short seccomp denylist does not block mount or ordinary file activity. NFS client modules are explicitly preloaded. A tenant administrator can mount a controlled NFS server; no host block device is required. The exact NFS version, callbacks and teardown/failure sequence remain prerequisites. Storage hosts serve backup data over NFS; that server workload alone does not establish this client-side tenant mount trigger. Roles are therefore node only.', 'xfrm':'XFRM netlink control checks netlink_net_capable(CAP_NET_ADMIN), so tenant user/network namespace administration can configure its own security associations and deletion without initial-userns authority. LXC default seccomp does not block the relevant networking or io_uring calls. XFRM/XFRM_USER are built in; ESP4/ESP6, XFRM_INTERFACE and XFRM_USER_COMPAT are built in in the exact .95 configuration. VTI is a module and optional modules must be separately available where required. Alternate XFRM-interface or max-depth paths prevent requiring VTI as a universal gate. IPV6_MIP6=m compiles receive call sites through IS_ENABLED but the mip6 module registers required destination/routing XFRM types; it is absent from preload and autoload defaults off. Actual loaded types, cryptographic algorithm, packet state,32-bit compatibility workloads and zerocopy mode are candidate-specific predicates. Storage backup/NFS workloads do not establish tenant-configured IPsec, so roles are node only.', 'cifs':'CIFS and smb3 filesystem types lack FS_USERNS_MOUNT in both exact archived .95 and current pinned .113. fs/super denies a non-initial-userns superblock for these filesystems. CIFS module preload and namespace CAP_SYS_ADMIN therefore do not let an ordinary tenant mount an attacker-selected share. A host-prepared/delegated mount or actual host CIFS client workload is required. The source-described replay sequence needs a response-bearing replayable error and failure before the next response replaces buffer ownership; SMB1 additionally needs legacy dialect negotiation. No storage CIFS-client workload is established by backup/NFS-server source, so scope is node only, conditional on such a mount. This optional workload is not a claim that default VPS operation reaches CIFS. The evaluator cannot represent actual mount delegation; an affected-release result is conservative applicability, not measured exploitation.', 'mptcp':'MPTCP is absent from the exact archived .95 build (CONFIG_MPTCP=n); tenant sysctls cannot enable compiled-out code. The negative conclusion applies to that exact build only. A kernel with MPTCP enabled additionally needs MPTCP sockets and negotiated protocol state; Fast Open defect80585 needs a listening endpoint, server Fast Open and valid cookie. Host net.mptcp.enabled or net.ipv4.tcp_fastopen cannot prove the tenant network namespace setting; namespace network administration can configure its own settings. Storage backup/NFS workload does not establish MPTCP sockets, so role node only under this tenant assessment. Actual kernels/history require the shared snapshot.', 'ceph':'CephFS is registered with FS_USERNS_MOUNT. Current LXC namespace mapping retains namespace CAP_SYS_ADMIN, mount is not in the short seccomp denylist, and ceph/libceph are explicitly preloaded. A tenant administrator can mount a controlled Ceph cluster without an RBD device and feed the shared client decoder/placement code. The primary examples/scenarios explain cluster-peer control; formal AV:N/PR:N does not remove the prerequisite that a Ceph client session exists. Storage backup/NFS-server workload is not evidence of consuming a tenant-supplied Ceph cluster, so roles are node only.'}[group]
 special=''
 if n=='68159':special='The primary KASAN stack uses RBD probing, while its CNA scenario explicitly includes CephFS/libceph client I/O. Source ceph_osdc_start_request/calc_target reaches the same placement path for CephFS. No CephFS reproducer was run. The source supports an out-of-bounds write; speculative arbitrary-read/control-flow consequences in the CNA scoring scenario are not a demonstrated vpsFree.cz exploit.\n'
 if n=='74730':special='Historical coverage maps downstream 6d5cc0d6681c54a1ddf186a4f9872ee1ae062612 to upstream cf616096a0f3a2b60f7d68b6b39674a6867ded9c and first cumulative v6. The NFS-cancellation boot variant needs separate intrinsic-fix/content review. Exact observed module/source/OS tuples are pending the coordinated shared-evidence review; accepted_livepatches remains empty until that gate. Quarantine is a deployment/availability fact and does not erase genuine independently verified historical activation.\n'
 text=f'''# {c} — {m['name']}

Assessment date:2026-10-19. Exact approved60 batch; factual bilingual candidates
await lead editorial review. No exploit was executed, no production conclusion
is inferred from source defaults, and no draft has been synchronized by this owner.

## Primary defect, score and correction

{r['description'][0]['value']}

Correction reviewed in full: {m['fix']}

- [Pinned Linux CNA record]({r['cna_url']}) (PUBLISHED at snapshot56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9)
- [Mainline introduction](https://git.kernel.org/stable/c/{introsha}), first affected {intro}
- [Mainline correction](https://git.kernel.org/stable/c/{mainsha}), first fixed {fix}
- [6.12 stable correction](https://git.kernel.org/stable/c/{stable['sha']}), first fixed {humanfix}

Formal metrics are Linux CNA CVSS source ratings, not a custom container score.
Their exploit-consequence discussion is attributed primary analysis, not proof
that the vpsAdminOS hardening/build was exploited:

```json
{metric}
```

## Complete branch rules and backport lineage

| Branch | First affected | First fixed | Introduction commit | Correction commit |
| --- | --- | --- | --- | --- |
{versiontable}

Global/CNA affected intervals were checked before adding older EOL branches.
A later branch inherits the mainline introduction unless CNA supplies a distinct
stable-backport interval/commit. Open-ended entries preserve affected EOL lines
without inventing a same-branch fix. The mainline global bounds also classify
unlisted releases; a stable backport before the mainline introduction is explicit.
CNA Git-fix references and first-unaffected versions are retained, and exact
Makefile branch checks are recorded in the session version-source manifest.

## Platform prerequisites, exact source and roles

{reach}

{sourcelinks}
- [vpsAdmin feature defaults](https://github.com/vpsfreecz/vpsadmin/blob/{V}/api/models/vps_feature.rb)
- [vpsAdmin device delegation](https://github.com/vpsfreecz/vpsadmin/blob/{V}/libnodectld/lib/nodectld/commands/vps/features.rb)
- [OS module loading policy](https://github.com/vpsfreecz/vpsadminos/blob/{O}/os/modules/config/kernel.nix)
- [OS LXC base config](https://github.com/vpsfreecz/vpsadminos/blob/{O}/osctld/configs/lxc/common.conf)
- [Storage workload source](https://github.com/vpsfreecz/vpsfree-cz-configuration/blob/{C}/cluster/cz.vpsfree/nodes/common/storage.nix)
- [Kernel selection and operational overrides](https://github.com/vpsfreecz/vpsfree-cz-configuration/blob/{C}/configs/node/kernels.nix)

Required interface declarations are {json.dumps(req['required_options'])}.
No host sysctl value is a sufficient generic predicate for this namespace/workload
path, so required_sysctls is empty. Loaded modules, actual mounts/protocol and
LSM state must be checked against the shared typed snapshot where relevant;
source preload and absent AppArmor in the archived build are not universal
runtime claims. Historical archived config is bound to Linux{F} with digest
c10922b492fdf39ed3027b9c8f7ce2846a5d3799d57d417a161595fa81a64969.

## Separate impact and protections

{special}
The impact is conditional on the prerequisite namespace, mount or protocol
setup described above; no initial VPS-root gain is inferred solely from a score. The concrete shared-kernel corruption makes host kernel compromise
and cross-VPS access possible consequences, while reviewed primary reports and
patches do not establish a complete working exploit on this platform. Kernel
oops/panic is a plausible host availability outcome. This is source-scoped
negative evidence only; it says nothing about production exploitation.

Allocator freelist hardening/randomization, zeroing and stack protection in the
archived build may raise exploit difficulty or detect a failed corruption; they
do not repair object lifetime or bounds. Monitored kernel warnings are detection
and availability evidence, not trigger prevention. The corrective code above
remediates this defect; correct activation/history must be independently bound.

## Runtime, history and mitigation evidence

The assessment requests retained history from2026-01-01T00:00:00Z, a reviewed
operational scope rather than a claim about earlier years. No per-node history
start override or historical attestation was copied. Until shared collection and
exact identity/content review, no accepted custom build, livepatch or BPF tuple
is asserted. No extra mitigations are implied by empty arrays.

Evaluate against the one coordinated ignored snapshot; do not recollect per CVE.
Missing current relevant evidence remains unknown. Missing historical config on
affected releases is conservative affected, not retrospective safety. Stable
fixed/pre-introduction releases can classify without configuration. Actual
boot/release transitions and reviewed cumulative-patch tuples determine mitigation
timing; an old livepatch cannot cross a reboot by inference. Unmodeled mount,
peer and workload predicates remain explicit and do not become ignored YAML keys
or manually edited evaluation results. Drafts may retain honest unknowns and do
not imply publication readiness. No API/schema/deployment compatibility change.
'''
 (dest/'analysis.md').write_text(text)
 print(c,'written',len(rules),'branchrules')
if __name__=='__main__':
 for suffix in sys.argv[1:]:render(suffix if suffix.startswith('CVE-')else'CVE-2026-'+suffix)
