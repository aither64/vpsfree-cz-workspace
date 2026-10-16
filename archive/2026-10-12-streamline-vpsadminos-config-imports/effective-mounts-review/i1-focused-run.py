import json,subprocess,time
from pathlib import Path
r=Path(__file__).resolve().parent.parent;q=r/'effective-mounts-i1-quick';src=r.parents[1]/'worktrees'/r.name/'vpsadminos'
a=json.loads((q/'retained-30-invocations.json').read_text());assert len(a)==30
start=time.monotonic();status=0
with (q/'focused-shell.log').open('w') as f:
 for argv in a:
  argv[1]=str(src/'tests/nixos-container-persistence-shell.sh')
  argv[2:4]=[str(q/'actual-generated-shell-inputs'/Path(p).name) for p in argv[2:4]]
  status=subprocess.call(argv,cwd=src,stdout=f,stderr=subprocess.STDOUT)
  if status:break
(q/'focused-shell.status').write_text(str(status)+'\n');(q/'focused-shell.elapsed').write_text(str(round(time.monotonic()-start))+'\n')
print('Focused 30-input batch terminal',status)
raise SystemExit(status)
