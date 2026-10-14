#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
repo=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin
branch=2026-10-05-network-ipv4-left-counter
old=d7d7fb66865fd1a5548a45a559f5c2be436bc470
[[ $(pwd -P) == "$repo" && $(git branch --show-current) == "$branch" ]]
[[ ${DEV_SESSION_SLUG-} == "$branch" && ${DEV_SESSION_WORKSPACE-} == /home/aither/workspace/ai/vpsfree.cz ]]
[[ $(git remote get-url origin) == git@github.com:vpsfreecz/vpsadmin.git ]]
for step in wrapper ruby-syntax-lint api-core api-full; do
  [[ $(cat "$tracking/visibility-review-fix-quick1-$step.exit") == 0 ]]
done
for bypass in OVERCOMMIT_DISABLE OVERCOMMIT_DISABLED SKIP ONLY PRE_COMMIT_ALLOW_NO_CONFIG HUSKY; do [[ -z ${!bypass-} ]]; done
[[ $(git config --get overcommit.configuration.verifysignatures) == 1 ]]
[[ $(git config --get overcommit.configuration.signature) =~ ^[0-9a-f]{64}$ ]]
for hook in pre-commit commit-msg pre-push; do
  hook_path=$(git rev-parse --git-path "hooks/$hook")
  test -x "$hook_path"
  rg -q 'Overcommit hook integration' "$hook_path"
done
case "${1-}" in
  amend)
    [[ $(git rev-parse HEAD) == "$old" ]]
    [[ $(git status --porcelain) == ' M api/spec/api/resources/network_write_spec.rb' ]]
    [[ ! -e "$tracking/visibility-review-fixed-v.sha" ]]
    sha256sum --check "$tracking/visibility-review-fix-quick1.sha256"
    git add -- api/spec/api/resources/network_write_spec.rb
    git diff --cached --check
    git diff --cached --binary >"$tracking/visibility-review-fix-staged.diff"
    cmp "$tracking/visibility-review-fix.diff" "$tracking/visibility-review-fix-staged.diff"
    git commit --amend -F "$tracking/visibility-commit.message"
    [[ $(git rev-parse HEAD^) == be136b6c00f03b85b7a12cc57550b4a1394a94a7 && -z $(git status --porcelain) ]]
    git diff --binary "$old" HEAD >"$tracking/visibility-review-fix-committed.diff"
    cmp "$tracking/visibility-review-fix.diff" "$tracking/visibility-review-fix-committed.diff"
    git diff --exit-code "$old" HEAD -- api/db/schema.rb api/db/migrate
    git rev-parse HEAD >"$tracking/visibility-review-fixed-v.sha"
    git range-diff "$old^..$old" HEAD^..HEAD >"$tracking/visibility-review-fixed-v-range-diff.log"
    ;;
  publish)
    head=${2:?Missing amended exact head}
    [[ $head =~ ^[0-9a-f]{40}$ && $(cat "$tracking/visibility-review-fixed-v.sha") == "$head" ]]
    [[ $(git rev-parse HEAD) == "$head" && -z $(git status --porcelain) ]]
    [[ ! -e "$tracking/visibility-review-fixed-v-published.sha" ]]
    [[ $(git ls-remote --heads origin "refs/heads/$branch" | cut -f1) == "$old" ]]
    git fetch --no-tags origin refs/heads/master:refs/remotes/origin/master "+refs/heads/$branch:refs/remotes/origin/$branch"
    [[ $(git rev-parse "refs/remotes/origin/$branch") == "$old" ]]
    git merge-base --is-ancestor origin/master "$head"
    git push --force-with-lease="refs/heads/$branch:$old" origin "$head:refs/heads/$branch"
    [[ $(git ls-remote --heads origin "refs/heads/$branch" | cut -f1) == "$head" ]]
    git fetch --no-tags origin "+refs/heads/$branch:refs/remotes/origin/$branch"
    [[ $(git rev-parse "refs/remotes/origin/$branch") == "$head" ]]
    printf '%s\n' "$head" >"$tracking/visibility-review-fixed-v-published.sha"
    ;;
  *) exit 2 ;;
esac
