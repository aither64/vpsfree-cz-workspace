"""Finite direct capture from fresh working6; no completed Campaign claim."""
import datetime, hashlib, json, os, re, shlex, stat, subprocess, sys, textwrap
from pathlib import Path

os.umask(0o077)
T = Path(__file__).resolve().parent
prep = json.loads((T / 'finish-working-delivery-direct-capture6-preparation.json').read_text())
packet = json.loads(Path(prep['packet_path']).read_text())
context = Path(prep['context']) / 'operation'
context.mkdir(mode=0o700)
root = Path(packet['campaign_root'])
directory = root / 'state/clusters/same-slug'
selection = json.loads((T / 'finish-working-delivery-package-realize6-acceptance.json').read_text())['selection']
metadata = json.loads(Path(selection['metadata']).read_text())
assert metadata['revision'] == prep['generator']
environment = packet['environment']
runtime = [selection['runtime'] + '/bin/vpsfree-kb-devcluster', '--state-root', str(root / 'state')]
output = Path(prep['output_root'])
commands, failure, exported, current, baseline = [], None, None, None, None
stage = 'post-start-connection'
G = 1024**3
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()

def write(path, value):
    with Path(path).open('x') as handle:
        json.dump(value, handle, indent=2)
        handle.write('\n')

def call(name, argv, data='', cwd=None):
    private = context / name
    private.mkdir(mode=0o700)
    with (private / 'stdout').open('xb') as out, (private / 'stderr').open('xb') as err:
        result = subprocess.run(argv, input=data.encode(), stdout=out, stderr=err,
                                env=environment, cwd=cwd or packet['cwd'])
    record = {'name': name, 'stage': stage, 'exit_code': result.returncode,
              'stdout_sha256': sha(private / 'stdout'), 'stderr_sha256': sha(private / 'stderr')}
    commands.append(record)
    write(private / 'native.json', record)
    if result.returncode:
        raise RuntimeError('native command refused; private diagnostics retained')
    return (private / 'stdout').read_bytes()

def engine(name, args, data=''):
    return call(name, runtime + [args[0], 'same-slug', *args[1:]], data)

def descriptor(name):
    raw = engine(name, ['connection'])
    value = json.loads(raw)
    assert value['provenance']['source'] == metadata
    assert sorted(value['machines']) == ['node1', 'services']
    if current:
        assert all(value[k] == current[k] for k in ('instance_id', 'run_id', 'artifact_id', 'artifact_sha256'))
    path = context / (name + '.json')
    path.write_bytes(raw)
    return value, path

def private_hash(path):
    s = path.lstat()
    assert stat.S_ISREG(s.st_mode) and s.st_uid == os.getuid() and stat.S_IMODE(s.st_mode) == 0o600
    return sha(path)

def identities():
    credentials = {n: private_hash(directory / 'credentials' / n) for n in
                   ['id_ed25519', 'id_ed25519.pub', 'vpsadmin-ca.crt', 'vpsadmin-ca.key',
                    'vpsadmin-cert.crt', 'vpsadmin-cert.key', 'known_hosts']}
    disks = {}
    for n in ['services-root.img', 'node1-tank.img']:
        s = (directory / 'disks' / n).lstat()
        assert stat.S_ISREG(s.st_mode) and s.st_uid == os.getuid() and s.st_size == 8*G
        disks[n] = {'device': s.st_dev, 'inode': s.st_ino, 'size': s.st_size}
    images = set()
    for p in directory.glob('result-config-*'):
        q = p.resolve(strict=True)
        assert str(q).startswith('/nix/store/') and q.is_file()
        images.add(json.loads(q.read_text())['machines']['services']['diskImage'])
    assert len(images) == 1
    image = Path(images.pop())
    s = image.stat()
    assert str(image).startswith('/nix/store/') and stat.S_ISREG(s.st_mode) and s.st_size == 8*G
    artifacts = {p.name: private_hash(p) for p in directory.glob('artifact-*.json')}
    assert len(artifacts) == 1
    assert sha(directory / ('artifact-' + current['artifact_id'] + '.json')) == current['artifact_sha256']
    return {'credentials': credentials, 'accounts_sha256': private_hash(directory / 'accounts.json'),
            'disks': disks, 'artifacts': artifacts,
            'images': [{'path': str(image), 'device': s.st_dev, 'inode': s.st_ino, 'size': s.st_size}]}

def host_admission(name):
    ram = int(next(x for x in Path('/proc/meminfo').read_text().splitlines() if x.startswith('MemAvailable:')).split()[1])*1024
    shm = os.statvfs('/dev/shm')
    assert ram >= 2*G and shm.f_bavail*shm.f_frsize >= G
    growth = sum(max(0, p.stat().st_size-p.stat().st_blocks*512) for p in (directory / 'disks').glob('*.img'))
    fs = os.statvfs('/nix/store')
    free = fs.f_bavail*fs.f_frsize
    required = growth + prep['other_retained_growth_bytes'] + 16*G + 3*G
    assert free >= required
    write(context / (name + '-host.json'), {'available_ram_bytes': ram, 'available_shm_bytes': shm.f_bavail*shm.f_frsize,
        'incremental_ram_required_bytes': 2*G, 'incremental_shm_required_bytes': G,
        'free_bytes': free, 'required_bytes': required, 'own_writable_growth_bytes': growth,
        'other_retained_growth_bytes': prep['other_retained_growth_bytes'], 'base_reserve_bytes': 16*G,
        'fixed_capture_uncertainty_bytes': 3*G, 'immutable_image_holes_charged_as_future_writes': False})

def resources(name):
    owner = Path(selection['source']) / 'tools/runtime-verify.rb'
    body = owner.read_text().split('    def resource_script(machine)\n', 1)[1].split('    def resources(', 1)[0]
    blocks = [textwrap.dedent(x) for x in re.findall(r"<<~'SH'\n(.*?)^\s*SH$", body, re.M | re.S)]
    assert len(blocks) == 3
    observations = {}
    for machine, extra in [('services', blocks[1]), ('node1', blocks[2])]:
        closure = current['provenance']['machine_toplevels'][machine]
        identity = Path(closure) / 'etc/vpsfree-kb-capture.json'
        assert json.loads(identity.read_bytes()) == current['provenance']['guest_identity']
        guard = 'set -eu\ntest "$(sha256sum /etc/vpsfree-kb-capture.json | cut -d " " -f 1)" = ' + shlex.quote(sha(identity)) + '\n'
        guard += 'test "$(readlink -f /run/current-system)" = ' + shlex.quote(closure) + '\n'
        raw = engine(name + '-' + machine, ['ssh', machine, '--', 'sh', '-s'], guard + blocks[0] + extra).decode()
        numeric = {k: int(v) for k, v in re.findall(r'^([a-z_]+)=([0-9]+)$', raw, re.M)}
        expected = ['available_memory_bytes', 'available_bytes', 'available_inodes'] if machine == 'services' else ['available_memory_bytes', 'tank_available_bytes']
        assert sorted(numeric) == sorted(expected)
        observations[machine] = numeric
    assert observations['services']['available_bytes'] >= G
    assert observations['services']['available_inodes'] >= 10000
    assert observations['services']['available_memory_bytes'] >= 256*1024**2
    assert observations['node1']['available_memory_bytes'] >= G+128*1024**2
    assert observations['node1']['tank_available_bytes'] >= 5*G
    proof = {'observations': observations, 'source_script_sha256': sha(owner),
             'source_and_system_closure_proved': True, 'no_guest_sysctl_change': True}
    write(context / (name + '-resources.json'), proof)
    return proof

try:
    current, connection = descriptor('initial-connection')
    baseline = identities()
    write(context / 'initial-private-identities.json', baseline)
    host_admission('initial')
    resource_proof = resources('initial')
    stage = 'member-read-and-live-lease'
    owner = Path(selection['source']) / 'tools/runtime-verify.rb'
    body = owner.read_text().split('    def read_smoke(connection_path)\n', 1)[1].split('    def resource_script', 1)[0]
    script = textwrap.dedent(re.search(r"<<~'JS'\n(.*?)^\s*JS$", body, re.M | re.S).group(1))
    member = json.loads(call('member-read', ['node', '-e', script, str(connection), selection['metadata'], selection['source']]))
    assert member['api_tls_verified'] and member['php_member_read'] and member['member']['login'] == 'test-user1'
    call('live-lease', ['node', str(Path(selection['source']) / 'tools/verify-live-lease.cjs'), str(connection),
                      selection['metadata'], selection['runtime'], str(root / 'state'), prep['configuration_path']])
    assert identities() == baseline
    post = {'schema': 1, 'generator': prep['generator'], 'complete': True,
            'source_ids': {k: current[k] for k in ('instance_id', 'run_id', 'artifact_id', 'artifact_sha256')},
            'resources': resource_proof, 'public_member_api_php_and_lease': True,
            'fresh_private_baseline': True, 'image_and_writable_disks_each_8GiB': True,
            'commands': list(commands), 'completed_campaign_or_stop_resume_claimed': False}
    write(T / 'finish-working-delivery-post-start6-proof.json', post)
    stage = 'direct-captures'
    capture = selection['capture'] + '/bin/vpsfree-kb-capture'
    for name, language, args, cwd in [
        ('cs-capture', 'cs', ['--cluster', 'same-slug', '--state-root', str(root / 'state'), '--output-root', str(output)], None),
        ('en-capture', 'en', ['--connection', str(connection), '--output-root', str(output)], None),
        ('en-default-cwd', 'en', ['--connection', str(connection)], str(output)),
    ]:
        stage = name + '-admission'
        descriptor(name + '-connection')
        assert identities() == baseline
        host_admission(name)
        if name != 'cs-capture':
            resources(name)
        stage = name
        call(name, [capture, *args, '--language', language, '--checkpoint', 'networking/ip-address-list'], cwd=cwd)
    stage = 'typed-fixture-proof'
    typed = json.loads(call('typed-fixture', ['node', prep['typed_resource_script'], selection['source'],
                    selection['metadata'], str(connection), str(output)]))
    assert typed['actual_numeric_result'] and typed['typed_resources'] == {'cpu':1, 'memory':1024, 'swap':0, 'diskspace':4096}
    write(context / 'typed-fixture-proof.json', typed)
    assert identities() == baseline
    stage = 'strict-validation-and-export'
    validate = selection['capture'] + '/bin/vpsfree-kb-validate'
    call('validate-update', [validate, '--update', '--output-root', str(output)])
    call('validate-strict', [validate, '--output-root', str(output)])
    rows = json.loads((output / 'tmp/capture-results.json').read_text())
    assert sorted((x['language'], x['id']) for x in rows) == [('cs','networking/ip-address-list'),('en','networking/ip-address-list')]
    assert all(x['provenance']['source'] == metadata and x['provenance']['run_id'] == current['run_id'] for x in rows)
    exporter = "require File.join(ARGV[0], 'tools/capture-export'); puts JSON.generate(KbCaptureArtifacts.export(ARGV[1], ARGV[2]))"
    exported = json.loads(call('locked-export', ['ruby','-e',exporter,selection['source'],str(output),prep['export_root']]))
except BaseException as error:
    failure = {'stage': stage, 'class': type(error).__name__}
finally:
    proof = {'schema':1, 'at':datetime.datetime.now(datetime.timezone.utc).isoformat(), 'generator':prep['generator'],
             'complete':failure is None, 'failure':failure, 'commands':commands, 'export':exported,
             'source_ids':{k:current[k] for k in ('instance_id','run_id','artifact_id','artifact_sha256')} if current else None,
             'original_campaign_replayed_or_relabelled':False, 'no_guest_sysctl_change':True,
             'limits':'Direct fresh-instance post-start/CS/EN/default-CWD/numeric fixture/strict inventory/export only. Visual acceptance, final media source checks and final stop remain separate.'}
    write(context / 'proof.json', proof)
    write(T / 'finish-working-delivery-direct-capture6-proof.json', proof)
    print(json.dumps({'complete':proof['complete'],'failure':failure,'exported':exported is not None}),flush=True)
sys.exit(0 if failure is None else 1)
