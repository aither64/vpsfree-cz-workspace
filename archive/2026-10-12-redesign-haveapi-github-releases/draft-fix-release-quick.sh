#!/usr/bin/env bash
set -euo pipefail
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-redesign-haveapi-github-releases/haveapi-release
[[ $(git rev-parse HEAD) == 7fb218e28a86ab1d27de74ccb92c2a45063a4f78 ]]
[[ -z $(git status --porcelain) ]]
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c bash -euo pipefail -c '
  make release-check
  make release-test
  GITHUB_RUN_ID=123 make release-test
  bundle exec rubocop
  bash -n utils/release/build.sh
  python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-redesign-haveapi-github-releases/release-runtime-check.py
  git diff --check b27a031fa03d8d985a3abd2679ce2fc14fe53602..HEAD
'
