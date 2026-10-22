#!/usr/bin/env bash
set -euo pipefail
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-redesign-haveapi-github-releases/haveapi-release
[[ $(git rev-parse HEAD) == b27a031* ]]
nix develop -c bash -euo pipefail -c '
  make release-check
  make release-test
  GITHUB_RUN_ID=123 make release-test
  bundle exec rubocop
  bash -n utils/release/build.sh
  python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-redesign-haveapi-github-releases/release-runtime-check.py
  git diff --check v0.29.9..HEAD
'
nix shell --inputs-from . nixpkgs#actionlint -c actionlint .github/workflows/release.yml
