from pathlib import Path
import subprocess,json,hashlib
T=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter');R=T.parent.parent/'worktrees'/T.name/'vpsfree-dev-workspace';OLD='fe2b6a08beeac48dffd932756ad81ff2749fe8fd';G=(T/'finish-k-atomic-reader-publish1-head').read_text().strip()
assert subprocess.check_output(['git','-C',str(R),'rev-parse','HEAD']).decode().strip()==OLD
assert subprocess.check_output(['git','-C',str(R),'status','--porcelain'])==b' M flake.nix\n'
assert (R/'flake.lock').read_bytes()==(T/'finish-e-generator-pin5-before.flake.lock').read_bytes()
assert (R/'flake.nix').read_bytes()==(T/'finish-e-generator-pin5-before.flake.nix').read_bytes().replace(b'ab09bd437b310f57e4ff2453ec0432555d85eaca',G.encode())
with (T/'finish-e-generator-pin5-generate.log').open('xb') as f:p=subprocess.run(['/nix/store/ima4p8pl9chccjprd6rdg9pqbr1qmfnq-nix-2.34.8/bin/nix','flake','update','kb-runtime'],cwd=R,stdout=f,stderr=subprocess.STDOUT)
with (T/'finish-e-generator-pin5-generate.exit').open('x') as f:f.write(str(p.returncode)+'\n')
if p.returncode==0:
 with (T/'finish-e-generator-pin5-generated.lock').open('xb') as f:f.write((R/'flake.lock').read_bytes())
print(json.dumps({'exit_code':p.returncode,'log':str(T/'finish-e-generator-pin5-generate.log'),'selected_k':G}));raise SystemExit(p.returncode)
