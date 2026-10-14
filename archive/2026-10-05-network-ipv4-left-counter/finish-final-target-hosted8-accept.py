from pathlib import Path
import json, hashlib, re, datetime, zipfile, io
T = Path(__file__).resolve().parent
D = T/'finish-final-target-hosted8'
s = json.loads((D/'summary.json').read_text())
for name,digest in s['sha256'].items():
 assert hashlib.sha256((D/name).read_bytes()).hexdigest() == digest, name
expected = {
 'vpsfreecz/vpsadmin':'f778f762047bff3f4bd725fbb73882f65babdd65',
 'aither64/dev-workspace':'16d949b39e162870cc21a6f23d2d138b2e642887',
 'vpsfreecz/dev-workspace':'78463762fcf79b94ae026ea1acc3a36354938cd1'}
rows=[]
for item in s['runs']:
 d=D/item['key'];native=json.loads((d/'final.json').read_text());jobs=json.loads((d/'final-jobs.json').read_text())
 assert item['head']==expected[item['repo']]
 assert native['head_sha']==item['head'] and native['head_branch']=='2026-10-05-network-ipv4-left-counter'
 assert native['id']==item['id'] and native['status']=='completed'
 assert item['conclusion']==native['conclusion']=='success',item
 assert item['log_exit']==item['zip_exit']==0
 assert zipfile.ZipFile(io.BytesIO((d/'logs.zip').read_bytes())).testzip() is None
 steps=[{'job':j['name'],'job_conclusion':j['conclusion'],'name':x['name'],'conclusion':x['conclusion']} for j in jobs['jobs'] for x in j['steps']]
 assert all(j['head_sha']==item['head'] and j['status']=='completed' and j['conclusion'] in ('success','skipped') for j in jobs['jobs'])
 log=(d/'full.log').read_text()
 ruby=[list(map(int,m)) for m in re.findall(r'(\d+) runs, (\d+) assertions, (\d+) failures, (\d+) errors, (\d+) skips',log)]
 examples=[{'examples':int(a),'failures':int(b),'pending':int(c) if c else 0} for a,b,c in re.findall(r'(\d+) examples?, (\d+) failures?(?:, (\d+) pending)?',log)]
 node={k:[int(x) for x in re.findall(r'(?:#|ℹ) '+k+r' (\d+)',log)] for k in ('tests','pass','fail','cancelled','skipped','todo')}
 assert all(x[2]==x[3]==0 for x in ruby)
 assert all(x['failures']==0 for x in examples)
 assert all(x==0 for k in ('fail','cancelled','todo') for x in node[k])
 if item['repo']=='vpsfreecz/dev-workspace':
  assert [8,68,0,0,0] in ruby and [5,58,0,0,0] in ruby
  assert next(x for x in steps if 'nix flake check' in x['name'])['conclusion']=='success'
  assert next(x for x in steps if 'devcluster-check' in x['name'])['conclusion']=='success'
 elif item['repo']=='aither64/dev-workspace':
  assert next(x for x in steps if x['name']=='Evaluate all checks')['conclusion']=='success'
  assert next(x for x in steps if x['name']=='Build package and focused checks')['conclusion']=='success'
 rows.append({**item,'steps':steps,'ruby_counters':ruby,'rspec_counters':examples,'node_counters':node,'full_log_sha256':hashlib.sha256((d/'full.log').read_bytes()).hexdigest()})
assert set(x['repo'] for x in rows)==set(expected)
vnames={x['name'] for x in rows if x['repo']=='vpsfreecz/vpsadmin'}
assert {'API Specs (topic parallel)','CI'}<=vnames,vnames
result={'schema':1,'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'result':'passed','scope':'Exact changed-head V/D/E hosted checks. C mechanical pins not a configuration build/deployment result; K/media retain separately closed exact evidence.','rows':rows,'artifact_count':len(s['sha256']),'summary_sha256':hashlib.sha256((D/'summary.json').read_bytes()).hexdigest(),'sha256':s['sha256'],'limits':'Native pending/skips retained as recorded. Rebase push does not change PHP/migration paths; their prior reviewed unchanged-blob evidence is retained separately, without claiming new-head reruns. No installation/guest/deployment/default-integration/publication claim. Only two PNGs fresh.'}
p=T/'finish-final-target-hosted8-acceptance1.json';assert not p.exists();p.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'result':'passed','artifact_count':result['artifact_count'],'runs':[{k:r[k] for k in ('repo','id','name','head','conclusion')} for r in rows]}))
