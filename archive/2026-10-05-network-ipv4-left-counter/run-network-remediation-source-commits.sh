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
for step in ruby-syntax-lint legacy-browser-syntax api-chown react-units react-quick; do
  [[ $(cat "$tracking/remediation-quick2-$step.exit") == 0 ]]
done
mode=${1:?Usage: v-api | v-webui | w | consolidate-v | consolidate-w}
run_step() {
  local name="$1" directory="$2"
  shift 2
  local result=0
  (cd "$directory" && "$@") >"$tracking/remediation-operation-$name.log" 2>&1 || result=$?
  printf '%s\n' "$result" >"$tracking/remediation-operation-$name.exit"
  printf '%s: exit %s\n' "$name" "$result"
  return "$result"
}
case "$mode" in
  v-api|v-webui)
    run_step "$mode" "$worktrees/vpsadmin" env VPSADMIN_PLUGINS=all nix develop .#vpsadmin --command bash "$tracking/remediation-fixup-in-shell.sh" "$mode"
    ;;
  w)
    run_step "$mode" "$worktrees/vpsadmin-webui" nix develop --command bash "$tracking/remediation-fixup-in-shell.sh" w
    ;;
  consolidate-v)
    run_step "$mode" "$worktrees/vpsadmin" env VPSADMIN_PLUGINS=all nix develop .#vpsadmin --command bash "$tracking/remediation-consolidate-in-shell.sh" v
    ;;
  consolidate-w)
    run_step "$mode" "$worktrees/vpsadmin-webui" nix develop --command bash "$tracking/remediation-consolidate-in-shell.sh" w
    ;;
  *) exit 2 ;;
esac
