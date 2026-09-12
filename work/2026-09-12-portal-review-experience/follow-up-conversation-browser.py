#!/usr/bin/env python3
"""Post-review packaged portal acceptance using an isolated Codex RPC fixture.

Run with Nix-provided Firefox, geckodriver, Selenium and openssl. The actual
candidate workspace-portal binary, embedded assets, handlers, submission ledger,
authority checks and activity recorder are used. Only Codex RPC data and tmux
identity are controlled. No real conversation, workspace or profile is touched.
"""
import argparse
import base64
import hashlib
import http.client
import http.server
import json
import os
from pathlib import Path
import shutil
import socket
import socketserver
import ssl
import struct
import subprocess
import tempfile
import threading
import time
import traceback
import urllib.request

SLUG = "conversation-browser-fixture"
THREAD = "fixture-thread"
TURN = "fixture-turn"
AGENT_TEXT = "Fixture **message** for copying.\n\nKeep the original Markdown."
MESSAGE_ONE = "Please keep this steer visible until processing."
MESSAGE_TWO = "A second independent steer."


def wait_for(check, label, timeout=25):
    deadline = time.monotonic() + timeout
    last = None
    while time.monotonic() < deadline:
        try:
            result = check()
            if result:
                return result
        except Exception as error:
            last = error
        time.sleep(0.1)
    raise AssertionError(f"Timed out: {label}; last error: {last}")


class Fixture:
    def __init__(self, root):
        self.root = root
        self.cwd = str(root / "workspace" / "work" / SLUG)
        self.lock = threading.RLock()
        self.peers = set()
        self.calls = []
        self.steers = []
        self.published = []
        self.started = int(time.time()) - 20
        self.completed = None
        self.block_ack = False
        self.failed_ack = 0
        self.http_calls = []

    def thread(self):
        return {
            "id": THREAD, "cwd": self.cwd, "path": str(self.root / "rollout.jsonl"),
            "model": "fixture-model", "reasoningEffort": "medium", "source": "appServer",
            "status": {"type": "idle" if self.completed else "active", "activeFlags": []},
            "ephemeral": False, "historyMode": "paginated", "turns": [],
            "preview": "Browser acceptance fixture", "createdAt": self.started - 20,
            "updatedAt": int(time.time()),
        }

    def turn(self):
        items = [{"id": "fixture-agent", "type": "agentMessage", "text": AGENT_TEXT}]
        items.extend(self.published)
        return {
            "id": TURN, "status": "completed" if self.completed else "inProgress",
            "startedAt": self.started, "completedAt": self.completed,
            "items": items, "itemsView": "full", "error": None,
        }

    def rpc(self, method, params):
        with self.lock:
            self.calls.append({"method": method, "at": time.time()})
            if method == "initialize":
                return {"userAgent": "isolated-browser-fixture"}
            if method == "thread/read":
                assert params["threadId"] == THREAD
                return {"thread": self.thread()}
            if method == "thread/resume":
                assert params["threadId"] == THREAD
                return {"thread": self.thread(), "model": "fixture-model", "reasoningEffort": "medium"}
            if method == "thread/turns/list":
                assert params["threadId"] == THREAD
                return {"data": [self.turn()], "nextCursor": None}
            if method == "thread/items/list":
                return {"data": [{"turnId": TURN, "item": item} for item in reversed(self.turn()["items"])], "nextCursor": None}
            if method == "thread/queue/list":
                return {"data": [], "nextCursor": None}
            if method in ("thread/list", "thread/loaded/list"):
                return {"data": [THREAD] if method == "thread/loaded/list" else [self.thread()], "nextCursor": None}
            if method == "model/list":
                return {"data": [{"id": "fixture-model", "model": "fixture-model", "displayName": "Fixture model", "description": "Isolated browser fixture", "isDefault": True, "supportedReasoningEfforts": [{"reasoningEffort": "medium", "description": "Medium"}], "defaultReasoningEffort": "medium"}], "nextCursor": None}
            if method == "collaborationMode/list":
                return {"data": [{"name": "Default", "mode": "default"}, {"name": "Plan", "mode": "plan"}]}
            if method == "account/rateLimits/read":
                return {"rateLimits": None, "rateLimitsByLimitId": {}}
            if method == "turn/steer":
                assert params["threadId"] == THREAD and params["expectedTurnId"] == TURN
                assert not self.completed
                self.steers.append(dict(params))
                return {"turnId": TURN}
            raise AssertionError(f"Unexpected Codex RPC {method}")

    def notify(self, method, params):
        with self.lock:
            peers = list(self.peers)
        for peer in peers:
            try:
                peer.send_json({"method": method, "params": params})
            except OSError:
                pass

    def publish(self, messages):
        with self.lock:
            self.published = [{"id": f"fixture-user-{index}", "type": "userMessage", "clientId": identity,
                               "content": [{"type": "text", "text": text, "text_elements": []}]}
                              for index, (identity, text) in enumerate(messages)]
        self.notify("thread/status/changed", {"threadId": THREAD, "status": self.thread()["status"]})

    def complete(self):
        with self.lock:
            self.completed = int(time.time())
        self.notify("turn/completed", {"threadId": THREAD, "turn": self.turn()})
        self.notify("thread/status/changed", {"threadId": THREAD, "status": self.thread()["status"]})


class RPCHandler(socketserver.StreamRequestHandler):
    def handle(self):
        self.write_lock = threading.Lock()
        first = self.rfile.readline()
        if not first.startswith(b"GET "):
            return
        headers = {}
        while True:
            line = self.rfile.readline()
            if line in (b"\r\n", b"\n", b""):
                break
            key, value = line.decode().split(":", 1)
            headers[key.lower()] = value.strip()
        accept = base64.b64encode(hashlib.sha1((headers["sec-websocket-key"] + "258EAFA5-E914-47DA-95CA-C5AB0DC85B11").encode()).digest()).decode()
        self.wfile.write(f"HTTP/1.1 101 Switching Protocols\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Accept: {accept}\r\n\r\n".encode())
        self.wfile.flush()
        fixture = self.server.fixture
        with fixture.lock:
            fixture.peers.add(self)
        fragments = b""
        try:
            while True:
                header = self.rfile.read(2)
                if len(header) != 2:
                    return
                final, opcode = bool(header[0] & 0x80), header[0] & 0x0F
                masked, length = bool(header[1] & 0x80), header[1] & 0x7F
                if length == 126:
                    length = struct.unpack("!H", self.rfile.read(2))[0]
                elif length == 127:
                    length = struct.unpack("!Q", self.rfile.read(8))[0]
                assert length < 1024 * 1024
                mask = self.rfile.read(4) if masked else b""
                data = self.rfile.read(length)
                if len(data) != length:
                    return
                if masked:
                    data = bytes(value ^ mask[index % 4] for index, value in enumerate(data))
                if opcode == 8:
                    return
                if opcode == 9:
                    self.send_frame(10, data)
                    continue
                if opcode not in (0, 1):
                    continue
                fragments += data
                if not final:
                    continue
                request = json.loads(fragments)
                fragments = b""
                if "id" not in request:
                    continue
                try:
                    result = fixture.rpc(request["method"], request.get("params") or {})
                    self.send_json({"id": request["id"], "result": result})
                except Exception as error:
                    self.send_json({"id": request["id"], "error": {"code": -32603, "message": str(error)}})
        finally:
            with fixture.lock:
                fixture.peers.discard(self)

    def send_frame(self, opcode, data):
        header = bytes([0x80 | opcode])
        length = len(data)
        header += bytes([length]) if length < 126 else b"\x7e" + struct.pack("!H", length) if length < 65536 else b"\x7f" + struct.pack("!Q", length)
        with self.write_lock:
            self.wfile.write(header + data)
            self.wfile.flush()

    def send_json(self, value):
        self.send_frame(1, json.dumps(value).encode())


class RPCServer(socketserver.ThreadingUnixStreamServer):
    daemon_threads = True


class UnixHTTPConnection(http.client.HTTPConnection):
    def __init__(self, path):
        super().__init__("localhost", timeout=40)
        self.path = path

    def connect(self):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.sock.settimeout(40)
        self.sock.connect(self.path)


class Proxy(http.server.BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.0"

    def do_GET(self):
        self.forward()

    def do_POST(self):
        self.forward()

    def do_DELETE(self):
        self.forward()

    def forward(self):
        fixture = self.server.fixture
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length) if length else None
        with fixture.lock:
            fixture.http_calls.append({"method": self.command, "path": self.path, "at": time.time()})
            block = fixture.block_ack and self.path.endswith("/message-ack")
            if block:
                fixture.failed_ack += 1
        if block:
            data = b'{"error":"Controlled acknowledgement connection failure"}'
            self.send_response(503)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
            return
        connection = UnixHTTPConnection(self.server.portal_socket)
        try:
            headers = {key: value for key, value in self.headers.items() if key.lower() not in ("connection", "accept-encoding")}
            connection.request(self.command, self.path, body=body, headers=headers)
            response = connection.getresponse()
            self.send_response(response.status)
            for key, value in response.getheaders():
                if key.lower() not in ("connection", "transfer-encoding"):
                    self.send_header(key, value)
            self.end_headers()
            while data := response.read1(16384):
                self.wfile.write(data)
                self.wfile.flush()
        except (BrokenPipeError, ConnectionResetError, TimeoutError):
            pass
        finally:
            connection.close()

    def log_message(self, _format, *_args):
        pass


def write(path, text, mode=0o600):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    path.chmod(mode)


def run(args):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.firefox.options import Options
    from selenium.webdriver.firefox.service import Service

    package = Path(args.package).resolve(strict=True)
    binary = package / "bin" / "workspace-portal"
    assert binary.is_file(), binary
    output = Path(args.output).resolve()
    output.mkdir(parents=True, exist_ok=True)
    report = {"package": str(package), "startedAt": time.time(), "checks": [], "passed": False}
    driver = None
    process = None
    rpc = None
    proxy = None
    with tempfile.TemporaryDirectory(prefix="portal-conversation-browser-") as temporary:
        root = Path(temporary)
        fixture = Fixture(root)
        workspace = root / "workspace"
        work = workspace / "work" / SLUG
        work.mkdir(parents=True)
        (workspace / "worktrees").mkdir()
        (workspace / "repos").mkdir()
        authority = root / "authority"
        authority.mkdir(mode=0o700)
        (root / "host-profile").symlink_to(package)
        socket_path = root / "codex.sock"
        write(work / "plan.md", "# Isolated browser acceptance\n")
        write(work / "state.md", "---\nlifecycle: active\n---\n\nBrowser acceptance fixture.\n")
        write(work / "portal.yml", f"schema: 1\nslug: {SLUG}\ncodex:\n  thread_id: {THREAD}\n  socket_path: {socket_path}\n  client_version: 0.154.0\ncreation:\n  state: ready\n  initial_goal_sent: true\n")
        write(root / "rollout.jsonl", json.dumps({"type": "turn_context", "payload": {"collaboration_mode": {"mode": "default", "settings": {"model": "fixture-model", "reasoning_effort": "medium"}}}}) + "\n")
        tmux_socket = str(root / "tmux.sock")
        identity = "a" * 64
        write(authority / f"{SLUG}.json", json.dumps({"schema": 1, "state": "ready", "slug": SLUG, "workspace": str(workspace), "tmux_socket": tmux_socket, "tmux_session_id": "$1", "tmux_identity": identity, "codex_thread_id": THREAD, "codex_socket_path": str(socket_path), "codex_client_version": "0.154.0"}))
        tuple_text = "\t".join(["$1", SLUG, "1", SLUG, str(workspace), SLUG, tmux_socket, THREAD, str(socket_path), "0.154.0", "%1", identity])
        write(root / "tmux", "#!/bin/sh\nprintf '%s\\n' '" + tuple_text + "'\n", 0o700)
        write(root / "dev-session", "#!/bin/sh\necho 'No lifecycle actions are allowed in this fixture' >&2\nexit 69\n", 0o700)
        write(root / "gh", "#!/bin/sh\nprintf '[]\\n'\n", 0o700)
        subprocess.run(["openssl", "req", "-x509", "-newkey", "rsa:2048", "-nodes", "-keyout", str(root / "key.pem"), "-out", str(root / "cert.pem"), "-days", "1", "-subj", "/CN=localhost", "-addext", "subjectAltName=DNS:localhost,IP:127.0.0.1"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        rpc = RPCServer(str(socket_path), RPCHandler)
        rpc.fixture = fixture
        threading.Thread(target=rpc.serve_forever, daemon=True).start()
        proxy = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Proxy)
        proxy.daemon_threads = True
        proxy.fixture = fixture
        proxy.portal_socket = str(root / "portal.sock")
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(str(root / "cert.pem"), str(root / "key.pem"))
        proxy.socket = context.wrap_socket(proxy.socket, server_side=True)
        base = f"https://127.0.0.1:{proxy.server_port}"
        threading.Thread(target=proxy.serve_forever, daemon=True).start()
        log = (output / "portal.log").open("w")
        try:
            command = [str(binary), "serve", "--unix-socket", proxy.portal_socket, "--workspace", str(workspace), "--base-url", base, "--dev-session", str(root / "dev-session"), "--authority-dir", str(authority), "--host-profile", str(root / "host-profile"), "--user-state-root", str(root / "user-state"), "--codex-socket", str(socket_path), "--codex-version", "0.154.0", "--tmux", str(root / "tmux"), "--gh", str(root / "gh")]
            process = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT, env={**os.environ, "DEV_SESSION_SLUG": SLUG, "DEV_SESSION_WORKSPACE": str(workspace)})
            wait_for(lambda: Path(proxy.portal_socket).exists() or process.poll() is not None, "portal listener")
            assert process.poll() is None, (output / "portal.log").read_text()
            options = Options()
            options.add_argument("-headless")
            options.accept_insecure_certs = True
            options.set_preference("dom.events.testing.asyncClipboard", True)
            if args.firefox:
                options.binary_location = args.firefox
            service = Service(executable_path=args.geckodriver or shutil.which("geckodriver"), log_output=str(output / "geckodriver.log"))
            driver = webdriver.Firefox(options=options, service=service)
            driver.set_window_size(1440, 1000)
            driver.set_script_timeout(20)
            page = base + "/" + SLUG + "/"
            driver.get(page)
            wait_for(lambda: driver.find_element(By.CSS_SELECTOR, ".message.agent .codex-entry-copy"), "real transcript render")
            assert driver.find_element(By.TAG_NAME, "body").get_attribute("data-interactive") == "true"
            assert driver.execute_script("return window.isSecureContext")
            copy = driver.find_element(By.CSS_SELECTOR, ".message.agent .codex-entry-copy")
            assert copy.get_attribute("aria-label") == "Copy message"
            assert copy.find_element(By.TAG_NAME, "svg").get_attribute("aria-hidden") == "true"
            assert copy.text == "", copy.text
            copy.click()
            wait_for(lambda: copy.get_attribute("data-copy-state") == "copied", "copy success icon")
            actual_clipboard = driver.execute_async_script("const done = arguments[0]; navigator.clipboard.readText().then(done, error => done({error:String(error)}));")
            assert actual_clipboard == AGENT_TEXT, actual_clipboard
            report["checks"].append("Native clipboard contains original Markdown; SVG copy/check icons and accessible label")
            driver.execute_script("window.fixtureOriginalWriteText = navigator.clipboard.writeText; navigator.clipboard.writeText = () => Promise.reject(new Error('Controlled clipboard failure'));")
            copy.click()
            wait_for(lambda: copy.get_attribute("data-copy-state") == "error", "copy failure icon")
            assert copy.get_attribute("aria-label") == "Copy failed. Try again."
            driver.execute_script("navigator.clipboard.writeText = window.fixtureOriginalWriteText; delete window.fixtureOriginalWriteText;")
            wait_for(lambda: copy.get_attribute("data-copy-state") == "idle", "copy feedback reset")
            report["checks"].append("Clipboard denial has accessible error feedback and recovers")

            def send(text):
                textarea = driver.find_element(By.CSS_SELECTOR, "#message-form textarea[name=message]")
                wait_for(lambda: textarea.is_enabled(), "enabled composer")
                textarea.send_keys(text)
                button = driver.find_element(By.ID, "message-send")
                assert button.text == "Steer now", button.text
                button.click()
                wait_for(lambda: any(text in row.text and "Sent to Codex" in row.text for row in driver.find_elements(By.CSS_SELECTOR, ".message-receipt")), "accepted steer visible")

            def stored():
                return driver.execute_script("const prefix=arguments[0]; return Object.keys(sessionStorage).filter(key=>key.startsWith(prefix)).map(key=>({key,...JSON.parse(sessionStorage.getItem(key))}));", f"workspace-portal.send-attempt.{SLUG}.{THREAD}.")

            send(MESSAGE_ONE)
            send(MESSAGE_TWO)
            records = stored()
            assert len(records) == 2 and all(item["state"] == "accepted" for item in records), records
            ids = {item["message"]: item["key"].split(".")[-1] for item in records}
            assert len(fixture.steers) == 2
            assert all(item["clientUserMessageId"] in ids.values() for item in fixture.steers)
            assert driver.execute_script("return document.querySelector('#message-receipts').compareDocumentPosition(document.querySelector('#message-form')) & Node.DOCUMENT_POSITION_FOLLOWING")
            driver.save_screenshot(str(output / "accepted-steers.png"))
            driver.refresh()
            wait_for(lambda: len(driver.find_elements(By.CSS_SELECTOR, '.message-receipt[data-receipt-state="accepted"]')) == 2, "accepted steers survive reload")
            assert len(fixture.steers) == 2, "Reload resubmitted a steer"
            report["checks"].append("Two actual accepted turn/steer requests remain above composer across same-tab reload without resend")

            fixture.publish([("different-client-id", MESSAGE_ONE)])
            driver.refresh()
            wait_for(lambda: MESSAGE_ONE in driver.find_element(By.ID, "transcript").text, "same-text different-ID transcript")
            assert len(driver.find_elements(By.CSS_SELECTOR, ".message-receipt")) == 2
            fixture.publish([(ids[MESSAGE_ONE], "Different canonical text")])
            driver.refresh()
            wait_for(lambda: "Different canonical text" in driver.find_element(By.ID, "transcript").text, "same-ID wrong-digest transcript")
            assert len(driver.find_elements(By.CSS_SELECTOR, ".message-receipt")) == 2
            assert all(item["state"] == "accepted" for item in stored())
            report["checks"].append("Same text with different ID and same ID with different digest do not hide accepted steers")

            fixture.block_ack = True
            fixture.publish([(ids[MESSAGE_ONE], MESSAGE_ONE)])
            driver.refresh()
            wait_for(lambda: len(driver.find_elements(By.CSS_SELECTOR, ".message-receipt")) == 1, "only exact observed steer hides")
            assert MESSAGE_TWO in driver.find_element(By.CSS_SELECTOR, ".message-receipt").text
            wait_for(lambda: fixture.failed_ack > 0, "controlled acknowledgement failure")
            first = next(item for item in stored() if item["message"] == MESSAGE_ONE)
            assert first["state"] == "observed" and first["transcriptDigest"] == hashlib.sha256(MESSAGE_ONE.encode()).hexdigest(), first
            driver.refresh()
            wait_for(lambda: len(driver.find_elements(By.CSS_SELECTOR, ".message-receipt")) == 1, "observed receipt stays hidden after reload despite failed acknowledgement")
            driver.save_screenshot(str(output / "observed-with-ack-failure.png"))
            fixture.publish([(ids[MESSAGE_ONE], MESSAGE_ONE), (ids[MESSAGE_TWO], MESSAGE_TWO)])
            driver.refresh()
            wait_for(lambda: len(stored()) == 2 and all(item["state"] == "observed" for item in stored()), "both receipts persist observed state")
            assert not driver.find_element(By.ID, "message-receipts").is_displayed()
            report["checks"].append("Canonical ID+digest match hides only corresponding steer; failed acknowledgements and reload do not resurrect cards")
            fixture.block_ack = False
            wait_for(lambda: stored() == [], "real handler acknowledgement retry clears durable records")
            assert len(fixture.steers) == 2, "Acknowledgement retry resubmitted a steer"
            report["checks"].append("Successful real-handler acknowledgement retry clears both records without resubmission")

            fixture.complete()
            wait_for(lambda: driver.find_element(By.ID, "codex-work-label").text == "Waiting for instructions", "new waiting label")
            elapsed = driver.find_element(By.ID, "codex-work-elapsed").text
            assert "waiting" in elapsed and elapsed.strip(), elapsed
            assert "Waiting for you" not in driver.find_element(By.TAG_NAME, "body").text
            driver.save_screenshot(str(output / "waiting-for-instructions.png"))
            report["checks"].append("Completed turn shows Waiting for instructions with separate elapsed wait timer")
            report["passed"] = True
        except Exception:
            report["error"] = traceback.format_exc()
            if driver is not None:
                try:
                    driver.save_screenshot(str(output / "failure.png"))
                    (output / "failure.html").write_text(driver.page_source)
                    report["visibleText"] = driver.find_element(By.TAG_NAME, "body").text
                except Exception:
                    pass
            raise
        finally:
            report["completedAt"] = time.time()
            report["rpcCalls"] = fixture.calls
            report["httpCalls"] = fixture.http_calls
            report["steerCount"] = len(fixture.steers)
            report["failedAcknowledgements"] = fixture.failed_ack
            (output / "result.json").write_text(json.dumps(report, indent=2) + "\n")
            if driver is not None:
                driver.quit()
            if process is not None:
                process.terminate()
                try:
                    process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    process.kill()
                    process.wait(timeout=5)
            log.close()
            proxy.shutdown()
            proxy.server_close()
            rpc.shutdown()
            rpc.server_close()
    print(json.dumps({"passed": report["passed"], "checks": report["checks"], "output": str(output)}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package", required=True, help="Exact built candidate package store path")
    parser.add_argument("--output", required=True, help="Directory for JSON evidence, screenshots and logs")
    parser.add_argument("--firefox", help="Optional Firefox executable path")
    parser.add_argument("--geckodriver", help="Optional geckodriver executable path")
    run(parser.parse_args())
