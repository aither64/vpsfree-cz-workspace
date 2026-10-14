import datetime
import json
import os
import pathlib
import subprocess

tracking = pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
systemctl = '/nix/store/khnfirshq5j299s6sfj0laxj0vr7gaa6-systemd-260.2/bin/systemctl'
loginctl = str(pathlib.Path(systemctl).with_name('loginctl'))

def properties(argv):
    result = subprocess.run(argv, check=True, capture_output=True, text=True)
    return dict(line.split('=', 1) for line in result.stdout.splitlines() if '=' in line)

assert os.getuid() == 1000
user = properties([loginctl, 'show-user', '1000', '--property=Linger', '--property=State', '--property=RuntimePath', '--property=Sessions'])
manager = properties([systemctl, 'show', 'user@1000.service', '--property=Id', '--property=ActiveState', '--property=SubState', '--property=Job', '--property=MainPID', '--property=ControlGroup'])
runtime = properties([systemctl, 'show', 'user-runtime-dir@1000.service', '--property=Id', '--property=ActiveState', '--property=SubState', '--property=Job'])
user_manager = properties([systemctl, '--user', 'show', '--property=Version', '--property=ControlGroup'])
assert user['Linger'] == 'yes' and user['RuntimePath'] == '/run/user/1000'
assert manager['ActiveState'] == 'active' and manager['SubState'] == 'running' and not manager['Job']
assert runtime['ActiveState'] == 'active' and not runtime['Job']
assert manager['ControlGroup'] == user_manager['ControlGroup'] == '/user.slice/user-1000.slice/user@1000.service'
pid = int(manager['MainPID'])
base = pathlib.Path('/proc') / str(pid)
before = (base / 'stat').read_text().rsplit(')', 1)[1].split()
native = {'pid': pid, 'uid': base.stat().st_uid, 'start_ticks': int(before[19]),
          'boot_id': pathlib.Path('/proc/sys/kernel/random/boot_id').read_text().strip(),
          'cgroup': (base / 'cgroup').read_text().strip()}
try:
    native['exe'] = os.readlink(base / 'exe')
except PermissionError:
    native['exe_unavailable'] = 'Named manager /proc exe read denied; no privilege change or guessed executable identity'
after = (base / 'stat').read_text().rsplit(')', 1)[1].split()
assert before[19] == after[19] and native['uid'] == 1000
assert native['cgroup'].split('::', 1)[1].startswith(manager['ControlGroup'] + '/')
sessions = [properties([loginctl, 'show-session', session, '--property=Id', '--property=State', '--property=Class', '--property=User'])
            for session in user['Sessions'].split()]
record = {'schema': 1, 'at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'scope': 'Read-only existing user-manager lifetime observation; no service launch or configuration mutation',
          'user': user, 'system_manager_unit': manager, 'runtime_directory_unit': runtime,
          'user_manager': user_manager, 'native_manager': native, 'sessions': sessions,
          'source': 'https://raw.githubusercontent.com/systemd/systemd/v260.5/src/login/logind-user.c',
          'reconciliation': 'user_get_state can report closing when retained pinning sessions are closing; that label alone does not establish manager teardown. user_may_gc preserves a lingering user while its units remain active. Actual Linger=yes, manager active/running and runtime-directory active with no queued unit jobs are independently observed. Exact reason for this label is not established.',
          'existing_lifetime_sufficient_for_later_context_gate': True,
          'configuration_or_linger_changed': False,
          'operation_admitted': False,
          'initial_observation_refusal': 'Named manager exe read raised PermissionError before any receipt or mutation; unavailable field is explicit in this read-only lifetime observation. Manager unit and PID/start/cgroup remain independently observed, not a full executable-tuple certification.',
          'limits': 'Recheck immediately before a launch and prove the exact new service running/MainPID/start/InvocationID/cgroup before verifier spawn. Explicit user termination, unexpected manager loss and resource kills are outside the persistence guarantee and confer no cleanup authority.'}
with (tracking / 'finish-working-delivery-user-lifetime1.json').open('x') as output:
    json.dump(record, output, indent=2)
    output.write('\n')
print(json.dumps({'existing_linger': user['Linger'], 'user_state': user['State'], 'manager': manager['ActiveState'] + '/' + manager['SubState'], 'pending_unit_job': bool(manager['Job']), 'operation_admitted': False}))
