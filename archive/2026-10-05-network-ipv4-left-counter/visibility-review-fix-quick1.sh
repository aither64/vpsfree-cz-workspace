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
prefix=visibility-review-fix-quick1
[[ ! -e "$tracking/$prefix-wrapper.log" && ! -e "$tracking/$prefix-wrapper.exit" ]]
set +e
(
  set -euo pipefail
  v_root=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin
  verify_source() {
    [[ $(git -C "$v_root" rev-parse HEAD) == d7d7fb66865fd1a5548a45a559f5c2be436bc470 ]]
    [[ $(git -C "$v_root" branch --show-current) == 2026-10-05-network-ipv4-left-counter ]]
    [[ $(git -C "$v_root" status --porcelain) == ' M api/spec/api/resources/network_write_spec.rb' ]]
    [[ ! ${DATABASE_URL+x} && ! -e "$v_root/api/config/database.yml" ]]
    git -C "$v_root" diff --exit-code HEAD -- api/db/schema.rb api/db/migrate
    sha256sum --check "$tracking/$prefix.sha256"
  }
  run_step() {
    local name=$1 directory=$2
    shift 2
    local step_result=0
    [[ ! -e "$tracking/$prefix-$name.log" && ! -e "$tracking/$prefix-$name.exit" ]]
    (cd "$directory" && "$@") >"$tracking/$prefix-$name.log" 2>&1 || step_result=$?
    printf '%s\n' "$step_result" >"$tracking/$prefix-$name.exit"
    printf '%s: exit %s\n' "$name" "$step_result"
    return "$step_result"
  }
  verify_source
  run_step ruby-syntax-lint "$v_root" env VPSADMIN_PLUGINS=all nix develop .#vpsadmin --command bash "$tracking/visibility-review-fix-checks.sh" ruby
  verify_source
  run_step api-core "$v_root" env VPSADMIN_PLUGINS=none nix develop .#api --command bash "$tracking/visibility-review-fix-checks.sh" core 36954
  verify_source
  run_step api-full "$v_root" env VPSADMIN_PLUGINS=all nix develop .#api --command bash "$tracking/visibility-review-fix-checks.sh" full 9346
  verify_source
) >"$tracking/$prefix-wrapper.log" 2>&1
result=$?
set -e
printf '%s\n' "$result" >"$tracking/$prefix-wrapper.exit"
printf 'Visibility review fix quick1 exit %s\n' "$result"
exit "$result"
