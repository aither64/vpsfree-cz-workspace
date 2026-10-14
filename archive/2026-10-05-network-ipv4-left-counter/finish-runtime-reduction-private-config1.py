#!/usr/bin/env python3
"""Create one fixed private reduced configuration; never alter retained campaigns."""
import datetime,hashlib,json,os,pathlib,secrets,socket
T=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
a=json.loads((T/'finish-runtime-reduction-package-realize1-acceptance.json').read_text());g=json.loads((T/'finish-runtime-reduction-review-acceptance1.json').read_text());assert a['accepted'] and a['generator']==g['generator'] and g['construction_may_proceed']
base=pathlib.Path('/home/aither/.local/state/vpsfree-kb-verification');st=base.lstat();assert base.is_dir() and not base.is_symlink() and st.st_uid==os.getuid() and st.st_mode&0o777==0o700
private=base/'2026-10-05-network-ipv4-left-counter-g13';assert not os.path.lexists(private)
c=json.loads((pathlib.Path(a['source'])/'cluster/default-config.json').read_text());c['services'].update(memoryMiB=2048,rootDiskMiB=8192)
node=c['nodes']['node1'];node.update(memoryMiB=2048,tankDiskGiB=8);c['nodes']={'node1':node};c['topologies']={'single':['node1']};c['dns']['enable']=False;c['resolver']={'mode':'cluster','upstreamNameservers':['10.0.2.3']}
c['local']={'bindAddress':'127.0.0.1','multicastPort':25320,'ports':{'services':{'ssh':25300,'https':25310},'node1':{'ssh':25301}}}
for group in ['domains','tmpDomains']:
 c[group]={name:name.lower()+('.tmp' if group=='tmpDomains' else '')+'.kb13.example.test' for name in c[group]}
for dns in c['dns']['servers'].values():dns['serverName']=dns['name']+'.kb13.example.test'
c['seed']['users']=[{'login':login,'password':secrets.token_urlsafe(24),'fullName':label,'email':login+'@example.test','level':level,'namespace':{'blockStart':start,'blockCount':8}} for login,label,level,start in [('test-admin','Test Administrator',99,1),('test-user1','Test Member One',1,9),('test-user2','Test Member Two',1,17)]]
# Probe only the four requested resources. No scan, fallback, or claim release.
opened=[]
try:
 for kind,port in [(socket.SOCK_STREAM,25300),(socket.SOCK_STREAM,25301),(socket.SOCK_STREAM,25310),(socket.SOCK_DGRAM,25320)]:
  s=socket.socket(socket.AF_INET,kind);opened.append(s);s.bind(('127.0.0.1' if kind==socket.SOCK_STREAM else '',port))
finally:
 for s in opened:s.close()
private.mkdir(mode=0o700);config=private/'config.json';fd=os.open(config,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o600)
with os.fdopen(fd,'w') as f:json.dump(c,f,indent=2);f.write('\n')
r={'schema':1,'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'generator':a['generator'],'private_parent':str(private),'campaign_root':str(private/'campaign'),'configuration':{'path':str(config),'sha256':hashlib.sha256(config.read_bytes()).hexdigest()},'profile':{'services_memory_mib':2048,'node1_memory_mib':2048,'root_image_mib':8192,'tank_gib':8},'ports':c['local'],'fixed_one_attempt':True,'accounts_exported':False,'old_campaigns_touched':False,'registry':'same ordinary XDG_RUNTIME_DIR and per-user registry; engine still performs ordinary claim/bind admission','real_admission':False}
with (T/'finish-runtime-reduction-private-config1.json').open('x') as f:json.dump(r,f,indent=2);f.write('\n')
print(json.dumps({'configuration_created':True,'receipt':'finish-runtime-reduction-private-config1.json','real_admission':False}))
