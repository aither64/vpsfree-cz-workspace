#!/usr/bin/env bash
set -euo pipefail
T=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
V=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin
test ! -e "$T/finish-api-render9-commit.log"
test ! -e "$T/finish-api-render9-commit.exit"
set +e
(
  set -euo pipefail
  cd "$V"
  test "$(git rev-parse HEAD)" = f778f762047bff3f4bd725fbb73882f65babdd65
  test "$(git branch --show-current)" = 2026-10-05-network-ipv4-left-counter
  test "$(git status --porcelain)" = ' M api/spec/models/ip_release_campaign_spec.rb'
  test -z "$(git diff --cached --name-only)"
  test "$(sha256sum api/spec/models/ip_release_campaign_spec.rb | cut -d ' ' -f1)" = 251d0a3815b26d22b4c8da66121395285f5bc6a58ca239b76f3239719ea299f2
  git diff --binary --full-index > "$T/finish-api-render9-source.diff"
  unset RUBYOPT RUBYLIB GEM_HOME GEM_PATH BUNDLE_GEMFILE BUNDLE_BIN_PATH BUNDLER_VERSION OVERCOMMIT_DISABLE OVERCOMMIT_DISABLED
  nix develop .#vpsadmin --command bash -ec '
    test -x "$(git rev-parse --git-path hooks)/pre-commit"
    test -x "$(git rev-parse --git-path hooks)/commit-msg"
    git add -- api/spec/models/ip_release_campaign_spec.rb
    git commit -F /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/finish-api-render9.message
  '
  test -z "$(git status --porcelain)"
  test "$(git diff --name-only HEAD~1 HEAD)" = api/spec/models/ip_release_campaign_spec.rb
  test "$(git rev-parse HEAD~1)" = f778f762047bff3f4bd725fbb73882f65babdd65
  git rev-parse HEAD > "$T/finish-api-render9.head"
) > "$T/finish-api-render9-commit.log" 2>&1
result=$?
printf '%s\n' "$result" > "$T/finish-api-render9-commit.exit"
exit "$result"
