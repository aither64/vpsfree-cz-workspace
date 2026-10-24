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
MANIFEST_SHA = '3e88cb2425376729392535dd894d8c5240747784ebf1d3937eee1b2b7c6f19d2'
DRIVER_SHA = '197187e8e8528f6bf3aac444d3bdec1f43fb89418a94e6fb745b8f0bb937f679'
ROOT = '/tmp/flake-update-guard-c7-git-cache-2026-10-24-1'
REVIEW = HERE / 'review-git-cache-report.md'
LOG = HERE / 'consumer-git-cache-race.log'


def main():
    if len(sys.argv) != 1:
        raise SystemExit('This frozen launcher takes no arguments')
    if (hashlib.sha256(MANIFEST.read_bytes()).hexdigest() != MANIFEST_SHA or not REVIEW.is_file()
            or hashlib.sha256(REVIEW.read_bytes()).hexdigest() != '6bb7afca1cd0b1794fb97bb3f8bcd20453a6ed94ae346fc0d375d4a27d4e92dd'):
        raise SystemExit('Frozen manifest and completed review receipt are required')
    manifest = json.loads(MANIFEST.read_text())
    driver = HERE / 'package-c7-git-cache-race.py'
    if hashlib.sha256(driver.read_bytes()).hexdigest() != DRIVER_SHA:
        raise SystemExit('Frozen driver hash mismatch')
    with LOG.open('x') as log:
        for suffix in [[]]:
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
        pass  # Race receipt contains the strict local target/index/HEAD/lock assertions.
    return 0


if __name__ == '__main__':
    sys.exit(main())
