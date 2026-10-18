import json,pathlib,time,subprocess,os
root=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz');out=root/'work/2026-10-16-idle-coordination-worker';run='f2ff2f60-5836-4c8b-9a1d-bc89637faa19';journal=pathlib.Path('/home/aither/.local/state/dev-workspaces/coordination/integrations')/(run+'.json');old=None
while True:
 value=json.loads(journal.read_text());projection={k:value.get(k) for k in ['phase','continuation','reason','jobs']};projection['completedSteps']=[k for k,v in value['steps'].items() if 'result' in v]
 if projection!=old:
  (out/'background-merge-observation.json').write_text(json.dumps(projection,indent=2)+'\n');print(json.dumps(projection),flush=True);old=projection
 if value.get('continuation',{}).get('state')=='needs_attention':raise SystemExit(3)
 if value['phase']=='complete':raise SystemExit(0)
 time.sleep(10)
