#!/usr/bin/env bash
# Runs only after root inspects and normally commits the K candidate.
set -euo pipefail
set -o noclobber
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
worktrees=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter
prefix=legacy-network-client
branch=2026-10-05-network-ipv4-left-counter
[[ ${DEV_SESSION_SLUG-} == "$branch" && ${DEV_SESSION_WORKSPACE-} == /home/aither/workspace/ai/vpsfree.cz ]]
head=$(cat "$tracking/$prefix-source.sha")
[[ $head =~ ^[0-9a-f]{40}$ && $(cat "$tracking/$prefix-published-v.sha") == "$head" ]]
[[ $(git -C "$worktrees/vpsadmin" ls-remote --heads origin "refs/heads/$branch" | cut -f1) == "$head" ]]
for repo in vpsfree-cz-configuration vpsfree-kb-contracts; do
  if [[ $repo == vpsfree-cz-configuration ]]; then
    mode=config; old=b217e0f0a74b45fe2a95fcc79c2eb646f21248ce; base=6f6aff9029cd57e1a0f9201356f7fdc9f6480671; count=2
  else
    mode=kb; old=609fd8a0070235339a4ddb567d905e466776d6a8; base=873758fd6aec0c03f50a94600e0ceab97946f255; count=1
  fi
  repo_root="$worktrees/$repo"
  final=$(cat "$tracking/$prefix-$mode-final.sha")
  [[ $final =~ ^[0-9a-f]{40}$ && $(git -C "$repo_root" rev-parse HEAD) == "$final" && -z $(git -C "$repo_root" status --porcelain) ]]
  [[ $(git -C "$repo_root" branch --show-current) == "$branch" && $(git -C "$repo_root" remote get-url origin) == "git@github.com:vpsfreecz/$repo.git" ]]
  [[ $(git -C "$repo_root" rev-list --count "$base..$final") == "$count" ]]
  [[ $(git -C "$repo_root" rev-parse "HEAD~$count") == "$base" ]]
  [[ $(cat "$tracking/$prefix-$mode-old-remote.sha") == "$old" ]]
  [[ $(git -C "$repo_root" ls-remote --heads origin "refs/heads/$branch" | cut -f1) == "$old" ]]
  git -C "$repo_root" fetch --no-tags origin refs/heads/master:refs/remotes/origin/master "+refs/heads/$branch:refs/remotes/origin/$branch"
  [[ $(git -C "$repo_root" rev-parse origin/master) == "$base" && $(git -C "$repo_root" rev-parse "refs/remotes/origin/$branch") == "$old" ]]
  git -C "$repo_root" merge-base --is-ancestor origin/master "$final"
  if [[ $mode == config ]]; then
    python3 "$tracking/visibility-current-base-config-guard.py" "$repo_root" "$old" "$base" "$head"
  else
    # Root writes kb-final.sha only after inspecting this exact five-file
    # candidate and making its normal commit; no K commit is automated here.
    (cd "$repo_root" && sha256sum --check --status "$tracking/$prefix-kb-candidate.sha256")
    python3 "$tracking/fixture-final-pin-guards.py" kb "$repo_root" "$old" "$head" e4c49bcdc91b33b7f644a2f125231cb413cf4bf4
  fi
  git -C "$repo_root" push --force-with-lease="refs/heads/$branch:$old" origin "$final:refs/heads/$branch"
  [[ $(git -C "$repo_root" ls-remote --heads origin "refs/heads/$branch" | cut -f1) == "$final" ]]
  git -C "$repo_root" fetch --no-tags origin "+refs/heads/$branch:refs/remotes/origin/$branch"
  [[ $(git -C "$repo_root" rev-parse "refs/remotes/origin/$branch") == "$final" ]]
  printf '%s\n' "$final" >"$tracking/$prefix-$mode-published.sha"
done
