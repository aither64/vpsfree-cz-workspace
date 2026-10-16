"""Run only the corrected declared fixture after the exact-input gate."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile
import time

record = Path(__file__).resolve().parent
tracking = record.parent
source = tracking.parents[1] / "worktrees" / tracking.name / "vpsadminos"
head = "d3bf74bc92ea0ced100df12ba10e1dadd7fd1ec5"
tree = "07e8de789e26dee44f48d8682d11d09f7adfd5be"
proof_dir = record / "host-inputs-original-source"
proof = json.loads((proof_dir / "comparison.json").read_text())
assert proof["source_head"] == head and proof["complete_non_script_equality"]
assert proof["all_twelve_current_scripts_unchanged_by_overlay"]
for path, digest in proof["inputs"].items():
    assert hashlib.sha256(Path(path).read_bytes()).hexdigest() == digest, path
assert (record / "runtime-clearance").read_text().strip() == head
assert subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=source, text=True).strip() == head
assert subprocess.check_output(["git", "rev-parse", "HEAD^{tree}"], cwd=source, text=True).strip() == tree
assert not subprocess.check_output(["git", "status", "--porcelain"], cwd=source, text=True).strip()
attempt = Path(tempfile.mkdtemp(prefix="runtime-declared.", dir=tracking))
state = tempfile.mkdtemp(prefix="ni.", dir="/tmp")
owner = {
    "session": tracking.name, "workspace": str(tracking.parents[1]),
    "uid": os.getuid(), "source": str(source), "head": head, "tree": tree,
    "host_source_head": proof["host_source_head"], "state_dir": state,
    "patterns": ["dist-config/nixos-persistence-upgrade#declared-backing-26.05"],
}
(attempt / "ownership.json").write_text(json.dumps(owner, indent=2) + "\n")
(record / "runtime-attempt").write_text(str(attempt) + "\n")
argv = ["./test-runner.sh", "test", "--state-dir", state, "--test-config",
        str(tracking / "image-test-config.nix"), "--no-destructive", "--jobs", "1", *owner["patterns"]]
env = os.environ.copy()
env["VPSADMINOS_CONFIG"] = str(proof_dir / "config.nix")
(attempt / "host-config.nix").write_bytes((proof_dir / "config.nix").read_bytes())
(attempt / "input-proof.json").write_text(json.dumps(proof, indent=2) + "\n")
(attempt / "invocation.json").write_text(json.dumps({"cwd": str(source), "argv": argv,
    "VPSADMINOS_CONFIG": env["VPSADMINOS_CONFIG"]}, indent=2) + "\n")
(attempt / "runner-inputs.json").write_bytes((record / "runner-inputs.json").read_bytes())
print(json.dumps({"attempt": str(attempt), "state": state, "head": head}), flush=True)
status = 130
started = time.monotonic()
try:
    with (attempt / "runtime.log").open("w") as output:
        status = subprocess.call(argv, cwd=source, env=env, stdout=output, stderr=subprocess.STDOUT)
finally:
    (attempt / "runtime.status").write_text(str(status) + "\n")
    (attempt / "elapsed-seconds").write_text(str(round(time.monotonic() - started)) + "\n")
print(json.dumps({"status": status, "attempt": str(attempt)}), flush=True)
raise SystemExit(status)
