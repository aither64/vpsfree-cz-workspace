import fcntl
import json
import os
from pathlib import Path
import subprocess

ROOT = Path('/home/aither/workspace/ai/vpsfree.cz')
OUT = ROOT / 'work/2026-10-20-portal-citation-deployment'
SOURCE = '2026-10-20-portal-citation-investigation'
CLAIM = '4b9cd663-80c6-49e7-ab71-93374477d298'
ENV = dict(os.environ, DEV_SESSION_SLUG=SOURCE, DEV_SESSION_WORKSPACE=str(ROOT),
           BUNDLE_PATH=str(ROOT / 'worktrees' / SOURCE / 'vpsfree-cz-configuration/.gems'))
INVENTORY = json.loads((ROOT / 'work' / SOURCE / 'premerge-final-inventory.json').read_text())
CONFIGURATION = ROOT / 'worktrees' / SOURCE / 'vpsfree-cz-configuration'
results = []


def git(name, cwd, *args, capture=False):
    command = ['git', '-C', str(cwd), *args]
    if name == 'vpsfree-cz-configuration' and not capture:
        command = ['nix', 'develop', str(CONFIGURATION), '--command', 'env',
                   'BUNDLE_PATH=' + ENV['BUNDLE_PATH'], *command]
    if capture:
        return subprocess.check_output(command, cwd=ROOT, env=ENV, text=True).strip()
    with (OUT / ('merge-' + name + '.log')).open('a') as log:
        subprocess.run(command, cwd=CONFIGURATION if name == "vpsfree-cz-configuration" else ROOT, env=ENV, stdout=log, stderr=subprocess.STDOUT, check=True)


assert json.loads((OUT / 'final-live-browser-result.json').read_text())['result'] == 'passed'
assert json.loads((OUT / 'rebase-live-history-result.json').read_text())['result'] == 'passed'
assert json.loads((OUT / 'title-activation-result.json').read_text())['result'] == 'passed'
status = json.loads(subprocess.check_output([
    'dev-session', 'coordination', 'claim-status', SOURCE, '--as-is', '--id', CLAIM, '--json'],
    cwd=ROOT, env=ENV, text=True))
assert status['state'] == 'held'

for name, value in INVENTORY.items():
    feature = ROOT / 'worktrees' / SOURCE / name
    assert git(name, feature, 'rev-parse', 'HEAD', capture=True) == value['head']
    assert not git(name, feature, 'status', '--porcelain', capture=True)
    expected_base = value['base']
    if name == 'workspace':
        assert git(name, ROOT, 'rev-parse', 'HEAD', capture=True) == expected_base
    else:
        assert git(name, feature, 'rev-parse', 'origin/master', capture=True) in {expected_base, value['head']}

try:
    for name in ['codex-web', 'dev-workspace', 'vpsfree-cz-configuration']:
        value = INVENTORY[name]
        feature = ROOT / 'worktrees' / SOURCE / name
        remote_before = git(name, feature, 'ls-remote', 'origin', 'refs/heads/master', capture=True).split()[0]
        if remote_before == value['head']:
            results.append({'repository': name, 'head': value['head'], 'remoteHead': remote_before, 'result': 'integrated', 'alreadyVerified': True})
            continue
        assert remote_before == value['base']
        target = ROOT / 'worktrees' / SOURCE / ('integration-' + name)
        assert not target.exists()
        git(name, feature, 'worktree', 'add', str(target), 'master')
        git(name, target, 'merge', '--ff-only', 'origin/master')
        git(name, target, 'merge', '--ff-only', value['head'])
        assert git(name, target, 'rev-parse', 'HEAD', capture=True) == value['head']
        assert not git(name, target, 'status', '--porcelain', capture=True)
        git(name, target, 'push', 'origin', 'master:refs/heads/master')
        remote = git(name, target, 'ls-remote', 'origin', 'refs/heads/master', capture=True).split()[0]
        assert remote == value['head']
        results.append({'repository': name, 'head': value['head'], 'remoteHead': remote, 'result': 'integrated'})
        (OUT / 'integration-progress.json').write_text(json.dumps(results, indent=2) + '\n')
        git(name, feature, 'worktree', 'remove', str(target))

    name = 'workspace'
    value = INVENTORY[name]
    with (ROOT / '.git/dev-session-tracking.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        assert git(name, ROOT, 'rev-parse', 'HEAD', capture=True) == value['base']
        assert not git(name, ROOT, 'status', '--porcelain', '--', 'flake.nix', 'flake.lock', capture=True)
        git(name, ROOT, 'merge', '--ff-only', value['head'])
        assert git(name, ROOT, 'rev-parse', 'HEAD', capture=True) == value['head']
        git(name, ROOT, 'push', 'origin', 'master:refs/heads/master')
        remote = git(name, ROOT, 'ls-remote', 'origin', 'refs/heads/master', capture=True).split()[0]
        assert remote == value['head']
        results.append({'repository': name, 'head': value['head'], 'remoteHead': remote, 'result': 'integrated'})
        (OUT / 'integration-progress.json').write_text(json.dumps(results, indent=2) + '\n')
    result = {'result': 'passed', 'repositories': results, 'featureRefsRetained': True}
except Exception as error:
    result = {'result': 'failed', 'repositories': results, 'error': str(error)}
    (OUT / 'integration-result.json').write_text(json.dumps(result, indent=2) + '\n')
    raise
(OUT / 'integration-result.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result))
