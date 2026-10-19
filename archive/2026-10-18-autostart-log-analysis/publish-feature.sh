#!/usr/bin/env bash
set -euo pipefail

cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-18-autostart-log-analysis/vpsadminos
expected=60f9ed1c153a734880e002b63d6ab7ed5fe87d0e
base=d531fc90888e3eabf17889b0dff94c648866cea4
branch=2026-10-18-autostart-log-analysis

test "$(git rev-parse HEAD)" = "$expected"
test "$(git branch --show-current)" = "$branch"
test "$(git remote get-url origin)" = git@github.com:vpsfreecz/vpsadminos.git
git diff --quiet
git diff --cached --quiet

git fetch origin refs/heads/staging:refs/remotes/origin/staging
staging_head=$(git rev-parse refs/remotes/origin/staging)
if [ "$staging_head" != "$base" ]; then
  echo "Upstream staging advanced to $staging_head; lead must assess before publication." >&2
  git log --oneline "$base..$staging_head"
  exit 1
fi

# Keep the reviewed head immutable while its VM check is running. A normal
# feature-ref push cannot rewrite an unrelated remote branch or merge staging.
git push origin "$expected:refs/heads/$branch"
remote_head=$(git ls-remote --exit-code origin "refs/heads/$branch")
test "${remote_head%%[[:space:]]*}" = "$expected"
echo "PUBLISHED: $branch at $expected; upstream staging remains $base."
