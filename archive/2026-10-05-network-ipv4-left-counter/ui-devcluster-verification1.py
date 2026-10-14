import json,os,pathlib,subprocess
workspace='/home/aither/workspace/ai/vpsfree.cz';slug='2026-10-05-network-ipv4-left-counter'; tracking=pathlib.Path(workspace)/'work'/slug
env=dict(os.environ,DEV_SESSION_SLUG=slug,DEV_SESSION_WORKSPACE=workspace,PATH='/home/aither/bin:'+os.environ['PATH'])
raw=subprocess.check_output(['vpsadmin-devcluster','status',slug,'--json'],env=env,cwd=workspace)
d=json.loads(raw)
result={k:d[k] for k in ('schema','found','kind','state','ready','webuiSource') if k in d}
result['services']=[{k:s[k] for k in ('label','url') if k in s} for s in d.get('services',[])]
result['login_details_in_portal']=any(s.get('accounts') for s in d.get('services',[]))
print(json.dumps(result,indent=2))
with (tracking/'ui-devcluster-verification1-status.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
assert d.get('found') and d.get('ready'),'cluster is not ready'
