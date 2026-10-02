#!/usr/bin/env python3
"""One use only: continue the known registered fixture without restarting Codex."""

import argparse
import hashlib
import importlib.util
import os
from pathlib import Path
import stat
import sys
from types import SimpleNamespace


SPEC = importlib.util.spec_from_file_location("creation_verification", Path(__file__).with_name("verify-creation.py"))
h = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(h)
ROOT, PACKAGE = h.SEEDED_ROOT, h.SEEDED_PACKAGE
PROOF = Path("/home/aither/.local/state/dev-workspaces/verification/2026-10-02-portal-creation-performance/benchmark-started-proof.json")
PROOF_SHA256 = "21d0465d65e5ec4a171dd50daf295f0328968d401cc4932164a1f40f8ed08a6f"
ALIAS_PROOF = PROOF.with_name("benchmark-socket-alias-proof.json")
ALIAS_PROOF_SHA256 = "3f6b7faf3e402bc3a4981a78b5dd0c56c447ddf5b398ea087ebfb14bfcaef84d"
CLAIM = ROOT / "started-continuation"
SOCKET = ROOT / "r/bench/app-server.sock"
PROFILE_IDENTITY = [64769, 18889018, 1790964862368558275, 1790964862368558275, str(PACKAGE)]
# Exact non-credential records from the demonstrated failure. Auth is never read.
RECORDS = {
    "result.json": "c2b9a581fa9c03f5397ac26c50a9aa6727a4818c3b85a48224d710f250169833",
    "registry.json": "8e0686ea055d23d51438586904f3aab123f7bcad5f38a498386c7dd9f7912e51",
    "history.json": "2ca62845a1e5c40144e3eb71ce33ec3fa5117db966d9a5a631878b2ce3c64ecf",
    "r/bench/registration-inventory.json": "74366daf4ce75fdae7dd9f2677d52159b5e11a4e0ee7b14f117f3d3c0c537442",
    "workspace/.dev-workspace.json": "9c6095b95548ee3daa6c01eaf3dd7de81cbb2ca0f3a7fdbdd99aac21697396db",
    "workspace/AGENTS.md": "d80db74d03f1e1dfeda18483f1aa50aa25432bc9c3be67a06586358c6f0c0fab",
    "bin/dev-session": "e581b478ea50b548491d1829d0aefa148e8d81308a64efed3a5d41f7c61b2269",
    "bin/workspace-portal": "c09991f35b0b37385cd1240a18689a06c35419fd589668f79442506df1ddb7d1",
    "codex/config.toml": "4a6d91cf2bed4ef5ac8ed28723e0074689259534722f855cbb8f690fa7ed069a",
    "seeded-continuation/result.json": "7eb74bb77579c53e5cb010a04131344edb765b41760ed95104b2315126ab8474",
    "seeded-continuation/register.stderr.log": "6047a79ca6298d7ef77b03ac86615a7926bf080964d9cbec4742c8284e282b91",
    "seeded-continuation/.dev-workspace.json": "6c744d2be2d8cea461ad42aa5f1b40d4609e5a1297428a1eabdeb66ace76d64c",
}
PROOF_RECORDS = {"config.json": "configSHA256", "processes.json": "processesSHA256",
                 "preset.json": "presetSHA256", "r/bench/registration.json": "registrationSHA256"}


def require_socket_alias(proof, alias):
    """The selected transport publishes this exact alias to its protected socket."""
    h.require(alias["originalProofSHA256"] == PROOF_SHA256 and alias["socketPath"] == str(SOCKET)
              and alias["pid"] == proof["pid"] and alias["kernelStartTicks"] == proof["kernelStartTicks"],
              "socket alias proof does not identify the original process")
    link, target = SOCKET.lstat(), Path(alias["resolvedTarget"]).lstat()
    for info, recorded in ((link, alias["alias"]), (target, alias["target"])):
        h.require([info.st_dev, info.st_ino, info.st_uid, info.st_mode, info.st_ctime_ns, info.st_mtime_ns] ==
                  [recorded[key] for key in ("device", "inode", "uid", "mode", "ctimeNs", "mtimeNs")],
                  "recorded socket alias or target identity changed")
    h.require(stat.S_ISLNK(link.st_mode) and link.st_uid == proof["uid"]
              and os.readlink(SOCKET) == alias["aliasTarget"] == alias["resolvedTarget"]
              and SOCKET.resolve(strict=True) == Path(alias["resolvedTarget"])
              and stat.S_ISSOCK(target.st_mode) and stat.S_IMODE(target.st_mode) == 0o600
              and target.st_uid == proof["uid"]
              and (target.st_dev, target.st_ino) == (proof["socketDevice"], proof["socketInode"]),
              "recorded socket alias does not resolve to the original private socket")


def require_host_identity(proof, native, alias):
    """Only the recorded PID, boot and socket; run in the parent's host context."""
    h.require(proof["pid"] == 1687746 and proof["uid"] == os.geteuid()
              and proof["cwd"] == str(ROOT) and proof["exe"] == proof["nativeEntrypoint"] == str(native)
              and proof["socketPath"] == str(SOCKET), "host proof does not identify this fixture")
    process = Path(f"/proc/{proof['pid']}")
    fields = (process / "stat").read_text().rsplit(") ", 1)[1].split()
    h.require(process.stat().st_uid == proof["uid"] and fields[0] not in ("Z", "X")
              and int(fields[19]) == proof["kernelStartTicks"]
              and Path("/proc/sys/kernel/random/boot_id").read_text().strip() == proof["bootId"],
              "recorded App Server boot/start identity changed")
    h.require((process / "exe").resolve(strict=True) == native
              and os.readlink(process / "cwd") == str(ROOT)
              and hashlib.sha256((process / "cmdline").read_bytes()).hexdigest() == proof["cmdlineSHA256"],
              "recorded App Server executable, cwd or command identity changed")
    require_socket_alias(proof, alias)
    listener = alias["listener"]
    h.require(os.readlink(process / "fd" / str(listener["fd"])) == f"socket:[{listener['kernelInode']}]",
              "recorded App Server listener descriptor changed")
    rows = [line.split(None, 7) for line in (process / "net/unix").read_text().splitlines()[1:]]
    # Accepted streams share the listener's path, but have their own kernel inode.
    matches = [row for row in rows if len(row) >= 7 and row[6] == str(listener["kernelInode"])]
    h.require(len(matches) == 1 and matches[0][3:] ==
              [listener["flags"], listener["type"], listener["state"],
               str(listener["kernelInode"]), alias["resolvedTarget"]],
              "recorded App Server no longer owns the exact listening socket")


def validate_started_fixture():
    h.require(ROOT.resolve(strict=True) == ROOT and PACKAGE.resolve(strict=True) == PACKAGE,
              "exact root or candidate is unavailable")
    info = ROOT.lstat()
    h.require(stat.S_ISDIR(info.st_mode) and info.st_uid == os.geteuid()
              and stat.S_IMODE(info.st_mode) == 0o700, "private fixture root identity changed")
    for path, digest in ((PROOF, PROOF_SHA256), (ALIAS_PROOF, ALIAS_PROOF_SHA256)):
        info = path.lstat()
        h.require(stat.S_ISREG(info.st_mode) and info.st_uid == os.geteuid()
                  and stat.S_IMODE(info.st_mode) == 0o600
                  and hashlib.sha256(path.read_bytes()).hexdigest() == digest,
                  "parent host proof changed or is not private")
    proof, alias = h.read(PROOF), h.read(ALIAS_PROOF)
    expected = {"app-server.log", "bin", "codex", "codex-version.stderr.log", "config.json", "events",
                "history", "history.json", "preset.json", "processes.json", "profile", "profile-token.stderr.log",
                "r", "register.stderr.log", "registry.json", "result.json", "seed-app-server.stderr.log",
                "seed-process.json", "seeded-continuation", "skills", "state", "team-preset.stderr.log",
                "workspace", "xdg-cache", "xdg-config", "xdg-state"}
    h.require({p.name for p in ROOT.iterdir()} == expected, "unexpected state or prior follow-on claim")
    for path in ROOT.rglob("*"):
        if path == SOCKET:
            require_socket_alias(proof, alias)
            continue
        info = path.lstat()
        h.require(info.st_uid == os.geteuid() and (path == ROOT / "profile" or not info.st_mode & 0o022),
                  "foreign owner or writable fixture path")
        h.require(stat.S_ISDIR(info.st_mode) or stat.S_ISREG(info.st_mode)
                  or (path == ROOT / "profile" and stat.S_ISLNK(info.st_mode)), "unexpected link or special fixture file")
    profile = (ROOT / "profile").lstat()
    h.require(stat.S_ISLNK(profile.st_mode) and
              [profile.st_dev, profile.st_ino, profile.st_ctime_ns, profile.st_mtime_ns,
               os.readlink(ROOT / "profile")] == PROFILE_IDENTITY, "private profile/token identity changed")
    auth = (ROOT / "codex/auth.json").lstat()
    h.require(stat.S_ISREG(auth.st_mode) and stat.S_IMODE(auth.st_mode) == 0o600, "retained auth is not private")
    layouts = {"r": {"bench"}, "r/bench": {"app-server.sock", "registration.json", "registration-inventory.json"},
               "state": {"transition.lock"}, "bin": {"dev-session", "workspace-portal"},
               "workspace": {"work", "worktrees", "archive", "repos", "AGENTS.md", ".dev-workspace.json"},
               "seeded-continuation": {"result.json", "register.stderr.log", ".dev-workspace.json"}}
    for name in ("events", "skills", "xdg-cache", "xdg-config", "xdg-state",
                 "workspace/work", "workspace/worktrees", "workspace/archive", "workspace/repos"):
        layouts[name] = set()
    for name, children in layouts.items():
        h.require({p.name for p in (ROOT / name).iterdir()} == children, "runtime/creation layout changed")
    records = {**RECORDS, **{name: proof[key] for name, key in PROOF_RECORDS.items()}}
    for name, digest in records.items():
        h.require(hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest,
                  f"retained non-credential record changed: {name}")
    previous, config, preset = (h.read(ROOT / name) for name in ("result.json", "config.json", "preset.json"))
    h.require(previous["state"] == "incomplete" and previous["results"] == [] and "warmup" not in previous
              and previous["candidate"] == str(PACKAGE) and previous["error"] ==
              "running App Server executable is not the selected Codex", "not the known pre-portal failure")
    launcher = (PACKAGE / "libexec/codex/bin/codex").resolve(strict=True)
    native = h.native_codex_entrypoint(launcher)
    h.require(str(launcher) == config["codex"] == proof["codexLauncher"] and config["root"] == str(ROOT)
              and config["package"] == str(PACKAGE) and config["workspace"] == str(ROOT / "workspace"),
              "selected package or config identity changed")
    processes = h.read(ROOT / "processes.json")
    h.require(processes == [{"label": "app-server", "pid": proof["pid"], "startedAt": proof["recordedStartedAt"]}],
              "recorded process sequence changed")
    contract = h.read(PACKAGE / "share/workspace-portal/runtime-contract.json")["agentTeamRegistration"]
    marker = h.read(ROOT / "r/bench/registration.json")
    inventory = h.read(ROOT / "r/bench/registration-inventory.json")
    workspace = {"name": "bench", "root": str(ROOT / "workspace")}
    h.require(marker["schema"] == contract["markerSchema"] and marker["workspace"] == workspace
              and marker["launch"]["codex_path"] == str(launcher) and marker["launch"]["package_root"] == str(PACKAGE)
              and marker["launch"]["policy"] == contract["policy"] and marker["launch"]["argv"] == []
              and marker["launch"]["required_native_child_threads"] == 0
              and inventory == {"schema": contract["markerSchema"], "workspace": workspace,
                                "package_root": str(PACKAGE), "states": []}, "registration contract changed")
    require_host_identity(proof, native, alias)
    history = h.read(ROOT / "history.json")
    paths = list((ROOT / "codex/sessions").rglob("*.jsonl"))
    h.require(previous["history"] == history and history["activeRollouts"] == len(paths) == 3379
              and history["paddingBytesPerThread"] == 16384 and history["archivedRollouts"] == 0
              and sum(p.stat().st_size for p in paths) == history["bytes"] == 208256155
              and not (ROOT / "codex/archived_sessions").exists(), "retained seed history changed")
    h.require(len({h.validate_seeded_rollout(p, ROOT) for p in paths}) == 3379, "seed identities changed")
    return previous, config, preset, processes, proof, native, records, alias


def preserve_started_failure(records):
    # Exclusive one-use claim; never clear it, including after a partial copy.
    CLAIM.mkdir(mode=0o700)
    for name, source in [(name, ROOT / name) for name in records] + [
            ("host-process-proof.json", PROOF), ("host-socket-alias-proof.json", ALIAS_PROOF)]:
        target = CLAIM / name
        target.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
        with target.open("xb") as stream:
            os.fchmod(stream.fileno(), 0o600)
            stream.write(source.read_bytes())
            stream.flush()
            os.fsync(stream.fileno())
    for directory in [p for p in CLAIM.rglob("*") if p.is_dir()] + [CLAIM, ROOT]:
        descriptor = os.open(directory, os.O_RDONLY | os.O_DIRECTORY)
        try:
            os.fsync(descriptor)
        finally:
            os.close(descriptor)


def main():
    argparse.ArgumentParser(description=__doc__).parse_args()
    os.umask(0o077)
    previous, config, preset, processes, proof, native, records, alias = validate_started_fixture()
    h.require(h.shutil.which("tmux"), "prepared tmux environment unavailable")
    require_host_identity(proof, native, alias)
    preserve_started_failure(records)
    result = {"state": "running", "candidate": str(PACKAGE), "startedAt": h.stamp(), "results": [],
              "history": previous["history"], "codexVersion": previous["codexVersion"],
              "resumedFrom": "started-continuation/result.json"}
    args = SimpleNamespace(model_timeout=180, history_count=3379, history_padding_bytes=16384, skip_faults=False)
    try:
        h.save(ROOT / "result.json", result)
        return h.finish_creation_verification(config, h.isolated_environment(ROOT, PACKAGE), preset, processes, result, args)
    except Exception as error:
        result.update(state="incomplete", finishedAt=h.stamp(),
                      error=str(error) if isinstance(error, h.Failure) else type(error).__name__)
        h.save(ROOT / "result.json", result)
        print("Follow-on incomplete; private evidence and all processes retained.", flush=True)
        return 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as error:
        reason = str(error) if isinstance(error, h.Failure) else type(error).__name__
        print(f"Follow-on failed: {reason}; evidence and processes retained. Do not retry.", file=sys.stderr)
        sys.exit(1)
