#!/usr/bin/env bash
set -uo pipefail
cd /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter || exit 1
/nix/store/5a0h3d6488628sh6w1ccqk8dizvmp8ji-python3-3.13.15-env/bin/python3.13 finish-kb-scope12-hosted.py > finish-kb-scope12-hosted-collector.log 2>&1
code=$?
printf '%s\n' "$code" > finish-kb-scope12-hosted-collector.exit
exit "$code"
