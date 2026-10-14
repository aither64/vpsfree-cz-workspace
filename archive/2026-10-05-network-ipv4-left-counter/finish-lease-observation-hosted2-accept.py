from pathlib import Path
import json,hashlib,re,datetime
T=Path.cwd(); O=T/'finish-lease-observation-hosted2'; summary=json.loads((O/'summary.json').read_text())
for n,h in summary['sha256'].items():assert hashlib.sha256((O/n).read_bytes()).hexdigest()==h,n
assert len(summary['sha256'])==27
expected={row[0]:row for row in json.loads((T/'finish-lease-observation-hosted2-runs.json').read_text())}; accounts=[]
for row in summary['runs']:
 key,repo,id,head=expected[row['key']];d=O/key;native=json.loads((d/'final.json').read_text());jobs=json.loads((d/'final-jobs.json').read_text());log=(d/'full.log').read_text(errors='replace')
 assert row['id']==native['id']==id and row['head']==native['head_sha']==head and native['status']=='completed' and native['conclusion']=='success' and row['log_exit']==row['zip_exit']==0
 assert jobs['jobs'] and all(j['conclusion']=='success'for j in jobs['jobs'])
 steps={s['name']:s['conclusion']for j in jobs['jobs']for s in j['steps']}
 assert head in log,'raw source checkout/fetch identity absent'
 if key in ['k','runtime-k']:
  assert steps['Run source repository checks']=='success' and steps['Run strict repository checks']=='skipped'
  assert 'nix develop --command bin/check --allow-missing' in log
  for runs,assertions in [(99,1242),(12,51),(34,1244),(33,744),(4,21)]:assert f'{runs} runs, {assertions} assertions, 0 failures, 0 errors, 0 skips' in log
  assert re.search(r'# tests 35\s.*?# suites 0\s.*?# pass 35',log,re.S),'new lease Node suite missing native35 pass'
 else:
  assert steps['Run nix flake check --print-build-logs']=='success' and steps['Run nix run .#devcluster-check']=='success'
  for runs,assertions in [(8,68),(5,58)]:assert f'{runs} runs, {assertions} assertions, 0 failures, 0 errors, 0 skips' in log
 accounts.append({'key':key,'repository':repo,'run':id,'head':head,'conclusion':'success','steps':steps,'full_log_sha256':hashlib.sha256((d/'full.log').read_bytes()).hexdigest()})
proof={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'k':expected['k'][3],'e':expected['e'][3],'all_27_hashes_verified':True,'sha256':summary['sha256'],'runs':accounts,'hosted_source_gate_complete':True,'source_review':'pending independent affected four lanes','strict_media':'skipped; no fresh media claim','local_ci':False,'real_operations':'not admitted or started','selected_suites':{'runtime':'99/1242','closure':'12/51','machine':'34/1244','verifier':'33/744','export':'4/21','lease_inventory_node':'35 native tests;22 parent methods','selected_e_sdk':'8/68','selected_e_public':'5/58'},'broader_skips':'Retain D real-tmux guards12/3 and E existing supplementary-group skip; nonverbose summaries do not identify every D skip.'}
with(T/'finish-lease-observation-hosted2-acceptance.json').open('x')as f:json.dump(proof,f,indent=2);f.write('\n')
print(json.dumps({'all_27_hashes_verified':True,'exact_heads':{'k':proof['k'],'e':proof['e']},'native_pass':True,'review_pending':True}))
