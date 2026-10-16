import subprocess,time
from pathlib import Path
r=Path(__file__).resolve().parent.parent
out=r/'effective-mounts-i1-quick'
src=r.parents[1]/'worktrees'/r.name/'vpsadminos'
start=time.monotonic()
with (out/'wrapper.log').open('w') as f:
 status=subprocess.call(['nix','develop','--profile','result/config-imports-dev-shell','--command','bash',str(r/'effective-mounts-review/i1-checks.sh')],cwd=src,stdout=f,stderr=subprocess.STDOUT)
(out/'wrapper.status').write_text(str(status)+'\n')
(out/'elapsed-seconds').write_text(str(round(time.monotonic()-start))+'\n')
print('I1 quick terminal',status)
raise SystemExit(status)
