from pathlib import Path
import os,subprocess,json,uuid
out=Path(__file__).resolve().parent;root=out.parents[1];slug=out.name
assert (out/'merge-runtime-followup-review.md').exists()
snapshot=json.loads((out/'merge-runtime-prepare.stdout').read_text());assert snapshot['operation']['featureHead']=='ea3f9d36397e8c2c846bd456e51385d73a3a358a'
ledger=json.loads(Path('/home/aither/.local/state/dev-workspaces/coordination/ledger.json').read_text());job_id='392a7bd6-eb3e-427d-89f5-80fdf05f1ed4';job=ledger['jobs'][job_id];assert job['state']=='needs_refresh'
env=os.environ|{'DEV_SESSION_SLUG':slug,'DEV_SESSION_WORKSPACE':str(root)}
def invoke(name,action,payload,id=None):
    p=out/(name+'-request.json')
    if p.exists():
        saved=json.loads(p.read_text());assert {k:v for k,v in saved.items() if k not in ['schema','requestId']}==payload
    else:p.write_text(json.dumps({'schema':1,'requestId':str(uuid.uuid4())}|payload,indent=2)+'\n')
    cmd=['dev-session','coordination',action,slug]+([id] if id else [])+['--as-is','--request',str(p),'--json']
    with (out/(name+'-receipt.json')).open('w') as stdout,(out/(name+'.log')).open('w') as stderr:
        result=subprocess.run(cmd,cwd=root,env=env,stdout=stdout,stderr=stderr)
    if result.returncode:raise SystemExit(name+' failed '+str(result.returncode))
    d=json.loads((out/(name+'-receipt.json')).read_text());print(name,d.get('id'),d.get('state'),flush=True);return d
source=json.loads((out/'merge-integration-request.json').read_text())['approval']
a=invoke('merge-runtime-refresh-approval','approve',{'kind':'merge','scope':[{'repository':'dev-workspace','target':'refs/heads/master'}],'reviewedSnapshot':snapshot['id'],'source':source})
invoke('merge-runtime-refresh','refresh',{'expectedRevision':job['revision'],'snapshot':snapshot,'approvalId':a['id']},job_id)
