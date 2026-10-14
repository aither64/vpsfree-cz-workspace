#!/usr/bin/env bash
set -euo pipefail
export PATH=/home/aither/.local/state/dev-workspaces/profile/bin:/home/aither/.nix-profile/bin:$PATH
TRACK=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
C=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-cz-configuration
cd "$C"
for suffix in log exit; do test ! -e "$TRACK/network-counter-c-pin1.$suffix"; done
set +e
(
 set -euo pipefail
 test "$(git rev-parse HEAD)" = 072cee195d826baf78351bfc283786eb63d6dfae
 test "$(git rev-parse origin/master)" = 7e744b49ef90ba39d13b0f82a10a1f4c161c75f3
 test -z "$(git status --porcelain)"
 test "$(git rev-list --count origin/master..HEAD)" = 2
 test "$(git diff --name-only 6f6aff9029cd57e1a0f9201356f7fdc9f6480671..HEAD)" = flake.lock
 test "$(git ls-remote origin refs/heads/2026-10-05-network-ipv4-left-counter | cut -f1)" = 072cee195d826baf78351bfc283786eb63d6dfae
 git log --format=fuller 6f6aff90..HEAD > "$TRACK/network-counter-c-old.history"
 git diff --binary --full-index 6f6aff90..HEAD > "$TRACK/network-counter-c-old.diff"
 git rev-parse HEAD^{tree} > "$TRACK/network-counter-c-old.tree"
 unset RUBYOPT RUBYLIB GEM_HOME GEM_PATH BUNDLE_GEMFILE BUNDLE_BIN_PATH BUNDLER_VERSION OVERCOMMIT_DISABLE OVERCOMMIT_DISABLED
 nix develop --command bash -ec '
   test -x "$(git rev-parse --git-path hooks)/pre-commit"
   test -x "$(git rev-parse --git-path hooks)/commit-msg"
   git -c rebase.autoStash=false rebase --onto origin/master HEAD
   confctl inputs channel set --commit --no-editor vpsadmin vpsadmin cc8e9e7e421a258a46279304c910f88e2ad33147
   confctl inputs channel set --commit --no-editor vpsadmin-webui vpsadmin-webui a9d0b5e9402faafef937894f50463da3c27e8935
 '
 test "$(git rev-parse HEAD~2)" = 7e744b49ef90ba39d13b0f82a10a1f4c161c75f3
 test -z "$(git status --porcelain)"
 test "$(git diff --name-only origin/master..HEAD)" = flake.lock
 python3 "$TRACK/fixture-final-pin-guards.py" config "$C" 7e744b49ef90ba39d13b0f82a10a1f4c161c75f3 cc8e9e7e421a258a46279304c910f88e2ad33147 a9d0b5e9402faafef937894f50463da3c27e8935
 git rev-parse HEAD > "$TRACK/network-counter-c-final1.sha"
 git log --format=fuller origin/master..HEAD > "$TRACK/network-counter-c-final1.history"
 git diff --binary --full-index origin/master..HEAD > "$TRACK/network-counter-c-final1.diff"
) > "$TRACK/network-counter-c-pin1.log" 2>&1
result=$?
printf '%s\n' "$result" > "$TRACK/network-counter-c-pin1.exit"
exit "$result"
