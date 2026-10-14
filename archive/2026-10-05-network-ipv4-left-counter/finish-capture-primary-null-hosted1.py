from pathlib import Path
import subprocess,json,time,datetime,hashlib
T=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter');OUT=T/'finish-capture-primary-null-hosted1';OUT.mkdir()
GH='/nix/store/lmnakv2iy4b8m8saqvwkxywyd76yvypl-gh-2.100.0/bin/gh'
RUNS=[]
expected_e='87908ab13a1c01d7f4117d70a70606e6854c2450'
for key,repo,branch,head in [
 ('k','vpsfreecz/vpsfree-kb-contracts','2026-10-05-network-ipv4-left-counter','d0b4f40708cc8b59aab7c91ae05fba695abc233c'),
 ('runtime-k','vpsfreecz/vpsfree-kb-contracts','2026-10-05-network-ipv4-left-counter-kb-runtime','d0b4f40708cc8b59aab7c91ae05fba695abc233c'),
 ('e','vpsfreecz/dev-workspace','2026-10-05-network-ipv4-left-counter',expected_e)]:
 while True:
  raw=subprocess.check_output([GH,'api','repos/'+repo+'/actions/runs?head_sha='+head+'&event=push&per_page=100'])
  matches=[r for r in json.loads(raw)['workflow_runs'] if r['head_sha']==head and r['head_branch']==branch and r['name']=='Check' and r['event']=='push']
  if matches:
   assert len(matches)==1
   RUNS.append([key,repo,matches[0]['id'],head]);print(json.dumps({'admitted_check':RUNS[-1]}),flush=True);break
  time.sleep(10)
(T/'finish-capture-primary-null-hosted1-runs.json').write_text(json.dumps(RUNS,indent=2)+'\n')
# Mandatory cancellation of only superseded runs on these owned feature refs.
for repo,branch,current in [('vpsfreecz/vpsfree-kb-contracts','2026-10-05-network-ipv4-left-counter','d0b4f40708cc8b59aab7c91ae05fba695abc233c'),('vpsfreecz/vpsfree-kb-contracts','2026-10-05-network-ipv4-left-counter-kb-runtime','d0b4f40708cc8b59aab7c91ae05fba695abc233c'),('vpsfreecz/dev-workspace','2026-10-05-network-ipv4-left-counter',expected_e)]:
 raw=subprocess.check_output([GH,'api','repos/'+repo+'/actions/runs?branch='+branch+'&per_page=100'])
 for r in json.loads(raw)['workflow_runs']:
  if r['head_branch']==branch and r['head_sha']!=current and r['status'] in ('queued','in_progress'):
   subprocess.run([GH,'run','cancel',str(r['id']),'--repo',repo],check=True,stdout=subprocess.DEVNULL)

# No new hosted guest campaign is selected. Cancel only named Managed jobs on these owned current refs.
managed=[]
for branch in ('2026-10-05-network-ipv4-left-counter','2026-10-05-network-ipv4-left-counter-kb-runtime'):
 raw=subprocess.check_output([GH,'api','repos/vpsfreecz/vpsfree-kb-contracts/actions/runs?branch='+branch+'&per_page=100'])
 for r in json.loads(raw)['workflow_runs']:
  if r['head_branch']==branch and r['head_sha']=='d0b4f40708cc8b59aab7c91ae05fba695abc233c' and r['name']=='Managed page runtime':
   managed.append({'id':r['id'],'head':r['head_sha'],'branch':branch,'status':r['status'],'conclusion':r['conclusion']})
   if r['status'] in ('queued','in_progress'):
    subprocess.run([GH,'run','cancel',str(r['id']),'--repo','vpsfreecz/vpsfree-kb-contracts'],check=True,stdout=subprocess.DEVNULL)
(T/'finish-capture-primary-null-hosted1-managed.json').write_text(json.dumps(managed,indent=2)+'\n')

def save(path,data):
 with path.open('xb') as f:f.write(data)
def api(repo,suffix):return subprocess.check_output([GH,'api','repos/'+repo+'/actions/'+suffix])
started=datetime.datetime.now(datetime.timezone.utc).isoformat();pending={};results=[]
for key,repo,id,head in RUNS:
 directory=OUT/key;directory.mkdir();raw=api(repo,'runs/'+str(id));run=json.loads(raw);assert run['head_sha']==head
 save(directory/'initial.json',raw);save(directory/'initial-jobs.json',api(repo,'runs/'+str(id)+'/jobs?per_page=100'));pending[key]=(repo,id,head,directory)
observer_start=time.monotonic();escalated=False
while pending:
 for key,(repo,id,head,directory) in list(pending.items()):
  raw=api(repo,'runs/'+str(id));run=json.loads(raw);assert run['head_sha']==head
  if run['status']!='completed':continue
  save(directory/'final.json',raw);save(directory/'final-jobs.json',api(repo,'runs/'+str(id)+'/jobs?per_page=100'))
  save(directory/'artifacts.json',api(repo,'runs/'+str(id)+'/artifacts?per_page=100'))
  p=subprocess.run([GH,'run','view',str(id),'--repo',repo,'--log'],capture_output=True);save(directory/'full.log',p.stdout);save(directory/'log-command.stderr',p.stderr)
  z=subprocess.run([GH,'api','repos/'+repo+'/actions/runs/'+str(id)+'/logs'],capture_output=True);save(directory/'logs.zip',z.stdout);save(directory/'zip-command.stderr',z.stderr)
  result={'key':key,'repo':repo,'id':id,'head':head,'conclusion':run['conclusion'],'log_exit':p.returncode,'zip_exit':z.returncode};results.append(result);del pending[key];print(json.dumps(result),flush=True)
 if pending and not escalated and time.monotonic()-observer_start>=1200:
  escalated=True;print("ESCALATION 20-minute observer target: "+json.dumps({key:{"repo":v[0],"run":v[1],"head":v[2]} for key,v in pending.items()}),flush=True)
 if pending:time.sleep(30)
summary={'started_at':started,'finished_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'runs':results,'sha256':{str(p.relative_to(OUT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(OUT.rglob('*')) if p.is_file()}}
save(OUT/'summary.json',(json.dumps(summary,indent=2)+'\n').encode());print('Hosted evidence retained; no retry or acceptance',flush=True)
