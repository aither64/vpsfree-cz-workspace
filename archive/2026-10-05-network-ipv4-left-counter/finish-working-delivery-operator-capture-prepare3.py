"""Prepare the same-pair canonical capture after positive public continuity."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import stat

os.umask(0o077)
tracking = Path(__file__).resolve().parent

def read(path):
    return json.loads(Path(path).read_text())

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def write(path, value):
    with Path(path).open('x') as output:
        json.dump(value, output, indent=2)
        output.write('\n')

prior = read(tracking / 'finish-working-delivery-runtime-smoke4-preparation.json')
packet = read(prior['packet_path'])
assert sha(prior['packet_path']) == prior['packet_sha256']
package = read(tracking / 'finish-working-delivery-package-realize3-acceptance.json')
acceptance = read(tracking / 'finish-working-delivery-public-continuity5-acceptance.json')
proof_path = tracking / 'finish-working-delivery-public-continuity5-proof.json'
cycle = read(proof_path)
assert acceptance['complete'] and acceptance['proof_sha256'] == sha(proof_path)
assert cycle['complete'] and cycle['complete_exit']['complete'] and cycle['sentinel_continuity_proved']
assert cycle['generator'] == package['generator'] == prior['generator']
root = Path(packet['campaign_root'])
failed = root / 'receipts/runtime-smoke-attempt.json'
assert sha(failed) == cycle['original_failed_attempt_sha256']
assert not (root / 'receipts/runtime-smoke.json').exists()
capacity = read(prior['capacity_path'])
assert sha(prior['capacity_path']) == prior['capacity_sha256']
assert sha(root / 'config.json') == prior['configuration_sha256']
tmp = Path(packet['environment']['TMPDIR'])
assert tmp.resolve(strict=True) == tmp and not tmp.is_symlink()
entry = tmp.stat()
assert entry.st_uid == os.getuid() and stat.S_IMODE(entry.st_mode) == 0o700
assert len(str(tmp).encode()) < 35

margin = capacity['resource_overheads']['runtime_browser']
ram = int(next(line for line in Path('/proc/meminfo').read_text().splitlines()
               if line.startswith('MemAvailable:')).split()[1]) * 1024
shm = os.statvfs('/dev/shm')
shm_free = shm.f_bavail * shm.f_frsize
assert ram >= margin['ram_bytes'] and shm_free >= margin['shm_bytes']
growth = 0
paths = [root / 'state/clusters/same-slug/disks' / name for name in cycle['continuity']['disks']]
paths += [Path(image['path']) for image in cycle['continuity']['images']]
seen = set()
for path in paths:
    entry = path.stat()
    key = (entry.st_dev, entry.st_ino)
    if key not in seen:
        seen.add(key)
        growth += max(0, entry.st_size - entry.st_blocks * 512)
fs = os.statvfs(packet['filesystem_path'])
available = fs.f_bavail * fs.f_frsize
budget = capacity['filesystems'][0]
assert Path(packet['filesystem_path']).stat().st_dev == budget['device']
required = growth + budget['reserve_bytes'] + budget['retained_growth_bytes'] + budget['build_headroom_bytes']
assert available >= required

output = root / 'output'
assert output.is_dir() and not output.is_symlink() and not any(output.iterdir())
assert output.stat().st_uid == os.getuid() and stat.S_IMODE(output.stat().st_mode) == 0o700
context = root.parent / 'operator-capture-context3'
context.mkdir(mode=0o700)
export = root / 'export-window3'
assert not export.exists() and not export.is_symlink()
helper = tracking / 'finish-working-delivery-operator-capture-window3.py'
packet.update(phase='operator-prepared-bilingual-capture',
              unit='kb-verify-network-counter-working4-capture.service',
              context=str(context),
              argv=['/nix/store/5a0h3d6488628sh6w1ccqk8dizvmp8ji-python3-3.13.15-env/bin/python3.13', str(helper)])
packet['environment'].update(NODE_PATH=package['selection']['node_path'],
    PLAYWRIGHT_BROWSERS_PATH=package['selection']['browsers'], FONTCONFIG_FILE=package['selection']['fonts'],
    GEM_HOME=package['selection']['gem_home'], GEM_PATH=package['selection']['gem_home'])
packet['bound_files'] += [{'path': str(path), 'sha256': sha(path)} for path in (helper, proof_path, failed)]
packet_path = context / 'packet.json'
write(packet_path, packet)
public = {'schema': 1, 'at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'kind': 'single-runtime-v1', 'generator': prior['generator'], 'extension': prior['extension'],
    'phase': packet['phase'], 'unit': packet['unit'], 'context': str(context),
    'packet_path': str(packet_path), 'packet_sha256': sha(packet_path),
    'capacity_path': prior['capacity_path'], 'real_admission': True, 'one_finite_window': True,
    'public_continuity_proof_sha256': sha(proof_path), 'output_root': str(output), 'export_root': str(export),
    'resumed': cycle['resumed'], 'short_private_tmpdir': str(tmp),
    'host': {'ram_available_bytes': ram, 'shm_available_bytes': shm_free,
        'additional_ram_required_bytes': margin['ram_bytes'], 'additional_shm_required_bytes': margin['shm_bytes'],
        'disk_available_bytes': available, 'disk_required_bytes': required},
    'limits': 'One same-resumed-instance public packaged CS/EN/default-CWD capture, strict full-inventory validation and five-file export. Existing positive guest/template/quota gates; guarded temporary node reserve1048576->65536 with restoration. No new VM/image/upscale/replay/forged Campaign completion. Visual acceptance and final stop remain separate.'}
write(tracking / 'finish-working-delivery-operator-capture-window3-preparation.json', public)
print(json.dumps({'capture_prepared': True, 'same_resumed_instance': cycle['resumed'], 'generator': prior['generator']}))
