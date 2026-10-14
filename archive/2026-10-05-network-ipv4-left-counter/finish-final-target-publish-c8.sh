#!/usr/bin/env bash
set -euo pipefail
T=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
W=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter
test ! -e "$T/finish-final-target-publish-c8.log"
test ! -e "$T/finish-final-target-publish-c8.exit"
set +e
(
  set -euo pipefail
  unset RUBYOPT RUBYLIB GEM_HOME GEM_PATH BUNDLE_GEMFILE BUNDLE_BIN_PATH BUNDLER_VERSION OVERCOMMIT_DISABLE OVERCOMMIT_DISABLED
  cd "$W/vpsadmin"
  test "$(git rev-parse HEAD)" = f778f762047bff3f4bd725fbb73882f65babdd65
  test -z "$(git status --porcelain)"
  nix develop .#vpsadmin --command git push --force-with-lease=refs/heads/2026-10-05-network-ipv4-left-counter:939159f27b5d627930281d5fac0c0aa9ba53bfc7 origin HEAD:refs/heads/2026-10-05-network-ipv4-left-counter
  cd "$W/dev-workspace"
  test "$(git rev-parse HEAD)" = 16d949b39e162870cc21a6f23d2d138b2e642887
  test -z "$(git status --porcelain)"
  git push --force-with-lease=refs/heads/2026-10-05-network-ipv4-left-counter:0a422d1fa9fb2077932a8062ee1d948c9f4f2177 origin HEAD:refs/heads/2026-10-05-network-ipv4-left-counter
  cd "$W/vpsfree-cz-configuration"
  test "$(git rev-parse HEAD)" = 4caeeb1a363e00d93b3c6e5e6b3335e64d3e4532
  test -z "$(git status --porcelain)"
  test "$(git rev-parse origin/master)" = 1697613eab00a4bb0642b79c355c0b673b758a41
  git branch preserve/finish-final-target-c4caeeb1 HEAD
  nix develop --command bash -ec '
    overcommit --sign
    git -c rebase.autoStash=false -c rebase.updateRefs=false rebase --onto 1697613eab00a4bb0642b79c355c0b673b758a41 4caeeb1a363e00d93b3c6e5e6b3335e64d3e4532
    test "$(git rev-parse HEAD)" = 1697613eab00a4bb0642b79c355c0b673b758a41
    confctl inputs channel set --commit --no-editor vpsadmin vpsadmin f778f762047bff3f4bd725fbb73882f65babdd65
    confctl inputs channel set --commit --no-editor vpsadmin-webui vpsadmin-webui cce681424b866f6a51cbc0a1e4daa226ed33fc07
  '
  test -z "$(git status --porcelain)"
  test "$(git rev-parse HEAD~2)" = 1697613eab00a4bb0642b79c355c0b673b758a41
  test "$(git diff --name-only origin/master HEAD)" = flake.lock
  git rev-parse HEAD > "$T/finish-final-target-c8.head"
) > "$T/finish-final-target-publish-c8.log" 2>&1
result=$?
printf '%s\n' "$result" > "$T/finish-final-target-publish-c8.exit"
exit "$result"
