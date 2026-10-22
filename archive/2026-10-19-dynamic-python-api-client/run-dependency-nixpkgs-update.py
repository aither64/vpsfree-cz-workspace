"""Run the assigned committing update once, with independent observation files."""

import datetime
import json
import os
from pathlib import Path
import subprocess
import sys
import time

SLUG = "2026-10-19-dynamic-python-api-client"
CLAIM = "342cd062-0205-45c7-b636-20d958b8fa75"
ROOT = Path("/home/aither/workspace/ai/vpsfree.cz")
CWD = ROOT / "worktrees" / SLUG / "haveapi"
EVIDENCE = ROOT / "work" / SLUG / "verification" / "dependency-refresh"
STATUS = EVIDENCE / "nixpkgs-update-status.json"
LOG = EVIDENCE / "nixpkgs-update.log"
COMMAND = [
    "nix", "develop", ".", "--command", "bash", "-euo", "pipefail", "-c",
    "./utils/update-nixpkgs.sh",
]
STARTED = time.monotonic()


def status(state, **extra):
    value = {
        "schema": 1, "state": state, "pid": os.getpid(),
        "pgid": os.getpgrp(), "claim": CLAIM, "cwd": str(CWD),
        "command": COMMAND, "log": str(LOG),
        "updatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "elapsedSeconds": round(time.monotonic() - STARTED, 3),
        **extra,
    }
    temporary = STATUS.with_suffix(".tmp")
    temporary.write_text(json.dumps(value, indent=2) + "\n")
    temporary.replace(STATUS)


def main():
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    assert not STATUS.exists() and not LOG.exists(), "Preserve earlier run evidence"
    status("awaiting_start", childPid=None, exitCode=None)
    print(f"READY pid={os.getpid()} status={STATUS}", flush=True)
    assert sys.stdin.readline().strip() == "START", "Explicit start signal required"
    claim = json.loads(subprocess.check_output([
        "dev-session", "coordination", "claim-status", SLUG, "--as-is",
        "--id", CLAIM, "--json",
    ], text=True))
    assert claim["state"] == "held"
    assert claim["ownerId"] == "e51277e3-c4c3-43eb-b889-90e84d91b5bf"
    assert subprocess.check_output([
        "git", "-C", str(CWD), "rev-parse", "HEAD",
    ], text=True).strip() == "c1823f3d70365b0442d0e2171bdf83bd4c6dbe31"
    assert not subprocess.check_output([
        "git", "-C", str(CWD), "status", "--porcelain",
    ], text=True).strip()
    for key in ("OVERCOMMIT_DISABLE", "OVERCOMMIT_DISABLED", "OVERCOMMIT_NO_VERIFY", "SKIP"):
        assert not os.environ.get(key), f"Unexpected hook override: {key}"
    environment = os.environ.copy()
    environment["DEV_WORKSPACE_CLAIM_ID"] = CLAIM
    with LOG.open("x") as stream:
        child = subprocess.Popen(COMMAND, cwd=CWD, env=environment,
                                 stdout=stream, stderr=subprocess.STDOUT)
        status("running", childPid=child.pid, exitCode=None)
        code = child.wait()
    status("completed", childPid=child.pid, exitCode=code)
    print(f"COMPLETED exit={code}", flush=True)
    return code


try:
    sys.exit(main())
except Exception as error:
    if EVIDENCE.exists():
        status("failed", childPid=None, exitCode=1, error=str(error))
    raise
