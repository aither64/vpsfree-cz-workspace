"""Read only bounded numeric node memory on the accepted artifact after failed browser launch."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess

os.umask(0o077)
tracking = Path(__file__).resolve().parent
prep = json.loads((tracking / 'finish-working-delivery-runtime-smoke3-preparation.json').read_text())
packet = json.loads(Path(prep['packet_path']).read_text())
result = json.loads((Path(prep['context']) / 'result.json').read_text())
assert result['complete'] and result['exit_code'] == 1 and not result.get('cancel_reason') and not result.get('wrapper_failure')
root = Path(packet['campaign_root'])
diagnosis = json.loads((tracking / 'finish-working-delivery-browser-path-diagnosis1.json').read_text())
failed_attempt = root / 'receipts/runtime-smoke-attempt.json'
assert hashlib.sha256(failed_attempt.read_bytes()).hexdigest() == diagnosis['failed_attempt_sha256']
assert not (root / 'receipts/runtime-smoke.json').exists()
package = json.loads((tracking / 'finish-working-delivery-package-realize2-acceptance.json').read_text())
selection = package['selection']
source = json.loads(Path(selection['metadata']).read_text())
accepted = json.loads((root / 'smoke-connection.json').read_text())
assert all(accepted[key] == diagnosis[key] for key in ['instance_id', 'run_id', 'artifact_id', 'artifact_sha256'])
context = root.parent / 'node-memory-observation4'
context.mkdir(mode=0o700)
base = [selection['runtime'] + '/bin/vpsfree-kb-devcluster', '--state-root', str(root / 'state')]
environment = packet['environment']
commands = []

def call(name, args, data=''):
    with (context / (name + '.stdout')).open('xb') as out, (context / (name + '.stderr')).open('xb') as err:
        native = subprocess.run(base + args, input=data.encode(), stdout=out, stderr=err, env=environment, cwd=packet['cwd'])
    commands.append({'name': name, 'native_exit_code': native.returncode,
        'stdout_sha256': hashlib.sha256((context / (name + '.stdout')).read_bytes()).hexdigest(),
        'stderr_sha256': hashlib.sha256((context / (name + '.stderr')).read_bytes()).hexdigest()})
    if native.returncode:
        raise RuntimeError('Public numeric observation failed; diagnostics retained privately')
    return (context / (name + '.stdout')).read_bytes()

status = json.loads(call('status', ['status', 'same-slug']))
assert status['found'] and status['ready'] and status['state'] == 'ready'
descriptor = json.loads(call('connection', ['connection', 'same-slug']))
assert descriptor == accepted and descriptor['provenance']['source'] == source
identity = json.loads(call('node-identity', ['ssh', 'same-slug', 'node1', '--', 'cat', '/etc/vpsfree-kb-capture.json']))
assert identity == descriptor['provenance']['guest_identity']
closure = call('node-closure', ['ssh', 'same-slug', 'node1', '--', 'readlink', '-f', '/run/current-system']).decode().strip()
assert closure == descriptor['provenance']['machine_toplevels']['node1']
script = r'''set -eu
awk '$1 ~ /^(MemTotal|MemFree|MemAvailable|Cached|SReclaimable|SUnreclaim):$/ { sub(/:$/, "", $1); if ($2 !~ /^[0-9]+$/ || $3 != "kB") exit 1; print $1 "_KiB=" $2; count++ } END { if (count != 6) exit 1 }' /proc/meminfo
reserve=$(cat /proc/sys/vm/min_free_kbytes)
printf 'min_free_kbytes_KiB=%s\n' "$reserve"
if test -r /proc/pressure/memory; then
  printf 'PSI_PRESENT=1\n'
  cat /proc/pressure/memory
else
  printf 'PSI_PRESENT=0\n'
fi
if test -r /proc/spl/kstat/zfs/arcstats; then
  awk '$1 ~ /^(size|c|c_min|c_max)$/ { if ($3 !~ /^[0-9]+$/) exit 1; print "ARC_" $1 "_bytes=" $3 }' /proc/spl/kstat/zfs/arcstats
fi
'''
raw = call('node-numeric-memory', ['ssh', 'same-slug', 'node1', '--', 'sh', '-s'], script).decode()
numeric = {}
pressure = []
for line in raw.splitlines():
    if '=' in line and line.split('=', 1)[1].isdigit():
        key, value = line.split('=', 1)
        numeric[key] = int(value)
    elif line.startswith(('some ', 'full ')):
        pressure.append(line)
    else:
        raise RuntimeError('Unexpected numeric observation output')
required = {'MemTotal_KiB', 'MemFree_KiB', 'MemAvailable_KiB', 'Cached_KiB', 'SReclaimable_KiB', 'SUnreclaim_KiB', 'min_free_kbytes_KiB', 'PSI_PRESENT'}
assert required <= numeric.keys()
value = {'schema': 1, 'at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'generator': prep['generator'],
    'instance_id': accepted['instance_id'], 'run_id': accepted['run_id'], 'artifact_id': accepted['artifact_id'],
    'source_identity_and_closure_matched': True, 'numeric_observations': numeric, 'pressure': pressure,
    'native_commands': commands, 'original_failed_attempt_sha256': hashlib.sha256(failed_attempt.read_bytes()).hexdigest(), 'runtime_completion_receipt_absent': True,
    'limits': 'Read-only numeric observations; no tuning, fixture mutation, resource increase, capture admission or exhaustion claim.'}
with (tracking / 'finish-working-delivery-node-memory-observation4.json').open('x') as output:
    json.dump(value, output, indent=2)
    output.write('\n')
print(json.dumps({'numeric_observation': 'complete', 'memory_available_bytes': numeric['MemAvailable_KiB'] * 1024,
    'reserve_bytes': numeric['min_free_kbytes_KiB'] * 1024, 'fixture_mutation': False}))
