#!/usr/bin/env bash
set -euo pipefail
umask 077
export PATH=/home/aither/bin:/run/wrappers/bin:/home/aither/.nix-profile/bin:/nix/profile/bin:/home/aither/.local/state/nix/profile/bin:/etc/profiles/per-user/aither/bin:/nix/var/nix/profiles/default/bin:/run/current-system/sw/bin:$PATH
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
worktrees=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter
cd "$tracking"
export DEV_SESSION_SLUG=2026-10-05-network-ipv4-left-counter
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
[[ $(dev-session current) == "$DEV_SESSION_SLUG" ]]
[[ ! -e legacy-network-client-publish-all.log && ! -e legacy-network-client-publish-all.exit ]]
set -o noclobber
set +e
(
  set -euo pipefail
  [[ $(cat "$tracking/legacy-network-client-config-final.sha") == 072cee195d826baf78351bfc283786eb63d6dfae ]]
  [[ $(cat "$tracking/legacy-network-client-kb-final.sha") == a50f8c1a11ea642edf823f04521f9eaa97132fd2 ]]
  bash "$tracking/legacy-network-client-operation.sh" publish-pins
  for mode in config kb; do
    if [[ $mode == config ]]; then repo=vpsfree-cz-configuration; else repo=vpsfree-kb-contracts; fi
    result=0
    [[ ! -e "$tracking/legacy-network-client-$mode-cancel.log" && ! -e "$tracking/legacy-network-client-$mode-cancel.exit" ]]
    (cd "$worktrees/$repo" && nix shell --inputs-from . nixpkgs#gh --command bash "$tracking/legacy-network-client-cancel-pin-ci.sh" "$mode" "$(cat "$tracking/legacy-network-client-$mode-published.sha")") >"$tracking/legacy-network-client-$mode-cancel.log" 2>&1 || result=$?
    printf '%s\n' "$result" >"$tracking/legacy-network-client-$mode-cancel.exit"
    (( result == 0 )) || exit "$result"
  done
) >"$tracking/legacy-network-client-publish-all.log" 2>&1
result=$?
set -e
printf '%s\n' "$result" >"$tracking/legacy-network-client-publish-all.exit"
printf 'Legacy client pin publication exit %s\n' "$result"
exit "$result"
