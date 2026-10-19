from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import json
import subprocess
import time

tracking = Path(__file__).resolve().parent
workspace = tracking.parents[1]
sources = workspace / "worktrees" / tracking.name
runtime = sources / "dev-workspace"
configuration = sources / "vpsfree-cz-configuration"
expected = {
    "dev-workspace": "09a407953026514ae84be81dab9442fd74b6a362",
    "vpsfree-cz-configuration": "6fe8d230f571d5883f8e00e002decc15bf9b6cd8",
    "workspace": "7c1a4c765b5fca5197fd88433096ef533d64aa87",
}
for repository, revision in expected.items():
    actual = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=sources / repository, text=True
    ).strip()
    if actual != revision:
        raise SystemExit(f"Unexpected {repository} head: {actual}")


def run(name, command, cwd):
    started = time.monotonic()
    stdout = tracking / f"baseline-refresh-{name}.stdout"
    stderr = tracking / f"baseline-refresh-{name}.log"
    with stdout.open("w") as out, stderr.open("w") as err:
        process = subprocess.run(command, cwd=cwd, stdout=out, stderr=err)
    result = {
        "name": name,
        "command": command,
        "exitStatus": process.returncode,
        "elapsed": time.monotonic() - started,
        "stdout": str(stdout),
        "stderr": str(stderr),
        "revisions": expected,
    }
    (tracking / f"baseline-refresh-{name}-result.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result), flush=True)
    return process.returncode


browser = [
    "nix", "develop", "--command", "env", "TMPDIR=/tmp",
    "PORTAL_BROWSER_TEST=1",
    "NODE_PATH=/nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1/lib/node_modules",
    "PLAYWRIGHT_BROWSERS_PATH=/nix/store/f0rap655j6wmqbfvqdw445kwcxkxwf7n-playwright-browsers",
    "go", "-C", "portal", "test", "-mod=readonly", "./internal/web",
    "-run", "^TestIndexRefreshPreservesSelection$", "-v", "-count=1",
]
browser_status = run("browser", browser, runtime)
if browser_status:
    raise SystemExit(browser_status)

gh = ["nix", "shell", "nixpkgs#gh", "-c", "gh"]
ci_status = run("ci-watch", gh + [
    "run", "watch", "39295653767", "--repo", "aither64/dev-workspace",
    "--exit-status", "--interval", "30",
], workspace)
run("ci-metadata", gh + [
    "run", "view", "39295653767", "--repo", "aither64/dev-workspace",
    "--json", "databaseId,headSha,status,conclusion,jobs",
], workspace)
run("ci-logs", gh + [
    "run", "view", "39295653767", "--repo", "aither64/dev-workspace", "--log",
], workspace)
if ci_status:
    raise SystemExit(ci_status)

for check in ("package", "session-archive-lifecycle"):
    status = run(f"{check}-derivation", [
        "nix", "eval", "--raw", f".#checks.x86_64-linux.{check}.drvPath",
    ], runtime)
    if status:
        raise SystemExit(status)

preparations = [
    ("machine-prepare", [
        "nix", "develop", "--command", "dev-session", "coordination", "prepare",
        tracking.name, "--as-is", "--request",
        str(tracking / "baseline-refresh-machine-prepare-request.json"), "--json",
    ], configuration),
    ("profile-prepare", [
        "dev-session", "coordination", "prepare", tracking.name, "--as-is",
        "--request", str(tracking / "baseline-refresh-profile-prepare-request.json"),
        "--json",
    ], workspace),
]
with ThreadPoolExecutor(max_workers=2) as executor:
    futures = [executor.submit(run, *preparation) for preparation in preparations]
    statuses = [future.result() for future in futures]
raise SystemExit(next((status for status in statuses if status), 0))
