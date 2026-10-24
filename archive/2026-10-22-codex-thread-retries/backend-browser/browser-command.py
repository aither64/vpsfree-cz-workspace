#!/usr/bin/env python3
"""Prepared exact-source browser operation. Lead watcher owns execution."""
from pathlib import Path
import datetime
import json
import os
import subprocess
import sys
import time

worktree = Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries/dev-workspace')
tracking = Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-codex-thread-retries/backend-browser')
expected = 'f0af20838ecc0b42812fc3d64e143227306ab6c4'
head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=worktree, text=True).strip()
if head != expected or subprocess.check_output(['git', 'status', '--porcelain'], cwd=worktree):
    raise SystemExit('Frozen browser source identity or cleanliness changed')
out = tracking / 'browser-attempt-1'
out.mkdir()
environment = dict(os.environ,
    PORTAL_BROWSER_TEST='1',
    NODE_PATH='/nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1/lib/node_modules',
    PLAYWRIGHT_BROWSERS_PATH='/nix/store/f0rap655j6wmqbfvqdw445kwcxkxwf7n-playwright-browsers',
    PORTAL_RETRY_BACKEND_OUTPUT=str(out / 'artifacts'))
argv = ['nix', 'develop', '--no-update-lock-file', '--command', 'go', '-C', 'portal',
        'test', '-mod=readonly', './internal/web', '-run', '^TestRetryBackendBrowser$',
        '-count=1', '-json', '-timeout=360s']
start = time.monotonic()
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
with (out / 'stdout.jsonl').open('w') as stdout, (out / 'stderr.log').open('w') as stderr:
    proc = subprocess.run(argv, cwd=worktree, env=environment, stdout=stdout, stderr=stderr)
after = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=worktree, text=True).strip()
clean = not subprocess.check_output(['git', 'status', '--porcelain'], cwd=worktree)
passed, failed, skipped = set(), [], []
for line in (out / 'stdout.jsonl').read_text().splitlines():
    try:
        event = json.loads(line)
    except json.JSONDecodeError:
        continue
    if event.get('Action') == 'pass' and 'Test' in event:
        passed.add(event['Test'])
    if event.get('Action') == 'fail':
        failed.append(event.get('Test', 'package'))
    if event.get('Action') == 'skip':
        skipped.append(event.get('Test', 'package'))
variants = ['desktop-root', 'desktop-member', 'mobile-root', 'mobile-member']
cases = ['policy-scope', 'policy-stale-and-lost-reply', 'scheduled-now', 'stop-and-stale-token',
         'unknown-and-confirmed', 'terminal-dismissal', 'footer-refresh', 'optional-unavailable-manual']
required_tests = {'TestRetryBackendBrowser'} | {'TestRetryBackendBrowser/' + name for name in variants}
missing = sorted(required_tests - passed)
case_errors, manifests = [], {}
for name in variants:
    try:
        manifest = json.loads((out / 'artifacts' / name / 'manifest.json').read_text())
        manifests[name] = manifest['cases']
        if manifest['name'] != name or manifest['cases'] != cases:
            case_errors.append(name + ': incomplete or duplicate case manifest')
    except (OSError, ValueError, KeyError) as error:
        case_errors.append(name + ': ' + str(error))
result = {'command': argv, 'cwd': str(worktree), 'startedAt': started,
          'elapsed': time.monotonic() - start, 'actualExit': proc.returncode,
          'before': head, 'after': after, 'clean': clean, 'missingTests': missing,
          'failed': failed, 'skipped': skipped, 'caseErrors': case_errors, 'manifests': manifests,
          'requiredCaseCount': 32,
          'pass': proc.returncode == 0 and after == expected and clean and
                  not missing and not failed and not skipped and not case_errors}
(out / 'result.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result), flush=True)
sys.exit(0 if result['pass'] else (proc.returncode or 1))
