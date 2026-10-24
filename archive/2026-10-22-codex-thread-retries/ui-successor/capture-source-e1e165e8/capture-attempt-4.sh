#!/usr/bin/env bash
set -euo pipefail
cd /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-codex-thread-retries
exec python3 ui-successor/capture-command.py \
  ui-successor/capture-attempt-4 \
  bash ui-successor/capture.sh
