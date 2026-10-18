import hashlib, json, os, pathlib, subprocess, sys, time, uuid
root = pathlib.Path("/home/aither/workspace/ai/vpsfree.cz")
slug = "2026-10-18-portal-untracked-files"
records = root / "work" / slug
os.umask(0o077)
verification = json.loads((records / "verification-result.json").read_text())
if verification.get("result") != "passed":
    raise SystemExit("Packaged verification has not passed")
evidence = []
for kind, name in [("review", "review-followup-report.md"), ("verification", "verification-result.json")]:
    path = records / name
    evidence.append({"kind": kind, "path": str(path.relative_to(root)), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
results = []
for kind in ["machine_activate", "profile_activate"]:
    request = {"schema": 1, "requestId": str(uuid.uuid4()), "kind": kind, "evidence": evidence}
    if kind == "machine_activate":
        request["target"] = "aitherdev"
    request_path = records / ("prepare-" + kind + "-request.json")
    request_path.write_text(json.dumps(request, indent=2) + "\n")
    started = time.time()
    with (records / ("prepared-" + kind + ".json")).open("w") as output, (records / ("prepare-" + kind + ".log")).open("w") as error:
        command = ["/home/aither/bin/dev-session", "coordination", "prepare", slug, "--as-is", "--request", str(request_path), "--json"]
        status = subprocess.run(command, cwd=root, stdout=output, stderr=error).returncode
    results.append({"kind": kind, "exitStatus": status, "elapsedSeconds": round(time.time() - started, 3)})
    (records / "deployment-preparation-result.json").write_text(json.dumps({"steps": results, "result": "passed" if len(results) == 2 and all(r["exitStatus"] == 0 for r in results) else "incomplete"}, indent=2) + "\n")
    if status:
        raise SystemExit(status)
