import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path('/home/aither/workspace/ai/vpsfree.cz')
OUT = ROOT / 'work/2026-10-20-portal-citation-deployment'
SLUG = '2026-10-20-portal-citation-deployment'
CFG = ROOT / 'worktrees' / SLUG / 'vpsfree-cz-configuration'
WS = ROOT / 'worktrees' / SLUG / 'workspace'
CLAIM = json.loads((OUT / 'machine-claim-request.json').read_text())['requestId']
ARTIFACTS = json.loads((OUT / 'rebased-artifacts.json').read_text())
ENV = dict(os.environ, DEV_SESSION_SLUG=SLUG, DEV_SESSION_WORKSPACE=str(ROOT),
           DEV_WORKSPACE_CLAIM_ID=CLAIM,
           BUNDLE_PATH=str(ROOT / 'worktrees/2026-10-20-portal-citation-investigation/vpsfree-cz-configuration/.gems'))


def run(command, cwd, log_name):
    with (OUT / log_name).open('w') as log:
        subprocess.run(command, cwd=cwd, env=ENV, stdout=log, stderr=subprocess.STDOUT, check=True)


phase = 'preflight'
started = time.time()
try:
    claim = json.loads(subprocess.check_output([
        'dev-session', 'coordination', 'claim-status', SLUG, '--as-is', '--id', CLAIM, '--json'],
        cwd=ROOT, env=ENV, text=True))
    assert claim['state'] == 'held'
    assert 'vpsfree:aitherdev' in claim['resources'] or 'machine:vpsfree:aitherdev' in claim['resources']
    assert subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=CFG, text=True).strip() == ARTIFACTS['configurationRevision']
    assert subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=WS, text=True).strip() == ARTIFACTS['workspaceRevision']
    assert not subprocess.check_output(['git', 'status', '--porcelain'], cwd=CFG, text=True)
    assert not subprocess.check_output(['git', 'status', '--porcelain'], cwd=WS, text=True)
    phase = 'system'
    run(['nix', 'develop', '--command', 'confctl', 'deploy', '--generation', ARTIFACTS['generationName'],
         '--dry-activate-first', '--enable-auto-rollback', '--no-reboot', '--yes',
         'cz.vpsfree/machines/aitherdev', 'switch'], CFG, 'rebase-system-activate.log')
    assert os.path.realpath('/run/current-system') == ARTIFACTS['system']
    assert os.path.realpath('/nix/var/nix/profiles/system') == ARTIFACTS['system']
    if '--system-only' in sys.argv:
        result = {'result': 'passed', 'phase': 'system_complete', 'system': ARTIFACTS['system'], 'claimId': CLAIM}
        (OUT / 'rebase-system-activation-result.json').write_text(json.dumps(result, indent=2) + '\n')
        print(json.dumps(result))
        sys.exit(0)
    phase = 'profile'
    run(['workspace-host', 'switch', '--source', str(WS)], ROOT, 'rebase-profile-activate.log')
    assert os.path.realpath('/home/aither/.local/state/dev-workspaces/profile') == ARTIFACTS['application']
    phase = 'complete'
    result = {'result': 'passed', 'phase': phase, 'elapsedSeconds': round(time.time() - started),
              'claimId': CLAIM, 'system': ARTIFACTS['system'], 'application': ARTIFACTS['application']}
except Exception as error:
    result = {'result': 'failed', 'phase': phase, 'elapsedSeconds': round(time.time() - started),
              'claimId': CLAIM, 'error': str(error)}
    (OUT / 'rebase-activation-result.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result))
    raise
(OUT / 'rebase-activation-result.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result))
