#!/usr/bin/env bash
set -euo pipefail
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/dev-workspace
exec nix develop --no-update-lock-file -c bash -euc '
node --check portal/internal/web/optional_questions_browser_test.cjs
node --check portal/internal/web/recovery_display_browser_test.cjs
node --check portal/internal/web/usability_browser_test.cjs
git diff --check
'
