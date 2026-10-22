#!/usr/bin/env bash
set -euo pipefail

cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-dynamic-python-api-client/haveapi
export DEV_WORKSPACE_CLAIM_ID=342cd062-0205-45c7-b636-20d958b8fa75

# Keep the workspace CLI outside the project's Ruby/Bundler activation.
unset GEM_HOME GEM_PATH BUNDLE_GEMFILE BUNDLE_LOCKFILE BUNDLE_BIN_PATH
unset BUNDLE_PATH BUNDLE_APP_CONFIG BUNDLER_VERSION RUBYOPT RUBYLIB
export BUNDLE_FROZEN=true PYTHONDONTWRITEBYTECODE=1

check_owned_inputs() {
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
assert subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip() == (
    'a8ea3132e7efe601aaa8965afe648459b3dab5c5'
)
assert subprocess.check_output(['git', 'rev-parse', 'HEAD^{tree}'], text=True).strip() == (
    '9a596258d912ca2075c36ded30d11b3984c656ae'
)
assert not subprocess.check_output(['git', '--no-optional-locks', 'status', '--porcelain'], text=True).strip()
for filename, expected in {
    'Gemfile.lock': '450de01a459fd59f8237065094ee4bf59d1263049af14244a768b29b7f2ebfc5',
    'servers/ruby/Gemfile.lock': '9a67113645cceed6c4abf54a207d3cd8186f335e59c45b7b0161c840aacd4636',
    'clients/ruby/Gemfile.lock': 'cf9311f2342ab2764b85a5092d47ff06a8567e6de17a03c8850a4d8f78e58b05',
    'clients/go/Gemfile.lock': '7fd2c67b745579cf39a9d9158d7cbe5503956b71c4237eff8ace3f028c98baf0',
}.items():
    assert hashlib.sha256(Path(filename).read_bytes()).hexdigest() == expected, filename
print('Exact owned source, held claim and all four bundle locks verified')
PY
}

check_owned_inputs

nix develop .#client-go --command bash -euo pipefail -c '
  test "$GEM_HOME" = "$HAVEAPI_REPO_ROOT/clients/go/.gems"
  ruby --version
  # The Go shell preloads Bundler for its own Gemfile through RUBYOPT. Remove
  # only that preload for these explicit server-bundle setup/load commands.
  # Match the scoped native-extension build setting in the root shell.
  env -u RUBYOPT \
    BUNDLE_GEMFILE="$HAVEAPI_REPO_ROOT/servers/ruby/Gemfile" \
    BUNDLE_LOCKFILE="$HAVEAPI_REPO_ROOT/servers/ruby/Gemfile.lock" \
    NIX_ENFORCE_PURITY=0 bundle install
  env -u RUBYOPT \
    BUNDLE_GEMFILE="$HAVEAPI_REPO_ROOT/servers/ruby/Gemfile" \
    BUNDLE_LOCKFILE="$HAVEAPI_REPO_ROOT/servers/ruby/Gemfile.lock" \
    bundle check
  env -u RUBYOPT \
    BUNDLE_GEMFILE="$HAVEAPI_REPO_ROOT/servers/ruby/Gemfile" \
    BUNDLE_LOCKFILE="$HAVEAPI_REPO_ROOT/servers/ruby/Gemfile.lock" \
    bundle exec ruby -e '\''
      abort "expected Ruby 3.4" unless RUBY_VERSION.start_with?("3.4.")
      require "haveapi"
      require "rackup"
      require "webrick"
      puts "Go ordinary gem home can load the locked server fixture bundle"
    '\''
'

check_owned_inputs
