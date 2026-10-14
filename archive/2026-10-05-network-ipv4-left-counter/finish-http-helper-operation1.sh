#!/usr/bin/env bash
set -euo pipefail
TRACK=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
V=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin
cd "$V"
for suffix in log exit head; do test ! -e "$TRACK/finish-http-helper-operation1.$suffix"; done
set +e
(
 set -euo pipefail
 test "$(git rev-parse HEAD)" = 7e86ee211d898256bd93cac7221c256636f3fcc3
 test "$(git branch --show-current)" = 2026-10-05-network-ipv4-left-counter
 test -z "$(git diff --cached --name-only)"
 sha256sum --check "$TRACK/finish-http-helper-inclusion-source1.sha256"
 sha256sum --check "$TRACK/finish-http-helper-inclusion-source1.source.sha256"
 git diff --binary --full-index > "$TRACK/finish-http-helper-operation1.initial.diff"
 cmp "$TRACK/finish-http-helper-inclusion-source1.diff" "$TRACK/finish-http-helper-operation1.initial.diff"
 git fetch origin master
 test "$(git rev-parse origin/master)" = 6c706c285681f1bc356cdc2569f5bd53817c6326
 test "$(git ls-remote origin refs/heads/2026-10-05-network-ipv4-left-counter | cut -f1)" = 7e86ee211d898256bd93cac7221c256636f3fcc3
 test -z "$(git for-each-ref --format='%(refname)' refs/heads/preserve/finish-http-v7e)"
 git branch preserve/finish-http-v7e 7e86ee211d898256bd93cac7221c256636f3fcc3
 unset RUBYOPT RUBYLIB GEM_HOME GEM_PATH BUNDLE_GEMFILE BUNDLE_BIN_PATH BUNDLER_VERSION OVERCOMMIT_DISABLE OVERCOMMIT_DISABLED
 nix develop .#vpsadmin --command bash -ec '
  test -x "$(git rev-parse --git-path hooks)/pre-commit"
  test -x "$(git rev-parse --git-path hooks)/commit-msg"
  mapfile -t paths < /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/finish-http-helper-inclusion-source1.paths
  git add -- "${paths[@]}"
  git diff --cached --binary --full-index > /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/finish-http-helper-operation1.staged.diff
  cmp /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/finish-http-helper-operation1.initial.diff /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/finish-http-helper-operation1.staged.diff
  git commit -F /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/finish-http-helper-operation1.message
  git rev-parse HEAD > /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/finish-http-helper-operation1.fixup
  git rev-parse HEAD^{tree} > /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/finish-http-helper-operation1.tree
  GIT_SEQUENCE_EDITOR=true git -c rebase.autoStash=false -c rebase.updateRefs=false rebase -i --autosquash 6c706c285681f1bc356cdc2569f5bd53817c6326
 '
 test -z "$(git status --porcelain)"
 test "$(git rev-list --count origin/master..HEAD)" = 4
 test "$(git rev-parse HEAD^{tree})" = "$(cat "$TRACK/finish-http-helper-operation1.tree")"
 sha256sum --check "$TRACK/finish-http-helper-inclusion-source1.source.sha256"
 git diff --exit-code 7e86ee211d898256bd93cac7221c256636f3fcc3 HEAD -- . ':!api/spec/api/resources/ip_address_spec.rb' ':!api/spec/api/resources/network_write_spec.rb' ':!api/spec/api/resources/vps_write_spec.rb'
 git diff 7e86ee211d898256bd93cac7221c256636f3fcc3 HEAD --binary --full-index > "$TRACK/finish-http-helper-operation1.final.diff"
 cmp "$TRACK/finish-http-helper-inclusion-source1.diff" "$TRACK/finish-http-helper-operation1.final.diff"
 git range-diff 6c706c285681f1bc356cdc2569f5bd53817c6326..7e86ee211d898256bd93cac7221c256636f3fcc3 6c706c285681f1bc356cdc2569f5bd53817c6326..HEAD > "$TRACK/finish-http-helper-operation1.range-diff"
 git log --reverse --format='%H %s' origin/master..HEAD > "$TRACK/finish-http-helper-operation1.history"
 git rev-parse HEAD > "$TRACK/finish-http-helper-operation1.head"
) > "$TRACK/finish-http-helper-operation1.log" 2>&1
result=$?
printf '%s\n' "$result" > "$TRACK/finish-http-helper-operation1.exit"
exit "$result"
