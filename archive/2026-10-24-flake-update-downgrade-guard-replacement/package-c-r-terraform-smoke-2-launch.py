#!/usr/bin/env python3
"""Launch the one prepared Terraform VM attempt with frozen arguments."""
import hashlib
import json
import os
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
EXPECTED = {'package-c-r-terraform-smoke-2.py': '685afed748231be3b8b9a708de4dc22045217282d6a7f54a6a67e6200da2d179', 'package-c-r-verification-manifest.json': 'bbeec793c0c6407023bd4f5eda8d942dbeaeded7cc7e435725d4352575023e8c', 'review-r-report.md': '2b9ecce9d66a5994e664b99ba0c1f1454631c14a923a53f58b25ece48ded99a9'}
if len(sys.argv) != 1:
    raise SystemExit('This fixed launcher takes no arguments')
for name, expected in EXPECTED.items():
    if hashlib.sha256((HERE / name).read_bytes()).hexdigest() != expected:
        raise SystemExit('Frozen input hash differs: ' + name)
argv = [sys.executable, str(HERE / 'package-c-r-terraform-smoke-2.py'),
        '--root', '/tmp/flake-update-guard-tf2',
        '--review-receipt', str(HERE / 'review-r-report.md'), 'terraform-smoke']
print('Executing argv: ' + json.dumps(argv), flush=True)
os.execv(argv[0], argv)
