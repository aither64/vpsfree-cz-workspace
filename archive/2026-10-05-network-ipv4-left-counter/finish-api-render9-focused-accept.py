from pathlib import Path
import json,hashlib,re,zipfile,io,datetime
T=Path(__file__).resolve().parent
D=T/'finish-api-render9-hosted'
head='59097cb4d67b732b0539f2db93a111013ee92555'
runs=json.loads((D/'runs.json').read_text())
required={'API Specs (topic parallel)','RuboCop','i18n health'}
assert required <= {r['name'] for r in runs}
rows=[]; hashes={}; observed=[]
for r in runs:
 d=D/r['key']
 if r['name'] not in required:
  observed.append({**r,'acceptance':'not included in focused correction gate; watcher retains observation'})
  continue
 n=json.loads((d/'final.json').read_text());j=json.loads((d/'final-jobs.json').read_text())
 assert r['head']==n['head_sha']==head and r['id']==n['id']
 assert n['head_branch']=='2026-10-05-network-ipv4-left-counter'
 assert n['status']=='completed' and n['conclusion']=='success' and n['run_attempt']==1
 assert zipfile.ZipFile(io.BytesIO((d/'logs.zip').read_bytes())).testzip() is None
 assert all(x['status']=='completed' and x['conclusion']=='success' and x['head_sha']==head for x in j['jobs'])
 log=(d/'full.log').read_text()
 counters=[{'examples':int(a),'failures':int(b),'pending':int(c) if c else 0} for a,b,c in re.findall(r'(\d+) examples?, (\d+) failures?(?:, (\d+) pending)?',log)]
 assert all(x['failures']==0 for x in counters)
 if r['name']=='API Specs (topic parallel)':
  assert len(j['jobs'])==27 and len(counters)==26
  for mode in ('core','full'):
   job=next(x for x in j['jobs'] if x['name']=='API specs ('+mode+') - foundation')
   source='\n'.join(x for x in log.splitlines() if x.startswith('API specs ('+mode+') - foundation\tRun RSpec (topic)'))
   assert 'renders singular and plural subjects, text and HTML for each message selection' in source
   assert re.search(r'1432 examples, 0 failures',source)
  assert next(x for x in j['jobs'] if x['name']=='API specs - topic coverage')['conclusion']=='success'
 for p in d.iterdir():
  if p.is_file():hashes[str(p.relative_to(D))]=hashlib.sha256(p.read_bytes()).hexdigest()
 rows.append({**r,'conclusion':n['conclusion'],'jobs':[{'id':x['id'],'name':x['name'],'conclusion':x['conclusion']} for x in j['jobs']],'rspec_counters':counters})
# Native foundation result JSONs are collected separately and required by repository guidance.
A=T/'finish-api-render9-artifacts'
manifest=json.loads((A/'manifest.json').read_text())
assert manifest['run']==next(r['id'] for r in rows if r['name']=='API Specs (topic parallel)')
assert manifest['head']==head
for mode in ('core','full'):
 result=json.loads((A/('rspec-results-'+mode+'-foundation.json')).read_text())
 assert result['summary']['example_count']==1432 and result['summary']['failure_count']==0
 assert result['summary'].get('errors_outside_of_examples_count',0)==0
 example=next(x for x in result['examples'] if x['id'].endswith('ip_release_campaign_spec.rb[1:48]'))
 assert example['status']=='passed' and example['pending_message'] is None
for name,digest in manifest['sha256'].items():assert hashlib.sha256((A/name).read_bytes()).hexdigest()==digest
p=T/'finish-api-render9-focused-acceptance1.json';assert not p.exists()
v={'schema':1,'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'result':'focused correction checks passed','head':head,'rows':rows,'sha256':hashes,'native_foundation_manifest':manifest,'additional_observed_runs':observed,'Important_disposition':'Direct step9 inherited test initialization verified by exact corrected API core/full matrices and aggregate. Original f778 API remains failed.','limits':'No original seed27800 replay or isolated cold-process reproduction. Original full118 production integration evidence retains f778 attribution; production bytes unchanged. Additional full CI remains watcher-owned and is not inferred passed. No config build, new guest, integration/deployment/activation/publication claim.'}
p.write_text(json.dumps(v,indent=2)+'\n');print(json.dumps({'result':v['result'],'head':head,'runs':[(r['id'],r['name']) for r in rows]}))
