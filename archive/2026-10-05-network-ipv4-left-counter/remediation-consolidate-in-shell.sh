#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
[[ ${DEV_SESSION_SLUG-} == 2026-10-05-network-ipv4-left-counter && ${DEV_SESSION_WORKSPACE-} == /home/aither/workspace/ai/vpsfree.cz ]]
mode=${1:?Missing source}
case "$mode" in
  v)
    repo=vpsadmin
    branch=2026-10-05-network-ipv4-left-counter
    base=c4d9b50f4e74417ed37b5fe410cca3ec1addc24e
    old=6b3628af665049dc095ba985ef0fbe8a22286863
    expected=$(cat "$tracking/remediation-fixup-v-webui.sha")
    before_count=4
    after_count=2
    ;;
  w)
    repo=vpsadmin-webui
    branch=dev/network-enabled
    base=02ac0c7de1a588dbb14a18e652fe3f7e9b45cc51
    old=811742f50cce2b7724784d0a674c8d4d5dcb6273
    expected=$(cat "$tracking/remediation-fixup-w.sha")
    before_count=2
    after_count=1
    ;;
  *) exit 2 ;;
esac
[[ $(pwd -P) == "/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/$repo" ]]
[[ $(git branch --show-current) == "$branch" ]]
[[ $(git rev-parse HEAD) == "$expected" ]]
[[ -z $(git status --porcelain) ]]
[[ $(git rev-list --count "$base..HEAD") == "$before_count" ]]
sha256sum --check "$tracking/remediation-source-freeze2.sha256"
sha256sum --check "$tracking/remediation-commit-freeze.sha256"
git log --format=fuller "$base..HEAD" >"$tracking/remediation-history-$mode-before.log"
git diff --binary "$base..HEAD" >"$tracking/remediation-tree-$mode-before.diff"
tree=$(git rev-parse 'HEAD^{tree}')
printf '%s\n' "$tree" >"$tracking/remediation-tree-$mode-before.sha"
GIT_SEQUENCE_EDITOR=true git -c rebase.autoStash=false rebase -i --autosquash "$base"
[[ $(git rev-parse 'HEAD^{tree}') == "$tree" ]]
[[ $(git rev-list --count "$base..HEAD") == "$after_count" ]]
[[ -z $(git status --porcelain) ]]
sha256sum --check "$tracking/remediation-source-freeze2.sha256"
if [[ $mode == v ]]; then
  git diff --exit-code "$old" HEAD -- api/db/migrate api/db/schema.rb
fi
git rev-parse HEAD >"$tracking/remediation-source-$mode.sha"
git log --format=fuller "$base..HEAD" >"$tracking/remediation-history-$mode-final.log"
git diff --binary "$base..HEAD" >"$tracking/remediation-tree-$mode-final.diff"
git range-diff "$base..$old" "$base..HEAD" >"$tracking/remediation-range-$mode.diff"
git show --format=fuller --stat HEAD
