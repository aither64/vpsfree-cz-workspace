"""One explicit public-operation sequence; never enters the failed Campaign."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import stat
import subprocess
import sys

os.umask(0o077)
tracking = Path(__file__).resolve().parent
preparation = json.loads((tracking / 'finish-working-delivery-public-continuity1-preparation.json').read_text())
packet = json.loads(Path(preparation['packet_path']).read_text())
root = Path(packet['campaign_root'])
context = Path(preparation['context']) / 'operation'
context.mkdir(mode=0o700)
package = json.loads((tracking / 'finish-working-delivery-package-realize2-acceptance.json').read_text())
selection = package['selection']
metadata = json.loads(Path(selection['metadata']).read_text())
diagnosis = json.loads((tracking / 'finish-working-delivery-browser-path-diagnosis1.json').read_text())
failed = root / 'receipts/runtime-smoke-attempt.json'
assert hashlib.sha256(failed.read_bytes()).hexdigest() == diagnosis['failed_attempt_sha256']
assert not (root / 'receipts/runtime-smoke.json').exists()
environment = packet['environment']
tmp = Path(environment['TMPDIR'])
assert tmp.is_dir() and not tmp.is_symlink() and tmp.stat().st_uid == os.getuid()
assert stat.S_IMODE(tmp.stat().st_mode) == 0o700 and len(str(tmp).encode()) < 35
runtime = [selection['runtime'] + '/bin/vpsfree-kb-devcluster', '--state-root', str(root / 'state')]
records = []
stage = 'fresh-public-attestation'

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def write(path, value):
    with Path(path).open('x') as output:
        json.dump(value, output, indent=2)
        output.write('\n')

def call(name, argv, data=''):
    directory = context / name
    directory.mkdir(mode=0o700)
    with (directory / 'stdout').open('xb') as out, (directory / 'stderr').open('xb') as err:
        native = subprocess.run(argv, input=data.encode(), stdout=out, stderr=err, env=environment, cwd=packet['cwd'])
    record = {'name': name, 'stage': stage, 'exit_code': native.returncode,
              'stdout_sha256': digest(directory / 'stdout'), 'stderr_sha256': digest(directory / 'stderr')}
    write(directory / 'native.json', record)
    records.append(record)
    if native.returncode:
        raise RuntimeError('Native public command failed; private diagnostics retained')
    return (directory / 'stdout').read_bytes()

def engine(name, args, data=''):
    return call(name, runtime + [args[0], 'same-slug'] + args[1:], data)

def descriptor(name):
    raw = engine(name + '-connection', ['connection'])
    value = json.loads(raw)
    assert value['provenance']['source'] == metadata
    assert set(value['machines']) == {'services', 'node1'}
    assert value['instance_id'] == diagnosis['instance_id']
    for machine, closure in value['provenance']['machine_toplevels'].items():
        assert json.loads(engine(name + '-' + machine + '-identity', ['ssh', machine, '--', 'cat', '/etc/vpsfree-kb-capture.json'])) == value['provenance']['guest_identity']
        assert engine(name + '-' + machine + '-closure', ['ssh', machine, '--', 'readlink', '-f', '/run/current-system']).decode().strip() == closure
    path = context / (name + '-connection.json')
    path.write_bytes(raw)
    return value, path

source_text = Path(selection['source'], 'tools/runtime-verify.rb').read_text()
assert hashlib.sha256(source_text.encode()).hexdigest() == '3adf8e4c33c2754ed4013a3b266592f82670ddf0154e27a040676ecca39e94fb'
start = source_text.index("      script = <<~'JS'", source_text.index('    def read_smoke'))
end = source_text.index('\n      JS', start)
read_smoke = '\n'.join(line[8:] for line in source_text[start:end].splitlines()[1:])

def browser_read(name, connection):
    value = json.loads(call(name, ['node', '-e', read_smoke, str(connection), selection['metadata'], selection['source']]))
    assert value['api_tls_verified'] and value['php_member_read']
    assert value['member']['login'] == 'test-user1'
    return {key: value[key] for key in ['api_tls_verified', 'php_member_read', 'instance_id', 'run_id']}

def identities():
    directory = root / 'state/clusters/same-slug'
    def private(path):
        st = path.lstat()
        assert stat.S_ISREG(st.st_mode) and st.st_uid == os.getuid() and stat.S_IMODE(st.st_mode) == 0o600
        return digest(path)
    credential_names = ['id_ed25519', 'id_ed25519.pub', 'vpsadmin-ca.crt', 'vpsadmin-ca.key', 'vpsadmin-cert.crt', 'vpsadmin-cert.key']
    credentials = {name: private(directory / 'credentials' / name) for name in credential_names}
    disks = {}
    for name in ['services-root.img', 'node1-tank.img']:
        st = (directory / 'disks' / name).lstat()
        assert stat.S_ISREG(st.st_mode) and st.st_uid == os.getuid() and st.st_size == 8 * 1024**3
        disks[name] = {'device': st.st_dev, 'inode': st.st_ino, 'size': st.st_size}
    artifacts = {p.name: private(p) for p in directory.glob('artifact-*.json')}
    assert len(artifacts) == 1
    image_paths = set()
    for p in directory.glob('result-config-*'):
        resolved = p.resolve(strict=True)
        assert str(resolved).startswith('/nix/store/')
        image_paths.add(json.loads(resolved.read_text())['machines']['services']['diskImage'])
    assert len(image_paths) == 1
    images = []
    for image in image_paths:
        st = Path(image).stat()
        assert stat.S_ISREG(st.st_mode) and st.st_size == 8 * 1024**3
        images.append({'path': image, 'device': st.st_dev, 'inode': st.st_ino, 'size': st.st_size})
    return {'credentials': credentials, 'known_hosts': private(directory / 'credentials/known_hosts'),
            'accounts_sha256': private(directory / 'accounts.json'), 'artifacts': artifacts, 'disks': disks, 'images': images}

def sentinels(name):
    return {machine: engine(name + '-' + machine, ['ssh', machine, '--', 'sha256sum', path]).decode().split()[0]
            for machine, path in [('services', '/root/kb-root-sentinel'), ('node1', '/tank/kb-data-sentinel')]}

try:
    initial, connection = descriptor('initial')
    assert all(initial[key] == diagnosis[key] for key in ['run_id', 'artifact_id', 'artifact_sha256'])
    stage = 'member-read-smoke'
    first_read = browser_read('member-read', connection)
    stage = 'public-live-lease'
    call('live-lease', ['node', str(Path(selection['source'], 'tools/verify-live-lease.cjs')), str(connection), selection['metadata'], selection['runtime'], str(root / 'state'), str(root / 'config.json')])
    print(json.dumps({'completed': 'real member PHP/TLS/API and public live lease'}), flush=True)
    stage = 'continuity-baseline'
    marker = preparation['operation_id']
    for machine, path in [('services', '/root/kb-root-sentinel'), ('node1', '/tank/kb-data-sentinel')]:
        engine('sentinel-create-' + machine, ['ssh', machine, '--', 'sh', '-c', 'set -eu; test ! -e "$1"; printf "%s" "$2" > "$1"', 'sh', path, marker])
    baseline, sentinel = identities(), sentinels('baseline-sentinel')
    write(context / 'continuity-baseline.json', {'identities': baseline, 'sentinels': sentinel})
    stage = 'ordinary-public-stop'
    engine('stop', ['stop', '--timeout', '900'])
    stopped = json.loads(engine('stopped-status', ['status']))
    assert stopped['found'] and not stopped['ready'] and stopped['state'] == 'stopped'
    proof_script = '''require File.join(ARGV[0], 'cluster/lib/kb_runtime')
s = KbRuntime::State.new(ARGV[1], 'same-slug')
s.lock('gate') do
  p = s.read(s.path("processes-#{ARGV[2]}.json"))
  l = s.read(s.path("launch-#{ARGV[2]}.json"))
  raise 'incomplete exit' unless p['schema'] == 1 && p['complete'] == true && p['run_id'] == ARGV[2]
  raise 'owned process not gone' unless [p['runner'], *p['children']].all? { |x| KbRuntime::ProcessIdentity.gone?(x) }
  r = KbRuntime::Resources.new(s)
  claim = File.join(r.root, "#{p['instance_id']}-#{p['run_id']}.json")
  raise 'retained own claim' if File.exist?(claim) || File.symlink?(claim)
  raise 'retained socket namespace' if File.exist?(l.fetch('socket_dir')) || File.symlink?(l.fetch('socket_dir'))
  puts JSON.generate({complete: true, runner_gone: true, children_gone: p['children'].length,
    own_claim_absent: true, socket_namespace_absent: true, instance_id: p['instance_id'], run_id: p['run_id'],
    artifact_id: p['artifact_id'], artifact_sha256: p['artifact_sha256']})
end'''
    proof = json.loads(call('complete-exit', ['ruby', '-e', proof_script, selection['source'], str(root / 'state'), initial['run_id']]))
    assert all(proof[key] == initial[key] for key in ['instance_id', 'run_id', 'artifact_id', 'artifact_sha256'])
    stage = 'fresh-resume-admission'
    capacity = json.loads(Path(preparation['capacity_path']).read_text())
    ram = int(next(line for line in Path('/proc/meminfo').read_text().splitlines() if line.startswith('MemAvailable:')).split()[1]) * 1024
    shm = os.statvfs('/dev/shm')
    assert ram >= 6 * 1024**3 and shm.f_bavail * shm.f_frsize >= 5 * 1024**3
    disk_paths = list((root / 'state/clusters/same-slug/disks').glob('*.img'))
    growth = sum(max(0, p.stat().st_size - p.stat().st_blocks * 512) for p in disk_paths)
    assert len(disk_paths) == 2
    for image in baseline['images']:
        growth += max(0, image['size'] - Path(image['path']).stat().st_blocks * 512)
    for budget in capacity['filesystems']:
        assert Path('/nix/store').stat().st_dev == budget['device']
        fs = os.statvfs('/nix/store')
        free = fs.f_bavail * fs.f_frsize
        required = growth + budget['reserve_bytes'] + budget['retained_growth_bytes'] + budget['build_headroom_bytes']
        assert free >= required
    write(context / 'resume-admission.json', {'ram_available_bytes': ram, 'shm_available_bytes': shm.f_bavail * shm.f_frsize,
        'filesystem_available_bytes': free, 'required_bytes': required, 'owned_remaining_growth_bytes': growth, 'image_rebuild': False})
    stage = 'same-artifact-public-resume'
    engine('resume', ['resume', '--timeout', '900'])
    resumed, resumed_connection = descriptor('resumed')
    assert resumed['run_id'] != initial['run_id']
    assert all(resumed[key] == initial[key] for key in ['instance_id', 'artifact_id', 'artifact_sha256'])
    assert resumed['provenance']['machine_toplevels'] == initial['provenance']['machine_toplevels']
    assert identities() == baseline and sentinels('resumed-sentinel') == sentinel
    stage = 'resumed-member-read'
    second_read = browser_read('resumed-member-read', resumed_connection)
    assert digest(failed) == diagnosis['failed_attempt_sha256'] and not (root / 'receipts/runtime-smoke.json').exists()
    stage = 'complete'
    value = {'schema': 1, 'at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'complete': True,
        'generator': preparation['generator'], 'operation_id': marker, 'initial': {k: initial[k] for k in ['instance_id', 'run_id', 'artifact_id', 'artifact_sha256']},
        'resumed': {k: resumed[k] for k in ['instance_id', 'run_id', 'artifact_id', 'artifact_sha256']},
        'first_read': first_read, 'resumed_read': second_read, 'public_lease_proof': True, 'complete_exit': proof,
        'continuity': baseline, 'sentinels': sentinel, 'commands': records, 'original_failed_attempt_sha256': digest(failed),
        'original_campaign_completed': False, 'capture_started': False, 'short_private_tmpdir': str(tmp)}
    write(context / 'completed.json', value)
    write(tracking / 'finish-working-delivery-public-continuity1-proof.json', value)
    print(json.dumps({'complete': True, 'public_stop_resume': True, 'same_artifact_continuity': True, 'capture_started': False}), flush=True)
except BaseException as error:
    write(context / 'failed.json', {'stage': stage, 'failure_class': type(error).__name__, 'commands': records,
        'original_failed_attempt_sha256': digest(failed), 'original_campaign_completed': False})
    print(json.dumps({'complete': False, 'stage': stage, 'failure_class': type(error).__name__, 'private_diagnostics': str(context)}), flush=True)
    sys.exit(1)
