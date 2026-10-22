#!/usr/bin/env bash
set -euo pipefail
cd /home/aither/.local/state/dev-workspaces/coordination/sources/c58704a08451a231fdf6c6123437133422af46dc/checkout
[[ $(git rev-parse HEAD) == c58704a08451a231fdf6c6123437133422af46dc ]]
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

#!/usr/bin/env bash
set -euo pipefail
cd /home/aither/.local/state/dev-workspaces/coordination/sources/c58704a08451a231fdf6c6123437133422af46dc/checkout
[[ $(git rev-parse HEAD) == c58704a08451a231fdf6c6123437133422af46dc ]]
git diff --quiet
export HAVEAPI_RELEASE_TOOLS_ONLY=1
nix develop --command bash -euo pipefail <<'HAVEAPI_HOOK_JSON_SETUP'
# Keep both entry points compatible with the coordinator's default JSON gem.
gem uninstall json --version 2.21.2 --install-dir "$GEM_HOME" --ignore-dependencies --executables
NIX_ENFORCE_PURITY=0 gem install json --version 2.9.1 --no-document
/nix/store/5shv7ihqxa98r1psfz995q3j2cwk22sa-ruby-3.4.9/bin/ruby -S gem uninstall json --version 2.21.2 --install-dir "$PWD/.gems/bundled/ruby/3.4.0" --ignore-dependencies --executables
/nix/store/5shv7ihqxa98r1psfz995q3j2cwk22sa-ruby-3.4.9/bin/ruby -S bundle lock --local --update json
NIX_ENFORCE_PURITY=0 /nix/store/5shv7ihqxa98r1psfz995q3j2cwk22sa-ruby-3.4.9/bin/ruby -S bundle install
NIX_ENFORCE_PURITY=0 bundle install
ruby -e 'require "json"; require "bundler"; Bundler.setup; require "overcommit"; require "rubocop"; puts "Repository exact-order probe: Ruby #{RUBY_VERSION}, JSON #{JSON::VERSION}, bundle #{Bundler.bundle_path}"'
/nix/store/5shv7ihqxa98r1psfz995q3j2cwk22sa-ruby-3.4.9/bin/ruby -e 'require "json"; require "bundler"; Bundler.setup; require "overcommit"; require "rubocop"; puts "Coordinator exact-order probe: Ruby #{RUBY_VERSION}, JSON #{JSON::VERSION}, bundle #{Bundler.bundle_path}"'
git diff --quiet
HAVEAPI_HOOK_JSON_SETUP
