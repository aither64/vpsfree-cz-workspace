import os, json
argv = ['python3', '/home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-flake-update-downgrade-guard-replacement/package-c-r-git-race-2.py', '--root', '/tmp/flake-update-guard-git-race-r-2', '--review-receipt', '/home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-flake-update-downgrade-guard-replacement/review-r-report.md']
os.chdir("/home/aither/workspace/ai/vpsfree.cz")
print("Exact launch argv: " + json.dumps(argv), flush=True)
os.execvp(argv[0], argv)
