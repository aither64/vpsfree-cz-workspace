#!/usr/bin/env bash
set -euo pipefail
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-redesign-haveapi-github-releases/haveapi
[[ $(git rev-parse HEAD) == c14e7d3158b91c134c2817b489cd29772fc09f82 ]]
nix develop -c bash -euo pipefail -c '
  make release-check
  make release-test
  GITHUB_RUN_ID=123 make release-test
  bundle exec rubocop
  bash -n utils/release/build.sh
  git diff --check origin/master...HEAD
'
