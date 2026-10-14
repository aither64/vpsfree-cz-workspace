#!/usr/bin/env bash
# Execute only after the lead accepts the final source commits and evidence.
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
worktrees=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter
if [[ ${DEV_SESSION_SLUG+x} || ${DEV_SESSION_WORKSPACE+x} ]]; then
  [[ ${DEV_SESSION_SLUG-} == 2026-10-05-network-ipv4-left-counter && ${DEV_SESSION_WORKSPACE-} == /home/aither/workspace/ai/vpsfree.cz ]]
fi
cd "$tracking"
[[ $(dev-session current) == 2026-10-05-network-ipv4-left-counter ]]
export DEV_SESSION_SLUG=2026-10-05-network-ipv4-left-counter
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
v_sha=${1:?Usage: publish-network-sources.sh V_SHA W_SHA}
w_sha=${2:?Missing W feature head}
[[ $v_sha =~ ^[0-9a-f]{40}$ && $w_sha =~ ^[0-9a-f]{40}$ ]]
run_step() {
  local name="$1" directory="$2"
  shift 2
  local result=0
  (cd "$directory" && "$@") >"$tracking/source-$name.log" 2>&1 || result=$?
  printf '%s\n' "$result" >"$tracking/source-$name.exit"
  printf '%s: exit %s\n' "$name" "$result"
  return "$result"
}
run_step publish-v "$worktrees/vpsadmin" nix develop .#vpsadmin --command bash "$tracking/publish-network-source-in-shell.sh" vpsadmin 2026-10-05-network-ipv4-left-counter master "$v_sha"
run_step publish-w "$worktrees/vpsadmin-webui" nix develop --command bash "$tracking/publish-network-source-in-shell.sh" vpsadmin-webui dev/network-enabled main "$w_sha"
