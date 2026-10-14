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
[[ ! -e "$tracking/visibility-review-fix-source-pins.log" && ! -e "$tracking/visibility-review-fix-source-pins.exit" ]]
set +e
(
  set -euo pipefail
  sha256sum --check "$tracking/visibility-review-fix-operation.sha256"
  cd "$worktrees/vpsadmin"
  env VPSADMIN_PLUGINS=all nix develop .#vpsadmin --command bash "$tracking/visibility-review-fix-v-operation.sh" amend
  head=$(cat "$tracking/visibility-review-fixed-v.sha")
  [[ $head =~ ^[0-9a-f]{40}$ ]]
  env VPSADMIN_PLUGINS=all nix develop .#vpsadmin --command bash "$tracking/visibility-review-fix-v-operation.sh" publish "$head"
  nix shell --inputs-from . nixpkgs#gh --command bash "$tracking/visibility-review-fix-cancel-ci.sh" "$head"
  cd "$worktrees/vpsfree-cz-configuration"
  nix develop --command bash "$tracking/visibility-review-fix-pin-operation.sh" config "$head"
  cd "$worktrees/vpsfree-kb-contracts"
  nix develop --command bash "$tracking/visibility-review-fix-pin-operation.sh" kb "$head"
) >"$tracking/visibility-review-fix-source-pins.log" 2>&1
result=$?
set -e
printf '%s\n' "$result" >"$tracking/visibility-review-fix-source-pins.exit"
exit "$result"
