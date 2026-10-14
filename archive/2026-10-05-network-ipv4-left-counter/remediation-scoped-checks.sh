#!/usr/bin/env bash
set -euo pipefail
v_root=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin
case "${1-}" in
  ruby)
    cd "$v_root"
    files=(api/models/transaction_chains/vps/update.rb api/spec/models/transaction_chains/vps/update_spec.rb)
    for path in "${files[@]}"; do ruby -c "$path"; done
    bundle exec rubocop --force-exclusion "${files[@]}"
    ;;
  api)
    cd "$v_root/api"
    [[ ! ${DATABASE_URL+x} && ! -e config/database.yml ]]
    bundle exec rspec spec/models/transaction_chains/vps/update_spec.rb
    ;;
  *) exit 2 ;;
esac
