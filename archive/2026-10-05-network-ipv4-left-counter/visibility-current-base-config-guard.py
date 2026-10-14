import copy
import json
import pathlib
import subprocess
import sys

repo, old, base, head = pathlib.Path(sys.argv[1]), *sys.argv[2:]
def read(rev):
    return json.loads(subprocess.check_output(['git', '-C', str(repo), 'show', f'{rev}:flake.lock']))
previous, upstream = read(old), read(base)
current = json.loads((repo / 'flake.lock').read_text())
inputs = current['nodes'][current['root']]['inputs']
assert current['nodes'][inputs['vpsadminServices']]['locked']['rev'] == head
assert current['nodes'][inputs['vpsadminWebui']]['locked']['rev'] == 'e4c49bcdc91b33b7f644a2f125231cb413cf4bf4'

def normalize(lock):
    result = copy.deepcopy(lock)
    root = result['nodes'][result['root']]['inputs']
    for name in ['vpsadminServices', 'vpsadminWebui']:
        for key in ['rev', 'narHash', 'lastModified']:
            result['nodes'][root[name]]['locked'].pop(key, None)
    return result

assert normalize(upstream) == normalize(current), 'Unrelated current-default identity/node/follows changed'
previous_inputs = previous['nodes'][previous['root']]['inputs']
assert previous_inputs['vpsadminWebui'] == inputs['vpsadminWebui']
assert previous['nodes'][previous_inputs['vpsadminWebui']] == current['nodes'][inputs['vpsadminWebui']], 'Agreed W locked metadata/follows changed'
print('Current upstream graph preserved except two selected pins; W identity and follows equal prior feature pin')
