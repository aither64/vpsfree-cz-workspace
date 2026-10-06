"""Verify ordinary installed CLI startup; never send a model prompt or stop its daemon."""
import fcntl
import json
import os
from pathlib import Path
import pty
import re
import select
import signal
import struct
import subprocess
import tempfile
import termios
import time

os.umask(0o077)
assert not os.environ.get("CODEX_HOME") and not os.environ.get("CODEX_SQLITE_HOME")
parent = Path("/home/aither/.local/state/dev-workspaces/verification/2026-10-02-codex-package-portal-settings")
parent.mkdir(parents=True, exist_ok=True, mode=0o700)
assert parent.stat().st_uid == os.getuid() and not parent.stat().st_mode & 0o077
root = Path(tempfile.mkdtemp(prefix="live-cli-", dir=parent))
binary = "/run/current-system/sw/bin/codex"
environment = dict(os.environ, TERM="xterm-256color")
master, slave = pty.openpty()
fcntl.ioctl(slave, termios.TIOCSWINSZ, struct.pack("HHHH", 40, 144, 0, 0))
process = subprocess.Popen([binary, "--no-alt-screen"],
                           cwd="/home/aither/workspace/ai/vpsfree.cz", env=environment,
                           stdin=slave, stdout=slave, stderr=slave, start_new_session=True)
os.close(slave)
transcript = bytearray()
ready = False
daemon_ready = False
next_probe = 0
try:
    deadline = time.monotonic() + 45
    while time.monotonic() < deadline:
        if select.select([master], [], [], 0.1)[0]:
            try:
                chunk = os.read(master, 65536)
            except OSError:
                break
            transcript.extend(chunk)
            if b"\x1b[6n" in chunk:
                os.write(master, b"\x1b[1;1R")
            clean = re.sub(rb"\x1b\[[0-?]*[ -/]*[@-~]", b"", transcript).lower()
            if any(marker in clean for marker in [b"openai codex", b"welcome to codex",
                    b"sign in", b"do you trust", b"select an account"]):
                ready = True
        if ready and time.monotonic() >= next_probe:
            # The header precedes auto-bootstrap. Keep this TUI alive until
            # the ordinary daemon reports its actual running server version.
            probe = subprocess.run([binary, "app-server", "daemon", "version"],
                                   cwd="/home/aither/workspace/ai/vpsfree.cz", env=environment,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5)
            (root / "bootstrap-version.json").write_bytes(probe.stdout)
            (root / "bootstrap-version.stderr.log").write_bytes(probe.stderr)
            if probe.returncode == 0:
                state = json.loads(probe.stdout)
                daemon_ready = state.get("status") == "running" and all(
                    state.get(field) == "0.160.0" for field in
                    ["cliVersion", "managedCodexVersion", "appServerVersion"])
                if daemon_ready:
                    break
            next_probe = time.monotonic() + 1
        if process.poll() is not None:
            break
finally:
    if process.poll() is None:
        os.killpg(process.pid, signal.SIGINT)
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGTERM)
            process.wait(timeout=5)
    os.close(master)
    (root / "startup.log").write_bytes(transcript)
print("Private live CLI evidence:", root, flush=True)
assert b"no complete local package" not in transcript.lower(), "startup package error"
assert ready, "startup screen not reached; inspect private evidence"
assert daemon_ready, "ordinary daemon bootstrap not ready; inspect private evidence"
result = subprocess.run([binary, "app-server", "daemon", "version"], cwd=root,
                        env=environment, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                        timeout=30)
(root / "daemon-version.json").write_bytes(result.stdout)
(root / "daemon-version.stderr.log").write_bytes(result.stderr)
assert result.returncode == 0, "native daemon version query failed; inspect private evidence"
data = json.loads(result.stdout)
assert data.get("status") == "running", "native daemon is not running"
for field in ["cliVersion", "managedCodexVersion", "appServerVersion"]:
    assert data.get(field) == "0.160.0", f"native daemon {field} mismatch"
print("PASS: ordinary live CLI startup without --no-daemon or a model prompt")
print("PASS: native daemon CLI, managed package and actual server are 0.160.0")
# The normal user daemon and updater remain available; stop only the test TUI.
