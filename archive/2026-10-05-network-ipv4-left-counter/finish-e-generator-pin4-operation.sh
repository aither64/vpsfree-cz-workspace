#!/usr/bin/env bash
set -euo pipefail
export PATH=/home/aither/bin:/run/wrappers/bin:/home/aither/.nix-profile/bin:/nix/profile/bin:/home/aither/.local/state/nix/profile/bin:/etc/profiles/per-user/aither/bin:/nix/var/nix/profiles/default/bin:/run/current-system/sw/bin:$PATH
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
cd "$tracking"
test "$(/home/aither/bin/dev-session current)" = 2026-10-05-network-ipv4-left-counter
test ! -e "$tracking/finish-e-generator-pin4-operation.log"
test ! -e "$tracking/finish-e-generator-pin4-operation.exit"
set -o noclobber
exec > >(tee "$tracking/finish-e-generator-pin4-operation.log") 2>&1
trap 'result=$?; printf "%s\n" "$result" >"$tracking/finish-e-generator-pin4-operation.exit"' EXIT
sha256sum --check finish-e-generator-pin4-controls.sha256
python3 - <<'INNER'
from pathlib import Path
import subprocess
p=Path.cwd();r=Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-dev-workspace')
assert subprocess.check_output(['git','-C',str(r),'rev-parse','HEAD']).decode().strip()=='7b5acc05d3b005ebfb4f05c2cc58d636faaabd1e'
assert subprocess.check_output(['git','-C',str(r),'status','--porcelain=v1','--untracked-files=all'])==b''
g=(p/'finish-k-inventory-select-publish1-head').read_text().strip();d=(p/'finish-d-force-fixture-publish1-head').read_text().strip()
assert g=='ab09bd437b310f57e4ff2453ec0432555d85eaca' and d=='b1ec1bf1c3bc6413b066816ca58468b67ad5e5a6'
for name in ['flake.nix','flake.lock']:
 with (p/('finish-e-generator-pin4-before.'+name)).open('xb') as f:f.write((r/name).read_bytes())
file=r/'flake.nix';s=file.read_bytes();oldg=b'a93fc97ed421d56dfe6753efb223af14948e5e6d';oldd=b'51aba080b264c28f5584867b6cf006bf423ae2f3'
assert s.count(oldg)==1 and s.count(oldd)==1
file.write_bytes(s.replace(oldg,g.encode()).replace(oldd,d.encode()))
INNER
nix-shell "$tracking/finish-e-generator-pin4.nix" --run "python3 $tracking/finish-e-generator-pin4.py"
