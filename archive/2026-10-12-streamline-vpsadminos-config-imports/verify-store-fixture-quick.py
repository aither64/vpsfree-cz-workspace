import json, subprocess
from pathlib import Path
r=Path(__file__).resolve().parent
p=r.parents[1]/'worktrees'/r.name/'vpsadminos'
status=1
try:
 with (r/'store-fixture-generated-eval.log').open('w') as err, (r/'store-fixture-generated-scripts.json').open('w') as out:
  s=subprocess.run(['nix','develop','--profile','result/config-imports-dev-shell','--command','nix','eval','--impure','--json','--file',str(r/'persistence-store-fixture-diagnosis/generated-scripts.nix')],cwd=p,stdout=out,stderr=err).returncode
 (r/'store-fixture-generated-eval.status').write_text(str(s)+'\n')
 assert s==0
 scripts=json.loads((r/'store-fixture-generated-scripts.json').read_text());assert len(scripts)==8
 outdir=r/'store-fixture-generated-scripts';outdir.mkdir(exist_ok=True)
 for name,body in scripts.items():
  dest=outdir/(name+'.rb');dest.write_text(body)
  with (outdir/(name+'.syntax.log')).open('w') as log:
   s=subprocess.run(['nix','develop','--profile','result/config-imports-dev-shell','--command','ruby','-c',str(dest)],cwd=p,stdout=log,stderr=subprocess.STDOUT).returncode
  assert s==0,name
 with (r/'store-fixture-final-wrapper.log').open('w') as log:
  status=subprocess.run(['bash',str(r/'verify-store-fixture-final.sh')],cwd=r,stdout=log,stderr=subprocess.STDOUT).returncode
finally:
 (r/'store-fixture-quick.status').write_text(str(status)+'\n')
raise SystemExit(status)
