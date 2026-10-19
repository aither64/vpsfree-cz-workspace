"""Verify frozen rollout evidence and unchanged predecessor before activation."""
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


assert (tracking / 'operations-clarity-bootstrap-prepare.status').read_text().strip() == '0'
prepared = read('operations-clarity-bootstrap-prepared.json')
request = read('operations-clarity-bootstrap-execution-request.json')
frozen = read('operations-clarity-acceptance-evidence.json')
assert prepared['request'] == request
assert request['requestId'] == read('operations-clarity-bootstrap-prepare-request.json')['requestId']
for name, digest in frozen['files'].items():
    assert sha(tracking / name) == digest, name
for evidence in request['evidence']:
    assert sha(root / evidence['path']) == evidence['sha256'], evidence['path']
for name, head in frozen['heads'].items():
    repo = root / 'worktrees/2026-10-13-workspace-coordination' / name
    assert subprocess.check_output(['git', '-C', str(repo), 'rev-parse', 'HEAD'], text=True).strip() == head
    assert not subprocess.check_output(['git', '-C', str(repo), 'status', '--porcelain'], text=True)
assert (tracking / 'operations-clarity-candidate-gc-root').resolve() == Path(frozen['candidatePackage'])

artifact_root = Path('/home/aither/.local/state/dev-workspaces/coordination/sources')


def artifact(digest):
    return json.loads((artifact_root / digest.removeprefix('sha256:') / 'artifact.json').read_text())


profile = artifact(request['profileArtifact'])
machine = artifact(request['machineSnapshot']['operation']['preparedArtifact'])
assert profile['candidatePackage'] == frozen['candidatePackage']
assert profile['source'] == prepared['source']
assert profile['profileToken'] == (tracking / 'operations-clarity-bootstrap-predecessor-token').read_text().strip()
assert request['machineSnapshot']['operation']['configurationHead'] == frozen['heads']['vpsfree-cz-configuration']
generations = root / 'worktrees/2026-10-13-workspace-coordination/vpsfree-cz-configuration/.confctl/generations/cz.vpsfree:machines:aitherdev'
generation_path = generations / frozen['systemGeneration'] / 'generation.json'
assert sha(generation_path) == frozen['systemGenerationSha256']
generation = json.loads(generation_path.read_text())
assert generation['toplevel'] == machine['toplevel']
assert machine['toplevel'] == frozen['systemPackage']

live = json.loads(subprocess.check_output(['python3', str(tracking / 'capture-live.py')], text=True))
baseline = read('operations-clarity-activation-baseline.json')
for path in ['/run/current-system', '/nix/var/nix/profiles/system', '/home/aither/.local/state/dev-workspaces/profile']:
    assert live[path] == baseline[path], path
for key in ['bootId', 'runningKernel']:
    assert live[key] == baseline[key], key
for service in ['workspace-codex@vpsfree-cz.service', 'workspace-codex-provider@vpsfree-cz.service']:
    assert live['services'][service] == baseline['services'][service], service
env = dict(os.environ, DEV_SESSION_SLUG='2026-10-13-workspace-coordination', DEV_SESSION_WORKSPACE=str(root))
status = json.loads(subprocess.check_output([
    'dev-session', 'coordination', 'status', '2026-10-13-workspace-coordination',
    '--as-is', '--json', '--bootstrap-owner', '55e83d75-cb96-417a-9308-11d3caf22dcd',
], env=env, text=True))
assert len(status['owners']) == 1 and len(status['jobs']) == 4
assert all(job['state'] == 'succeeded' for job in status['jobs'])
reservation = next(r for r in status['reservations'] if r['id'] == 'd114323d-806c-479f-b7a4-8c1a08afb45b')
assert reservation['ownerId'] == '55e83d75-cb96-417a-9308-11d3caf22dcd'
assert reservation['state'] == 'deployed_review'
for name, data in [('operations-clarity-execution-preflight-live.json', live), ('operations-clarity-execution-preflight-status.json', status)]:
    path = tracking / name
    assert not path.exists(), name
    path.write_text(json.dumps(data, indent=2) + '\n')
print(json.dumps({'outcome': 'passed', 'candidate': profile['candidatePackage'], 'system': machine['toplevel'], 'requestId': request['requestId'], 'reservationId': reservation['id']}))
