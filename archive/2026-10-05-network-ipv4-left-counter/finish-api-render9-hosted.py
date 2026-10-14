from pathlib import Path
import subprocess, json, time, datetime, hashlib
T = Path(__file__).resolve().parent
OUT = T/'finish-api-render9-hosted'
OUT.mkdir()
GH = '/nix/store/lmnakv2iy4b8m8saqvwkxywyd76yvypl-gh-2.100.0/bin/gh'
branch = '2026-10-05-network-ipv4-left-counter'
selected = [('v', 'vpsfreecz/vpsadmin', (T/'finish-api-render9.head').read_text().strip())]
def api(repo,suffix):
 return subprocess.check_output([GH,'api','repos/'+repo+'/actions/'+suffix])
def save(path,data):
 with path.open('xb') as f: f.write(data)
RUNS=[]
for prefix,repo,head in selected:
 raw=api(repo,'runs?branch='+branch+'&per_page=100')
 observed=json.loads(raw)['workflow_runs']
 save(OUT/(prefix+'-discovery.json'),raw)
 matches=[r for r in observed if r['head_sha']==head and r['head_branch']==branch and r['event']=='push']
 assert matches, (prefix,'no exact push run')
 if prefix!='v': matches=[r for r in matches if r['name']=='Check'];assert len(matches)==1
 for r in matches:
  RUNS.append({'key':prefix+'-'+str(r['id']),'repo':repo,'id':r['id'],'head':head,'name':r['name']})
 for r in observed:
  if r['head_branch']==branch and r['head_sha']!=head and r['status'] in ('queued','in_progress'):
   subprocess.run([GH,'run','cancel',str(r['id']),'--repo',repo],check=True,capture_output=True)
save(OUT/'runs.json',(json.dumps(RUNS,indent=2)+'\n').encode())
print(json.dumps({'selected_runs':RUNS}),flush=True)
started=datetime.datetime.now(datetime.timezone.utc).isoformat()
pending={};results=[]
for item in RUNS:
 directory=OUT/item['key'];directory.mkdir()
 raw=api(item['repo'],'runs/'+str(item['id']));assert json.loads(raw)['head_sha']==item['head']
 save(directory/'initial.json',raw)
 save(directory/'initial-jobs.json',api(item['repo'],'runs/'+str(item['id'])+'/jobs?per_page=100'))
 pending[item['key']]=(item,directory)
start=time.monotonic();escalated=False
while pending:
 for key,(item,directory) in list(pending.items()):
  repo,id=item['repo'],item['id'];raw=api(repo,'runs/'+str(id));run=json.loads(raw);assert run['head_sha']==item['head']
  if run['status']!='completed':continue
  save(directory/'final.json',raw)
  save(directory/'final-jobs.json',api(repo,'runs/'+str(id)+'/jobs?per_page=100'))
  save(directory/'artifacts.json',api(repo,'runs/'+str(id)+'/artifacts?per_page=100'))
  p=subprocess.run([GH,'run','view',str(id),'--repo',repo,'--log'],capture_output=True)
  save(directory/'full.log',p.stdout);save(directory/'log-command.stderr',p.stderr)
  z=subprocess.run([GH,'api','repos/'+repo+'/actions/runs/'+str(id)+'/logs'],capture_output=True)
  save(directory/'logs.zip',z.stdout);save(directory/'zip-command.stderr',z.stderr)
  result={**item,'conclusion':run['conclusion'],'log_exit':p.returncode,'zip_exit':z.returncode}
  results.append(result);del pending[key];print(json.dumps(result),flush=True)
 if pending and not escalated and time.monotonic()-start>=1200:
  escalated=True;print('ESCALATION observer target20minutes '+json.dumps([x[0] for x in pending.values()]),flush=True)
 if pending:time.sleep(30)
summary={'started_at':started,'finished_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'runs':results,'sha256':{str(p.relative_to(OUT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(OUT.rglob('*')) if p.is_file()}}
save(OUT/'summary.json',(json.dumps(summary,indent=2)+'\n').encode())
print('Closed native evidence; no retry or acceptance',flush=True)
