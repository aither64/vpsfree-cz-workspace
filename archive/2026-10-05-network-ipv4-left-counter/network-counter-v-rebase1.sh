#!/usr/bin/env bash
set -euo pipefail
export PATH=/home/aither/.local/state/dev-workspaces/profile/bin:/home/aither/.nix-profile/bin:$PATH
TRACK=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin
for suffix in log exit; do test ! -e "$TRACK/network-counter-v-rebase1.$suffix"; done
set +e
(
 set -euo pipefail
 test "$(git rev-parse HEAD)" = 818cf3646baca7218d7b15e7ef2e6ca7dd984f59
 test "$(git rev-parse origin/master)" = 81f1f1aabdd18a042d276aa4be3ca32173ff14d0
 test -z "$(git status --porcelain)"
 git log --format=fuller c4d9b50..HEAD > "$TRACK/network-counter-v-pre-rebase.history"
 git diff --binary --full-index c4d9b50..HEAD > "$TRACK/network-counter-v-pre-rebase.diff"
 git merge-tree --write-tree HEAD origin/master > "$TRACK/network-counter-v-expected-rebase.tree"
 unset RUBYOPT RUBYLIB GEM_HOME GEM_PATH BUNDLE_GEMFILE BUNDLE_BIN_PATH BUNDLER_VERSION OVERCOMMIT_DISABLE OVERCOMMIT_DISABLED
 nix develop .#vpsadmin --command bash -ec '
  GIT_SEQUENCE_EDITOR=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/network-counter-v-sequence1.py git rebase -i --onto 81f1f1aabdd18a042d276aa4be3ca32173ff14d0 c4d9b50f4e74417ed37b5fe410cca3ec1addc24e
 '
 test "$(git rev-parse HEAD^{tree})" = "$(cat "$TRACK/network-counter-v-expected-rebase.tree")"
 sha256sum --check "$TRACK/network-counter-v-source1.sha256"
 test -z "$(git status --porcelain)"
 git rev-parse HEAD > "$TRACK/network-counter-v-final1.sha"
 git log --format=fuller origin/master..HEAD > "$TRACK/network-counter-v-final1.history"
 git diff --binary --full-index origin/master..HEAD > "$TRACK/network-counter-v-final1.diff"
 git range-diff c4d9b50..818cf3646 81f1f1aa..HEAD > "$TRACK/network-counter-v-final1.range-diff"
) > "$TRACK/network-counter-v-rebase1.log" 2>&1
result=$?
printf '%s\n' "$result" > "$TRACK/network-counter-v-rebase1.exit"
exit "$result"
