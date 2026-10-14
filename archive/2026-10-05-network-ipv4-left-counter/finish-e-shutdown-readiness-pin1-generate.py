from pathlib import Path
import subprocess,json,sys,hashlib
T=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
R=T.parents[1]/'worktrees'/T.name/'vpsfree-dev-workspace'
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=R).decode().strip()==(T/'finish-e-shutdown-readiness-pin1-before.head').read_text().strip()
assert subprocess.check_output(['git','status','--porcelain'],cwd=R)==b' M flake.nix\n'
assert (R/'flake.lock').read_bytes()==(T/'finish-e-shutdown-readiness-pin1-before.flake.lock').read_bytes()
assert (R/'flake.nix').read_bytes()==(T/'finish-e-shutdown-readiness-pin1-before.flake.nix').read_bytes().replace(b'0271532264adf5eeb33123d136d9a0663faf21b0',b'3bb675f1e730ee9f18416363f6700f4000e44d0c')
with (T/'finish-e-shutdown-readiness-pin1-generate.log').open('xb') as log:
 p=subprocess.run(['/nix/store/ima4p8pl9chccjprd6rdg9pqbr1qmfnq-nix-2.34.8/bin/nix','flake','update','kb-runtime'],cwd=R,stdout=log,stderr=subprocess.STDOUT)
with (T/'finish-e-shutdown-readiness-pin1-generate.exit').open('x') as f:f.write(str(p.returncode)+'\n')
if p.returncode==0:
 with (T/'finish-e-shutdown-readiness-pin1-generated.lock').open('xb') as f:f.write((R/'flake.lock').read_bytes())
print(json.dumps({'exit_code':p.returncode,'log':str(T/'finish-e-shutdown-readiness-pin1-generate.log'),'selected_k':'3bb675f1e730ee9f18416363f6700f4000e44d0c'}),flush=True)
sys.exit(p.returncode)
