#!/usr/bin/env python3
"""Prepare capture only after the exact real runtime receipt succeeds."""
import datetime
import hashlib
import json
import os
import pathlib

T = pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
os.umask(0o077)

def read(path):
    return json.loads(pathlib.Path(path).read_text())

def sha(path):
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()

def write(path, value):
    with pathlib.Path(path).open('x') as output:
        json.dump(value, output, indent=2)
        output.write('\n')

prep = read(T / 'finish-working-delivery-runtime-smoke2-preparation.json')
packet = read(prep['packet_path'])
assert sha(prep['packet_path']) == prep['packet_sha256']
parent = pathlib.Path(prep['context']).parent
root = pathlib.Path(packet['campaign_root'])
native_path = pathlib.Path(prep['context']) / 'result.json'
native = read(native_path)
assert native['complete'] and native['exit_code'] == 0 and not native.get('cancel_reason') and not native.get('wrapper_failure')
assert native['generator'] == packet['generator'] and native['phase'] == 'runtime-smoke'
runtime_path = root / 'receipts/runtime-smoke.json'
runtime = read(runtime_path)
assert runtime['schema'] == 1 and runtime['kind'] == 'single-runtime-v1' and runtime['phase'] == 'runtime-smoke' and runtime['complete']
capacity = read(prep['capacity_path'])
assert runtime['inputs'] == capacity['bindings']
assert capacity['roles']['state_images']['path'] == str(root)
assert sha(prep['capacity_path']) == prep['capacity_sha256']
assert sha(runtime['inputs']['selection']['metadata']) == next(x['sha256'] for x in packet['bound_files'] if x['path'] == runtime['inputs']['selection']['metadata'])
accepted_path = root / 'accepted-runtime.json'
accepted = read(accepted_path)
assert accepted['provenance']['source'] == runtime['inputs']['source']
assert accepted['capabilities'] and accepted['run_id'] and accepted['artifact_id']

# Existing guests already reduce these availability figures. Admit only the
# assessed additional browser/CLI demand here; the public verifier independently
# proves live continuity and accounts actual disk blocks before fixture work.
ram = int(next(line for line in pathlib.Path('/proc/meminfo').read_text().splitlines() if line.startswith('MemAvailable:')).split()[1]) * 1024
shm = os.statvfs('/dev/shm')
shm_available = shm.f_bavail * shm.f_frsize
fs = os.statvfs(packet['filesystem_path'])
available = fs.f_bavail * fs.f_frsize
overhead = capacity['resource_overheads']['runtime_browser']
assert ram >= overhead['ram_bytes'] and shm_available >= overhead['shm_bytes']
assert available >= packet['reserve_bytes']
context = parent / 'bilingual-capture-context'
context.mkdir(mode=0o700)
packet['phase'] = 'bilingual-capture'
packet['unit'] = 'kb-verify-network-counter-working2-bilingual-capture.service'
packet['context'] = str(context)
assert packet['argv'][-2:] == ['--phase', 'runtime-smoke']
packet['argv'][-1] = 'bilingual-capture'
packet['bound_files'] += [{'path': str(path), 'sha256': sha(path)} for path in (runtime_path, accepted_path)]
packet_path = context / 'packet.json'
write(packet_path, packet)
public = {'schema': 1, 'at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'kind': 'single-runtime-v1', 'generator': packet['generator'], 'extension': prep['extension'],
    'phase': packet['phase'], 'unit': packet['unit'], 'context': str(context),
    'packet_path': str(packet_path), 'packet_sha256': sha(packet_path),
    'capacity_path': prep['capacity_path'], 'capacity_sha256': prep['capacity_sha256'],
    'configuration_sha256': prep['configuration_sha256'], 'real_admission': True,
    'one_finite_attempt': True, 'runtime_result_sha256': sha(native_path),
    'runtime_receipt_sha256': sha(runtime_path), 'accepted_runtime_sha256': sha(accepted_path),
    'instance_id': accepted['instance_id'], 'run_id': accepted['run_id'],
    'artifact_id': accepted['artifact_id'], 'artifact_sha256': accepted['artifact_sha256'],
    'host': {'ram_available_bytes': ram, 'shm_available_bytes': shm_available,
        'additional_ram_required_bytes': overhead['ram_bytes'], 'additional_shm_required_bytes': overhead['shm_bytes'],
        'available_disk_bytes': available, 'protected_reserve_bytes': packet['reserve_bytes']},
    'limits': 'Same completed resumed instance only. Public verifier repeats attestation, continuity, live capacity and guest/template/quota checks before fixtures. Original runtime unit retains its guests. No new VM, replay, upscale, cleanup or unit retirement.'}
write(T / 'finish-working-delivery-bilingual-capture-preparation.json', public)
print(json.dumps({'admitted_same_instance': True, 'phase': packet['phase'], 'instance_id': accepted['instance_id'],
    'additional_ram_gib': overhead['ram_bytes'] / 1024**3, 'additional_shm_gib': overhead['shm_bytes'] / 1024**3}))
