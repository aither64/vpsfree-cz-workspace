#!/usr/bin/env python3
"""Root-owned normal Git consolidation of the exact checked E input stream."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile

tracking = Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
repo = Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-dev-workspace')
base = '0ff827df13e82dfab4b536ff29979280f264e8f5'
first = 'ce970275e7209616a5ebc1a6d3f49c35e49a55c6'
old = 'd2079f605ae87871037ae73c5e5daf20a3e0d03d'
branch = '2026-10-05-network-ipv4-left-counter'
old_k = '93a16d6cecb6bc847ec9335a3f170eb8b301ab56'
new_k = '68aa33b451a14eb7bf4b2f1a090a8e5a2f80b52e'
prefix = 'kb-runtime-e-review-consolidated'

def run(*args, env=None):
    return subprocess.check_output(args, cwd=repo, env=env)

def git(*args, env=None):
    return run('git', *args, env=env)

def save(suffix, value):
    if isinstance(value, str):
        value = value.encode()
    with (tracking / f'{prefix}.{suffix}').open('xb') as output:
        output.write(value)

assert git('rev-parse', 'HEAD').decode().strip() == old
assert git('branch', '--show-current').decode().strip() == branch
assert git('remote', 'get-url', 'origin').decode().strip() == 'git@github.com:vpsfreecz/dev-workspace.git'
assert not git('diff', '--cached', '--binary')
assert git('status', '--porcelain=v1', '--untracked-files=all').decode().splitlines() == [' M flake.lock', ' M flake.nix']
assert git('rev-list', '--reverse', f'{base}..{old}').decode().splitlines() == [first, old]
for packet, steps in [('pin1', ['preflight', 'generate', 'graph', 'whitespace']), ('pair1', ['toolchain', 'syntax', 'sdk', 'composition'])]:
    assert (tracking / f'kb-runtime-e-review-{packet}.exit').read_text().strip() == '0'
    for step in steps:
        assert (tracking / f'kb-runtime-e-review-{packet}-{step}.exit').read_text().strip() == '0'
run('sha256sum', '--check', str(tracking / 'kb-runtime-e-review-pair1-source.sha256'))
run('sha256sum', '--check', str(tracking / 'kb-runtime-e-review-pair1-immutable.sha256'))
run('sha256sum', '--check', str(tracking / 'kb-runtime-e-review-pin1-generated.sha256'))
assert (repo / 'flake.lock').read_bytes() == (tracking / 'kb-runtime-e-review-pin1-generated.lock').read_bytes()
assert git('diff', '--binary', '--', 'flake.nix', 'flake.lock') == (tracking / 'kb-runtime-e-review-pin1-generated.diff').read_bytes()
git('diff', '--check')
tracked = git('ls-files').decode().splitlines()
framework_names = {'.overcommit.yml', '.pre-commit-config.yaml', 'lefthook.yml', 'lefthook.yaml', '.huskyrc', '.huskyrc.json'}
assert not [p for p in tracked if Path(p).name in framework_names or '/.husky/' in '/' + p]
hooks_config = subprocess.run(['git', 'config', '--get', 'core.hooksPath'], cwd=repo, capture_output=True)
assert hooks_config.returncode == 1 and not hooks_config.stdout
hooks = Path(git('rev-parse', '--git-path', 'hooks').decode().strip())
if not hooks.is_absolute():
    hooks = repo / hooks
assert not [p for p in hooks.iterdir() if p.is_file() and not p.name.endswith('.sample')]
git('fetch', 'origin', 'master')
assert git('rev-parse', 'origin/master').decode().strip() == base
git('merge-base', '--is-ancestor', base, old)
remote = git('ls-remote', '--heads', 'origin', f'refs/heads/{branch}')
assert remote in (b'', f'{old}\trefs/heads/{branch}\n'.encode()), remote
save('before.remote', remote)
save('old-history', git('log', '--reverse', '--format=fuller', f'{base}..{old}'))
save('old-full.diff', git('diff', '--binary', '--full-index', base, old))
save('input-correction.diff', git('diff', '--binary', '--full-index', '--', 'flake.nix', 'flake.lock'))
old_provider_message = git('show', '-s', '--format=%B', old)
old_input_message = git('show', '-s', '--format=%B', first)
with tempfile.TemporaryDirectory(prefix='kb-e-consolidate-index-', dir=tracking) as scratch:
    env = os.environ.copy()
    env['GIT_INDEX_FILE'] = str(Path(scratch) / 'index')
    git('read-tree', old, env=env)
    git('add', '--', 'flake.nix', 'flake.lock', env=env)
    expected = git('write-tree', env=env).decode().strip()
save('expected.tree', expected + '\n')
message = tracking / 'kb-runtime-e-review-fixup.message'
message_bytes = b'fixup! flake: pin portable KB and streaming workspace runtimes\n\nSelect the corrected portable KB runtime while preserving its dependency\ngraph and the existing generic dispatcher and provider behavior.\n'
with message.open('xb') as output:
    output.write(message_bytes)
assert max(map(len, message_bytes.decode().splitlines())) <= 80
git('add', '--', 'flake.nix', 'flake.lock')
assert git('diff', '--cached', '--name-only').decode().splitlines() == ['flake.lock', 'flake.nix']
assert git('write-tree').decode().strip() == expected
git('diff', '--cached', '--check')
git('commit', '-F', str(message))
env = os.environ.copy()
env['GIT_SEQUENCE_EDITOR'] = 'true'
git('-c', 'rebase.updateRefs=false', 'rebase', '-i', '--autosquash', base, env=env)
head = git('rev-parse', 'HEAD').decode().strip()
commits = git('rev-list', '--reverse', f'{base}..{head}').decode().splitlines()
assert len(commits) == 2 and commits[-1] == head
assert not git('rev-list', '--merges', f'{base}..{head}')
assert git('rev-parse', 'HEAD^{tree}').decode().strip() == expected
assert not git('status', '--porcelain=v1', '--untracked-files=all')
assert git('show', '-s', '--format=%B', commits[0]) == old_input_message
assert git('show', '-s', '--format=%B', head) == old_provider_message
assert git('diff', '--name-only', old, head).decode().splitlines() == ['flake.lock', 'flake.nix']
# The rewritten first commit has only the requested input identity differences.
# Its flake body must remain the old input commit's body, not provider changes.
old_first_flake = git('show', f'{first}:flake.nix')
new_first_flake = git('show', f'{commits[0]}:flake.nix')
assert old_first_flake.count(old_k.encode()) == 1
assert new_first_flake == old_first_flake.replace(old_k.encode(), new_k.encode())
assert git('show', f'{commits[0]}:flake.lock') == (repo / 'flake.lock').read_bytes()
# Final equality to the pre-rebase expected tree proves provider content was retained.
save('head.sha', head + '\n')
save('history', git('log', '--reverse', '--format=fuller', f'{base}..{head}'))
save('full.diff', git('diff', '--binary', '--full-index', base, head))
save('correction.diff', git('diff', '--binary', '--full-index', old, head))
save('range-diff', git('range-diff', '--no-color', f'{base}..{old}', f'{base}..{head}'))
save('proof.json', json.dumps({'base': base, 'old_head': old, 'head': head, 'commits': commits, 'tree': expected, 'hook_context': 'no declared framework or custom hooks; normal hooks enabled', 'message_sha256': hashlib.sha256(message_bytes).hexdigest()}, indent=2) + '\n')
print('Consolidated exact checked E tree:', head, flush=True)
