#!/usr/bin/env bash
set -euo pipefail
umask 077
export PATH=/home/aither/bin:/run/wrappers/bin:/home/aither/.nix-profile/bin:/nix/profile/bin:/home/aither/.local/state/nix/profile/bin:/etc/profiles/per-user/aither/bin:/nix/var/nix/profiles/default/bin:/run/current-system/sw/bin:$PATH
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
worktrees=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter
export DEV_SESSION_SLUG=2026-10-05-network-ipv4-left-counter
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
[[ $(dev-session current) == "$DEV_SESSION_SLUG" ]]
sha256sum --check "$tracking/legacy-network-client-runtime.sha256"
python3 - "$tracking/legacy-network-client-post-review-gate.json" <<'PYGATE'
import json, sys
j=json.load(open(sys.argv[1]))
assert j['cleared'] is True and j['workflow_step']==9
assert j['v']=='5d5527a67315c18b595345aa6996d7724c1ed071'
assert j['config']=='072cee195d826baf78351bfc283786eb63d6dfae'
assert j['w']=='e4c49bcdc91b33b7f644a2f125231cb413cf4bf4'
assert j['kb']=='a50f8c1a11ea642edf823f04521f9eaa97132fd2'
PYGATE
bash "$tracking/legacy-network-client-run-vm.sh" legacy 5d5527a67315c18b595345aa6996d7724c1ed071
cd "$worktrees/vpsfree-cz-configuration"
nix develop --command bash "$tracking/legacy-network-client-build-configs.sh" 5d5527a67315c18b595345aa6996d7724c1ed071 072cee195d826baf78351bfc283786eb63d6dfae
