#!/usr/bin/env bash
set -euo pipefail
T=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
V=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin
cd "$V"
test ! -e "$T/finish-final-target-v-rebase8.log"
test ! -e "$T/finish-final-target-v-rebase8.exit"
set +e
(
  set -euo pipefail
  test "$(git rev-parse HEAD)" = 939159f27b5d627930281d5fac0c0aa9ba53bfc7
  test -z "$(git status --porcelain)"
  test "$(git branch --show-current)" = 2026-10-05-network-ipv4-left-counter
  test "$(git rev-parse origin/master)" = 7d911899d0d3d335546f6b3676b2eb46a291764d
  test "$(git rev-parse refs/tags/retained-network-capture-v939159f2)" = 939159f27b5d627930281d5fac0c0aa9ba53bfc7
  git ls-tree -r HEAD api/db > "$T/finish-final-target-v-rebase8-before-db.txt"
  unset RUBYOPT RUBYLIB GEM_HOME GEM_PATH BUNDLE_GEMFILE BUNDLE_BIN_PATH BUNDLER_VERSION OVERCOMMIT_DISABLE OVERCOMMIT_DISABLED
  nix develop .#vpsadmin --command bash -ec '
    overcommit --sign
    git push origin refs/tags/retained-network-capture-v939159f2
    test "$(git ls-remote origin refs/tags/retained-network-capture-v939159f2 | cut -f1)" = 939159f27b5d627930281d5fac0c0aa9ba53bfc7
    git -c rebase.autoStash=false -c rebase.updateRefs=false rebase --onto 7d911899d0d3d335546f6b3676b2eb46a291764d 8a50010f46ad134e132394f2159d031601c17778
  '
  test -z "$(git status --porcelain)"
  test "$(git rev-list --count origin/master..HEAD)" = 4
  git ls-tree -r HEAD api/db > "$T/finish-final-target-v-rebase8-after-db.txt"
  cmp "$T/finish-final-target-v-rebase8-before-db.txt" "$T/finish-final-target-v-rebase8-after-db.txt"
  git range-diff --no-color 8a50010f46ad134e132394f2159d031601c17778..939159f27b5d627930281d5fac0c0aa9ba53bfc7 origin/master..HEAD > "$T/finish-final-target-v-rebase8.range-diff"
  git rev-parse HEAD > "$T/finish-final-target-v-rebase8.head"
) > "$T/finish-final-target-v-rebase8.log" 2>&1
result=$?
printf '%s\n' "$result" > "$T/finish-final-target-v-rebase8.exit"
exit "$result"
