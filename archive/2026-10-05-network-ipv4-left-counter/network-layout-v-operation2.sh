#!/usr/bin/env bash
set -euo pipefail
export PATH=/home/aither/bin:/home/aither/.local/state/dev-workspaces/profile/bin:/home/aither/.nix-profile/bin:$PATH
TRACK=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
V=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin
cd "$V"
for suffix in log exit sha; do test ! -e "$TRACK/network-layout-v-operation2.$suffix"; done
set +e
(
 set -euo pipefail
 test "$(git rev-parse HEAD)" = cc8e9e7e421a258a46279304c910f88e2ad33147
 test "$(git branch --show-current)" = 2026-10-05-network-ipv4-left-counter
 git diff --cached --quiet
 sha256sum --check "$TRACK/php-network-alignment-source1.controls.sha256"
 sha256sum --check "$TRACK/php-network-alignment-source1.sha256"
 LC_ALL=C sort "$TRACK/php-network-alignment-source1.paths" > "$TRACK/network-layout-v-expected2.paths"
 git diff --name-only | LC_ALL=C sort > "$TRACK/network-layout-v-actual2.paths"
 cmp "$TRACK/network-layout-v-expected2.paths" "$TRACK/network-layout-v-actual2.paths"
 git fetch --no-tags origin +refs/heads/master:refs/remotes/origin/master
 test "$(git rev-parse origin/master)" = 81f1f1aabdd18a042d276aa4be3ca32173ff14d0
 git merge-base --is-ancestor origin/master HEAD
 test "$(git ls-remote origin refs/heads/2026-10-05-network-ipv4-left-counter | cut -f1)" = cc8e9e7e421a258a46279304c910f88e2ad33147
 unset RUBYOPT RUBYLIB GEM_HOME GEM_PATH BUNDLE_GEMFILE BUNDLE_BIN_PATH BUNDLER_VERSION OVERCOMMIT_DISABLE OVERCOMMIT_DISABLED
 nix develop .#vpsadmin --command bash -ec '
   test -x "$(git rev-parse --git-path hooks)/pre-commit"
   test -x "$(git rev-parse --git-path hooks)/commit-msg"
   ruby -rovercommit -e "puts Overcommit::VERSION"
   mapfile -t paths < /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/php-network-alignment-source1.paths
   git add -- "${paths[@]}"
   git diff --cached --name-only > /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/network-layout-v-staged2.paths
   cmp /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/network-layout-v-expected2.paths /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/network-layout-v-staged2.paths
   git commit -F /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/network-layout-v-fixup.message
   git rev-parse HEAD^{tree} > /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/network-layout-v-fixup.tree
   GIT_SEQUENCE_EDITOR=true git -c rebase.autoStash=false -c rebase.updateRefs=false rebase -i --autosquash 5b6700dc604c851be6b8fccd013897cc57aea5ce
 '
 test -z "$(git status --porcelain)"
 test "$(git rev-parse HEAD^{tree})" = "$(cat "$TRACK/network-layout-v-fixup.tree")"
 test "$(git rev-parse HEAD~3)" = 5b6700dc604c851be6b8fccd013897cc57aea5ce
 git log --reverse --format=%s origin/master..HEAD > "$TRACK/network-layout-v-final.subjects"
 cmp "$TRACK/network-layout-v-old.subjects" "$TRACK/network-layout-v-final.subjects"
 git show --format= --binary --full-index HEAD~1 > "$TRACK/network-layout-v-final.index-patch"
 git show --format= --binary --full-index HEAD > "$TRACK/network-layout-v-final.counter-patch"
 cmp "$TRACK/network-layout-v-old.index-patch" "$TRACK/network-layout-v-final.index-patch"
 cmp "$TRACK/network-layout-v-old.counter-patch" "$TRACK/network-layout-v-final.counter-patch"
 git ls-tree -r HEAD api docs plugins tests/suite flake.nix flake.lock webui/lang > "$TRACK/network-layout-v-final.protected-blobs"
 cmp "$TRACK/network-layout-v-old.protected-blobs" "$TRACK/network-layout-v-final.protected-blobs"
 sha256sum --check "$TRACK/php-network-alignment-source1.sha256"
 git rev-parse HEAD > "$TRACK/network-layout-v-operation2.sha"
 git log --format=fuller origin/master..HEAD > "$TRACK/network-layout-v-final.history"
 git diff --binary --full-index origin/master..HEAD > "$TRACK/network-layout-v-final.diff"
 test "$(git ls-remote origin refs/heads/master | cut -f1)" = 81f1f1aabdd18a042d276aa4be3ca32173ff14d0
 test "$(git ls-remote origin refs/heads/2026-10-05-network-ipv4-left-counter | cut -f1)" = cc8e9e7e421a258a46279304c910f88e2ad33147
 nix develop .#vpsadmin --command git push --force-with-lease=refs/heads/2026-10-05-network-ipv4-left-counter:cc8e9e7e421a258a46279304c910f88e2ad33147 origin HEAD:refs/heads/2026-10-05-network-ipv4-left-counter
 test "$(git ls-remote origin refs/heads/2026-10-05-network-ipv4-left-counter | cut -f1)" = "$(cat "$TRACK/network-layout-v-operation2.sha")"
 git fetch --no-tags origin +refs/heads/2026-10-05-network-ipv4-left-counter:refs/remotes/origin/2026-10-05-network-ipv4-left-counter
) > "$TRACK/network-layout-v-operation2.log" 2>&1
result=$?
printf '%s\n' "$result" > "$TRACK/network-layout-v-operation2.exit"
exit "$result"
