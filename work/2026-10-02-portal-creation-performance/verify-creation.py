#!/usr/bin/env python3
"""Deferred isolated real-package creation benchmark. Never run on production state.

Read verification-prototype.md before execution. This file uses Python's standard
library and package binaries; it does not build, install or activate anything.
"""

import argparse
import datetime as dt
import fcntl
import hashlib
import http.client
import json
import os
from pathlib import Path
import queue
import re
import shlex
import shutil
import socket
import stat
import statistics
import subprocess
import sys
import tempfile
import threading
import time
import urllib.parse


PREFIX = b"\x1eDEV_WORKSPACE_CREATION_PROGRESS/1 "
BINDING = Path("/home/aither/workspace/ai/vpsfree.cz")
GOAL = ("This is an isolated session-creation verification. Reply with exactly READY. "
        "Do not use tools, inspect files, delegate, change state, set a goal, or "
        "perform any session lifecycle action.")
MAX_OUTPUT = 16 * 1024 * 1024
SEEDED_ROOT = Path("/tmp/pcp-oct02-a")
SEEDED_PACKAGE = Path("/nix/store/0klh7dhca2dwyfwsz0m67pbjj2nml70d-dev-workspace-0.2.0")
WORKSPACE_FIXTURE = {"schema": 2, "displayLabel": "Isolated creation verification",
                     "hostLabel": "verification", "sshHost": "",
                     "portal": {"hostname": "creation.invalid", "aliases": []},
                     "developmentClusterProviders": []}


class Failure(Exception):
    pass


def require(value, message):
    if not value:
        raise Failure(message)


def stamp():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def instant(value):
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00")).timestamp()


def save(path, value):
    path = Path(path)
    with path.open("w", encoding="utf-8") as stream:
        os.chmod(path, 0o600)
        json.dump(value, stream, indent=2, sort_keys=True)
        stream.write("\n")


def append(path, value):
    encoded = (json.dumps(value, separators=(",", ":")) + "\n").encode()
    descriptor = os.open(path, os.O_WRONLY | os.O_APPEND | os.O_CREAT, 0o600)
    try:
        os.write(descriptor, encoded)
    finally:
        os.close(descriptor)


def read(path):
    with Path(path).open(encoding="utf-8") as stream:
        return json.load(stream)


def run(argv, environment, root, label, timeout=60, input_bytes=None, record_stderr=True):
    # Do not put argv, environment, auth data, or raw command output on stdout.
    error_path = root / (label + ".stderr.log") if record_stderr else Path(os.devnull)
    with error_path.open("ab") as error:
        result = subprocess.run(argv, input=input_bytes, stdout=subprocess.PIPE,
                                stderr=error, env=environment, cwd=root, timeout=timeout)
    require(result.returncode == 0, f"{label} failed (exit {result.returncode}); private stderr retained")
    require(len(result.stdout) <= MAX_OUTPUT, f"{label} output exceeded limit")
    return result.stdout


def inherited_fds():
    result = []
    for key in ("DEV_WORKSPACE_TRANSITION_LOCK_FD", "DEV_SESSION_LIFECYCLE_LOCK_FD"):
        value = os.environ.get(key)
        if value and value.isdecimal():
            descriptor = int(value)
            os.fstat(descriptor)
            result.append(descriptor)
    return tuple(result)


def option(argv, name):
    return argv[argv.index(name) + 1] if name in argv else None


def forward_stderr(pipe, event_path, on_event=None):
    # Fixed-size reads; never wait for an unbounded diagnostic line.
    pending = b""
    discarding = False
    while True:
        chunk = os.read(pipe.fileno(), 16384)
        if not chunk:
            break
        os.write(2, chunk)
        for value in chunk:
            if discarding:
                if value == 10:
                    discarding = False
                continue
            if not pending and value != 30:
                continue
            pending += bytes((value,))
            if len(pending) > 4096:
                pending = b""
                discarding = value != 10
            elif value == 10:
                frame, pending = pending, b""
                if not frame.startswith(PREFIX):
                    continue
                try:
                    event = json.loads(frame[len(PREFIX):])
                except (ValueError, UnicodeDecodeError):
                    continue
                if isinstance(event, dict):
                    append(event_path, {"observedAt": stamp(), "monotonicNs": time.monotonic_ns(),
                                        "progress": event})
                    if on_event:
                        on_event(event)


CORRECTED_FAULT_SLUGS = ("2026-10-02-creation-root-loss-corrected", "2026-10-02-creation-member-loss")


def creation_fault_path(config, slug):
    # Preserve the stranded original fault evidence in fault.json.
    corrected = config.get("rootRecoveryProvider") is not None and slug in CORRECTED_FAULT_SLUGS
    return Path(config["root"]) / ("corrected-fault.json" if corrected else "fault.json")


def root_recovery_provider(config, argv):
    """Only the two retained-fixture thread/create calls may use this test provider."""
    original = str(Path(config["package"]) / "bin/workspace-portal")
    selected = config.get("rootRecoveryProvider")
    if selected is None or argv[:2] != ["thread", "create"] or option(argv, "--session-slug") not in CORRECTED_FAULT_SLUGS:
        return original
    require(config["root"] == str(SEEDED_ROOT) and config["package"] == str(SEEDED_PACKAGE)
            and isinstance(selected, dict) and set(selected) == {"path", "sha256"},
            "corrected provider is outside the exact fault fixture")
    path = Path(selected["path"])
    require(path.is_absolute() and path.resolve(strict=True) == path
            and path.parent.name == "bin" and path.name == "workspace-portal"
            and path.parent.parent.parent == Path("/nix/store") and str(path) != original
            and path.is_file() and os.access(path, os.X_OK)
            and isinstance(selected["sha256"], str) and re.fullmatch(r"[0-9a-f]{64}", selected["sha256"]),
            "corrected provider identity is invalid")
    binary = path.read_bytes()
    require(binary.startswith(b"\x7fELF") and hashlib.sha256(binary).hexdigest() == selected["sha256"],
            "corrected compiled provider hash changed")
    return str(path)


def child_mode(kind, config_path, argv):
    """Executable fixtures at the same boundary used by CommandRunner tests."""
    config = read(config_path)
    root = Path(config["root"])
    package = Path(config["package"])
    if kind == "dev-session":
        slug = argv[1] if len(argv) > 1 else "unknown"
        require(re.fullmatch(r"[A-Za-z0-9_-]+", slug), "unexpected helper slug")
        command = [str(package / "libexec/workspace-portal/dev-session"),
                   *config["devSessionArgs"], "--", *argv]
        event_path = root / "events" / (slug + ".jsonl")
        append(event_path, {"observedAt": stamp(), "monotonicNs": time.monotonic_ns(),
                            "boundary": "dev-session-begin"})
        process = subprocess.Popen(command, stderr=subprocess.PIPE, pass_fds=inherited_fds())
        forward_stderr(process.stderr, event_path)
        code = process.wait()
        append(event_path, {"observedAt": stamp(), "monotonicNs": time.monotonic_ns(),
                            "boundary": "dev-session-end", "exitCode": code})
        return code

    actual = root_recovery_provider(config, argv)
    if actual != str(package / "bin/workspace-portal"):
        append(root / "events" / (option(argv, "--session-slug") + ".jsonl"),
               {"observedAt": stamp(), "monotonicNs": time.monotonic_ns(),
                "providerDispatch": {**config["rootRecoveryProvider"],
                                     "argvSHA256": hashlib.sha256(json.dumps(argv).encode()).hexdigest()}})
    fault_path = creation_fault_path(config, option(argv, "--session-slug"))
    fault = read(fault_path) if fault_path.exists() else {}
    matches = (fault.get("armed") and option(argv, "--session-slug") == fault.get("slug"))
    root_loss = matches and fault.get("kind") == "root-response" and argv[:2] == ["thread", "create"]
    member_loss = matches and fault.get("kind") == "member-progress" and argv[:2] == ["team", "apply-preset"]
    if not (root_loss or member_loss):
        os.execv(actual, [actual, *argv])

    # Only this exact helper PID is faulted. The portal, App Server and tmux stay.
    process = subprocess.Popen([actual, *argv], stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, pass_fds=inherited_fds())
    output = bytearray()

    def drain_stdout():
        while True:
            chunk = os.read(process.stdout.fileno(), 16384)
            if not chunk:
                return
            if len(output) + len(chunk) > MAX_OUTPUT:
                fault["injectionError"] = "helper stdout exceeded bound"
                process.kill()
                return
            output.extend(chunk)

    def inject(event):
        if member_loss and fault.get("armed") and event.get("stage") == "team_member" and event.get("event") == "finish":
            fault.update(armed=False, triggeredAt=stamp(), member=event.get("member"), helperPID=process.pid)
            save(fault_path, fault)
            try:
                process.kill()
            except ProcessLookupError:
                fault["injectionError"] = "helper already exited at member boundary"
                save(fault_path, fault)

    reader = threading.Thread(target=drain_stdout)
    reader.start()
    fault_events = "corrected-fault-events.jsonl" if fault_path.name == "corrected-fault.json" else "fault-events.jsonl"
    forward_stderr(process.stderr, root / fault_events, inject)
    code = process.wait()
    reader.join()
    if root_loss and code == 0:
        response = json.loads(output)
        require(isinstance(response.get("threadId"), str), "root helper returned no thread ID")
        fault.update(armed=False, triggeredAt=stamp(), rootThreadID=response["threadId"], helperPID=process.pid)
        save(fault_path, fault)
        os.write(2, b"verification: successful root helper response intentionally withheld\n")
        return 97
    if member_loss and not fault.get("armed"):
        os.write(2, b"verification: team helper intentionally interrupted after member progress\n")
        return 98
    os.write(1, bytes(output))
    return code if code >= 0 else 128 - code


class StdioRPC:
    """The real Codex stdio interface, used only before the portal starts."""

    def __init__(self, binary, environment, root):
        self.error = (root / "seed-app-server.stderr.log").open("ab")
        self.process = subprocess.Popen([str(binary), "app-server"], env=environment, cwd=root,
                                        stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                        stderr=self.error, start_new_session=True)
        self.messages = queue.Queue(maxsize=128)
        self.serial = 0

        def reader():
            try:
                while True:
                    line = self.process.stdout.readline(MAX_OUTPUT + 1)
                    if not line:
                        self.messages.put(None)
                        return
                    if len(line) > MAX_OUTPUT:
                        self.messages.put(Failure("seed RPC record exceeded bound"))
                        return
                    self.messages.put(json.loads(line))
            except Exception:
                self.messages.put(Failure("seed RPC reader failed"))

        self.reader = threading.Thread(target=reader, daemon=True)
        self.reader.start()
        self.call("initialize", {"clientInfo": {"name": "dev-workspace", "version": "0.1.0"},
                                 "capabilities": {"experimentalApi": True}})
        self.send({"method": "initialized"})

    def send(self, value):
        self.process.stdin.write((json.dumps(value) + "\n").encode())
        self.process.stdin.flush()

    def call(self, method, params):
        self.serial += 1
        current = self.serial
        self.send({"id": current, "method": method, "params": params})
        deadline = time.monotonic() + 60
        while True:
            try:
                message = self.messages.get(timeout=max(0.01, deadline - time.monotonic()))
            except queue.Empty:
                raise Failure(f"seed {method} timed out; process retained") from None
            require(message is not None and not isinstance(message, Exception), "seed RPC connection failed")
            if message.get("id") == current and "method" not in message:
                require("error" not in message, f"seed {method} returned an RPC error; no response body logged")
                return message.get("result", {})
            if "id" in message and "method" in message:
                self.send({"id": message["id"], "error": {"code": -32601, "message": "verification has no tool handler"}})

    def finish(self):
        # End the foreground stdio task normally; retain every generated thread.
        self.process.stdin.close()
        try:
            code = self.process.wait(timeout=30)
        except subprocess.TimeoutExpired:
            raise Failure("seed stdio task did not exit on EOF; process retained") from None
        self.error.close()
        require(code == 0, "seed stdio task failed on EOF")


class UnixHTTP(http.client.HTTPConnection):
    def __init__(self, path):
        super().__init__("creation.invalid", timeout=30)
        self.path = str(path)

    def connect(self):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.sock.settimeout(self.timeout)
        self.sock.connect(self.path)


def http(config, method, path, body=None):
    connection = UnixHTTP(config["portalSocket"])
    headers = {"Host": "creation.invalid", "Origin": "https://creation.invalid", "Accept": "application/json"}
    if isinstance(body, dict):
        body = json.dumps(body)
        headers["Content-Type"] = "application/json"
    elif body is not None:
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    try:
        connection.request(method, path, body=body, headers=headers)
        response = connection.getresponse()
        data = response.read(MAX_OUTPUT + 1)
        require(len(data) <= MAX_OUTPUT, "HTTP response exceeded bound")
        require(response.status in (200, 202), f"{method} {path} returned HTTP {response.status}")
        return json.loads(data)
    finally:
        connection.close()


def wait_socket(path, process, label):
    deadline = time.monotonic() + 45
    while time.monotonic() < deadline:
        require(process.poll() is None, f"{label} exited before publishing its socket")
        if path.exists() and stat.S_ISSOCK(path.stat().st_mode):
            return
        time.sleep(0.05)
    raise Failure(f"{label} socket not ready; process retained")


def spawn(argv, environment, root, label, processes):
    log = (root / (label + ".log")).open("ab")
    process = subprocess.Popen(argv, env=environment, cwd=root, stdin=subprocess.DEVNULL,
                               stdout=log, stderr=log, start_new_session=True)
    log.close()
    processes.append({"label": label, "pid": process.pid, "startedAt": stamp()})
    save(root / "processes.json", processes)
    return process


def seed_history(config, environment, preset, count, padding, timeout):
    root = Path(config["root"])
    home = Path(config["codexHome"])
    started = time.monotonic()
    server = StdioRPC(Path(config["codex"]), environment, root)
    save(root / "seed-process.json", {"pid": server.process.pid, "startedAt": stamp()})
    for index in range(count):
        require(time.monotonic() - started < timeout, "history setup deadline reached; seed process retained")
        directory = root / "history" / str(index % 128)
        directory.mkdir(parents=True, exist_ok=True, mode=0o700)
        result = server.call("thread/start", {"cwd": str(directory), "model": preset["leadModel"],
                             "threadSource": "vscode", "approvalPolicy": "never", "sandbox": "read-only"})
        identifier = result["thread"]["id"]
        server.call("thread/inject_items", {"threadId": identifier, "items": [{"type": "message",
                    "role": "developer", "content": [{"type": "input_text", "text":
                    "Synthetic creation-performance history; no model turn. " + ("x" * padding)}]}]})
        metadata = server.call("thread/read", {"threadId": identifier, "includeTurns": False})["thread"]
        require(metadata.get("source") == "vscode", "seed history has the wrong source classification")
        rollout = Path(metadata.get("path", "")).resolve()
        require(rollout.is_relative_to(home) and rollout.is_file(), "seed did not persist isolated history")
        server.call("thread/unsubscribe", {"threadId": identifier})
        if (index + 1) % 250 == 0:
            print(f"Seeded {index + 1}/{count} synthetic historical threads", flush=True)
    server.finish()
    paths = list((home / "sessions").rglob("*.jsonl"))
    require(len(paths) == count, "seed history file count differs from requested count")
    result = {"activeRollouts": len(paths), "archivedRollouts": 0, "paddingBytesPerThread": padding,
              "bytes": sum(path.stat().st_size for path in paths),
              "seconds": time.monotonic() - started,
              "shape": "real start/inject metadata; synthetic developer-only history; no model turns"}
    save(root / "history.json", result)
    return result


def validate_seeded_rollout(path, root):
    """Read private synthetic history only; never log its payloads."""
    require(16384 <= path.stat().st_size <= MAX_OUTPUT, "seed rollout size is unexpected")
    metadata, injected = [], 0
    padding = "Synthetic creation-performance history; no model turn. " + "x" * 16384
    for raw in path.read_bytes().splitlines():
        item = json.loads(raw)
        kind, payload = item.get("type"), item.get("payload", {})
        require(kind in ("session_meta", "response_item", "world_state", "turn_context"),
                "seed rollout contains unexpected activity")
        if kind == "session_meta":
            metadata.append(payload)
        elif kind == "response_item":
            require(payload.get("type") == "message" and payload.get("role") in ("developer", "user"),
                    "seed rollout contains model or tool activity")
            injected += (payload.get("role") == "developer" and
                         payload.get("content") == [{"type": "input_text", "text": padding}])
    require(len(metadata) == 1 and injected == 1, "seed rollout lacks its exact original seed payload")
    meta = metadata[0]
    identifier = meta.get("id")
    require(isinstance(identifier, str) and re.fullmatch(r"[0-9a-f-]{36}", identifier)
            and path.name.endswith(identifier + ".jsonl"), "seed rollout identity differs")
    require(meta.get("source") == "vscode" and meta.get("cli_version") == "0.160.0"
            and meta.get("cwd") in {str(root / "history" / str(i)) for i in range(128)},
            "seed rollout source, version or cwd differs")
    return identifier


def require_no_seeded_services(root, seed_pid):
    # This exact pre-registration fixture recorded only the seed subprocess.
    # validate_seeded_resume separately refuses runtime/registration markers.
    # Refuse reused PIDs too: the original fixture did not record a process start tick.
    require(type(seed_pid) is int and seed_pid > 0 and not Path(f"/proc/{seed_pid}").exists(),
            "seed process remains or its PID is ambiguous")
    require(str(root) + "/" not in Path("/proc/net/unix").read_text(),
            "a private runtime socket remains")


def validate_seeded_resume(root, package, auth, args):
    """One known pre-registration failure only. This function never writes."""
    require(root == SEEDED_ROOT and root.resolve(strict=True) == root and package == SEEDED_PACKAGE,
            "seeded continuation requires the exact original root and candidate")
    require(args.team_id == "delegated" and args.history_count == 3379
            and args.history_padding_bytes == 16384 and args.model_timeout == 180
            and args.history_timeout == 3600 and not args.skip_faults,
            "seeded continuation requires the original settings and every acceptance gate")
    info = root.lstat()
    require(stat.S_ISDIR(info.st_mode) and info.st_uid == os.geteuid()
            and stat.S_IMODE(info.st_mode) == 0o700, "seeded root must be owned mode 0700")
    expected = {"bin", "codex", "codex-version.stderr.log", "events", "history", "history.json",
                "preset.json", "r", "register.stderr.log", "result.json", "seed-app-server.stderr.log",
                "seed-process.json", "skills", "state", "team-preset.stderr.log", "workspace",
                "xdg-cache", "xdg-config", "xdg-state"}
    require({p.name for p in root.iterdir()} == expected,
            "seeded fixture has missing, unexpected or previous-continuation records")
    for path in root.rglob("*"):
        info = path.lstat()
        require((stat.S_ISDIR(info.st_mode) or stat.S_ISREG(info.st_mode))
                and info.st_uid == os.geteuid() and not info.st_mode & 0o022,
                "seeded fixture contains a link, special file, foreign owner or writable path")
    retained_auth = root / "codex/auth.json"
    require(auth == retained_auth and stat.S_ISREG(retained_auth.lstat().st_mode)
            and stat.S_IMODE(retained_auth.lstat().st_mode) == 0o600,
            "continuation must reuse the owned mode-0600 auth file; no credential copy")
    for name in ("bin", "events", "r", "skills", "xdg-cache", "xdg-config", "xdg-state",
                 "workspace/work", "workspace/worktrees", "workspace/archive", "workspace/repos"):
        require((root / name).is_dir() and not any((root / name).iterdir()),
                "seeded fixture has runtime, creation or unexpected setup records")
    require({p.name for p in (root / "workspace").iterdir()} ==
            {"work", "worktrees", "archive", "repos", "AGENTS.md", ".dev-workspace.json"},
            "seeded workspace layout changed")
    require({p.name for p in (root / "state").iterdir()} == {"transition.lock"},
            "seeded host state contains more than the original registration lock")
    lock = root / "state/transition.lock"
    require(lock.stat().st_size == 0, "original registration lock is not empty")
    with lock.open("rb") as stream:
        try:
            fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise Failure("original registration lock is held") from None
    old_fixture = {k: v for k, v in WORKSPACE_FIXTURE.items() if k != "sshHost"}
    require(read(root / "workspace/.dev-workspace.json") == old_fixture,
            "workspace fixture is not the original missing-sshHost failure")
    require((root / "codex/config.toml").read_text() == 'cli_auth_credentials_store = "file"\n',
            "retained Codex settings changed")
    require((root / "workspace/AGENTS.md").read_text() ==
            "This is an isolated benchmark fixture. Do not use tools or change state for the initial READY request.\n",
            "retained workspace instructions changed")
    require({p.name for p in (root / "history").iterdir()} == {str(i) for i in range(128)}
            and all(p.is_dir() and not any(p.iterdir()) for p in (root / "history").iterdir()),
            "synthetic history cwd layout changed")
    previous = read(root / "result.json")
    require(set(previous) == {"candidate", "error", "finishedAt", "history", "results", "startedAt", "state"}
            and previous["state"] == "incomplete" and previous["results"] == []
            and previous["candidate"] == str(package)
            and previous["error"] == "register failed (exit 1); private stderr retained",
            "continuation requires the original registration failure with zero creations")
    require((root / "register.stderr.log").read_text().strip() ==
            f"error: invalid workspace configuration: {root}/workspace/.dev-workspace.json",
            "registration diagnostic differs from the supported failure")
    seed = read(root / "seed-process.json")
    require(set(seed) == {"pid", "startedAt"}
            and instant(previous["startedAt"]) <= instant(seed["startedAt"]) <= instant(previous["finishedAt"]),
            "seed process record does not belong to the failed run")
    require_no_seeded_services(root, seed["pid"])
    history = read(root / "history.json")
    require(previous["history"] == history and history["activeRollouts"] == 3379
            and history["archivedRollouts"] == 0 and history["paddingBytesPerThread"] == 16384
            and history["seconds"] > 0 and history["shape"] ==
            "real start/inject metadata; synthetic developer-only history; no model turns",
            "original history evidence differs or does not meet the acceptance dimensions")
    require(not (root / "codex/archived_sessions").exists(), "archived history is unexpected")
    paths = list((root / "codex/sessions").rglob("*.jsonl"))
    require(len(paths) == 3379 and sum(p.stat().st_size for p in paths) == history["bytes"],
            "persisted history count or bytes differ from completed seeding")
    require(len({validate_seeded_rollout(path, root) for path in paths}) == 3379,
            "seeded history has duplicate identities")
    return previous


def preserve_seeded_failure(root):
    # mkdir is the single-use claim. Any interruption leaves it present and refuses a retry.
    preserved = root / "seeded-continuation"
    try:
        preserved.mkdir(mode=0o700)
    except FileExistsError:
        raise Failure("seeded continuation was already claimed; parent diagnosis required") from None
    for name in ("result.json", "register.stderr.log", "workspace/.dev-workspace.json"):
        with (preserved / Path(name).name).open("xb") as target:
            os.fchmod(target.fileno(), 0o600)
            target.write((root / name).read_bytes())
            target.flush()
            os.fsync(target.fileno())
    for directory in (preserved, root):
        descriptor = os.open(directory, os.O_RDONLY | os.O_DIRECTORY)
        try:
            os.fsync(descriptor)
        finally:
            os.close(descriptor)


def wait_creation(config, status, timeout=240):
    root = Path(config["root"])
    slug = status["slug"]
    previous = None
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        current = http(config, "GET", f"/api/sessions/{slug}/creation")
        projection = {key: current.get(key) for key in ("state", "phase", "attempt", "startedAt", "updatedAt")}
        if projection != previous:
            append(root / "events" / (slug + ".jsonl"),
                   {"observedAt": stamp(), "monotonicNs": time.monotonic_ns(), "httpStatus": projection})
            previous = projection
        if current["state"] != "running":
            return current
        time.sleep(0.1)
    raise Failure(f"creation {slug} exceeded observation deadline; no cancellation performed")


def snapshot(config, slug):
    root = Path(config["state"])
    workspace = config["workspace"]
    namespace = Path(workspace).name + "-" + hashlib.sha256(workspace.encode()).hexdigest()[:16]
    receipt = read(root / "portal" / namespace / "creations" / (slug + ".json"))
    roster_path = root / "codex-teams" / namespace / (slug + ".json")
    roster = read(roster_path) if roster_path.exists() else None
    return receipt, roster


def ready_evidence(config, status, preset):
    receipt, roster = snapshot(config, status["slug"])
    require(receipt["state"] == "ready" and receipt["schema"] == 3, "Full-team receipt not ready")
    require(roster and roster["slug"] == status["slug"] and roster["workspace"] == config["workspace"],
            "missing or wrong ready roster")
    require(roster["catalogDigest"] == preset["catalogDigest"] and roster["teamDigest"] == preset["teamDigest"],
            "catalog snapshot changed")
    require(len(roster["members"]) == len(preset["members"]), "ready member count differs")
    for member, expected in zip(roster["members"], preset["members"]):
        require(member["state"] == "ready" and member.get("threadId"), "member has no ready thread")
        for key in ("address", "model", "reasoningEffort", "purpose", "access", "instructions"):
            require(member.get(key) == expected.get(key), f"retained member {key} changed")
    return receipt, roster


def initial_goal_parts(payload):
    # Selected 0.160 persists classifications aligned with canonical content.
    content = payload.get("content", [])
    kinds = (payload.get("internal_chat_message_metadata_passthrough") or {}).get("content_item_kinds")
    require(content and isinstance(kinds, list) and len(kinds) == len(content),
            "canonical user content has no aligned classifications")
    count = 0
    contexts = {"agents_md.instructions": ("# AGENTS.md instructions", "</INSTRUCTIONS>"),
                "environments.environment_context": ("<environment_context>", "</environment_context>")}
    for part, kind in zip(content, kinds):
        require(part.get("type") == "input_text" and isinstance(part.get("text"), str),
                "unexpected canonical user content type")
        text = part["text"]
        if kind == "user.text":
            require(text == GOAL, "unexpected initial user request")
            count += 1
        else:
            require(kind in contexts and text.startswith(contexts[kind][0]) and text.endswith(contexts[kind][1]),
                    "unexpected canonical user context")
    return count


def wait_model(config, slug, root_id, timeout):
    # Read only timestamps/types/counts. Never log rollout text or model output.
    started = time.monotonic()
    response_at = None
    completed_at = None
    count = 0
    while time.monotonic() - started < timeout:
        paths = list((Path(config["codexHome"]) / "sessions").rglob(f"*{root_id}.jsonl"))
        require(len(paths) <= 1, "multiple rollouts use a recorded root ID")
        if paths:
            count = 0
            for raw in paths[0].read_bytes().splitlines():
                try:
                    item = json.loads(raw)
                except ValueError:
                    continue  # A final partial write will be read on the next poll.
                payload = item.get("payload", {})
                kind = payload.get("type")
                # Codex 0.160 ResponseItem uses snake_case: every invocation
                # ends in _call. Outputs also prove tool activity; tool search
                # is the only output variant without the _call_output suffix.
                tool_activity = isinstance(kind, str) and (
                    kind.endswith(("_call", "_call_output")) or kind == "tool_search_output")
                require(not tool_activity,
                        f"benchmark model used a tool in {slug}; inspect private evidence")
                if item.get("type") == "event_msg" and kind == "user_message":
                    require(payload.get("message") == GOAL, "unexpected initial user request echo")
                if item.get("type") == "response_item" and kind == "message" and payload.get("role") == "user":
                    count += initial_goal_parts(payload)
                if ((item.get("type") == "response_item" and kind == "message" and payload.get("role") == "assistant")
                        or (item.get("type") == "event_msg" and kind == "agent_message")):
                    response_at = response_at or item.get("timestamp")
                if item.get("type") == "event_msg" and kind == "task_complete":
                    completed_at = item.get("timestamp")
            if completed_at:
                require(count == 1, "initial request was absent or submitted more than once")
                require(response_at, "model turn completed without an assistant response")
                return {"firstAssistantAt": response_at, "turnCompletedAt": completed_at,
                        "initialUserMessages": count}
        time.sleep(0.25)
    raise Failure(f"model completion not observed within {timeout}s for {slug}; readiness timing remains separate")


def create(config, preset, name, model_timeout, fault_kind=None):
    root = Path(config["root"])
    date = dt.datetime.now(dt.timezone.utc).date().isoformat()
    slug = date + "-" + name
    if fault_kind:
        save(creation_fault_path(config, slug), {"kind": fault_kind, "slug": slug, "armed": True})
    request_start = time.monotonic_ns()
    accepted = http(config, "POST", "/sessions", urllib.parse.urlencode({
        "name": name, "creation_date": date, "goal": GOAL,
        "team": preset["id"], "catalogDigest": preset["catalogDigest"]}))
    require(accepted["slug"] == slug and accepted["attempt"] == 1, "unexpected creation acceptance")
    status = wait_creation(config, accepted)
    result = {"slug": slug, "acceptedAt": accepted["startedAt"], "firstAttempt": status}
    before = None
    if fault_kind:
        fault = read(creation_fault_path(config, slug))
        require(not fault.get("armed") and not fault.get("injectionError"), "fault boundary was not reached")
        require(status["state"] in ("failed", "paused"), "fault did not leave a retryable receipt")
        before_receipt, before = snapshot(config, slug)
        if fault_kind == "member-progress":
            require(before and any(member["state"] == "ready" for member in before["members"]),
                    "no member had completed before interruption")
            require(any(member["state"] != "ready" for member in before["members"]),
                    "partial-member boundary missed: all members ready; result is inconclusive")
        save(root / (name + "-before-retry.json"), {"receipt": before_receipt, "roster": before, "fault": fault})
        result["fault"] = fault
        retried = http(config, "POST", f"/api/sessions/{slug}/creation/retry",
                       {"receiptId": status["receiptId"], "attempt": status["attempt"]})
        require(retried["attempt"] == 2 and retried["receiptId"] == accepted["receiptId"], "retry identity changed")
        status = wait_creation(config, retried)
    return complete_creation(config, preset, name, slug, model_timeout, fault_kind,
                             request_start, accepted, result, before, status)


def complete_creation(config, preset, name, slug, model_timeout, fault_kind,
                      request_start, accepted, result, before, status):
    root = Path(config["root"])
    require(status["state"] == "ready", f"creation {slug} ended as {status['state']}; private receipt retained")
    ready_observed = time.monotonic_ns()
    receipt, roster = ready_evidence(config, status, preset)
    if before:
        require(before["rootThreadId"] == roster["rootThreadId"], "partial-member retry replaced its root")
        final_members = {member["address"]: member for member in roster["members"]}
        for member in before["members"]:
            if member["state"] == "ready":
                require(final_members[member["address"]]["threadId"] == member["threadId"], "retry replaced a ready member")
    result.update(readyAt=receipt["updatedAt"], readyObservedAt=stamp(),
                  observedRequestToReadySeconds=(ready_observed - request_start) / 1e9,
                  acceptanceToReadySeconds=instant(receipt["updatedAt"]) - instant(accepted["startedAt"]),
                  rootThreadID=roster["rootThreadId"],
                  memberThreadIDs={member["address"]: member["threadId"] for member in roster["members"]})
    save(root / (name + "-ready.json"), result)
    model = wait_model(config, slug, roster["rootThreadId"], model_timeout)
    model["acceptanceToFirstAssistantSeconds"] = instant(model["firstAssistantAt"]) - instant(accepted["startedAt"])
    model["readyToFirstAssistantSeconds"] = instant(model["firstAssistantAt"]) - instant(receipt["updatedAt"])
    result["model"] = model
    if fault_kind == "root-response":
        result["rootOutcome"] = ("same ID recovered" if result["fault"]["rootThreadID"] == roster["rootThreadId"]
                                 else "unmaterialized root replaced after helper disconnected")
        if result["fault"]["rootThreadID"] != roster["rootThreadId"]:
            old = list((Path(config["codexHome"]) / "sessions").rglob(f"*{result['fault']['rootThreadID']}.jsonl"))
            require(not old, "root replacement left materialized history for the lost root")
    result["stages"] = progress_evidence(config, slug, preset)
    save(root / (name + "-result.json"), result)
    print(f"{name}: ready in {result['acceptanceToReadySeconds']:.3f}s; "
          f"first assistant in {model['acceptanceToFirstAssistantSeconds']:.3f}s", flush=True)
    return result


def progress_evidence(config, slug, preset):
    root = Path(config["root"])
    events = [json.loads(line) for line in (root / "events" / (slug + ".jsonl")).read_text().splitlines()]
    stages = [event for event in events if "progress" in event]
    finished = [event["progress"] for event in stages if event["progress"].get("event") == "finish"]
    require({"conversation", "prompt", "terminal", "evidence"}.issubset({event.get("stage") for event in finished}),
            "required completed progress stages were not forwarded through Ruby")
    require(len([event for event in finished if event.get("stage") == "team_member"]) >= len(preset["members"]),
            "per-member completion progress is missing")
    visible = [event["httpStatus"] for event in events if event.get("httpStatus", {}).get("state") == "running"]
    broad = {"Checking session settings…", "Checking recorded request…", "Initializing the conversation and terminal…"}
    require(any(event.get("phase") not in broad for event in visible), "no live detailed phase was visible before ready")
    return stages


def native_codex_entrypoint(launcher):
    """Resolve the owning docs/codex-package.md layout, not the public shell launcher."""
    launcher = Path(launcher).resolve(strict=True)
    require(launcher.name == "codex" and launcher.parent.name == "bin"
            and launcher.parent.parent.parent == Path("/nix/store"), "unexpected public Codex package layout")
    runtime = launcher.parent.parent / "libexec/codex"
    manifest = read(runtime / "codex-package.json")
    require(manifest == {"layoutVersion": 1, "version": "0.160.0", "variant": "codex",
                         "target": "x86_64-unknown-linux-gnu", "entrypoint": "bin/codex",
                         "resourcesDir": "codex-resources", "pathDir": "codex-path"},
            "selected Codex manifest does not match the supported assembled contract")
    declared = runtime / manifest["entrypoint"]
    native = declared.resolve(strict=True)
    require(native == declared and native.is_file() and os.access(native, os.X_OK),
            "declared native Codex entrypoint is missing, linked or not executable")
    return native


def isolated_environment(root, package):
    # Allowlist inheritance: no production session, tmux, agent, proxy or API-key environment.
    environment = {key: os.environ[key] for key in ("PATH", "HOME", "USER", "LOGNAME", "LANG",
                    "SSL_CERT_FILE", "NIX_SSL_CERT_FILE") if key in os.environ}
    environment.update(CODEX_HOME=str(root / "codex"), CODEX_SQLITE_HOME=str(root / "codex"),
        DEV_WORKSPACE_CODEX_HOME=str(root / "codex"), XDG_CONFIG_HOME=str(root / "xdg-config"),
        XDG_CACHE_HOME=str(root / "xdg-cache"), XDG_STATE_HOME=str(root / "xdg-state"),
        XDG_RUNTIME_DIR=str(root / "r"), DEV_WORKSPACES_STATE=str(root / "state"),
        DEV_WORKSPACES_CONFIG=str(root / "registry.json"), DEV_WORKSPACES_PROFILE=str(root / "profile"),
        DEV_WORKSPACES_RUNTIME_DIR=str(root / "r"), DEV_WORKSPACES_SKILLS_DIR=str(root / "skills"),
        DEV_WORKSPACES_SYSTEM_CODEX=str(package / "libexec/codex/bin/codex"),
        DEV_WORKSPACES_ROUTER_SOCKET=str(root / "r/router.sock"), DEV_WORKSPACES_NAMESPACE="dev-workspaces",
        SHELL="/bin/sh", TERM="xterm-256color", RUST_LOG="warn")
    return environment


def finish_creation_verification(config, environment, preset, processes, result, args):
    root, package, workspace = (Path(config[key]) for key in ("root", "package", "workspace"))
    (root / "r/bench/authority").mkdir(mode=0o700, exist_ok=True)
    # Seed the isolated server without reading the operator's ~/.tmux.conf.
    tmux = shutil.which("tmux")
    run([tmux, "-f", "/dev/null", "-S", str(root / "r/bench/tmux.sock"), "new-session",
         "-d", "-s", "__workspace_portal_keeper", "-x", "160", "-y", "50", "/bin/sh"],
        environment, root, "tmux-start")
    tmux_pid = int(run([tmux, "-S", str(root / "r/bench/tmux.sock"), "display-message", "-p", "#{pid}"],
                      environment, root, "tmux-pid").decode().strip())
    processes.append({"label": "tmux", "pid": tmux_pid, "startedAt": stamp(),
                      "socket": str(root / "r/bench/tmux.sock")})
    save(root / "processes.json", processes)
    portal_args = [str(package / "bin/workspace-portal"), "serve", "--workspace", str(workspace),
        "--base-url", "https://creation.invalid", "--unix-socket", config["portalSocket"],
        "--dev-session", str(root / "bin/dev-session"), "--authority-dir", str(root / "r/bench/authority"),
        "--user-state-root", str(root / "state"), "--package-root", str(package), "--workspace-name", "bench",
        "--registration-marker", str(root / "r/bench/registration.json"),
        "--host-profile", str(root / "profile"), "--transition-lock", str(root / "state/transition.lock"),
        "--codex-socket", str(root / "r/bench/app-server.sock"), "--codex-version", "0.160.0",
        "--tmux", tmux]
    portal = spawn(portal_args, environment, root, "portal", processes)
    wait_socket(Path(config["portalSocket"]), portal, "portal")
    require(http(config, "GET", "/healthz")["ok"], "portal health failed")
    result["warmup"] = create(config, preset, "creation-warmup", args.model_timeout)
    return finish_creation_samples(config, preset, result, args)


def finish_creation_samples(config, preset, result, args):
    root = Path(config["root"])
    for index in range(1, 6):
        result["results"].append(create(config, preset, f"creation-sample-{index}", args.model_timeout))
        save(root / "result.json", result)
    values = [entry["acceptanceToReadySeconds"] for entry in result["results"]]
    result["timing"] = {"allSeconds": values, "medianSeconds": statistics.median(values), "maxSeconds": max(values),
                        "passed": statistics.median(values) < 10 and max(values) < 15}
    save(root / "result.json", result)
    if not args.skip_faults:
        result["faults"] = [create(config, preset, "creation-root-loss", args.model_timeout, "root-response"),
                            create(config, preset, "creation-member-loss", args.model_timeout, "member-progress")]
    representative = args.history_count >= 3379 and args.history_padding_bytes >= 16384
    result["state"] = "passed" if result["timing"]["passed"] and representative and not args.skip_faults else "incomplete"
    result["finishedAt"] = stamp()
    result["retained"] = "All sessions, private runtime services, tmux, history and evidence remain; no cleanup performed."
    save(root / "result.json", result)
    print(f"Median {statistics.median(values):.3f}s; maximum {max(values):.3f}s; result {result['state']}", flush=True)
    return 0 if result["state"] == "passed" else 2


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate", required=True, type=Path, help="built consuming workspace package in /nix/store")
    parser.add_argument("--auth-json", required=True, type=Path, help="explicit credential source; private copy only, never logged")
    parser.add_argument("--evidence-root", type=Path, help="new short absolute path outside Git; default private /tmp/pcp-*")
    parser.add_argument("--resume-seeded", action="store_true",
                        help="single-use continuation of /tmp/pcp-oct02-a before registration; reuse its auth file")
    parser.add_argument("--team-id", default="delegated", help="installed Full team ID; no model overrides")
    parser.add_argument("--history-count", type=int, default=3379)
    parser.add_argument("--history-padding-bytes", type=int, default=16384)
    parser.add_argument("--history-timeout", type=int, default=3600)
    parser.add_argument("--model-timeout", type=int, default=180)
    parser.add_argument("--skip-faults", action="store_true", help="timing-only run; never reports full verification passed")
    args = parser.parse_args()
    os.umask(0o077)
    for command in ("git", "ruby", "tmux"):
        require(shutil.which(command), f"required Nix-environment tool missing: {command}")
    require(args.candidate.is_dir(), "candidate package is absent; restore the exact selected package before execution")
    package = args.candidate.resolve(strict=True)
    require(package.parent == Path("/nix/store"), "candidate must be a canonical built Nix package")
    auth = args.auth_json.resolve(strict=True)
    require(auth.is_file() and auth.stat().st_uid == os.geteuid() and not auth.stat().st_mode & 0o077,
            "auth source must be an owned private regular file")
    require(0 <= args.history_count <= 10000 and 0 <= args.history_padding_bytes <= 65536, "invalid history dimensions")
    require(1 <= args.history_timeout <= 7200 and 1 <= args.model_timeout <= 600, "invalid timeout")
    for relative in ("bin/workspace-host", "bin/workspace-portal", "libexec/codex/bin/codex",
                     "libexec/workspace-portal/dev-session"):
        require(os.access(package / relative, os.X_OK), f"candidate lacks {relative}")
    if args.resume_seeded:
        require(args.evidence_root == SEEDED_ROOT, "--resume-seeded requires --evidence-root /tmp/pcp-oct02-a")
        root = args.evidence_root
    elif args.evidence_root:
        require(args.evidence_root.is_absolute() and not args.evidence_root.exists(), "evidence root must be new and absolute")
        root = args.evidence_root.parent.resolve(strict=True) / args.evidence_root.name
    else:
        root = Path(tempfile.mkdtemp(prefix="pcp-", dir="/tmp"))
    require(not root.is_relative_to(BINDING), "evidence must be outside the coordination Git tree")
    probe = subprocess.run(["git", "-C", str(root.parent), "rev-parse", "--is-inside-work-tree"],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    require(probe.returncode != 0, "evidence parent must be outside Git")
    if not args.resume_seeded:
        root.mkdir(mode=0o700, exist_ok=not args.evidence_root)
    require(len(os.fsencode(root / "r/bench/app-server.sock")) < 104, "evidence path too long for Unix sockets")
    print("Private verification evidence:", root, flush=True)
    previous = validate_seeded_resume(root, package, auth, args) if args.resume_seeded else None
    continuation_started = False
    result = {"state": "running", "candidate": str(package), "startedAt": stamp(), "results": []}
    if not args.resume_seeded:
        save(root / "result.json", result)
    try:
        workspace = root / "workspace"
        if not args.resume_seeded:
            for name in ("workspace", "state", "r", "xdg-config", "xdg-cache", "xdg-state", "codex", "bin", "events", "skills"):
                (root / name).mkdir(mode=0o700)
            for name in ("work", "worktrees", "archive", "repos"):
                (workspace / name).mkdir(mode=0o700)
            save(workspace / ".dev-workspace.json", WORKSPACE_FIXTURE)
            (workspace / "AGENTS.md").write_text("This is an isolated benchmark fixture. Do not use tools or change state for the initial READY request.\n")
            shutil.copyfile(auth, root / "codex/auth.json")
            os.chmod(root / "codex/auth.json", 0o600)
            (root / "codex/config.toml").write_text('cli_auth_credentials_store = "file"\n')
        environment = isolated_environment(root, package)
        codex = (package / "libexec/codex/bin/codex").resolve(strict=True)
        version = run([str(codex), "--version"], environment, root, "codex-version",
                      record_stderr=not args.resume_seeded).decode().strip()
        require(version == "codex-cli 0.160.0", "candidate does not select Codex 0.160.0")
        preset = json.loads(run([str(package / "bin/workspace-portal"), "team-preset", "--package-root",
                     str(package), "--team", args.team_id], environment, root, "team-preset",
                     record_stderr=not args.resume_seeded))
        require(preset["name"] == "Full team" and len(preset["members"]) >= 3, "selected preset is not installed Full team")
        config = {"root": str(root), "package": str(package), "workspace": str(workspace),
                  "state": str(root / "state"), "codexHome": str(root / "codex"), "codex": str(codex),
                  "portalSocket": str(root / "r/bench/portal.sock")}
        if args.resume_seeded:
            require(preset == read(root / "preset.json"), "installed Full team differs from the seeded preset")
            require_no_seeded_services(root, read(root / "seed-process.json")["pid"])
            preserve_seeded_failure(root)
            continuation_started = True
            result.update(history=previous["history"], resumedFrom="seeded-continuation/result.json",
                          codexVersion=version)
            save(workspace / ".dev-workspace.json", WORKSPACE_FIXTURE)
            save(root / "result.json", result)
        else:
            save(root / "preset.json", preset)
            result["history"] = seed_history(config, environment, preset, args.history_count,
                                              args.history_padding_bytes, args.history_timeout)
        # Register only while the private profile is absent; no activation path is entered.
        run([str(package / "bin/workspace-host"), "register", "bench", str(workspace)], environment, root, "register")
        (root / "profile").symlink_to(package)
        token = run(["ruby", "-r", str(package / "libexec/workspace-profile-identity.rb"), "-e",
                     "puts DevWorkspaceProfileIdentity.token(ARGV.fetch(0))", str(root / "profile")],
                    environment, root, "profile-token").decode().strip()
        require(re.fullmatch("[0-9a-f]{64}", token), "private profile token unavailable")
        script = Path(__file__).resolve()
        for kind, filename in (("dev-session", "dev-session"), ("portal", "workspace-portal")):
            command = [sys.executable, str(script), "--child", kind, str(root / "config.json")]
            target = root / "bin" / filename
            target.write_text("#!/bin/sh\nexec " + shlex.join(command) + ' "$@"\n')
            target.chmod(0o700)
        config["devSessionArgs"] = ["--require-runtime", "--workspace", str(workspace),
            "--host-profile", str(root / "profile"), "--expected-host-generation", str(package),
            "--expected-host-profile-token", token, "--transition-lock", str(root / "state/transition.lock"),
            "--authority-dir", str(root / "r/bench/authority"), "--tmux-socket", str(root / "r/bench/tmux.sock"),
            "--codex-command", str(codex), "--codex-socket", str(root / "r/bench/app-server.sock"),
            "--codex-version", "0.160.0", "--portal-command", str(root / "bin/workspace-portal"),
            "--portal-base-url", "https://creation.invalid"]
        save(root / "config.json", config)
        processes = []
        app_server = spawn([str(package / "bin/workspace-host"), "run-codex", "bench"], environment, root, "app-server", processes)
        wait_socket(root / "r/bench/app-server.sock", app_server, "App Server")
        actual = Path(f"/proc/{app_server.pid}/exe").resolve()
        require(actual == native_codex_entrypoint(codex), "running App Server executable is not the selected Codex")
        return finish_creation_verification(config, environment, preset, processes, result, args)
    except Exception as error:
        if args.resume_seeded and not continuation_started:
            if isinstance(error, Failure):
                raise
            raise Failure("seeded continuation refused before replacement; original evidence retained") from None
        # Never serialize an arbitrary exception that may embed child output.
        result.update(state="incomplete", finishedAt=stamp(),
                      error=str(error) if isinstance(error, Failure) else type(error).__name__)
        save(root / "result.json", result)
        print("Verification incomplete; inspect private result.json. Services and sessions retained.", flush=True)
        return 1


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--child":
        try:
            sys.exit(child_mode(sys.argv[2], sys.argv[3], sys.argv[4:]))
        except Exception:
            os.write(2, b"verification helper fixture failed; no diagnostic payload emitted\n")
            sys.exit(99)
    else:
        try:
            sys.exit(main())
        except Failure as error:
            print(str(error), file=sys.stderr)
            sys.exit(1)
