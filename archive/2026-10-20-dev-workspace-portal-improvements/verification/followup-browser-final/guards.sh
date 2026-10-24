#!/usr/bin/env bash
set -euo pipefail
umask 077
packet=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/followup-browser-final
python3 - <<'GUARDS'
import os,subprocess
from pathlib import Path
slug='2026-10-20-dev-workspace-portal-improvements'
workspace='/home/aither/workspace/ai/vpsfree.cz'
tracking=Path(workspace)/'work'/slug
identity=(os.environ.get('DEV_SESSION_SLUG'),os.environ.get('DEV_SESSION_WORKSPACE'))
if identity not in [(None,None),(slug,workspace)]:
    raise SystemExit('Session markers conflict with the trusted binding')
if subprocess.check_output(['dev-session','current'],cwd=tracking,text=True).strip()!=slug:
    raise SystemExit('Current session does not match the trusted binding')
root=Path(workspace)/'worktrees'/slug
heads={'codex-web': '6e32a9043ee6367d92bfaf8d3ebdf48036e275f9', 'dev-workspace': 'd617ef3968280e9955da85e2d7464a47030e7087', 'workspace': '48215f8c24f29358af338ac153d4ece88e1f4da2', 'vpsfree-cz-configuration': '9ab2909175b7248b5800237edd016b523d10d011'}
for name,head in heads.items():
    if subprocess.check_output(['git','-C',str(root/name),'rev-parse','HEAD'],text=True).strip()!=head:
        raise SystemExit('Exact source guard failed: '+name)
    if subprocess.check_output(['git','-C',str(root/name),'status','--porcelain']):
        raise SystemExit('Clean source guard failed: '+name)
print('Exact bound session and clean final A/B/C/config source guards pass')
GUARDS
