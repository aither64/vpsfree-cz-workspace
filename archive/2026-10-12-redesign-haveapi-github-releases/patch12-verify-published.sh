#!/usr/bin/env bash
set -euo pipefail
records=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-redesign-haveapi-github-releases
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-redesign-haveapi-github-releases/haveapi-release
[[ $(git rev-parse HEAD) == 355c2990a4bfd3940d3234cb2077ad0127f43551 ]]
export GITHUB_RUN_ID=39313082898
export HAVEAPI_RELEASE_TOOLS_ONLY=1
nix develop -c ruby "$records/patch12-verify-destinations.rb" "$records"
nix develop -c python3 "$records/patch12-verify-public-bytes.py" "$records"
