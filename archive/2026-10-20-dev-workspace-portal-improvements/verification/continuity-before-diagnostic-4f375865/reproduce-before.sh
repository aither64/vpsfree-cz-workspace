#!/usr/bin/env bash
set -euo pipefail
umask 077
unset DEBUG PWDEBUG NODE_DEBUG
python3 - <<'CHECK'
import os,subprocess
slug,workspace=os.getenv('DEV_SESSION_SLUG'),os.getenv('DEV_SESSION_WORKSPACE')
assert (slug is None and workspace is None) or (slug=='2026-10-20-dev-workspace-portal-improvements' and workspace=='/home/aither/workspace/ai/vpsfree.cz')
assert subprocess.check_output(['dev-session','current'],text=True).strip()=='2026-10-20-dev-workspace-portal-improvements'
CHECK
export DEV_SESSION_SLUG=2026-10-20-dev-workspace-portal-improvements
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
export NODE_PATH=/nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1/lib/node_modules
export PLAYWRIGHT_BROWSERS_PATH=/nix/store/f0rap655j6wmqbfvqdw445kwcxkxwf7n-playwright-browsers
python3 - <<'PREPARE'
import fcntl,pathlib
root=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz')
with open(root/'.git/dev-session-tracking.lock','a') as f:
 fcntl.flock(f,fcntl.LOCK_EX|fcntl.LOCK_NB)
 pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/continuity-before-diagnostic-4f375865/attempts/before-reproduction-1').mkdir(parents=True,exist_ok=False,mode=0o700)
PREPARE
exec timeout 180 /nix/store/l07gdbxylzfl8pbx9pxy6fyg95w4hjwy-nodejs-24.19.0/bin/node /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/continuity-before-diagnostic-4f375865/continuity-diagnostic.cjs before /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/continuity-before-diagnostic-4f375865/attempts/before-reproduction-1
