#!/usr/bin/env bash
set -euo pipefail
test "$(ruby -e 'print RUBY_VERSION.split(".").take(2).join(".")')" = 3.3
export GEM_HOME="$PWD/.gems/ruby/$(ruby -e 'require "rbconfig"; print RbConfig::CONFIG["ruby_version"]')"
export GEM_PATH="$GEM_HOME"
export BUNDLE_PATH="$PWD/.gems"
export BUNDLE_APP_CONFIG="$PWD/.bundle"
mkdir -p "$GEM_HOME"
if ! gem list -i bundler -v 2.5.7 >/dev/null; then
  gem install --no-document bundler -v 2.5.7
fi
ruby "$GEM_HOME/bin/bundle" update
printf 'Dependency resolution Ruby: '
ruby --version
