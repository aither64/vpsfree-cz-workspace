"""Prepared operation wrapper. Only the lead-selected fresh watcher executes it."""
import datetime
import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESSION = HERE.parent
WORKSPACE = Path('/home/aither/workspace/ai/vpsfree.cz')
REPO = WORKSPACE / 'worktrees/2026-10-22-codex-thread-retries/dev-workspace'
EXPECTED = '45e14be3d34a9ca2d3b418c310da927351b7f330'
EXPECTED_TREE = 'edb3f41dec072a44e03a4f4a7a4c4e8894b440f4'
ORIGINAL_MANIFEST_HASH = 'bca462b87f4062b053bd86273faaf92799b0a5693e8a87d3cec6e7064a85c642'
OUTPUT = SESSION / 'backend-successor/I-B1/accepted-fork-attempt-2'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def identity():
    return subprocess.check_output(
        ['git', '-C', str(REPO), 'rev-parse', 'HEAD', 'HEAD^{tree}'], text=True
    ).splitlines()


def clean():
    return not subprocess.check_output(['git', '-C', str(REPO), 'status', '--porcelain'])


def guard_fixtures(brief):
    return {name: digest(REPO / name) for name in brief['owned_files']}


def write_receipt(receipt):
    (OUTPUT / 'result.json').write_text(json.dumps(receipt, indent=2) + '\n')


def main():
    # Read-only guards only. Never repair a source/ref/env mismatch or reuse an
    # output directory: uncertainty returns to the lead without launching tests.
    actual_env = [os.environ.get(k) for k in ('DEV_SESSION_SLUG', 'DEV_SESSION_WORKSPACE')]
    expected_env = ['2026-10-22-codex-thread-retries', str(WORKSPACE)]
    if actual_env not in ([None, None], expected_env):
        raise RuntimeError('session environment does not match the bound session')
    current = subprocess.check_output(['dev-session', 'current'], cwd=SESSION, text=True).strip()
    if current != expected_env[0]:
        raise RuntimeError('dev-session current does not match the bound session')
    if os.environ.get('CGO_ENABLED', '').strip() not in ('', '1'):
        raise RuntimeError('CGO_ENABLED must remain enabled/default; no cgo workaround authorized')
    original_path = HERE / 'watcher-brief.json'
    if digest(original_path) != ORIGINAL_MANIFEST_HASH:
        raise RuntimeError('original immutable manifest changed')
    original = json.loads(original_path.read_text())
    brief_path = HERE / 'accepted-fork-2-brief.json'
    brief = json.loads(brief_path.read_text())
    command = list(original['argv'])
    command.insert(command.index('-c'), 'nixpkgs#gcc')
    if command != brief['argv'] or brief['cwd'] != str(REPO / 'portal'):
        raise RuntimeError('attempt2 differs from the authorized GCC-only command correction')
    if brief['head'] != EXPECTED or brief['tree'] != EXPECTED_TREE:
        raise RuntimeError('attempt2 source binding changed')
    if (brief['required_leaf_tests'] != original['required_leaf_tests'] or
            brief['expected_leaf_count'] != original['expected_leaf_count'] or original['expected_leaf_count'] != 21):
        raise RuntimeError('required leaf manifest changed')
    required = original['required_leaf_tests']
    if len(required) != 21 or len(set(required)) != 21 or command[-1] != '-json' or '-timeout=45s' not in command:
        raise RuntimeError('required exact manifest/timeout/JSON invariant changed')
    expected_files = {name: metadata['sha256'] for name, metadata in original['owned_files'].items()}
    before_files = guard_fixtures(original)
    if before_files != expected_files or brief['owned_files'] != original['owned_files']:
        raise RuntimeError('original reviewed fixture bytes changed')
    if identity() != [EXPECTED, EXPECTED_TREE] or not clean():
        raise RuntimeError('source HEAD/tree/clean guard failed')
    preservation = json.loads((HERE / 'accepted-fork-2-preservation.json').read_text())
    for name, expected_hash in preservation.items():
        if digest(SESSION / name) != expected_hash:
            raise RuntimeError('original attempt1/packet evidence changed: ' + name)
    # mkdir is the unique operation claim; nothing precreates or overwrites it.
    OUTPUT.mkdir(exist_ok=False)
    started = time.monotonic()
    receipt = {
        'status': 'running', 'command': command, 'cwd': brief['cwd'],
        'startedAt': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'before': EXPECTED, 'beforeTree': EXPECTED_TREE, 'beforeClean': True,
        'beforeFixtureHashes': before_files, 'scriptSHA256': digest(Path(__file__)),
        'briefSHA256': digest(brief_path), 'originalManifestSHA256': ORIGINAL_MANIFEST_HASH,
        'environment': {name: os.environ.get(name) for name in ('CGO_ENABLED', 'CC', 'CXX', 'GOFLAGS')},
        'requiredLeafCount': 21, 'actualExit': None,
    }
    write_receipt(receipt)
    try:
        with (OUTPUT / 'stdout.jsonl').open('x') as stdout, (OUTPUT / 'stderr.log').open('x') as stderr:
            result = subprocess.run(command, cwd=brief['cwd'], stdout=stdout, stderr=stderr)
        # Preserve the raw process result separately before any post-checks.
        receipt['actualExit'] = result.returncode
        receipt['commandElapsed'] = time.monotonic() - started
        (OUTPUT / 'exit.json').write_text(json.dumps({
            'actualExit': result.returncode, 'elapsed': receipt['commandElapsed'],
        }, indent=2) + '\n')
        write_receipt(receipt)
        after, after_tree = identity()
        after_clean = clean()
        after_files = guard_fixtures(original)
        passed, run, package_pass = set(), set(), False
        skipped, failed, invalid = [], [], []
        for line_no, line in enumerate((OUTPUT / 'stdout.jsonl').read_text().splitlines(), 1):
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                invalid.append(line_no)
                continue
            action, test = event.get('Action'), event.get('Test')
            if action == 'run' and test:
                run.add(test)
            if action == 'pass':
                if test:
                    passed.add(test)
                elif event.get('Package') == 'github.com/aither64/dev-workspace/portal/internal/web':
                    package_pass = True
            if action == 'skip':
                skipped.append(test or 'package')
            if action == 'fail' or action == 'build-fail':
                failed.append(test or event.get('ImportPath') or 'package')
        missing = sorted(set(required) - passed)
        missing_run = sorted(set(required) - run)
        missing_top = sorted(set(brief['required_top_level_tests']) - passed)
        preserved = all(digest(SESSION / name) == h for name, h in preservation.items())
        passed_all = (result.returncode == 0 and package_pass and not missing and not missing_run and
                      not missing_top and not skipped and not failed and not invalid and
                      after == EXPECTED and after_tree == EXPECTED_TREE and after_clean and
                      after_files == expected_files and preserved)
        receipt.update({
            'status': 'completed', 'elapsed': time.monotonic() - started,
            'after': after, 'afterTree': after_tree, 'clean': after_clean,
            'afterFixtureHashes': after_files, 'originalEvidenceUnchanged': preserved,
            'missingRequiredCases': missing, 'missingRunCases': missing_run,
            'missingTopLevelCases': missing_top, 'skipped': skipped, 'failed': failed,
            'invalidJSONLineNumbers': invalid, 'passedTestsAndSubtests': len(passed),
            'passed': sorted(passed), 'packagePass': package_pass, 'pass': passed_all,
        })
        write_receipt(receipt)
        print(json.dumps(receipt), flush=True)
        return 0 if passed_all else (result.returncode or 1)
    except BaseException as error:
        receipt.update(status='incomplete', elapsed=time.monotonic() - started,
                       collectorError=type(error).__name__ + ': ' + str(error), **{'pass': False})
        write_receipt(receipt)
        raise


if __name__ == '__main__':
    sys.exit(main())
