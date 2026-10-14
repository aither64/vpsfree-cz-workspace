from pathlib import Path
import subprocess, os, json, datetime
T=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter');E=T.parent.parent/'worktrees'/T.name/'vpsfree-dev-workspace'
NIX='/nix/store/ima4p8pl9chccjprd6rdg9pqbr1qmfnq-nix-2.34.8/bin/nix'
env={k:os.environ[k] for k in ['HOME','USER','LOGNAME','XDG_RUNTIME_DIR'] if k in os.environ}
env['PATH']=str(Path(NIX).parent)+':'+str(Path('/nix/store/5vpcfsdx1lcnlb2y4k7xyc74shp5qwbh-git-2.54.0/bin/git').parent)+':/run/current-system/sw/bin'
env['NIX_CONFIG']='experimental-features = nix-command flakes\nmax-jobs = 1\ncores = 1\n'
with(T/'finish-e-runtime-reduction-pin2-generate2.log').open('xb') as o:
 p=subprocess.run([NIX,'flake','update','kb-runtime'],cwd=E,env=env,stdout=o,stderr=subprocess.STDOUT)
with(T/'finish-e-runtime-reduction-pin2-generate2.exit').open('x') as o:o.write(str(p.returncode)+'\n')
if p.returncode==0:
 with(T/'finish-e-runtime-reduction-pin2-generated2.lock').open('xb') as o:o.write((E/'flake.lock').read_bytes())
print(json.dumps({'exit':p.returncode,'operation':'mechanical exact kb-runtime lock selection; no eval/build/test','log':str(T/'finish-e-runtime-reduction-pin2-generate2.log')}),flush=True)
raise SystemExit(p.returncode)
