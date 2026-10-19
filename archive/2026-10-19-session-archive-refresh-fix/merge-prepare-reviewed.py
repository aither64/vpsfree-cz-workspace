from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import json
import subprocess
import time

tracking = Path(__file__).resolve().parent
workspace = tracking.parents[1]
expected = {
    "dev-workspace": "09a407953026514ae84be81dab9442fd74b6a362",
    "workspace": "7c1a4c765b5fca5197fd88433096ef533d64aa87",
}


def prepare(repository):
    source = workspace / "worktrees" / tracking.name / repository
    actual = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=source, text=True
    ).strip()
    if actual != expected[repository]:
        raise SystemExit(f"Unexpected {repository} source head: {actual}")
    command = [
        "dev-session", "coordination", "prepare", tracking.name, "--as-is",
        "--request", str(tracking / f"merge-{repository}-prepare-request.json"),
        "--json",
    ]
    started = time.monotonic()
    stdout = tracking / f"merge-{repository}-prepare.stdout"
    stderr = tracking / f"merge-{repository}-prepare.log"
    with stdout.open("w") as out, stderr.open("w") as err:
        process = subprocess.run(command, cwd=workspace, stdout=out, stderr=err)
    result = {
        "repository": repository, "head": actual, "exitStatus": process.returncode,
        "elapsed": time.monotonic() - started, "stdout": str(stdout),
        "stderr": str(stderr), "command": command,
    }
    (tracking / f"merge-{repository}-prepare-result.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result), flush=True)
    return process.returncode


with ThreadPoolExecutor(max_workers=2) as executor:
    statuses = list(executor.map(prepare, expected))
raise SystemExit(next((status for status in statuses if status), 0))
