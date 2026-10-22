#!/usr/bin/env bash
set -euo pipefail
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-redesign-haveapi-github-releases/haveapi
[[ $(git rev-parse HEAD) == 526648131af45df68c25ac0042a52f22c7a81df5 ]]
[[ -z $(git status --porcelain) ]]
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c bash -euo pipefail -c '
  make release-check
  make release-test
  GITHUB_RUN_ID=123 make release-test
  bundle exec rubocop
  bash -n utils/release/build.sh
  test -z "$(git diff --name-only c14e7d3158b91c134c2817b489cd29772fc09f82..HEAD -- servers clients)"
  git diff --check c14e7d3158b91c134c2817b489cd29772fc09f82..HEAD
'
