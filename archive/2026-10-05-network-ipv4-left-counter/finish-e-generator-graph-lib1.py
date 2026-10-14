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


