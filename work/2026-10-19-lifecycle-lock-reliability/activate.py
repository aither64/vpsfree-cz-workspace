from pathlib import Path
import json,subprocess,os,uuid
tracking=Path(__file__).resolve().parent
workspace=tracking.parents[1]
slug=tracking.name
env=os.environ | {'DEV_SESSION_SLUG':slug,'DEV_SESSION_WORKSPACE':str(workspace),'TMPDIR':'/tmp'}
for name in ['packaged','machine-prepare','profile-prepare']:
    assert json.loads((tracking/(name+'-result.json')).read_text())['exitStatus']==0, name
inventory=json.loads((tracking/'branch-inventory.json').read_text())
for name,item in inventory.items():
    path=Path(item['worktree'])
    assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=path,text=True).strip()==item['head']
    assert not subprocess.check_output(['git','status','--porcelain'],cwd=path,text=True)

def request(name,payload):
    path=tracking/(name+'-request.json')
    if path.exists():
        saved=json.loads(path.read_text())
        assert {k:v for k,v in saved.items() if k not in ['schema','requestId']}==payload
    else:
        path.write_text(json.dumps({'schema':1,'requestId':str(uuid.uuid4())}|payload,indent=2)+'\n')
    return path

def invoke(name,action,payload):
    path=request(name,payload)
    cmd=['dev-session','coordination',action,slug,'--as-is','--request',str(path),'--json']
    with (tracking/(name+'-receipt.json')).open('w') as out,(tracking/(name+'.log')).open('w') as err:
        result=subprocess.run(cmd,cwd=workspace,env=env,stdout=out,stderr=err)
    if result.returncode:raise SystemExit(name+' failed: '+str(result.returncode))
    data=json.loads((tracking/(name+'-receipt.json')).read_text())
    print(json.dumps({'operation':name,'id':data.get('id'),'state':data.get('state')}),flush=True)
    return data

def prepared(name):
    text=(tracking/(name+'-prepare.stdout')).read_text()
    value,end=json.JSONDecoder().raw_decode(text[text.index('{'):])
    assert value.get('id','').startswith('sha256:')
    assert isinstance(value.get('operation'),dict) and value.get('evidence')
    return value
snapshots={name:prepared(name) for name in ['machine','profile']}
source={'kind':'user_instruction','reference':'2026-10-19 conversation: archive reliability repair and deployment',
        'quote':"investigate and fix it, aitherdev can be deployed using vpsfree-cz-configuration. i'd rather you made it so that we'd avoid these sorts of errors altogether.\nImplement the plan.\nnote that when a service is archived, it should also release machine reservations."}
approvals={}
for name in ['machine','profile']:
    approvals[name]=invoke(name+'-approval','approve',{'kind':'deploy','scope':[{'machine':'vpsfree:aitherdev','actions':['switch','profile_activate'],'reboot':False}],'reviewedSnapshot':snapshots[name]['id'],'source':source})['id']
reservation=invoke('reservation','reserve',{'target':'aitherdev','mode':'deploy_first','approvalId':approvals['machine'],'integrationObligations':[{'repository':name,'target':'refs/heads/master'} for name in inventory]})['id']
machine=invoke('machine-submit','submit',{'kind':'machine_activate','dependsOn':[],'approvalId':approvals['machine'],'reservationId':reservation,'snapshot':snapshots['machine']})
profile=invoke('profile-submit','submit',{'kind':'profile_activate','dependsOn':[machine['id']],'approvalId':approvals['profile'],'reservationId':reservation,'snapshot':snapshots['profile']})
(tracking/'activation-jobs.json').write_text(json.dumps({'reservation':reservation,'machine':machine['id'],'profile':profile['id']},indent=2)+'\n')
