#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
cd "$tracking"
test "$(dev-session current)" = 2026-10-05-network-ipv4-left-counter
export DEV_SESSION_SLUG=2026-10-05-network-ipv4-left-counter
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
v_root=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin
w_root=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin-webui
run_step() {
  local name="$1" directory="$2"
  shift 2
  local result=0
  (cd "$directory" && "$@") >"$tracking/quick6-$name.log" 2>&1 || result=$?
  printf '%s\n' "$result" >"$tracking/quick6-$name.exit"
  printf '%s: exit %s\n' "$name" "$result"
  return "$result"
}
run_step ruby-syntax-lint "$v_root" nix develop .#vpsadmin --command bash "$tracking/implementer-scoped-checks.sh" ruby
run_step php-locales "$v_root" nix develop .#webui --command bash "$tracking/implementer-scoped-checks.sh" php-locales
run_step php-format "$v_root" nix develop .#vpsadmin --command bash "$tracking/implementer-scoped-checks.sh" php-format
run_step php-syntax-lint-unit "$v_root" nix develop .#webui --command bash "$tracking/implementer-scoped-checks.sh" php
run_step nix-format "$v_root" nix develop .#vpsadmin --command bash "$tracking/implementer-scoped-checks.sh" nix
run_step api-batches-continuity "$v_root" env VPSADMIN_PLUGINS=all nix develop .#api --command bundle exec rspec spec/models/transaction_chains/ip/allocate_spec.rb spec/models/transaction_chains/export/create_spec.rb spec/models/transaction_chains/vps/create_spec.rb spec/models/transaction_chains/vps/clone/os_to_os_spec.rb spec/models/transaction_chains/vps/migrate_spec.rb spec/models/transaction_chains/vps/swap_spec.rb spec/models/transaction_chains/vps/replace/os_spec.rb
run_step react-inventory "$w_root" nix develop --command npm run docs:inventory
run_step react-quick "$w_root" nix develop --command npm run ci:quick
