#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
v_root=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin
prefix=visibility-review-fix-quick1
case "${1-}" in
  ruby)
    cd "$v_root"
    ruby -c api/spec/api/resources/network_write_spec.rb
    export RUBOCOP_CACHE_ROOT="$tracking/$prefix-rubocop-cache"
    bundle exec rubocop --force-exclusion api/spec/api/resources/network_write_spec.rb
    ;;
  core|full)
    mode=$1
    seed=${2:?Missing randomized seed}
    [[ $seed =~ ^[0-9]+$ ]]
    if [[ $mode == core ]]; then plugins=none; else plugins=all; fi
    [[ ${VPSADMIN_PLUGINS-} == "$plugins" ]]
    cd "$v_root/api"
    [[ ! ${DATABASE_URL+x} && ! -e config/database.yml ]]
    [[ ${VPSADMIN_TEST_DB_AUTO-1} != 0 ]]
    [[ ! -e "$tracking/$prefix-api-$mode.json" ]]
    export TMPDIR=/tmp
    bundle exec ruby -rdigest -rrspec/core/version -e '
      puts "Ruby=#{RUBY_VERSION} Bundler=#{Bundler::VERSION} RSpec=#{RSpec::Core::Version::STRING}"
      puts "VPSADMIN_PLUGINS=#{ENV.fetch("VPSADMIN_PLUGINS")} Gemfile.lock=#{Digest::SHA256.file("Gemfile.lock").hexdigest}"
    '
    # Existing RSpec helper owns unique temporary MariaDB and normal-exit cleanup.
    bundle exec rspec spec/api/resources/network_write_spec.rb --seed "$seed" \
      --format documentation --format json --out "$tracking/$prefix-api-$mode.json"
    ;;
  *) exit 2 ;;
esac
