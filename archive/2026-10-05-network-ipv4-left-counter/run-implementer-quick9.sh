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
w_root=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin-webui
run_step() {
  local name="$1"
  shift
  local result=0
  (cd "$w_root" && "$@") >"$tracking/quick9-$name.log" 2>&1 || result=$?
  printf '%s\n' "$result" >"$tracking/quick9-$name.exit"
  printf '%s: exit %s\n' "$name" "$result"
  return "$result"
}
run_step react-units nix develop --command npm test -- src/lib/api/networks.test.ts src/lib/api/ipAddresses.test.ts src/pages/app/networking/fetchAssignableIpAddresses.test.ts src/pages/app/admin/cluster/NetworksPage.test.tsx src/pages/app/networking/UserNetworkAddressActions.test.tsx
run_step react-quick nix develop --command npm run ci:quick
