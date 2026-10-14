#!/usr/bin/env python3
"""Create one fixed private reduced configuration; never alter retained campaigns."""
import datetime,hashlib,json,os,pathlib,secrets,socket
T=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
a=json.loads((T/'finish-corrected-package-realize1-acceptance.json').read_text());g=json.loads((T/'finish-corrected-qualification-architect-acceptance2.json').read_text());stop=json.loads((T/'finish-corrected-g13-stop-acceptance1.json').read_text());assert a['accepted'] and a['generator']==g['source'] and g['one_fresh_qualification_selected'] and stop['accepted']
base=pathlib.Path('/home/aither/.local/state/vpsfree-kb-verification');st=base.lstat();assert base.is_dir() and not base.is_symlink() and st.st_uid==os.getuid() and st.st_mode&0o777==0o700
private=base/'2026-10-05-network-ipv4-left-counter-g14';assert not os.path.lexists(private)
c=json.loads((pathlib.Path(a['source'])/'cluster/default-config.json').read_text());c['services'].update(memoryMiB=2048,rootDiskMiB=8192)
node=c['nodes']['node1'];node.update(memoryMiB=2048,tankDiskGiB=8);c['nodes']={'node1':node};c['topologies']={'single':['node1']};c['dns']['enable']=False;c['resolver']={'mode':'cluster','upstreamNameservers':['10.0.2.3']}
c['local']={'bindAddress':'127.0.0.1','multicastPort':25420,'ports':{'services':{'ssh':25400,'https':25410},'node1':{'ssh':25401}}}
for group in ['domains','tmpDomains']:
 c[group]={name:name.lower()+('.tmp' if group=='tmpDomains' else '')+'.kb14.example.test' for name in c[group]}
for dns in c['dns']['servers'].values():dns['serverName']=dns['name']+'.kb14.example.test'
c['mail']['capture']['webAuth']['password']=secrets.token_urlsafe(24)
c['adminer']['webAuth']['password']=secrets.token_urlsafe(24)
c['seed']['users']=[{'login':login,'password':secrets.token_urlsafe(24),'fullName':label,'email':login+'@example.test','level':level,'namespace':{'blockStart':start,'blockCount':8}} for login,label,level,start in [('test-admin','Test Administrator',99,1),('test-user1','Test Member One',1,9),('test-user2','Test Member Two',1,17)]]
# Every password value is new; no G13 configuration or credentials are imported.
assert len(c['seed']['users'])==3
assert len({c['mail']['capture']['webAuth']['password'],c['adminer']['webAuth']['password'],*[u['password']for u in c['seed']['users']]})==5
# Probe only the four requested resources. No scan, fallback, or claim release.
opened=[]
try:
 for kind,port in [(socket.SOCK_STREAM,25400),(socket.SOCK_STREAM,25401),(socket.SOCK_STREAM,25410),(socket.SOCK_DGRAM,25420)]:
  s=socket.socket(socket.AF_INET,kind);opened.append(s);s.bind(('127.0.0.1' if kind==socket.SOCK_STREAM else '',port))
finally:
 for s in opened:s.close()
private.mkdir(mode=0o700);config=private/'config.json';fd=os.open(config,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o600)
with os.fdopen(fd,'w') as f:json.dump(c,f,indent=2);f.write('\n')
r={'schema':1,'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'generator':a['generator'],'private_parent':str(private),'campaign_root':str(private/'campaign'),'configuration':{'path':str(config),'sha256':hashlib.sha256(config.read_bytes()).hexdigest()},'profile':{'services_memory_mib':2048,'node1_memory_mib':2048,'root_image_mib':8192,'tank_gib':8},'ports':c['local'],'fixed_one_attempt':True,'accounts_exported':False,'all_five_password_values_fresh':True,'g13_config_or_credentials_copied':False,'old_campaigns_touched':False,'registry':'same ordinary XDG_RUNTIME_DIR and per-user registry; engine still performs ordinary claim/bind admission','real_admission':False}
with (T/'finish-corrected-private-config1.json').open('x') as f:json.dump(r,f,indent=2);f.write('\n')
print(json.dumps({'configuration_created':True,'receipt':'finish-corrected-private-config1.json','real_admission':False}))
