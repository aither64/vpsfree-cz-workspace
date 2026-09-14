"""Read-only acceptance against the active profile and authenticated portal."""
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
host = 'vpsfree-cz.workspace.aitherdev.int.vpsfree.cz'
context = ssl.create_default_context(cafile='/var/lib/dev-workspaces/public/ca.pem')
password = Path('/var/lib/dev-workspaces/password/password').read_text().strip()
authorization = 'Basic ' + base64.b64encode(('aither:' + password).encode()).decode()

def get(path, authenticated=True):
    conn = http.client.HTTPSConnection(host, context=context, timeout=30)
    try:
        conn.request('GET', path, headers={'Authorization': authorization} if authenticated else {})
        response = conn.getresponse()
        body = response.read()
        return response.status, response.getheader('Cache-Control'), body
    finally:
        conn.close()

results = {'profileLink': profile.readlink().name, 'package': expected, 'tlsVerified': True}
status, _, _ = get('/static/app.js', authenticated=False)
assert status == 401, f'Unauthenticated asset status {status}'
results['unauthenticatedAssetStatus'] = status
for path in ['/healthz', '/' + tracking.name + '/']:
    status, cache, body = get(path)
    assert status == 200, f'{path}: HTTP {status}'
    results[path] = {'status': status, 'cacheControl': cache}
source = workspace / 'worktrees' / tracking.name / 'dev-workspace' / 'portal/internal/web/static'
for asset in ['app.js', 'style.css']:
    status, cache, body = get('/static/' + asset)
    assert status == 200 and cache == 'no-store', f'{asset}: status/cache mismatch'
    digest = hashlib.sha256(body).hexdigest()
    assert digest == hashlib.sha256((source / asset).read_bytes()).hexdigest(), f'{asset}: source mismatch'
    results[asset] = {'status': status, 'cacheControl': cache, 'sha256': digest, 'matchesReviewedSource': True}
units = ['workspace-router.service'] + ['workspace-' + kind + '@vpsfree-cz.service' for kind in ['portal', 'codex', 'tmux']]
for unit in units:
    assert subprocess.check_output(['systemctl', '--user', 'is-active', unit], text=True).strip() == 'active', unit
results['activeServices'] = units
(tracking / 'post-deployment.json').write_text(json.dumps(results, indent=2) + '\n')
print(json.dumps(results, indent=2))
