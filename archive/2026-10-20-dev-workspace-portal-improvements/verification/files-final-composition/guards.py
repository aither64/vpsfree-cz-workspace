import json,os,subprocess
from pathlib import Path
p=Path(__file__).resolve().parent
root=Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements')
assert subprocess.check_output(['dev-session','current'],text=True).strip()=='2026-10-20-dev-workspace-portal-improvements'
a,b=os.getenv('DEV_SESSION_SLUG'),os.getenv('DEV_SESSION_WORKSPACE')
assert (a is None and b is None) or (a=='2026-10-20-dev-workspace-portal-improvements' and b=='/home/aither/workspace/ai/vpsfree.cz')
for name,head in json.loads((p/'final-heads.json').read_text()).items():
 assert isinstance(head,str) and len(head)==40 and all(c in '0123456789abcdef' for c in head), 'final handoff identities pending'
 assert subprocess.check_output(['git','-C',str(root/name),'rev-parse','HEAD'],text=True).strip()==head,name
 assert not subprocess.check_output(['git','-C',str(root/name),'status','--porcelain']),name
assert Path('/home/aither/bin/workspace-host').resolve()==Path('/nix/store/f5h1qmr03qva6khyijgc2wxd1ff4k4cw-dev-workspace-0.2.0/bin/workspace-host')
