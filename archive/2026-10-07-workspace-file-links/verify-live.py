import base64
import hashlib
import json
import pathlib
import ssl
import urllib.error
import urllib.parse
import urllib.request

ROOT = pathlib.Path('/home/aither/workspace/ai/vpsfree.cz')
BASE = 'https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz'
SLUG = '2026-10-07-workspace-file-links'
context = ssl.create_default_context(cafile='/var/lib/dev-workspaces/public/ca.pem')
password = pathlib.Path('/var/lib/dev-workspaces/password/password').read_text().strip()
authorization = 'Basic ' + base64.b64encode(('aither:' + password).encode()).decode()


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, msg, headers, newurl):
        return None


opener = urllib.request.build_opener(
    urllib.request.HTTPSHandler(context=context), NoRedirect())


def get(path, authenticated=True):
    headers = {'Authorization': authorization} if authenticated else {}
    request = urllib.request.Request(BASE + path, headers=headers)
    try:
        response = opener.open(request, timeout=30)
    except urllib.error.HTTPError as response_error:
        response = response_error
    with response:
        return response.status, response.headers, response.read()


results = {'tls_verified': True, 'checks': []}


def check(name, path, expected, authenticated=True):
    status, headers, body = get(path, authenticated)
    results['checks'].append({'name': name, 'status': status,
                              'expected': expected, 'passed': status == expected})
    assert status == expected, (name, status, expected)
    return headers, body


legacy = str(ROOT) + '/docs/agent-instructions/lifecycle.md:93'
headers, _ = check('original URL', legacy, 302)
target = headers['Location']
assert target == '/workspace-files?path=docs%2Fagent-instructions%2Flifecycle.md#L93'
results['redirect'] = target
headers, body = check('canonical viewer', target, 200)
assert headers['Cache-Control'] == 'no-store'
assert b'data-file-api="/api/workspace/file"' in body
assert b'Back to session' not in body
_, body = check('shared document API', '/api/workspace/file?' +
                urllib.parse.urlencode({'path': 'docs/agent-instructions/lifecycle.md'}), 200)
document = json.loads(body)
text = (ROOT / 'docs/agent-instructions/lifecycle.md').read_text()
assert document['source'] == 'workspace'
assert document['content']['text'] == text
assert len(text.splitlines()) >= 93
results['document_sha256'] = hashlib.sha256(text.encode()).hexdigest()
results['line_93_sha256'] = hashlib.sha256(text.splitlines()[92].encode()).hexdigest()
check('root AGENTS API', '/api/workspace/file?path=AGENTS.md', 200)
check('authentication', '/api/workspace/file?path=AGENTS.md', 401, False)
for path in ['.git/config', '../AGENTS.md', 'repos/workspace.git/config',
             'work/' + SLUG + '/plan.md', 'worktrees/' + SLUG + '/workspace/AGENTS.md']:
    check('excluded: ' + path, '/api/workspace/file?' + urllib.parse.urlencode({'path': path}), 400)
check('missing file', '/api/workspace/file?path=file-link-missing-2026-10-07.md', 404)
check('untracked note', '/api/workspace/file?' + urllib.parse.urlencode({
    'path': 'notes/dev-workspace/2026-10-07-file-links-ci-baseline-race.md'}), 404)
headers, _ = check('existing session legacy link', str(ROOT) + '/work/' + SLUG + '/plan.md:1', 302)
assert headers['Location'] == '/files/' + SLUG + '?artifact=plan.md#L1'
check('existing session viewer', headers['Location'], 200)
_, body = check('existing session API', '/api/sessions/' + SLUG + '/file?artifact=plan.md', 200)
assert json.loads(body)['source'] == 'artifact'
output = ROOT / 'work' / SLUG / 'live-verification.json'
output.write_text(json.dumps(results, indent=2) + '\n')
print(json.dumps(results, indent=2))
