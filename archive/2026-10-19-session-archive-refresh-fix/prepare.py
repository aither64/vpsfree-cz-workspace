import concurrent.futures, json, subprocess, time
from pathlib import Path
root = Path(__file__).resolve().parent
workspace = root.parents[1]
configuration = workspace / "worktrees" / root.name / "vpsfree-cz-configuration"
def run(kind):
 command = ["dev-session", "coordination", "prepare", root.name, "--as-is", "--request", str(root / (kind + "-prepare-request.json")), "--json"]
 cwd = workspace
 if kind == "machine_activate":
  command = ["nix", "develop", "--command"] + command
  cwd = configuration
 started = time.monotonic()
 with (root / (kind + "-prepare.stdout")).open("w") as out, (root / (kind + "-prepare.log")).open("w") as err:
  process = subprocess.run(command, cwd=cwd, stdout=out, stderr=err)
 result = {"kind": kind, "exitStatus": process.returncode, "elapsed": time.monotonic() - started}
 (root / (kind + "-prepare-result.json")).write_text(json.dumps(result) + "\n")
 print(json.dumps(result), flush=True)
 return result
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
 results = list(pool.map(run, ["machine_activate", "profile_activate"]))
(root / "preparation-results.json").write_text(json.dumps(results, indent=2) + "\n")
raise SystemExit(0 if all(x["exitStatus"] == 0 for x in results) else 1)
