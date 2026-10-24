from pathlib import Path
import json
import os
import shlex
import subprocess
import time

p = Path(__file__).resolve().parent
r = json.loads((p / 'deployment-release.json').read_text())
assert r['recoveryAuthorized']
run = Path((p / 'private-run-path.txt').read_text().strip())
assert not (run / 'command.json').exists()
os.umask(0o077)
args = [r['outputs']['profile'] + '/bin/workspace-host',
        'recover-failed-creation-delete', '--source', r['W']['worktree'],
        '--workspace', 'vpsfree-cz', '--session',
        '2026-10-24-flake-update-downgrade-guard', '--request-id',
        '625e1f52-0a41-4127-80c4-bc058fdbfa45']
env = os.environ.copy()
env.update(DEV_SESSION_SLUG='2026-10-22-codex-thread-retries',
           DEV_SESSION_WORKSPACE='/home/aither/workspace/ai/vpsfree.cz',
           DEV_WORKSPACE_CLAIM_ID='201af6c8-08a2-48e6-be3e-b69ce916eee1')
assert subprocess.check_output(['dev-session', 'current'], env=env,
                               text=True).strip() == env['DEV_SESSION_SLUG']
claim = json.loads(subprocess.check_output([
    'dev-session', 'coordination', 'claim-status', env['DEV_SESSION_SLUG'],
    '--as-is', '--id', env['DEV_WORKSPACE_CLAIM_ID'], '--json'], env=env))
assert claim['state'] == 'held'
assert claim['ownerId'] == '7cbe38cb-30c7-452d-8015-3907552c550d'
assert claim['resources'] == ['machine:vpsfree:aitherdev']
for key in ['W', 'C']:
    d = r[key]
    assert subprocess.check_output(['git', '-C', d['worktree'], 'rev-parse',
                                    'HEAD'], text=True).strip() == d['head']
    assert not subprocess.check_output(['git', '-C', d['worktree'], 'status',
                                       '--porcelain'], text=True).strip()
(run / 'command.json').write_text(json.dumps({
    'argv': args, 'originalOperation': r['operation']['id'],
    'environment': {k: env[k] for k in ['DEV_SESSION_SLUG',
                    'DEV_SESSION_WORKSPACE', 'DEV_WORKSPACE_CLAIM_ID']}
}, indent=2) + '\n')
started = time.monotonic()
print('Public candidate recovery started; raw transcript private', flush=True)
with (run / 'script.stderr').open('wb') as err:
    result = subprocess.run([
        'script', '--quiet', '--return', '--flush', '--log-out',
        str(run / 'recovery.terminal'), '--command', shlex.join(args)
    ], env=env, stdout=subprocess.DEVNULL, stderr=err)
status = {'step': 'same-operation-public-recovery', 'exit': result.returncode,
          'elapsed': time.monotonic() - started,
          'originalOperation': r['operation']['id']}
(run / 'status.json').write_text(json.dumps(status, indent=2) + '\n')
(p / 'recovery-interactive.status.json').write_text(
    json.dumps(status, indent=2) + '\n')
print(json.dumps(status), flush=True)
raise SystemExit(result.returncode)
