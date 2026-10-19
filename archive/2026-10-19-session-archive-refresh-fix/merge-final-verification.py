from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import json
import subprocess
import time

tracking = Path(__file__).resolve().parent
workspace = tracking.parents[1]


def run(name, command, cwd=workspace):
    started = time.monotonic()
    with (tracking / f"{name}.stdout").open("w") as out:
        with (tracking / f"{name}.log").open("w") as err:
            result = subprocess.run(command, cwd=cwd, stdout=out, stderr=err)
    receipt = {
        "exitStatus": result.returncode,
        "elapsed": time.monotonic() - started,
        "command": command,
    }
    (tracking / f"{name}-result.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({"operation": name, **receipt}), flush=True)
    return result.returncode


def prepare():
    source = workspace / "worktrees" / tracking.name / "workspace"
    head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=source, text=True).strip()
    if head != "c32995867329663badcc40a56473c36f9c338f94":
        raise RuntimeError(f"Unexpected workspace head: {head}")
    return run("merge-workspace-refresh-prepare", [
        "dev-session", "coordination", "prepare", tracking.name, "--as-is",
        "--request", str(tracking / "merge-workspace-refresh-prepare-request.json"), "--json",
    ])


def ci():
    code = run("merge-runtime-ci-watch", [
        "gh", "run", "watch", "39306064979", "--repo", "aither64/dev-workspace",
        "--interval", "30", "--exit-status",
    ])
    run("merge-runtime-ci-metadata", [
        "gh", "run", "view", "39306064979", "--repo", "aither64/dev-workspace",
        "--json", "databaseId,headSha,headBranch,event,status,conclusion,url,jobs",
    ])
    if code:
        run("merge-runtime-ci-failure", [
            "gh", "run", "view", "39306064979", "--repo", "aither64/dev-workspace", "--log-failed",
        ])
    return code


with ThreadPoolExecutor(max_workers=2) as executor:
    results = [executor.submit(prepare), executor.submit(ci)]
    codes = [future.result() for future in results]
raise SystemExit(next((code for code in codes if code), 0))
