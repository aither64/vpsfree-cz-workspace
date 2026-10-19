#!/usr/bin/env python3
import hashlib
import json
import os
import subprocess
import uuid
from pathlib import Path

root = Path('/home/aither/workspace/ai/vpsfree.cz')
t = root / 'work/2026-10-13-workspace-coordination'
expected = {
    'dev-workspace': '0651f64c5ed13d8a3dcf70cfa7ba4c991ea1ac97',
    'vpsfree-dev-workspace': 'c697acc70b05c9bc6cf7bf53fe63700f1f6c1276',
    'workspace': '091563377e4ee885f53e2fcbc6be0c91c0771bbc',
    'vpsfree-cz-configuration': '63a0b59a32296c1a3de6512d1d6d3dc1e3a400e6',
}
for repo, head in expected.items():
    wd = root / 'worktrees/2026-10-13-workspace-coordination' / repo
    def git(*args):
        return subprocess.check_output(['git', '-C', str(wd), *args], text=True)
    assert git('rev-parse', 'HEAD').strip() == head
    assert git('status', '--porcelain') == ''
for name in ['stdout-candidate-build.status', 'stdout-system-build.status', 'native-final.status']:
    assert (t / name).read_text().strip() == '0', name
candidate = (t / 'stdout-candidate.path').read_text().strip()
assert candidate == (t / 'candidate-package.path').read_text().strip()
assert os.path.realpath(t / 'stdout-candidate-gc-root') == candidate
ci = json.loads((t / 'stdout-runtime-ci.json').read_text())
assert ci['headSha'] == expected['dev-workspace']
assert ci['status'] == 'completed' and ci['conclusion'] == 'success'
extension = json.loads((t / 'library-extension-ci.json').read_text())
assert extension['headSha'] == expected['vpsfree-dev-workspace']
assert extension['status'] == 'completed' and extension['conclusion'] == 'success'
for historical in ['acceptance-evidence.json', 'library-acceptance-evidence.json']:
    previous = json.loads((t / historical).read_text())
    for name, info in previous['files'].items():
        assert hashlib.sha256((t / name).read_bytes()).hexdigest() == info['sha256'], name
files = [
    'acceptance-evidence.json', 'library-acceptance-evidence.json',
    'profile-stdout-review.md', 'profile-stdout-review-packet.md',
    'profile-stdout-inventory.json', 'profile-stdout-fix.patch',
    'profile-stdout-quick.log', 'profile-stdout-host.log',
    'profile-stdout-composition.log', 'profile-stdout-config-pin.log',
    'stdout-candidate-check.log', 'stdout-candidate-build.log',
    'stdout-candidate-build.status', 'stdout-system-build.log',
    'stdout-system-build.status', 'stdout-runtime-ci.json',
    'library-extension-ci.json', 'native-final.log', 'native-final.status',
]
record = {
    'schema': 1, 'heads': expected, 'candidatePackage': candidate,
    'systemPackage': '/nix/store/l1y7x5pa0j5cpqk9sffv0mcgmsamd3bl-nixos-system-aitherdev-26.05.20261012.7993f34',
    'ci': {
        'runtime': {'runId': 38432529049, 'headSha': ci['headSha'], 'conclusion': 'success'},
        'extension': {'runId': 38427613788, 'headSha': extension['headSha'], 'conclusion': 'success'},
    },
    'verification': {
        'review': 'All four affected Astra/xhigh lanes passed; independent actual-child overflow probe; no migrations.',
        'quick': 'Public preparation JSON/failure regression 1/12; full Host 161/1224; composition and history checks passed.',
        'package': 'Exact composed candidate build and packaged checks passed; sandbox skips retained in build log.',
        'system': 'Exact configuration build passed, no local kernel compilation.',
        'baselineAcceptance': 'Original flake/VM/systemd/native evidence reused. Original batch exit 2 was diagnosed native fixture setup; final native status 0 is the passing evidence.',
        'realPreparation': 'Required separately before activation; previous superseded preparation succeeded before wrapper JSON parsing failed.',
    },
    'files': {name: {'sha256': hashlib.sha256((t / name).read_bytes()).hexdigest()} for name in files},
}
evidence = t / 'stdout-acceptance-evidence.json'
assert not evidence.exists()
evidence.write_text(json.dumps(record, indent=2) + '\n')
request_file = t / 'bootstrap-prepare-request.json'
saved = t / 'bootstrap-prepare-before-stdout-fix.json'
assert not saved.exists()
saved.write_bytes(request_file.read_bytes())
references = [
    ('review', 'review-reconciliation.md'),
    ('review', 'confctl-library-review.md'),
    ('review', 'profile-stdout-review.md'),
    ('verification', evidence.name),
]
request = {
    'schema': 1, 'requestId': str(uuid.uuid4()),
    'approvalQuote': 'you can deploy it to aitherdev using vpsfree-cz-configuration',
    'evidence': [
        {'kind': kind, 'path': str((t / name).relative_to(root)),
         'sha256': hashlib.sha256((t / name).read_bytes()).hexdigest()}
        for kind, name in references
    ],
    'target': 'aitherdev',
}
request_file.write_text(json.dumps(request, indent=2) + '\n')
for name in ['bootstrap-prepare.status', 'bootstrap-prepared.json.tmp']:
    old = t / name
    if old.exists():
        saved = t / ('before-stdout-fix-' + name)
        assert not saved.exists()
        old.rename(saved)
print(json.dumps({'candidate': candidate, 'requestId': request['requestId']}))
