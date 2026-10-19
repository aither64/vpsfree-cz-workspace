import hashlib
import json
import re
import subprocess
import uuid
from pathlib import Path

root = Path('/home/aither/workspace/ai/vpsfree.cz')
t = root / 'work/2026-10-13-workspace-coordination'
for name in ['verification', 'candidate-build', 'system-build']:
    assert (t / f'operations-tab-{name}.status').read_text().strip() == '0'
ci = json.loads((t / 'operations-tab-ci-final.json').read_text())
assert ci['headSha'] == 'ef4ec58d1838ed01706c0e85e306117821a0a114'
assert ci['status'] == 'completed' and ci['conclusion'] == 'success'
confirmed_ci = json.loads((t / 'operations-tab-ci-run-confirmed.json').read_text())
for key in ['databaseId', 'headSha', 'status', 'conclusion', 'url']:
    assert confirmed_ci[key] == ci[key]
heads = {i['repository']: i['head'] for i in json.loads((t / 'operations-tab-final-inventory.json').read_text())}
names = re.findall(r'^([0-9]{4}-[0-9]{2}-[0-9]{2}--[0-9]{2}-[0-9]{2}-[0-9]{2})$', (t / 'operations-tab-system-build.log').read_text(), re.MULTILINE)
assert len(names) == 1
generation_path = root / 'worktrees/2026-10-13-workspace-coordination/vpsfree-cz-configuration/.confctl/generations/cz.vpsfree:machines:aitherdev' / names[0] / 'generation.json'
generation = json.loads(generation_path.read_text())
assert generation['inputs_info']['devWorkspace']['rev'] == heads['dev-workspace']
runtime = root / 'worktrees/2026-10-13-workspace-coordination/dev-workspace'
prior_head = '84dde222628bb52e6e3149a8527700d753c2151e'
changed = set(subprocess.check_output(['git', '-C', str(runtime), 'diff', '--name-only', prior_head, heads['dev-workspace']], text=True).splitlines())
assert changed == {
    'portal/internal/web/static/coordination.js',
    'portal/internal/web/coordination_browser_test.cjs',
    'portal/internal/web/templates/session.html',
    'portal/internal/web/templates/operations.html',
    'portal/internal/web/templates/index.html',
}
preview = json.loads((t / 'operations-tab-preview-browser-result.json').read_text())
assert preview['outcome'] == 'passed'
files = [
    'operations-clarity-review.md', 'operations-clarity-review-reconciliation.md',
    'operations-tab-review-reconciliation.md', 'operations-tab-final-inventory.json',
    'operations-tab-runtime-delta.patch', 'operations-tab-composition.log',
    'operations-tab-quick.log', 'operations-tab-preview-browser-result.json',
    'operations-tab-verification.sh', 'operations-tab-candidate-build.log',
    'operations-tab-workspace-checks.log', 'operations-tab-system-build.log',
    'operations-tab-ci-final.json', 'operations-tab-ci-run-confirmed.json',
    'operations-clarity-vm-checks.log',
    'operations-clarity-acceptance-evidence.json',
]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


value = {
    'schema': 1, 'heads': heads,
    'candidatePackage': (t / 'operations-tab-candidate.path').read_text().strip(),
    'systemPackage': generation['toplevel'], 'systemGeneration': names[0],
    'systemGenerationSha256': sha(generation_path), 'ci': confirmed_ci,
    'ciObservation': 'Original jobs snapshot retains stale step metadata; fresh exact-run query confirms completed/success. The jobs refresh returned HTTP 502.',
    'checks': {'package': 'passed', 'workspace': 'passed', 'matchingSystem': 'passed',
               'quickBrowser': '10 passed', 'realBrowserPreview': 'passed'},
    'reusedVMChecks': {'testedHead': prior_head, 'sourceDelta': sorted(changed),
                     'reason': 'Only browser listener, templates and regression fixture changed; backend, host, worker and VM sources are identical.',
                     'hostModuleIdempotency': 'passed locally', 'sessionRecoveryBoot': 'passed locally'},
    'files': {name: sha(t / name) for name in files},
}
evidence_path = t / 'operations-tab-acceptance-evidence.json'
assert not evidence_path.exists()
evidence_path.write_text(json.dumps(value, indent=2) + '\n')
evidence = []
for kind, name in [('review', 'operations-clarity-review.md'), ('review', 'operations-tab-review-reconciliation.md'), ('verification', evidence_path.name)]:
    evidence.append({'kind': kind, 'path': str((t / name).relative_to(root)), 'sha256': sha(t / name)})
request = {'schema': 1, 'requestId': str(uuid.uuid4()), 'approvalQuote': 'you can deploy it to aitherdev using vpsfree-cz-configuration', 'evidence': evidence, 'target': 'aitherdev'}
path = t / 'operations-tab-bootstrap-prepare-request.json'
assert not path.exists()
path.write_text(json.dumps(request, indent=2) + '\n')
print('Corrected tab verification evidence frozen; deployment request prepared')
