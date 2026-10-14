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
  commit) exit 2 ;;
  publish) exit 2 ;;
  config)
    [[ $# == 2 && $2 =~ ^[0-9a-f]{40}$ ]]
    directory="$worktrees/vpsfree-cz-configuration"
    command=(nix develop --command bash "$tracking/visibility-pin-retained-w.sh" config "$2")
    ;;
  kb)
    [[ $# == 2 && $2 =~ ^[0-9a-f]{40}$ ]]
    directory="$worktrees/vpsfree-kb-contracts"
    command=(nix develop --command bash "$tracking/visibility-pin-retained-w.sh" kb "$2")
    ;;
  *) exit 2 ;;
esac
[[ ! -e "$tracking/visibility-pin-retained-w-$mode.log" && ! -e "$tracking/visibility-pin-retained-w-$mode.exit" ]]
set +e
(
  set -euo pipefail
  sha256sum --check "$tracking/visibility-final-operation.sha256"
  sha256sum --check "$tracking/visibility-publication-retry.sha256"
  sha256sum --check "$tracking/visibility-pin-retained-w.sha256"
  cd "$directory"
  "${command[@]}"
) >"$tracking/visibility-pin-retained-w-$mode.log" 2>&1
result=$?
set -e
printf '%s\n' "$result" >"$tracking/visibility-pin-retained-w-$mode.exit"
printf 'Visibility operation %s exit %s\n' "$mode" "$result"
exit "$result"
