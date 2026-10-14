#!/usr/bin/env bash
set -euo pipefail
umask 077
export PATH=/home/aither/bin:/run/wrappers/bin:/home/aither/.nix-profile/bin:/nix/profile/bin:/home/aither/.local/state/nix/profile/bin:/etc/profiles/per-user/aither/bin:/nix/var/nix/profiles/default/bin:/run/current-system/sw/bin:$PATH
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
cd "$tracking"
[[ $(dev-session current) == 2026-10-05-network-ipv4-left-counter ]]
[[ ! -e legacy-network-client-source-pins.log && ! -e legacy-network-client-source-pins.exit ]]
set -o noclobber
set +e
(
  set -euo pipefail
  sha256sum --check --status "$tracking/legacy-network-client-operation.sha256"
  for mode in consolidate publish-v cancel-v config kb-candidate; do
    bash "$tracking/legacy-network-client-operation.sh" "$mode"
  done
) >"$tracking/legacy-network-client-source-pins.log" 2>&1
result=$?
set -e
printf '%s\n' "$result" >"$tracking/legacy-network-client-source-pins.exit"
printf 'Legacy client source and pins exit %s\n' "$result"
exit "$result"
