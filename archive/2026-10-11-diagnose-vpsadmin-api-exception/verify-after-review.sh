#!/usr/bin/env bash
set -euo pipefail
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-11-diagnose-vpsadmin-api-exception/haveapi
nix develop -c bash -s <<'VERIFY'
set -euo pipefail
repo_root="$PWD"
evidence_dir=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-11-diagnose-vpsadmin-api-exception
cd servers/ruby
BUNDLE_GEMFILE="$PWD/Gemfile" bundle exec rspec
cd "$repo_root"
fixture_dir="$(mktemp -d -t haveapi-clean-package.XXXXXXXX)"
trap 'rm -rf -- "$fixture_dir"' EXIT
git archive HEAD | tar -x -C "$fixture_dir"
cd "$fixture_dir"
git init --quiet
git add .
cd servers/ruby
export BUNDLE_GEMFILE="$PWD/Gemfile"
bundle install --local
if bundle exec rake build > "$evidence_dir/clean-build-rejection.log" 2>&1; then
  echo 'A clean server build unexpectedly succeeded without shared documentation' >&2
  exit 1
fi
rg --quiet 'Missing or empty shared documentation:.*json-schema.html' "$evidence_dir/clean-build-rejection.log"
rg --quiet 'Run `make doc`' "$evidence_dir/clean-build-rejection.log"
cd ../..
make --dry-run release > "$evidence_dir/release-dry-run.log"
IFS= read -r first_command < "$evidence_dir/release-dry-run.log"
test "$first_command" = './utils/copydoc.sh servers/*'
make doc
cd servers/ruby
bundle exec rspec spec/packaging_spec.rb
VERIFY
