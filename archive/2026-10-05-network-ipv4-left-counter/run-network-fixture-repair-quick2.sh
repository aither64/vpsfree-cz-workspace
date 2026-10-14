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
[[ ! -e "$tracking/fixture-repair-quick2-wrapper.log" && ! -e "$tracking/fixture-repair-quick2-wrapper.exit" ]]
set +e
(
  set -euo pipefail
  v_root=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin
  w_root=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin-webui
  [[ $(git -C "$v_root" rev-parse HEAD) == 30603a832d2848207bd7319c79c6b0388bc8646a ]]
  [[ $(git -C "$w_root" rev-parse HEAD) == b3b756a7b45864459bd39481a0d5245886777660 ]]
  sha256sum --check "$tracking/network-fixture-repair-freeze2.sha256"
  run_step() {
    local name="$1" directory="$2"
    shift 2
    local step_result=0
    [[ ! -e "$tracking/fixture-repair-quick2-$name.log" && ! -e "$tracking/fixture-repair-quick2-$name.exit" ]]
    (cd "$directory" && "$@") >"$tracking/fixture-repair-quick2-$name.log" 2>&1 || step_result=$?
    printf '%s\n' "$step_result" >"$tracking/fixture-repair-quick2-$name.exit"
    printf '%s: exit %s\n' "$name" "$step_result"
    return "$step_result"
  }
  run_step ruby-syntax-lint "$v_root" env VPSADMIN_PLUGINS=all nix develop .#vpsadmin --command bash "$tracking/network-fixture-repair-checks.sh" ruby
  run_step api-core "$v_root" env VPSADMIN_PLUGINS=none nix develop .#api --command bash "$tracking/network-fixture-repair-checks.sh" core 36954
  run_step api-full "$v_root" env VPSADMIN_PLUGINS=all nix develop .#api --command bash "$tracking/network-fixture-repair-checks.sh" full 9346
  run_step react-quick "$w_root" nix develop --command npm run ci:quick
  sha256sum --check "$tracking/network-fixture-repair-freeze2.sha256"
) >"$tracking/fixture-repair-quick2-wrapper.log" 2>&1
result=$?
set -e
printf '%s\n' "$result" >"$tracking/fixture-repair-quick2-wrapper.exit"
printf 'Fixture repair quick2 exit %s\n' "$result"
exit "$result"
