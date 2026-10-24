#!/usr/bin/env python3
"""Frozen org-only evidence successor; root owns launch after race reconciliation."""
import hashlib
import json
from pathlib import Path
import shlex
import subprocess
import sys

HERE = Path(__file__).resolve().parent
MANIFEST = HERE / 'package-c7-git-cache-org-manifest-2.json'
MANIFEST_SHA = '2b44596163bb29c7761c5ff08ee3be574abb741bfd9274a5e6685f4895bb3c34'
DRIVER = HERE / 'package-c7-git-cache-org-post-review-2.py'
DRIVER_SHA = '9914b1be04590b93af3d85cafef60013cf0e5c65bcfb9223dfd70ec1f48259e3'
REVIEW = HERE / 'review-git-cache-report.md'
REVIEW_SHA = '6bb7afca1cd0b1794fb97bb3f8bcd20453a6ed94ae346fc0d375d4a27d4e92dd'
ROOT = '/tmp/flake-update-guard-c7-git-cache-org-2'
LOG = HERE / 'consumer-git-cache-org-2.log'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    if len(sys.argv) != 1:
        raise SystemExit('Frozen launcher takes no arguments')
    if digest(MANIFEST) != MANIFEST_SHA or digest(DRIVER) != DRIVER_SHA or digest(REVIEW) != REVIEW_SHA:
        raise SystemExit('Frozen source/review binding changed')
    if Path(ROOT).exists() or Path(ROOT).is_symlink():
        raise SystemExit('Existing attempt requires parent diagnosis; never overwrite or retry')
    argv = [sys.executable, str(DRIVER), '--root', ROOT, '--review-receipt', str(REVIEW),
            '--manifest-sha256', MANIFEST_SHA, 'project', 'vpsadminos-org-configuration']
    with LOG.open('x') as log:
        line = 'SAFE argv: ' + shlex.join(argv) + '\n'
        print(line, end='', flush=True); log.write(line); log.flush()
        process = subprocess.Popen(argv, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in process.stdout:
            print(line, end='', flush=True); log.write(line); log.flush()
        status = process.wait()
        log.write('Operation exit: ' + str(status) + '\n'); log.flush()
        if status:
            return status if 0 < status < 256 else 1
        receipt = json.loads((Path(ROOT) / 'project-vpsadminos-org-configuration/receipt.json').read_text())
        if not (receipt['complete'] and receipt['exit_status'] == 0 and receipt['final']['status'] == ''
                and receipt['final']['lock_equals_head'] and not receipt['cold_cache_claim']
                and receipt['fixture_local_exclude']['rule'] == '/.bundle/config'):
            raise SystemExit('Org-only final receipt acceptance incomplete; parent diagnosis required')
    return 0


if __name__ == '__main__':
    sys.exit(main())
