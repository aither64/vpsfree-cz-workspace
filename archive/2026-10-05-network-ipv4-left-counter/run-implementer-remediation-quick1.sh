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
v_root=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin
w_root=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin-webui
sha256sum --check "$tracking/remediation-source-freeze.sha256"
run_step() {
  local name="$1" directory="$2"
  shift 2
  local result=0
  (cd "$directory" && "$@") >"$tracking/remediation-quick1-$name.log" 2>&1 || result=$?
  printf '%s\n' "$result" >"$tracking/remediation-quick1-$name.exit"
  printf '%s: exit %s\n' "$name" "$result"
  return "$result"
}
run_step ruby-syntax-lint "$v_root" env VPSADMIN_PLUGINS=all nix develop .#vpsadmin --command bash "$tracking/remediation-scoped-checks.sh" ruby
run_step legacy-browser-syntax "$w_root" nix develop --command node --check "$v_root/tests/playwright/webui/specs/admin-cluster.spec.cjs"
run_step api-chown "$v_root" env VPSADMIN_PLUGINS=all nix develop .#api --command bash "$tracking/remediation-scoped-checks.sh" api
run_step react-units "$w_root" nix develop --command npm test -- src/lib/api/networks.test.ts src/lib/api/ipAddresses.test.ts src/pages/app/networking/fetchAssignableIpAddresses.test.ts src/pages/app/admin/cluster/NetworksPage.test.tsx src/pages/app/networking/UserNetworkAddressActions.test.tsx src/pages/app/admin/ipAddresses/useProgressiveSuggestedIpQueries.test.tsx
run_step react-quick "$w_root" nix develop --command npm run ci:quick
sha256sum --check "$tracking/remediation-source-freeze.sha256"
