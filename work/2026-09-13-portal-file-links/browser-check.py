"""Exercise the packaged source viewer against an isolated workspace fixture."""
import argparse
import hashlib
import http.client
import http.server
import json
import os
from pathlib import Path
import socket
import subprocess
import tempfile
import threading
import time
from urllib.parse import quote, urlencode

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait


parser = argparse.ArgumentParser()
parser.add_argument("--portal-bin", required=True)
parser.add_argument("--tools", default="/tmp/portal-file-links-browser-tools/bin")
parser.add_argument("--output", required=True)
parser.add_argument("--legacy-editor")
args = parser.parse_args()
output = Path(args.output)
output.mkdir(parents=True, exist_ok=True)
results = []


def git(*command):
    return subprocess.check_output(["git", *map(str, command)], stderr=subprocess.PIPE, text=True).strip()


with tempfile.TemporaryDirectory(prefix="portal-file-links-") as temporary:
    root = Path(temporary)
    workspace = root / "workspace"
    bare = workspace / "repos" / "project.git"
    seed = root / "seed"
    worktree = workspace / "worktrees" / "example" / "project"
    tracking = workspace / "work" / "example"
    tracking.mkdir(parents=True)
    bare.parent.mkdir(parents=True)
    git("init", "--bare", "--initial-branch=master", bare)
    git("init", "--initial-branch=master", seed)
    git("-C", seed, "config", "user.name", "Fixture")
    git("-C", seed, "config", "user.email", "fixture@example.invalid")
    source_path = "src/example file.nix"
    (seed / "src").mkdir()
    source = "\n".join(f"# source line {i}" for i in range(1, 401)) + "\n"
    source = source.replace("# source line 10\n", "<script>window.sourceExecuted = true</script>\n")
    (seed / source_path).write_text(source)
    git("-C", seed, "add", ".")
    git("-C", seed, "commit", "-m", "source fixture")
    head = git("-C", seed, "rev-parse", "HEAD")
    git("--git-dir=" + str(bare), "fetch", seed, "HEAD:refs/heads/feature")
    git("--git-dir=" + str(bare), "update-ref", "refs/remotes/origin/master", head)
    git("--git-dir=" + str(bare), "worktree", "add", worktree, "feature")
    manifest = f"schema: 1\nslug: example\nrepositories:\n  - name: project\n    project: project\n    branch: feature\n    default_branch: master\n    initial_base_sha: {head}\n"
    (tracking / "portal.yml").write_text(manifest)
    (tracking / "state.md").write_text("---\nlifecycle: active\n---\n")
    (tracking / "plan.md").write_text(f"# Plan\n[Referenced file](<{worktree / source_path}:95>)\n")
    (root / "generation").mkdir()
    (root / "host-profile").symlink_to(root / "generation")
    socket_path = root / "portal.sock"
    portal_log = open(output / "portal.log", "w")
    process = subprocess.Popen([
        args.portal_bin, "serve", "--workspace", str(workspace),
        "--base-url", "https://workspace.example.test", "--unix-socket", str(socket_path),
        "--host-profile", str(root / "host-profile"), "--dev-session", "/bin/false",
        "--user-state-root", str(root / "user-state"), "--authority-dir", str(root / "authorities"),
        "--codex-socket", str(root / "absent-codex.sock"), "--gh", "/bin/false",
    ], stdout=portal_log, stderr=portal_log)

    class UnixConnection(http.client.HTTPConnection):
        def connect(self):
            self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            self.sock.connect(str(socket_path))

    class Proxy(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            if use_legacy[0] and self.path.split("?", 1)[0] == "/static/review-editor.js":
                body = Path(args.legacy_editor).read_bytes()
                self.send_response(200)
                self.send_header("Content-Type", "text/javascript")
                self.send_header("Cache-Control", "no-store")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return
            connection = UnixConnection("localhost", timeout=20)
            connection.request("GET", self.path)
            response = connection.getresponse()
            body = response.read()
            self.send_response(response.status)
            for key, value in response.getheaders():
                if key.lower() not in ("connection", "transfer-encoding", "content-length"):
                    self.send_header(key, value)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            connection.close()

        def log_message(self, *_):
            pass

    use_legacy = [False]
    proxy = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Proxy)
    threading.Thread(target=proxy.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{proxy.server_port}"
    options = Options()
    options.add_argument("-headless")
    options.binary_location = args.tools + "/firefox"
    options.set_capability("webSocketUrl", True)
    driver = None
    try:
        for _ in range(200):
            if socket_path.exists():
                break
            if process.poll() is not None:
                raise RuntimeError("Portal failed: " + (output / "portal.log").read_text())
            time.sleep(.1)
        driver = webdriver.Firefox(options=options, service=Service(executable_path=args.tools + "/geckodriver", log_output=str(output / "geckodriver.log")))
        wait = WebDriverWait(driver, 20)
        query = urlencode({"repository": hashlib.sha256(b"project").hexdigest()[:32], "path": source_path})
        viewer = base + "/files/example?" + query

        def selected(line):
            wait.until(lambda d: d.execute_script("return document.querySelector('.review-linked-line')?.textContent") == ("<script>window.sourceExecuted = true</script>" if line == 10 else f"# source line {line}"))
            return driver.execute_script("const l=document.querySelector('.review-linked-line').getBoundingClientRect(), s=document.querySelector('.cm-scroller').getBoundingClientRect(); return {lineTop:l.top,lineBottom:l.bottom,scrollTop:s.top,scrollBottom:s.bottom,documentWidth:document.documentElement.scrollWidth,width:innerWidth};")

        for label, width, height in [("desktop", 1440, 1000), ("narrow", 390, 844)]:
            driver.browsing_context.set_viewport(context=driver.current_window_handle, viewport={"width": width, "height": height})
            driver.get(base + quote(str(worktree / source_path), safe="/") + ":95")
            metrics = selected(95)
            assert "/files/example?" in driver.current_url and driver.current_url.endswith("#L95")
            assert metrics["scrollTop"] <= metrics["lineTop"] <= metrics["scrollBottom"]
            assert metrics["documentWidth"] <= metrics["width"] + 1
            assert "Current worktree" in driver.find_element(By.ID, "source-file-version").text
            wait.until(lambda d: not d.find_elements(By.CSS_SELECTOR, ".review-syntax-status"))
            driver.save_screenshot(str(output / f"{label}.png"))
            results.append({"check": label, "metrics": metrics})

        driver.get(viewer + "#L10")
        selected(10)
        assert not driver.execute_script("return !!window.sourceExecuted")
        driver.find_element(By.CSS_SELECTOR, '.cm-gutterElement a[data-line="11"]').click()
        selected(11)
        assert driver.current_url.endswith("#L11")
        driver.refresh()
        selected(11)
        driver.back()
        selected(10)
        driver.get(viewer)
        wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, ".cm-editor")) == 1)
        assert not driver.find_elements(By.CSS_SELECTOR, ".review-linked-line")
        driver.get(viewer + "#L999")
        wait.until(lambda d: "Line 999 is not present" in d.find_element(By.ID, "source-file-notice").text)
        driver.get(viewer + "#L0")
        wait.until(lambda d: "invalid" in d.find_element(By.ID, "source-file-notice").text)
        driver.get(viewer + "#L95")
        selected(95)
        driver.execute_script("location.hash='L10'; setTimeout(() => { location.hash='L999'; }, 0);")
        wait.until(lambda d: "Line 999 is not present" in d.find_element(By.ID, "source-file-notice").text)
        time.sleep(.1)
        assert "Line 999 is not present" in driver.find_element(By.ID, "source-file-notice").text
        driver.get(viewer + "#L95")
        selected(95)
        driver.execute_script("Object.defineProperty(navigator, 'clipboard', {value: {writeText: async text => {window.copiedLink = text;}}});")
        driver.find_element(By.ID, "source-file-copy").click()
        wait.until(lambda d: d.find_element(By.ID, "source-file-copy").text == "Copied")
        assert driver.execute_script("return window.copiedLink") == driver.current_url
        original_tab = driver.current_window_handle
        driver.switch_to.new_window("tab")
        driver.get(viewer + "#L95")
        selected(95)
        driver.close()
        driver.switch_to.window(original_tab)
        results.append({"check": "line click, reload, back, new tab, invalid/missing line, HTML as source", "passed": True})

        driver.get(base + "/files/example?artifact=plan.md#L2")
        wait.until(lambda d: d.execute_script("return document.querySelector('.review-linked-line')?.textContent.startsWith('[Referenced file]')"))
        assert "Current session artifact" in driver.find_element(By.ID, "source-file-version").text
        driver.get(base + "/api/sessions/example/artifact-preview?path=plan.md")
        assert "/files/example?" in driver.find_element(By.TAG_NAME, "body").text

        git("--git-dir=" + str(bare), "worktree", "remove", worktree)
        (tracking / "state.md").write_text("---\nlifecycle: complete\n---\n")
        (tracking / "portal.yml").write_text(manifest + f"    final_head_sha: {head}\nfinalized_at: '2026-09-13T12:00:00Z'\n")
        (workspace / "archive").mkdir()
        tracking.rename(workspace / "archive" / "example")
        driver.get(viewer + "#L95")
        selected(95)
        assert head in driver.find_element(By.ID, "source-file-version").text
        driver.get(base + quote(str(tracking / "plan.md"), safe="/") + ":2")
        wait.until(lambda d: "Archived session artifact" in d.find_element(By.ID, "source-file-version").text)
        results.append({"check": "artifact source and exact archive fallback after worktree removal", "passed": True})
        if args.legacy_editor:
            use_legacy[0] = True
            driver.get(viewer + "#L95")
            selected(95)
            results.append({"check": "retained new source page with pre-feature editor after rollback", "passed": True})
        (output / "results.json").write_text(json.dumps(results, indent=2) + "\n")
        print(json.dumps(results, indent=2))
    finally:
        if driver:
            driver.quit()
        proxy.shutdown()
        process.terminate()
        process.wait(timeout=30)
        portal_log.close()
