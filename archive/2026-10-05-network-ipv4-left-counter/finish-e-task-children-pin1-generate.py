from pathlib import Path
import subprocess,json,sys
T=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter');R=Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-dev-workspace')
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=R).decode().strip()=='dfc7155bd10315733508174fa7297ce8e9250625'
assert subprocess.check_output(['git','status','--porcelain'],cwd=R)==b' M flake.nix\n'
assert (R/'flake.lock').read_bytes()==(T/'finish-e-task-children-pin1-before.flake.lock').read_bytes()
assert (R/'flake.nix').read_bytes()==(T/'finish-e-task-children-pin1-before.flake.nix').read_bytes().replace(b'3bb675f1e730ee9f18416363f6700f4000e44d0c',b'29b17bf4bb151fbbb6b693c559cb16a196fa41c5')
with(T/'finish-e-task-children-pin1-generate.log').open('xb') as log:
 p=subprocess.run(['/nix/store/ima4p8pl9chccjprd6rdg9pqbr1qmfnq-nix-2.34.8/bin/nix','flake','update','kb-runtime'],cwd=R,stdout=log,stderr=subprocess.STDOUT)
with(T/'finish-e-task-children-pin1-generate.exit').open('x')as f:f.write(str(p.returncode)+'\n')
if p.returncode==0:
 with(T/'finish-e-task-children-pin1-generated.lock').open('xb')as f:f.write((R/'flake.lock').read_bytes())
print(json.dumps({'exit_code':p.returncode,'selected_k':'29b17bf4bb151fbbb6b693c559cb16a196fa41c5','log':str(T/'finish-e-task-children-pin1-generate.log')}),flush=True)
sys.exit(p.returncode)
