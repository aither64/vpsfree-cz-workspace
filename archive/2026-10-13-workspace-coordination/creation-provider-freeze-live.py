"""Freeze checked, read-only observations of the reserved successor rollout."""
import datetime
import hashlib
import json
import os
import subprocess
from pathlib import Path

root = Path('/home/aither/workspace/ai/vpsfree.cz')
tracking = root / 'work/2026-10-13-workspace-coordination'


def read(name):
    return json.loads((tracking / name).read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(name, value):
    path = tracking / name
    assert not path.exists(), name
    path.write_text(json.dumps(value, indent=2) + '\n')


assert (tracking / 'creation-provider-bootstrap-execution.status').read_text().strip() == '0'
result = read('creation-provider-bootstrap-result.json')
frozen = read('creation-provider-acceptance-evidence.json')
assert result['state'] == 'deployed_review'
assert result['reservationId'] == 'd114323d-806c-479f-b7a4-8c1a08afb45b'
for name, digest in frozen['files'].items():
    assert sha(tracking / name) == digest, name
live = json.loads(subprocess.check_output(['python3', str(tracking / 'capture-live.py')], text=True))
baseline = read('creation-provider-activation-baseline.json')
for path in ['/run/current-system', '/nix/var/nix/profiles/system']:
    assert live[path]['resolved'] == frozen['systemPackage'], path
assert live['/home/aither/.local/state/dev-workspaces/profile']['resolved'] == frozen['candidatePackage']
for key in ['bootId', 'runningKernel']:
    assert live[key] == baseline[key], key
for service, observation in live['services'].items():
    assert 'ActiveState=active' in observation, service
for service in ['workspace-codex@vpsfree-cz.service', 'workspace-codex-provider@vpsfree-cz.service']:
    assert live['services'][service] == baseline['services'][service], service
env = dict(os.environ, DEV_SESSION_SLUG='2026-10-13-workspace-coordination', DEV_SESSION_WORKSPACE=str(root))
status = json.loads(subprocess.check_output([
    'dev-session', 'coordination', 'status', '2026-10-13-workspace-coordination',
    '--as-is', '--json', '--bootstrap-owner', '55e83d75-cb96-417a-9308-11d3caf22dcd',
], env=env, text=True))
assert len(status['owners']) == 1 and len(status['jobs']) == 10
assert all(job['state'] == 'succeeded' for job in status['jobs'])
jobs = [next(job for job in status['jobs'] if job['id'] == job_id) for job_id in result['jobs']]
assert [job['kind'] for job in jobs] == ['machine_activate', 'profile_activate']
assert all(job['result']['outcome'] == 'applied' for job in jobs)
reservation = next(r for r in status['reservations'] if r['id'] == result['reservationId'])
assert reservation['ownerId'] == '55e83d75-cb96-417a-9308-11d3caf22dcd'
assert reservation['state'] == 'deployed_review'
worker_units = {}
for job in jobs:
    unit = 'workspace-operation-' + job['result']['attemptId'] + '.service'
    output = subprocess.check_output([
        'systemctl', '--user', 'show', unit, '-p', 'ActiveState', '-p', 'SubState',
        '-p', 'InvocationID', '-p', 'ExecMainStatus',
    ], text=True)
    observed = dict(line.split('=', 1) for line in output.splitlines())
    assert observed['SubState'] == 'exited' and observed['ExecMainStatus'] == '0', unit
    worker_units[job['id']] = dict(unit=unit, **observed)
api = json.loads(subprocess.check_output([
    'curl', '--fail', '--silent', '--show-error', '--unix-socket', '/run/dev-workspaces/router.sock',
    '-H', 'Host: vpsfree-cz.workspace.aitherdev.int.vpsfree.cz', 'http://localhost/api/coordination',
], text=True))
holder = next(h for w in api['workspaces'] for h in w['reservationHolders']
              if h['ownerId'] == reservation['ownerId'])
assert holder['slug'] == '2026-10-13-workspace-coordination'
assert holder['machines'][0]['state'] == 'deployed_review'
assert holder['machines'][0]['deployments'] == 10
save('creation-provider-deployed-live-identities.json', live)
save('creation-provider-deployed-coordination-status.json', status)
save('creation-provider-deployed-api.json', api)
save('creation-provider-deployed-worker-status.json', worker_units)
save('creation-provider-deployed-live-checks.json', {
    'schema': 1, 'observedAt': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'outcome': 'passed', 'sourceHeads': frozen['heads'],
    'systemPackage': frozen['systemPackage'], 'candidatePackage': frozen['candidatePackage'],
    'requestId': read('creation-provider-bootstrap-execution-request.json')['requestId'],
    'bootstrapUnit': 'workspace-coordination-creation-bootstrap-execute-20261013.service',
    'bootstrapInvocation': (tracking / 'creation-provider-execute-invocation').read_text().strip(),
    'reservation': {key: reservation[key] for key in ['id', 'ownerId', 'machine', 'state', 'revision', 'mode']},
    'jobs': jobs, 'workerUnits': worker_units,
    'checks': {'exactSystemAndProfile': True, 'allServicesActive': True,
               'bootAndKernelUnchanged': True, 'nativePidsUnchanged': True,
               'reservationHeld': True, 'tenSucceededJobs': True},
})
print('Live system, profile, services, worker receipts and retained reservation passed')
