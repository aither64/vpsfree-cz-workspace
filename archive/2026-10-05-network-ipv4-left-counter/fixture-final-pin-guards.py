import copy
import json
import re
import subprocess
import sys
from pathlib import Path


def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args], text=True)


mode, repo, old, v_sha, w_sha = sys.argv[1:]
repo = Path(repo)
assert re.fullmatch(r'[0-9a-f]{40}', v_sha)
assert re.fullmatch(r'[0-9a-f]{40}', w_sha)

if mode == 'set-kb':
    previous = json.loads((repo / 'captures.json').read_text())['vpsadmin_commit']
    assert previous != v_sha
    patterns = {
        'flake.nix': r'(vpsadmin\.url = "github:vpsfreecz/vpsadmin/)' + previous + r'(";)',
        'captures.json': r'("vpsadmin_commit": ")' + previous + r'(")',
        'contract/navigation.yml': r'(vpsadmin_revision: )' + previous + r'(\n)',
        'contract/pages.yml': r'(  vpsadmin: )' + previous + r'(\n)',
    }
    prepared = {}
    for name, pattern in patterns.items():
        path = repo / name
        updated, count = re.subn(pattern, lambda m: m[1] + v_sha + m[2], path.read_text())
        assert count == 1, (name, count)
        prepared[path] = updated
    for path, updated in prepared.items():
        path.write_text(updated)
    sys.exit(0)

assert mode in ['config', 'kb']
original = json.loads(git(repo, 'show', f'{old}:flake.lock'))
current = json.loads((repo / 'flake.lock').read_text())
root = current['nodes'][current['root']]['inputs']
targets = {'vpsadminServices': v_sha, 'vpsadminWebui': w_sha} if mode == 'config' else {'vpsadmin': v_sha}
for name, revision in targets.items():
    node = current['nodes'][root[name]]
    assert node['locked']['rev'] == revision, (name, node['locked']['rev'])
if mode == 'config':
    assert current['nodes'][root['vpsadminWebui']]['inputs']['vpsadmin'] == ['vpsadminServices']


def normalize(lock):
    ret = copy.deepcopy(lock)
    inputs = ret['nodes'][ret['root']]['inputs']
    for name in targets:
        node = ret['nodes'][inputs[name]]
        for key in ['rev', 'narHash', 'lastModified']:
            node['locked'].pop(key, None)
        # K deliberately uses an exact source URL; C uses channel-owned locks.
        if mode == 'kb':
            node['original'].pop('rev', None)
    return ret


assert normalize(original) == normalize(current), 'Unrelated lock identity, node or follows changed'
if mode == 'kb':
    assert current['nodes'][root['vpsadmin']]['original']['rev'] == v_sha
    # Keep fingerprints, capture bindings and page prose byte-identical to the
    # previous inspected pin. Only the selected source revision may differ.
    for name in ['flake.nix', 'captures.json', 'contract/navigation.yml', 'contract/pages.yml']:
        previous = git(repo, 'show', f'{old}:{name}')
        old_v = original['nodes'][original['nodes'][original['root']]['inputs']['vpsadmin']]['locked']['rev']
        assert (repo / name).read_text() == previous.replace(old_v, v_sha), name
print(f'{mode}: exact selected pins, unrelated lock graph and follows preserved')
