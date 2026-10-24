#!/usr/bin/env bash
set -euo pipefail
# Read-only utility entry, separate from the parent-only activation driver.
cd /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements
unset DEBUG PWDEBUG NODE_DEBUG
export NODE_PATH=/nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1/lib/node_modules
export PLAYWRIGHT_BROWSERS_PATH=/nix/store/f0rap655j6wmqbfvqdw445kwcxkxwf7n-playwright-browsers
exec timeout 180 /nix/store/l07gdbxylzfl8pbx9pxy6fyg95w4hjwy-nodejs-24.19.0/bin/node /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/followup-activation-d617/continuity.cjs "$@"
