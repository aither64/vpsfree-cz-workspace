import json, os, subprocess, time
from pathlib import Path
root = Path(__file__).resolve().parent
source = root.parents[1] / "worktrees" / root.name / "dev-workspace"
commands = [
 ("browser", ["nix", "develop", "--command", "env", "TMPDIR=/tmp", "PORTAL_BROWSER_TEST=1", "NODE_PATH=/nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1/lib/node_modules", "PLAYWRIGHT_BROWSERS_PATH=/nix/store/f0rap655j6wmqbfvqdw445kwcxkxwf7n-playwright-browsers", "go", "-C", "portal", "test", "-mod=readonly", "./internal/web", "-run", "^TestIndexRefreshPreservesSelection$", "-v", "-count=1"]),
 ("packaged", ["nix", "build", "--no-link", "--print-out-paths", "--print-build-logs", ".#checks.x86_64-linux.package", ".#checks.x86_64-linux.session-archive-lifecycle"]),
]
results = []
for name, command in commands:
 started = time.monotonic()
 with (root / (name + ".log")).open("w") as output:
  process = subprocess.run(command, cwd=source, stdout=output, stderr=subprocess.STDOUT)
 result = {"name": name, "command": command, "exitStatus": process.returncode, "elapsed": time.monotonic() - started, "revision": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=source, text=True).strip()}
 results.append(result)
 (root / "verification-results.json").write_text(json.dumps(results, indent=2) + "\n")
 print(json.dumps(result), flush=True)
 if process.returncode:
  raise SystemExit(process.returncode)
