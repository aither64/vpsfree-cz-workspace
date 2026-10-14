#!/usr/bin/env bash
set -euo pipefail
TRACK=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
V=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin
cd "$V"
for suffix in log exit sha; do test ! -e "$TRACK/finish-http-v2-commit1.$suffix"; done
set +e
(
  set -euo pipefail
  test "$(git rev-parse HEAD)" = 12a3cb677ee0482cad9f61fbb70a401283da82e6
  test "$(git branch --show-current)" = 2026-10-05-network-ipv4-left-counter
  git diff --cached --binary --full-index > "$TRACK/finish-http-v2-initial-index.diff"
  cmp "$TRACK/finish-http-v-staged.diff" "$TRACK/finish-http-v2-initial-index.diff"
  sha256sum --check "$TRACK/finish-http-errors-source2.sha256"
  sha256sum --check "$TRACK/finish-http-errors-source2.controls.sha256"
  test "$(git rev-parse refs/heads/preserve/finish-http-v12)" = 12a3cb677ee0482cad9f61fbb70a401283da82e6
  git diff HEAD --binary --full-index > "$TRACK/finish-http-v2-owned.diff"
  cmp "$TRACK/finish-http-errors-source2.diff" "$TRACK/finish-http-v2-owned.diff"
  git rev-parse HEAD^{tree} > "$TRACK/finish-http-v2-old.tree"
  git log --reverse --format='%H %s' 81f1f1aabdd18a042d276aa4be3ca32173ff14d0..HEAD > "$TRACK/finish-http-v2-old.history"
  git ls-tree -r HEAD api/db > "$TRACK/finish-http-v2-old.db-blobs"
  git show --format= --binary --full-index HEAD~2 > "$TRACK/finish-http-v2-old.php-patch"
  git show --format= --binary --full-index HEAD~1 > "$TRACK/finish-http-v2-old.index-patch"
  git show --format= --binary --full-index HEAD > "$TRACK/finish-http-v2-old.counter-patch"
  unset RUBYOPT RUBYLIB GEM_HOME GEM_PATH BUNDLE_GEMFILE BUNDLE_BIN_PATH BUNDLER_VERSION OVERCOMMIT_DISABLE OVERCOMMIT_DISABLED
  nix develop .#vpsadmin --command bash -ec '
    test -x "$(git rev-parse --git-path hooks)/pre-commit"
    test -x "$(git rev-parse --git-path hooks)/commit-msg"
    ruby -rovercommit -e "puts Overcommit::VERSION"
    mapfile -t paths < /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/finish-http-errors-source2.paths
    git add -- "${paths[@]}"
    git diff --cached --binary --full-index > /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/finish-http-v2-staged.diff
    cmp /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/finish-http-v2-owned.diff /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/finish-http-v2-staged.diff
    git commit -F /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/finish-http-v2-fixup.message
    git rev-parse HEAD > /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/finish-http-v2-fixup.sha
    git rev-parse HEAD^{tree} > /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/finish-http-v2-fixup.tree
  '
  test -z "$(git status --porcelain)"
  sha256sum --check "$TRACK/finish-http-errors-source2.sha256"
  test "$(git rev-parse origin/master)" = 6c706c285681f1bc356cdc2569f5bd53817c6326
  GIT_SEQUENCE_EDITOR=true git -c rebase.autoStash=false -c rebase.updateRefs=false rebase -i --autosquash --onto 6c706c285681f1bc356cdc2569f5bd53817c6326 81f1f1aabdd18a042d276aa4be3ca32173ff14d0
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
) > "$TRACK/finish-http-v2-commit1.log" 2>&1
result=$?
printf '%s\n' "$result" > "$TRACK/finish-http-v2-commit1.exit"
exit "$result"
