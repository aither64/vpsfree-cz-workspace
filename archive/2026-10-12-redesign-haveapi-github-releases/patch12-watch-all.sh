#!/usr/bin/env bash
set -uo pipefail
records=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-redesign-haveapi-github-releases
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-redesign-haveapi-github-releases/haveapi-release
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c python3 "$records/patch12-watch-ordinary-ci.py" 355c2990a4bfd3940d3234cb2077ad0127f43551 v0.29.12 patch12 '["servers/ruby RSpec","clients/ruby RSpec","clients/go RSpec","clients/js tests","clients/php PHPUnit","i18n health","RuboCop"]' > "$records/patch12-ordinary-ci-watch.log" 2>&1
ordinary_result=$?
printf '%s\n' "$ordinary_result" > "$records/patch12-ordinary-ci-watch.status"
printf 'Ordinary tag checks completed: %s\n' "$ordinary_result"
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c python3 "$records/patch12-watch-tag.py" > "$records/patch12-tag-watch.log" 2>&1
tag_result=$?
printf '%s\n' "$tag_result" > "$records/patch12-tag-watch.status"
printf 'Tag release observer: %s\n' "$tag_result"
if [[ $ordinary_result -ne 0 || $tag_result -ne 0 ]]; then exit 1; fi
