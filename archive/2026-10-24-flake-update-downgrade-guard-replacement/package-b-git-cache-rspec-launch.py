#!/usr/bin/env python3
"""Run the frozen, reviewed Git provider package check without argument transcription."""
import hashlib
import json
import os
from pathlib import Path
import sys

if len(sys.argv) != 1:
    raise SystemExit("This launcher accepts no arguments")
tracking = Path("/home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-flake-update-downgrade-guard-replacement")
script = tracking / "package-b-git-cache-rspec.sh"
review = tracking / "review-git-cache-report.md"
for path, expected in (
    (script, "098c7ad4152c1064253690c578d3ae439f7d4db539d6ee72ef22329b1aaec718"),
    (review, "6bb7afca1cd0b1794fb97bb3f8bcd20453a6ed94ae346fc0d375d4a27d4e92dd"),
):
    if hashlib.sha256(path.read_bytes()).hexdigest() != expected:
        raise SystemExit("Frozen operation receipt mismatch")
run_root = "/tmp/flake-update-guard-b-git-cache-rspec-2026-10-24-1"
argv = ["bash", str(script)]
print(json.dumps({"argv": argv, "root": run_root, "review_receipt": str(review)}), flush=True)
env = os.environ.copy()
env["B_GIT_ROOT"] = run_root
env["B_GIT_REVIEW_RECEIPT"] = str(review)
os.chdir(tracking)
os.execvpe(argv[0], argv, env)
