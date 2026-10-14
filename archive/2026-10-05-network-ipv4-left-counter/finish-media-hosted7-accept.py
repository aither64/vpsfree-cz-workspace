from pathlib import Path
import json,hashlib,re,datetime
T=Path(__file__).resolve().parent;D=T/'finish-media-hosted7';s=json.loads((D/'summary.json').read_text())
for name,digest in s['sha256'].items():assert hashlib.sha256((D/name).read_bytes()).hexdigest()==digest
assert len(s['sha256'])==36
rows=[]
for item in s['runs']:
 assert item['conclusion']=='success' and item['log_exit']==item['zip_exit']==0
 d=D/item['key'];native=json.loads((d/'final.json').read_text());jobs=json.loads((d/'final-jobs.json').read_text());assert native['head_sha']==item['head'] and native['status']=='completed' and native['conclusion']=='success'
 steps=[{'name':x['name'],'conclusion':x['conclusion']} for j in jobs['jobs'] for x in j['steps']];log=(d/'full.log').read_text()
 ruby=[list(map(int,m)) for m in re.findall(r'(\d+) runs, (\d+) assertions, (\d+) failures, (\d+) errors, (\d+) skips',log)]
 node={k:[int(x) for x in re.findall(r'(?:#|ℹ) '+k+r' (\d+)',log)] for k in ('tests','pass','fail','cancelled','skipped','todo')}
 assert ruby and all(x[2]==x[3]==0 for x in ruby)
 assert all(x==0 for k in ('fail','cancelled','todo') for x in node[k])
 if item['key']!='e':
  strict = item['key']=='strict-k'
  assert next(x for x in steps if x['name']=='Run source repository checks')['conclusion']==('skipped' if strict else 'success')
  assert next(x for x in steps if x['name']=='Run strict repository checks')['conclusion']==('success' if strict else 'skipped')
  if strict: assert native['event']=='workflow_dispatch' and native['id']==38307863150
  assert item['head']=='706b9d8c18edde528af4fb5279786491aedd47fa'
  assert node['tests']==node['pass'] and node['tests'][0]==106 and all(x==0 for x in node['skipped'])
  assert all(x[-1]==0 for x in ruby)
 else:
  assert item['head']=='dc94c8f60b4e869ce738f4c242459cc5cadf1b3d'
  assert next(x for x in steps if 'nix flake check' in x['name'])['conclusion']=='success'
  assert next(x for x in steps if 'devcluster-check' in x['name'])['conclusion']=='success'
  assert [8,68,0,0,0] in ruby and [5,58,0,0,0] in ruby
 rows.append({**item,'steps':steps,'ruby_counters':ruby,'node_counters':node,'full_log_sha256':hashlib.sha256((d/'full.log').read_bytes()).hexdigest()})
v={'schema':1,'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'result':'passed','scope':'Exact final media M706b9d8 source/runtime/strict full inventory and paired E source/package gates. Only two images fresh; actual guest/capture generator remains Gd0b4f407, not media recording M. Broader D/E environment skips retained.','rows':rows,'artifact_count':36,'summary_sha256':hashlib.sha256((D/'summary.json').read_bytes()).hexdigest(),'sha256':s['sha256']}
p=T/'finish-media-hosted7-acceptance1.json';assert not p.exists();p.write_text(json.dumps(v,indent=2)+'\n');print(json.dumps({'result':'passed','rows':[{k:x[k] for k in ('key','id','head','conclusion','node_counters')} for x in rows]}))
