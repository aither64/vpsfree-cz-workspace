#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
workspace=/home/aither/workspace/ai/vpsfree.cz
slug=2026-10-05-network-ipv4-left-counter
repo_root="$workspace/worktrees/$slug/vpsadmin-webui-proxy-addr"
stage=${1:?Usage: proxy-addr-maintenance-prep1.sh generate|quick}
[[ $# == 1 && ( $stage == generate || $stage == quick ) ]]
if [[ -n ${DEV_SESSION_SLUG+x} || -n ${DEV_SESSION_WORKSPACE+x} ]]; then
  [[ ${DEV_SESSION_SLUG-} == "$slug" && ${DEV_SESSION_WORKSPACE-} == "$workspace" ]]
fi
cd "$tracking"
[[ $(dev-session current) == "$slug" ]]
export DEV_SESSION_SLUG="$slug" DEV_SESSION_WORKSPACE="$workspace"
prefix=proxy-addr-maintenance-prep1
[[ ! -e "$tracking/$prefix-$stage-wrapper.log" && ! -e "$tracking/$prefix-$stage-wrapper.exit" ]]
set +e
(
  set -euo pipefail
  sha256sum --check "$tracking/$prefix.freeze.sha256"
  cd "$repo_root"
  nix develop --command bash "$tracking/$prefix-in-shell.sh" "$stage"
) >"$tracking/$prefix-$stage-wrapper.log" 2>&1
result=$?
set -e
printf '%s\n' "$result" >"$tracking/$prefix-$stage-wrapper.exit"
printf '%s stage exited %s; aggregate: %s\n' "$stage" "$result" "$tracking/$prefix-$stage-wrapper.log"
exit "$result"
