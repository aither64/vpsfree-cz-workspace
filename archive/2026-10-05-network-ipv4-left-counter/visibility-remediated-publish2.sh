#!/usr/bin/env bash
set -euo pipefail
umask 077
export PATH=/home/aither/bin:/run/wrappers/bin:/home/aither/.nix-profile/bin:/nix/profile/bin:/home/aither/.local/state/nix/profile/bin:/etc/profiles/per-user/aither/bin:/nix/var/nix/profiles/default/bin:/run/current-system/sw/bin:$PATH
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
worktrees=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter
export DEV_SESSION_SLUG=2026-10-05-network-ipv4-left-counter
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
[[ $(dev-session current) == "$DEV_SESSION_SLUG" ]]
sha256sum --check "$tracking/visibility-remediated-publish2.sha256"
run_step() {
  local mode=$1 head=$2 operation=$3 repo=$4 result=0
  [[ ! -e "$tracking/visibility-remediated-$mode-$operation.log" && ! -e "$tracking/visibility-remediated-$mode-$operation.exit" ]]
  cd "$worktrees/$repo"
  nix develop --command bash "$tracking/visibility-review-fixed-$operation-pins.sh" "$mode" "$head" >"$tracking/visibility-remediated-$mode-$operation.log" 2>&1 || result=$?
  printf '%s\n' "$result" >"$tracking/visibility-remediated-$mode-$operation.exit"
  return "$result"
}
run_step config b217e0f0a74b45fe2a95fcc79c2eb646f21248ce publish vpsfree-cz-configuration
run_step kb 609fd8a0070235339a4ddb567d905e466776d6a8 publish vpsfree-kb-contracts
for entry in config:b217e0f0a74b45fe2a95fcc79c2eb646f21248ce:vpsfree-cz-configuration kb:609fd8a0070235339a4ddb567d905e466776d6a8:vpsfree-kb-contracts; do
  mode=${entry%%:*}; rest=${entry#*:}; head=${rest%%:*}; repo=${rest#*:}
  cd "$worktrees/$repo"
  result=0
  nix develop --command bash "$tracking/visibility-review-fixed-cancel-pin-ci.sh" "$mode" "$head" >"$tracking/visibility-remediated-$mode-ci.log" 2>&1 || result=$?
  printf '%s\n' "$result" >"$tracking/visibility-remediated-$mode-ci.exit"
  (( result == 0 )) || exit "$result"
done
