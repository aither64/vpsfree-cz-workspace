from pathlib import Path
import json,subprocess,os,http.client,socket
tracking=Path(__file__).resolve().parent
workspace=tracking.parents[1]
slug=tracking.name
jobs=json.loads((tracking/'activation-jobs.json').read_text())
ledger=json.loads(Path('/home/aither/.local/state/dev-workspaces/coordination/ledger.json').read_text())
for key in ['machine','profile']:
    job=ledger['jobs'][jobs[key]]
    assert job['state']=='succeeded', (key,job['state'],job.get('reason'))
    assert job['ownerId']==ledger['reservations'][jobs['reservation']]['ownerId']
snapshot_path=tracking/'machine-refresh-snapshot.json'
if not snapshot_path.exists(): snapshot_path=tracking/'machine-snapshot.json'
snapshot=json.loads(snapshot_path.read_text())
artifact_id=snapshot['operation']['preparedArtifact'].removeprefix('sha256:')
artifact=json.loads((Path('/home/aither/.local/state/dev-workspaces/coordination/sources')/artifact_id/'artifact.json').read_text())
current=os.path.realpath('/run/current-system');system_profile=os.path.realpath('/nix/var/nix/profiles/system')
assert current==system_profile==artifact['toplevel']
text=(tracking/'profile-prepare.stdout').read_text();profile_snapshot=json.JSONDecoder().raw_decode(text[text.index('{'):])[0]
selected=os.path.realpath('/home/aither/.local/state/dev-workspaces/profile')
assert selected==profile_snapshot['operation']['candidatePackage']
class UnixHTTP(http.client.HTTPConnection):
    def connect(self):
        self.sock=socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)
        self.sock.connect('/run/user/1000/dev-workspaces/vpsfree-cz/portal.sock')
connection=UnixHTTP('localhost',timeout=15);connection.request('GET','/healthz');r=connection.getresponse();health=json.loads(r.read());connection.close();assert r.status==200 and health['ok']
services=['workspace-portal@vpsfree-cz','workspace-codex@vpsfree-cz','workspace-router','workspace-coordinator']
for service in services:
    subprocess.run(['systemctl','--user','is-active',service],check=True,stdout=subprocess.DEVNULL)
assert ledger['reservations']['1ce9be0f-bd17-4c85-ab64-1a94fd352c4c']['state']=='released'
assert ledger['reservations'][jobs['reservation']]['state']=='deployed_review'
result={'runtime':'6ab3b48f57981f4358094b47cac1ba724c458396','system':current,'profile':selected,'jobs':jobs,'oldReservation':'released','services':'active','portalHealth':health}
(tracking/'deployment-acceptance.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
