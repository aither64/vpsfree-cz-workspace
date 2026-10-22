#!/usr/bin/env bash
set -uo pipefail
records=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-redesign-haveapi-github-releases
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-redesign-haveapi-github-releases/haveapi-release
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c python3 "$records/patch11-watch-ordinary-ci.py" 7fb218e28a86ab1d27de74ccb92c2a45063a4f78 v0.29.11 patch11 '["servers/ruby RSpec","clients/ruby RSpec","clients/go RSpec","clients/js tests","clients/php PHPUnit","i18n health","RuboCop"]' > "$records/patch11-ordinary-ci-watch.log" 2>&1
ordinary_result=$?
printf '%s\n' "$ordinary_result" > "$records/patch11-ordinary-ci-watch.status"
printf 'Ordinary tag checks completed: %s\n' "$ordinary_result"
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c python3 "$records/patch11-watch-tag.py" > "$records/patch11-tag-watch.log" 2>&1
tag_result=$?
printf '%s\n' "$tag_result" > "$records/patch11-tag-watch.status"
printf 'Tag release observer: %s\n' "$tag_result"
if [[ $ordinary_result -ne 0 || $tag_result -ne 0 ]]; then exit 1; fi
