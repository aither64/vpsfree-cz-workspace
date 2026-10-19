import hashlib,json,os,subprocess
from pathlib import Path
root=Path('/home/aither/workspace/ai/vpsfree.cz');t=root/'work/2026-10-13-workspace-coordination'
def read(path):return json.loads(path.read_text())
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
assert (t/'operations-bootstrap-prepare.status').read_text().strip()=='0'
prepared=read(t/'operations-bootstrap-prepared.json');request=read(t/'operations-bootstrap-execution-request.json');assert prepared['request']==request
frozen=read(t/'operations-acceptance-evidence.json')
for name,item in frozen['files'].items():assert sha(t/name)==item['sha256'],name
for item in request['evidence']:assert sha(root/item['path'])==item['sha256'],item['path']
assert request['requestId']==read(t/'operations-bootstrap-prepare-request.json')['requestId']
for name,head in frozen['heads'].items():
 repo=root/'worktrees/2026-10-13-workspace-coordination'/name
 assert subprocess.check_output(['git','-C',str(repo),'rev-parse','HEAD'],text=True).strip()==head
 assert not subprocess.check_output(['git','-C',str(repo),'status','--porcelain'],text=True)
assert (t/'operations-candidate-gc-root').resolve()==Path(frozen['candidatePackage'])
artifactRoot=Path('/home/aither/.local/state/dev-workspaces/coordination/sources')
def artifact(digest):return read(artifactRoot/digest.removeprefix('sha256:')/'artifact.json')
profile=artifact(request['profileArtifact']);machine=artifact(request['machineSnapshot']['operation']['preparedArtifact'])
assert profile['candidatePackage']==frozen['candidatePackage'] and profile['source']==prepared['source']
assert machine['toplevel']==frozen['systemPackage']
assert request['machineSnapshot']['operation']['configurationHead']==frozen['heads']['vpsfree-cz-configuration']
assert profile['profileToken']==(t/'operations-bootstrap-predecessor-token').read_text().strip()
live=json.loads(subprocess.check_output(['python3',str(t/'capture-live.py')],text=True))
baseline=read(t/'operations-activation-baseline.json')
for path in ['/run/current-system','/nix/var/nix/profiles/system','/home/aither/.local/state/dev-workspaces/profile']:assert live[path]==baseline[path],path
for key in ['bootId','runningKernel']:assert live[key]==baseline[key],key
for service in ['workspace-codex@vpsfree-cz.service','workspace-codex-provider@vpsfree-cz.service']:assert live['services'][service]==baseline['services'][service]
env=dict(os.environ,DEV_SESSION_SLUG='2026-10-13-workspace-coordination',DEV_SESSION_WORKSPACE=str(root))
status=json.loads(subprocess.check_output(['dev-session','coordination','status','2026-10-13-workspace-coordination','--as-is','--json','--bootstrap-owner','55e83d75-cb96-417a-9308-11d3caf22dcd'],env=env,text=True))
assert len(status['owners'])==1 and len(status['jobs'])==2 and all(job['state']=='succeeded' for job in status['jobs'])
reservation=next(r for r in status['reservations'] if r['id']=='d114323d-806c-479f-b7a4-8c1a08afb45b')
assert reservation['ownerId']=='55e83d75-cb96-417a-9308-11d3caf22dcd' and reservation['state']=='deployed_review'
(t/'operations-execution-preflight-live.json').write_text(json.dumps(live,indent=2)+'\n')
(t/'operations-execution-preflight-status.json').write_text(json.dumps(status,indent=2)+'\n')
print(json.dumps({'outcome':'passed','candidate':profile['candidatePackage'],'system':machine['toplevel'],'requestId':request['requestId'],'reservationId':reservation['id']}))
