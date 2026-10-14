#!/usr/bin/env python3
"""Inspect only this targeted E lock update against exact owning source locks."""
import json
import sys
from pathlib import Path


def load(path):
    value = json.loads(Path(path).read_text())
    assert value["version"] == 7
    assert value["root"] in value["nodes"]
    return value


def resolve(lock, path):
    node = lock["root"]
    remaining = tuple(path)
    seen = set()
    while remaining:
        position = (node, remaining)
        assert position not in seen, ("cyclic follows", path)
        seen.add(position)
        reference = lock["nodes"][node]["inputs"][remaining[0]]
        tail = remaining[1:]
        if isinstance(reference, str):
            node, remaining = reference, tail
        else:
            assert isinstance(reference, list) and all(isinstance(x, str) for x in reference)
            # Preserve the unresolved suffix after a follows encountered mid-path.
            node, remaining = lock["root"], tuple(reference) + tail
    return node


def graph(lock, prefix=(), owned_prefix=False):
    result = {}

    def visit(relative, ancestors):
        key = resolve(lock, prefix + relative)
        assert key not in ancestors, ("cyclic input graph", prefix + relative)
        node = lock["nodes"][key]
        entry = {name: node[name] for name in ("locked", "original", "flake") if name in node}
        if not relative:
            # The selected input has its own identity; its source-lock root does not.
            entry = {}
        edges = {}
        for name, reference in node.get("inputs", {}).items():
            if isinstance(reference, list):
                if owned_prefix:
                    assert reference[:len(prefix)] == list(prefix), ("external override/follows", prefix, reference)
                    reference = reference[len(prefix):]
                edges[name] = {"follows": reference}
            else:
                assert isinstance(reference, str)
                edges[name] = {"direct": True}
        entry["inputs"] = edges
        result["/".join(relative)] = entry
        for name in sorted(edges):
            visit(relative + (name,), ancestors | {key})

    visit((), set())
    return result


before, after, selected_d, selected_k = map(load, sys.argv[1:5])
d_receipt = json.loads(Path(sys.argv[5]).read_text())
old_root = before["nodes"][before["root"]]["inputs"]
new_root = after["nodes"][after["root"]]["inputs"]
assert set(new_root) == set(old_root) | {"kb-runtime"}
assert "kb-runtime" not in old_root
unrelated = sorted(set(old_root) - {"dev-workspace"})
for name in unrelated:
    old_node = before["nodes"][resolve(before, (name,))]
    new_node = after["nodes"][resolve(after, (name,))]
    assert {k: old_node[k] for k in ("locked", "original", "flake") if k in old_node} == {
        k: new_node[k] for k in ("locked", "original", "flake") if k in new_node
    }, ("changed unrelated root input", name)
    assert graph(before, (name,)) == graph(after, (name,)), ("changed unrelated graph", name)

selected = {
    "dev-workspace": ("aither64", "dev-workspace", "51aba080b264c28f5584867b6cf006bf423ae2f3", selected_d),
    "kb-runtime": ("vpsfreecz", "vpsfree-kb-contracts", "93a16d6cecb6bc847ec9335a3f170eb8b301ab56", selected_k),
}
summary = {}
for name, (owner, repo, revision, source_lock) in selected.items():
    node = after["nodes"][resolve(after, (name,))]
    for field in ("locked", "original"):
        assert node[field]["type"] == "github"
        assert node[field]["owner"] == owner and node[field]["repo"] == repo
        assert node[field]["rev"] == revision, ("wrong selected revision", name, field)
    if name == "dev-workspace":
        assert node["locked"] == {key: value for key, value in d_receipt["locked"].items() if key != "__final"}
    assert graph(after, (name,), owned_prefix=True) == graph(source_lock), ("selected source graph differs", name)
    summary[name] = {"revision": revision, "narHash": node["locked"]["narHash"],
                     "semantic_paths": len(graph(source_lock))}
print(json.dumps({"selected": summary, "preserved_root_inputs": unrelated}, indent=2))
