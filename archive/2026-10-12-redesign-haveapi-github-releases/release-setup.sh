#!/usr/bin/env bash
set -euo pipefail
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-redesign-haveapi-github-releases/haveapi-release
unset GEM_HOME GEM_PATH BUNDLE_GEMFILE BUNDLE_PATH RUBYOPT
nix develop -c bash -euo pipefail -c '
  ruby --version
  bundle exec ruby -e '\''require "overcommit"; require "rubocop"; require "rspec"; puts "release hook dependencies loaded"'\''
'
