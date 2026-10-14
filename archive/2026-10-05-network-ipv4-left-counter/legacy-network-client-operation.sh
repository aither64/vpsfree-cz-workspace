#!/usr/bin/env bash
# Prepared modes only; the lead selects and launches each reviewed operation.
set -euo pipefail
export PATH="/home/aither/bin:/run/wrappers/bin:/home/aither/.nix-profile/bin:/nix/profile/bin:/home/aither/.local/state/nix/profile/bin:/etc/profiles/per-user/aither/bin:/nix/var/nix/profiles/default/bin:/run/current-system/sw/bin:$PATH"
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
worktrees=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter
prefix=legacy-network-client
if [[ ${DEV_SESSION_SLUG+x} || ${DEV_SESSION_WORKSPACE+x} ]]; then
  [[ ${DEV_SESSION_SLUG-} == 2026-10-05-network-ipv4-left-counter && ${DEV_SESSION_WORKSPACE-} == /home/aither/workspace/ai/vpsfree.cz ]]
fi
cd "$tracking"
[[ $(dev-session current) == 2026-10-05-network-ipv4-left-counter ]]
export DEV_SESSION_SLUG=2026-10-05-network-ipv4-left-counter
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
operation=${1:?Usage: consolidate|publish-v|cancel-v|config|kb-candidate|publish-pins}
[[ $# == 1 ]]
case "$operation" in consolidate|publish-v|cancel-v|config|kb-candidate|publish-pins) ;; *) exit 2 ;; esac
[[ ! -e "$tracking/$prefix-$operation-wrapper.log" && ! -e "$tracking/$prefix-$operation-wrapper.exit" ]]
set -o noclobber
set +e
(
  set -euo pipefail
  sha256sum --check --status "$tracking/$prefix-operation.sha256"
  sha256sum --check --status "$tracking/$prefix-quick4.sha256"
  for step in wrapper formatter syntax phpunit locales; do [[ $(cat "$tracking/$prefix-quick4-$step.exit") == 0 ]]; done
  run_step() {
    local name=$1 directory=$2
    shift 2
    local step_result=0
    [[ ! -e "$tracking/$prefix-operation-$name.log" && ! -e "$tracking/$prefix-operation-$name.exit" ]]
    (cd "$directory" && "$@") >"$tracking/$prefix-operation-$name.log" 2>&1 || step_result=$?
    printf '%s\n' "$step_result" >"$tracking/$prefix-operation-$name.exit"
    printf '%s: exit %s\n' "$name" "$step_result"
    return "$step_result"
  }
  case "$operation" in
    consolidate|publish-v)
      if [[ $operation == consolidate ]]; then source_mode=consolidate; else source_mode=publish; fi
      run_step "$operation" "$worktrees/vpsadmin" env VPSADMIN_PLUGINS=all nix develop .#vpsadmin --command bash "$tracking/$prefix-source-operation.sh" "$source_mode"
      ;;
    cancel-v)
      head=$(cat "$tracking/$prefix-source.sha")
      run_step "$operation" "$worktrees/vpsadmin" nix shell --inputs-from . nixpkgs#gh --command bash "$tracking/$prefix-cancel-ci.sh" "$head"
      ;;
    config|kb-candidate)
      head=$(cat "$tracking/$prefix-source.sha")
      if [[ $operation == config ]]; then repo=vpsfree-cz-configuration; pin_mode=config; else repo=vpsfree-kb-contracts; pin_mode=kb; fi
      run_step "$operation" "$worktrees/$repo" nix develop --command bash "$tracking/$prefix-pin-operation.sh" "$pin_mode" "$head"
      ;;
    publish-pins)
      # K must already have been inspected and committed by root; no automatic
      # transition from kb-candidate into a commit or publication.
      run_step "$operation" "$worktrees/vpsfree-cz-configuration" nix develop --command bash "$tracking/$prefix-pin-publication.sh"
      ;;
  esac
  sha256sum --check --status "$tracking/$prefix-operation.sha256"
) >"$tracking/$prefix-$operation-wrapper.log" 2>&1
result=$?
set -e
printf '%s\n' "$result" >"$tracking/$prefix-$operation-wrapper.exit"
printf 'Legacy network client %s exit %s\n' "$operation" "$result"
exit "$result"
