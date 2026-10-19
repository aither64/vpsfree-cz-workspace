from pathlib import Path
import os,subprocess,json,uuid
out=Path(__file__).resolve().parent;workspace=out.parents[1];slug=out.name
env=os.environ|{'DEV_SESSION_SLUG':slug,'DEV_SESSION_WORKSPACE':str(workspace),'TMPDIR':'/tmp'}
assert json.loads((out/'machine-refresh-prepare-result.json').read_text())['exitStatus']==0
assert (out/'config-refresh-review.md').exists()
text=(out/'machine-refresh-prepare.stdout').read_text();snapshot=json.JSONDecoder().raw_decode(text[text.index('{'):])[0]
assert snapshot['operation']['configurationHead']=='0067299ab9739f522fec0780cda98649ae630406'
(out/'machine-refresh-snapshot.json').write_text(json.dumps(snapshot,indent=2)+'\n')
jobs=json.loads((out/'activation-jobs.json').read_text());ledger=json.loads(Path('/home/aither/.local/state/dev-workspaces/coordination/ledger.json').read_text());job=ledger['jobs'][jobs['machine']]
assert job['state']=='needs_refresh' and job['attempt']=='7baddda9-6872-46c7-81c6-d792eea6e574'
def invoke(name,action,payload,job_id=None):
    path=out/(name+'-request.json')
    if path.exists():
        request=json.loads(path.read_text());assert {k:v for k,v in request.items() if k not in ['schema','requestId']}==payload
    else:
        request={'schema':1,'requestId':str(uuid.uuid4())}|payload;path.write_text(json.dumps(request,indent=2)+'\n')
    cmd=['dev-session','coordination',action,slug]+([job_id] if job_id else [])+['--as-is','--request',str(path),'--json']
    with (out/(name+'-receipt.json')).open('w') as stdout,(out/(name+'.log')).open('w') as stderr:
        process=subprocess.run(cmd,cwd=workspace,env=env,stdout=stdout,stderr=stderr)
    if process.returncode:raise SystemExit(str(cmd)+' failed '+str(process.returncode))
    result=json.loads((out/(name+'-receipt.json')).read_text());print(json.dumps({'name':name,'id':result.get('id'),'state':result.get('state')}),flush=True);return result
source=json.loads((out/'machine-approval-request.json').read_text())['source']
approval=invoke('machine-refresh-approval','approve',{'kind':'deploy','scope':[{'machine':'vpsfree:aitherdev','actions':['switch','profile_activate'],'reboot':False}],'reviewedSnapshot':snapshot['id'],'source':source})['id']
invoke('machine-refresh','refresh',{'expectedRevision':job['revision'],'snapshot':snapshot,'approvalId':approval},jobs['machine'])
