#!/usr/bin/env bash
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
mode=${1:?Missing commit/publish/cancel/config/kb operation}
case "$mode" in
  commit)
    [[ $# == 1 ]]
    directory="$worktrees/vpsadmin"
    command=(env VPSADMIN_PLUGINS=all nix develop .#vpsadmin --command bash "$tracking/visibility-v-operation.sh" commit)
    ;;
  publish)
    [[ $# == 2 && $2 =~ ^[0-9a-f]{40}$ ]]
    directory="$worktrees/vpsadmin"
    command=(bash "$tracking/visibility-v-operation.sh" publish "$2")
    ;;
  cancel)
    [[ $# == 2 && $2 =~ ^[0-9a-f]{40}$ ]]
    directory="$worktrees/vpsadmin"
    command=(nix shell --inputs-from . nixpkgs#gh --command bash "$tracking/visibility-cancel-ci.sh" "$2")
    ;;
  config)
    [[ $# == 2 && $2 =~ ^[0-9a-f]{40}$ ]]
    directory="$worktrees/vpsfree-cz-configuration"
    command=(nix develop --command bash "$tracking/visibility-pin-operation.sh" config "$2")
    ;;
  kb)
    [[ $# == 2 && $2 =~ ^[0-9a-f]{40}$ ]]
    directory="$worktrees/vpsfree-kb-contracts"
    command=(nix develop --command bash "$tracking/visibility-pin-operation.sh" kb "$2")
    ;;
  *) exit 2 ;;
esac
[[ ! -e "$tracking/visibility-operation-$mode.log" && ! -e "$tracking/visibility-operation-$mode.exit" ]]
set +e
(
  set -euo pipefail
  sha256sum --check "$tracking/visibility-operation.sha256"
  cd "$directory"
  "${command[@]}"
) >"$tracking/visibility-operation-$mode.log" 2>&1
result=$?
set -e
printf '%s\n' "$result" >"$tracking/visibility-operation-$mode.exit"
printf 'Visibility operation %s exit %s\n' "$mode" "$result"
exit "$result"
