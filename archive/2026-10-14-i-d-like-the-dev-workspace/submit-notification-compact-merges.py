"""Lead-owned approved fast-forward integrations; no deployment or lifecycle work."""
from pathlib import Path
import json,subprocess,uuid,hashlib
r=Path(__file__).resolve().parent;slug=r.name
assert subprocess.check_output(['dev-session','current'],text=True).strip()==slug
assert json.loads((r/'notification-compact-merge-snapshot-inspection.json').read_text())['decision']=='accepted'
heads={x['repository']:x for x in json.loads((r/'notification-compact-merge-final-heads.json').read_text())['repositories']}
def write(n,v):
 with (r/n).open('x') as f:json.dump(v,f,indent=2);f.write('\n')
def call(command,request,output):
 with (r/output).open('x') as f:subprocess.run(['dev-session','coordination',command,slug,'--as-is','--request',str(r/request),'--json'],stdout=f,check=True)
 return json.loads((r/output).read_text())
deps=[]
for repo in ['dev-workspace','vpsfree-cz-configuration','workspace']:
 suffix='-v2' if repo!='dev-workspace' else '';snap=json.loads((r/f'notification-compact-merge-{repo}-prepared{suffix}.json').read_text());row=heads[repo]
 checkout=r.parents[1]/'worktrees'/slug/repo
 assert subprocess.check_output(['git','-C',str(checkout),'rev-parse','HEAD'],text=True).strip()==row['head']
 assert not subprocess.check_output(['git','-C',str(checkout),'status','--porcelain'])
 for ev in snap['evidence']:assert hashlib.sha256(Path(ev['path']).read_bytes()).hexdigest()==ev['sha256']
 approval={'schema':1,'requestId':str(uuid.uuid4()),'kind':'merge','scope':[{'repository':repo,'target':'refs/heads/master'}],'reviewedSnapshot':snap['id'],'source':{'kind':'user_instruction','reference':'Current bound conversation: user acceptance and explicit merge direction after deployed compact menu; scope recorded in notification-compact-merge-authorization.json','quote':'i like it, merge it'}}
 req=f'notification-compact-merge-{repo}-approval-request.json';out=f'notification-compact-merge-{repo}-approved.json';write(req,approval);approved=call('approve',req,out)
 submit={'schema':1,'requestId':str(uuid.uuid4()),'kind':'merge','dependsOn':deps,'approvalId':approved['id'],'reservationId':None,'snapshot':snap}
 req=f'notification-compact-merge-{repo}-submit-request.json';out=f'notification-compact-merge-{repo}-submitted.json';write(req,submit);submitted=call('submit',req,out);deps=[submitted['id']]
 print(json.dumps({'repository':repo,'head':row['head'],'job':submitted['id'],'state':submitted.get('state')}),flush=True)
