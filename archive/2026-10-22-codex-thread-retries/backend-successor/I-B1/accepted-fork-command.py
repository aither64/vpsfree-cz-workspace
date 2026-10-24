import datetime
import hashlib
import json
import subprocess
import sys
import time
from pathlib import Path

tracking = Path(__file__).resolve().parent
session = tracking.parents[1]
repo = Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries/dev-workspace')
expected = '45e14be3d34a9ca2d3b418c310da927351b7f330'
expected_tree = 'edb3f41dec072a44e03a4f4a7a4c4e8894b440f4'

def identity():
    return subprocess.check_output(['git', '-C', str(repo), 'rev-parse', 'HEAD', 'HEAD^{tree}'], text=True).splitlines()

assert identity() == [expected, expected_tree]
assert not subprocess.check_output(['git', '-C', str(repo), 'status', '--porcelain'])
brief = json.loads((session / 'accepted-fork-source-lock/watcher-brief.json').read_text())
for name, metadata in brief['owned_files'].items():
    assert hashlib.sha256((repo / name).read_bytes()).hexdigest() == metadata['sha256']
command = brief['argv']
assert command[-1] == '-json' and '-timeout=45s' in command
assert brief['cwd'] == str(repo / 'portal')
output = tracking / 'accepted-fork-attempt-1'
output.mkdir(exist_ok=False)
started = time.monotonic()
receipt = {
    'status': 'running', 'command': command, 'cwd': brief['cwd'],
    'startedAt': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'before': expected, 'beforeTree': expected_tree,
}
(output / 'result.json').write_text(json.dumps(receipt, indent=2) + '\n')
with (output / 'stdout.jsonl').open('x') as stdout, (output / 'stderr.log').open('x') as stderr:
    result = subprocess.run(command, cwd=brief['cwd'], stdout=stdout, stderr=stderr)
after, after_tree = identity()
clean = not subprocess.check_output(['git', '-C', str(repo), 'status', '--porcelain'])
passed = set()
skipped, failed = [], []
for line in (output / 'stdout.jsonl').read_text().splitlines():
    try:
        event = json.loads(line)
    except json.JSONDecodeError:
        continue
    if event.get('Action') == 'pass' and 'Test' in event:
        passed.add(event['Test'])
    if event.get('Action') == 'skip':
        skipped.append(event.get('Test', 'package'))
    if event.get('Action') == 'fail':
        failed.append(event.get('Test', 'package'))
missing = sorted(set(brief['required_leaf_tests']) - passed)
receipt.update({
    'status': 'completed', 'actualExit': result.returncode,
    'elapsed': time.monotonic() - started, 'after': after, 'afterTree': after_tree,
    'clean': clean, 'requiredLeafCount': brief['expected_leaf_count'],
    'missingRequiredCases': missing, 'skipped': skipped, 'failed': failed,
    'passedTestsAndSubtests': len(passed),
    'pass': result.returncode == 0 and not missing and not skipped and not failed
            and after == expected and after_tree == expected_tree and clean,
})
(output / 'result.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps(receipt), flush=True)
sys.exit(0 if receipt['pass'] else (result.returncode or 1))
