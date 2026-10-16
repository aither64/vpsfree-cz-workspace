"""Failure-only, read-only projection of this VM's fixed disposable fixture."""
import json
import os
import stat

BASE = "/home/developer/.local/state/dev-workspaces/providers/fixture/"
UUID = "aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa"
ROOT = "/home/developer/workspace"
SOCKET = "/run/user/1000/dev-workspaces/fixture/app-server.sock"
PHASES = {"waiting", "applying", "applied", "canceled", "failed", "recovery-required"}
STAGES = {"capturing", "quiescing", "daemon-stop", "shared-start"}
PROVIDERS = {"openai", "pool", "pooltwo"}


def private_json(name, maximum):
    # Fixed basename only. Never follow a snapshot reference supplied by state.
    fd = os.open(BASE + name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    with os.fdopen(fd, "rb") as stream:
        info = os.fstat(stream.fileno())
        if not stat.S_ISREG(info.st_mode) or info.st_uid != 1000 or info.st_mode & 0o077:
            raise ValueError("private file")
        if info.st_size > maximum:
            raise ValueError("file bound")
        data = stream.read(maximum + 1)
        if len(data) > maximum:
            raise ValueError("read bound")
        return json.loads(data)


def enum(value, allowed):
    return value if isinstance(value, str) and value in allowed else "invalid-or-absent"


def main():
    result = {"kind": "fixture-provider-metadata"}
    try:
        state = private_json("state.json", 1024 * 1024)
        assert isinstance(state, dict) and state.get("schema") == 1
        assert state.get("workspace") == "fixture" and state.get("root") == ROOT
        assert state.get("socket") == SOCKET
        op = state["operation"]
        assert isinstance(op, dict) and op.get("id") == UUID
        blockers = op.get("blockers")
        result["operation"] = {
            "phase": enum(op.get("phase"), PHASES),
            "stage": enum(op.get("stage"), STAGES),
            "active": enum(state.get("active"), PROVIDERS),
            "target": enum(op.get("target"), PROVIDERS),
            "previousActive": enum(op.get("previousActive"), PROVIDERS),
            "blockerCount": len(blockers) if isinstance(blockers, list) else None,
        }
        snapshot_name = UUID + ".snapshot.json"
        assert op.get("snapshot") == BASE + snapshot_name
        try:
            snapshot = private_json(snapshot_name, 16 * 1024 * 1024)
            assert isinstance(snapshot, dict) and snapshot.get("schema") == 1
            assert snapshot.get("workspace") == ROOT
            threads, loaded = snapshot["threads"], snapshot["loaded"]
            assert isinstance(threads, list) and len(threads) <= 4096
            assert isinstance(loaded, list) and len(loaded) <= 4096
            result["snapshot"] = {"status": "validated", "threadCount": len(threads), "loadedCount": len(loaded)}
        except Exception:
            result["snapshot"] = {"status": "unavailable-or-invalid"}
        try:
            terminals = private_json(snapshot_name + ".terminals", 1024 * 1024)
            assert isinstance(terminals, dict) and terminals.get("schema") == 1
            assert terminals.get("workspace") == "fixture" and terminals.get("root") == ROOT
            assert terminals.get("socket") == SOCKET
            assert isinstance(terminals["terminals"], list) and len(terminals["terminals"]) <= 4096
            result["terminals"] = {"status": "validated", "terminalCount": len(terminals["terminals"])}
        except Exception:
            result["terminals"] = {"status": "unavailable-or-invalid"}
    except Exception:
        result["state"] = "unavailable-or-invalid"
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
