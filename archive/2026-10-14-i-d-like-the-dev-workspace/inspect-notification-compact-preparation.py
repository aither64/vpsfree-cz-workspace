"""Lead exact artifact inspection; read-only native identities, no activation."""
from pathlib import Path
import hashlib,json,subprocess
root=Path(__file__).resolve().parent
rev='8cb1c0e545e1343d311f7cb9405eee83c468b4a6'
def load(name):return json.loads((root/name).read_text())
def digest(v):return 'sha256:'+hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
heads={x['repository']:x['head'] for x in load('notification-compact-final-heads.json')['repositories']}
summary={}
for mode in ['machine','profile']:
 s=load(mode+'-prepared-notification-compact-8cb1c0e5.json');assert digest({k:v for k,v in s.items() if k!='id'})==s['id']
 o=s['operation'];coverage={x['repository']:x['revision'] for x in o['coverage']}
 assert coverage['dev-workspace']==rev
 assert coverage['vpsfree-cz-configuration' if mode=='machine' else 'workspace']==heads['vpsfree-cz-configuration' if mode=='machine' else 'workspace']
 a_id=o['preparedArtifact'];p=Path('/home/aither/.local/state/dev-workspaces/coordination/sources')/a_id.removeprefix('sha256:')/'artifact.json';a=json.loads(p.read_text());assert a['id']==a_id and digest({k:v for k,v in a.items() if k!='id'})==a_id
 for ev in s['evidence']:assert hashlib.sha256(Path(ev['path']).read_bytes()).hexdigest()==ev['sha256']
 row={'snapshot':s['id'],'artifact':a_id,'coverage':coverage,'artifactDigestVerified':True,'evidenceVerified':True}
 if mode=='machine':
  assert a['configurationRevision']==heads['vpsfree-cz-configuration']
  assert a['environmentPackage']==str((root/'notification-compact-confctl-environment-root').resolve())
  assert Path(a['environmentPackage']+'/bin/workspace-confctl-environment').is_file()
  assert subprocess.check_output(['git','-C',a['source'],'rev-parse','HEAD'],text=True).strip()==heads['vpsfree-cz-configuration']
  row.update({'toplevel':a['toplevel'],'environmentPackage':a['environmentPackage'],'autoRollback':a['autoRollback'],'expectedLive':o['expectedLive']})
 else:
  assert coverage['vpsfree-dev-workspace']=='767dfd587e346168e1443e65ccdb67ce748f3fe3' and coverage['codex-web']=='5f15b9293f9b1eef7469a34d7b2044c743160283'
  assert o['expectedProfileToken']==s['preparedGeneration']['profileToken']
  assert Path(o['candidatePackage']).is_dir()
  row.update({'candidatePackage':o['candidatePackage'],'expectedProfileToken':o['expectedProfileToken']})
 summary[mode]=row
live=subprocess.check_output(['ssh','-o','BatchMode=yes','-o','ConnectTimeout=8','-o','LogLevel=ERROR','root@172.16.106.40','readlink -f /run/current-system /nix/var/nix/profiles/system /home/aither/.local/state/dev-workspaces/profile'],text=True,timeout=20).splitlines()
assert live==[summary['machine']['expectedLive']['runningSystem'],summary['machine']['expectedLive']['systemProfile'],load('profile-prepared-notification-compact-8cb1c0e5.json')['preparedGeneration']['package']]
summary.update({'schema':1,'runtimeRevision':rev,'decision':'accepted','livePredecessorMatches':True,'livePredecessor':live,'orderedActions':['machine_activate','profile_activate'],'reboot':False,'activationPerformed':False})
with (root/'notification-compact-preparation-inspection.json').open('x') as f:json.dump(summary,f,indent=2);f.write('\n')
print(json.dumps(summary,indent=2))
