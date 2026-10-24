#!/usr/bin/env bash
set -euo pipefail
umask 077
cd /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements
: "${DEV_WORKSPACE_CLAIM_ID:?held machine claim required}"
export DEV_SESSION_SLUG=2026-10-20-dev-workspace-portal-improvements
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
activation_dir="$PWD/verification/activation-530038a8"
mkdir -p "$activation_dir"
test ! -e "$activation_dir/result.json"
python3 - <<'CHECKS'
import json,os,subprocess
from pathlib import Path
assert subprocess.check_output(['dev-session','current'],text=True).strip()=='2026-10-20-dev-workspace-portal-improvements'
assert Path('/home/aither/bin/workspace-host').resolve()==Path('/nix/store/6bbjch8a42315qq855803c3y97knis2l-dev-workspace-0.2.0/bin/workspace-host')
base=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification')
assert (base/'deployment-candidate-530038a8/roots/candidate').resolve()==Path('/nix/store/hzf9qda2ckjsv72b689bclc6p3v8ap9l-dev-workspace-0.2.0')
assert (base/'deployment-candidate-530038a8/metadata-assertions.log').is_file()
assert json.loads((base/'configuration-450e1ff5/deployment/copy-status.json').read_text())['state']=='passed'
claim=json.loads(subprocess.check_output(['dev-session','coordination','claim-status','2026-10-20-dev-workspace-portal-improvements','--as-is','--id',os.environ['DEV_WORKSPACE_CLAIM_ID'],'--json'],text=True))
assert claim['state']=='held' and claim['resources']==['machine:vpsfree:aitherdev'] and claim['request']['repositories']==[]
(base/'activation-530038a8/claim.json').write_text(json.dumps(claim,indent=2)+'\n')
CHECKS
python3 - "$activation_dir" <<'RUN'
from pathlib import Path
import json,subprocess,sys,time
p=Path(sys.argv[1]);started=time.monotonic()
phases=[('system-dry',['python3','/tmp/portal-improvements-confctl.py','dry']),('system-switch',['python3','/tmp/portal-improvements-confctl.py','switch']),('profile-switch',['/home/aither/bin/workspace-host','switch','--source','/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/workspace'])]
result={'state':'running','phase':None}
status=p/'status.json'
for name,argv in phases:
 result.update(phase=name,argv=argv);status.write_text(json.dumps(result)+'\n')
 with (p/(name+'.log')).open('wb') as log:
  run=subprocess.run(argv,stdout=log,stderr=log,stdin=subprocess.DEVNULL)
 result.update(exit=run.returncode,elapsed_seconds=round(time.monotonic()-started,3))
 if run.returncode:
  result['state']='failed';break
else:
 result['state']='passed'
 result['selectedPackage']=str(Path('/home/aither/.local/state/dev-workspaces/profile').resolve())
 if result['selectedPackage']!='/nix/store/hzf9qda2ckjsv72b689bclc6p3v8ap9l-dev-workspace-0.2.0':
  result.update(state='failed',exit=1)
status.write_text(json.dumps(result,indent=2)+'\n');(p/'result.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
sys.exit(result['exit'])
RUN
