#!/usr/bin/env bash
set -euo pipefail
# PREPARED ONLY. PARENT launches; a utility may observe status, never this driver.
cd /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements
exec python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/automatic-release-policy/activation/activation-driver.py
