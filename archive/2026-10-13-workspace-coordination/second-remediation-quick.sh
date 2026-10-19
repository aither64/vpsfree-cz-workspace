#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-13-workspace-coordination
nix develop --command bash "$tracking/remediation-quick.sh"
