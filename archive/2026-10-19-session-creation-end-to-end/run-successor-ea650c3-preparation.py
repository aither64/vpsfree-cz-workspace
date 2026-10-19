"""Lead-owned exact preparation, with independent terminal observation receipts."""
import json
import pathlib
import subprocess
import sys
import time

here = pathlib.Path(__file__).resolve().parent
workspace = here.parents[1]
kind = sys.argv[1]
assert kind in ("system", "profile")
configuration = workspace / "worktrees" / here.name / "vpsfree-cz-configuration"
prefix = here / f"successor-ea650c3-{kind}-prepare"
command = [
    "/home/aither/.local/state/dev-workspaces/profile/bin/dev-session",
    "coordination", "prepare", here.name, "--as-is", "--request",
    str(prefix.with_name(prefix.name + "-request.json")), "--json",
]
cwd = workspace
if kind == "system":
    cwd = configuration
    command = ["nix", "develop", "--command", "env",
               f"BUNDLE_GEMFILE={configuration / 'Gemfile'}",
               f"BUNDLE_PATH={configuration / '.gems'}", *command]
start = time.monotonic()
with prefix.with_suffix(".json").open("w") as output, prefix.with_suffix(".log").open("w") as errors:
    process = subprocess.run(command, cwd=cwd, stdout=output, stderr=errors)
result = {"kind": kind, "exitStatus": process.returncode,
          "elapsedSeconds": time.monotonic() - start, "command": command}
prefix.with_name(prefix.name + "-result.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result), flush=True)
sys.exit(process.returncode)
