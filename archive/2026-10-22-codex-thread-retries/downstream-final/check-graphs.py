#!/usr/bin/env python3
"""Capture and check the exact downstream pin-only graph transition."""

import hashlib
import json
import pathlib
import subprocess

ROOT = pathlib.Path('/home/aither/workspace/ai/vpsfree.cz')
OUT = pathlib.Path(__file__).resolve().parent
PREP = json.loads((OUT / 'preparation.json').read_text())
RUNTIME = 'c79af9736c04f6e7cd9c6b2197913d101896544c'
CLIENT = '5743f94c2fbd01b65438847d2e2bab0f01df32ae'
EXTENSION = '767dfd587e346168e1443e65ccdb67ce748f3fe3'


def git(path, *args):
    return subprocess.check_output(['git', '-C', str(path), *args], text=True).strip()


def node_at(lock, path):
    key = lock['root']
    for name in path:
        key = lock['nodes'][key]['inputs'][name]
        assert isinstance(key, str), (path, 'unexpected follows')
    return key


def semantic_graph(lock):
    """Node map plus every ordinary or follows edge, without renaming nodes."""
    return {
        'root': lock['root'],
        'nodes': lock['nodes'],
        'edges': [
            {'from': key, 'input': name, 'reference': value}
            for key, node in sorted(lock['nodes'].items())
            for name, value in sorted(node.get('inputs', {}).items())
        ],
    }


receipt = {'runtime': RUNTIME, 'client': CLIENT, 'repositories': {}}
for name, before in PREP['repositories'].items():
    path = pathlib.Path(before['path'])
    current = json.loads((path / 'flake.lock').read_text())
    runtime_path = ['vpsfree-dev-workspace', 'dev-workspace'] if name == 'workspace' else ['devWorkspace']
    runtime_key = node_at(current, runtime_path)
    client_key = node_at(current, runtime_path + ['codex-web'])
    assert current['nodes'][runtime_key]['locked']['rev'] == RUNTIME
    assert current['nodes'][client_key]['locked']['rev'] == CLIENT
    if name == 'workspace':
        extension_key = node_at(current, ['vpsfree-dev-workspace'])
        assert current['nodes'][extension_key]['locked']['rev'] == EXTENSION
        assert f'inputs.dev-workspace.url = "github:aither64/dev-workspace/{RUNTIME}";' in (path / 'flake.nix').read_text()
    baseline = before['target_lock']
    assert current['root'] == baseline['root']
    assert set(current['nodes']) == set(baseline['nodes'])
    assert semantic_graph(current)['edges'] == semantic_graph(baseline)['edges']
    changed = [key for key in current['nodes'] if current['nodes'][key] != baseline['nodes'][key]]
    assert set(changed) == {runtime_key, client_key}, changed
    transitions = {}
    for key in changed:
        previous, final = baseline['nodes'][key], current['nodes'][key]
        assert set(previous) == set(final)
        assert {k: v for k, v in previous.items() if k not in ('locked', 'original')} == {
            k: v for k, v in final.items() if k not in ('locked', 'original')
        }
        assert {k: v for k, v in previous['original'].items() if k != 'rev'} == {
            k: v for k, v in final['original'].items() if k != 'rev'
        }
        assert {k: v for k, v in previous['locked'].items() if k not in ('rev', 'narHash', 'lastModified')} == {
            k: v for k, v in final['locked'].items() if k not in ('rev', 'narHash', 'lastModified')
        }
        transitions[key] = {'before': previous, 'after': final}
    gem_unchanged = None
    if (path / 'Gemfile.lock').exists():
        gem_unchanged = git(path, 'show', before['fresh_target'] + ':Gemfile.lock') == (path / 'Gemfile.lock').read_text().strip()
        assert gem_unchanged
    graph = semantic_graph(current)
    encoded = json.dumps(graph, sort_keys=True, separators=(',', ':')).encode()
    (OUT / f'{name}.final.graph.json').write_text(json.dumps(graph, indent=2) + '\n')
    (OUT / f'{name}.final.flake.lock').write_bytes((path / 'flake.lock').read_bytes())
    receipt['repositories'][name] = {
        'fresh_base': before['fresh_target'],
        'runtime_path': runtime_path,
        'runtime_node': runtime_key,
        'client_node': client_key,
        'runtime_locked': current['nodes'][runtime_key]['locked'],
        'client_locked': current['nodes'][client_key]['locked'],
        'node_count': len(current['nodes']),
        'edge_count': len(graph['edges']),
        'semantic_graph_sha256': hashlib.sha256(encoded).hexdigest(),
        'changed_nodes_relative_fresh_default': transitions,
        'all_other_nodes_identical': True,
        'all_edges_and_follows_identical': True,
        'gemfile_lock_equal_fresh_default': gem_unchanged,
        'deployed_head': before['deployed_head'],
        'deployed_base': before['old_base'],
        'baseline_changes_separately_recorded': f'{name}.baseline.diff',
    }
(OUT / 'graph-proof.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps({name: {key: value[key] for key in ('fresh_base', 'runtime_node', 'client_node', 'node_count', 'edge_count', 'all_other_nodes_identical', 'all_edges_and_follows_identical')} for name, value in receipt['repositories'].items()}, indent=2))
