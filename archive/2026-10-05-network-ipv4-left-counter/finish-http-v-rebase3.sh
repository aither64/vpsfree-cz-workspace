#!/usr/bin/env bash
set -euo pipefail
TRACK=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
V=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin
cd "$V"
for suffix in log exit; do test ! -e "$TRACK/finish-http-v-rebase3.$suffix"; done
set +e
(
  set -euo pipefail
  test "$(git rev-parse HEAD)" = c2dd37f8c907400d0c37d7833f994cde305b7abf
  test -z "$(git status --porcelain)"
  sha256sum --check "$TRACK/finish-http-errors-source2.sha256"
  test "$(git rev-parse origin/master)" = 6c706c285681f1bc356cdc2569f5bd53817c6326
  unset RUBYOPT RUBYLIB GEM_HOME GEM_PATH BUNDLE_GEMFILE BUNDLE_BIN_PATH BUNDLER_VERSION OVERCOMMIT_DISABLE OVERCOMMIT_DISABLED
  nix develop .#vpsadmin --command bash -ec '
    GIT_SEQUENCE_EDITOR=true git -c rebase.autoStash=false -c rebase.updateRefs=false rebase -i --autosquash --onto 6c706c285681f1bc356cdc2569f5bd53817c6326 81f1f1aabdd18a042d276aa4be3ca32173ff14d0
  '

  test -z "$(git status --porcelain)"
  test "$(git rev-list --count origin/master..HEAD)" = 4
  git ls-tree -r HEAD api/db > "$TRACK/finish-http-v2-final.db-blobs"
  cmp "$TRACK/finish-http-v2-old.db-blobs" "$TRACK/finish-http-v2-final.db-blobs"
  git show --format= --binary --full-index HEAD~2 > "$TRACK/finish-http-v2-final.php-patch"
  git show --format= --binary --full-index HEAD~1 > "$TRACK/finish-http-v2-final.index-patch"
  git show --format= --binary --full-index HEAD > "$TRACK/finish-http-v2-final.counter-patch"
  cmp "$TRACK/finish-http-v2-old.php-patch" "$TRACK/finish-http-v2-final.php-patch"
  cmp "$TRACK/finish-http-v2-old.index-patch" "$TRACK/finish-http-v2-final.index-patch"
  cmp "$TRACK/finish-http-v2-old.counter-patch" "$TRACK/finish-http-v2-final.counter-patch"
  sha256sum --check "$TRACK/finish-http-errors-source2.sha256"
  git diff --exit-code "$(cat "$TRACK/finish-http-v2-fixup.sha")" HEAD -- . ':!packages'
  git rev-parse HEAD > "$TRACK/finish-http-v2-commit1.sha"
) > "$TRACK/finish-http-v-rebase3.log" 2>&1
result=$?
printf '%s\n' "$result" > "$TRACK/finish-http-v-rebase3.exit"
exit "$result"
