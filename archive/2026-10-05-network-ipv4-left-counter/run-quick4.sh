#!/usr/bin/env bash
set -euo pipefail

tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
v_repo=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin
w_repo=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin-webui

if [[ -n ${DATABASE_URL:-} || -e "$v_repo/api/config/database.yml" ]]; then
  printf '%s\n' 'Refusing configured database; isolated automatic test DB required.' >&2
  exit 2
fi

run_check() {
  local check_name=$1 check_dir=$2 check_status
  shift 2
  if (cd "$check_dir" && "$@") >"$tracking/quick4-$check_name.log" 2>&1; then
    check_status=0
  else
    check_status=$?
  fi
  printf '%s\n' "$check_status" >"$tracking/quick4-$check_name.exit"
  printf '%s: exit %s\n' "$check_name" "$check_status"
  return "$check_status"
}

run_check counter "$v_repo" env VPSADMIN_PLUGINS=all nix develop .#api --command \
  bundle exec rspec spec/api/resources/cluster_spec.rb:183
run_check migration "$v_repo" env VPSADMIN_PLUGINS=none nix develop .#api --command \
  bundle exec rspec spec/migrations/20261006120000_add_network_enabled_spec.rb
run_check react-units "$w_repo" nix develop --command npm test -- \
  src/lib/api/networks.test.ts src/lib/api/ipAddresses.test.ts \
  src/pages/app/networking/fetchAssignableIpAddresses.test.ts \
  src/pages/app/admin/cluster/NetworksPage.test.tsx
run_check react-types "$w_repo" nix develop --command npm run typecheck
