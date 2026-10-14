#!/usr/bin/env bash
set -euo pipefail
umask 077
export PATH=/home/aither/bin:/run/wrappers/bin:/home/aither/.nix-profile/bin:/nix/profile/bin:/home/aither/.local/state/nix/profile/bin:/etc/profiles/per-user/aither/bin:/nix/var/nix/profiles/default/bin:/run/current-system/sw/bin:$PATH
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
worktrees=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter
export DEV_SESSION_SLUG=2026-10-05-network-ipv4-left-counter
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
[[ $(dev-session current) == "$DEV_SESSION_SLUG" ]]
sha256sum --check "$tracking/visibility-final-runtime-checks.sha256"
python3 - "$tracking/visibility-post-review-gate.json" <<'PYGATE'
import json, sys
j=json.load(open(sys.argv[1]))
assert j['cleared'] is True and j['workflow_step']==9
assert j['v']=='cc3337d0a2699a8b28a0327bbee5ef62f3fbe166'
assert j['config']=='b217e0f0a74b45fe2a95fcc79c2eb646f21248ce'
assert j['w']=='e4c49bcdc91b33b7f644a2f125231cb413cf4bf4'
assert j['kb']=='609fd8a0070235339a4ddb567d905e466776d6a8'
PYGATE
for mode in migration restore legacy; do
  bash "$tracking/visibility-run-vm.sh" "$mode" cc3337d0a2699a8b28a0327bbee5ef62f3fbe166
done
cd "$worktrees/vpsfree-cz-configuration"
nix develop --command bash "$tracking/visibility-build-configs.sh" cc3337d0a2699a8b28a0327bbee5ef62f3fbe166 b217e0f0a74b45fe2a95fcc79c2eb646f21248ce
