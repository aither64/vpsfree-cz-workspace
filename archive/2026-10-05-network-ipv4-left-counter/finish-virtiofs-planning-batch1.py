#!/usr/bin/env python3
"""One sequential read-only planning batch; no realization or guest operation."""
import pathlib
import subprocess
import sys

tracking = pathlib.Path(__file__).resolve().parent
for helper in (
    'finish-virtiofs-plan-projection1.py',
    'finish-virtiofs-kernel-builder-proof1.py',
    'finish-virtiofs-closure-plan1.py',
    'finish-virtiofs-missing-closure-facts1.py',
):
    result = subprocess.run([sys.executable, str(tracking / helper)], cwd=tracking)
    if result.returncode:
        raise SystemExit(result.returncode)
