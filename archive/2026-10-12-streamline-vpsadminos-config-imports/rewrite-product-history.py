#!/usr/bin/env python3
"""Hook-enabled rebase helper for the exact owned, unmerged product series."""
import json
import subprocess
import sys
from pathlib import Path

record = Path(__file__).resolve().parent
spec = json.loads((record / "history-rewrite-inputs.json").read_text())
messages = json.loads((record / "finished-commit-message-paths.json").read_text())

def git(*args):
    return subprocess.check_output(["git", *args], text=True).strip()

def proof(phase, expected_tree):
    observed = {"phase": phase, "head": git("rev-parse", "HEAD"),
                "tree": git("rev-parse", "HEAD^{tree}")}
    if observed["tree"] != expected_tree:
        raise RuntimeError(f"Tree changed during {phase}: {observed}")
    with (record / "history-rewrite-proofs.jsonl").open("a") as handle:
        handle.write(json.dumps(observed) + "\n")
    print(json.dumps(observed))

mode = sys.argv[1]
if mode == "sequence":
    todo = Path(sys.argv[2])
    commits = [line.split()[1] for line in todo.read_text().splitlines()
               if line.startswith("pick ")]
    expected = [spec[k] for k in ("selector", "oldFix", "policy", "technical")]
    if len(commits) != len(expected) or not all(b.startswith(a) for a,b in zip(commits,expected)):
        raise RuntimeError(f"Unexpected owned range: {commits}")
    helper = f"python3 {record}/rewrite-product-history.py"
    todo.write_text(
        f"pick {spec['selector']}\nexec {helper} selector\n"
        f"pick {spec['oldFix']}\nexec {helper} old-fix\n"
        f"fixup {spec['technical']}\nexec {helper} final-fix\n"
        f"pick {spec['policy']}\nexec {helper} final-tree\n"
    )
elif mode in ("selector", "old-fix", "final-fix"):
    key = {"selector":"selector", "old-fix":"persistence-old-matter", "final-fix":"persistence"}[mode]
    subprocess.run(["git", "commit", "--amend", "-F", messages[key]], check=True)
    if mode == "selector":
        proof(mode, spec["selectorTree"])
    elif mode == "old-fix":
        proof(mode, spec["oldFixTree"])
elif mode == "final-tree":
    proof(mode, spec["technicalTree"])
else:
    raise ValueError(mode)
