import base64, hashlib, json, pathlib, ssl, urllib.request
root = pathlib.Path("/home/aither/workspace/ai/vpsfree.cz")
records = root / "work/2026-10-18-portal-untracked-files"
password = pathlib.Path("/var/lib/dev-workspaces/password/password").read_text().strip()
credential = base64.b64encode(("aither:" + password).encode()).decode()
context = ssl.create_default_context(cafile="/var/lib/dev-workspaces/public/ca.pem")
url = "https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/api/sessions/2026-10-17-confctl-rust-rewrite-plan/file?artifact=design.md"
request = urllib.request.Request(url, headers={"Authorization": "Basic " + credential})
with urllib.request.urlopen(request, context=context, timeout=30) as response:
    status = response.status
    file = json.load(response)
assert status == 200
assert file["path"] == "design.md"
assert file["source"] == "artifact"
expected = (root / "work/2026-10-17-confctl-rust-rewrite-plan/design.md").read_bytes().decode("utf8")
assert file["content"]["text"] == expected
result = {"result": "passed", "status": status, "path": file["path"], "source": file["source"], "sha256": hashlib.sha256(expected.encode()).hexdigest(), "tlsVerified": True, "authenticated": True}
(records / "live-external-link-result.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result))
