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
old_revision = "93a16d6cecb6bc847ec9335a3f170eb8b301ab56"
revision = "68aa33b451a14eb7bf4b2f1a090a8e5a2f80b52e"
root_inputs = before["nodes"][before["root"]]["inputs"]
assert set(root_inputs) == {"nixpkgs", "dev-workspace", "kb-runtime", "devcluster-vpsadmin", "devcluster-vpsadminos", "devcluster-vpsadminWebui", "devcluster-vpsf-status"}
assert before["root"] == after["root"] and before["version"] == after["version"]
assert root_inputs == after["nodes"][after["root"]]["inputs"], "root edges changed"
key = resolve(before, ("kb-runtime",))
assert key == resolve(after, ("kb-runtime",)), "selected K node renamed"
old_node, new_node = before["nodes"][key], after["nodes"][key]
for field in ("locked", "original"):
    assert old_node[field]["type"] == new_node[field]["type"] == "github"
    assert old_node[field]["owner"] == new_node[field]["owner"] == "vpsfreecz"
    assert old_node[field]["repo"] == new_node[field]["repo"] == "vpsfree-kb-contracts"
    assert old_node[field]["rev"] == old_revision and new_node[field]["rev"] == revision
assert set(old_node["locked"]) == set(new_node["locked"])
assert isinstance(new_node["locked"]["lastModified"], int)
assert new_node["locked"]["narHash"].startswith("sha256-")
# Strict whole-lock equality except the requested source identity. The original
# revision necessarily follows the exact changed URL; only these three locked
# identity fields may differ. Inputs, follows and every other node stay exact.
expected = json.loads(json.dumps(before))
for field in ("rev", "narHash", "lastModified"):
    expected["nodes"][key]["locked"][field] = new_node["locked"][field]
expected["nodes"][key]["original"]["rev"] = revision
assert expected == after, "generator widened beyond selected K identity"
assert graph(after, ("kb-runtime",), owned_prefix=True) == graph(selected_k), "K own graph/follows differ"
assert graph(before, ("kb-runtime",)) == graph(after, ("kb-runtime",)), "K dependency graph changed"
assert graph(after, ("dev-workspace",), owned_prefix=True) == graph(selected_d), "D own graph differs"
d_node = after["nodes"][resolve(after, ("dev-workspace",))]
assert d_node["locked"] == {k: v for k, v in d_receipt["locked"].items() if k != "__final"}
assert d_node["locked"]["rev"] == d_receipt["revision"] == "51aba080b264c28f5584867b6cf006bf423ae2f3"
for name in sorted(set(root_inputs) - {"kb-runtime"}):
    assert graph(before, (name,)) == graph(after, (name,)), ("unrelated semantic graph changed", name)
print(json.dumps({"selected_k": new_node["locked"], "k_semantic_paths": len(graph(selected_k)), "d_semantic_paths": len(graph(selected_d)), "preserved_other_root_inputs": sorted(set(root_inputs) - {"kb-runtime"})}, indent=2))
