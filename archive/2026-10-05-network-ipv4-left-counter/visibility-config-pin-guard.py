import copy
import json
import pathlib
import re
import subprocess
import sys

repo, old, head = pathlib.Path(sys.argv[1]), sys.argv[2], sys.argv[3]
assert re.fullmatch(r'[0-9a-f]{40}', head)
previous = json.loads(subprocess.check_output(['git', '-C', str(repo), 'show', f'{old}:flake.lock']))
current = json.loads((repo / 'flake.lock').read_text())
inputs = current['nodes'][current['root']]['inputs']
assert current['nodes'][inputs['vpsadminServices']]['locked']['rev'] == head
assert current['nodes'][inputs['vpsadminWebui']]['locked']['rev'] == 'e4c49bcdc91b33b7f644a2f125231cb413cf4bf4'


def normalize(lock):
    normalized = copy.deepcopy(lock)
    root = normalized['nodes'][normalized['root']]['inputs']
    node = normalized['nodes'][root['vpsadminServices']]
    for key in ['rev', 'narHash', 'lastModified']:
        node['locked'].pop(key, None)
    return normalized


assert normalize(previous) == normalize(current), 'W or unrelated lock identities/nodes/follows changed'
print('Only backend locked revision/content/time changed; complete W and unrelated lock graph preserved')
