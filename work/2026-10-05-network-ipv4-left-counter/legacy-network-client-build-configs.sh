#!/usr/bin/env bash
# Execute only after the final committed legacy client/pin review is cleared.
set -euo pipefail
set -o noclobber
umask 077
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
worktrees=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter
v_sha=${1:?Missing reviewed V head}
c_sha=${2:?Missing reviewed C head}
w_sha=e4c49bcdc91b33b7f644a2f125231cb413cf4bf4
[[ $v_sha =~ ^[0-9a-f]{40}$ && $c_sha =~ ^[0-9a-f]{40}$ && $# == 2 ]]
[[ ${DEV_SESSION_SLUG-} == 2026-10-05-network-ipv4-left-counter ]]
[[ ${DEV_SESSION_WORKSPACE-} == /home/aither/workspace/ai/vpsfree.cz ]]
[[ $(pwd -P) == "$worktrees/vpsfree-cz-configuration" ]]
verify_sources() {
  for entry in "vpsadmin:$v_sha" "vpsadmin-webui:$w_sha" "vpsfree-cz-configuration:$c_sha"; do
    local repo=${entry%%:*} head=${entry#*:}
    [[ $(git -C "$worktrees/$repo" rev-parse HEAD) == "$head" ]]
    [[ -z $(git -C "$worktrees/$repo" status --porcelain) ]]
  done
}
verify_sources
while IFS= read -r host; do
  name=${host##*/}
  [[ ! -e "$tracking/legacy-network-client-config-build-$name.log" && ! -e "$tracking/legacy-network-client-config-build-$name.exit" ]]
done <"$tracking/network-affected-config-hosts.txt"
while IFS= read -r host; do
  name=${host##*/}
  result=0
  confctl build --yes "$host" >"$tracking/legacy-network-client-config-build-$name.log" 2>&1 || result=$?
  printf '%s\n' "$result" >"$tracking/legacy-network-client-config-build-$name.exit"
  printf '%s: exit %s\n' "$host" "$result"
  (( result == 0 )) || exit "$result"
  verify_sources
done <"$tracking/network-affected-config-hosts.txt"
