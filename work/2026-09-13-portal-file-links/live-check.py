"""Read-only HTTPS and browser verification of the deployed example links."""
import http.server
import json
from pathlib import Path
import threading
from urllib.parse import quote, urlsplit

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait

base = "https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz"
ca = "/var/lib/dev-workspaces/public/ca.pem"
auth = ("aither", Path("/var/lib/dev-workspaces/password/password").read_text().strip())
tools = "/tmp/portal-file-links-browser-tools/bin"
root = Path("/home/aither/workspace/ai/vpsfree.cz")
output = root / "work/2026-09-13-portal-file-links/live-browser"
output.mkdir(exist_ok=True)
slug = "2026-08-18-vpsadmin-password-reset"
cases = [("proxy", "cluster/cz.vpsfree/containers/prg/proxy/module.nix", 10),
         ("frontend", "cluster/cz.vpsfree/vpsadmin/common/frontend.nix", 95)]
results = []


def get(path, authenticated=True):
    return requests.get(base + path, auth=auth if authenticated else None, verify=ca,
                        timeout=30, allow_redirects=False, headers={"Accept-Encoding": "identity"})


assert get("/healthz", False).status_code == 401
assert get("/files/" + slug + "?artifact=plan.md", False).status_code == 401
assert get("/healthz").status_code == 200


class Proxy(http.server.BaseHTTPRequestHandler):
    # Browser reads go through the real HTTPS portal. Credentials remain only in
    # this process and never enter a URL, browser profile, screenshot or log.
    def do_GET(self):
        if not self.path.startswith("/"):
            self.send_error(400)
            return
        response = get(self.path)
        self.send_response(response.status_code)
        for key, value in response.headers.items():
            if key.lower() not in ("connection", "transfer-encoding", "content-length", "content-encoding"):
                self.send_header(key, value)
        self.send_header("Content-Length", str(len(response.content)))
        self.end_headers()
        self.wfile.write(response.content)

    def log_message(self, *_):
        pass


proxy = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Proxy)
threading.Thread(target=proxy.serve_forever, daemon=True).start()
browser_base = f"http://127.0.0.1:{proxy.server_port}"
options = Options()
options.add_argument("-headless")
options.binary_location = tools + "/firefox"
options.set_capability("webSocketUrl", True)
driver = webdriver.Firefox(options=options, service=Service(executable_path=tools + "/geckodriver", log_output=str(output / "geckodriver.log")))
try:
    driver.browsing_context.set_viewport(context=driver.current_window_handle, viewport={"width": 1440, "height": 1000})
    wait = WebDriverWait(driver, 30)
    for label, relative, line in cases:
        path = root / "worktrees" / slug / "vpsfree-cz-configuration" / relative
        original = quote(str(path), safe="/") + f":{line}"
        redirect = get(original)
        assert redirect.status_code == 302, redirect.status_code
        target = redirect.headers["Location"]
        assert target.endswith(f"#L{line}")
        query = urlsplit(target).query
        content = get(f"/api/sessions/{slug}/file?{query}")
        content.raise_for_status()
        source = content.json()
        expected = path.read_bytes().decode("utf-8")
        assert source["content"]["text"] == expected
        assert source["source"] == "worktree"
        driver.get(browser_base + original)
        wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, ".review-linked-line")) == 1)
        assert driver.find_element(By.CSS_SELECTOR, ".review-linked-line").get_property("textContent") == expected.splitlines()[line-1]
        assert driver.find_element(By.CSS_SELECTOR, '[aria-current="line"]').get_attribute("data-line") == str(line)
        wait.until(lambda d: not d.find_elements(By.CSS_SELECTOR, ".review-syntax-status"))
        driver.save_screenshot(str(output / f"{label}.png"))
        results.append({"example": label, "status": content.status_code, "url": base + target,
                        "line": line, "matches_current_file": True, "highlighted": True})
    assert get(f"/api/sessions/{slug}/file?artifact=../../.git/config").status_code == 400
    results.append({"authentication": "unauthenticated reads return 401", "traversal": "rejected"})
    (output / "results.json").write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps(results, indent=2))
finally:
    driver.quit()
    proxy.shutdown()
