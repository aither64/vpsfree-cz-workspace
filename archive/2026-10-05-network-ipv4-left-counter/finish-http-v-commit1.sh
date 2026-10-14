#!/usr/bin/env bash
set -euo pipefail
TRACK=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
V=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin
cd "$V"
for suffix in log exit sha; do test ! -e "$TRACK/finish-http-v-commit1.$suffix"; done
set +e
(
  set -euo pipefail
  test "$(git rev-parse HEAD)" = 12a3cb677ee0482cad9f61fbb70a401283da82e6
  test "$(git branch --show-current)" = 2026-10-05-network-ipv4-left-counter
  git diff --cached --quiet
  sha256sum --check "$TRACK/finish-http-errors-source1.sha256"
  sha256sum --check "$TRACK/finish-http-errors-source1.controls.sha256"
  git show-ref --verify --quiet refs/heads/preserve/finish-http-v12 && exit 2
  git branch preserve/finish-http-v12 HEAD
  git diff --binary --full-index > "$TRACK/finish-http-v-owned.diff"
  git rev-parse HEAD^{tree} > "$TRACK/finish-http-v-old.tree"
  git log --reverse --format='%H %s' 81f1f1aabdd18a042d276aa4be3ca32173ff14d0..HEAD > "$TRACK/finish-http-v-old.history"
  git ls-tree -r HEAD api/db > "$TRACK/finish-http-v-old.db-blobs"
  git show --format= --binary --full-index HEAD~2 > "$TRACK/finish-http-v-old.php-patch"
  git show --format= --binary --full-index HEAD~1 > "$TRACK/finish-http-v-old.index-patch"
  git show --format= --binary --full-index HEAD > "$TRACK/finish-http-v-old.counter-patch"
  unset RUBYOPT RUBYLIB GEM_HOME GEM_PATH BUNDLE_GEMFILE BUNDLE_BIN_PATH BUNDLER_VERSION OVERCOMMIT_DISABLE OVERCOMMIT_DISABLED
  nix develop .#vpsadmin --command bash -ec '
    test -x "$(git rev-parse --git-path hooks)/pre-commit"
    test -x "$(git rev-parse --git-path hooks)/commit-msg"
    ruby -rovercommit -e "puts Overcommit::VERSION"
    mapfile -t paths < /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/finish-http-errors-source1.paths
    git add -- "${paths[@]}" docs/ip-locking.md
    git diff --cached --binary --full-index > /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/finish-http-v-staged.diff
    cmp /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/finish-http-v-owned.diff /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/finish-http-v-staged.diff
    git commit -F /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/finish-http-v-fixup.message
    git rev-parse HEAD > /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/finish-http-v-fixup.sha
    git rev-parse HEAD^{tree} > /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/finish-http-v-fixup.tree
  '
  test -z "$(git status --porcelain)"
  sha256sum --check "$TRACK/finish-http-errors-source1.sha256"
  test "$(git rev-parse origin/master)" = 6c706c285681f1bc356cdc2569f5bd53817c6326
  GIT_SEQUENCE_EDITOR=true git -c rebase.autoStash=false -c rebase.updateRefs=false rebase -i --autosquash --onto 6c706c285681f1bc356cdc2569f5bd53817c6326 81f1f1aabdd18a042d276aa4be3ca32173ff14d0
  test -z "$(git status --porcelain)"
  test "$(git rev-list --count origin/master..HEAD)" = 4
  git ls-tree -r HEAD api/db > "$TRACK/finish-http-v-final.db-blobs"
  cmp "$TRACK/finish-http-v-old.db-blobs" "$TRACK/finish-http-v-final.db-blobs"
  git show --format= --binary --full-index HEAD~2 > "$TRACK/finish-http-v-final.php-patch"
  git show --format= --binary --full-index HEAD~1 > "$TRACK/finish-http-v-final.index-patch"
  git show --format= --binary --full-index HEAD > "$TRACK/finish-http-v-final.counter-patch"
  cmp "$TRACK/finish-http-v-old.php-patch" "$TRACK/finish-http-v-final.php-patch"
  cmp "$TRACK/finish-http-v-old.index-patch" "$TRACK/finish-http-v-final.index-patch"
  cmp "$TRACK/finish-http-v-old.counter-patch" "$TRACK/finish-http-v-final.counter-patch"
  sha256sum --check "$TRACK/finish-http-errors-source1.sha256"
  git diff --exit-code "$(cat "$TRACK/finish-http-v-fixup.sha")" HEAD -- . ':!packages'
  git rev-parse HEAD > "$TRACK/finish-http-v-commit1.sha"
) > "$TRACK/finish-http-v-commit1.log" 2>&1
result=$?
printf '%s\n' "$result" > "$TRACK/finish-http-v-commit1.exit"
exit "$result"
