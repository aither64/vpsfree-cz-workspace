from pathlib import Path
import hashlib
import json
import os
import subprocess
import time

packet = Path(__file__).resolve().parent
repo = Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries/dev-workspace')
release = json.loads((packet / 'native-release.json').read_text())
assert release['reviewAccepted'] and not release['executionHeld']
for key, expected in [('DEV_SESSION_SLUG', '2026-10-22-codex-thread-retries'),
                      ('DEV_SESSION_WORKSPACE', '/home/aither/workspace/ai/vpsfree.cz')]:
    assert key not in os.environ or os.environ[key] == expected
assert subprocess.check_output(['dev-session', 'current'], text=True).strip() == '2026-10-22-codex-thread-retries'
native = Path(release['native'])
assert hashlib.sha256(native.read_bytes()).hexdigest() == release['nativeSHA256']
assert hashlib.sha256((native.parent.parent / 'libexec/codex/bin/codex').read_bytes()).hexdigest() == release['underlyingSHA256']
expected_inputs = json.loads((packet / 'native-input-fix/inputs-before.json').read_text())

def identity():
    for selector, value in [('HEAD', release['B']['head']), ('HEAD^{tree}', release['B']['tree'])]:
        assert subprocess.check_output(['git', '-C', str(repo), 'rev-parse', selector], text=True).strip() == value
    assert not subprocess.check_output(['git', '-C', str(repo), 'status', '--porcelain'], text=True).strip()
    actual = {name: hashlib.sha256((repo / name).read_bytes()).hexdigest() for name in expected_inputs}
    assert actual == expected_inputs
    return actual

before = identity()
os.umask(0o077)
run = packet / release['run']
run.mkdir()
args = ['nix', 'develop', str(repo), '-c', 'env', 'GOFLAGS=', 'GOWORK=off',
        'LIVE_SWITCH_CODEX=' + str(native), 'go', '-C', 'portal', 'test', '-mod=readonly',
        '-tags=live_switch_integration', './cmd/workspace-portal', '-run',
        '^' + release['case'] + '$', '-count=1', '-timeout=120s', '-json']
(run / 'command.json').write_text(json.dumps({'argv': args, 'cwd': str(repo),
    'head': release['B']['head'], 'native': release['native'], 'nativeSHA256': release['nativeSHA256']}, indent=2) + '\n')
(run / 'inputs-before.json').write_text(json.dumps(before, indent=2) + '\n')
started = time.monotonic()
with (run / 'stdout.jsonl').open('xb') as out, (run / 'stderr').open('xb') as err:
    result = subprocess.run(args, cwd=repo, stdout=out, stderr=err)
after = identity()
(run / 'inputs-after.json').write_text(json.dumps(after, indent=2) + '\n')
events = [json.loads(line) for line in (run / 'stdout.jsonl').read_text().splitlines() if line.startswith('{')]
passes = [e for e in events if e.get('Action') == 'pass' and e.get('Test') == release['case']]
bad = [e for e in events if e.get('Action') in ('fail', 'build-fail', 'skip')]
accepted = result.returncode == 0 and len(passes) == 1 and not bad
receipt = {'result': 'passed' if accepted else 'failed', 'exit': result.returncode,
           'elapsed': time.monotonic() - started, 'head': release['B']['head'],
           'case': release['case'], 'passes': len(passes), 'bad': bad,
           'inputsUnchanged': before == after, 'inputCount': len(before)}
(run / 'result.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps(receipt), flush=True)
raise SystemExit(0 if accepted else 1)
