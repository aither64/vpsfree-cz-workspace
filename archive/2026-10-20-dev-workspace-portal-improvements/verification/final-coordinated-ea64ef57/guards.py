import json,os,subprocess
from pathlib import Path
p=Path(__file__).resolve().parent
root=Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements')
assert subprocess.check_output(['dev-session','current'],text=True).strip()=='2026-10-20-dev-workspace-portal-improvements'
a,b=os.getenv('DEV_SESSION_SLUG'),os.getenv('DEV_SESSION_WORKSPACE')
assert (a is None and b is None) or (a=='2026-10-20-dev-workspace-portal-improvements' and b=='/home/aither/workspace/ai/vpsfree.cz')
for name,head in json.loads((p/'final-heads.json').read_text()).items():
 assert subprocess.check_output(['git','-C',str(root/name),'rev-parse','HEAD'],text=True).strip()==head,name
 assert not subprocess.check_output(['git','-C',str(root/name),'status','--porcelain']),name
assert Path('/home/aither/bin/workspace-host').resolve()==Path('/nix/store/hzf9qda2ckjsv72b689bclc6p3v8ap9l-dev-workspace-0.2.0/bin/workspace-host')
