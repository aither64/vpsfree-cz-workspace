#!/usr/bin/env python3
"""Lead read-only continuity/health receipt after the authorized profile switch."""
import json
from pathlib import Path
import subprocess
import time

TRACK = Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-codex-thread-retries')
BASE = TRACK / 'incident2-prepared-plan'
release = json.loads((BASE / 'deployment-release.json').read_text())
assert release['activationAuthorized'] is True
composed = json.loads((TRACK / release['composedResult']).read_text())
before = json.loads((BASE / 'preactivation-baseline.json').read_text())
old_team = json.loads((BASE / 'preactivation-team.json').read_text())
assert subprocess.check_output(['dev-session', 'current'], cwd=TRACK, text=True).strip() == '2026-10-22-codex-thread-retries'
services = []
for old in before['services']:
    raw = subprocess.check_output(['systemctl', '--user', 'show', old['Id'], '--property=Id,ActiveState,SubState,MainPID,NRestarts,ExecMainStartTimestampMonotonic,ExecMainStatus'], text=True)
    row = dict(line.split('=', 1) for line in raw.splitlines() if '=' in line)
    assert row['ActiveState'] == 'active' and row['SubState'] == 'running', row
    process = Path('/proc') / row['MainPID']
    row['processExe'] = str((process / 'exe').resolve())
    row['processStartTicks'] = (process / 'stat').read_text().rsplit(')', 1)[1].split()[19]
    if old['Id'] in ('workspace-codex@vpsfree-cz.service', 'workspace-tmux@vpsfree-cz.service'):
        for key in ('MainPID', 'processExe', 'processStartTicks'):
            assert row[key] == old[key], (old['Id'], key, old[key], row[key])
    if old['Id'] in ('workspace-router.service', 'workspace-portal@vpsfree-cz.service'):
        assert row['processExe'] == str(Path(composed['profile']) / 'bin/workspace-portal'), row
    services.append(row)
for name, old in before['sockets'].items():
    st = Path(old['path']).stat()
    assert (st.st_dev, st.st_ino) == (old['device'], old['inode']), name
team = json.loads(subprocess.check_output(['dev-session', 'team', 'list', '2026-10-22-codex-thread-retries', '--as-is'], cwd=TRACK, text=True))['roster']
projected = {key: team[key] for key in ('slug', 'workspace', 'rootThreadId', 'catalogDigest')}
projected['members'] = [{key: member[key] for key in ('address', 'threadId', 'state', 'model', 'reasoningEffort', 'access')} for member in team['members']]
assert projected == old_team
profile = str(Path('/home/aither/.local/state/dev-workspaces/profile').resolve())
system = str(Path('/run/current-system').resolve())
system_profile = str(Path('/nix/var/nix/profiles/system').resolve())
assert profile == composed['profile']
assert system == system_profile == composed['toplevel']
health = {}
for label, socket in [('portal', '/run/user/1000/dev-workspaces/vpsfree-cz/portal.sock'), ('router', '/run/dev-workspaces/router.sock')]:
    body = subprocess.check_output(['curl', '--fail', '--silent', '--show-error', '--max-time', '10', '--unix-socket', socket, '-H', 'Host: vpsfree-cz.workspace.aitherdev.int.vpsfree.cz', 'http://localhost/healthz'], text=True)
    health[label] = json.loads(body)
    assert health[label] == {'ok': True}
result = {'observedAtUnix': time.time(), 'profile': profile, 'system': system, 'systemProfile': system_profile, 'services': services, 'nativeTmuxProcessesAndSocketsPreserved': True, 'retainedRootMemberIdentitiesAndSettingsPreserved': True, 'health': health, 'limits': 'No injected browser submission or native delivery claim; user original-request recovery remains to confirm.'}
(BASE / 'postactivation-continuity.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
