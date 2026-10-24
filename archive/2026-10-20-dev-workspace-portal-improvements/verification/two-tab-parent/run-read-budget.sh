#!/usr/bin/env bash
set -euo pipefail
python3 - <<'GUARD'
import os,subprocess
from pathlib import Path
assert subprocess.check_output(['dev-session','current'],text=True).strip()=='2026-10-20-dev-workspace-portal-improvements'
a,b=os.getenv('DEV_SESSION_SLUG'),os.getenv('DEV_SESSION_WORKSPACE')
assert (a is None and b is None) or (a=='2026-10-20-dev-workspace-portal-improvements' and b=='/home/aither/workspace/ai/vpsfree.cz')
r=Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements')
for name,head in {'codex-web':'ea64ef57fdd2ff5fd60715b62f2d1696bc0133e5','dev-workspace':'bc40cdda2d28c9732396db4163daa244bba79acb'}.items():
 assert subprocess.check_output(['git','-C',str(r/name),'rev-parse','HEAD'],text=True).strip()==head
 assert not subprocess.check_output(['git','-C',str(r/name),'status','--porcelain'])
assert Path('/home/aither/bin/workspace-host').resolve()==Path('/nix/store/hzf9qda2ckjsv72b689bclc6p3v8ap9l-dev-workspace-0.2.0/bin/workspace-host')
GUARD
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/dev-workspace
test "$(git rev-parse HEAD)" = bc40cdda2d28c9732396db4163daa244bba79acb
test -z "$(git status --porcelain)"
test ! -e /tmp/portal-followup-absent-providers.json
export DEV_SESSION_SLUG=2026-10-20-dev-workspace-portal-improvements
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
export DEV_WORKSPACES_CODEX_PROVIDERS=/tmp/portal-followup-absent-providers.json
unset PORTAL_FIREFOX_TABS_TEST
export PORTAL_FIREFOX_READ_BUDGET_TEST=1
export FIREFOX_BINARY=/nix/store/nhqwiw8s88b3zy3pka98gizjgw6i2h8d-firefox-155.0/bin/firefox
export GECKODRIVER_BINARY=/nix/store/b5g0k5g2bsvar0y38mn4zdfailhk0b77-geckodriver-0.36.0/bin/geckodriver
xvfb_run=/nix/store/iyzy0zy23i1njxar2sd1hr4hmk56dalh-xvfb-run-1+g87f6705/bin/xvfb-run
test -x "$FIREFOX_BINARY"
test -x "$GECKODRIVER_BINARY"
test -x "$xvfb_run"
exec nix develop --no-update-lock-file -c "$xvfb_run" --auto-servernum \
 --server-args='-screen 0 1920x1080x24 -nolisten tcp' \
 go -C portal test -mod=readonly ./internal/web -run '^TestFirefoxReadBudget$' -count=1 -v
