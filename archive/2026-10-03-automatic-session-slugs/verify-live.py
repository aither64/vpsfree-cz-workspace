#!/usr/bin/env python3
"""Authorized post-deployment canaries. Keep their sessions and identities."""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import time
import uuid
from urllib.parse import urlencode

parser = argparse.ArgumentParser()
parser.add_argument("--candidate", required=True)
args = parser.parse_args()
candidate = Path(args.candidate)
root = Path("/home/aither/workspace/ai/vpsfree.cz")
tracking = root / "work/2026-10-03-automatic-session-slugs"
runtime = root / "worktrees/2026-10-03-automatic-session-slugs/dev-workspace"
base = "https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz"
assert candidate.is_dir() and str(candidate).startswith("/nix/store/")
assert Path("/home/aither/.local/state/dev-workspaces/profile").resolve() == candidate
assert (tracking / "deployment.status").read_text().strip() == "0"
password = Path("/var/lib/dev-workspaces/password/password").read_text().strip()
assert re.fullmatch(r"[0-9a-fA-F]{64}", password)
auth = ('user = "aither:' + password + '"\n').encode()
del password

def request(path, body=None):
    command = ["curl", "--config", "-", "--cacert", "/var/lib/dev-workspaces/public/ca.pem",
               "--silent", "--show-error", "--max-time", "20", "--write-out", "\n%{http_code}",
               "--header", "Accept: application/json"]
    with tempfile.TemporaryDirectory(prefix="automatic-session-slugs-canary-") as directory:
        if body is not None:
            payload = Path(directory) / "request"
            payload.write_bytes(body)
            payload.chmod(0o600)
            command += ["--header", "Origin: " + base, "--header", "Content-Type: application/x-www-form-urlencoded",
                        "--data-binary", "@" + str(payload)]
        command += [base + path]
        result = subprocess.run(command, input=auth, capture_output=True, timeout=25)
    if result.returncode:
        raise RuntimeError("HTTPS request failed with curl exit " + str(result.returncode))
    data, status = result.stdout.rsplit(b"\n", 1)
    return int(status), data

code, index = request("/")
assert code == 200
assert b"Custom short name (optional)" in index
assert b'Leave the name blank' in index
catalog = json.loads((candidate / "share/dev-workspace/agent-teams.json").read_text())
assert "solo" in catalog["teams"]
assert catalog["catalog_digest"].encode() in index
for asset in ["app.js", "preparation.js", "creation.js"]:
    code, content = request("/static/" + asset)
    assert code == 200
    assert content == (runtime / "portal/internal/web/static" / asset).read_bytes()
print("PASS authenticated HTTPS, optional-name form and exact shipped assets", flush=True)

state_path = tracking / "canary-identities.json"
assert not state_path.exists(), "Prior canary identities must be recovered, not overwritten"
entries = []
def save_entries():
    temporary = state_path.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(entries, indent=2) + "\n")
    temporary.chmod(0o600)
    temporary.replace(state_path)

for kind in ["automatic", "custom"]:
    request_id = str(uuid.uuid4())
    custom = "Slug_canary_" + uuid.uuid4().hex[:8] if kind == "custom" else ""
    fields = {"clientRequestId": request_id, "goal": "Automatic slug verification. Reply Ready and remain idle. Do not edit files, run commands, create clusters, send messages, or make external changes.",
              "creation_date": datetime.date.today().isoformat(), "name": custom,
              "team": "solo", "catalogDigest": catalog["catalog_digest"], "model": "", "effort": ""}
    body = urlencode(fields).encode()
    entry = {"kind": kind, "requestId": request_id, "customName": custom,
             "fields": fields, "bodySha256": hashlib.sha256(body).hexdigest(), "status": "issued", "issuedAt": datetime.datetime.now(datetime.timezone.utc).isoformat()}
    entries.append(entry)
    save_entries()  # Preserve the exact attempt before its first network mutation.
    code, result = request("/sessions", body)
    assert code == 202, "Canary admission was not confirmed; recover the recorded request ID"
    status = json.loads(result)
    assert status["requestId"] == request_id
    assert re.fullmatch(r"[0-9a-f]{64}", status["receiptId"])
    assert status["url"] == "/creations/" + request_id + "/"
    entry.update({"receiptId": status["receiptId"], "attempt": status["attempt"], "url": status["url"]})
    save_entries()
    replay_code, replay_bytes = request("/sessions", body)
    replay = json.loads(replay_bytes)
    assert replay_code == 202 and replay["requestId"] == request_id and replay["receiptId"] == status["receiptId"]
    changed = dict(fields, goal=fields["goal"] + " Changed input.")
    conflict_code, _ = request("/sessions", urlencode(changed).encode())
    assert conflict_code == 409
    deadline = time.monotonic() + 180
    while True:
        code, data = request("/api/session-creations/" + request_id)
        assert code == 200
        current = json.loads(data)
        assert current["requestId"] == request_id and current["receiptId"] == status["receiptId"]
        if current["state"] == "ready":
            break
        if current["state"] in ["failed", "paused", "conflict", "cancelled", "gone"]:
            entry.update({"status": current["state"], "attempt": current["attempt"]})
            save_entries()
            raise RuntimeError("Recorded " + kind + " canary needs recovery")
        if time.monotonic() >= deadline:
            entry["status"] = "incomplete"
            save_entries()
            raise RuntimeError("Recorded canary did not become ready within the acceptance deadline")
        time.sleep(1)
    slug = current["slug"]
    assert re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}-[A-Za-z0-9][A-Za-z0-9_-]{0,47}", slug)
    assert current["canonicalUrl"] == "/" + slug + "/"
    if custom:
        assert slug.endswith("-" + custom)
    code, _ = request(current["canonicalUrl"])
    assert code == 200
    code, details_bytes = request("/api/sessions/" + slug + "/details")
    assert code == 200
    details = json.loads(details_bytes)
    code, thread_bytes = request("/api/sessions/" + slug + "/thread")
    assert code == 200
    thread = json.loads(thread_bytes)
    assert isinstance(thread["threadId"], str) and thread["threadId"]
    digest = hashlib.sha256(str(root).encode()).hexdigest()[:16]
    private_root = Path("/home/aither/.local/state/dev-workspaces/portal") / (root.name + "-" + digest)
    own_record = None
    for directory in ["session-preparation-mappings", "session-preparations"]:
        record_path = private_root / directory / (request_id + ".json")
        if record_path.is_file():
            own_record = json.loads(record_path.read_text())
            break
    assert own_record is not None
    assert own_record["workspace"] == str(root) and own_record["requestId"] == request_id
    assert own_record["receiptId"] == status["receiptId"] and own_record["slug"] == slug
    outcome = own_record.get("namingOutcome", "")
    assert outcome == ("custom" if custom else "model"), "Canary must prove actual model naming or exact custom-name bypass"
    entry.update({"status": "ready", "slug": slug, "namingOutcome": outcome, "canonicalUrl": current["canonicalUrl"],
                  "detailsKeys": sorted(details.keys()), "threadId": thread["threadId"],
                  "threadStatus": thread["status"], "model": thread["model"],
                  "reasoningEffort": thread["reasoningEffort"]})
    save_entries()
    print("PASS " + kind + " canary, identical replay and changed-input409: " + slug, flush=True)
print("PASS retained canaries; no session lifecycle or ref cleanup performed", flush=True)
