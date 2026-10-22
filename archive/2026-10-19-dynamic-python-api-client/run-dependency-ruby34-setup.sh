#!/usr/bin/env bash
set -euo pipefail

cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-dynamic-python-api-client/haveapi
export DEV_WORKSPACE_CLAIM_ID=342cd062-0205-45c7-b636-20d958b8fa75

python3 - <<'PY'
import hashlib
import json
from pathlib import Path
import subprocess

claim = json.loads(subprocess.check_output([
    'dev-session', 'coordination', 'claim-status',
    '2026-10-19-dynamic-python-api-client', '--as-is',
    '--id', '342cd062-0205-45c7-b636-20d958b8fa75', '--json',
], text=True))
assert claim['state'] == 'held'
assert claim['ownerId'] == 'e51277e3-c4c3-43eb-b889-90e84d91b5bf'
assert hashlib.sha256(Path('flake.lock').read_bytes()).hexdigest() == (
    'a52bdf3a3b9a069175d3af298234c3cf7adeba54540833eed6ad902e9ccc0a64'
)
assert subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip() == (
    'c1823f3d70365b0442d0e2171bdf83bd4c6dbe31'
)
assert subprocess.check_output(['git', 'diff', '--cached', '--name-only'], text=True).strip() == 'flake.nix'
print('Setup preflight: held claim, original HEAD, exact generated lock and owned staged compatibility source')
PY

# Use each declared shell's ordinary GEM_HOME and initialization. Frozen Bundler
# prevents incidental dependency resolution while rebuilding native extensions.
unset GEM_HOME GEM_PATH BUNDLE_GEMFILE BUNDLE_PATH BUNDLE_APP_CONFIG RUBYOPT
unset HAVEAPI_RELEASE_TOOLS_ONLY
export BUNDLE_FROZEN=true

nix flake check --all-systems --no-build
nix flake check

nix develop . --command bash -euo pipefail -c '
  test "$GEM_HOME" = "$HAVEAPI_REPO_ROOT/.gems"
  ruby --version
  bundle check
  bundle exec ruby -rrbconfig -e '\''
    abort "expected Ruby 3.4" unless RUBY_VERSION.start_with?("3.4.")
    require "overcommit"
    require "rake"
    require "json"
    require "prism"
    require "bigdecimal"
    puts "root ABI=#{RbConfig::CONFIG.fetch("ruby_version")} Overcommit=#{Gem.loaded_specs.fetch("overcommit").version} native extensions loaded"
  '\''
  uv --version
  ruff --version
'

nix develop .#server-ruby --command bash -euo pipefail -c '
  test "$GEM_HOME" = "$HAVEAPI_REPO_ROOT/.gems"
  cd "$HAVEAPI_REPO_ROOT/servers/ruby"
  ruby --version
  bundle check
  bundle exec ruby -e '\''
    abort "expected Ruby 3.4" unless RUBY_VERSION.start_with?("3.4.")
    require "json"
    require "sqlite3"
    require "redcarpet"
    require "haveapi"
    puts "server Ruby/native gems loaded"
  '\''
'

nix develop .#client-ruby --command bash -euo pipefail -c '
  test "$GEM_HOME" = "$HAVEAPI_REPO_ROOT/.gems"
  cd "$HAVEAPI_REPO_ROOT/clients/ruby"
  ruby --version
  bundle check
  bundle exec ruby -e '\''
    abort "expected Ruby 3.4" unless RUBY_VERSION.start_with?("3.4.")
    require "haveapi/client"
    puts "Ruby client loaded"
  '\''
'

nix develop .#client-go --command bash -euo pipefail -c '
  test "$GEM_HOME" = "$HAVEAPI_REPO_ROOT/clients/go/.gems"
  cd "$HAVEAPI_REPO_ROOT/clients/go"
  ruby --version
  bundle check
  bundle exec ruby -e '\''
    abort "expected Ruby 3.4" unless RUBY_VERSION.start_with?("3.4.")
    require "haveapi/go_client"
    puts "Go generator loaded"
  '\''
'

nix develop .#client-python --command bash -euo pipefail -c '
  test "$GEM_HOME" = "$HAVEAPI_REPO_ROOT/.gems"
  ruby -rovercommit -e '\''
    abort "expected Ruby 3.4" unless RUBY_VERSION.start_with?("3.4.")
    puts "Python shell normal hook loader ready"
  '\''
  uv --version
  ruff --version
'

python3 - <<'PY'
import hashlib
from pathlib import Path
assert hashlib.sha256(Path('flake.lock').read_bytes()).hexdigest() == (
    'a52bdf3a3b9a069175d3af298234c3cf7adeba54540833eed6ad902e9ccc0a64'
)
print('Generated flake.lock preserved exactly; setup/check batch complete')
PY
