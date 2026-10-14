#!/usr/bin/env bash
set -euo pipefail
T=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
V=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin
test ! -e "$T/finish-api-fixture10-commit.log"
test ! -e "$T/finish-api-fixture10-commit.exit"
set +e
(
  set -euo pipefail
  cd "$V"
  test "$(git rev-parse HEAD)" = 59097cb4d67b732b0539f2db93a111013ee92555
  test "$(git branch --show-current)" = 2026-10-05-network-ipv4-left-counter
  test "$(git status --porcelain)" = ' M api/spec/support/network_export_dns_chain_spec_helpers.rb'
  test -z "$(git diff --cached --name-only)"
  test "$(sha256sum api/spec/support/network_export_dns_chain_spec_helpers.rb | cut -d ' ' -f1)" = 1d0e72cb7606006b88c0ef991aee8d470e610c37d23041cfe4c612c0dbd4e104
  git diff --binary --full-index > "$T/finish-api-fixture10-source.diff"
  unset RUBYOPT RUBYLIB GEM_HOME GEM_PATH BUNDLE_GEMFILE BUNDLE_BIN_PATH BUNDLER_VERSION OVERCOMMIT_DISABLE OVERCOMMIT_DISABLED
  nix develop .#vpsadmin --command bash -ec '
    test -x "$(git rev-parse --git-path hooks)/pre-commit"
    test -x "$(git rev-parse --git-path hooks)/commit-msg"
    git add -- api/spec/support/network_export_dns_chain_spec_helpers.rb
    git commit -F /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/finish-api-fixture10.message
  '
  test -z "$(git status --porcelain)"
  test "$(git diff --name-only HEAD~1 HEAD)" = api/spec/support/network_export_dns_chain_spec_helpers.rb
  test "$(git rev-parse HEAD~1)" = 59097cb4d67b732b0539f2db93a111013ee92555
  git rev-parse HEAD > "$T/finish-api-fixture10.head"
) > "$T/finish-api-fixture10-commit.log" 2>&1
result=$?
printf '%s\n' "$result" > "$T/finish-api-fixture10-commit.exit"
exit "$result"
