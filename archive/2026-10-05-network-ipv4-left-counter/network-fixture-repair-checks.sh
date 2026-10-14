#!/usr/bin/env bash
set -euo pipefail
v_root=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin
case "${1-}" in
  ruby)
    cd "$v_root"
    ruby -c api/spec/models/ip_ownership_concurrency_spec.rb
    bundle exec rubocop --force-exclusion api/spec/models/ip_ownership_concurrency_spec.rb
    ;;
  core|full)
    mode=$1
    seed=${2:?Missing randomized seed}
    [[ $seed =~ ^[0-9]+$ ]]
    if [[ $mode == core ]]; then expected_plugins=none; else expected_plugins=all; fi
    [[ ${VPSADMIN_PLUGINS-} == "$expected_plugins" ]]
    cd "$v_root/api"
    [[ ! ${DATABASE_URL+x} && ! -e config/database.yml ]]
    # RSpec owns its isolated temporary MariaDB through the existing helper.
    # Include every concurrency example and the adjacent Create regression.
    bundle exec rspec spec/models/ip_ownership_concurrency_spec.rb \
      spec/models/transaction_chains/vps/create_spec.rb --seed "$seed"
    ;;
  *) exit 2 ;;
esac
