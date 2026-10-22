#!/usr/bin/env bash
set -euo pipefail
cd /home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-redesign-haveapi-github-releases
while [[ ! -f patch12-integrate-and-tag.status ]]; do sleep 2; done
push_result=$(cat patch12-integrate-and-tag.status)
if [[ "$push_result" != 0 ]]; then
  tail -n 60 patch12-integrate-and-tag.log
  exit "$push_result"
fi
bash patch12-watch-all.sh
