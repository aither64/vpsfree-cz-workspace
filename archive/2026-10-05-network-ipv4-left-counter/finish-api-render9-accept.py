from pathlib import Path
import json,hashlib,re,zipfile,io,datetime
T=Path(__file__).resolve().parent
D=T/'finish-api-render9-hosted'
s=json.loads((D/'summary.json').read_text())
for name,digest in s['sha256'].items():
 assert hashlib.sha256((D/name).read_bytes()).hexdigest()==digest,name
head='59097cb4d67b732b0539f2db93a111013ee92555'
rows=[]
for r in s['runs']:
 d=D/r['key'];n=json.loads((d/'final.json').read_text());j=json.loads((d/'final-jobs.json').read_text())
 assert r['head']==n['head_sha']==head
 assert r['id']==n['id'] and n['head_branch']=='2026-10-05-network-ipv4-left-counter'
 assert n['status']=='completed' and n['conclusion']==r['conclusion']=='success',r
 assert r['log_exit']==r['zip_exit']==0
 assert zipfile.ZipFile(io.BytesIO((d/'logs.zip').read_bytes())).testzip() is None
 assert all(x['status']=='completed' and x['conclusion'] in ('success','skipped') and x['head_sha']==head for x in j['jobs'])
 log=(d/'full.log').read_text()
 rspec=[{'examples':int(a),'failures':int(b),'pending':int(c) if c else 0} for a,b,c in re.findall(r'(\d+) examples?, (\d+) failures?(?:, (\d+) pending)?',log)]
 assert all(x['failures']==0 for x in rspec)
 steps=[{'job':x['name'],'name':y['name'],'conclusion':y['conclusion']} for x in j['jobs'] for y in x['steps']]
 if r['name']=='API Specs (topic parallel)':
  assert len(j['jobs'])==27 and len(rspec)==26
  for mode in ('core','full'):
   job=next(x for x in j['jobs'] if x['name']=='API specs ('+mode+') - foundation');assert job['conclusion']=='success'
   source='\n'.join(x for x in log.splitlines() if x.startswith('API specs ('+mode+') - foundation\tRun RSpec (topic)'))
   assert 'renders singular and plural subjects, text and HTML for each message selection' in source
   assert re.search(r'1432 examples, 0 failures',source),mode
  assert next(x for x in j['jobs'] if x['name']=='API specs - topic coverage')['conclusion']=='success'
 rows.append({**r,'steps':steps,'rspec_counters':rspec,'full_log_sha256':hashlib.sha256((d/'full.log').read_bytes()).hexdigest()})
assert 'API Specs (topic parallel)' in {r['name'] for r in rows}
p=T/'finish-api-render9-acceptance1.json';assert not p.exists()
v={'schema':1,'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'result':'passed','head':head,'rows':rows,'artifact_count':len(s['sha256']),'sha256':s['sha256'],'summary_sha256':hashlib.sha256((D/'summary.json').read_bytes()).hexdigest(),'Important_disposition':'Requested narrow inherited fixture initialization directly inspected under step9; fresh canonical corrected-source core/full API matrices and aggregate pass. Original f778 run38310941934 remains failed.','limits':'No original seed27800 replay or isolated cold-process reproduction claimed. Original V full118 integration/database/PHP passes retained with exact protected production bytes. D/E/K/media unchanged. No new guest, config build, deployment/integration/publication/activation claim.'}
p.write_text(json.dumps(v,indent=2)+'\n');print(json.dumps({'result':'passed','head':head,'rows':[{k:r[k] for k in ('id','name','conclusion')} for r in rows]}))
