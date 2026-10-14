#!/usr/bin/env bash
set -euo pipefail
[[ ${DEV_SESSION_SLUG-} == 2026-10-05-network-ipv4-left-counter && ${DEV_SESSION_WORKSPACE-} == /home/aither/workspace/ai/vpsfree.cz ]]
[[ $(pwd -P) == /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-cz-configuration ]]
[[ $1 =~ ^[0-9a-f]{40}$ && $2 =~ ^[0-9a-f]{40}$ ]]
test -x "$(git rev-parse --git-path hooks/pre-commit)"
confctl inputs channel set --commit --no-editor vpsadmin vpsadmin "$1"
confctl inputs channel set --commit --no-editor vpsadmin-webui vpsadmin-webui "$2"
git log -2 --format=fuller
git diff HEAD~2 HEAD -- flake.nix flake.lock
python3 - "$1" "$2" <<'PY'
import json, sys
from pathlib import Path
lock = json.loads(Path('flake.lock').read_text())
root = lock['nodes'][lock['root']]['inputs']
assert lock['nodes'][root['vpsadminServices']]['locked']['rev'] == sys.argv[1]
webui = lock['nodes'][root['vpsadminWebui']]
assert webui['locked']['rev'] == sys.argv[2]
assert webui['inputs']['vpsadmin'] == ['vpsadminServices']
PY
