#!/usr/bin/env python3
"""Finite, private operation wrapper for the accepted ordinary-host campaign."""
import datetime
import hashlib
import json
import os
import pathlib
import signal
import subprocess
import sys
import time

packet_path = pathlib.Path(sys.argv[1])
packet = json.loads(packet_path.read_text())
context = pathlib.Path(packet['context'])
assert context.is_dir() and context.stat().st_uid == os.getuid()
assert context.stat().st_mode & 0o777 == 0o700
record = {'schema': 1, 'unit': packet['unit'], 'phase': packet['phase'],
          'generator': packet['generator'], 'started_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'wrapper_sha256': hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
          'packet_sha256': hashlib.sha256(packet_path.read_bytes()).hexdigest(),
          'complete': False, 'daemon_or_detached_cleanup_certified': False}
child = None
cancel = None
interruption = None

def note_signal(number, _frame):
    global interruption
    interruption = number

signal.signal(signal.SIGTERM, note_signal)
signal.signal(signal.SIGINT, note_signal)

def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def write(name, value):
    fd = os.open(context / name, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, 'w') as output:
        json.dump(value, output, indent=2)
        output.write('\n')

def unit_properties():
    result = subprocess.run([packet['systemctl'], '--user', 'show', packet['unit'],
        '--property=ActiveState,SubState,MainPID,InvocationID,ControlGroup,Type,ExitType,RemainAfterExit,KillMode,OOMPolicy,Restart,CollectMode,ExecStartPre,ExecStartPost,ExecStop,ExecStopPost,OnFailure,BindsTo,PartOf'],
        capture_output=True, text=True, timeout=10)
    if result.returncode:
        raise RuntimeError('exact user-service properties unavailable')
    return dict(line.split('=', 1) for line in result.stdout.splitlines() if '=' in line)

def tuple_of(pid):
    base = pathlib.Path('/proc') / str(pid)
    try:
        before = (base / 'stat').read_text().rsplit(')', 1)[1].split()
        value = {'pid': pid, 'uid': base.stat().st_uid,
            'boot_id': pathlib.Path('/proc/sys/kernel/random/boot_id').read_text().strip(),
            'start_ticks': int(before[19]), 'state': before[0], 'ppid': int(before[1]),
            'pgid': int(before[2]), 'sid': int(before[3]),
            'exe': os.readlink(base / 'exe'),
            'argv': [x.decode(errors='replace') for x in (base / 'cmdline').read_bytes().split(b'\0') if x],
            'cgroup': (base / 'cgroup').read_text().strip()}
        after = (base / 'stat').read_text().rsplit(')', 1)[1].split()
        if before[19] != after[19] or value['uid'] != os.getuid():
            return None
        return value
    except (FileNotFoundError, ProcessLookupError):
        return None

def recorded_live_tuples():
    observations = []
    for state in ['state-a', 'state-b']:
        directory = pathlib.Path(packet['campaign_root']) / state / 'clusters' / 'same-slug'
        for name in directory.glob('processes-*.json'):
            try:
                # Observation only: never authorize control or infer completion.
                st = name.lstat()
                if not name.is_file() or name.is_symlink() or st.st_uid != os.getuid() or st.st_mode & 0o777 != 0o600 or st.st_size > 2 * 1024**2:
                    continue
                proof = json.loads(name.read_text())
                for claimed in [proof['runner'], *proof['children']]:
                    actual = tuple_of(claimed['pid'])
                    if actual and all(actual.get(key) == claimed.get(key) for key in ['uid', 'boot_id', 'start_ticks', 'exe', 'argv']):
                        observations.append({'state': state, 'instance_id': proof['instance_id'],
                            'run_id': proof['run_id'], 'artifact_id': proof['artifact_id'],
                            'record_complete': proof['complete'], 'tuple': actual})
            except (FileNotFoundError, KeyError, json.JSONDecodeError):
                continue
    return observations

try:
    deadline = time.monotonic() + 80
    while True:
        properties = unit_properties()
        if properties.get('ActiveState') == 'active' and properties.get('SubState') == 'running' and properties.get('MainPID') == str(os.getpid()):
            break
        if interruption or time.monotonic() >= deadline:
            raise RuntimeError('service context was not admitted before verification')
        time.sleep(0.2)
    own = tuple_of(os.getpid())
    expected = {'Type': 'exec', 'ExitType': 'cgroup', 'RemainAfterExit': 'yes',
                'KillMode': 'control-group', 'OOMPolicy': 'continue', 'Restart': 'no', 'CollectMode': 'inactive'}
    assert all(properties.get(k) == v for k, v in expected.items()), 'service properties differ'
    assert properties['InvocationID'] and properties['ControlGroup'].startswith(packet['manager_cgroup'] + '/'), 'manager boundary differs'
    assert own and own['cgroup'].endswith(properties['ControlGroup']), 'wrapper cgroup differs'
    assert properties['ControlGroup'] != packet['exec_cgroup'] and not properties['ControlGroup'].startswith(packet['exec_cgroup'] + '/'), 'service inherits command teardown boundary'
    assert all(not properties.get(k) for k in ['ExecStartPre', 'ExecStartPost', 'ExecStop', 'ExecStopPost', 'OnFailure', 'BindsTo', 'PartOf']), 'unexpected lifecycle hooks'
    for item in packet['bound_files']:
        assert hashlib.sha256(pathlib.Path(item['path']).read_bytes()).hexdigest() == item['sha256'], 'operation binding changed'
    record['controller'] = own
    record['admitted_context'] = properties
    write('admitted.json', record)
    environment = packet['environment']
    with (context / 'native.stdout').open('xb') as output, (context / 'native.stderr').open('xb') as error, (context / 'measurements.jsonl').open('x') as measurements:
        if interruption:
            raise RuntimeError('interrupted before child launch')
        child = subprocess.Popen(packet['argv'], cwd=packet['cwd'], env=environment,
            stdin=subprocess.DEVNULL, stdout=output, stderr=error, close_fds=True)
        record['verifier'] = tuple_of(child.pid)
        assert record['verifier'], 'child exited before a current tuple could be retained'
        write('started.json', record)
        while child.poll() is None:
            fs = os.statvfs(packet['filesystem_path'])
            free = fs.f_bavail * fs.f_frsize
            ram = int(next(line for line in pathlib.Path('/proc/meminfo').read_text().splitlines() if line.startswith('MemAvailable:')).split()[1]) * 1024
            shm = os.statvfs('/dev/shm')
            shm_free = shm.f_bavail * shm.f_frsize
            measurements.write(json.dumps({'at': now(), 'free_bytes': free, 'ram_bytes': ram,
                'shm_bytes': shm_free, 'recorded_live_tuples': recorded_live_tuples()}) + '\n')
            measurements.flush()
            if free < packet['reserve_bytes']:
                cancel = 'protected host and retained sparse-growth reserve lost'
            elif ram < 8 * 1024**3 or shm_free < 2 * 1024**3:
                cancel = 'host RAM/shared-memory safety headroom lost'
            elif interruption:
                cancel = 'wrapper signal ' + str(interruption)
            expected_kernels = packet.get('expected_kernels')
            if expected_kernels:
                for config in pathlib.Path(packet['campaign_root']).glob('state-*/clusters/same-slug/result-config-*'):
                    if config.is_symlink() and str(config.resolve()).startswith('/nix/store/') and config.is_file():
                        actual = json.loads(config.read_text())['machines']
                        if {key: value['kernel'] for key, value in actual.items()} != expected_kernels:
                            cancel = 'actual prepared kernels differ from accepted exact projections'
            if cancel:
                break
            time.sleep(1)
        if cancel and child.poll() is None:
            current = tuple_of(child.pid)
            retained = record['verifier']
            assert current and current['ppid'] == os.getpid() and all(current[k] == retained[k] for k in ['uid', 'boot_id', 'start_ticks']), 'owned child cancellation tuple changed'
            child.terminate()
            try:
                child.wait(timeout=15)
            except subprocess.TimeoutExpired:
                # This wrapper is the sole parent/reaper and still owns this PID.
                child.kill()
                child.wait()
        child.wait()
        record.update(complete=True, exit_code=child.returncode, cancel_reason=cancel)
except BaseException as failure:
    record.update(wrapper_failure=type(failure).__name__, wrapper_message=str(failure), cancel_reason=cancel)
    # Unexpected wrapper failure provides no expanded shutdown authority.
finally:
    record['finished_at'] = now()
    try:
        record['final_context'] = unit_properties()
    except BaseException:
        record['final_context'] = 'unavailable'
    record['evidence_sha256'] = {file.name: hashlib.sha256(file.read_bytes()).hexdigest()
        for file in context.iterdir() if file.is_file() and file.name not in ['packet.json', 'result.json']}
    write('result.json', record)
sys.exit(record.get('exit_code', 1) if record.get('complete') and not record.get('wrapper_failure') else 1)
