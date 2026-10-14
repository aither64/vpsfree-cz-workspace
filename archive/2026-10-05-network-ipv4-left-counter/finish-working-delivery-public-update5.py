"""One selected same-instance public update, with separate immutable evidence."""
from pathlib import Path
import datetime,hashlib,json,os,re,shlex,stat,subprocess,sys,textwrap
os.umask(0o077)
T=Path(__file__).resolve().parent
prep=json.loads((T/'finish-working-delivery-public-update5-preparation.json').read_text())
packet=json.loads(Path(prep['packet_path']).read_text())
a=json.loads((T/'finish-working-delivery-package-realize5-acceptance.json').read_text());s=a['selection']
mode=sys.argv[1];assert mode in ('preflight','post')
context=Path(prep['context'])/('observation-'+mode);context.mkdir(mode=0o700)
root=Path(packet['campaign_root']);directory=root/'state/clusters/same-slug';env=packet['environment']
metadata=json.loads(Path(s['metadata']).read_text())
before=json.loads((root/'accepted-runtime.json').read_text());base=json.loads((root/'continuity.json').read_text())
oldmeta=before['provenance']['source'];commands=[];stage='existing-source-attestation';failure=None;current=None
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,v):
 with Path(p).open('x') as f:json.dump(v,f,indent=2);f.write('\n')
def call(name,argv,data='',cwd='/home/aither'):
 d=context/name;d.mkdir(mode=0o700)
 with (d/'stdout').open('xb') as out,(d/'stderr').open('xb') as err:
  r=subprocess.run(argv,input=data.encode(),stdout=out,stderr=err,cwd=cwd,env=env)
 row={'name':name,'stage':stage,'exit_code':r.returncode,'stdout_sha256':sha(d/'stdout'),'stderr_sha256':sha(d/'stderr')};commands.append(row);write(d/'native.json',row)
 if r.returncode:raise RuntimeError('native public command failed; private diagnostics retained')
 return (d/'stdout').read_bytes()
def engine(name,args,data=''):
 return call(name,[s['runtime']+'/bin/vpsfree-kb-devcluster','--state-root',str(root/'state'),args[0],'same-slug',*args[1:]],data)
def descriptor(name,expected):
 raw=engine(name,['connection']);v=json.loads(raw);assert v['provenance']['source']==expected
 assert sorted(v['machines'])==['node1','services']
 p=context/(name+'.json');p.write_bytes(raw)
 for machine,closure in v['provenance']['machine_toplevels'].items():
  identity=json.loads(engine(name+'-'+machine+'-identity',['ssh',machine,'--','cat','/etc/vpsfree-kb-capture.json']))
  assert identity==v['provenance']['guest_identity']
  actual=engine(name+'-'+machine+'-system',['ssh',machine,'--','readlink','-f','/run/current-system']).decode().strip();assert actual==closure
 return v,p
original={p:sha(p) for p in [root/'accepted-runtime.json',root/'continuity.json',root/'receipts/runtime-smoke.json',root/'receipts/runtime-smoke-attempt.json',root/'receipts/bilingual-capture-attempt.json']}
def continuity(v,label):
 expected=base['identities']
 for name,digest in expected['credentials'].items():
  p=directory/'credentials'/name;x=p.lstat();assert stat.S_ISREG(x.st_mode) and x.st_uid==os.getuid() and stat.S_IMODE(x.st_mode)==0o600 and sha(p)==digest
 assert sha(directory/'accounts.json')==expected['accounts_sha256']
 assert sha(directory/'credentials/known_hosts')==prep['known_hosts_sha256']
 for name,value in expected['disks'].items():
  x=(directory/'disks'/name).lstat();assert stat.S_ISREG(x.st_mode) and x.st_uid==os.getuid();assert {'device':x.st_dev,'inode':x.st_ino,'size':x.st_size}==value
 for name,digest in expected['artifacts'].items():assert sha(directory/name)==digest
 for path,digest in original.items():assert sha(path)==digest
 for machine,digest in base['sentinels'].items():
  sentinel='/root/kb-root-sentinel' if machine=='services' else '/tank/kb-data-sentinel'
  observed=engine(label+'-'+machine+'-sentinel',['ssh',machine,'--','sha256sum',sentinel]).decode().split()[0];assert observed==digest
 assert v['instance_id']==before['instance_id']
def capacity():
 fs=os.statvfs(prep['filesystem_path']);free=fs.f_bavail*fs.f_frsize
 ram=int(next(x for x in Path('/proc/meminfo').read_text().splitlines() if x.startswith('MemAvailable:')).split()[1])*1024
 shm=os.statvfs('/dev/shm');available_shm=shm.f_bavail*shm.f_frsize
 assert free>=prep['disk_required_bytes'] and ram>=6*1024**3 and available_shm>=5*1024**3
 write(context/'fresh-admission.json',{'free_bytes':free,'required_bytes':prep['disk_required_bytes'],'ram_available_bytes':ram,'shm_available_bytes':available_shm,'additional_ram_bytes':6*1024**3,'additional_shm_bytes':5*1024**3})
def resources(label):
 # Use the selected verifier's exact generated shell, through public SSH.
 owner=Path(s['source'])/'tools/runtime-verify.rb'
 body=owner.read_text().split('    def resource_script(machine)\n',1)[1].split('    def resources(',1)[0]
 blocks=[textwrap.dedent(x) for x in re.findall(r"<<~'SH'\n(.*?)^\s*SH$",body,re.M|re.S)]
 assert len(blocks)==3
 observed={}
 for machine,extra in [('services',blocks[1]),('node1',blocks[2])]:
  output=engine(label+'-'+machine+'-resources',['ssh',machine,'--','sh','-s'],blocks[0]+extra).decode()
  numeric={k:int(v) for k,v in re.findall(r'^([a-z_]+)=([0-9]+)$',output,re.M)}
  wanted=['available_memory_bytes','available_bytes','available_inodes'] if machine=='services' else ['available_memory_bytes','tank_available_bytes']
  assert sorted(numeric)==sorted(wanted)
  observed[machine]=dict(numeric,pressure='\n'.join(x for x in output.splitlines() if not re.fullmatch(r'[a-z_]+=[0-9]+',x)))
 assert observed['services']['available_bytes']>=1024**3 and observed['services']['available_inodes']>=10000
 write(context/(label+'-resources.json'),{'observations':observed,'source_script_sha256':sha(owner),'capture_admitted':False})
try:
 assert a['accepted'] and a['generator']==prep['generator'] and sha(prep['configuration_path'])==prep['configuration_sha256']
 if mode=='preflight':
  assert not (directory/'update.json').exists(), 'retained update is not a fresh operation'
  old,_=descriptor('predecessor',oldmeta);assert all(old[k]==before[k] for k in ('instance_id','run_id','artifact_id','artifact_sha256'));continuity(old,'before')
  resources('before')
  stage='fresh-candidate-overlap-admission';capacity()
 else:
  stage='candidate-source-attestation';current,connection=descriptor('candidate',metadata)
  assert current['instance_id']==before['instance_id'] and current['run_id']!=before['run_id'] and current['artifact_id']!=before['artifact_id']
  continuity(current,'after');resources('after')
  proof=json.loads((directory/('processes-'+before['run_id']+'.json')).read_text())
  assert proof['complete'] is True and all(proof[k]==before[k] for k in ('instance_id','run_id','artifact_id','artifact_sha256'))
  stage='new-source-member-api-php-read'
  script=Path(prep['read_smoke_script']).read_text()
  value=json.loads(call('read-smoke',['node','-e',script,str(connection),s['metadata'],s['source']]))
  assert value['api_tls_verified'] is True and value['php_member_read'] is True and value['member']['login']=='test-user1'
  write(context/'member-read.json',value)
  stage='new-source-public-lease-proof'
  call('live-lease',['node',s['source']+'/tools/verify-live-lease.cjs',str(connection),s['metadata'],s['runtime'],str(root/'state'),str(root/'config.json')])
  continuity(current,'final')
except BaseException as e:failure={'stage':stage,'class':type(e).__name__}
finally:
 value={'schema':1,'mode':mode,'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'generator':prep['generator'],'previous_generator':oldmeta['revision'],'complete':failure is None,'failure':failure,'commands':commands,'source_ids':{k:current[k] for k in ('instance_id','run_id','artifact_id','artifact_sha256')} if current else None,'previous_source_ids':{k:before[k] for k in ('instance_id','run_id','artifact_id','artifact_sha256')},'original_receipt_sha256':{str(p):d for p,d in original.items()},'credential_account_trust_disk_sentinel_continuity':failure is None,'old_complete_process_receipt':mode=='post' and failure is None,'public_member_api_php_and_lease':mode=='post' and failure is None,'connection_path':str(context/'candidate.json') if current else None,'limit':'One same-instance public prepared source update and subsequent read/lease proof; no failed Campaign replay, new pair, resize, reset or capture claimed.'}
 write(context/'proof.json',value);write(T/('finish-working-delivery-public-update5-'+('preflight' if mode=='preflight' else 'proof')+'.json'),value)
 print(json.dumps({'complete':value['complete'],'failure':failure,'source_ids':value['source_ids']}),flush=True)
sys.exit(0 if failure is None else 1)
