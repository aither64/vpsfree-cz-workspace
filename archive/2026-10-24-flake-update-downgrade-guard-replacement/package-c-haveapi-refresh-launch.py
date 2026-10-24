#!/usr/bin/env python3
"""Launch the reviewed HaveAPI-only pattern; credential loading stays private."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
EXPECTED = {'package-c-haveapi-refresh-post-review.py': 'c0ff46d07593482468e148a1ea0588e1806475a1cfcd22859535147fa72911ca', 'package-c-haveapi-refresh-verification-manifest.json': '5484745a91c545dc4ebde972e0c7745db44a5f3e92e0004c1cc2121a19c56f39', 'review-haveapi-refresh-report.md': '3e07ec8ebeed1dd69ed9e5988501527cf143ef1920dcb7439bfaad334dc3e25e'}
if len(sys.argv) != 1:
    raise SystemExit('This fixed launcher takes no arguments')
for name, expected in EXPECTED.items():
    if hashlib.sha256((HERE / name).read_bytes()).hexdigest() != expected:
        raise SystemExit('Frozen input hash differs: ' + name)

# Select the relogged GitHub CLI credential rather than an inherited token.
auth_env = dict(os.environ)
auth_env.pop('GH_TOKEN', None)
auth_env.pop('GITHUB_TOKEN', None)
try:
    auth = subprocess.run(
        ['gh', 'auth', 'token', '--hostname', 'github.com'],
        env=auth_env, stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        timeout=30, check=False)
    if auth.returncode != 0:
        raise ValueError()
    token = auth.stdout.decode('utf-8').strip()
    if not token or any(character in token for character in ('\n', '\r', '\0')):
        raise ValueError()
except Exception:
    raise SystemExit('Unable to load GitHub credentials') from None

child_env = dict(os.environ)
child_env.pop('GH_TOKEN', None)
child_env['GITHUB_TOKEN'] = token
argv = [sys.executable, str(HERE / 'package-c-haveapi-refresh-post-review.py'),
        '--root', '/tmp/flake-update-guard-haveapi-refresh-1',
        '--review-receipt', str(HERE / 'review-haveapi-refresh-report.md'), 'project', 'haveapi']
print('Executing argv: ' + json.dumps(argv), flush=True)
try:
    os.execve(argv[0], argv, child_env)
except Exception:
    raise SystemExit('Unable to start HaveAPI verification') from None
