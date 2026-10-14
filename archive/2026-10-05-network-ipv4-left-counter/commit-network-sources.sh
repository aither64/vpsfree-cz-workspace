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
mode=${1:?Usage: commit-network-sources.sh v-api | v-webui | w | all}
case "$mode" in
  v-api|v-webui|all)
    for step in quick6-ruby-syntax-lint quick6-php-locales quick8-php-format quick8-php-syntax-lint-unit quick8-nix-format quick8-api-batches-continuity; do
      [[ $(cat "$tracking/$step.exit") == 0 ]]
    done
    ;;
esac
case "$mode" in
  w|all)
    [[ $(cat "$tracking/quick8-react-inventory.exit") == 0 ]]
    [[ $(cat "$tracking/quick9-react-units.exit") == 0 ]]
    [[ $(cat "$tracking/quick9-react-quick.exit") == 0 ]]
    ;;
esac
run_step() {
  local name="$1" directory="$2"
  shift 2
  local result=0
  (cd "$directory" && "$@") >"$tracking/source-$name.log" 2>&1 || result=$?
  printf '%s\n' "$result" >"$tracking/source-$name.exit"
  printf '%s: exit %s\n' "$name" "$result"
  return "$result"
}
case "$mode" in
  v-api)
    run_step commit-v-api "$worktrees/vpsadmin" env VPSADMIN_PLUGINS=all nix develop .#vpsadmin --command bash "$tracking/commit-network-source-in-shell.sh" v-api
    ;;
  v-webui)
    run_step commit-v-webui "$worktrees/vpsadmin" env VPSADMIN_PLUGINS=all nix develop .#vpsadmin --command bash "$tracking/commit-network-source-in-shell.sh" v-webui
    ;;
  w)
    run_step commit-w "$worktrees/vpsadmin-webui" nix develop --command bash "$tracking/commit-network-source-in-shell.sh" w
    ;;
  all)
    bash "$tracking/commit-network-sources.sh" v-api
    bash "$tracking/commit-network-sources.sh" v-webui
    bash "$tracking/commit-network-sources.sh" w
    ;;
  *) exit 2 ;;
esac
