#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
[[ $(pwd -P) == /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-cz-configuration ]]
[[ ${DEV_SESSION_SLUG-} == 2026-10-05-network-ipv4-left-counter && ${DEV_SESSION_WORKSPACE-} == /home/aither/workspace/ai/vpsfree.cz ]]
while IFS= read -r host; do
  result=0
  confctl build --yes "$host" >"$tracking/post-review-config-${host##*/}.log" 2>&1 || result=$?
  printf '%s\n' "$result" >"$tracking/post-review-config-${host##*/}.exit"
  printf '%s: exit %s\n' "$host" "$result"
  (( result == 0 )) || exit "$result"
done <"$tracking/network-affected-config-hosts.txt"
