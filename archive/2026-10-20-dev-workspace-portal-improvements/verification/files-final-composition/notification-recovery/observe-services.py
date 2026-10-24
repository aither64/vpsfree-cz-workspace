import hashlib,json,subprocess,sys
from pathlib import Path
out={}
for label,unit in [('portal','workspace-portal@vpsfree-cz.service'),('native','workspace-codex@vpsfree-cz.service'),('tmux','workspace-tmux@vpsfree-cz.service')]:
 r=subprocess.run(['systemctl','--user','show',unit,'--property=MainPID,ActiveState,SubState'],capture_output=True,text=True,check=True)
 fields=dict(line.split('=',1) for line in r.stdout.splitlines() if '=' in line);pid=int(fields['MainPID']);entry={'pid':pid,'active':fields['ActiveState'],'sub':fields['SubState']}
 if pid>0:
  stat=Path('/proc/'+str(pid)+'/stat').read_text();entry['startTicks']=stat[stat.rfind(')')+2:].split()[19];entry['executable']=str(Path('/proc/'+str(pid)+'/exe').resolve())
 out[label]=entry
out['profile']=str(Path('/home/aither/.local/state/dev-workspaces/profile').resolve())
out['system']=str(Path('/run/current-system').resolve());out['systemProfile']=str(Path('/nix/var/nix/profiles/system').resolve())
if len(sys.argv)==2:
 p=Path(sys.argv[1]);assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k in ['profile','system','systemProfile']}))
