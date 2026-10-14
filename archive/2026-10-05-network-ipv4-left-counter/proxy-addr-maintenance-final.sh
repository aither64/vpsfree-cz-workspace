#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
workspace=/home/aither/workspace/ai/vpsfree.cz
slug=2026-10-05-network-ipv4-left-counter
repo_root="$workspace/worktrees/$slug/vpsadmin-webui-proxy-addr"
prefix=proxy-addr-maintenance-final
operation=${1:?Usage: proxy-addr-maintenance-final.sh commit|packages|publish [EXACT_SHA]}
case "$operation" in
  commit) [[ $# == 1 ]] ;;
  packages|publish) [[ $# == 2 && $2 =~ ^[0-9a-f]{40}$ ]] ;;
  *) exit 2 ;;
esac
if [[ -n ${DEV_SESSION_SLUG+x} || -n ${DEV_SESSION_WORKSPACE+x} ]]; then
  [[ ${DEV_SESSION_SLUG-} == "$slug" && ${DEV_SESSION_WORKSPACE-} == "$workspace" ]]
fi
cd "$tracking"
[[ $(dev-session current) == "$slug" ]]
export DEV_SESSION_SLUG="$slug" DEV_SESSION_WORKSPACE="$workspace"
[[ ! -e "$tracking/$prefix-$operation-wrapper.log" && ! -e "$tracking/$prefix-$operation-wrapper.exit" ]]
set +e
(
  set -euo pipefail
  sha256sum --check "$tracking/$prefix.freeze.sha256"
  cd "$repo_root"
  nix develop --command bash "$tracking/$prefix-in-shell.sh" "$@"
) >"$tracking/$prefix-$operation-wrapper.log" 2>&1
result=$?
set -e
printf '%s\n' "$result" >"$tracking/$prefix-$operation-wrapper.exit"
printf '%s exited %s; aggregate: %s\n' "$operation" "$result" "$tracking/$prefix-$operation-wrapper.log"
exit "$result"
