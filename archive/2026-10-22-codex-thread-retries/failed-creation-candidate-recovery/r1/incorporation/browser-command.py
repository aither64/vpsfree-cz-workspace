#!/usr/bin/env python3
"""Preparation only: lead-selected fresh watcher owns the one actual batch."""
from pathlib import Path
import datetime
import hashlib
import json
import os
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
SESSION = HERE.parents[2]
REPO = Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries/dev-workspace')
HEAD = 'f75f79e545c29ec9e741d33504c3ce741a3a9dd4'
TREE = 'c3f0b49b920ad4d8778f711014cb37dba4296e4c'
OUT = HERE / 'browser-attempt-7'

def identity():
    return subprocess.check_output(['git', 'rev-parse', 'HEAD', 'HEAD^{tree}'], cwd=REPO, text=True).splitlines()

def clean():
    return not subprocess.check_output(['git', 'status', '--porcelain'], cwd=REPO)

def write(path, value):
    path.write_text(json.dumps(value, indent=2) + '\n')

def main():
    markers = [os.getenv('DEV_SESSION_SLUG'), os.getenv('DEV_SESSION_WORKSPACE')]
    if markers not in ([None, None], ['2026-10-22-codex-thread-retries', '/home/aither/workspace/ai/vpsfree.cz']):
        raise RuntimeError('wrong session environment')
    current = subprocess.check_output(['dev-session', 'current'], cwd=SESSION, text=True).strip()
    if current != '2026-10-22-codex-thread-retries' or identity() != [HEAD, TREE] or not clean():
        raise RuntimeError('session/source/clean guard failed')
    if os.getenv('CGO_ENABLED', '').strip() not in ('', '1'):
        raise RuntimeError('cgo must remain enabled/default')
    browser_manifest = json.loads((SESSION / 'backend-browser/case-manifest.json').read_text())
    assert len(browser_manifest['all32']) == 32
    variants, cases = browser_manifest['variants'], browser_manifest['cases']
    browser_tests = {'TestRetryBackendBrowser'} | {'TestRetryBackendBrowser/' + v for v in variants}
    env = dict(os.environ, PORTAL_BROWSER_TEST='1',
        NODE_PATH='/nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1/lib/node_modules',
        PLAYWRIGHT_BROWSERS_PATH='/nix/store/f0rap655j6wmqbfvqdw445kwcxkxwf7n-playwright-browsers',
        PORTAL_RETRY_BACKEND_OUTPUT=str(OUT / 'browser/artifacts'))
    # This child inherits the complete repository Nix shell PATH. It verifies
    # the actual tool resolution, including GCC, before launching the browser Go run.
    tool_guard = "import shutil,subprocess,sys,json; names=['go','gcc','ruby','node','git']; paths={n:shutil.which(n) for n in names}; print(json.dumps({'nixTools':paths}),file=sys.stderr,flush=True); assert all(paths.values()),paths; sys.exit(subprocess.run(sys.argv[1:]).returncode)"
    prefix = ['nix', 'develop', '--no-update-lock-file', '--command', 'python3', '-c', tool_guard]
    stages = [('browser', '^TestRetryBackendBrowser$', '360s', browser_tests)]
    OUT.mkdir(exist_ok=False)
    summary = {'head': HEAD, 'tree': TREE, 'startedAt': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'stages': [], 'pass': False}
    write(OUT / 'result.json', summary)
    started = time.monotonic()
    for name, selector, budget, required in stages:
        if identity() != [HEAD, TREE] or not clean():
            raise RuntimeError('source changed before next stage')
        directory = OUT / name
        directory.mkdir()
        argv = prefix + ['go', '-C', 'portal', 'test', '-mod=readonly', './internal/web', '-run', selector, '-count=1', '-json', '-timeout=' + budget]
        before = time.monotonic()
        with (directory / 'stdout.jsonl').open('x') as stdout, (directory / 'stderr.log').open('x') as stderr:
            result = subprocess.run(argv, cwd=REPO, env=env, stdout=stdout, stderr=stderr)
        receipt = {'stage': name, 'command': argv, 'actualExit': result.returncode, 'elapsed': time.monotonic() - before}
        write(directory / 'exit.json', receipt)
        passed, run, failed, skipped, invalid = set(), set(), [], [], []
        package_pass = False
        for number, line in enumerate((directory / 'stdout.jsonl').read_text().splitlines(), 1):
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                invalid.append(number)
                continue
            action, test = event.get('Action'), event.get('Test')
            if action == 'run' and test:
                run.add(test)
            if action == 'pass':
                if test:
                    passed.add(test)
                else:
                    package_pass = True
            if action in ('fail', 'build-fail'):
                failed.append(test or 'package')
            if action == 'skip':
                skipped.append(test or 'package')
        case_errors = []
        if name == 'browser':
            for variant in variants:
                try:
                    value = json.loads((directory / 'artifacts' / variant / 'manifest.json').read_text())
                    if value['name'] != variant or value['cases'] != cases:
                        case_errors.append(variant)
                except (OSError, ValueError, KeyError) as error:
                    case_errors.append(variant + ': ' + str(error))
        receipt.update(missing=sorted(required - passed), missingRun=sorted(required - run), failed=failed,
            skipped=skipped, invalidJSON=invalid, caseErrors=case_errors, after=identity(), clean=clean())
        receipt['pass'] = result.returncode == 0 and package_pass and not any([receipt['missing'], receipt['missingRun'], failed, skipped, invalid, case_errors]) and receipt['after'] == [HEAD, TREE] and receipt['clean']
        write(directory / 'result.json', receipt)
        summary['stages'].append(receipt)
        summary['elapsed'] = time.monotonic() - started
        write(OUT / 'result.json', summary)
    summary['pass'] = len(summary['stages']) == 1 and all(v['pass'] for v in summary['stages'])
    summary['scriptSHA256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    write(OUT / 'result.json', summary)
    print(json.dumps(summary), flush=True)
    return 0 if summary['pass'] else 1

if __name__ == '__main__':
    sys.exit(main())
