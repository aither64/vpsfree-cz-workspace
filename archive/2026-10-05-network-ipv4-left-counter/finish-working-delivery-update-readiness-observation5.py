import datetime,hashlib,json,os,pathlib,subprocess,sys
os.umask(0o077)
T=pathlib.Path(__file__).resolve().parent
a=json.loads((T/'finish-working-delivery-package-realize5-acceptance.json').read_text());s=a['selection']
old=json.loads((T/'finish-working-delivery-runtime-smoke5-preparation.json').read_text());packet=json.loads(pathlib.Path(old['packet_path']).read_text());root=pathlib.Path(packet['campaign_root'])
context=root.parent/'update-readiness-observation5';context.mkdir(mode=0o700)
env=packet['environment'].copy();env['PATH']=s['path'];before=json.loads((root/'accepted-runtime.json').read_text());records=[];stage='connection';failure=None;resources={}
sha=lambda p:hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def call(name,args):
 d=context/name;d.mkdir(mode=0o700)
 with (d/'stdout').open('xb') as o,(d/'stderr').open('xb') as e:
  r=subprocess.run([s['runtime']+'/bin/vpsfree-kb-devcluster','--state-root',str(root/'state'),args[0],'same-slug',*args[1:]],env=env,stdin=subprocess.DEVNULL,stdout=o,stderr=e,cwd='/home/aither')
 records.append({'name':name,'exit_code':r.returncode,'stdout_sha256':sha(d/'stdout'),'stderr_sha256':sha(d/'stderr')})
 if r.returncode:raise RuntimeError('public command refused; native private diagnostics retained')
 return (d/'stdout').read_bytes()
try:
 current=json.loads(call('connection',['connection']))
 assert all(current[k]==before[k] for k in ['instance_id','run_id','artifact_id','artifact_sha256']) and current['provenance']==before['provenance']
 for machine,closure in current['provenance']['machine_toplevels'].items():
  stage=machine+'-identity';identity=json.loads(call(stage,['ssh',machine,'--','cat','/etc/vpsfree-kb-capture.json']));assert identity==current['provenance']['guest_identity']
  stage=machine+'-system';system=call(stage,['ssh',machine,'--','readlink','-f','/run/current-system']).decode().strip();assert system==closure
  sentinel='/root/kb-root-sentinel' if machine=='services' else '/tank/kb-data-sentinel'
  stage=machine+'-sentinel';digest=call(stage,['ssh',machine,'--','sha256sum',sentinel]).decode().split()[0]
  base=json.loads((root/'continuity.json').read_text());assert digest==base['sentinels'][machine]
  stage=machine+'-free';args=['ssh',machine,'--','df','-B1','--output=avail,iavail','/nix/store'] if machine=='services' else ['ssh',machine,'--','zfs','get','-Hp','-o','value','available','tank']
  output=call(stage,args).decode().splitlines()
  resources[machine]=[list(map(int,line.split())) for line in output if line.strip() and all(x.isdigit() for x in line.split())]
  assert len(resources[machine])==1
except BaseException as e:failure={'stage':stage,'class':type(e).__name__}
value={'schema':1,'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'complete':failure is None,'failure':failure,'previous_generator':before['provenance']['source']['revision'],'source_ids':{k:before[k] for k in ['instance_id','run_id','artifact_id','artifact_sha256']},'commands':records,'resources':resources,'operation_launched':False,'limits':'Fresh ordinary connection/SSH identity/closure/sentinel/resource read only. No new source build/update/fixture/capture or complete qualification.'}
(context/'proof.json').write_text(json.dumps(value,indent=2)+'\n');(T/'finish-working-delivery-update-readiness-observation5.json').write_text(json.dumps(value,indent=2)+'\n')
print(json.dumps({'complete':value['complete'],'failure':failure,'resources':resources}),flush=True);sys.exit(0 if failure is None else 1)
