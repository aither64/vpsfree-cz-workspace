#!/usr/bin/env bash
set -euo pipefail
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-portal-citation-deployment/workspace
exec nix build --out-link /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-portal-citation-deployment/final-app-root --print-out-paths .#default
