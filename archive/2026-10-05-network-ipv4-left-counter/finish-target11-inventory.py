from pathlib import Path
import json,subprocess,hashlib,datetime
T=Path(__file__).resolve().parent
old=json.loads((T/'finish-api-fixture10-inventory.json').read_text())
rows=[]
for r in old['rows']:
 r=dict(r);p=r['worktree']
 if r['key']=='d': r['base']='7c07b540a5e45cac4b39351f713cf3528e4df614'
 if r['key']=='c': r['base']='bfb1d89c95308024a9269974c207bf7cefe1fb1c'
 def g(*a):return subprocess.check_output(['git','-C',p,*a])
 r['head']=g('rev-parse','HEAD').decode().strip();r['tree']=g('rev-parse','HEAD^{tree}').decode().strip()
 r['merge_base']=g('merge-base',r['base'],r['head']).decode().strip();assert r['merge_base']==r['base']
 r['clean']=not g('status','--porcelain');assert r['clean']
 r['commits']=g('log','--reverse','--format=%H %s',r['base']+'..'+r['head']).decode().splitlines()
 r['merge_commits']=g('rev-list','--merges',r['base']+'..'+r['head']).decode().splitlines();assert not r['merge_commits']
 r['artifacts']={}
 for name,args in [('diff',['diff','--binary','--full-index',r['base'],r['head']]),('history',['log','--reverse','--format=fuller','--date=iso-strict',r['base']+'..'+r['head']])]:
  f='finish-target11-inventory-'+r['key']+'.'+name;b=g(*args);(T/f).write_bytes(b)
  r['artifacts'][name]={'path':f,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
 rows.append(r)
assert [len(r['commits']) for r in rows]==[6,1,2,3,3,2]
v={**old,'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'rows':rows,'consolidation':'Four original network V owners plus two separate inherited fixture corrections. C two final channels on current bfb. D three equivalent feature owners on7c07 with upstream provider admission retained. E single paired-input owner selects final D including codex-web5f15, separate unchanged provider. No repeated selector tail. V/W/K/G/media exact.','limits':'V hosted proof closed. New D/E hosted evidence and affected review pending; no configuration build, default integration, deployment/activation/publication or lifecycle authority.'}
(T/'finish-target11-inventory.json').write_text(json.dumps(v,indent=2)+'\n')
print(json.dumps({'counts':[len(r['commits']) for r in rows],'heads':{r['key']:r['head'] for r in rows}}))
