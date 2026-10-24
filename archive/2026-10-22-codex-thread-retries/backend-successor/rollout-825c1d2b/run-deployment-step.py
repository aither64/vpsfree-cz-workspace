#!/usr/bin/env python3
"""Lead-only exact named-generation deployment steps, one explicit step per run."""
import json
import os
from pathlib import Path
import subprocess
import sys
import time

TRACK = Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-codex-thread-retries')
BASE = TRACK / 'backend-successor/rollout-825c1d2b'
RELEASE = json.loads((BASE / 'deployment-release.json').read_text())
assert RELEASE['activationAuthorized'] is True
GROUP = Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries')
C, W = GROUP / 'vpsfree-cz-configuration', GROUP / 'workspace'
CLAIM = '201af6c8-08a2-48e6-be3e-b69ce916eee1'
MACHINE = 'cz.vpsfree/machines/aitherdev'
step = sys.argv[1]
assert step in ('copy', 'dry-activate', 'system-switch', 'profile-switch', 'status', 'health-inventory', 'health-check')
b = json.loads((TRACK / RELEASE['abResult']).read_text())
composed = json.loads((TRACK / RELEASE['composedResult']).read_text())
assert b['result'] == composed['result'] == 'passed'
assert b['head'] == RELEASE['B']['head']
generation = composed['generation']
env = os.environ.copy()
env.update(DEV_SESSION_SLUG='2026-10-22-codex-thread-retries', DEV_SESSION_WORKSPACE='/home/aither/workspace/ai/vpsfree.cz',
           DEV_WORKSPACE_CLAIM_ID=CLAIM, CONFCTL_TTY='0', BUNDLE_GEMFILE=str(C / 'Gemfile'),
           BUNDLE_APP_CONFIG=str(C / '.bundle'), BUNDLE_PATH=str(C / '.gems'))
os.umask(0o077)
RUN = TRACK / RELEASE['run']
RUN.mkdir(exist_ok=True)
assert not (RUN / (step + '.command.json')).exists(), 'Step already attempted; reconcile original effects before another attempt'
current = subprocess.check_output(['dev-session', 'current'], cwd=TRACK, env=env, text=True).strip()
assert current == env['DEV_SESSION_SLUG']
for source, expected in [(W, RELEASE['W']['head']), (C, RELEASE['C']['head'])]:
    assert subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=source, text=True).strip() == expected
    assert not subprocess.check_output(['git', 'status', '--porcelain'], cwd=source, text=True).strip()
claim = json.loads(subprocess.check_output(['dev-session', 'coordination', 'claim-status', current, '--as-is', '--id', CLAIM, '--json'], cwd=TRACK, env=env, text=True))
assert claim['state'] == 'held' and claim['ownerId'] == '7cbe38cb-30c7-452d-8015-3907552c550d'
assert claim['resources'] == ['machine:vpsfree:aitherdev']
(RUN / (step + '.claim.json')).write_text(json.dumps(claim, indent=2) + '\n')
prefix = ['nix', 'develop', str(C), '-c', 'confctl', '--color', 'never']
cwd = C
if step in ('copy', 'dry-activate', 'system-switch'):
    args = prefix + ['deploy', '--yes', '--generation', generation]
    if step == 'copy':
        args += ['--copy-only']
    args += ['--no-reboot', MACHINE, 'dry-activate' if step == 'dry-activate' else 'switch']
elif step == 'profile-switch':
    args, cwd = ['workspace-host', 'switch', '--source', str(W)], TRACK
elif step == 'status':
    args = prefix + ['status', '--yes', '--generation', generation, MACHINE]
elif step == 'health-inventory':
    args = prefix + ['ls', '--output', 'name,checks', MACHINE]
else:
    args = prefix + ['health-check', '--yes', '--max-jobs', '2', MACHINE]
record = {'command': args, 'cwd': str(cwd), 'generation': generation, 'expectedSystem': composed['toplevel'],
          'expectedProfile': composed['profile'], 'environment': {k:env[k] for k in ('DEV_SESSION_SLUG','DEV_SESSION_WORKSPACE','DEV_WORKSPACE_CLAIM_ID','CONFCTL_TTY','BUNDLE_GEMFILE','BUNDLE_APP_CONFIG','BUNDLE_PATH')}}
(RUN / (step + '.command.json')).write_text(json.dumps(record, indent=2) + '\n')
started = time.monotonic()
with (RUN / (step + '.stdout')).open('wb') as out, (RUN / (step + '.stderr')).open('wb') as err:
    result = subprocess.run(args, cwd=cwd, env=env, stdout=out, stderr=err)
status = {'step':step, 'exit':result.returncode, 'elapsed':time.monotonic()-started}
(RUN / (step + '.status.json')).write_text(json.dumps(status, indent=2) + '\n')
print(json.dumps(status), flush=True)
print((RUN / (step + '.stdout')).read_text()[-4000:])
if result.returncode:
    print((RUN / (step + '.stderr')).read_text()[-4000:], file=sys.stderr)
sys.exit(result.returncode)
