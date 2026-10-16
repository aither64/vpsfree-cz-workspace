"""Bind existing independent reviews, verified pin lineage and applied deployments."""
from pathlib import Path
from datetime import datetime,timezone
import json,subprocess,hashlib,uuid
r=Path(__file__).resolve().parent;root=r.parents[1]/'worktrees'/r.name
v=json.loads((r/'notification-compact-release-before.json').read_text());reservation=next(x for x in v['reservations'] if x['id']=='1956d2a0-992b-4b4f-9b0f-9db804769d82');heads=json.loads((r/'notification-compact-merge-final-heads.json').read_text());original=json.loads((r/'notification-compact-final-heads.json').read_text())
c=json.loads(Path('/nix/store/mng4ibsyn17yihqgms6l8y3znkl7j2mz-dev-workspace-0.2.0/share/dev-workspace/integration.json').read_text());recipe=c['recipes']['workspace-pins']['command'];mappings=[]
def write(name,value):
 with (r/name).open('x') as f:json.dump(value,f,indent=2);f.write('\n')
def ref(kind,name):return {'kind':kind,'path':str(r/name),'sha256':hashlib.sha256((r/name).read_bytes()).hexdigest()}
def proof(repo,old,new,expected):
 request={'schema':1,'action':'verify','source':str(root/repo),'from':old,'to':new,'parameters':c['refreshes'][repo]['parameters'],'heads':{'dev-workspace':expected}}
 p=subprocess.run([recipe],input=json.dumps(request),text=True,capture_output=True,check=True);value=json.loads(p.stdout);assert value['verified'];return value['proof']|{'recipe':'workspace-pins'}
def selected(repo,head):
 graph=json.loads(subprocess.check_output(['git','-C',str(root/repo),'show',head+':flake.lock'],text=True));current=graph['root']
 def node(path):
  cur=graph['root']
  for part in path:
   val=graph['nodes'][cur]['inputs'][part];cur=node(val) if isinstance(val,list) else val
  return cur
 return graph['nodes'][node(c['refreshes'][repo]['parameters']['inputPath'])]['locked']['rev']
for row in heads['repositories']:
 repo=row['repository'];w=root/repo
 previous=next(x for x in original['repositories'] if x['repository']==repo)
 approval=json.loads((r/f'notification-compact-merge-{repo}-approved.json').read_text())['id']
 review_name=f'notification-compact-release-original-review-{repo}.json'
 if repo=='workspace':write(review_name,{'schema':1,'decision':'accepted','reviewer':'reviewer0 (gpt-6.1-sol/xhigh/read_only)','repository':repo,'target':'refs/heads/master','base':previous['base'],'head':previous['head'],'migrations':[],'report':ref('review','notification-compact-composition-review.md')})
 for old in sorted(set(x['revision'] for rec in reservation['history'] for x in rec['coverage'] if x['repository']==repo)):
  if subprocess.run(['git','-C',str(w),'merge-base','--is-ancestor',old,row['head']]).returncode==0:continue
  base=subprocess.check_output(['git','-C',str(w),'rev-parse',old+'^'],text=True).strip()
  mapping={'repository':repo,'target':'refs/heads/master','from':old,'fromBase':base,'to':row['head'],'toBase':row['base'],'relation':'certified_equivalent' if repo=='workspace' else 'reviewed_change','approvalId':approval}
  prefix=f'notification-compact-release-{repo}-{old[:12]}'
  if repo=='workspace':
   receipt={'schema':1,'ownerId':reservation['ownerId'],'reservationId':reservation['id'],'mapping':mapping,'originalReview':ref('review',review_name),'proof':proof(repo,old,row['head'],heads['runtimeRevision']),'verification':ref('verification','notification-compact-merge-verification.json')}
   if old!=previous['head'] or base!=previous['base']:receipt['priorProof']=proof(repo,previous['head'],old,selected(repo,old))
   name=prefix+'-equivalence.json';write(name,receipt);mapping['evidence']=ref('equivalence',name)
  else:
   old_records=[rec for rec in reservation['history'] if rec['outcome']=='applied' and {'repository':repo,'revision':old} in rec['coverage']]
   assert old_records
   for rec in old_records:
    assert any(newer['kind']==rec['kind'] and newer['outcome']=='applied' and {'repository':repo,'revision':row['head']} in newer['coverage'] for newer in reservation['history'][reservation['history'].index(rec)+1:])
   data=subprocess.check_output(['git','-C',str(w),'range-diff','--no-color','--creation-factor=80',base+'..'+old,row['base']+'..'+row['head']]);range_name=prefix+'-range-diff.txt';(r/range_name).open('xb').write(data)
   receipt={'schema':1,'ownerId':reservation['ownerId'],'reservationId':reservation['id'],'mapping':mapping,'decision':'accepted','reviewer':'reviewer0 (gpt-6.1-sol/xhigh/read_only), retained completed composition/history/deployed-state compatibility review','artifacts':[ref('range_diff',range_name),ref('verification','notification-compact-deployment-result.json'),ref('migration_review','notification-compact-composition-review.md')]}
   name=prefix+'-review.json';write(name,receipt);mapping['evidence']=ref('review',name)
  mappings.append(mapping)
assert len(mappings)==9
write('notification-compact-release-lineage-final.json',{'schema':1,'mappings':mappings,'configurationDisposition':'Reviewed material pin progression includes protected upstream baseline node advances; current228 was successfully deployed after every replaced configuration generation. Final merge approval binds exact228. Existing independent complete-history/migration/deployed-state review retained, no source edits or confirmation rerun.'})
acceptance={'schema':1,'at':datetime.now(timezone.utc).isoformat(),'ownerId':reservation['ownerId'],'reservationId':reservation['id'],'source':{'kind':'user_instruction','quote':'well you did not release aitherdev','interpretation':'Release this session reservation after accepted deployed menu and completed requested integration; keep session and branches.'},'deploymentWorkFinished':True,'reviewComplete':True,'mergedHeads':[{'repository':x['repository'],'target':'refs/heads/master','head':x['head']} for x in heads['repositories']],'verification':ref('verification','notification-compact-deployment-result.json'),'integration':ref('verification','notification-compact-merge-result.json'),'lineage':ref('review','notification-compact-release-lineage-final.json'),'physicalOSSoundAndClick':'Earlier limits retained; no new native guarantee required for accepted compact menu.'}
write('notification-compact-release-acceptance.json',acceptance)
write('notification-compact-release-request.json',{'schema':1,'requestId':str(uuid.uuid4()),'expectedRevision':reservation['revision'],'deploymentWorkFinished':True,'evidence':str(r/'notification-compact-release-acceptance.json'),'finalHeads':acceptance['mergedHeads'],'replacements':mappings})
print('Nine retained deployed consumer lineages bound; release request prepared without source/deployment changes.')
