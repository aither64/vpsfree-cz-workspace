#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
if [[ ${DEV_SESSION_SLUG+x} || ${DEV_SESSION_WORKSPACE+x} ]]; then
  [[ ${DEV_SESSION_SLUG-} == 2026-10-05-network-ipv4-left-counter && ${DEV_SESSION_WORKSPACE-} == /home/aither/workspace/ai/vpsfree.cz ]]
fi
cd "$tracking"
[[ $(dev-session current) == 2026-10-05-network-ipv4-left-counter ]]
export DEV_SESSION_SLUG=2026-10-05-network-ipv4-left-counter
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
export VISIBILITY_CHECK_PREFIX=visibility-quick2
[[ ! -e "$tracking/visibility-quick2-wrapper.log" && ! -e "$tracking/visibility-quick2-wrapper.exit" ]]
set +e
(
  set -euo pipefail
  v_root=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin
  sha256sum --check "$tracking/visibility-quick2.sha256"
  python3 "$tracking/visibility-guard.py"
  run_step() {
    local name="$1" directory="$2"
    shift 2
    local step_result=0
    [[ ! -e "$tracking/visibility-quick2-$name.log" && ! -e "$tracking/visibility-quick2-$name.exit" ]]
    (cd "$directory" && "$@") >"$tracking/visibility-quick2-$name.log" 2>&1 || step_result=$?
    printf '%s\n' "$step_result" >"$tracking/visibility-quick2-$name.exit"
    printf '%s: exit %s\n' "$name" "$step_result"
    return "$step_result"
  }
  run_step ruby-syntax-lint "$v_root" env VPSADMIN_PLUGINS=all nix develop .#vpsadmin --command bash "$tracking/visibility-checks.sh" ruby
  run_step api-core "$v_root" env VPSADMIN_PLUGINS=none nix develop .#api --command bash "$tracking/visibility-checks.sh" core 36954
  run_step api-full "$v_root" env VPSADMIN_PLUGINS=all nix develop .#api --command bash "$tracking/visibility-checks.sh" full 9346
  sha256sum --check "$tracking/visibility-quick2.sha256"
  python3 "$tracking/visibility-guard.py"
) >"$tracking/visibility-quick2-wrapper.log" 2>&1
result=$?
set -e
printf '%s\n' "$result" >"$tracking/visibility-quick2-wrapper.exit"
printf 'Visibility quick2 exit %s\n' "$result"
exit "$result"
