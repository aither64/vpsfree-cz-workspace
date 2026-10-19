"""Read-only native/durable proof for a fixture admitted by live-browser.cjs."""
import asyncio
import hashlib
import json
import pathlib
import sqlite3
import subprocess
import sys

import websockets
import yaml

HERE = pathlib.Path(__file__).resolve().parent
WORKSPACE = HERE.parents[1]
label, provider, member_count = sys.argv[1:]
assert label.replace("-", "").isalnum()
record = json.loads((HERE / f"live-{label}.json").read_text())
assert record.get("verifiedAt"), "browser acceptance must finish first"
slug = record["slug"]
assert slug not in [HERE.name, "2026-10-19-haveapi-async-client-plan"]
assert record["threadId"] != "01a153f2-476c-7710-a39f-75ad837fbe94"
directory = WORKSPACE / "work" / slug
assert directory.parent == WORKSPACE / "work" and directory.name == slug
user_state = pathlib.Path.home() / ".local/state/dev-workspaces"
workspace_key = WORKSPACE.name + "-" + hashlib.sha256(str(WORKSPACE).encode()).hexdigest()[:16]
portal_state = user_state / "portal" / workspace_key
socket = "/run/user/1000/dev-workspaces/vpsfree-cz/app-server.sock"


def read_json(file):
    return json.loads(file.read_text())


async def native(identity):
    async with websockets.unix_connect(socket, max_size=16 * 1024 * 1024) as connection:
        async def rpc(number, method, params):
            await connection.send(json.dumps({"id": number, "method": method, "params": params}))
            while True:
                response = json.loads(await connection.recv())
                if response.get("id") == number:
                    assert "error" not in response, response
                    return response["result"]
        await rpc(1, "initialize", {"clientInfo": {"name": "live-creation-proof", "version": "1"},
                                    "capabilities": {"experimentalApi": True}})
        await connection.send(json.dumps({"method": "initialized"}))
        return (await rpc(2, "thread/read", {"threadId": identity, "includeTurns": True}))["thread"]


def exchange(thread, marker, turn_id):
    matches = [(turn, item) for turn in thread["turns"] for item in turn["items"]
               if item["type"] == "userMessage" and marker in json.dumps(item)]
    assert len(matches) == 1, (marker, matches)
    turn = matches[0][0]
    assert turn["id"] == turn_id and turn["status"] == "completed", turn
    assert any(item["type"] == "agentMessage" and item["text"].strip() == marker
               for item in turn["items"]), turn


async def main():
    manifest = yaml.safe_load((directory / "portal.yml").read_text())
    assert manifest["codex"]["thread_id"] == record["threadId"], manifest
    assert manifest["creation"]["state"] == "ready", manifest
    receipt = read_json(portal_state / "creations" / f"{slug}.json")
    assert receipt["receiptId"] == record["receiptId"] and receipt["state"] == "ready", receipt
    completion = read_json(portal_state / "creations" / f"{slug}.{record['receiptId']}.complete.json")
    assert completion["slug"] == slug and completion["receiptId"] == record["receiptId"], completion
    assert completion["threadId"] == record["threadId"], completion
    if record["kind"] == "fork":
        assert not (WORKSPACE / "worktrees/.locks" / f"{slug}.fork.json").exists()
    else:
        journal = read_json(WORKSPACE / "worktrees/.locks" / f"{slug}.creation.json")
        assert journal["state"] == "ready" and manifest["creation"]["initial_goal_sent"] is True
        if record["options"].get("provider"):
            assert journal["provider"] == record["options"]["provider"], journal
    thread = await native(record["threadId"])
    assert thread["modelProvider"] == provider and thread["cwd"] == str(directory), thread
    assert thread["model"] == "gpt-6.1-sol" and thread["reasoningEffort"] == "high", thread
    if record["kind"] == "fork":
        assert thread["forkedFromId"] == record["source"]["threadId"], thread
    if record["kind"] != "fork":
        exchange(thread, record["initialMarker"], record["initial"]["turnId"])
    if record["kind"] == "plan":
        plan = record["submitted"]["planText"]
        assert plan and hashlib.sha256(plan.encode()).hexdigest() == record["submitted"]["planSha256"]
        initial = next(item for turn in thread["turns"] for item in turn["items"]
                       if item["type"] == "userMessage" and record["initialMarker"] in json.dumps(item))
        delivered = "\n".join(part["text"] for part in initial["content"] if part["type"] == "text")
        # Match planCreationGoal/read_goal's ASCII boundary normalization while
        # retaining the captured plan's original bytes and hash above.
        expected_goal = ("Implement the following approved plan from session "
                         + record["source"]["slug"] + ".\n\n" + plan).strip(" \t\n\v\f\r\x00")
        assert delivered == expected_goal, (expected_goal, delivered)
        assert journal["goal_sha256"] == hashlib.sha256(expected_goal.encode()).hexdigest()
    exchange(thread, record["followupMarker"], record["followup"]["turnId"])
    result = json.loads(subprocess.check_output(
        ["dev-session", "team", "list", slug, "--as-is"], cwd=WORKSPACE))
    roster = result["roster"]
    assert roster["rootThreadId"] == record["threadId"] and roster["slug"] == slug, roster
    members = roster["members"] or []
    assert len(members) == int(member_count), roster
    assert roster["leadModel"] == "gpt-6.1-sol" and roster["leadEffort"] == "high", roster
    identities, member_proofs = [record["threadId"]], []
    for member in members:
        assert member["state"] == "ready", member
        metadata = await native(member["threadId"])
        assert metadata["modelProvider"] == provider and metadata["cwd"] == str(directory), metadata
        assert metadata["projectId"] == member["projectId"], metadata
        assert metadata["model"] == member["model"] and metadata["reasoningEffort"] == member["reasoningEffort"], metadata
        identities.append(member["threadId"])
        member_proofs.append({"retained": member, "native": metadata})
    assert len(identities) == len(set(identities)), identities
    databases = list((pathlib.Path.home() / ".codex").glob("state_*.sqlite"))
    assert len(databases) == 1, databases
    with sqlite3.connect(databases[0].as_uri() + "?mode=ro", uri=True) as database:
        observed = database.execute("SELECT id FROM threads WHERE cwd=? AND archived=0", (str(directory),)).fetchall()
    assert {row[0] for row in observed} == set(identities), observed
    proof = {"schema": 1, "label": label, "slug": slug, "requestId": record.get("requestId"),
             "receiptId": record["receiptId"], "provider": provider, "browserVerifiedAt": record["verifiedAt"],
             "native": thread, "members": member_proofs, "manifest": manifest,
             "receipt": receipt, "completion": completion, "activeIDs": sorted(identities)}
    (HERE / f"live-{label}-proof.json").write_text(json.dumps(proof, indent=2) + "\n")
    print(json.dumps({"label": label, "slug": slug, "provider": provider, "activeIDs": sorted(identities),
                      "initialTurn": record.get("initial", {}).get("turnId"), "followupTurn": record["followup"]["turnId"]}))


asyncio.run(main())
