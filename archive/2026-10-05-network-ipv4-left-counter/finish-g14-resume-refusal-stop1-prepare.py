#!/usr/bin/env python3
"""Prepare one separately selected exact public G14 graceful stop; never launch."""
import datetime
import hashlib
import json
import os
import pathlib
import subprocess

tracking = pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
root = pathlib.Path('/home/aither/.local/state/vpsfree-kb-verification/2026-10-05-network-ipv4-left-counter-g14-public-continuation1')
old_context = root / 'public-smoke-context'
previous = json.loads((old_context / 'packet.json').read_bytes())
observation = json.loads((tracking / 'finish-g14-resume-key-observation1.json').read_bytes())
snapshot = observation['snapshot']
assert snapshot['run_id'] == '91c20a6a-948a-447c-aeb1-338b9581a0b4'
assert snapshot['runner_matches_launch'] and snapshot['own_claim_present'] and not snapshot['ready']
assert snapshot['phase'] == 'verifying' and not snapshot['processes_complete']
assert all(item['matches_recorded_identity'] for item in snapshot['children'])
assert observation['original_failed_attempt_sha256'] == 'f5a7f1c287912b1beb6d1608d4e66c670599265e571dd9786317126ad5954125'

context = root / 'resume-refusal-stop-context'
context.mkdir(mode=0o700)
packet = dict(previous)
packet['context'] = str(context)
packet['unit'] = 'kb-verify-network-counter-g14-resume-refusal-stop1.service'
packet['phase'] = 'separate-public-stop-after-resume-trust-refusal'
packet['argv'] = ['/nix/store/iz66p9qv5aybgkm4lq6ich7jgma04zrk-vpsfree-kb-devcluster/bin/vpsfree-kb-devcluster',
    '--state-root', '/home/aither/.local/state/vpsfree-kb-verification/2026-10-05-network-ipv4-left-counter-g14/campaign/state',
    'stop', 'same-slug', '--timeout', '900']
assert pathlib.Path(packet['argv'][0]).is_file()
packet['minimum_host_ram_bytes'] = 512 * 1024**2
packet['minimum_host_shm_bytes'] = 64 * 1024**2
packet['bound_files'] = []
paths = [tracking / 'finish-continuation-service-phase2.py', tracking / 'finish-g14-resume-refusal-stop1-launch.py',
    tracking / 'finish-lease-observation-review1-acceptance.json', tracking / 'finish-g14-resume-key-observation1.json',
    pathlib.Path(packet['argv'][0]), pathlib.Path('/nix/store/rm2h27hrml95lbwri4vcmg6f7jlkrbqp-source/cluster/lib/kb_runtime.rb')]
for path in paths:
    packet['bound_files'].append({'path': str(path), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
free = os.statvfs(packet['filesystem_path'])
free_bytes = free.f_bavail * free.f_frsize
ram = int(next(line for line in pathlib.Path('/proc/meminfo').read_text().splitlines() if line.startswith('MemAvailable:')).split()[1]) * 1024
shm = os.statvfs('/dev/shm'); shm_bytes = shm.f_bavail * shm.f_frsize
assert free_bytes > packet['reserve_bytes'] and ram > packet['minimum_host_ram_bytes'] and shm_bytes > packet['minimum_host_shm_bytes']
result = subprocess.run([packet['systemctl'], '--user', 'show', packet['unit'], '--property=LoadState'], capture_output=True, text=True)
assert 'LoadState=not-found' in result.stdout
packet_path = context / 'packet.json'
with os.fdopen(os.open(packet_path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600), 'w') as output:
    json.dump(packet, output, indent=2); output.write('\n')
proof = {'schema': 1, 'at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'kind': 'retained-g725-public-stop-v1',
    'generator': previous['generator'], 'harness_revision': observation['harness_revision'], 'real_admission': True,
    'unit': packet['unit'], 'context': str(context), 'packet_sha256': hashlib.sha256(packet_path.read_bytes()).hexdigest(),
    'instance_id': snapshot['instance_id'], 'run_id': snapshot['run_id'], 'artifact_id': snapshot['artifact_id'],
    'argv': packet['argv'], 'reserve_bytes': packet['reserve_bytes'], 'fresh_free_bytes': free_bytes,
    'decision': 'Separately selected one ordinary public graceful stop of the exact newly resumed owned G14 run, after its finite smoke unit ended at trust refusal. User continue/finish scope already includes ordinary stop; release guest RAM without deleting disks or evidence. Public controller must freshly authenticate exact launch/socket/peer and prove complete exit. No failed-unit replay, trust change, reset, unit/group kill, force, old-state cleanup, new pair or qualification pass.',
    'first_failure': 'Retain any refused/incomplete stop; no automatic repeat or expanded control authority.'}
target = tracking / 'finish-g14-resume-refusal-stop1-preparation.json'
with target.open('x') as output:
    json.dump(proof, output, indent=2); output.write('\n')
print(json.dumps({'prepared': True, 'unit': packet['unit'], 'argv': packet['argv'], 'new_disk_or_guest_allocation': 0}))
