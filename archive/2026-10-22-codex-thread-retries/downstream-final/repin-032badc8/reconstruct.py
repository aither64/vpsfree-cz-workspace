#!/usr/bin/env python3
"""Read-only reconstruction of the reviewed W/C trees plus the exact repin."""

import copy
import hashlib
import json
from pathlib import Path
import subprocess

OUT = Path(__file__).resolve().parent
PREP = json.loads((OUT / 'preparation.json').read_text())


def raw_git(path, *args, data=None):
    return subprocess.check_output(['git', '-C', str(path), *args], input=data)


def git(path, *args):
    return raw_git(path, *args).decode().strip()


result = {'schema': 1, 'runtime': PREP['new_runtime'], 'repositories': {}}
for name, old in PREP['repositories'].items():
    path = Path(old['worktree'])
    final = git(path, 'rev-parse', 'HEAD')
    assert not git(path, 'status', '--porcelain'), name
    assert git(path, 'rev-parse', 'HEAD^') == old['base'], name
    assert git(path, 'rev-list', old['base'] + '..HEAD').splitlines() == [final]
    lock = copy.deepcopy(old['old_lock'])
    assert lock == json.loads(raw_git(path, 'show', old['old_head'] + ':flake.lock'))
    assert old['old_flake_nix'].encode() == raw_git(path, 'show', old['old_head'] + ':flake.nix')
    key = lock['root']
    route = ['vpsfree-dev-workspace', 'dev-workspace'] if name == 'workspace' else ['devWorkspace']
    for edge in route:
        key = lock['nodes'][key]['inputs'][edge]
        assert isinstance(key, str)
    node = lock['nodes'][key]
    assert node['locked']['rev'] == PREP['old_runtime']
    node['locked'].update({
        'rev': PREP['new_runtime'],
        'narHash': PREP['new_runtime_nar'],
        'lastModified': PREP['new_runtime_last_modified'],
    })
    if name == 'workspace':
        assert node['original']['rev'] == PREP['old_runtime']
        node['original']['rev'] = PREP['new_runtime']
    else:
        assert 'rev' not in node['original']
    expected = {'flake.lock': (json.dumps(lock, indent=2) + '\n').encode()}
    if name == 'workspace':
        before_url = 'github:aither64/dev-workspace/' + PREP['old_runtime']
        assert old['old_flake_nix'].count(before_url) == 1
        expected['flake.nix'] = old['old_flake_nix'].replace(
            before_url, 'github:aither64/dev-workspace/' + PREP['new_runtime']
        ).encode()
    expected_blobs = {}
    for file, content in expected.items():
        assert content == (path / file).read_bytes(), (name, file, 'working bytes')
        assert content == raw_git(path, 'show', final + ':' + file), (name, file, 'committed bytes')
        expected_blobs[file] = raw_git(path, 'hash-object', '--stdin', data=content).decode().strip()
    # Reconstruct the entire raw root tree from the reviewed tree. Only the
    # expected top-level file blob IDs may be replaced; modes/names/other trees
    # are copied byte for byte. hash-object without -w writes no Git objects.
    original_tree = raw_git(path, 'cat-file', 'tree', old['old_tree'])
    reconstructed = bytearray()
    offset = 0
    replaced = set()
    while offset < len(original_tree):
        end = original_tree.index(b'\0', offset)
        header = original_tree[offset:end]
        file = header.split(b' ', 1)[1].decode()
        oid = original_tree[end + 1:end + 21]
        if file in expected_blobs:
            oid = bytes.fromhex(expected_blobs[file])
            replaced.add(file)
        reconstructed.extend(header + b'\0' + oid)
        offset = end + 21
    assert replaced == set(expected_blobs)
    tree = raw_git(path, 'hash-object', '-t', 'tree', '--stdin', data=bytes(reconstructed)).decode().strip()
    assert tree == git(path, 'rev-parse', 'HEAD^{tree}'), name
    actual_changed = git(path, 'diff', '--name-only', old['old_head'], final).splitlines()
    assert sorted(actual_changed) == sorted(expected), (name, actual_changed)
    result['repositories'][name] = {
        'base': old['base'], 'reviewed_head': old['old_head'],
        'reviewed_tree': old['old_tree'], 'final_head': final,
        'reconstructed_final_tree': tree, 'matches_committed_tree': True,
        'expected_blobs': expected_blobs,
        'expected_content_sha256': {k: hashlib.sha256(v).hexdigest() for k, v in expected.items()},
        'only_runtime_pin_fields_changed': True,
        'all_other_nodes_edges_follows_and_source_entries_identical': True,
        'node_count': len(lock['nodes']),
        'edge_count': sum(len(n.get('inputs', {})) for n in lock['nodes'].values()),
        'complete_series': [final], 'migrations': [],
    }
print(json.dumps(result, indent=2))
