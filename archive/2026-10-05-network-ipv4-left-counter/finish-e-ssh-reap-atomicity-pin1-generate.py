from pathlib import Path
import subprocess,json
T=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter');R=T.parent.parent/'worktrees'/T.name/'vpsfree-dev-workspace';OLD='dbb1d2ed04a08e436a458049687dcd2998db7939';G=(T/'finish-k-ssh-reap-atomicity-publish1-head').read_text().strip()
assert subprocess.check_output(['git','-C',str(R),'rev-parse','HEAD']).decode().strip()==OLD
assert subprocess.check_output(['git','-C',str(R),'status','--porcelain=v1','--untracked-files=all'])==b' M flake.nix\n'
assert (R/'flake.lock').read_bytes()==(T/'finish-e-ssh-reap-atomicity-pin1-before.flake.lock').read_bytes()
assert (R/'flake.nix').read_bytes()==(T/'finish-e-ssh-reap-atomicity-pin1-before.flake.nix').read_bytes().replace(b'd1260ed1eb3aed125f11488cf1c8ce45ed384ad4',G.encode())
with (T/'finish-e-ssh-reap-atomicity-pin1-generate.log').open('xb') as log:p=subprocess.run(['/nix/store/ima4p8pl9chccjprd6rdg9pqbr1qmfnq-nix-2.34.8/bin/nix','flake','update','kb-runtime'],cwd=R,stdout=log,stderr=subprocess.STDOUT)
with (T/'finish-e-ssh-reap-atomicity-pin1-generate.exit').open('x') as f:f.write(str(p.returncode)+'\n')
if p.returncode==0:
 with (T/'finish-e-ssh-reap-atomicity-pin1-generated.lock').open('xb') as f:f.write((R/'flake.lock').read_bytes())
print(json.dumps({'exit_code':p.returncode,'log':str(T/'finish-e-ssh-reap-atomicity-pin1-generate.log'),'selected_k':G}));raise SystemExit(p.returncode)
