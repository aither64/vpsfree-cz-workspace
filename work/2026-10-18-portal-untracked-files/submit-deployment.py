"""Record existing user direction and submit the two prepared deployment jobs."""
import json
import os
import pathlib
import subprocess
import uuid

root = pathlib.Path("/home/aither/workspace/ai/vpsfree.cz")
slug = "2026-10-18-portal-untracked-files"
records = root / "work" / slug
os.umask(0o077)
assert json.loads((records / "verification-result.json").read_text())["result"] == "passed"
assert json.loads((records / "deployment-preparation-result.json").read_text())["result"] == "passed"


def request(action, label, fields):
    path = records / (label + "-request.json")
    if path.exists():
        payload = json.loads(path.read_text())
        assert {key: payload[key] for key in fields} == fields
    else:
        payload = {"schema": 1, "requestId": str(uuid.uuid4()), **fields}
        path.write_text(json.dumps(payload, indent=2) + "\n")
    with (records / (label + ".json")).open("w") as output, (records / (label + ".log")).open("w") as error:
        result = subprocess.run(
            ["/home/aither/bin/dev-session", "coordination", action, slug,
             "--as-is", "--request", str(path), "--json"],
            cwd=root, stdout=output, stderr=error,
        )
    if result.returncode:
        raise SystemExit(result.returncode)
    return json.loads((records / (label + ".json")).read_text())


prepared = {kind: json.loads((records / ("prepared-" + kind + ".json")).read_text())
            for kind in ["machine_activate", "profile_activate"]}
assert prepared["machine_activate"]["operation"]["configurationHead"] == "cf1271132140ca69776c6b24efce7891a531c736"
assert prepared["machine_activate"]["operation"]["target"] == "aitherdev"
expected_coverage = {
    "machine_activate": {"dev-workspace": "c1c620f91a04a70d599d208953b412a466981999",
                         "vpsfree-cz-configuration": "cf1271132140ca69776c6b24efce7891a531c736"},
    "profile_activate": {"dev-workspace": "c1c620f91a04a70d599d208953b412a466981999",
                         "workspace": "2b60e845de29aef76f3b31690f00e74bc0b2f614"},
}
for kind, expected in expected_coverage.items():
    actual = prepared[kind]["operation"]["coverage"]
    for name, revision in expected.items():
        assert {"repository": name, "revision": revision} in actual
approvals = {}
for kind, snapshot in prepared.items():
    approvals[kind] = request("approve", "approval-" + kind, {
        "kind": "deploy",
        "scope": [{"machine": "vpsfree:aitherdev", "actions": ["switch", "profile_activate"], "reboot": False}],
        "reviewedSnapshot": snapshot["id"],
        "source": {
            "kind": "user_instruction",
            "reference": "Initiating user request and implementation direction in this conversation",
            "quote": "aitherdev can be deployed using vpsfree-cz-configuration\nImplement the plan.",
        },
    })
reservation = request("reserve", "reservation", {
    "target": "aitherdev", "mode": "deploy_first",
    "approvalId": approvals["machine_activate"]["id"],
    "integrationObligations": [{"repository": name, "target": "refs/heads/master"}
                               for name in ["dev-workspace", "workspace", "vpsfree-cz-configuration"]],
})
jobs = {}
for kind, snapshot in prepared.items():
    jobs[kind] = request("submit", "submission-" + kind, {
        "kind": kind,
        "dependsOn": [] if kind == "machine_activate" else [jobs["machine_activate"]["id"]],
        "approvalId": approvals[kind]["id"],
        "reservationId": reservation["id"], "snapshot": snapshot,
    })
result = {"result": "submitted", "reservation": reservation, "jobs": jobs}
(records / "deployment-submission-result.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result))
