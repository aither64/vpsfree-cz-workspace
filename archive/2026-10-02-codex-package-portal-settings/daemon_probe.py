"""Probe normal CLI/daemon startup in private state without any model request."""
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
import sys
import tempfile
import termios
import time

binary = str(Path(sys.argv[1]).resolve())
root = Path(tempfile.mkdtemp(prefix="codex-package-daemon-"))
home = root / "home"
home.mkdir(mode=0o700)
environment = dict(os.environ, CODEX_HOME=str(home), CODEX_SQLITE_HOME=str(home), OPENAI_API_KEY="",
                   CODEX_API_KEY="", TERM="xterm-256color")
print("private daemon artifacts:", root, flush=True)


def command(*args):
    result = subprocess.run([binary, "app-server", "daemon", *args],
                            env=environment, cwd=root, text=True,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            timeout=60)
    with (root / "daemon-commands.stderr.log").open("a") as log:
        log.write("daemon " + " ".join(args) + "\n" + result.stderr)
    print("daemon", *args, "exit", result.returncode, result.stdout.strip(), flush=True)
    assert result.returncode == 0, result.stdout
    return result.stdout


def startup(label, arguments):
    master, slave = pty.openpty()
    fcntl.ioctl(slave, termios.TIOCSWINSZ, struct.pack("HHHH", 40, 144, 0, 0))
    process = subprocess.Popen([binary, *arguments], cwd=root, env=environment,
                               stdin=slave, stdout=slave, stderr=slave,
                               start_new_session=True)
    os.close(slave)
    transcript = bytearray()
    ready = False
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
                clean = re.sub(rb"\x1b\[[0-?]*[ -/]*[@-~]", b"", transcript)
                if any(marker in clean.lower() for marker in
                       [b"sign in", b"welcome to codex", b"no saved session",
                        b"no previous session", b"log in"]):
                    ready = True
                    break
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
        (root / (label + ".log")).write_bytes(transcript)
    text = transcript.decode("utf-8", "replace").lower()
    assert "no complete local package" not in text, label
    assert "escapes package" not in text and "symlink escapes" not in text, label
    assert ready, f"{label}: no expected startup/login screen; inspect private log"
    print(label, "startup screen reached without package error", flush=True)


def version():
    data = json.loads(command("version"))
    for field in ["cliVersion", "managedCodexVersion", "appServerVersion"]:
        assert data.get(field) == "0.160.0", f"{field} mismatch: {data.get(field)!r}"
    return data


try:
    # No explicit daemon start: this must exercise ordinary auto-bootstrap.
    startup("plain", ["--no-alt-screen"])
    version()
    startup("resume", ["resume", "--last", "--no-alt-screen"])
    startup("fork", ["fork", "--last", "--no-alt-screen"])
    manifests = list((home / "packages" / "app-server-daemon").rglob("codex-package.json"))
    assert manifests, "daemon did not copy a complete local package"
    for manifest in manifests:
        data = json.loads(manifest.read_text())
        assert data["version"] == "0.160.0" and data["layoutVersion"] == 1, data
        package = manifest.parent
        for relative in ["bin/codex", "bin/codex-code-mode-host", "bin/logs_client",
                         "codex-path/rg", "codex-resources/bwrap"]:
            path = package / relative
            assert path.is_file() and os.access(path, os.X_OK), relative
            assert not path.is_symlink(), relative
    print("daemon copied complete 0.160.0 runtime", flush=True)
    command("restart")
    version()
    print("PASS: normal CLI/resume/fork and copied-daemon restart", flush=True)
finally:
    try:
        command("stop")
    finally:
        subprocess.run([sys.executable, str(Path(__file__).with_name("cleanup_private_daemon.py")),
                        str(root)], check=True)
