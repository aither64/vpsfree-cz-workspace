#!/usr/bin/env bash
set -euo pipefail
source_dir=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-redesign-haveapi-github-releases/haveapi-release
target_dir=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-redesign-haveapi-github-releases/haveapi-release-target-0.29.11
records=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-redesign-haveapi-github-releases
expected=7fb218e28a86ab1d27de74ccb92c2a45063a4f78
base=b27a031fa03d8d985a3abd2679ce2fc14fe53602
cd "$source_dir"
[[ $(git rev-parse HEAD) == "$expected" ]]
[[ -z $(git status --porcelain) ]]
[[ ! -e "$target_dir" ]]
[[ $(git ls-remote origin refs/heads/haveapi-0.29 | cut -f1) == "$base" ]]
[[ -z $(git ls-remote origin refs/tags/v0.29.11) ]]
if git show-ref --verify --quiet refs/tags/v0.29.11; then
  printf 'Local v0.29.11 already exists; inspect before retrying\n' >&2
  exit 1
fi
export HAVEAPI_RELEASE_TOOLS_ONLY=1
nix develop -c bundle exec git worktree add --detach "$target_dir" refs/remotes/origin/haveapi-0.29
[[ $(git -C "$target_dir" rev-parse HEAD) == "$base" ]]
nix develop -c bundle exec git -C "$target_dir" merge --ff-only "$expected"
[[ $(git -C "$target_dir" rev-parse HEAD) == "$expected" ]]
nix develop -c bundle exec git -C "$target_dir" tag -a v0.29.11 "$expected" -F "$records/patch11-tag-message.txt"
nix develop -c bundle exec git -C "$target_dir" push --atomic origin HEAD:refs/heads/haveapi-0.29 refs/tags/v0.29.11
