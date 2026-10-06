#!/usr/bin/env python3
"""One use only: validate the completed warm-up, then run all five samples and faults."""

import argparse
import hashlib
import importlib.util
import os
from pathlib import Path
import stat
import sys
from types import SimpleNamespace


SPEC = importlib.util.spec_from_file_location("started_verification", Path(__file__).with_name("verify-started-creation.py"))
d = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(d)
h = d.h
ROOT, PACKAGE = d.ROOT, d.PACKAGE
PROOF = d.PROOF.with_name("benchmark-warmup-proof.json")
PROOF_SHA256 = "42c582ce94c42d27454cd65ae11094b822a657ffc8acac9ca0f39566a9ae36a9"
CLAIM = ROOT / "warmup-continuation"
SLUG = "2026-10-02-creation-warmup"
ROOT_ID = "01a0fe0c-52c2-76e1-98bf-f11e1455623a"
NAMESPACE = "workspace-e015aa0dc07aa15b"
EVENTS = f"events/{SLUG}.jsonl"
EVENTS_SHA256 = "ebc032fae00bc43799b9818baedac630fcb153dab4169285c77d8e544a5b943b"
CODEX_CONFIG_SHA256 = "5e6aaa3ba5d51ab835aa9803bf04706bd55f1e6d53e6410d659bf6053e8a0b75"
CREATION_JOURNAL = f"workspace/worktrees/.locks/{SLUG}.creation.json"
CREATION_JOURNAL_SHA256 = "da2324cab28eae16f6bd97af531c91f8b3cbd5523195f8490247f112538d7e51"


def require_retained_services(proof, original, alias, native):
    d.require_host_identity(original, native, alias)
    h.require(proof["bootId"] == original["bootId"] and
              [(p["label"], p["pid"]) for p in proof["processes"]] ==
              [("app-server", 1687746), ("tmux", 1798536), ("portal", 1798541)],
              "warm-up process proof changed")
    for recorded in proof["processes"]:
        process = Path(f"/proc/{recorded['pid']}")
        fields = (process / "stat").read_text().rsplit(") ", 1)[1].split()
        h.require(process.stat().st_uid == recorded["uid"] == os.geteuid()
                  and fields[0] not in ("Z", "X") and int(fields[19]) == recorded["kernelStartTicks"]
                  and (process / "exe").resolve(strict=True) == Path(recorded["exe"])
                  and os.readlink(process / "cwd") == recorded["cwd"] == str(ROOT)
                  and hashlib.sha256((process / "cmdline").read_bytes()).hexdigest() == recorded["cmdlineSHA256"],
                  "retained runtime process identity changed")
    h.require([s["path"] for s in proof["sockets"]] ==
              [str(ROOT / "r/bench" / name) for name in ("app-server.sock", "tmux.sock", "portal.sock")],
              "warm-up socket proof changed")
    for recorded in proof["sockets"]:
        path = Path(recorded["path"])
        for info, expected in ((path.lstat(), recorded["link"]), (path.stat(), recorded["target"])):
            h.require([info.st_dev, info.st_ino, info.st_uid, info.st_mode, info.st_ctime_ns, info.st_mtime_ns] ==
                      [expected[key] for key in ("device", "inode", "uid", "mode", "ctimeNs", "mtimeNs")],
                      "retained runtime socket identity changed")
        h.require(path.stat().st_uid == os.geteuid() and stat.S_ISSOCK(path.stat().st_mode)
                  and str(path.resolve(strict=True)) == recorded["resolvedPath"]
                  and (os.readlink(path) if path.is_symlink() else None) == recorded["aliasTarget"],
                  "retained runtime socket target changed")


def require_records(records):
    for name, digest in records.items():
        h.require(hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest,
                  f"retained non-credential record changed: {name}")


def completed_warmup(config, preset):
    warmup = h.read(ROOT / "creation-warmup-ready.json")
    h.require(warmup["slug"] == SLUG and warmup["rootThreadID"] == ROOT_ID
              and warmup["firstAttempt"]["state"] == "ready" and warmup["firstAttempt"]["attempt"] == 1,
              "not the known ready warm-up")
    receipt, roster = h.ready_evidence(config, warmup["firstAttempt"], preset)
    h.require(receipt["attempt"] == 1 and receipt["goal"] == h.GOAL
              and receipt["receiptId"] == warmup["firstAttempt"]["receiptId"]
              and receipt["startedAt"] == warmup["acceptedAt"] and receipt["updatedAt"] == warmup["readyAt"]
              and roster["rootThreadId"] == ROOT_ID and warmup["memberThreadIDs"] ==
              {m["address"]: m["threadId"] for m in roster["members"]}
              and warmup["acceptanceToReadySeconds"] == h.instant(receipt["updatedAt"]) - h.instant(receipt["startedAt"]),
              "warm-up receipt, roster or timing identity changed")
    model = h.wait_model(config, SLUG, ROOT_ID, 180)
    model["acceptanceToFirstAssistantSeconds"] = h.instant(model["firstAssistantAt"]) - h.instant(warmup["acceptedAt"])
    model["readyToFirstAssistantSeconds"] = h.instant(model["firstAssistantAt"]) - h.instant(warmup["readyAt"])
    warmup["model"] = model
    warmup["stages"] = h.progress_evidence(config, SLUG, preset)
    return warmup


def validate_warmup_fixture():
    h.require(ROOT.resolve(strict=True) == ROOT and PACKAGE.resolve(strict=True) == PACKAGE,
              "exact root or candidate is unavailable")
    info = ROOT.lstat()
    h.require(stat.S_ISDIR(info.st_mode) and info.st_uid == os.geteuid()
              and stat.S_IMODE(info.st_mode) == 0o700, "private fixture root changed")
    for path, digest in ((PROOF, PROOF_SHA256), (d.PROOF, d.PROOF_SHA256), (d.ALIAS_PROOF, d.ALIAS_PROOF_SHA256)):
        info = path.lstat()
        h.require(stat.S_ISREG(info.st_mode) and info.st_uid == os.geteuid() and stat.S_IMODE(info.st_mode) == 0o600
                  and hashlib.sha256(path.read_bytes()).hexdigest() == digest, "parent metadata proof changed")
    proof, original, alias = h.read(PROOF), h.read(d.PROOF), h.read(d.ALIAS_PROOF)
    h.require(proof["root"] == str(ROOT) and proof["candidate"] == str(PACKAGE)
              and proof["originalProcessProofSHA256"] == d.PROOF_SHA256
              and proof["originalAliasProofSHA256"] == d.ALIAS_PROOF_SHA256, "proof lineage changed")
    records = dict(d.RECORDS)
    # The normal warm-up CLI recorded tui.screen_reader_detection_done = true.
    # The original pre-portal config remains pinned in started-continuation.
    records["codex/config.toml"] = CODEX_CONFIG_SHA256
    for recorded in proof["files"].values():
        records[str(Path(recorded["path"]).relative_to(ROOT))] = recorded["sha256"]
    records[EVENTS] = EVENTS_SHA256
    records[CREATION_JOURNAL] = CREATION_JOURNAL_SHA256
    prior = {**d.RECORDS, **{name: original[key] for name, key in d.PROOF_RECORDS.items()},
             "host-process-proof.json": d.PROOF_SHA256, "host-socket-alias-proof.json": d.ALIAS_PROOF_SHA256}
    records.update({f"started-continuation/{name}": digest for name, digest in prior.items()})
    require_records(records)
    previous, config, preset, processes = (h.read(ROOT / name) for name in
                                          ("result.json", "config.json", "preset.json", "processes.json"))
    h.require(previous["state"] == "incomplete" and previous["results"] == [] and "warmup" not in previous
              and previous["candidate"] == str(PACKAGE) and previous["error"] ==
              "initial request was absent or submitted more than once"
              and previous["resumedFrom"] == "started-continuation/result.json", "not the known warm-up failure")
    h.require(config["root"] == str(ROOT) and config["package"] == str(PACKAGE)
              and config["workspace"] == str(ROOT / "workspace") and config["codex"] == original["codexLauncher"],
              "retained config changed")
    native = h.native_codex_entrypoint(config["codex"])
    require_retained_services(proof, original, alias, native)
    h.require([{k: p[k] for k in ("label", "pid", "startedAt")} for p in processes] ==
              [{k: p[k] for k in ("label", "pid", "startedAt")} for p in proof["processes"]],
              "runtime process records changed")
    profile = (ROOT / "profile").lstat()
    h.require(stat.S_ISLNK(profile.st_mode) and
              [profile.st_dev, profile.st_ino, profile.st_ctime_ns, profile.st_mtime_ns,
               os.readlink(ROOT / "profile")] == d.PROFILE_IDENTITY, "private profile identity changed")
    socket_paths = {Path(s["path"]) for s in proof["sockets"]}
    for path in ROOT.rglob("*"):
        info = path.lstat()
        if path in socket_paths:
            continue  # Exact metadata and targets already proved above, repeated before claim.
        h.require(info.st_uid == os.geteuid() and (path == ROOT / "profile" or not info.st_mode & 0o022)
                  and (stat.S_ISDIR(info.st_mode) or stat.S_ISREG(info.st_mode)
                       or (path == ROOT / "profile" and stat.S_ISLNK(info.st_mode))),
                  "foreign owner, writable path or unexpected special file")
    auth = (ROOT / "codex/auth.json").lstat()
    h.require(stat.S_ISREG(auth.st_mode) and stat.S_IMODE(auth.st_mode) == 0o600, "retained auth is not private")
    top = set("app-server.log bin codex codex-version.stderr.log config.json creation-warmup-ready.json events "
              "history history.json portal.log preset.json processes.json profile profile-token.stderr.log r "
              "register.stderr.log registry.json result.json seed-app-server.stderr.log seed-process.json "
              "seeded-continuation skills started-continuation state team-preset.stderr.log tmux-pid.stderr.log "
              "tmux-start.stderr.log workspace xdg-cache xdg-config xdg-state".split())
    receipt_id = h.read(ROOT / "creation-warmup-ready.json")["firstAttempt"]["receiptId"]
    layouts = {".": top, "events": {SLUG + ".jsonl"}, "workspace/work": {SLUG},
               "workspace/worktrees": {".locks", SLUG}, f"workspace/worktrees/{SLUG}": set(),
               "workspace/worktrees/.locks": {SLUG + ".creation.json"},
               "r": {"bench"}, "r/bench": {"authority", "app-server.sock", "portal.sock", "tmux.sock",
                   "registration.json", "registration-inventory.json"},
               "r/bench/authority": {SLUG + suffix for suffix in (".creation.lock", ".json", ".lock")},
               "state": {"transition.lock", "portal", "codex-teams"}, "state/codex-teams": {NAMESPACE},
               f"state/codex-teams/{NAMESPACE}": {SLUG + suffix for suffix in (".json", ".lock", ".operation.lock")},
               "state/portal": {NAMESPACE}, f"state/portal/{NAMESPACE}/creations":
                   {SLUG + ".json", f"{SLUG}.{receipt_id}.complete.json", f"{SLUG}.{receipt_id}.complete.json.request"}}
    for name in ("workspace/archive", "workspace/repos", "skills"):
        layouts[name] = set()
    for name, children in layouts.items():
        h.require({p.name for p in (ROOT / name).iterdir()} == children, "unexpected session, runtime or continuation state")
    for name in ("workspace/worktrees/.locks", f"workspace/worktrees/{SLUG}"):
        info = (ROOT / name).lstat()
        h.require(stat.S_ISDIR(info.st_mode) and stat.S_IMODE(info.st_mode) == 0o700,
                  "retained warm-up worktree directory changed")
    journal = (ROOT / CREATION_JOURNAL).lstat()
    h.require(stat.S_ISREG(journal.st_mode) and stat.S_IMODE(journal.st_mode) == 0o600 and journal.st_size == 4163,
              "retained warm-up creation journal changed")
    h.require({str(p.relative_to(ROOT / "started-continuation")) for p in (ROOT / "started-continuation").rglob("*")
               if p.is_file()} == set(prior), "original continuation evidence changed")
    warmup = completed_warmup(config, preset)
    history = h.read(ROOT / "history.json")
    team_ids = {ROOT_ID, *warmup["memberThreadIDs"].values()}
    rollouts = list((ROOT / "codex/sessions").rglob("*.jsonl"))
    seeds = [p for p in rollouts if not any(p.name.endswith(t + ".jsonl") for t in team_ids)]
    h.require(len(team_ids) == 4 and len(rollouts) == 3383 and len(seeds) == 3379
              and previous["history"] == history and history["activeRollouts"] == 3379
              and history["paddingBytesPerThread"] == 16384 and history["archivedRollouts"] == 0
              and sum(p.stat().st_size for p in seeds) == history["bytes"] == 208256155
              and not (ROOT / "codex/archived_sessions").exists(), "retained seed history changed")
    h.require(len({h.validate_seeded_rollout(p, ROOT) for p in seeds}) == 3379, "seed identities changed")
    return previous, config, preset, warmup, proof, original, alias, native, records


def preserve_warmup_failure(records):
    CLAIM.mkdir(mode=0o700)
    sources = [(name, ROOT / name) for name in records]
    sources += [("warmup-host-proof.json", PROOF), ("host-process-proof.json", d.PROOF),
                ("host-socket-alias-proof.json", d.ALIAS_PROOF)]
    for name, source in sources:
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
    previous, config, preset, warmup, proof, original, alias, native, records = validate_warmup_fixture()
    require_records(records)
    require_retained_services(proof, original, alias, native)
    preserve_warmup_failure(records)
    result = {"state": "running", "candidate": str(PACKAGE), "startedAt": h.stamp(), "results": [],
              "history": previous["history"], "codexVersion": previous["codexVersion"], "warmup": warmup,
              "resumedFrom": "warmup-continuation/result.json"}
    args = SimpleNamespace(model_timeout=180, history_count=3379, history_padding_bytes=16384, skip_faults=False)
    try:
        h.save(ROOT / "result.json", result)
        return h.finish_creation_samples(config, preset, result, args)
    except Exception as error:
        result.update(state="incomplete", finishedAt=h.stamp(),
                      error=str(error) if isinstance(error, h.Failure) else type(error).__name__)
        h.save(ROOT / "result.json", result)
        print("After-warm-up continuation incomplete; all evidence and processes retained.", flush=True)
        return 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as error:
        reason = str(error) if isinstance(error, h.Failure) else type(error).__name__
        print(f"After-warm-up continuation failed: {reason}; evidence retained. Do not retry.", file=sys.stderr)
        sys.exit(1)
