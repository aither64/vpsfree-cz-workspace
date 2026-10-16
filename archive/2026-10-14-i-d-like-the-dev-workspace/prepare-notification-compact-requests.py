#!/usr/bin/env python3
"""Seal preparation evidence after final checks/review; does not deploy."""
import hashlib
import json
from pathlib import Path
import subprocess
import uuid

TRACKING = Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace')
ROOT = Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-14-i-d-like-the-dev-workspace')
RUNTIME = '8cb1c0e545e1343d311f7cb9405eee83c468b4a6'


def read_json(name):
    return json.loads((TRACKING / name).read_text())


def reference(kind, name):
    path = TRACKING / name
    return {'kind': kind, 'path': str(path), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}


heads = read_json('notification-compact-final-heads.json')
assert heads['runtimeRevision'] == RUNTIME
for item in heads['repositories']:
    repo = ROOT / item['repository']
    git = lambda *args: subprocess.check_output(['git', '-C', str(repo), *args]).decode().strip()
    assert git('rev-parse', 'HEAD') == item['head']
    assert git('status', '--porcelain') == ''
    for name, digest in item['artifacts'].items():
        assert hashlib.sha256((TRACKING / name).read_bytes()).hexdigest() == digest

for name in ['notification-compact-8cb1c0e5-browser.status', 'notification-compact-8cb1c0e5-flake.status']:
    status = dict(line.split('=', 1) for line in (TRACKING / name).read_text().splitlines())
    assert status['revision'] == RUNTIME and status['exit_status'] == '0'
ci = read_json('notification-compact-8cb1c0e5-ci-result.json')
assert ci['headSha'] == RUNTIME and ci['conclusion'] == 'success' and ci['status'] == 'completed'
verification = read_json('verification-notification-compact.json')
assert verification['runtimeRevision'] == RUNTIME and verification['applicableAutomatedChecks'] == 'PASS'

review_names = [
    'notification-compact-source-gate.json',
    'notification-compact-review.md',
    'notification-compact-review-dispositions.md',
]
chain = {'schema': 1, 'runtimeRevision': RUNTIME, 'reviews': [reference('review', name) for name in review_names]}
with (TRACKING / 'notification-compact-review-chain.json').open('x') as file:
    json.dump(chain, file, indent=2)
    file.write('\n')
evidence = [reference('review', name) for name in [
    'notification-compact-review-chain.json', 'notification-compact-composition-review.md', 'notification-compact-final-heads.json',
]] + [reference('verification', 'verification-notification-compact.json')]
for prefix, kind in [('machine', 'machine_activate'), ('profile', 'profile_activate')]:
    request = {'schema': 1, 'requestId': str(uuid.uuid4()), 'kind': kind, 'evidence': evidence}
    if prefix == 'machine':
        request['target'] = 'aitherdev'
    with (TRACKING / f'{prefix}-prepare-notification-compact-request.json').open('x') as file:
        json.dump(request, file, indent=2)
        file.write('\n')
print('Exact checked preparation requests sealed; no coordinator operation performed.')
