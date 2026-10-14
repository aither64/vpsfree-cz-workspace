#!/usr/bin/env bash
set -euo pipefail
T=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
W=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter
test ! -e "$T/finish-api-render9-publish-c.log"
test ! -e "$T/finish-api-render9-publish-c.exit"
set +e
(
  set -euo pipefail
  test "$(cat "$T/finish-api-render9-commit2.exit")" = 0
  VREV=$(cat "$T/finish-api-render9.head")
  cd "$W/vpsadmin"
  test "$(git rev-parse HEAD)" = "$VREV"
  test "$(git rev-parse HEAD~1)" = f778f762047bff3f4bd725fbb73882f65babdd65
  test -z "$(git status --porcelain)"
  unset RUBYOPT RUBYLIB GEM_HOME GEM_PATH BUNDLE_GEMFILE BUNDLE_BIN_PATH BUNDLER_VERSION OVERCOMMIT_DISABLE OVERCOMMIT_DISABLED
  nix develop .#vpsadmin --command git push origin HEAD:refs/heads/2026-10-05-network-ipv4-left-counter
  cd "$W/vpsfree-cz-configuration"
  test "$(git rev-parse HEAD)" = 961f5b61f608c60390caa7f76be0377ba389bb2d
  test -z "$(git status --porcelain)"
  test "$(git rev-parse origin/master)" = 1697613eab00a4bb0642b79c355c0b673b758a41
  git branch preserve/finish-api-render9-c961f5b61 HEAD
  export KB_RENDER_VREV="$VREV"
  nix develop --command bash -ec '
    git -c rebase.autoStash=false -c rebase.updateRefs=false rebase --onto 1697613eab00a4bb0642b79c355c0b673b758a41 961f5b61f608c60390caa7f76be0377ba389bb2d
    test "$(git rev-parse HEAD)" = 1697613eab00a4bb0642b79c355c0b673b758a41
    confctl inputs channel set --commit --no-editor vpsadmin vpsadmin "$KB_RENDER_VREV"
    confctl inputs channel set --commit --no-editor vpsadmin-webui vpsadmin-webui cce681424b866f6a51cbc0a1e4daa226ed33fc07
  '
  test -z "$(git status --porcelain)"
  test "$(git rev-parse HEAD~2)" = 1697613eab00a4bb0642b79c355c0b673b758a41
  test "$(git diff --name-only origin/master HEAD)" = flake.lock
  git rev-parse HEAD > "$T/finish-api-render9-c.head"
  nix develop --command git push --force-with-lease=refs/heads/2026-10-05-network-ipv4-left-counter:961f5b61f608c60390caa7f76be0377ba389bb2d origin HEAD:refs/heads/2026-10-05-network-ipv4-left-counter
) > "$T/finish-api-render9-publish-c.log" 2>&1
result=$?
printf '%s\n' "$result" > "$T/finish-api-render9-publish-c.exit"
exit "$result"
