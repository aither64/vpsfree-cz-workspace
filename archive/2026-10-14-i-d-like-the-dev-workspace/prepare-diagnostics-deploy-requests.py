#!/usr/bin/env python3
"""Seal reviewed final evidence for build/copy preparation; never activate."""
import hashlib
import json
from pathlib import Path
import subprocess
import uuid

record = Path(__file__).resolve().parent
workspace = record.parent.parent
revision = '0b403305e085aa01884cf56acea7c717f78f7e86'
assert subprocess.check_output(['dev-session', 'current'], cwd=record, text=True).strip() == record.name
heads = json.loads((record / 'diagnostics-final-heads.json').read_text())
for source in heads['repositories']:
    checkout = workspace / 'worktrees' / record.name / source['repository']
    assert subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=checkout, text=True).strip() == source['head']
    assert not subprocess.check_output(['git', 'status', '--porcelain'], cwd=checkout)
    for name, digest in source['artifacts'].items():
        assert hashlib.sha256((record / name).read_bytes()).hexdigest() == digest
for name in ('provider-recovery-final.status', 'runtime-diagnostics-flake.status'):
    status = dict(line.split('=', 1) for line in (record / name).read_text().splitlines())
    assert status['revision'] == revision and status['exit_status'] == '0'
assert (record / 'verification-diagnostics.md').read_text().splitlines()[2].startswith('Status: PASS.'), 'Lead verification reconciliation is pending.'
ci = json.loads((record / 'ci-provider-diagnostics.json').read_text())
assert ci['headSha'] == revision and ci['status'] == 'completed' and ci['conclusion'] == 'success'

names = ('review.md', 'review-dispositions.md', 'provider-disable-review.md',
         'provider-disable-dispositions.md', 'provider-diagnostics-review.md',
         'provider-diagnostics-dispositions.md', 'diagnostics-composition-review.md',
         'diagnostics-final-heads.json', 'verification-diagnostics.md', 'provider-verification.md')
evidence = []
for name in names:
    path = record / name
    evidence.append({'kind': 'verification' if name in ('verification-diagnostics.md', 'provider-verification.md') else 'review',
                     'path': str(path), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
paths = {kind: record / f'{kind}-diagnostics-prepare-request.json' for kind in ('machine_activate', 'profile_activate')}
assert not any(path.exists() for path in paths.values()), 'Retain existing requests; inspect before retry.'
for kind, path in paths.items():
    request = {'schema': 1, 'requestId': str(uuid.uuid4()), 'kind': kind, 'evidence': evidence}
    if kind == 'machine_activate':
        request['target'] = 'aitherdev'
    with path.open('x') as output:
        output.write(json.dumps(request, indent=2) + '\n')
