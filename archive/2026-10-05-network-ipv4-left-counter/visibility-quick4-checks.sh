#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
v_root=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin
check_prefix=${VISIBILITY_CHECK_PREFIX:?Missing check receipt prefix}
[[ $check_prefix =~ ^visibility-quick[0-9]+$ ]]
ruby_paths=(
  api/spec/api/resources/ip_address_spec.rb
  api/spec/api/resources/ip_address_assignment_spec.rb
)
spec_paths=(
  spec/api/resources/network_read_spec.rb
  spec/api/resources/ip_address_spec.rb
  spec/api/resources/host_ip_address_spec.rb
  spec/api/resources/network_interface_spec.rb
  spec/api/resources/ip_address_assignment_spec.rb
)
case "${1-}" in
  ruby)
    cd "$v_root"
    for path in "${ruby_paths[@]}"; do ruby -c "$path"; done
    export RUBOCOP_CACHE_ROOT="$tracking/$check_prefix-rubocop-cache"
    bundle exec rubocop --force-exclusion "${ruby_paths[@]}"
    ;;
  core|full)
    mode=$1
    if [[ $mode == core ]]; then
      selected_specs=(
        'spec/api/resources/ip_address_spec.rb[1:2:1:7]'
        'spec/api/resources/ip_address_spec.rb[1:3:1]'
        'spec/api/resources/ip_address_assignment_spec.rb[1:2:1]'
      )
    else
      selected_specs=("${spec_paths[@]}")
    fi
    seed=${2:?Missing randomized seed}
    [[ $seed =~ ^[0-9]+$ ]]
    if [[ $mode == core ]]; then expected_plugins=none; else expected_plugins=all; fi
    [[ ${VPSADMIN_PLUGINS-} == "$expected_plugins" ]]
    cd "$v_root/api"
    [[ ! ${DATABASE_URL+x} && ! -e config/database.yml ]]
    [[ ${VPSADMIN_TEST_DB_AUTO-1} != 0 ]]
    [[ ! -e "$tracking/$check_prefix-api-$mode.json" ]]
    export TMPDIR=/tmp
    bundle exec ruby -rdigest -rrspec/core/version -e '
      puts "Ruby=#{RUBY_VERSION} Bundler=#{Bundler::VERSION} RSpec=#{RSpec::Core::Version::STRING}"
      puts "VPSADMIN_PLUGINS=#{ENV.fetch("VPSADMIN_PLUGINS")} Gemfile.lock=#{Digest::SHA256.file("Gemfile.lock").hexdigest}"
    '
    # The existing RSpec helper owns an isolated temporary MariaDB per process.
    bundle exec rspec "${selected_specs[@]}" --seed "$seed" --format documentation \
      --format json --out "$tracking/$check_prefix-api-$mode.json"
    ;;
  *) exit 2 ;;
esac
