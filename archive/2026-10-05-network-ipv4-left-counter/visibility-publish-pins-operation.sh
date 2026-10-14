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
sha256sum --check "$tracking/visibility-publish-pins.sha256"
[[ ! -e "$tracking/visibility-pin-publication.log" && ! -e "$tracking/visibility-pin-publication.exit" ]]
set +e
(
  set -euo pipefail
  cd "$worktrees/vpsfree-cz-configuration"
  nix develop --command bash "$tracking/visibility-publish-pin-branches.sh" config 74a1a6acbc272cc73a3bca468ed10a8b93464957
  nix shell --inputs-from . nixpkgs#gh --command bash "$tracking/visibility-cancel-pin-ci.sh" config 74a1a6acbc272cc73a3bca468ed10a8b93464957
  cd "$worktrees/vpsfree-kb-contracts"
  nix develop --command bash "$tracking/visibility-publish-pin-branches.sh" kb 1f8817e5c519818f7fb156751cdacc784d998f42
  nix shell --inputs-from . nixpkgs#gh --command bash "$tracking/visibility-cancel-pin-ci.sh" kb 1f8817e5c519818f7fb156751cdacc784d998f42
) >"$tracking/visibility-pin-publication.log" 2>&1
result=$?
set -e
printf '%s\n' "$result" >"$tracking/visibility-pin-publication.exit"
exit "$result"
