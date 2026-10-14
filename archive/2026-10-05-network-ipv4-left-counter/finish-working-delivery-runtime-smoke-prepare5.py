#!/usr/bin/env python3
"""Prepare one exact public operation, without starting the verifier."""
import datetime
import hashlib
import json
import os
import pathlib
import stat
import tempfile

T = pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
os.umask(0o077)
def read(name):
    return json.loads((T / name).read_text())
def sha(path):
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()
def write(path, value):
    with path.open('x') as output:
        json.dump(value, output, indent=2)
        output.write('\n')

a = read('finish-working-delivery-package-realize4-acceptance.json')
c = read('finish-working-delivery-private-config5.json')
o = read('finish-working-delivery-admission-observation5.json')
lifetime = read('finish-working-delivery-user-lifetime5.json')
p = read('finish-working-delivery-closure-plan4.json')
m = read('finish-working-delivery-missing-closure-facts4.json')
k = read('finish-working-delivery-kernel-builder-proof4.json')
baseline = read('finish-runtime-reduction-retained-payload-baseline1.json')
gate = read('finish-practical-runtime-hosted1-acceptance1.json')
assert gate['result'] == 'passed' and a['accepted']
review = read('finish-practical-runtime-review1-disposition.json')
assert review['result'] == 'complete; one Advisory accepted; no Blocking or Important' and review['heads']['K'] == a['generator']
assert gate['rows'][0]['head'] == gate['rows'][1]['head'] == a['generator']
assert gate['rows'][2]['head'] == review['heads']['E']
assert p['exit_code'] == 0 and not p['kernel_derivations_to_build'] and not m['missing_facts']
assert o['kvm_api'] == 12 and lifetime['existing_lifetime_sufficient_for_later_context_gate'] and lifetime['user']['Linger'] == 'yes' and lifetime['system_manager_unit']['ActiveState'] == 'active' and not lifetime['system_manager_unit']['Job']
G = 1024**3
parent = pathlib.Path(c['private_parent'])
root = str(parent / 'campaign')
c['profile'] = {'services_memory_mib': 4096, 'node1_memory_mib': 4096, 'services_root_mib': 8192, 'node1_tank_gib': 8, 'topology': 'single', 'network': 'local'}
assert not pathlib.Path(root).exists()
capacity_path = parent / 'capacity5.json'
selection = a['selection']
source = json.loads(pathlib.Path(selection['metadata']).read_text())
config = json.loads(pathlib.Path(c['configuration']['path']).read_text())
assert sha(c['configuration']['path']) == c['configuration']['sha256']
bindings = {'kind': 'single-runtime-v1', 'source': source, 'selection': selection,
    'configuration': config, 'configuration_sha256': c['configuration']['sha256'],
    'root': root, 'capacity_receipt': str(capacity_path)}
staging_assessment = baseline['nar_bytes'] + m['nar_bytes']
publication_overlap = 8 * G
overlap = max(0, staging_assessment + publication_overlap - 16 * G)
assert k['builder_memory_mib'] == 4096
assert p['configuration_sha256'] == m['configuration_sha256'] == c['configuration']['sha256']
assert config['services']['memoryMiB'] == config['nodes']['node1']['memoryMiB'] == 4096
assert all(x['fstype'] == 'ext4' for x in o['roles'].values())
headroom, reserve, intrinsic = 8 * G, 16 * G, 24 * G
retained = o['retained_growth_bytes']
available = min(x['available_bytes'] for x in o['roles'].values())
assert len({x['device'] for x in o['roles'].values()}) == 1
required = intrinsic + m['nar_bytes'] + reserve + retained + headroom + overlap
assert available >= required and o['ram_available_bytes'] >= 10 * G and o['shm_available_bytes'] >= 9 * G
realized = [a['verify'], a['source'], *k['kernel_outputs']]
for path in realized:
    mode = os.lstat(path).st_mode
    assert stat.S_ISREG(mode) or stat.S_ISDIR(mode)
receipt = {'schema': 1, 'kind': 'single-runtime-v1', 'bindings': bindings, 'observed_at': o['at'],
    'roles': {role: {key: value for key, value in fact.items() if key != 'available_bytes'} for role, fact in o['roles'].items()},
    'owned_output': {'allocated_bytes': 0, 'apparent_bytes': 0}, 'realized_paths': realized,
    'missing_paths': [{'path': x['path'], 'kind': 'closure', 'nar_size': x['nar_size'], 'download_size': x['download_size']} for x in m['paths']],
    'resource_overheads': {
        'construction': {'ram_bytes': 2 * G, 'shm_bytes': G, 'assessment': 'One4096MiB image builder at one job/core, separately assessed2GiB host/process/build RAM and1GiB shared-memory margin. Sequential with runtime; unknown scratch monitored.'},
        'runtime_browser': {'ram_bytes': 2 * G, 'shm_bytes': G, 'assessment': 'One8GiB services/node1 pair plus separately assessed2GiB public CLI/Chromium/process RAM and1GiB shared-memory margin. Full before start/resume; incremental margins only after exact live capture continuity.'}},
    'filesystems': [{'device': o['roles']['store']['device'], 'reserve_bytes': reserve,
        'retained_growth_bytes': retained, 'build_headroom_bytes': headroom,
        'observed_available_bytes': available, 'construction_overlap_bytes': overlap,
        'construction_overlap_assessment': 'One shared ext4 filesystem; public Software.prepare/build finishes image construction before runner root-copy/tank allocation. Construction row: missing closures + assessed staging (prior services closure3127554904B plus current missing369808248B) +8GiB raw image + conservative8GiB publication-copy allowance. Runtime row: missing closures +24GiB image/root/tank outputs. Known excess=max(0,staging+publication_overlap-16GiB)=0. Prior staging is an assessment baseline, not current payload fit proof; unknown extra workfiles/scratch and any retained remnants stay covered by separate8GiB assessed headroom and live protected-reserve monitoring. No daemon scratch bound, zero staging or GC credit claimed.'}],
    'build_plan': {'scratch_bound': 'unknown', 'max_jobs': 1, 'cores': 1,
        'assessment': 'Public runtimePlan-derived image/toplevel/runner dry-run:Current exact plan and fetched-path sizes are recorded in closure-plan4 and missing-closure-facts4. No kernel compile planned. Fixed8GiB native fit gate inside public start precedes runner reserve/spawn. One immutable attempt after reviewed smaller services workload and positively completed sequential replacement; failure preserves evidence and requires a demonstrated-blocker repair before any separately admitted fresh attempt. No resize/replay/automatic cleanup.',
        'daemon_scratch_evidence': 'Current root-owned /nix/var/nix/builds exists on64769/ext4; system nix.conf has no build-dir override; retained native planning and Nix convention agree. Observation1 records actual filesystem. Unknown scratch monitored, no guessed upper bound.',
        'derivations': p['planned_derivations'],
        'kernel_substitutions': ['Exact generator/config-bound kernel-builder-proof4: both projected kernel derivations/all5outputs local recursive path-info, exact-output dry-run0/no compile.', 'Exact full image/toplevel/runner closure-plan4 has no kernel build; builder Linux6.18.48 out/modules are cached substitutes. Actual prepared kernel map must equal projected kernels.']},
    'capture_assessment': {'assessment': 'Optional same-instance inventory creates one real1CPU/1GiB/4GiB VPS. Node free memory must cover1GiB plus128MiB OS/ZFS margin; services256MiB live free margin/10000inodes; tank4GiB quota plus assessed1GiB template/metadata headroom. Finite assessment, not measured fit. Actual resource/quota/template checks remain mandatory; shortfall ends optional capture without upscale/replay.',
        'minimum_free_inodes': 10000, 'services_memory_bytes': 256 * 1024**2,
        'node_memory_bytes': G + 128 * 1024**2, 'template_metadata_bytes': G}}
assert receipt['roles']['state_images']['path'] == root
assert receipt['bindings']['root'] == root
write(capacity_path, receipt)
context = parent / 'runtime-smoke-context5'
context.mkdir(mode=0o700)
cwd = parent / 'ordinary-cwd5'
cwd.mkdir(mode=0o700)
tmp = pathlib.Path(tempfile.mkdtemp(prefix='kbf-', dir='/tmp'))
assert len(str(tmp).encode()) < 35 and stat.S_IMODE(tmp.stat().st_mode) == 0o700
environment = {key: os.environ[key] for key in ['HOME', 'USER', 'LOGNAME'] if key in os.environ}
environment.update(XDG_RUNTIME_DIR='/run/user/1000', PATH=selection['path'], LANG='C.UTF-8', TMPDIR=str(tmp),
    NIX_SSL_CERT_FILE=selection['certificates'], SSL_CERT_FILE=selection['certificates'],
    NIX_CONFIG='experimental-features = nix-command flakes\nmax-jobs = 1\ncores = 1\nextra-substituters = https://cache.vpsadminos.org\nextra-trusted-public-keys = cache.vpsadminos.org:wpIJlNZQIhS+0gFf1U3MC9sLZdLW3sh5qakOWGDoDrE=\n')
unit = 'kb-verify-network-counter-working5-runtime-smoke.service'
wrapper = T / 'finish-runtime-reduction-service-phase1.py'
bound = [c['configuration']['path'], str(capacity_path), selection['metadata'], a['selection_path'], str(wrapper)]
packet = {'schema': 1, 'generator': a['generator'], 'phase': 'runtime-smoke', 'unit': unit,
    'context': str(context), 'campaign_root': root,
    'systemctl': '/nix/store/khnfirshq5j299s6sfj0laxj0vr7gaa6-systemd-260.2/bin/systemctl',
    'manager_cgroup': o['user_manager']['ControlGroup'], 'exec_cgroup': o['exec_cgroup'].split('::', 1)[1],
    'cwd': str(cwd), 'environment': environment,
    'argv': [a['verify'] + '/bin/vpsfree-kb-verify', '--root', root, '--config', c['configuration']['path'],
        '--capacity-receipt', str(capacity_path), '--phase', 'runtime-smoke'],
    'bound_files': [{'path': path, 'sha256': sha(path)} for path in bound],
    'filesystem_path': '/nix/store', 'reserve_bytes': reserve + retained,
    'minimum_host_ram_bytes': G, 'minimum_host_shm_bytes': 512 * 1024**2,
    'expected_kernels': k['kernel_map']}
packet_path = context / 'packet.json'
write(packet_path, packet)
public = {'schema': 1, 'at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'kind': 'single-runtime-v1', 'generator': a['generator'], 'extension': '1c68b426620dda5b70caa2265a89a37ef871cfc5',
    'phase': 'runtime-smoke', 'unit': unit, 'context': str(context), 'packet_path': str(packet_path),
    'packet_sha256': sha(packet_path), 'capacity_path': str(capacity_path), 'capacity_sha256': sha(capacity_path),
    'configuration_sha256': c['configuration']['sha256'], 'real_admission': True,
    'one_finite_attempt': True, 'profile': c['profile'],
    'filesystem': {'observed_available_bytes': available, 'intrinsic_new_output_bytes': intrinsic,
        'missing_closure_nar_bytes': m['nar_bytes'], 'retained_sparse_growth_bytes': retained,
        'base_reserve_bytes': reserve, 'assessed_build_headroom_bytes': headroom,
        'assessed_construction_overlap_bytes': overlap, 'assessed_staging_bytes': staging_assessment, 'conservative_publication_copy_bytes': publication_overlap, 'uncommitted_available_after_all_admission_charges': available - required},
    'host': {'observed_ram_available_bytes': o['ram_available_bytes'], 'observed_shm_available_bytes': o['shm_available_bytes'],
        'prestart_peak_ram_bytes': 10 * G, 'prestart_peak_shm_bytes': 9 * G},
    'evidence': ['finish-practical-runtime-hosted1-acceptance1.json', 'finish-working-delivery-package-realize4-acceptance.json',
        'finish-working-delivery-admission-observation5.json', 'finish-working-delivery-user-lifetime5.json',
        'finish-working-delivery-plan-projection4.json', 'finish-working-delivery-kernel-builder-proof4.json',
        'finish-working-delivery-closure-plan4.json', 'finish-working-delivery-missing-closure-facts4.json'],
    'limits': 'Native8GiB fit remains unproved; unknown scratch monitored. Same ordinary registry/disjoint ports. Exact ordinary user-service RUNNING before verifier. Failure ends this immutable attempt; task continues through demonstrated-blocker repairs. No replay/upscale/automatic old cleanup/reset/unit retirement/default integration/activation.'}
write(T / 'finish-working-delivery-runtime-smoke5-preparation.json', public)
print(json.dumps({'admitted_one_attempt': True, 'unit': unit, 'new_disk_gib': 24, 'guest_ram_gib': 8,
    'remaining_uncommitted_gib': (available - required) / G,
    'preparation': 'finish-working-delivery-runtime-smoke5-preparation.json'}))
