"""Read-only HTTPS acceptance; credentials stay in process memory."""
import argparse, base64, hashlib, json, re, ssl, time, urllib.error, urllib.parse, urllib.request
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--features", action="store_true")
args = parser.parse_args()
base = "https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz"
slug = "2026-09-12-portal-review-experience"
context = ssl.create_default_context(cafile="/var/lib/dev-workspaces/public/ca.pem")
password = Path("/var/lib/dev-workspaces/password/password").read_text().strip()
authorization = "Basic " + base64.b64encode(("aither:" + password).encode()).decode()
results = []
def request(path, authorized=True, payload=None):
    headers = {"Authorization": authorization} if authorized else {}
    body = None
    if payload is not None:
        body = json.dumps(payload).encode()
        headers.update({"Content-Type": "application/json", "Origin": base})
    started = time.monotonic()
    try:
        response = urllib.request.urlopen(urllib.request.Request(base + path, data=body, headers=headers), context=context, timeout=30)
    except urllib.error.HTTPError as error:
        response = error
    with response:
        data = response.read()
        results.append({"path": path.split("?")[0], "status": response.status, "seconds": round(time.monotonic()-started, 3)})
        return response.status, data, response.headers
assert request("/healthz", False)[0] == 401
status, data, _ = request("/healthz")
assert status == 200 and json.loads(data)["ok"] is True
status, data, _ = request("/" + slug + "/")
assert status == 200
page = data.decode()
if args.features:
    assert re.search(r'aria-selected="true"[^>]*data-transcript-filter="messages"', page)
    assert 'id="codex-work-counts"' in page and 'id="codex-duration"' in page
    for asset in ("app.js", "repository-review.js", "repository-review.css", "review-editor.js"):
        status, data, headers = request("/static/" + asset)
        assert status == 200 and len(data) > 100
        assert headers.get("Cache-Control") == "no-store"
    api = "/api/sessions/" + slug
    for name in ("codex-web", "dev-workspace", "vpsfree-dev-workspace", "workspace"):
        repository = hashlib.sha256(name.encode()).hexdigest()[:32]
        status, data, _ = request(api + "/repository-history?" + urllib.parse.urlencode({"repository":repository}))
        assert status == 200, (name, status)
        history = json.loads(data)
        assert history["history"]["commits"], name
        status, data, _ = request(api + "/repository-comparison?" + urllib.parse.urlencode({"repository":repository}), payload={"snapshot":history["snapshot"]})
        assert status == 200, (name, status)
        comparison = json.loads(data)
        assert comparison["files"], name
        results.append({"repository":name, "commits":len(history["history"]["commits"]), "files":len(comparison["files"]), "head":history["pair"]["head"]})
    status, data, _ = request("/codex/conversations/" + slug + "/activity")
    assert status == 200
    activity = json.loads(data)
    assert activity["threadId"] == "01a09541-d1ba-7e32-a634-6f915c2da0a4"
    results.append({"activity": {key: activity.get(key) for key in ("threadId","currentState","workingMs","waitingMs","unclassifiedMs")}})
print(json.dumps({"features":args.features,"checks":results}, indent=2))
