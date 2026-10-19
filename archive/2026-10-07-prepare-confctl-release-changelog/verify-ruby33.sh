#!/usr/bin/env bash
set -euo pipefail
test "$(ruby -e 'print RUBY_VERSION.split(".").take(2).join(".")')" = 3.3
export GEM_HOME="$PWD/.gems/ruby/$(ruby -e 'require "rbconfig"; print RbConfig::CONFIG["ruby_version"]')"
export GEM_PATH="$GEM_HOME"
export BUNDLE_PATH="$PWD/.gems"
export BUNDLE_APP_CONFIG="$PWD/.bundle"
printf 'Minimum supported runtime check: '
ruby --version
ruby "$GEM_HOME/bin/bundle" check
source_tree=$PWD
records=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-07-prepare-confctl-release-changelog
spec_work=$(mktemp -d "$records/rspec-ruby33.XXXXXX")
export BUNDLE_GEMFILE="$source_tree/Gemfile"
cd "$spec_work"
ruby "$GEM_HOME/bin/bundle" exec rspec -I "$source_tree/spec" --require "$source_tree/spec/spec_helper.rb" "$source_tree/spec"
