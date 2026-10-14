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
prefix=legacy-network-client-quick2
[[ ! -e "$tracking/$prefix-wrapper.log" && ! -e "$tracking/$prefix-wrapper.exit" ]]
set -o noclobber
set +e
(
  set -euo pipefail
  v_root=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin
  verify_source() {
    [[ $(git -C "$v_root" rev-parse HEAD) == cc3337d0a2699a8b28a0327bbee5ef62f3fbe166 ]]
    [[ $(git -C "$v_root" branch --show-current) == 2026-10-05-network-ipv4-left-counter ]]
    [[ -z $(git -C "$v_root" diff --cached --name-only) ]]
    [[ $(git -C "$v_root" status --porcelain) == "$(cat "$tracking/$prefix.status")" ]]
    [[ $(git -C "$v_root" diff --name-only) == "$(cat "$tracking/$prefix.paths")" ]]
    git -C "$v_root" diff --exit-code HEAD -- api/db/schema.rb api/db/migrate tests/suite tests/playwright webui/composer.json webui/composer.lock webui/lang
    sha256sum --check --status "$tracking/$prefix.sha256"
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
  run_step formatter "$v_root" nix develop .#vpsadmin --command bash "$tracking/$prefix-checks.sh" formatter
  verify_source
  run_step syntax "$v_root" nix develop .#webui --command bash "$tracking/$prefix-checks.sh" syntax
  verify_source
  run_step phpunit "$v_root" nix develop .#webui --command bash "$tracking/$prefix-checks.sh" phpunit
  verify_source
  run_step locales "$v_root" nix develop .#webui --command bash "$tracking/$prefix-checks.sh" locales
  verify_source
) >"$tracking/$prefix-wrapper.log" 2>&1
result=$?
set -e
printf '%s\n' "$result" >"$tracking/$prefix-wrapper.exit"
printf 'Legacy network real-client quick1 exit %s\n' "$result"
exit "$result"
