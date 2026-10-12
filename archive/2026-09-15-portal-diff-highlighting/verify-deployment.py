"""Check the active user profile, authenticated asset and preserved services."""
import base64
import hashlib
import http.client
import json
from pathlib import Path
import ssl
import subprocess

tracking = Path(__file__).resolve().parent
workspace = tracking.parents[1]
profile = Path('/home/aither/.local/state/dev-workspaces/profile')
expected = (tracking / 'site-package.txt').read_text().strip()
assert str(profile.resolve()) == expected, 'Active profile does not match the built site package'
previous = json.loads((tracking / 'pre-deployment.json').read_text())
host = 'vpsfree-cz.workspace.aitherdev.int.vpsfree.cz'
context = ssl.create_default_context(cafile='/var/lib/dev-workspaces/public/ca.pem')
password = Path('/var/lib/dev-workspaces/password/password').read_text().strip()
authorization = 'Basic ' + base64.b64encode(('aither:' + password).encode()).decode()

def get(path, authenticated=True):
    conn = http.client.HTTPSConnection(host, context=context, timeout=30)
    try:
        conn.request('GET', path, headers={'Authorization': authorization} if authenticated else {})
        response = conn.getresponse()
        return response.status, response.getheader('Cache-Control'), response.read()
    finally:
        conn.close()

results = {'profileLink': profile.readlink().name, 'package': expected, 'tlsVerified': True}
status, _, _ = get('/static/review-editor.js', authenticated=False)
assert status == 401
results['unauthenticatedAssetStatus'] = status
for path in ['/healthz', '/' + tracking.name + '/']:
    status, cache, body = get(path)
    assert status == 200, f'{path}: HTTP {status}'
    results[path] = {'status': status, 'cacheControl': cache}
status, cache, body = get('/static/review-editor.js')
source = workspace / 'worktrees' / tracking.name / 'dev-workspace/portal/review-ui/dist/review-editor.js'
assert status == 200 and cache == 'no-store'
digest = hashlib.sha256(body).hexdigest()
assert digest == hashlib.sha256(source.read_bytes()).hexdigest(), 'Served editor differs from reviewed bundle'
results['editorAsset'] = {'status': status, 'cacheControl': cache, 'sha256': digest, 'matchesReviewedBundle': True}
results['services'] = {}
for unit, before in previous['units'].items():
    current = dict(line.split('=', 1) for line in subprocess.check_output(
        ['systemctl', '--user', 'show', unit, '-p', 'MainPID', '-p', 'ActiveState'], text=True).splitlines())
    assert current['ActiveState'] == 'active', unit
    if unit.startswith(('workspace-codex@', 'workspace-tmux@')):
        assert current['MainPID'] == before['MainPID'], 'Runtime process changed: ' + unit
    results['services'][unit] = current
results['systemUnchanged'] = str(Path('/run/current-system').resolve()) == previous['system']
assert results['systemUnchanged']
(tracking / 'post-deployment.json').write_text(json.dumps(results, indent=2) + '\n')
print(json.dumps(results, indent=2))
