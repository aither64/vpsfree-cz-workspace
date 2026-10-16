"""Prove exact tested-host reuse without normalizing any host field."""
import hashlib
import json
from pathlib import Path

directory = Path(__file__).resolve().parent
record = directory.parent
assert (directory / "eval.status").read_text().strip() == "0"
old_path = record.parent / "runtime-effective.yf2uje2x/original-config.json"
quick_path = record / "quick/inputs.json"
current_path = directory / "config.json"
old = json.loads(old_path.read_text())
quick = json.loads(quick_path.read_text())
current = json.loads(current_path.read_text())
assert quick["persistenceCheck"] == "/nix/store/6218pz068gff57gp72fjhw2b0ylh5msd-nixos-container-persistence.drv"
assert set(old) == set(current) == set(quick["config"])
host = lambda value: {k: v for k, v in value.items() if k != "testScripts"}
assert host(old) == host(current), "Complete host/runner configuration differs"
assert len(current["testScripts"]) == 12
assert current["testScripts"] == quick["config"]["testScripts"], "Host overlay changed a script"
receipt = {
    "schema": 1,
    "source_head": "d3bf74bc92ea0ced100df12ba10e1dadd7fd1ec5",
    "host_source_head": "edb90d2fe2190d88d8b9d2d21bd0def79eedc898",
    "complete_non_script_equality": True,
    "all_twelve_current_scripts_unchanged_by_overlay": True,
    "normal_check_derivation": quick["persistenceCheck"],
    "inputs": {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in (old_path, quick_path, current_path, directory / "config.nix", directory / "evaluate.nix")},
}
(directory / "comparison.json").write_text(json.dumps(receipt, indent=2) + "\n")
print(json.dumps(receipt, indent=2))
