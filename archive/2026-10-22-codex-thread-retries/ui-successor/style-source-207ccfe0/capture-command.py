#!/usr/bin/env python3
"""Retain one explicitly selected command's own logs and exit receipt."""
import datetime
import json
import os
from pathlib import Path
import subprocess
import sys
import time

if len(sys.argv) < 3:
    raise SystemExit("usage: capture-command.py OUTPUT_DIRECTORY COMMAND [ARG...]")
output = Path(sys.argv[1]).resolve()
command = sys.argv[2:]
output.mkdir(parents=True, exist_ok=False)
repo = Path("/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries/dev-workspace")
def identity():
    return subprocess.check_output(["git", "-C", str(repo), "rev-parse", "HEAD", "HEAD^{tree}"], text=True).splitlines()
def write(value):
    temporary = output / "result.json.tmp"
    temporary.write_text(json.dumps(value, indent=2) + "\n")
    temporary.replace(output / "result.json")
started = time.monotonic_ns()
record = {"schema": 1, "provenance": "This wrapper owns one subprocess.run; logs open before command launch.",
          "command": command, "cwd": os.getcwd(), "source_before": identity(),
          "started_at": datetime.datetime.now(datetime.UTC).isoformat(), "status": "running"}
write(record)
environment = os.environ.copy()
environment["PORTAL_RETRY_SCREENSHOTS"] = str(output / "screenshots")
with (output / "stdout.log").open("xb") as stdout, (output / "stderr.log").open("xb") as stderr:
    try:
        result = subprocess.run(command, env=environment, stdout=stdout, stderr=stderr, check=False)
        raw_code = result.returncode
        code = raw_code if raw_code >= 0 else 128 - raw_code
    except OSError as error:
        raw_code = None
        code = 127
        record["launch_error"] = str(error)
record.update({"status": "completed", "raw_returncode": raw_code, "exit_code": code,
               "finished_at": datetime.datetime.now(datetime.UTC).isoformat(),
               "elapsed_ms": (time.monotonic_ns() - started) // 1000000, "source_after": identity()})
record["source_changed"] = record["source_before"] != record["source_after"]
write(record)
print(json.dumps({"result": str(output / "result.json"), "exit_code": code,
                  "elapsed_ms": record["elapsed_ms"], "source_changed": record["source_changed"]}), flush=True)
raise SystemExit(code if code else int(record["source_changed"]))
