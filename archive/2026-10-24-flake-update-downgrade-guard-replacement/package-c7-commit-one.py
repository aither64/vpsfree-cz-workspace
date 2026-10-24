#!/usr/bin/env python3
"""Ordinary staged commits for the seven owned consumer worktrees only."""
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path('/home/aither/workspace/ai/vpsfree.cz')
SLUG = '2026-10-24-flake-update-downgrade-guard-replacement'
SESSION = ROOT / 'work' / SLUG
PROJECTS = {
    'haveapi': ['.github/workflows/update-nixpkgs.yml', 'doc/agent-instructions/development.md'],
    'terraform-provider-vpsadmin': ['.github/workflows/update-vpsadmin-flake.yml', 'README.md', 'tools/update-vpsadmin-flake-input.sh'],
    'vpsadminos': ['.github/workflows/flake-update.yml', 'README.md'],
    'vpsf-status': ['.github/workflows/update-dependencies.yml', 'README.md'],
    'vpsfree-irc-bot': ['.github/workflows/nixpkgs-update.yml', 'README.md', 'tools/update_nixpkgs_flake.sh'],
    'vpsfree-cz-configuration': ['.github/workflows/daily-update.yml'],
    'vpsadminos-org-configuration': ['.github/workflows/daily-update.yml'],
}
project = sys.argv[1]
paths = PROJECTS[project]
worktree = ROOT / 'worktrees' / SLUG / project
record_path = SESSION / ('package-c7-final-commit-' + project + '.json')
assert not record_path.exists(), record_path
start = next(p for p in json.loads((SESSION / 'package-c7-cache-start-inventory.json').read_text())['projects'] if p['project'] == project)


def git(*args):
    return subprocess.run(['git', '-C', str(worktree), *args], check=True, text=True, capture_output=True).stdout


assert git('rev-parse', 'HEAD').strip() == start['head']
assert git('branch', '--show-current').strip() == SLUG
assert git('diff', '--cached', '--name-only') == ''
assert set(git('diff', '--name-only').splitlines()) == set(paths)
assert git('diff', '--name-only', '--', 'flake.nix', 'flake.lock') == ''
git('diff', '--check')
if (worktree / '.overcommit.yml').exists() or (worktree / 'lefthook.yml').exists():
    hook = Path(git('rev-parse', '--git-path', 'hooks/pre-commit').strip())
    if not hook.is_absolute():
        hook = worktree / hook
    assert hook.exists(), 'declared pre-commit hook missing'
message = SESSION / ('package-c7-final-message-' + project + '.txt')
if project == 'vpsf-status':
    subject = 'fixup! Guard automated flake updates with commit ancestry checks'
    message = SESSION / 'package-c7-status-fixup-message.txt'
    message.write_text(subject + '\n\nReuse cached Git history and select the final shared guard for CI.\n')
git('add', '--', *paths)
expected_tree = git('write-tree').strip()
command = ['nix', 'develop', '--no-write-lock-file', '-c', 'git', 'commit']
if project != 'vpsf-status':
    command += ['--amend']
command += ['-F', str(message)]
result = subprocess.run(command, cwd=worktree, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
log = SESSION / ('package-c7-final-commit-' + project + '.log')
log.write_text(result.stdout)
record = {'project': project, 'old_head': start['head'], 'command': command, 'cwd': str(worktree),
          'exit': result.returncode, 'log': str(log), 'expected_tree': expected_tree,
          'head_after': git('rev-parse', 'HEAD').strip(), 'tree_after': git('rev-parse', 'HEAD^{tree}').strip(),
          'status_after': git('status', '--porcelain=v1'), 'temporary_status_fixup': project == 'vpsf-status'}
record_path.write_text(json.dumps(record, indent=2) + '\n')
print(result.stdout)
if result.returncode:
    raise SystemExit(result.returncode)
assert record['tree_after'] == expected_tree
assert record['status_after'] == '', record['status_after']
print(project, 'ordinary hooks/commit passed; clean tree', record['head_after'])
