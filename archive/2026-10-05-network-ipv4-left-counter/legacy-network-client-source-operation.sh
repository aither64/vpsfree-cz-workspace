#!/usr/bin/env bash
# Prepared operation; root must inspect and select its mode before execution.
set -euo pipefail
set -o noclobber
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
repo=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin
prefix=legacy-network-client
branch=2026-10-05-network-ipv4-left-counter
base=c4d9b50f4e74417ed37b5fe410cca3ec1addc24e
api_commit=fc4f01a025e373ba5c85a7e78ea8b61ac1e1dc1f
legacy=be136b6c00f03b85b7a12cc57550b4a1394a94a7
old=cc3337d0a2699a8b28a0327bbee5ef62f3fbe166
[[ $(pwd -P) == "$repo" && $(git branch --show-current) == "$branch" ]]
[[ ${DEV_SESSION_SLUG-} == "$branch" && ${DEV_SESSION_WORKSPACE-} == /home/aither/workspace/ai/vpsfree.cz ]]
[[ $(git remote get-url origin) == git@github.com:vpsfreecz/vpsadmin.git ]]
for step in wrapper formatter syntax phpunit locales; do
  [[ $(cat "$tracking/$prefix-quick4-$step.exit") == 0 ]]
done
sha256sum --check --status "$tracking/$prefix-operation.sha256"
sha256sum --check --status "$tracking/$prefix-quick4.sha256"
for bypass in OVERCOMMIT_DISABLE OVERCOMMIT_DISABLED SKIP ONLY PRE_COMMIT_ALLOW_NO_CONFIG HUSKY; do [[ -z ${!bypass-} ]]; done
[[ -z $(git config --get core.hooksPath || true) ]]
[[ $(git config --get overcommit.configuration.verifysignatures) == 1 ]]
[[ $(git config --get overcommit.configuration.signature) =~ ^[0-9a-f]{64}$ ]]
for hook in pre-commit commit-msg pre-push; do
  hook_path=$(git rev-parse --git-path "hooks/$hook")
  test -x "$hook_path"
  rg -q 'Overcommit hook integration' "$hook_path"
done
case "${1-}" in
  consolidate)
    [[ $(git rev-parse HEAD) == "$old" && -z $(git diff --cached --name-only) ]]
    [[ $(git status --porcelain) == "$(cat "$tracking/$prefix-quick4.status")" ]]
    [[ $(git diff --name-only) == "$(cat "$tracking/$prefix-quick4.paths")" ]]
    [[ $(git rev-parse HEAD~2) == "$api_commit" && $(git rev-parse HEAD~1) == "$legacy" ]]
    [[ $(git rev-list --count "$base..HEAD") == 3 ]]
    [[ $(git ls-remote --heads origin "refs/heads/$branch" | cut -f1) == "$old" ]]
    git fetch --no-tags origin refs/heads/master:refs/remotes/origin/master "+refs/heads/$branch:refs/remotes/origin/$branch"
    [[ $(git rev-parse "refs/remotes/origin/$branch") == "$old" ]]
    git merge-base --is-ancestor origin/master "$api_commit"
    git diff --exit-code "$base" HEAD -- .overcommit.yml .git-hooks
    git diff --exit-code HEAD -- api docs tests webui/composer.json webui/composer.lock webui/lang
    git rev-parse "$old^{tree}" >"$tracking/$prefix-original-source-tree.sha"
    git log --reverse --format=fuller "$base..$old" >"$tracking/$prefix-original-source-history.log"
    git diff --binary "$base..$old" >"$tracking/$prefix-original-source.diff"
    printf '%s\n' "$old" >"$tracking/$prefix-old-v-remote.sha"
    git add --pathspec-from-file="$tracking/$prefix-quick4.paths"
    git diff --cached --check
    git diff --cached --binary >"$tracking/$prefix-fixup-staged.diff"
    cmp "$tracking/$prefix-quick4.diff" "$tracking/$prefix-fixup-staged.diff"
    git commit -F "$tracking/$prefix-fixup.message"
    [[ $(git rev-parse HEAD^) == "$old" && -z $(git status --porcelain) ]]
    git rev-parse HEAD >"$tracking/$prefix-fixup.sha"
    tree=$(git rev-parse 'HEAD^{tree}')
    printf '%s\n' "$tree" >"$tracking/$prefix-before-autosquash-tree.sha"
    git log --reverse --format=fuller "$base..HEAD" >"$tracking/$prefix-before-autosquash-history.log"
    GIT_SEQUENCE_EDITOR=true GIT_EDITOR=true git -c rebase.autoStash=false -c rebase.updateRefs=false rebase -i --autosquash "$api_commit"
    [[ $(git rev-parse 'HEAD^{tree}') == "$tree" && -z $(git status --porcelain) ]]
    [[ $(git rev-list --count "$base..HEAD") == 3 && $(git rev-parse HEAD~2) == "$api_commit" ]]
    git log --reverse --format=%s "$base..HEAD" >"$tracking/$prefix-final-subjects.txt"
    cmp "$tracking/$prefix-original-subjects.txt" "$tracking/$prefix-final-subjects.txt"
    git diff --binary HEAD~1 HEAD >"$tracking/$prefix-final-index.diff"
    cmp "$tracking/$prefix-original-index.diff" "$tracking/$prefix-final-index.diff"
    git diff --exit-code "$old" HEAD -- api docs tests webui/composer.json webui/composer.lock webui/lang
    git diff --binary "$old" HEAD >"$tracking/$prefix-consolidated-correction.diff"
    cmp "$tracking/$prefix-quick4.diff" "$tracking/$prefix-consolidated-correction.diff"
    sha256sum --check --status "$tracking/$prefix-quick4.sha256"
    git rev-parse HEAD >"$tracking/$prefix-source.sha"
    git log --reverse --format=fuller "$base..HEAD" >"$tracking/$prefix-final-source-history.log"
    git diff --binary "$base..HEAD" >"$tracking/$prefix-final-source.diff"
    git range-diff "$base..$old" "$base..HEAD" >"$tracking/$prefix-source-range.diff"
    ;;
  publish)
    head=$(cat "$tracking/$prefix-source.sha")
    [[ $head =~ ^[0-9a-f]{40}$ && $(git rev-parse HEAD) == "$head" && -z $(git status --porcelain) ]]
    [[ $(git rev-parse HEAD~2) == "$api_commit" && $(git rev-list --count "$base..HEAD") == 3 ]]
    [[ $(git rev-parse 'HEAD^{tree}') == "$(cat "$tracking/$prefix-before-autosquash-tree.sha")" ]]
    [[ $(git ls-remote --heads origin "refs/heads/$branch" | cut -f1) == "$old" ]]
    git fetch --no-tags origin refs/heads/master:refs/remotes/origin/master "+refs/heads/$branch:refs/remotes/origin/$branch"
    [[ $(git rev-parse "refs/remotes/origin/$branch") == "$old" ]]
    git merge-base --is-ancestor origin/master "$head"
    git push --force-with-lease="refs/heads/$branch:$old" origin "$head:refs/heads/$branch"
    [[ $(git ls-remote --heads origin "refs/heads/$branch" | cut -f1) == "$head" ]]
    git fetch --no-tags origin "+refs/heads/$branch:refs/remotes/origin/$branch"
    [[ $(git rev-parse "refs/remotes/origin/$branch") == "$head" ]]
    printf '%s\n' "$head" >"$tracking/$prefix-published-v.sha"
    ;;
  *) exit 2 ;;
esac
