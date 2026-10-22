#!/usr/bin/env bash
set -euo pipefail
cd /home/aither/.local/state/dev-workspaces/coordination/sources/c14e7d3158b91c134c2817b489cd29772fc09f82/checkout
[[ $(git rev-parse HEAD) == c14e7d3158b91c134c2817b489cd29772fc09f82 ]]
git diff --quiet
[[ ! -f .bundle/config ]]
export HAVEAPI_RELEASE_TOOLS_ONLY=1
nix develop --command bash -euo pipefail <<'HAVEAPI_HOOK_SETUP'
bundle config set --local path .gems/bundled
NIX_ENFORCE_PURITY=0 bundle install
ruby -e 'require "bundler/setup"; require "overcommit"; require "rubocop"; puts "Repository hooks load: Ruby #{RUBY_VERSION}, bundle #{Bundler.bundle_path}"'
NIX_ENFORCE_PURITY=0 /nix/store/5shv7ihqxa98r1psfz995q3j2cwk22sa-ruby-3.4.9/bin/ruby -S bundle install
/nix/store/5shv7ihqxa98r1psfz995q3j2cwk22sa-ruby-3.4.9/bin/ruby -e 'require "bundler/setup"; require "overcommit"; require "rubocop"; puts "Coordinator probe loads: Ruby #{RUBY_VERSION}, bundle #{Bundler.bundle_path}"'
git diff --quiet
HAVEAPI_HOOK_SETUP
