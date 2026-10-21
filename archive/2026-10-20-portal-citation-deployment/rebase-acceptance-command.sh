#!/usr/bin/env bash
set -euo pipefail
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-portal-citation-investigation/dev-workspace
exec nix develop --command env \
  PLAYWRIGHT_MODULE=/nix/store/5cwkzbaxg65vbbnjvz05w8jm9m9kbam7-playwright-test-1.61.1/lib/node_modules/@playwright/test \
  CHROMIUM=/nix/store/789yhb4v2kq51jwl4acmmjvxs7mfrlhv-chromium-152.0.7977.75/bin/chromium \
  CITATION_RESULT=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-portal-citation-deployment/rebase-live-browser-result.json \
  node /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-portal-citation-deployment/verify-live-citations.cjs
