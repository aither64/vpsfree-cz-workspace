"""First short-TMPDIR browser read; original failed operations are retained."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

os.umask(0o077)
tracking = Path(__file__).resolve().parent
prep = json.loads((tracking / 'finish-working-delivery-public-member-read3-preparation.json').read_text())
packet = json.loads(Path(prep['packet_path']).read_text())
root = Path(packet['campaign_root'])
context = Path(prep['context']) / 'operation'
context.mkdir(mode=0o700)
pkg = json.loads((tracking / 'finish-working-delivery-package-realize3-acceptance.json').read_text())
s = pkg['selection']
diagnosis = json.loads((tracking / 'finish-working-delivery-runtime-smoke4-failure-proof1.json').read_text())
failed = root / 'receipts/runtime-smoke-attempt.json'
assert hashlib.sha256(failed.read_bytes()).hexdigest() == diagnosis['failed_attempt_sha256']
assert not (root / 'receipts/runtime-smoke.json').exists()
records = []

def call(name, argv):
    with (context / (name + '.stdout')).open('xb') as out, (context / (name + '.stderr')).open('xb') as err:
        r = subprocess.run(argv, stdin=subprocess.DEVNULL, stdout=out, stderr=err, env=packet['environment'], cwd=packet['cwd'])
    records.append({'name': name, 'exit_code': r.returncode,
        'stdout_sha256': hashlib.sha256((context / (name + '.stdout')).read_bytes()).hexdigest(),
        'stderr_sha256': hashlib.sha256((context / (name + '.stderr')).read_bytes()).hexdigest()})
    if r.returncode:
        raise RuntimeError('Native public read failed; private diagnostics retained')
    return (context / (name + '.stdout')).read_bytes()

try:
    raw = call('connection', [s['runtime'] + '/bin/vpsfree-kb-devcluster', '--state-root', str(root / 'state'), 'connection', 'same-slug'])
    d = json.loads(raw)
    assert d['provenance']['source'] == json.loads(Path(s['metadata']).read_text())
    assert all(d[k] == diagnosis['source_ids'][k] for k in ['instance_id', 'run_id', 'artifact_id', 'artifact_sha256'])
    connection = context / 'connection.json'
    connection.write_bytes(raw)
    text = Path(s['source'], 'tools/runtime-verify.rb').read_text()
    assert hashlib.sha256(text.encode()).hexdigest() == '3adf8e4c33c2754ed4013a3b266592f82670ddf0154e27a040676ecca39e94fb'
    start = text.index("      script = <<~'JS'", text.index('    def read_smoke'))
    end = text.index('\n      JS', start)
    script = '\n'.join(x[8:] for x in text[start:end].splitlines()[1:])
    value = json.loads(call('member-browser-read', ['node', '-e', script, str(connection), s['metadata'], s['source']]))
    assert value['api_tls_verified'] and value['php_member_read'] and value['member']['login'] == 'test-user1'
    call('live-lease', ['node', str(Path(s['source'], 'tools/verify-live-lease.cjs')), str(connection), s['metadata'], s['runtime'], str(root / 'state'), str(root / 'config.json')])
    assert hashlib.sha256(failed.read_bytes()).hexdigest() == diagnosis['failed_attempt_sha256']
    proof = {'schema': 1, 'complete': True, 'generator': prep['generator'],
        'api_tls_verified': True, 'ordinary_member_php_read': True, 'real_public_live_lease': True,
        'instance_id': d['instance_id'], 'run_id': d['run_id'], 'artifact_id': d['artifact_id'], 'artifact_sha256': d['artifact_sha256'],
        'short_private_tmpdir': packet['environment']['TMPDIR'], 'commands': records,
        'original_failed_attempt_sha256': diagnosis['failed_attempt_sha256'], 'original_campaign_completed': False,
        'lifecycle_or_fixture_mutation': False, 'limits': 'Separate public browser and lease proof; stop/resume/capture remain pending.'}
    with (tracking / 'finish-working-delivery-public-member-read3-proof.json').open('x') as out:
        json.dump(proof, out, indent=2); out.write('\n')
    print(json.dumps({'complete': True, 'ordinary_member_php_read': True, 'public_live_lease': True}), flush=True)
except BaseException as error:
    with (context / 'failed.json').open('x') as out:
        json.dump({'failure_class': type(error).__name__, 'commands': records}, out, indent=2); out.write('\n')
    print(json.dumps({'complete': False, 'failure_class': type(error).__name__, 'private_diagnostics': str(context)}), flush=True)
    sys.exit(1)
