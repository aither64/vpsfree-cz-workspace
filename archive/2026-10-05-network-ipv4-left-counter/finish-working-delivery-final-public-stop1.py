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
preparation = json.loads((tracking / 'finish-working-delivery-final-public-stop1-preparation.json').read_text())
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
    path = context / (name + '-connection.json')
    path.write_bytes(raw)
    return value, path

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


try:
    restored = json.loads((tracking / 'finish-working-delivery-operator-capture-window2-disposition.json').read_text())
    assert restored['restoration'] == {'complete': True, 'reserve_kib': 1048576}
    assert restored['source_ids'] == preparation['source_ids']
    prior = json.loads((tracking / 'finish-working-delivery-public-continuity4-proof.json').read_text())
    assert prior['complete'] and prior['resumed'] == preparation['source_ids']
    for unit in preparation['closed_operation_units']:
        status = subprocess.run([packet['systemctl'], '--user', 'show', unit,
            '--property=MainPID,SubState'], capture_output=True, text=True, check=True)
        props = dict(line.split('=', 1) for line in status.stdout.splitlines() if '=' in line)
        assert props['MainPID'] == '0' and props['SubState'] in ['exited', 'dead', 'failed']
    initial, connection = descriptor('initial')
    assert {k: initial[k] for k in preparation['source_ids']} == preparation['source_ids']
    stage = 'retained-continuity-baseline'
    baseline = identities()
    assert baseline == prior['continuity']
    write(context / 'continuity-baseline.json', baseline)
    stage = 'final-ordinary-public-stop'
    engine('stop', ['stop', '--timeout', '900'])
    stopped = json.loads(engine('stopped-status', ['status']))
    assert stopped['found'] and not stopped['ready'] and stopped['state'] == 'stopped'
    stage = 'complete-exit-proof'
    proof_script = """require File.join(ARGV[0], 'cluster/lib/kb_runtime')
s = KbRuntime::State.new(ARGV[1], 'same-slug')
s.lock('gate') do
  p = s.read(s.path("processes-#{ARGV[2]}.json"))
  l = s.read(s.path("launch-#{ARGV[2]}.json"))
  ids = JSON.parse(ARGV[3])
  raise 'foreign exit proof' unless ids.all? { |k,v| p[k] == v && l[k] == v }
  raise 'incomplete exit' unless p['schema'] == 1 && p['complete'] == true
  raise 'owned process not gone' unless [p['runner'], *p['children']].all? { |x| KbRuntime::ProcessIdentity.gone?(x) }
  r = KbRuntime::Resources.new(s)
  claim = File.join(r.root, "#{p['instance_id']}-#{p['run_id']}.json")
  raise 'retained own claim' if File.exist?(claim) || File.symlink?(claim)
  raise 'retained socket namespace' if File.exist?(l.fetch('socket_dir')) || File.symlink?(l.fetch('socket_dir'))
  puts JSON.generate(ids.merge(complete: true, runner_gone: true, children_gone: p['children'].length,
    own_claim_absent: true, socket_namespace_absent: true))
end"""
    proof = json.loads(call('complete-exit', ['ruby', '-e', proof_script, selection['source'], str(root / 'state'), initial['run_id'], json.dumps(preparation['source_ids'])]))
    assert all(proof[k] == v for k,v in preparation['source_ids'].items())
    assert identities() == baseline
    assert digest(failed) == diagnosis['failed_attempt_sha256'] and not (root / 'receipts/runtime-smoke.json').exists()
    assert not (root / 'receipts/accepted-runtime.json').exists()
    stage = 'complete'
    value = {'schema': 1, 'at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'complete': True,
        'generator': preparation['generator'], 'source_ids': preparation['source_ids'],
        'ordinary_public_stop': True, 'complete_exit': proof, 'continuity_unchanged': True,
        'commands': records, 'original_failed_attempt_sha256': digest(failed),
        'original_campaign_completed': False, 'canonical_media_proved': False,
        'temporary_node_reserve_restored_before_stop': True, 'retained_disks': True,
        'force_reset_resume_builder_or_new_pair': False}
    write(context / 'completed.json', value)
    write(tracking / 'finish-working-delivery-final-public-stop1-proof.json', value)
    print(json.dumps({'complete': True, 'ordinary_public_stop': True, 'children_gone': proof['children_gone'], 'retained_disks': True}), flush=True)
except BaseException as error:
    value = {'schema': 1, 'at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'complete': False,
        'generator': preparation['generator'], 'source_ids': preparation['source_ids'],
        'stage': stage, 'failure_class': type(error).__name__, 'commands': records,
        'original_failed_attempt_sha256': digest(failed), 'original_campaign_completed': False,
        'force_or_reset_authorized': False}
    write(context / 'failed.json', value)
    write(tracking / 'finish-working-delivery-final-public-stop1-proof.json', value)
    print(json.dumps({'complete': False, 'stage': stage, 'failure_class': type(error).__name__, 'private_diagnostics': str(context)}), flush=True)
    sys.exit(1)
