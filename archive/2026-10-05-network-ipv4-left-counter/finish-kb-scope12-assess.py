from pathlib import Path
import json,hashlib,re,zipfile
T=Path(__file__).resolve().parent;O=T/'finish-kb-scope12-hosted'
summary=json.loads((O/'summary.json').read_bytes())
for name,digest in summary['sha256'].items():
 assert hashlib.sha256((O/name).read_bytes()).hexdigest()==digest,name
rows=[]
counter=r'(\d+) runs, (\d+) assertions, (\d+) failures, (\d+) errors, (\d+) skips'
node_pattern=r'(?:#|ℹ) (tests|suites|pass|fail|cancelled|skipped|todo) (\d+)'
for item in summary['runs']:
 D=O/item['key'];run=json.loads((D/'final.json').read_bytes());initial=json.loads((D/'initial.json').read_bytes())
 assert run['id']==initial['id']==item['id']
 assert run['head_sha']==initial['head_sha']==item['head']
 assert run['status']=='completed' and run['run_attempt']==1
 assert run['conclusion']==item['conclusion']
 assert item['log_exit']==item['zip_exit']==0
 assert not (D/'log-command.stderr').read_bytes() and not (D/'zip-command.stderr').read_bytes()
 log=(D/'full.log').read_text();assert item['head'] in log
 raw_counts=[list(map(int,m)) for m in re.findall(counter,log)]
 with zipfile.ZipFile(D/'logs.zip') as z:
  assert z.testzip() is None
  primary=[(n,z.read(n).decode()) for n in z.namelist() if '/' not in n]
  assert primary
  zip_counts=[list(map(int,m)) for n,s in primary for m in re.findall(counter,s)]
 assert sorted(raw_counts)==sorted(zip_counts)
 assert sorted(re.findall(node_pattern,log))==sorted(m for n,s in primary for m in re.findall(node_pattern,s))
 assert all(int(value)==0 for key,value in re.findall(node_pattern,log) if key in ('fail','cancelled'))
 jobs=json.loads((D/'final-jobs.json').read_bytes())['jobs']
 steps=[{'job':j['name'],'job_id':j['id'],'job_conclusion':j['conclusion'],'step':s['name'],'conclusion':s['conclusion']} for j in jobs for s in j['steps']]
 if item['key'].startswith('k-'):
  assert run['event']=='workflow_dispatch'
  strict=[s for s in steps if s['step']=='Run strict repository checks'];assert len(strict)==1 and strict[0]['conclusion']=='success'
  assert 'Valid inventory: 60 concepts, 120 variants,' in log
  assert 'nix develop --command bin/check' in log
  assert 'ℹ tests 119' in log and 'ℹ pass 119' in log
 assert all(c[2]==0 and c[3]==0 for c in raw_counts),raw_counts
 assert all(j['conclusion']=='success' for j in jobs)
 rows.append({**item,'attempt':run['run_attempt'],'jobs':[{'id':j['id'],'name':j['name'],'conclusion':j['conclusion']} for j in jobs],'ruby_counters':raw_counts,'node_counters':re.findall(node_pattern,log),'steps':steps,'raw_log_sha256':hashlib.sha256((D/'full.log').read_bytes()).hexdigest(),'zip_primary_log_members':[n for n,s in primary]})
result={'schema':1,'result':'passed' if all(r['conclusion']=='success' for r in rows) else 'mixed','summary_sha256':hashlib.sha256((O/'summary.json').read_bytes()).hexdigest(),'collector_hash_count':len(summary['sha256']),'all_collector_hashes_match':True,'raw_zip_counters_agree':True,'rows':rows,'limits':'K strict full source and retained120-image validation; E package/configuration runner checks. Real skips retained. No new guest/capture/activation/deployment/integration; old G/M receipts remain historical.'}
(T/'finish-kb-scope12-acceptance.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'result':result['result'],'hashes':result['collector_hash_count'],'rows':[{'id':r['id'],'conclusion':r['conclusion'],'jobs':r['jobs'],'ruby_unique':sorted({tuple(c) for c in r['ruby_counters']})} for r in rows]}))
