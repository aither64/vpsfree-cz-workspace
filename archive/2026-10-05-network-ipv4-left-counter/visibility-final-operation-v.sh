#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
v_root=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin
branch=2026-10-05-network-ipv4-left-counter
old=be136b6c00f03b85b7a12cc57550b4a1394a94a7
base=c4d9b50f4e74417ed37b5fe410cca3ec1addc24e
[[ $(pwd -P) == "$v_root" ]]
[[ $(git branch --show-current) == "$branch" ]]
[[ $(git remote get-url origin) == git@github.com:vpsfreecz/vpsadmin.git ]]
[[ ${DEV_SESSION_SLUG-} == "$branch" && ${DEV_SESSION_WORKSPACE-} == /home/aither/workspace/ai/vpsfree.cz ]]
[[ $(cat "$tracking/visibility-quick2-ruby-syntax-lint.exit") == 0 ]]
for step in wrapper ruby-syntax-lint api-core api-full; do
  [[ $(cat "$tracking/visibility-quick4-$step.exit") == 0 ]]
done
for bypass in OVERCOMMIT_DISABLE OVERCOMMIT_DISABLED SKIP ONLY PRE_COMMIT_ALLOW_NO_CONFIG HUSKY; do
  [[ -z ${!bypass-} ]]
done
case "${1-}" in
  commit)
    [[ $(git rev-parse HEAD) == "$old" && $(git rev-list --count "$base..HEAD") == 2 ]]
    [[ ! -e "$tracking/visibility-source-v.sha" ]]
    sha256sum --check "$tracking/visibility-quick4.sha256"
    python3 "$tracking/visibility-guard.py"
    [[ $(git config --get overcommit.configuration.verifysignatures) == 1 ]]
    [[ $(git config --get overcommit.configuration.signature) =~ ^[0-9a-f]{64}$ ]]
    for hook in pre-commit commit-msg; do
      hook_path=$(git rev-parse --git-path "hooks/$hook")
      test -x "$hook_path"
      rg -q 'Overcommit hook integration' "$hook_path"
    done
    git add -- api/lib/vpsadmin/api/resources/network.rb api/lib/vpsadmin/api/resources/ip_address.rb \
      api/spec/api/resources/network_read_spec.rb api/spec/api/resources/ip_address_spec.rb \
      api/spec/api/resources/host_ip_address_spec.rb api/spec/api/resources/network_interface_spec.rb \
      api/spec/api/resources/ip_address_assignment_spec.rb docs/ip-locking.md
    git diff --cached --check
    git diff --cached --binary >"$tracking/visibility-v-staged.diff"
    cmp "$tracking/visibility-quick4.diff" "$tracking/visibility-v-staged.diff"
    git commit -F "$tracking/visibility-commit.message"
    [[ -z $(git status --porcelain) && $(git rev-parse HEAD^) == "$old" ]]
    [[ $(git rev-list --count "$base..HEAD") == 3 ]]
    git diff --exit-code "$old" HEAD -- api/db/schema.rb api/db/migrate
    sha256sum --check "$tracking/visibility-quick4.sha256"
    git rev-parse HEAD >"$tracking/visibility-source-v.sha"
    git log --reverse --format=fuller "$base..HEAD" >"$tracking/visibility-v-final-history.log"
    git diff --binary "$base..HEAD" >"$tracking/visibility-v-final.diff"
    ;;
  publish)
    head=${2:?Missing exact committed head}
    [[ $head =~ ^[0-9a-f]{40}$ && $(cat "$tracking/visibility-source-v.sha") == "$head" ]]
    [[ $(git rev-parse HEAD) == "$head" && $(git rev-parse HEAD^) == "$old" && -z $(git status --porcelain) ]]
    [[ ! -e "$tracking/visibility-published-v.sha" ]]
    [[ $(git ls-remote --heads origin "refs/heads/$branch" | cut -f1) == "$old" ]]
    git fetch --no-tags origin refs/heads/master:refs/remotes/origin/master \
      "+refs/heads/$branch:refs/remotes/origin/$branch"
    [[ $(git rev-parse "refs/remotes/origin/$branch") == "$old" ]]
    git merge-base --is-ancestor origin/master "$head"
    git log --oneline --left-right "origin/master...$head" >"$tracking/visibility-v-default-comparison.log"
    [[ $(git ls-remote --heads origin "refs/heads/$branch" | cut -f1) == "$old" ]]
    git push origin "$head:refs/heads/$branch"
    [[ $(git ls-remote --heads origin "refs/heads/$branch" | cut -f1) == "$head" ]]
    git fetch --no-tags origin "+refs/heads/$branch:refs/remotes/origin/$branch"
    [[ $(git rev-parse "refs/remotes/origin/$branch") == "$head" ]]
    printf '%s\n' "$head" >"$tracking/visibility-published-v.sha"
    ;;
  *) exit 2 ;;
esac
