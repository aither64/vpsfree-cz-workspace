#!/usr/bin/env python3
"""Launch the one Terraform VM attempt; credential loading stays private."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
EXPECTED = {'package-c-r-terraform-smoke-2.py': '685afed748231be3b8b9a708de4dc22045217282d6a7f54a6a67e6200da2d179', 'package-c-r-verification-manifest.json': 'bbeec793c0c6407023bd4f5eda8d942dbeaeded7cc7e435725d4352575023e8c', 'review-r-report.md': '2b9ecce9d66a5994e664b99ba0c1f1454631c14a923a53f58b25ece48ded99a9'}
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
argv = [sys.executable, str(HERE / 'package-c-r-terraform-smoke-2.py'),
        '--root', '/tmp/flake-update-guard-tf3',
        '--review-receipt', str(HERE / 'review-r-report.md'), 'terraform-smoke']
print('Executing argv: ' + json.dumps(argv), flush=True)
try:
    os.execve(argv[0], argv, child_env)
except Exception:
    raise SystemExit('Unable to start Terraform verification') from None
