"""One explicitly selected public capture window, with guarded restoration."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import shlex
import stat
import signal
import subprocess
import sys

os.umask(0o077)
def interrupted(number, _frame):
    raise KeyboardInterrupt("selected capture window interrupted")
signal.signal(signal.SIGTERM, interrupted)
signal.signal(signal.SIGINT, interrupted)
tracking = Path(__file__).resolve().parent
prep = json.loads((tracking / 'finish-working-delivery-operator-capture-window6-preparation.json').read_text())
packet = json.loads(Path(prep['packet_path']).read_text())
context = Path(prep['context']) / 'operation'
context.mkdir(mode=0o700)
root = Path(packet['campaign_root'])
selection = json.loads((tracking / 'finish-working-delivery-package-realize3-acceptance.json').read_text())['selection']
metadata = json.loads(Path(selection['metadata']).read_text())
capacity = json.loads(Path(prep['capacity_path']).read_text())
cycle = json.loads((tracking / 'finish-working-delivery-public-continuity5-proof.json').read_text())
assert cycle['complete'] and cycle['complete_exit']['complete']
assert cycle['generator'] == prep['generator']
failed = root / 'receipts/runtime-smoke-attempt.json'
runtime = [selection['runtime'] + '/bin/vpsfree-kb-devcluster', '--state-root', str(root / 'state')]
environment = packet['environment']
output = Path(prep['output_root'])
records = []
stage = 'fresh-resumed-continuity'
reserve_attempted = False
restoration = None
failure = None
fixture_preparation = None
export = None
current = None

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def write(path, value):
    with Path(path).open('x') as handle:
        json.dump(value, handle, indent=2)
        handle.write('\n')

def call(name, argv, data='', cwd=None):
    directory = context / name
    directory.mkdir(mode=0o700)
    with (directory / 'stdout').open('xb') as out, (directory / 'stderr').open('xb') as err:
        result = subprocess.run(argv, input=data.encode(), stdout=out, stderr=err,
                                env=environment, cwd=cwd or packet['cwd'])
    record = {'name': name, 'stage': stage, 'exit_code': result.returncode,
              'stdout_sha256': sha(directory / 'stdout'), 'stderr_sha256': sha(directory / 'stderr')}
    records.append(record)
    write(directory / 'native.json', record)
    if result.returncode:
        raise RuntimeError('Native public command failed; private diagnostics retained')
    return (directory / 'stdout').read_bytes()

def engine(name, args, data=''):
    return call(name, runtime + [args[0], 'same-slug'] + args[1:], data)

def descriptor(name):
    raw = engine(name, ['connection'])
    value = json.loads(raw)
    assert value['provenance']['source'] == metadata
    assert all(value[key] == cycle['resumed'][key]
               for key in ('instance_id', 'run_id', 'artifact_id', 'artifact_sha256'))
    path = context / (name + '.json')
    path.write_bytes(raw)
    return value, path

def private_hash(path):
    entry = path.lstat()
    assert stat.S_ISREG(entry.st_mode) and entry.st_uid == os.getuid()
    assert stat.S_IMODE(entry.st_mode) == 0o600
    return sha(path)

def continuity():
    directory = root / 'state/clusters/same-slug'
    base = cycle['continuity']
    for name, digest in base['credentials'].items():
        assert private_hash(directory / 'credentials' / name) == digest
    assert private_hash(directory / 'credentials/known_hosts') == base['known_hosts']
    assert private_hash(directory / 'accounts.json') == base['accounts_sha256']
    assert {p.name: private_hash(p) for p in directory.glob('artifact-*.json')} == base['artifacts']
    for name, expected in base['disks'].items():
        entry = (directory / 'disks' / name).lstat()
        assert stat.S_ISREG(entry.st_mode) and entry.st_uid == os.getuid()
        assert {'device': entry.st_dev, 'inode': entry.st_ino, 'size': entry.st_size} == expected
    for expected in base['images']:
        entry = Path(expected['path']).stat()
        assert {'device': entry.st_dev, 'inode': entry.st_ino, 'size': entry.st_size} == {
            key: expected[key] for key in ('device', 'inode', 'size')}
    assert sha(failed) == cycle['original_failed_attempt_sha256']
    assert not (root / 'receipts/runtime-smoke.json').exists()

def guard(machine):
    closure = current['provenance']['machine_toplevels'][machine]
    identity = Path(closure) / 'etc/vpsfree-kb-capture.json'
    assert json.loads(identity.read_bytes()) == current['provenance']['guest_identity']
    return ('set -eu\n'
            'test "$(sha256sum /etc/vpsfree-kb-capture.json | cut -d " " -f 1)" = ' + shlex.quote(sha(identity)) + '\n'
            'test "$(readlink -f /run/current-system)" = ' + shlex.quote(closure) + '\n')

def host_admission(name):
    ram = int(next(line for line in Path('/proc/meminfo').read_text().splitlines()
                   if line.startswith('MemAvailable:')).split()[1]) * 1024
    shm = os.statvfs('/dev/shm')
    margin = capacity['resource_overheads']['runtime_browser']
    assert ram >= margin['ram_bytes'] and shm.f_bavail * shm.f_frsize >= margin['shm_bytes']
    growth = 0
    for p in (root / 'state/clusters/same-slug/disks').glob('*.img'):
        entry = p.stat()
        growth += max(0, entry.st_size - entry.st_blocks * 512)
    for image in cycle['continuity']['images']:
        entry = Path(image['path']).stat()
        growth += max(0, entry.st_size - entry.st_blocks * 512)
    observations = []
    for budget in capacity['filesystems']:
        assert Path('/nix/store').stat().st_dev == budget['device']
        fs = os.statvfs('/nix/store')
        free = fs.f_bavail * fs.f_frsize
        required = growth + budget['reserve_bytes'] + budget['retained_growth_bytes'] + budget['build_headroom_bytes']
        assert free >= required
        observations.append({'free_bytes': free, 'required_bytes': required, 'remaining_growth_bytes': growth})
    write(context / (name + '-host.json'), {'ram_bytes': ram, 'shm_bytes': shm.f_bavail * shm.f_frsize,
        'additional_ram_required_bytes': margin['ram_bytes'], 'additional_shm_required_bytes': margin['shm_bytes'],
        'filesystems': observations})

def resources(name):
    values = {}
    pressure = {}
    for machine in ('services', 'node1'):
        script = guard(machine)
        script += "available_memory_bytes=$(awk '/^MemAvailable:/ {printf \"%.0f\", $2 * 1024}' /proc/meminfo)\nprintf 'available_memory_bytes=%s\\n' \"$available_memory_bytes\"\n"
        script += 'if test -r /proc/pressure/memory; then cat /proc/pressure/memory; fi\n'
        if machine == 'services':
            script += ('available_bytes=$(df -B1 --output=avail /)\navailable_inodes=$(df --output=iavail /)\n'
                       "printf 'available_bytes=%s\\n' \"$(printf '%s\\n' \"$available_bytes\" | tail -n 1 | tr -d ' ')\"\n"
                       "printf 'available_inodes=%s\\n' \"$(printf '%s\\n' \"$available_inodes\" | tail -n 1 | tr -d ' ')\"\n")
        else:
            script += ('tank_available_bytes=$(zfs get -Hp -o value available tank)\n'
                       "printf 'tank_available_bytes=%s\\n' \"$tank_available_bytes\"\n"
                       'test "$(cat /proc/sys/vm/min_free_kbytes)" = 65536\n')
        lines = engine(name + '-' + machine, ['ssh', machine, '--', 'sh', '-s'], script).decode().splitlines()
        parsed = dict(re.findall(r'^([a-z_]+)=([0-9]+)$', '\n'.join(lines), re.M))
        required = ('available_memory_bytes', 'available_bytes', 'available_inodes') if machine == 'services' else ('available_memory_bytes', 'tank_available_bytes')
        assert sorted(parsed) == sorted(required)
        values[machine] = {key: int(value) for key, value in parsed.items()}
        pressure[machine] = [line for line in lines if not re.fullmatch(r'[a-z_]+=[0-9]+', line)]
    assessment = capacity['capture_assessment']
    assert values['services']['available_bytes'] >= 1024**3
    assert values['services']['available_inodes'] >= assessment['minimum_free_inodes']
    assert values['services']['available_memory_bytes'] >= assessment['services_memory_bytes']
    assert values['node1']['available_memory_bytes'] >= assessment['node_memory_bytes']
    assert values['node1']['tank_available_bytes'] >= 4 * 1024**3 + assessment['template_metadata_bytes']
    write(context / (name + '-guests.json'), {'numeric': values, 'pressure': pressure,
        'assessment': assessment, 'reserve_kib': 65536, 'all_original_thresholds_passed': True})

def sentinel_continuity(name):
    for machine, expected in cycle['sentinels'].items():
        script = guard(machine) + 'sha256sum ' + shlex.quote(expected['path']) + '\n'
        observed = engine(name + '-' + machine + '-sentinel', ['ssh', machine, '--', 'sh', '-s'], script).decode().split()[0]
        assert observed == expected['sha256']

try:
    continuity()
    current, connection = descriptor('initial-connection')
    sentinel_continuity('initial')
    host_admission('initial')
    stage = 'temporary-reserve-preparation'
    reserve_attempted = True
    script = guard('node1')
    script += ('test "$(cat /proc/sys/vm/min_free_kbytes)" = 1048576\n'
               'printf 65536 > /proc/sys/vm/min_free_kbytes\n'
               'test "$(cat /proc/sys/vm/min_free_kbytes)" = 65536\n'
               'printf "reserve_before_kib=1048576\\nreserve_after_kib=65536\\n"\n')
    engine('prepare-reserve', ['ssh', 'node1', '--', 'sh', '-s'], script)
    capture = selection['capture'] + '/bin/vpsfree-kb-capture'
    stage = 'zero-swap-member-fixture-admission'
    host_admission('member-fixture')
    resources('member-fixture')
    sentinel_continuity('member-fixture')
    stage = 'zero-swap-member-fixture-preparation'
    call('member-fixture-preparation', ['node', prep['fixture_preparation'], selection['source'], str(connection), selection['metadata'], prep['fixture_result'], prep['fixture_error']])
    fixture_preparation = json.loads(Path(prep['fixture_result']).read_bytes())
    assert fixture_preparation['complete'] and not fixture_preparation['failure']
    assert all(fixture_preparation['source_ids'][key] == current[key] for key in ('instance_id', 'run_id', 'artifact_id', 'artifact_sha256'))
    for name, language, arguments, cwd in (
        ('cs-capture', 'cs', ['--cluster', 'same-slug', '--state-root', str(root / 'state'), '--output-root', str(output)], None),
        ('en-capture', 'en', ['--connection', str(connection), '--output-root', str(output)], None),
        ('en-default-cwd', 'en', ['--connection', str(connection)], str(output)),
    ):
        stage = name + '-admission'
        continuity()
        descriptor(name + '-connection')
        host_admission(name)
        resources(name)
        sentinel_continuity(name)
        stage = name
        call(name, [capture, *arguments, '--language', language, '--checkpoint', 'networking/ip-address-list'], cwd=cwd)
    sentinel_continuity('post-capture')
    stage = 'strict-installed-validation-export'
    validate = selection['capture'] + '/bin/vpsfree-kb-validate'
    call('validate-update', [validate, '--update', '--output-root', str(output)])
    call('validate-strict', [validate, '--output-root', str(output)])
    rows = json.loads((output / 'tmp/capture-results.json').read_bytes())
    assert sorted((row['language'], row['id']) for row in rows) == [('cs', 'networking/ip-address-list'), ('en', 'networking/ip-address-list')]
    assert all(row['provenance']['source'] == metadata for row in rows)
    assert all(row['provenance']['run_id'] == current['run_id'] for row in rows)
    exporter = "require File.join(ARGV[0], 'tools/capture-export'); puts JSON.generate(KbCaptureArtifacts.export(ARGV[1], ARGV[2]))"
    export = json.loads(call('locked-five-file-export', ['ruby', '-e', exporter, selection['source'], str(output), prep['export_root']]))
except BaseException as error:
    failure = {'stage': stage, 'failure_class': type(error).__name__}
finally:
    if reserve_attempted:
        stage = 'guarded-reserve-restoration'
        try:
            descriptor('restoration-connection')
            script = guard('node1')
            script += ('value=$(cat /proc/sys/vm/min_free_kbytes)\n'
                       'if test "$value" = 65536; then printf 1048576 > /proc/sys/vm/min_free_kbytes; '
                       'elif test "$value" != 1048576; then exit 1; fi\n'
                       'test "$(cat /proc/sys/vm/min_free_kbytes)" = 1048576\n'
                       'printf "reserve_restored_kib=1048576\\n"\n')
            engine('restore-reserve', ['ssh', 'node1', '--', 'sh', '-s'], script)
            continuity()
            restoration = {'complete': True, 'reserve_kib': 1048576}
        except BaseException as error:
            restoration = {'complete': False, 'failure_class': type(error).__name__}
    value = {'schema': 1, 'at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'generator': prep['generator'], 'complete': failure is None and restoration and restoration['complete'],
        'failure': failure, 'restoration': restoration, 'export': export, 'commands': records,
        'source_ids': {key: current[key] for key in ('instance_id', 'run_id', 'artifact_id', 'artifact_sha256')} if current else None,
        'original_failed_attempt_sha256': sha(failed), 'original_campaign_completed': False,
        'operator_prepared_reserve_kib': 65536, 'stock_default_capture_fit_claimed': False,
        'sentinel_continuity_proved': cycle['sentinel_continuity_proved'],
        'operator_prepared_fixture': fixture_preparation, 'diagnostic_entry_used': False, 'installed_capture_entry_pass_claimed': failure is None,
        'limits': 'Genuine packaged capture/validator from reviewed Gcd2, with short private TMPDIR and guarded temporary node reserve. Strict full-inventory and five-file export; visual acceptance/final ordinary stop remain separate.'}
    write(context / 'result.json', value)
    write(tracking / 'finish-working-delivery-operator-capture-window6-proof.json', value)
    print(json.dumps({'complete': bool(value['complete']), 'failure': failure, 'restoration': restoration,
                      'exported': export is not None, 'original_campaign_completed': False}), flush=True)
sys.exit(0 if value['complete'] else 1)
