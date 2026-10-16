"""Lead-owned exact deploy approvals/submission. No merge or lifecycle operation."""
from pathlib import Path
import json, subprocess, uuid
root=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace')
slug=root.name
reservation='1956d2a0-992b-4b4f-9b0f-9db804769d82'
revision='8cb1c0e545e1343d311f7cb9405eee83c468b4a6'
def write(name,value):
 with (root/name).open('x') as f:json.dump(value,f,indent=2);f.write('\n')
def call(command,request,output):
 p=root/request
 with (root/output).open('x') as f:
  subprocess.run(['dev-session','coordination',command,slug,'--as-is','--request',str(p),'--json'],stdout=f,check=True)
 return json.loads((root/output).read_text())
import hashlib
assert subprocess.check_output(['dev-session','current'],text=True).strip()==slug
heads=json.loads((root/'notification-compact-final-heads.json').read_text())
for item in heads['repositories']:
 checkout=root.parents[1]/'worktrees'/slug/item['repository']
 assert subprocess.check_output(['git','-C',str(checkout),'rev-parse','HEAD'],text=True).strip()==item['head']
 assert not subprocess.check_output(['git','-C',str(checkout),'status','--porcelain'],text=True).strip()
checks=json.loads((root/'verification-notification-compact.json').read_text())
assert checks['runtimeRevision']==revision and checks['applicableAutomatedChecks']=='PASS'
for name,digest in checks['artifacts'].items():
 assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,name
assert (root/'notification-compact-preparation-inspection.json').is_file()
inspection=json.loads((root/'notification-compact-preparation-inspection.json').read_text())
assert inspection['decision']=='accepted' and inspection['runtimeRevision']==revision

assert (root/'notification-compact-composition-review.md').is_file()
deps=[]
for mode,proof in [('machine','machine-prepared-notification-compact-8cb1c0e5.json'),('profile','profile-prepared-notification-compact-8cb1c0e5.json')]:
 snap=json.loads((root/proof).read_text());assert next(x['revision'] for x in snap['operation']['coverage'] if x['repository']=='dev-workspace')==revision
 approval={'schema':1,'requestId':str(uuid.uuid4()),'kind':'deploy','scope':[{'machine':'vpsfree:aitherdev','actions':['switch','profile_activate'],'reboot':False}],'reviewedSnapshot':snap['id'],'source':{'kind':'user_instruction','reference':'Retained exact user implementation/verification/aitherdev deployment direction in bound session','quote':'ok, proceed until it is implemented & verified. you can also deploy aitherdev using vpsfree-cz-configuration.'}}
 ar=mode+'-approval-notification-compact-request.json';ao=mode+'-approved-notification-compact.json';write(ar,approval);approved=call('approve',ar,ao)
 print(json.dumps({'mode':mode,'approvalReceipt':approved}),flush=True)
 # Selected receipt field shape is checked by lead before running this helper.
 approval_id=approved['id']
 request={'schema':1,'requestId':str(uuid.uuid4()),'kind':mode+'_activate','dependsOn':deps,'approvalId':approval_id,'reservationId':reservation,'snapshot':snap}
 sr=mode+'-submit-notification-compact-request.json';so=mode+'-submitted-notification-compact.json';write(sr,request);submitted=call('submit',sr,so)
 print(json.dumps({'mode':mode,'submission':submitted}),flush=True)
 deps=[submitted['id']]
