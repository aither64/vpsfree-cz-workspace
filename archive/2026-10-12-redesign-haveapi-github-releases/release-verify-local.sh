#!/usr/bin/env bash
set -euo pipefail
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-redesign-haveapi-github-releases/haveapi-release
expected=$1
[[ $(git rev-parse HEAD) == "$expected" ]]
nix develop -c bash -euo pipefail -c '
  make release-deps
  make release-check
  make release-test
  bundle exec rake i18n:health
  make release
  make test
  ruby utils/release/cli.rb smoke-npm dist
  ruby utils/release/cli.rb verify dist
  package_dir=$(mktemp -d)
  for package in dist/*.gem; do
    gem unpack "$package" --target "$package_dir"
  done
  version=$(cat VERSION)
  ruby -I "$package_dir/haveapi-client-$version/lib" \
    -I "$package_dir/haveapi-$version/lib" \
    -I "$package_dir/haveapi-go-client-$version/lib" \
    -e '\''require "haveapi"; require "haveapi/client"; require "haveapi/go_client"; abort "Packaged version mismatch" unless [HaveAPI::VERSION, HaveAPI::Client::VERSION, HaveAPI::GoClient::VERSION].all? { |v| v == ARGV.fetch(0) }; puts "Loaded all packaged Ruby libraries"'\'' "$version"
'
