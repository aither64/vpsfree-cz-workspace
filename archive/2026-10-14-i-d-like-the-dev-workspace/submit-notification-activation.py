"""Lead-owned exact deploy approvals/submission. No merge or lifecycle operation."""
from pathlib import Path
import json, subprocess, uuid
root=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace')
slug=root.name
reservation='1956d2a0-992b-4b4f-9b0f-9db804769d82'
revision='469757183ba9491d642b56e91658dc64e390647b'
def write(name,value):
 with (root/name).open('x') as f:json.dump(value,f,indent=2);f.write('\n')
def call(command,request,output):
 p=root/request
 with (root/output).open('x') as f:
  subprocess.run(['dev-session','coordination',command,slug,'--as-is','--request',str(p),'--json'],stdout=f,check=True)
 return json.loads((root/output).read_text())
checks=json.loads((root/'verification-notification-activation.json').read_text())
assert checks['runtimeRevision']==revision and checks['applicableAutomatedChecks']=='PASS'
assert (root/'notification-activation-composition-review.md').is_file()
deps=[]
for mode,proof in [('machine','machine-prepared-notification-activation-v2.json'),('profile','profile-prepared-46975718.json')]:
 snap=json.loads((root/proof).read_text());assert next(x['revision'] for x in snap['operation']['coverage'] if x['repository']=='dev-workspace')==revision
 approval={'schema':1,'requestId':str(uuid.uuid4()),'kind':'deploy','scope':[{'machine':'vpsfree:aitherdev','actions':['switch','profile_activate'],'reboot':False}],'reviewedSnapshot':snap['id'],'source':{'kind':'user_instruction','reference':'Retained exact user implementation/verification/aitherdev deployment direction in bound session','quote':'ok, proceed until it is implemented & verified. you can also deploy aitherdev using vpsfree-cz-configuration.'}}
 ar=mode+'-approval-notification-activation-request.json';ao=mode+'-approved-notification-activation.json';write(ar,approval);approved=call('approve',ar,ao)
 print(json.dumps({'mode':mode,'approvalReceipt':approved}),flush=True)
 # Selected receipt field shape is checked by lead before running this helper.
 approval_id=approved['id']
 request={'schema':1,'requestId':str(uuid.uuid4()),'kind':mode+'_activate','dependsOn':deps,'approvalId':approval_id,'reservationId':reservation,'snapshot':snap}
 sr=mode+'-submit-notification-activation-request.json';so=mode+'-submitted-notification-activation.json';write(sr,request);submitted=call('submit',sr,so)
 print(json.dumps({'mode':mode,'submission':submitted}),flush=True)
 deps=[submitted['id']]
