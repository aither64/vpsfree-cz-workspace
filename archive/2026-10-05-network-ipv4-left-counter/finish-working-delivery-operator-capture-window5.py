"""Finite same-instance captures from the genuinely accepted corrected source."""
import datetime, hashlib, json, os, re, shlex, stat, subprocess, sys, textwrap
from pathlib import Path

os.umask(0o077)
T = Path(__file__).resolve().parent
prep = json.loads((T / 'finish-working-delivery-operator-capture-working5-preparation.json').read_text())
packet = json.loads(Path(prep['packet_path']).read_text())
context = Path(prep['context']) / 'operation'
context.mkdir(mode=0o700)
root = Path(packet['campaign_root'])
selection = json.loads((T / 'finish-working-delivery-package-realize5-acceptance.json').read_text())['selection']
metadata = json.loads(Path(selection['metadata']).read_text())
update = json.loads((T / 'finish-working-delivery-public-update5-proof.json').read_text())
assert update['complete'] and update['old_complete_process_receipt'] and update['public_member_api_php_and_lease']
assert update['generator'] == prep['generator'] == metadata['revision']
baseline = json.loads((root / 'continuity.json').read_text())
directory = root / 'state/clusters/same-slug'
capacity = json.loads(Path(prep['capacity_path']).read_text())
environment = packet['environment']
runtime = [selection['runtime'] + '/bin/vpsfree-kb-devcluster', '--state-root', str(root / 'state')]
output = Path(prep['output_root'])
commands = []
stage = 'current-source-attestation'
current = None
failure = None
export = None
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
    commands.append({'name': name, 'stage': stage, 'exit_code': result.returncode,
                     'stdout_sha256': sha(private / 'stdout'), 'stderr_sha256': sha(private / 'stderr')})
    if result.returncode:
        raise RuntimeError('native command refused; private diagnostics retained')
    return (private / 'stdout').read_bytes()

def engine(name, args, data=''):
    return call(name, runtime + [args[0], 'same-slug', *args[1:]], data)

def descriptor(name):
    raw = engine(name, ['connection'])
    value = json.loads(raw)
    assert value['provenance']['source'] == metadata
    assert all(value[k] == update['source_ids'][k] for k in ('instance_id', 'run_id', 'artifact_id', 'artifact_sha256'))
    path = context / (name + '.json')
    path.write_bytes(raw)
    return value, path

def continuity(name):
    identities = baseline['identities']
    for filename, digest in identities['credentials'].items():
        p = directory / 'credentials' / filename
        s = p.lstat()
        assert stat.S_ISREG(s.st_mode) and s.st_uid == os.getuid() and stat.S_IMODE(s.st_mode) == 0o600
        assert sha(p) == digest
    assert sha(directory / 'accounts.json') == identities['accounts_sha256']
    assert sha(directory / 'credentials/known_hosts') == prep['known_hosts_sha256']
    for filename, expected in identities['disks'].items():
        s = (directory / 'disks' / filename).lstat()
        assert stat.S_ISREG(s.st_mode) and s.st_uid == os.getuid()
        assert {'device': s.st_dev, 'inode': s.st_ino, 'size': s.st_size} == expected
    for filename, digest in identities['artifacts'].items():
        assert sha(directory / filename) == digest
    assert sha(directory / ('artifact-' + current['artifact_id'] + '.json')) == current['artifact_sha256']
    for path, digest in update['original_receipt_sha256'].items():
        assert sha(path) == digest
    for machine, expected in baseline['sentinels'].items():
        sentinel = '/root/kb-root-sentinel' if machine == 'services' else '/tank/kb-data-sentinel'
        observed = engine(name + '-' + machine + '-sentinel', ['ssh', machine, '--', 'sha256sum', sentinel]).decode().split()[0]
        assert observed == expected

def host_admission(name):
    ram = int(next(x for x in Path('/proc/meminfo').read_text().splitlines() if x.startswith('MemAvailable:')).split()[1]) * 1024
    shm = os.statvfs('/dev/shm')
    margins = capacity['resource_overheads']['runtime_browser']
    assert ram >= margins['ram_bytes'] and shm.f_bavail * shm.f_frsize >= margins['shm_bytes']
    growth = sum(max(0, p.stat().st_size - p.stat().st_blocks * 512) for p in (directory / 'disks').glob('*.img'))
    fs = os.statvfs('/nix/store')
    free = fs.f_bavail * fs.f_frsize
    required = growth + prep['other_retained_growth_bytes'] + 16 * 1024**3 + 1024**3
    assert free >= required
    write(context / (name + '-host.json'), {'available_ram_bytes': ram, 'available_shm_bytes': shm.f_bavail * shm.f_frsize,
        'incremental_margins': margins, 'free_bytes': free, 'required_bytes': required,
        'own_writable_growth_bytes': growth, 'capture_output_headroom_bytes': 1024**3,
        'immutable_image_holes_charged_as_future_writes': False})

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
        raw = engine(name + '-' + machine + '-resources', ['ssh', machine, '--', 'sh', '-s'], guard + blocks[0] + extra).decode()
        numeric = {k: int(v) for k, v in re.findall(r'^([a-z_]+)=([0-9]+)$', raw, re.M)}
        expected = ['available_memory_bytes', 'available_bytes', 'available_inodes'] if machine == 'services' else ['available_memory_bytes', 'tank_available_bytes']
        assert sorted(numeric) == sorted(expected)
        observations[machine] = dict(numeric, pressure='\n'.join(x for x in raw.splitlines() if not re.fullmatch(r'[a-z_]+=[0-9]+', x)))
    assessed = capacity['capture_assessment']
    assert observations['services']['available_bytes'] >= 1024**3
    assert observations['services']['available_inodes'] >= assessed['minimum_free_inodes']
    assert observations['services']['available_memory_bytes'] >= assessed['services_memory_bytes']
    assert observations['node1']['available_memory_bytes'] >= assessed['node_memory_bytes']
    assert observations['node1']['tank_available_bytes'] >= 4 * 1024**3 + assessed['template_metadata_bytes']
    write(context / (name + '-resources.json'), {'observations': observations, 'assessment': assessed,
        'source_script_sha256': sha(owner), 'no_guest_sysctl_change': True})

try:
    current, connection = descriptor('initial-connection')
    capture = selection['capture'] + '/bin/vpsfree-kb-capture'
    for name, language, args, cwd in [
        ('cs-capture', 'cs', ['--cluster', 'same-slug', '--state-root', str(root / 'state'), '--output-root', str(output)], None),
        ('en-capture', 'en', ['--connection', str(connection), '--output-root', str(output)], None),
        ('en-default-cwd', 'en', ['--connection', str(connection)], str(output)),
    ]:
        stage = name + '-admission'
        current, _ = descriptor(name + '-connection')
        continuity(name)
        host_admission(name)
        resources(name)
        stage = name
        call(name, [capture, *args, '--language', language, '--checkpoint', 'networking/ip-address-list'], cwd=cwd)
    stage = 'typed-fixture-result-proof'
    typed = json.loads(call('typed-resource-proof', ['node', prep['typed_resource_script'], selection['source'],
        selection['metadata'], str(connection), str(output)]))
    assert typed['actual_numeric_result'] and typed['typed_resources'] == {'cpu': 1, 'memory': 1024, 'swap': 0, 'diskspace': 4096}
    write(context / 'typed-fixture-result.json', typed)
    continuity('after-captures')
    stage = 'strict-validation-and-locked-export'
    validate = selection['capture'] + '/bin/vpsfree-kb-validate'
    call('validate-update', [validate, '--update', '--output-root', str(output)])
    call('validate-strict', [validate, '--output-root', str(output)])
    rows = json.loads((output / 'tmp/capture-results.json').read_bytes())
    assert sorted((x['language'], x['id']) for x in rows) == [('cs', 'networking/ip-address-list'), ('en', 'networking/ip-address-list')]
    assert all(x['provenance']['source'] == metadata and x['provenance']['run_id'] == current['run_id'] for x in rows)
    exporter = "require File.join(ARGV[0], 'tools/capture-export'); puts JSON.generate(KbCaptureArtifacts.export(ARGV[1], ARGV[2]))"
    export = json.loads(call('five-file-export', ['ruby', '-e', exporter, selection['source'], str(output), prep['export_root']]))
except BaseException as error:
    failure = {'stage': stage, 'class': type(error).__name__}
finally:
    proof = {'schema': 1, 'at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'generator': prep['generator'],
        'complete': failure is None, 'failure': failure, 'commands': commands, 'export': export,
        'source_ids': {k: current[k] for k in ('instance_id', 'run_id', 'artifact_id', 'artifact_sha256')} if current else None,
        'no_guest_sysctl_change': True, 'original_campaign_replayed_or_relabelled': False,
        'limits': 'Same genuinely accepted source, stock node4GiB, CS/EN/default-CWD captures, typed fixture result, strict validation and locked five-file export. Visual acceptance/final ordinary stop remain separate.'}
    write(context / 'proof.json', proof)
    write(T / 'finish-working-delivery-operator-capture-working5-proof.json', proof)
    print(json.dumps({'complete': proof['complete'], 'failure': failure, 'exported': export is not None}), flush=True)
sys.exit(0 if failure is None else 1)
