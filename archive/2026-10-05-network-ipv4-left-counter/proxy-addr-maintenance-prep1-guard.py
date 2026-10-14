import copy
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path


tracking = Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
repo = Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin-webui-proxy-addr')
base = '02ac0c7de1a588dbb14a18e652fe3f7e9b45cc51'
prefix = 'proxy-addr-maintenance-prep1'
mode = sys.argv[1]
assert mode in ['before', 'remote', 'lock', 'receipts', 'ready']


def git(*args):
    return subprocess.check_output(['git', '-C', str(repo), *args], text=True)


def original(name):
    return git('show', f'{base}:{name}')


assert git('rev-parse', 'HEAD').strip() == base
assert git('branch', '--show-current').strip() == 'dev/proxy-addr-patch'
assert git('remote', 'get-url', 'origin').strip() == 'git@github.com:vpsfreecz/vpsadmin-webui.git'
assert not git('diff', '--cached', '--name-only').strip(), 'Unexpected staged changes'
allowed = set() if mode in ['before', 'remote'] else {'bff/package-lock.json'}
if mode == 'ready':
    allowed |= {'packages/bff.nix', 'docs/design/PACKAGING.md', 'docs/work-log/2026-10-06-proxy-addr-patch.md'}
changed = set(filter(None, git('diff', base, '--name-only').splitlines()))
untracked = set(filter(None, git('ls-files', '--others', '--exclude-standard').splitlines()))
assert (changed | untracked) <= allowed, f'Out-of-scope changes: {(changed | untracked) - allowed}'

if mode in ['before', 'remote']:
    assert not (repo / 'node_modules').exists()
    assert not (repo / 'bff/node_modules').exists()
    if mode == 'remote':
        rows = (tracking / f'{prefix}-remote-base.log').read_text().splitlines()
        assert rows == [f'{base}\trefs/heads/main'], 'Remote main advanced or maintenance branch already published'
    print('Exact clean maintenance base; both npm installations are absent')
    sys.exit(0)

old = json.loads(original('bff/package-lock.json'))
current = json.loads((repo / 'bff/package-lock.json').read_text())
metadata = json.loads((tracking / f'{prefix}-registry-metadata.log').read_text())
key = 'node_modules/proxy-addr'
old_node, node = old['packages'][key], current['packages'][key]
assert old_node['version'] == '2.0.7'
assert node['version'] == metadata['version'] == '2.0.8'
assert node['resolved'] == metadata['dist']['tarball'] == 'https://registry.npmjs.org/proxy-addr/-/proxy-addr-2.0.8.tgz'
assert node['integrity'] == metadata['dist']['integrity']
assert node['dependencies'] == old_node['dependencies'] == metadata['dependencies']
assert node['engines'] == old_node['engines'] == metadata['engines']
assert node['license'] == old_node['license'] == metadata['license']
if 'funding' in node:
    assert node['funding'] == metadata['funding']


def normalized_node(value):
    result = copy.deepcopy(value)
    for field in ['version', 'resolved', 'integrity', 'funding']:
        result.pop(field, None)
    return result


assert normalized_node(old_node) == normalized_node(node), 'Unexpected selected-node metadata change'
del old['packages'][key]
del current['packages'][key]
assert old == current, 'Unrelated lock node, dependency constraint or lock metadata changed'
lock_hash = hashlib.sha256((repo / 'bff/package-lock.json').read_bytes()).hexdigest()
print('Exact proxy-addr 2.0.7 -> 2.0.8; manifests, other lock nodes and runtime source unchanged')

if mode == 'receipts':
    hashes = {}
    for project in ['bff', 'root']:
        values = re.findall(r'^sha256-[A-Za-z0-9+/]{43}=$',
                            (tracking / f'{prefix}-prefetch-{project}.log').read_text(), re.MULTILINE)
        assert len(values) == 1, (project, values)
        hashes[project] = values[0]
    root_hash = re.search(r'npmDepsHash = "([^"]+)";', original('packages/frontend.nix')).group(1)
    old_bff_hash = re.search(r'npmDepsHash = "([^"]+)";', original('packages/bff.nix')).group(1)
    assert hashes['root'] == root_hash, 'Unchanged frontend lock produced a different hash'
    assert hashes['bff'] != old_bff_hash, 'Changed BFF lock did not produce a new dependency hash'
    for name, value in [('bff-npmDepsHash.txt', hashes['bff']),
                        ('root-npmDepsHash.txt', hashes['root']),
                        ('generated-lock.sha256', lock_hash)]:
        path = tracking / f'{prefix}-{name}'
        with path.open('x') as receipt:
            receipt.write(value + '\n')
    print(json.dumps(hashes, sort_keys=True))
elif mode == 'ready':
    assert lock_hash == (tracking / f'{prefix}-generated-lock.sha256').read_text().strip()
    new_hash = (tracking / f'{prefix}-bff-npmDepsHash.txt').read_text().strip()
    previous = original('packages/bff.nix')
    old_hash = re.search(r'npmDepsHash = "([^"]+)";', previous).group(1)
    assert (repo / 'packages/bff.nix').read_text() == previous.replace(old_hash, new_hash)
    assert (tracking / f'{prefix}-generate-wrapper.exit').read_text().strip() == '0'
    print('Owner-applied BFF hash matches canonical prefetch; generated lock bytes remain frozen')
