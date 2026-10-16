#!/usr/bin/env python3
"""Prepare requests only; run after final evidence files and pins are ready."""
import hashlib
import json
from pathlib import Path
import uuid
root = Path(__file__).resolve().parent
for kind in ('machine_activate', 'profile_activate'):
    evidence = []
    for name in ('review.md', 'review-dispositions.md', 'composition-review.md', 'verification.md'):
        path = root / name
        if not path.is_file():
            raise SystemExit(f'Cannot prepare without {name}')
        evidence.append({'kind': 'verification' if name == 'verification.md' else 'review',
                         'path': str(path), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
    value = {'schema': 1, 'requestId': str(uuid.uuid4()), 'kind': kind, 'evidence': evidence}
    if kind == 'machine_activate':
        value['target'] = 'aitherdev'
    target = root / f'{kind}-prepare-request.json'
    if target.exists():
        raise SystemExit(f'Refusing to replace an existing request: {target.name}')
    target.write_text(json.dumps(value, indent=2) + '\n')
