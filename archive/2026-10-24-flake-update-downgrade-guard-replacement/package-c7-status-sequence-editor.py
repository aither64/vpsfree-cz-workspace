#!/usr/bin/env python3
"""Consolidate only this session's cache amendment into the status adoption."""
from pathlib import Path
import json
import shlex
import subprocess
import sys

ROOT = Path('/home/aither/workspace/ai/vpsfree.cz')
SLUG = '2026-10-24-flake-update-downgrade-guard-replacement'
WORKTREE = ROOT / 'worktrees' / SLUG / 'vpsf-status'
SESSION = ROOT / 'work' / SLUG
ADOPTION = 'ebb7e6a2252f5a7f61d06a5935bb4c88a6c1964e'
VENDOR = '6b5e8a6089926112bfbb63a45413b886ee56e549'
METRICS = 'd4c816bbf7ad22b9b2dcb424c1f316b1d0b6c6aa'
records = []
for line in Path(sys.argv[1]).read_text().splitlines():
    if not line or line.startswith('#'):
        continue
    kind, short, *message = line.split()
    assert kind == 'pick', line
    full = subprocess.run(['git', '-C', str(WORKTREE), 'rev-parse', short],
                          check=True, text=True, capture_output=True).stdout.strip()
    records.append((full, ' '.join(message)))
assert len(records) == 4, records
assert [x[0] for x in records[:3]] == [ADOPTION, VENDOR, METRICS], records
expected_fixup = json.loads((SESSION / 'package-c7-final-commit-vpsf-status.json').read_text())['head_after']
assert records[3][0] == expected_fixup, records
lines = [f'pick {ADOPTION}', f'fixup {records[3][0]}',
         'exec git commit --amend -F ' + shlex.quote(str(SESSION / 'package-c7-final-message-vpsf-status.txt')),
         f'pick {VENDOR}', f'pick {METRICS}']
Path(sys.argv[1]).write_text('\n'.join(lines) + '\n')
