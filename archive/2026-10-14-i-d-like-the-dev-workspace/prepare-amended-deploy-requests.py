#!/usr/bin/env python3
"""Seal final amended evidence for build/copy preparation, without activation."""
import hashlib
import json
from pathlib import Path
import subprocess
import uuid

record = Path(__file__).resolve().parent
heads = json.loads((record / 'amended-final-heads.json').read_text())
for name, source in heads.items():
    checkout = source['worktree']
    actual = subprocess.check_output(['git', '-C', checkout, 'rev-parse', 'HEAD'], text=True).strip()
    dirty = subprocess.check_output(['git', '-C', checkout, 'status', '--porcelain'], text=True).strip()
    if actual != source['head'] or dirty:
        raise SystemExit(f'Frozen source changed: {name}')

evidence = []
for name in ('review.md', 'review-dispositions.md', 'provider-disable-review.md',
             'provider-disable-dispositions.md', 'amended-composition-review.md',
             'verification.md', 'provider-verification.md'):
    path = record / name
    evidence.append({'kind': 'verification' if name in ('verification.md', 'provider-verification.md') else 'review',
                     'path': str(path), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})

for kind in ('machine_activate', 'profile_activate'):
    request = {'schema': 1, 'requestId': str(uuid.uuid4()), 'kind': kind, 'evidence': evidence}
    if kind == 'machine_activate':
        request['target'] = 'aitherdev'
    path = record / f'{kind}-amended-prepare-request.json'
    with path.open('x') as output:
        output.write(json.dumps(request, indent=2) + '\n')
