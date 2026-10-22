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
expected = {
    'flake.nix': '37d7230994d0ed95c3ecfef2ba43d65933f4b55c28d1e56f48f07c7bf79de91c',
    'Gemfile.lock': '450de01a459fd59f8237065094ee4bf59d1263049af14244a768b29b7f2ebfc5',
    'servers/ruby/Gemfile.lock': '9a67113645cceed6c4abf54a207d3cd8186f335e59c45b7b0161c840aacd4636',
}
for filename, digest in expected.items():
    assert hashlib.sha256(Path(filename).read_bytes()).hexdigest() == digest, filename
assert hashlib.sha256(subprocess.check_output(['git', 'show', ':flake.nix'])).hexdigest() == expected['flake.nix']
for filename in ('clients/ruby/Gemfile.lock', 'clients/go/Gemfile.lock'):
    assert not Path(filename).exists(), f'Unexpected preexisting component lock: {filename}'
print('Setup preflight: held claim, guarded source/index, exact generated lock, frozen preexisting root/server locks; client/Go locks absent')
PY

# Use each declared shell's ordinary GEM_HOME and initialization. Freeze only
# existing root/server locks; allow ordinary first-time client/Go lock creation.
unset GEM_HOME GEM_PATH BUNDLE_GEMFILE BUNDLE_PATH BUNDLE_APP_CONFIG RUBYOPT
unset HAVEAPI_RELEASE_TOOLS_ONLY
export BUNDLE_FROZEN=true

# Attempt 1 already passed the unchanged all-systems no-build evaluation.
# Complete its interrupted normal flake check here.
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

env -u BUNDLE_FROZEN nix develop .#client-ruby --command bash -euo pipefail -c '
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

env -u BUNDLE_FROZEN nix develop .#client-go --command bash -euo pipefail -c '
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
expected = {
    'flake.nix': '37d7230994d0ed95c3ecfef2ba43d65933f4b55c28d1e56f48f07c7bf79de91c',
    'Gemfile.lock': '450de01a459fd59f8237065094ee4bf59d1263049af14244a768b29b7f2ebfc5',
    'servers/ruby/Gemfile.lock': '9a67113645cceed6c4abf54a207d3cd8186f335e59c45b7b0161c840aacd4636',
}
for filename, digest in expected.items():
    assert hashlib.sha256(Path(filename).read_bytes()).hexdigest() == digest, filename
for filename in ('clients/ruby/Gemfile.lock', 'clients/go/Gemfile.lock'):
    lock = Path(filename)
    assert lock.is_file(), f'Ordinary first-install lock missing: {filename}'
    print(f'Created ignored lock {filename}: SHA256 {hashlib.sha256(lock.read_bytes()).hexdigest()}')
print('Exact source/generated lock and preexisting root/server locks preserved; setup/check batch complete')
PY
