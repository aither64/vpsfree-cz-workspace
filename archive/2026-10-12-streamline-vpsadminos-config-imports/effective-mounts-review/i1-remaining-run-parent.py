import subprocess,time
from pathlib import Path
r=Path(__file__).resolve().parent.parent
out=r/'effective-mounts-i1-quick'
src=r.parents[1]/'worktrees'/r.name/'vpsadminos'
start=time.monotonic()
with (out/'remaining-wrapper.log').open('w') as f:
 status=subprocess.call(['nix','develop','--profile','result/config-imports-dev-shell','--command','bash',str(r/'effective-mounts-review/i1-remaining-checks.sh')],cwd=src,stdout=f,stderr=subprocess.STDOUT)
(out/'remaining-wrapper.status').write_text(str(status)+'\n')
(out/'remaining-elapsed-seconds').write_text(str(round(time.monotonic()-start))+'\n')
print('I1 quick terminal',status)
raise SystemExit(status)
