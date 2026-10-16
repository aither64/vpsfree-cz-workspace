#!/usr/bin/env python3
"""Build exact queue requests from reviewed snapshots; no activation execution."""
import json, uuid
from pathlib import Path
root=Path(__file__).resolve().parent
slug='2026-10-14-i-d-like-the-dev-workspace'
quote='ok, proceed until it is implemented & verified. you can also deploy aitherdev using vpsfree-cz-configuration.'
def read(name):return json.loads((root/name).read_text())
def write(name,data):
 p=root/name
 if p.exists():raise SystemExit(f'Refusing overwrite: {name}')
 p.write_text(json.dumps({'schema':1,'requestId':str(uuid.uuid4()),**data},indent=2)+'\n')
profile=read('profile-prepared.json')
write('profile-approval-request.json',{'kind':'deploy','scope':[{'machine':'vpsfree:aitherdev','actions':['switch','profile_activate'],'reboot':False}], 'reviewedSnapshot':profile['id'],'source':{'kind':'user_instruction','reference':'User direction in this bound conversation before implementation','quote':quote}})
approval=read('machine-approval.json')
write('reservation-request.json',{'target':'aitherdev','mode':'deploy_first','approvalId':approval['id'],'integrationObligations':[{'repository':name,'target':'refs/heads/master'} for name in ['dev-workspace','workspace','vpsfree-cz-configuration']]})
