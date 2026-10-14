#!/usr/bin/env bash
set -euo pipefail
export PATH=/home/aither/bin:/run/wrappers/bin:/home/aither/.nix-profile/bin:/nix/profile/bin:/home/aither/.local/state/nix/profile/bin:/etc/profiles/per-user/aither/bin:/nix/var/nix/profiles/default/bin:/run/current-system/sw/bin:$PATH
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
repo=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter
cd "$tracking"
test "$(/home/aither/bin/dev-session current)" = 2026-10-05-network-ipv4-left-counter
test ! -e finish-k-e-stub-correction1.log
test ! -e finish-k-e-stub-correction1.exit
set -o noclobber
exec > >(tee finish-k-e-stub-correction1.log) 2>&1
trap 'result=$?; printf "%s\n" "$result" >finish-k-e-stub-correction1.exit' EXIT
sha256sum --check finish-k-e-stub-correction1.controls.sha256
(cd "$repo/vpsfree-kb-contracts-runtime"; nix develop --command python3 "$tracking/finish-k-verifier-stub-publish1.py")
python3 - <<'PY'
from pathlib import Path
import subprocess
t=Path.cwd()
r=Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-dev-workspace')
assert subprocess.check_output(['git','-C',str(r),'rev-parse','HEAD']).decode().strip()=='94f9f8061b8ae6db3f98fbd8a2e1c73490869cd7'
assert subprocess.check_output(['git','-C',str(r),'status','--porcelain=v1','--untracked-files=all'])==b''
g=(t/'finish-k-verifier-stub-publish1-head').read_text().strip()
for name in ['flake.nix','flake.lock']:
 with (t/('finish-e-generator-pin2-before.'+name)).open('xb') as f:f.write((r/name).read_bytes())
p=r/'flake.nix';a=p.read_bytes();old=b'8ebc58c24ddbf13a9bf0d0c2c3425275c194adf9'
assert a.count(old)==1
p.write_bytes(a.replace(old,g.encode()))
PY
nix-shell "$tracking/finish-e-generator-pin2.nix" --run "python3 $tracking/finish-e-generator-pin2.py"
