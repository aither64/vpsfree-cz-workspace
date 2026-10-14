from pathlib import Path
import subprocess,json,time,datetime,hashlib
T=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter');OUT=T/'finish-runtime-reduction-hosted4';OUT.mkdir()
GH='/nix/store/lmnakv2iy4b8m8saqvwkxywyd76yvypl-gh-2.100.0/bin/gh'
RUNS=json.loads((T/'finish-runtime-reduction-hosted4-runs.json').read_text())
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
