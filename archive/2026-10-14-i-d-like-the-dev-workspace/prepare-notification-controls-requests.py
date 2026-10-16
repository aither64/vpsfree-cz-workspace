#!/usr/bin/env python3
"""Seal preparation evidence after final checks/review; does not deploy."""
import hashlib
import json
from pathlib import Path
import subprocess
import uuid

TRACKING = Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace')
ROOT = Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-14-i-d-like-the-dev-workspace')
RUNTIME = '1038d4abdde8b115c21b5940b14be637cfa967b6'


def read_json(name):
    return json.loads((TRACKING / name).read_text())


def reference(kind, name):
    path = TRACKING / name
    return {'kind': kind, 'path': str(path), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}


heads = read_json('notification-controls-final-heads.json')
assert heads['runtimeRevision'] == RUNTIME
for item in heads['repositories']:
    repo = ROOT / item['repository']
    git = lambda *args: subprocess.check_output(['git', '-C', str(repo), *args]).decode().strip()
    assert git('rev-parse', 'HEAD') == item['head']
    assert git('status', '--porcelain') == ''
    for name, digest in item['artifacts'].items():
        assert hashlib.sha256((TRACKING / name).read_bytes()).hexdigest() == digest

for name in ['notification-controls-1038-browser.status', 'notification-controls-1038-flake.status']:
    status = dict(line.split('=', 1) for line in (TRACKING / name).read_text().splitlines())
    assert status['revision'] == RUNTIME and status['exit_status'] == '0'
ci = read_json('notification-controls-1038-ci-result.json')
assert ci['headSha'] == RUNTIME and ci['conclusion'] == 'success' and ci['status'] == 'completed'
verification = read_json('verification-notification-controls.json')
assert verification['runtimeRevision'] == RUNTIME and verification['applicableAutomatedChecks'] == 'PASS'

review_names = [
    'notification-controls-1038-source-gate.json',
    'notification-controls-native-read-review.md',
    'notification-controls-review-dispositions.md',
]
chain = {'schema': 1, 'runtimeRevision': RUNTIME, 'reviews': [reference('review', name) for name in review_names]}
with (TRACKING / 'notification-controls-review-chain.json').open('x') as file:
    json.dump(chain, file, indent=2)
    file.write('\n')
evidence = [reference('review', name) for name in [
    'notification-controls-review-chain.json', 'notification-controls-composition-review.md', 'notification-controls-final-heads.json',
]] + [reference('verification', 'verification-notification-controls.json')]
for prefix, kind in [('machine', 'machine_activate'), ('profile', 'profile_activate')]:
    request = {'schema': 1, 'requestId': str(uuid.uuid4()), 'kind': kind, 'evidence': evidence}
    if prefix == 'machine':
        request['target'] = 'aitherdev'
    with (TRACKING / f'{prefix}-prepare-notification-controls-request.json').open('x') as file:
        json.dump(request, file, indent=2)
        file.write('\n')
print('Exact checked preparation requests sealed; no coordinator operation performed.')
