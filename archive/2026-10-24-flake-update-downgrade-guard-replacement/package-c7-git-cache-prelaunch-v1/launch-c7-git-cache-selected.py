#!/usr/bin/env python3
"""Fixed no-argument post-review launcher; no credential lookup or auth loader."""
import hashlib
import json
from pathlib import Path
import shlex
import subprocess
import sys

HERE = Path(__file__).resolve().parent
MANIFEST = HERE / 'package-c7-git-cache-manifest.json'
MANIFEST_SHA = 'b154eec8eae770278adf23d8e375d235f8a85930f4e1e08f4e36fcdefdf0b425'
DRIVER_SHA = '7015f6719ab89bfd63d1ac11aa78e4f31ab5278f53438dd96b8337033a87d6a4'
ROOT = '/tmp/flake-update-guard-c7-git-cache-2026-10-24-1'
REVIEW = HERE / 'review-git-cache-report.md'
LOG = HERE / 'consumer-git-cache-selected.log'


def main():
    if len(sys.argv) != 1:
        raise SystemExit('This frozen launcher takes no arguments')
    if (hashlib.sha256(MANIFEST.read_bytes()).hexdigest() != MANIFEST_SHA or not REVIEW.is_file()
            or hashlib.sha256(REVIEW.read_bytes()).hexdigest() != '6bb7afca1cd0b1794fb97bb3f8bcd20453a6ed94ae346fc0d375d4a27d4e92dd'):
        raise SystemExit('Frozen manifest and completed review receipt are required')
    manifest = json.loads(MANIFEST.read_text())
    driver = HERE / 'package-c7-git-cache-post-review.py'
    if hashlib.sha256(driver.read_bytes()).hexdigest() != DRIVER_SHA:
        raise SystemExit('Frozen driver hash mismatch')
    with LOG.open('x') as log:
        for suffix in [['project', 'haveapi'], ['project', 'terraform-provider-vpsadmin'], ['project', 'vpsadminos'], ['project', 'vpsf-status'], ['project', 'vpsfree-irc-bot'], ['project', 'vpsfree-cz-configuration'], ['project', 'vpsadminos-org-configuration']]:
            argv = [sys.executable, str(driver), '--root', ROOT, '--review-receipt', str(REVIEW),
                    '--manifest-sha256', MANIFEST_SHA, *suffix]
            line = 'SAFE argv: ' + shlex.join(argv) + '\n'
            print(line, end='', flush=True); log.write(line); log.flush()
            process = subprocess.Popen(argv, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            for line in process.stdout:
                print(line, end='', flush=True); log.write(line); log.flush()
            status = process.wait()
            log.write('Operation exit: ' + str(status) + '\n'); log.flush()
            if status:
                return status if 0 < status < 256 else 1
        receipts = [json.loads((Path(ROOT) / ('project-' + item['project']) / 'receipt.json').read_text()) for item in manifest['projects']]
        url = 'https://github.com/NixOS/nixpkgs'
        cold = [r['stage'] for r in receipts if url in r['new_mirrors']]
        warm = [r['stage'] for r in receipts if url in r['reused_mirrors'] and r['warm_final_cache_unchanged']]
        summary = {'provider_head': manifest['provider_head'], 'manifest_sha256': MANIFEST_SHA,
                   'scope': manifest['scope'], 'all_seven_full_workflows': False,
                   'project_receipts': [str(Path(ROOT) / r['stage'] / 'receipt.json') for r in receipts],
                   'nixpkgs_url': url, 'nixpkgs_cold_install_stages': cold, 'nixpkgs_warm_reuse_stages': warm,
                   'additional_cold_mirrors': {r['stage']: [u for u in r['new_mirrors'] if u != url] for r in receipts},
                   'selected_paths_complete': all(r['complete'] and r['exit_status'] == 0 for r in receipts)}
        (Path(ROOT) / 'selected-paths-summary.json').write_text(json.dumps(summary, indent=2) + '\n')
        if len(cold) != 1 or not warm or not summary['selected_paths_complete']:
            log.write('Cache/selected-path acceptance incomplete; parent diagnosis required\n')
            return 2
    return 0


if __name__ == '__main__':
    sys.exit(main())
