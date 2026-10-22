#!/usr/bin/env bash
set -uo pipefail
records=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-redesign-haveapi-github-releases
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-redesign-haveapi-github-releases/haveapi-release
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c gh run watch 39313082898 --repo vpsfreecz/haveapi --exit-status --interval 15
watch_result=$?
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c gh run view 39313082898 --repo vpsfreecz/haveapi --json databaseId,headSha,headBranch,event,status,conclusion,jobs,url > "$records/patch12-publication-final.json"
metadata_result=$?
if [[ $watch_result -ne 0 ]]; then
  HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c gh run view 39313082898 --repo vpsfreecz/haveapi --log-failed > "$records/patch12-publication-failed.log" 2>&1
fi
if [[ $watch_result -ne 0 ]]; then exit "$watch_result"; fi
exit "$metadata_result"
