import json, os, subprocess, time
from pathlib import Path
root = Path(__file__).resolve().parent
started = time.monotonic()
heads = {
    "haveapi": "68cc80b012b7a6b9bcdf35c008c338cbc3f4c000",
    "vpsadmin-rust-client": "945af6a97717a7a6373507bbc9592d5cd53727c2",
}
worktrees = Path("/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-18-rust-client-generator")
def source_state():
    for repo, head in heads.items():
        actual = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=worktrees/repo, text=True).strip()
        dirty = subprocess.check_output(["git", "status", "--porcelain"], cwd=worktrees/repo, text=True)
        if actual != head or dirty:
            raise SystemExit("Source head or cleanliness guard failed: " + repo)
source_state()
op = json.loads((root/"operations.json").read_text())[0]
local_started = time.monotonic()
with (root/"package.log").open("w") as output:
    local = subprocess.run(op["argv"], cwd=op["cwd"], stdout=output, stderr=subprocess.STDOUT)
local_result = {"operation": op["name"], "exit_status": local.returncode, "elapsed_seconds": round(time.monotonic()-local_started, 3), "heads": heads, "cwd": op["cwd"]}
(root/"package-result.json").write_text(json.dumps(local_result, indent=2)+"\n")
print("Local package operation exit:", local.returncode, flush=True)
source_state()
while not (root/"ci-runs.json").exists():
    time.sleep(10)
runs = json.loads((root/"ci-runs.json").read_text())
remaining = {(r["repo"], r["id"]): r for r in runs}
completed = []
while remaining:
    for key, item in list(remaining.items()):
        args = ["gh", "run", "view", str(item["id"]), "--repo", item["repo"], "--json", "databaseId,headSha,headBranch,event,status,conclusion,workflowName,url,jobs"]
        query = subprocess.run(args, text=True, capture_output=True)
        if query.returncode:
            (root/"ci-read-error.txt").write_text(query.stderr)
            raise SystemExit("CI status read failed; active IDs retained in ci-runs.json")
        data = json.loads(query.stdout)
        if data["headSha"] != item["head"] or data["headBranch"] != "2026-10-18-rust-client-generator" or data["event"] != "push":
            raise SystemExit("CI identity guard failed")
        (root/f"run-{item['id']}.json").write_text(json.dumps(data, indent=2)+"\n")
        if data["status"] == "completed":
            completed.append({"repo": item["repo"], **data})
            del remaining[key]
            print("CI completed:", item["repo"], item["id"], data["conclusion"], flush=True)
            if data["conclusion"] != "success":
                with (root/f"failed-{item['id']}.log").open("w") as log:
                    subprocess.run(["gh", "run", "view", str(item["id"]), "--repo", item["repo"], "--log-failed"], stdout=log, stderr=subprocess.STDOUT)
    if remaining:
        time.sleep(30)
source_state()
result = {"result": "passed" if local.returncode == 0 and all(r["conclusion"] == "success" for r in completed) else "failed", "elapsed_seconds": round(time.monotonic()-started, 3), "local": local_result, "runs": completed, "active_operations": []}
(root/"result.json").write_text(json.dumps(result, indent=2)+"\n")
(root/"watcher-result.txt").write_text(f"Result: {result['result']}. Local exit {local.returncode}; {len(completed)} exact-head CI runs completed. Elapsed {result['elapsed_seconds']}s. No active operation. See result.json and package.log.\n")
print("Batch result:", result["result"], flush=True)
raise SystemExit(0 if result["result"] == "passed" else 1)
