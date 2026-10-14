from pathlib import Path
import subprocess,json,hashlib
T=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter');R=T.parent.parent/'worktrees'/T.name/'vpsfree-dev-workspace';OLD='02c77f1a46f5878054ada009e3e893a58e207568';G=(T/'finish-k-g4-stop-path-publish1-head').read_text().strip()
assert subprocess.check_output(['git','-C',str(R),'rev-parse','HEAD']).decode().strip()==OLD
assert subprocess.check_output(['git','-C',str(R),'status','--porcelain'])==b' M flake.nix\n'
assert (R/'flake.lock').read_bytes()==(T/'finish-e-generator-pin6-before.flake.lock').read_bytes()
assert (R/'flake.nix').read_bytes()==(T/'finish-e-generator-pin6-before.flake.nix').read_bytes().replace(b'25539d837dea07f868b807db79dca436ab5075f7',G.encode())
with (T/'finish-e-generator-pin6-generate.log').open('xb') as f:p=subprocess.run(['/nix/store/ima4p8pl9chccjprd6rdg9pqbr1qmfnq-nix-2.34.8/bin/nix','flake','update','kb-runtime'],cwd=R,stdout=f,stderr=subprocess.STDOUT)
with (T/'finish-e-generator-pin6-generate.exit').open('x') as f:f.write(str(p.returncode)+'\n')
if p.returncode==0:
 with (T/'finish-e-generator-pin6-generated.lock').open('xb') as f:f.write((R/'flake.lock').read_bytes())
print(json.dumps({'exit_code':p.returncode,'log':str(T/'finish-e-generator-pin6-generate.log'),'selected_k':G}));raise SystemExit(p.returncode)
